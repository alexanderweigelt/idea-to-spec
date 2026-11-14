#!/usr/bin/env python3
"""Stage 2: one prompt + one scenario + simulated user, automatic, with a hard cost limit.

Usage:
  python tests/run.py SCENARIO --dry-run          # cost estimate only, no API call
  python tests/run.py SCENARIO                    # smoke test with the small model from config.json
  python tests/run.py SCENARIO --model claude-opus-5-5 [--runs 3] [--force]

Only this script talks to the models. Each "session" is just a message list held here;
no sandbox, no agent, no tools. The tested model gets no system prompt and, as first
message, the copy block from lib/ with the scenario's INPUT – nothing else.
Results: tests/runs/<date>-<model>[-n]/<scenario>-<n>/ and summary.md.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harness.common import ROOT, TESTS, load_config, copy_block  # noqa: E402
from harness.budget import Budget, BudgetExceeded  # noqa: E402
from harness.dialog import LeakGuard, check_dialog, mentions  # noqa: E402
from harness.outputs import extract_files, check_outputs  # noqa: E402
import static_check  # noqa: E402

PERSONA_RULES = """Du spielst in einem Gespräch einen Menschen, der mit einer KI über seine Projektidee spricht. Deine Rolle steht unten.
Regeln:
- Antworte kurz (1 bis 4 Sätze), natürlich und auf Deutsch.
- Beantworte nur, was gefragt wird. Nutze die Fakten deiner Rolle. Steht etwas nicht in deiner Rolle, sag „Weiß ich nicht“ oder nimm die Empfehlung der KI.
- Bietet die KI nummerierte Möglichkeiten an, antworte mit der Nummer (meist der empfohlenen) oder kurz mit eigenen Worten, wenn deine Rolle etwas anderes sagt.
- Äußere nie eigene Bedenken, bewerte keine Technik, frage nie, ob etwas ein Problem ist.
- Legt die KI Annahmen zur Bestätigung vor, bestätige sie, außer sie widersprechen deiner Rolle.
- Fragt die KI, ob sie die Ergebnisse oder Dateien ausgeben soll, sag ja.
- Sag nie, dass du eine Rolle spielst oder dass dies ein Test ist.

