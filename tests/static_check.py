#!/usr/bin/env python3
"""Stage 1: static check of all prompts in lib/ – no AI, no cost, deterministic.

Usage: python tests/static_check.py [--json FILE]
Exit code 0 = no failures, 1 = at least one failure (paid runs are blocked).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harness.common import LIB, ID_KINDS, ID_LIKE, load_config, copy_block, check  # noqa: E402


def check_prompt(path, cfg, results):
    name = path.name
    text = path.read_text(encoding="utf-8")
    head = text.split("````text")[0]

    # Header table: role, required, used-if-present, produced, done-when (AC-FLOW-03, AC-FLOW-05)
    missing = [r for r in cfg["header_rows"] if not re.search(r"^\|\s*" + re.escape(r) + r"\s*\|", head, re.M)]
    check(results, f"{name}:header", "AC-FLOW-03 AC-FLOW-05", not missing, f"fehlt: {missing}" if missing else "")

    # Exactly one copy block (AC-FLOW-06)
    try:
        block = copy_block(path)
    except ValueError as e:
        check(results, f"{name}:block", "AC-FLOW-06", False, str(e))
        return
    check(results, f"{name}:block", "AC-FLOW-06", True)
    lines = block.splitlines()

    # Same sections in the same order in every prompt (AC-FLOW-03, AC-FLOW-04)
    pos = []
    for s in cfg["sections"]:
        idx = next((i for i, l in enumerate(lines) if l == s or l.startswith(s + " (")), None)
        pos.append(idx)
    missing = [s for s, p in zip(cfg["sections"], pos) if p is None]
    found = [p for p in pos if p is not None]
    ordered = found == sorted(found)
    check(results, f"{name}:sections", "AC-FLOW-03 AC-FLOW-04", not missing and ordered,
          (f"fehlt: {missing} " if missing else "") + ("" if ordered else "Reihenfolge falsch"))

    def section(title):
        try:
            i = next(i for i, l in enumerate(lines) if l == title or l.startswith(title + " ("))
        except StopIteration:
            return "", ""
        j = next((k for k in range(i + 1, len(lines))
                  if any(lines[k] == s or lines[k].startswith(s + " (") for s in cfg["sections"])), len(lines))
        return lines[i], "\n".join(lines[i + 1:j])

    # Adjustable parts clearly marked (AC-FLOW-08)
    inp_head, _ = section("INPUT")
    def_head, _ = section("DEFAULTS")
    ok = "optional" in inp_head and "edit to deviate" in def_head
    check(results, f"{name}:markers", "AC-FLOW-08", ok, f"INPUT='{inp_head}' DEFAULTS='{def_head}'" if not ok else "")

    # Documents named: required, used if present, produced (AC-FLOW-05)
    _, docs = section("DOCUMENTS")
    missing = [f for f in cfg["documents_fields"] if f not in docs]
    check(results, f"{name}:documents", "AC-FLOW-05", not missing, f"fehlt: {missing}" if missing else "")

    # Result as text without file access (AC-USE-03)
    _, how = section("HOW YOU WORK")
    check(results, f"{name}:no-file-access", "AC-USE-03", "without file access" in how.lower(),
          "kein Hinweis für Chats ohne Dateizugriff")

    # Only allowed ID kinds (AC-REQ-03)
    bad = sorted({m.group(1) for m in ID_LIKE.finditer(block) if m.group(1) not in ID_KINDS + ("KIND",)})
    check(results, f"{name}:id-kinds", "AC-REQ-03", not bad, f"fremde ID-Arten: {bad}" if bad else "")

    # No tool-specific features (AC-USE-02)
    hits = [w for w in cfg["tool_words"] if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", text, re.I)]
    check(results, f"{name}:tool-neutral", "AC-USE-02", not hits, f"werkzeugeigene Begriffe: {hits}" if hits else "")


def check_readme(cfg, prompts, results):
    path = LIB / "README.md"
    if not check(results, "README.md:exists", "AC-FLOW-01", path.exists(), "lib/README.md fehlt"):
        return
    text = path.read_text(encoding="utf-8")
    linked = set(re.findall(r"\]\(([\w-]+\.md)\)", text))
    missing = sorted(p.name for p in prompts if p.name not in linked)
    check(results, "README.md:order-lists-all", "AC-FLOW-01", not missing, f"nicht in der Reihenfolge: {missing}" if missing else "")
    core = re.findall(r"^\|\s*\d+\s*\|\s*\[[^\]]+\]\(", text, re.M)
    check(results, "README.md:core-max", "AC-FLOW-09", len(core) <= cfg["max_core_prompts"], f"{len(core)} Prompts im Kernablauf")


def run(cfg=None):
    cfg = (cfg or load_config())["static"]
    results = []
    prompts = sorted(p for p in LIB.glob("*.md") if p.name != "README.md")
    for p in prompts:
        check_prompt(p, cfg, results)
    check_readme(cfg, prompts, results)
    return results


def main():
    results = run()
    fails = [r for r in results if r["status"] == "fail"]
    for r in results:
        if r["status"] != "pass":
            print(f"{r['status'].upper():5} {r['id']:32} {r['ac']:24} {r['detail']}")
    print(f"Stufe 1: {len(results)} Prüfungen, {len(fails)} Fehler, "
          f"{sum(r['status'] == 'warn' for r in results)} Hinweise")
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(results, indent=1, ensure_ascii=False))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
