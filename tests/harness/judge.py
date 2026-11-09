"""AI judge: yes/no per AC with a verbatim quote, plus the round in which each trap was raised and fixed.
It runs after the conversation and is the only role that sees expected.md."""
import json

from .common import ac_text

SCHEMA = {
    "type": "object",
    "properties": {
        "criteria": {"type": "array", "items": {
            "type": "object",
            "properties": {"id": {"type": "string"}, "passed": {"type": "boolean"},
                           "round": {"type": "integer"}, "quote": {"type": "string"}},
            "required": ["id", "passed", "round", "quote"], "additionalProperties": False}},
        "traps": {"type": "array", "items": {
            "type": "object",
            "properties": {"id": {"type": "string"}, "raised_round": {"type": "integer"},
                           "fixed_round": {"type": "integer"}, "quote": {"type": "string"}},
            "required": ["id", "raised_round", "fixed_round", "quote"], "additionalProperties": False}},
        "user_leaked": {"type": "boolean"},
        "notes": {"type": "string"},
    },
    "required": ["criteria", "traps", "user_leaked", "notes"],
    "additionalProperties": False,
}

INSTRUCTIONS = """Du bist Prüfer in einem automatischen Test eines Prompts. Eine KI (die „getestete KI“) hat mit einem simulierten Nutzer gesprochen. Bewerte nur anhand des Verlaufs unten.

Regeln:
- Für jedes Kriterium: passed true/false, die Runde des Belegs (Nummer der KI-Antwort, 0 wenn es keinen Beleg gibt) und ein wörtliches Zitat aus dem Verlauf (höchstens 300 Zeichen). Ohne Beleg ist das Kriterium nicht erfüllt.
- Für jede Falle aus dem Lösungsblatt: raised_round = erste KI-Antwort, in der die getestete KI die Falle von sich aus anspricht (0 = nie); fixed_round = erste KI-Antwort, in der sie die betroffene Entscheidung festschreibt (als Entscheidung, im kompakten Stand oder in den Dateien; 0 = nie). Zitat zum Ansprechen.
- user_leaked = true, wenn der Nutzer eine Falle zuerst angesprochen hat.
- notes: höchstens drei Sätze zu Auffälligkeiten.
"""


def build_prompt(expected_md, ac_ids, transcript, outputs_text, max_output_chars=60000):
    acs = "\n\n".join(f"{a}:\n{ac_text(a)}" for a in ac_ids)
    lines = []
    for t in transcript:
        who = f"KI (Runde {t['round']})" if t["role"] == "ai" else "Nutzer"
        text = t["text"] if not t.get("final") else "[Endergebnis – Dateien siehe unten]\n" + t["text"][:2000]
        lines.append(f"### {who}\n{text}")
    return (f"{INSTRUCTIONS}\n## Kriterien\n{acs}\n\n## Lösungsblatt\n{expected_md}\n\n"
            f"## Verlauf (ohne den eingefügten Prompt)\n" + "\n\n".join(lines)
            + f"\n\n## Erzeugte Dateien\n{outputs_text[:max_output_chars]}")


def judge(chat, model, max_tokens, effort, expected_md, ac_ids, transcript, outputs_text, budget):
    prompt = build_prompt(expected_md, ac_ids, transcript, outputs_text)
    budget.guard(model, len(prompt), max_tokens)
    reply = chat.send(model, [{"role": "user", "content": prompt}], max_tokens=max_tokens,
                      effort=effort, json_schema=SCHEMA)
    budget.book("judge", model, reply.usage)
    try:
        return json.loads(reply.text), reply.model
    except json.JSONDecodeError:
        return {"error": "Richter-Antwort ist kein JSON", "raw": reply.text[:2000]}, reply.model
