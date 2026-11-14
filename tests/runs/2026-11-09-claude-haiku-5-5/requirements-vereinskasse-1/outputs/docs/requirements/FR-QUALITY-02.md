# FR-QUALITY-02 – Absenden in höchstens 60 Sekunden
Owner: REQUIREMENTS.md · Group: QUALITY · Status: confirmed

## Statement
Ein Mitglied kann eine Einreichung mit Foto, Betrag und Datum in höchstens 60 Sekunden absenden.

## Rationale
Die Einreichung soll im Alltag schnell gehen. Quelle: user (Annahme A6, bestätigt).

## Acceptance criteria
### AC-QUALITY-02
```gherkin
Given Anna hat ein Belegfoto aufgenommen
When Anna Betrag und Datum bestätigt und die Einreichung absendet
Then ist die Einreichung in höchstens 60 Sekunden abgesendet
```

## Failure cases in real use
- Das Foto ist groß und die Verbindung schwach → [OQ-OFFLINE-01](REQUIREMENTS.md#oq-offline-01)

## References
[OQ-OFFLINE-01](REQUIREMENTS.md#oq-offline-01)
