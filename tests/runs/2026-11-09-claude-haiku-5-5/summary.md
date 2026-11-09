# Testlauf 2026-11-09-claude-haiku-5-5

- Szenario: `requirements-vereinskasse` · Prompt: `lib/requirements.md`
- Modelle: getestet `claude-haiku-5-5`, Nutzer `claude-haiku-5-5`, Richter `claude-haiku-5-5`
- Automatischer Lauf: ja · Datum: 2026-11-09T12:40:32 · Fingerabdruck: `69cea0930429cd9d`
- Kosten gesamt: **0.028 USD** (Grenzen: 2.0 je Lauf, 10.0 je Testlauf)
- Bestanden: **0 von 1** Läufen

| Lauf | Ende | Runden | Skript | Kriterien | Fallen (angesprochen/festgeschrieben) | Kosten USD |
|---|---|---|---|---|---|---|
| requirements-vereinskasse-1 | final | 9 | ✗ | 0/0 | – | 0.028 |

## Nicht erfüllt (mit Beleg)
- requirements-vereinskasse-1 · warn · AC-DIALOG-19 · Runden ohne nummerierte Themenliste vor der ersten Frage: [2, 3, 5, 6, 7]
- requirements-vereinskasse-1 · fail · OQ-SPEC-07 · README.md mit „IDs lesen“ und „Specification“ fehlt
- requirements-vereinskasse-1 · Richter-Fehler: Richter-Antwort ist kein JSON

## Token je Rolle

| Rolle | Modell | Aufrufe | Input | Cache-Schreiben | Cache-Lesen | Output | USD |
|---|---|---|---|---|---|---|---|
| tested | claude-haiku-5-5 | 9 | 36 | 17089 | 82220 | 36037 | 0.021 |
| user | claude-haiku-5-5 | 8 | 32 | 9195 | 38776 | 107 | 0.002 |
| judge | claude-haiku-5-5 | 1 | 4 | 21145 | 0 | 6000 | 0.006 |

Stichproben: `transcript.jsonl` und `outputs/` je Lauf. Bewertung durch einen Menschen.
