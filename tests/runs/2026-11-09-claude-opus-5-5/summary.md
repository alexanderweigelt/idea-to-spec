# Testlauf 2026-11-09-claude-opus-5-5

- Szenario: `requirements-vereinskasse` · Prompt: `lib/requirements.md`
- Modelle: getestet `claude-opus-5-5`, Nutzer `claude-haiku-5-5`, Richter `claude-haiku-5-5`
- Automatischer Lauf: ja · Datum: 2026-11-09T13:06:54 · Fingerabdruck: `a2bf50d8a582a4f8`
- Kosten gesamt: **1.108 USD** (Grenzen: 2.0 je Lauf, 10.0 je Testlauf)
- Bestanden: **0 von 1** Läufen

| Lauf | Ende | Runden | Skript | Kriterien | Fallen (angesprochen/festgeschrieben) | Kosten USD |
|---|---|---|---|---|---|---|
| requirements-vereinskasse-1 | truncated | 7 | ✗ | 10/10 | T1 1/2 ✓, T2 1/2 ✓ | 1.108 |

## Nicht erfüllt (mit Beleg)
- requirements-vereinskasse-1 · warn · AC-DIALOG-09 · Runden mit mehr als 3 Empfehlungen: [1]
- requirements-vereinskasse-1 · warn · AC-DIALOG-19 · Runden ohne nummerierte Themenliste vor der ersten Frage: [3]
- requirements-vereinskasse-1 · fail · AC-SPEC-12 · keine Datei docs/requirements/<ID>.md
- requirements-vereinskasse-1 · Notiz Richter: Beide Fallen (PWA im App Store, Datenschutz bei Google Cloud Vision) hat die KI bereits in Runde 1 von sich aus und vor dem Festschreiben angesprochen. Der Verlauf endet abgeschnitten mitten in der Liste der Annahmen (OQ-QUALITY-05) in Runde 7, daher ist die Vollständigkeit des Ergebnisdokuments nicht prüfbar.

## Token je Rolle

| Rolle | Modell | Aufrufe | Input | Cache-Schreiben | Cache-Lesen | Output | USD |
|---|---|---|---|---|---|---|---|
| tested | claude-opus-5-5 | 7 | 28 | 27349 | 86334 | 47181 | 1.098 |
| user | claude-haiku-5-5 | 6 | 24 | 15407 | 42080 | 1227 | 0.003 |
| judge | claude-haiku-5-5 | 1 | 4 | 29281 | 0 | 6464 | 0.007 |

Stichproben: `transcript.jsonl` und `outputs/` je Lauf. Bewertung durch einen Menschen.
