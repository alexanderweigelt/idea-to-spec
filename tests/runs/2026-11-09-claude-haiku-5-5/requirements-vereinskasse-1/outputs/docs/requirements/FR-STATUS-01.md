# FR-STATUS-01 – Drei Stufen einer Einreichung
Owner: REQUIREMENTS.md · Group: STATUS · Status: confirmed

## Statement
Das System führt jede Einreichung in genau einer der Stufen „eingereicht“, „geprüft“ oder „erstattet“, und nur der Kassenwart darf die Stufen „geprüft“ und „erstattet“ setzen.

## Rationale
Die Stufen bilden den realen Ablauf ab. Quelle: user (Entscheidung Kernablauf, Frage 4).

## Acceptance criteria
### AC-STATUS-01
```gherkin
Given die Einreichung E1 hat die Stufe „eingereicht“
When der Kassenwart die Stufe auf „geprüft“ setzt
Then hat E1 die Stufe „geprüft“
```

## Failure cases in real use
- Der Status wurde falsch gesetzt → [OQ-STATUS-01](REQUIREMENTS.md#oq-status-01)

## References
[OQ-STATUS-01](REQUIREMENTS.md#oq-status-01)
