# Testlauf 2026-11-09-claude-haiku-5-5-2

- Szenario: `requirements-vereinskasse` · Prompt: `lib/requirements.md`
- Modelle: getestet `claude-haiku-5-5`, Nutzer `claude-haiku-5-5`, Richter `claude-haiku-5-5`
- Automatischer Lauf: ja · Datum: 2026-11-09T12:46:04 · Fingerabdruck: `1b914a4e2d51aada`
- Kosten gesamt: **0.036 USD** (Grenzen: 2.0 je Lauf, 10.0 je Testlauf)
- Bestanden: **0 von 1** Läufen

| Lauf | Ende | Runden | Skript | Kriterien | Fallen (angesprochen/festgeschrieben) | Kosten USD |
|---|---|---|---|---|---|---|
| requirements-vereinskasse-1 | final | 11 | ✗ | 8/10 | T1 1/2 ✓, T2 1/11 ✓ | 0.036 |

## Nicht erfüllt (mit Beleg)
- requirements-vereinskasse-1 · warn · AC-DIALOG-07 · Fragerunden ohne markierte Empfehlung: [10]
- requirements-vereinskasse-1 · warn · AC-DIALOG-19 · Runden ohne nummerierte Themenliste vor der ersten Frage: [1, 2, 3, 4, 10]
- requirements-vereinskasse-1 · fail · AC-SPEC-09 · IDs ohne Link oder mit Zusatztext: {'REQUIREMENTS.md': ['OQ-LEGAL-01', 'OQ-PLATFORM-01'], 'FR-CAPTURE-01.md': ['OQ-CAPTURE-01'], 'FR-CAPTURE-02.md': ['OQ-CAPTURE-01'], 'FR-PHOTO-01.md': ['OQ-ASSUME-08', 'OQ-PHOTO-01'], 'FR-CONNECT-01.md': ['OQ-CONNECT-01'], 'FR-QUALITY-01.md': ['OQ-QUALITY-01'], 'FR-REVIEW-01.md': ['OQ-REVIEW-01'], 'FR-ROLES-01.md': ['OQ-ROLES-01'], 'FR-RETENTION-01.md': ['OQ-LEGAL-02', 'OQ-RETENTION-01'], 'FR-PLATFORM-01.md': ['OQ-PLATFORM-01'], 'FR-PLATFORM-03.md': ['OQ-GOAL-02']}
- requirements-vereinskasse-1 · Richter · AC-DIALOG-02 · Runde 11: „OQ-GOAL-03 – Nutzer? Antwort: Mitglieder und Kassenwart, ein Verein, eine Kasse. Begründung: Annahme ASSUME-03, bestätigt. Datum: (bei Speicherung eintragen). Quelle: user.“
- requirements-vereinskasse-1 · Richter · AC-DIALOG-16 · Runde 1: „Schlechte Verbindung: Fotos sollten lokal gespeichert und später hochgeladen werden können. Das ist eine Anforderung, kein Zusatz.“
- requirements-vereinskasse-1 · Notiz Richter: Die KI nannte in Runde 1 beide Fallen ungefragt, die Plattform-Falle wurde in Runde 2 ausdrücklich als Widerspruch geführt. Die Datenschutz-Falle blieb als offene Frage an den Legal-Prompt, wurde aber in Runde 11 in FR-CAPTURE-01 als „given (Erkennung über Google Cloud Vision)“ festgeschrieben. Die Dokumente enthalten zudem Einträge mit Quelle „user“ (z. B. OQ-GOAL-03), die der Nutzer nie beantwortet hat.

## Token je Rolle

| Rolle | Modell | Aufrufe | Input | Cache-Schreiben | Cache-Lesen | Output | USD |
|---|---|---|---|---|---|---|---|
| tested | claude-haiku-5-5 | 11 | 44 | 19384 | 132448 | 40632 | 0.024 |
| user | claude-haiku-5-5 | 10 | 40 | 13789 | 68461 | 440 | 0.003 |
| judge | claude-haiku-5-5 | 1 | 4 | 27886 | 0 | 10699 | 0.009 |

Stichproben: `transcript.jsonl` und `outputs/` je Lauf. Bewertung durch einen Menschen.