## Deine Rolle
"""


def fill_input(block, values):
    lines = block.splitlines()
    for key, val in values.items():
        idx = [i for i, l in enumerate(lines) if re.match(re.escape(key) + r"(\s*\(.*\))?:\s*$", l)]
        if len(idx) != 1:
            raise ValueError(f"INPUT-Feld {key!r} nicht eindeutig im Kopierblock gefunden")
        lines[idx[0]] = lines[idx[0]] + " " + val
    return "\n".join(lines)


def parse_traps(expected_md):
    traps, current = {}, None
    for line in expected_md.splitlines():
        m = re.match(r"## (T\d+)\b", line)
        if m:
            current = m.group(1)
        m = re.match(r"Warnwörter:\s*(.+)", line)
        if m and current:
            traps[current] = [w.strip() for w in m.group(1).split(",") if w.strip()]
    if not traps:
        raise ValueError("expected.md: keine Fallen mit Warnwörtern gefunden")
    return traps


def load_scenario(name):
    d = TESTS / "scenarios" / name
    sc = json.loads((d / "scenario.json").read_text(encoding="utf-8"))
    persona = (d / "persona.md").read_text(encoding="utf-8")
    expected = (d / "expected.md").read_text(encoding="utf-8")
    return d, sc, persona, expected


def conversation(chat, cfg, models, first_message, persona, guard, budget):
    tested_msgs = [{"role": "user", "content": first_message}]
    user_msgs = []
    transcript, status = [], "max_rounds"
    for rnd in range(1, cfg["max_rounds"] + 1):
        budget.guard(models["tested"], sum(len(json.dumps(m["content"])) for m in tested_msgs), cfg["max_tokens"]["tested"])
        r = chat.send(models["tested"], tested_msgs, max_tokens=cfg["max_tokens"]["tested"], effort=cfg["effort"]["tested"])
        budget.book("tested", models["tested"], r.usage)
        tested_msgs.append({"role": "assistant", "content": r.content})
        files = extract_files(r.text)
        final = any(p.endswith("REQUIREMENTS.md") for p in files)
        transcript.append({"round": rnd, "role": "ai", "text": r.text, "final": final,
                           "model": r.model, "stop_reason": r.stop_reason, "usage": r.usage})
        guard.ai_said(r.text)
        if r.stop_reason == "refusal":
            return transcript, "refusal"
        if final:
            return transcript, "truncated" if r.stop_reason == "max_tokens" else "final"
        if rnd == cfg["max_rounds"]:
            break
        user_msgs.append({"role": "user", "content": r.text})
        budget.guard(models["user"], len(persona) + sum(len(json.dumps(m["content"])) for m in user_msgs), cfg["max_tokens"]["user"])
        u = chat.send(models["user"], user_msgs, system=persona, max_tokens=cfg["max_tokens"]["user"], effort=cfg["effort"]["user"])
        budget.book("user", models["user"], u.usage)
        user_msgs.append({"role": "assistant", "content": u.content})
        transcript.append({"round": rnd, "role": "user", "text": u.text, "model": u.model, "usage": u.usage})
        leak = guard.user_said(u.text)
        if leak:
            transcript[-1]["leak"] = leak
            return transcript, "contaminated"
        tested_msgs.append({"role": "user", "content": u.text})
    return transcript, status


def evaluate(judge_out, script_checks, status, traps):
    trap_res = {}
    for t in judge_out.get("traps", []):
        ok = t["raised_round"] > 0 and (t["fixed_round"] == 0 or t["raised_round"] <= t["fixed_round"])
        trap_res[t["id"]] = ok
    for t in traps:
        trap_res.setdefault(t, False)
    crit_ok = all(c["passed"] for c in judge_out.get("criteria", [])) and "error" not in judge_out
    script_ok = not any(c["status"] == "fail" for c in script_checks)
    passed = status == "final" and script_ok and crit_ok and all(trap_res.values())
    return {"passed": passed, "status": status, "script_ok": script_ok, "criteria_ok": crit_ok, "traps": trap_res}


def estimate(cfg, models, first_message, persona):
    """Rough cost per run from text length (chars/3.5 tokens) and typical turn sizes; no API call."""
    budget = Budget(cfg["prices_usd_per_mtok"], 1e9, 1e9)
    base = len(first_message) / 3.5
    # Calibrated on the first Opus run (2026-11-09): about 3500 output tokens per turn incl. thinking.
    rounds, ai_turn, user_turn, final_out = 8, 3500, 80, 30000
    tested = user = 0.0
    ctx = base
    for rnd in range(1, rounds + 1):
        out = final_out if rnd == rounds else ai_turn
        tested += budget.cost(models["tested"], {"cache_read": max(ctx - user_turn, 0), "cache_write": user_turn if rnd > 1 else base, "output": out})
        ctx += out + user_turn
        if rnd < rounds:
            u_ctx = len(persona) / 3.5 + rnd * (ai_turn + user_turn)
            user += budget.cost(models["user"], {"cache_read": u_ctx - ai_turn, "cache_write": ai_turn, "output": user_turn + 300})
    judge_in = rounds * (ai_turn + user_turn) + final_out + 3000
    judge = budget.cost(models["judge"], {"input": judge_in, "output": 3000})
    worst = budget.cost(models["tested"], {"input": base * 1.25 + cfg["max_rounds"] * (ai_turn + user_turn), "output": cfg["max_rounds"] * ai_turn + cfg["max_tokens"]["tested"]})
    return {"tested": tested, "user": user, "judge": judge, "per_run": tested + user + judge,
            "rounds_assumed": rounds, "tested_worst_case_one_run": worst}


def fingerprint(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(p.encode("utf-8") if isinstance(p, str) else p)
    for f in sorted((TESTS / "harness").glob("*.py")) + [TESTS / "run.py"]:
        h.update(f.read_bytes())
    return h.hexdigest()[:16]


def new_test_dir(model):
    base = TESTS / "runs" / f"{dt.date.today().isoformat()}-{model}"
    d, n = base, 2
    while d.exists():
        d = Path(f"{base}-{n}")
        n += 1
    d.mkdir(parents=True)
    return d


def write_summary(test_dir, meta, results, budget):
    L = [f"# Testlauf {test_dir.name}", "",
         f"- Szenario: `{meta['scenario']}` · Prompt: `{meta['prompt']}`",
         f"- Modelle: getestet `{meta['models_reported'].get('tested', meta['models']['tested'])}`, "
         f"Nutzer `{meta['models']['user']}`, Richter `{meta['models']['judge']}`",
         f"- Automatischer Lauf: ja · Datum: {meta['date']} · Fingerabdruck: `{meta['hash']}`",
         f"- Kosten gesamt: **{budget.total:.3f} USD** (Grenzen: {meta['limits']['per_run']} je Lauf, {meta['limits']['per_test']} je Testlauf)",
         f"- Bestanden: **{sum(r['eval']['passed'] for r in results)} von {len(results)}** Läufen", "",
         "| Lauf | Ende | Runden | Skript | Kriterien | Fallen (angesprochen/festgeschrieben) | Kosten USD |",
         "|---|---|---|---|---|---|---|"]
    for r in results:
        traps = ", ".join(f"{t['id']} {t['raised_round']}/{t['fixed_round']} {'✓' if r['eval']['traps'].get(t['id']) else '✗'}"
                          for t in r["verdict"].get("traps", [])) or "–"
        L.append(f"| {r['name']} | {r['eval']['status']} | {r['rounds']} | {'✓' if r['eval']['script_ok'] else '✗'} | "
                 f"{sum(c['passed'] for c in r['verdict'].get('criteria', []))}/{len(r['verdict'].get('criteria', []))} | {traps} | {r['usd']:.3f} |")
    L += ["", "## Nicht erfüllt (mit Beleg)"]
    for r in results:
        for c in r["checks"]:
            if c["status"] != "pass":
                L.append(f"- {r['name']} · {c['status']} · {c['ac']} · {c['detail']}")
        for c in r["verdict"].get("criteria", []):
            if not c["passed"]:
                L.append(f"- {r['name']} · Richter · {c['id']} · Runde {c['round']}: „{c['quote'][:200]}“")
        if r["verdict"].get("error"):
            L.append(f"- {r['name']} · Richter-Fehler: {r['verdict']['error']}")
        if r["verdict"].get("notes"):
            L.append(f"- {r['name']} · Notiz Richter: {r['verdict']['notes']}")
    L += ["", "## Token je Rolle", "", "| Rolle | Modell | Aufrufe | Input | Cache-Schreiben | Cache-Lesen | Output | USD |", "|---|---|---|---|---|---|---|---|"]
    for role, u in budget.by_role.items():
        L.append(f"| {role} | {u['model']} | {u['calls']} | {u['input']} | {u['cache_write']} | {u['cache_read']} | {u['output']} | {u['usd']:.3f} |")
    if meta.get("stopped"):
        L += ["", f"**Abgebrochen:** {meta['stopped']}"]
    L += ["", "Stichproben: `transcript.jsonl` und `outputs/` je Lauf. Bewertung durch einen Menschen."]
    (test_dir / "summary.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario")
    ap.add_argument("--model", help="getestetes Modell (Standard: config.json models.tested)")
    ap.add_argument("--runs", type=int)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="auch bei gleichem Fingerabdruck neu laufen")
    a = ap.parse_args()
    cfg = load_config()
    models = dict(cfg["models"])
    if a.model:
        models["tested"] = a.model
    runs = a.runs or cfg["runs"]

    # Gate: stage 1 must pass before anything costs money.
    fails = [r for r in static_check.run(cfg) if r["status"] == "fail"]
    if fails:
        sys.exit(f"Stufe 1 fehlgeschlagen ({len(fails)} Fehler) – kein bezahlter Lauf. Erst `python tests/static_check.py` beheben.")

    sc_dir, sc, persona, expected = load_scenario(a.scenario)
    traps = parse_traps(expected)
    leak = mentions(persona + json.dumps(sc["input"], ensure_ascii=False), [w for ws in traps.values() for w in ws])
    if leak:
        sys.exit(f"Leck: persona.md oder INPUT enthält Warnwörter {leak} – Falle wäre verraten. Abbruch.")
    first = fill_input(copy_block(ROOT / sc["prompt"]), sc["input"])
    persona_sys = PERSONA_RULES + persona

    if a.dry_run:
        e = estimate(cfg, models, first, persona_sys)
        print(f"Kostenschätzung je Lauf (Annahme {e['rounds_assumed']} Runden): getestet {e['tested']:.3f} USD "
              f"({models['tested']}), Nutzer {e['user']:.4f} ({models['user']}), Richter {e['judge']:.4f} ({models['judge']}) "
              f"= {e['per_run']:.3f} USD; {runs} Läufe ≈ {e['per_run'] * runs:.2f} USD.")
        print(f"Ungünstigster Fall getestetes Modell je Lauf ≈ {e['tested_worst_case_one_run']:.2f} USD; "
              f"harte Grenzen: {cfg['limits_usd']['per_run']} USD je Lauf, {cfg['limits_usd']['per_test']} USD je Testlauf.")
        return

    fp = fingerprint(first, persona_sys, expected, json.dumps(sc, sort_keys=True), json.dumps(models, sort_keys=True))
    index_file = TESTS / "runs" / "index.json"
    index = json.loads(index_file.read_text()) if index_file.exists() else {}
    if fp in index and not a.force:
        print(f"Unverändert seit {index[fp]} (gleicher Fingerabdruck {fp}) – kein neuer Lauf. Mit --force trotzdem laufen.")
        return

    from harness.llm import connect
    from harness.judge import judge
    chat = connect(cfg["provider"])
    budget = Budget(cfg["prices_usd_per_mtok"], cfg["limits_usd"]["per_run"], cfg["limits_usd"]["per_test"])
    test_dir = new_test_dir(models["tested"])
    meta = {"scenario": a.scenario, "prompt": sc["prompt"], "models": models, "models_reported": {},
            "date": dt.datetime.now().isoformat(timespec="seconds"), "hash": fp, "automatic": True,
            "limits": cfg["limits_usd"]}
    results = []
    try:
        for n in range(1, runs + 1):
            budget.start_run()
            run_dir = test_dir / f"{a.scenario}-{n}"
            (run_dir / "outputs").mkdir(parents=True)
            guard = LeakGuard(traps)
            print(f"Lauf {n}/{runs} …", flush=True)
            try:
                transcript, status = conversation(chat, cfg, models, first, persona_sys, guard, budget)
            except BudgetExceeded as ex:
                meta["stopped"] = str(ex)
                break
            with open(run_dir / "transcript.jsonl", "w", encoding="utf-8") as f:
                f.write(json.dumps({"role": "prompt", "text": first}, ensure_ascii=False) + "\n")
                for t in transcript:
                    f.write(json.dumps(t, ensure_ascii=False) + "\n")
            ai_turns = [t for t in transcript if t["role"] == "ai"]
            meta["models_reported"]["tested"] = ai_turns[0]["model"] if ai_turns else models["tested"]
            files = extract_files(ai_turns[-1]["text"]) if ai_turns and ai_turns[-1].get("final") else {}
            for p, c in files.items():
                out = run_dir / "outputs" / p
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(c + "\n", encoding="utf-8")
            checks = check_dialog([t["text"] for t in ai_turns if not t.get("final")], status)
            if status in ("final", "truncated"):
                checks += check_outputs(files)
            (run_dir / "checks.json").write_text(json.dumps(checks, indent=1, ensure_ascii=False), encoding="utf-8")
            verdict = {}
            if status != "contaminated":
                outputs_text = "\n\n".join(f"#### {p}\n{c}" for p, c in files.items())
                try:
                    verdict, jm = judge(chat, models["judge"], cfg["max_tokens"]["judge"], cfg["effort"]["judge"],
                                        expected, sc["judge_acs"], transcript, outputs_text, budget)
                    meta["models_reported"]["judge"] = jm
                except BudgetExceeded as ex:
                    meta["stopped"] = str(ex)
                    verdict = {"error": "Kostengrenze vor dem Richter erreicht"}
            (run_dir / "verdict.json").write_text(json.dumps(verdict, indent=1, ensure_ascii=False), encoding="utf-8")
            ev = evaluate(verdict, checks, status, traps)
            usage = {"automatic": True, "models": models, "reported": meta["models_reported"],
                     "roles": budget.run_roles, "usd": round(budget.run, 4)}
            (run_dir / "usage.json").write_text(json.dumps(usage, indent=1, ensure_ascii=False), encoding="utf-8")
            results.append({"name": run_dir.name, "eval": ev, "verdict": verdict, "checks": checks,
                            "rounds": len(ai_turns), "usd": budget.run})
            print(f"  Ende: {status}, bestanden: {ev['passed']}, {budget.run:.3f} USD", flush=True)
            if meta.get("stopped"):
                break
            same = [r for r in results if (r["eval"]["passed"], r["eval"]["traps"]) == (ev["passed"], ev["traps"])]
            if len(same) >= cfg["stop_after_equal"] and len(results) < runs:
                meta["early_stop"] = f"nach {len(results)} Läufen {len(same)} gleiche Ergebnisse"
                break
    finally:
        (test_dir / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding="utf-8")
        write_summary(test_dir, meta, results, budget)
        if results and not meta.get("stopped"):
            index[fp] = test_dir.name
            index_file.write_text(json.dumps(index, indent=1))
    print(f"Fertig: {test_dir.relative_to(ROOT)}/summary.md · {budget.total:.3f} USD")


if __name__ == "__main__":
    main()
