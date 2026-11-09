# FR-QUALITY-01 – Erkennungsvorschlag innerhalb von 5 Sekunden
Owner: REQUIREMENTS.md · Group: QUALITY · Status: confirmed

## Statement
Das System zeigt den Vorschlag für Betrag und Datum innerhalb von 5 Sekunden nach dem Hochladen des Fotos, bei normaler Mobilfunkverbindung.

## Rationale
Mitglieder warten nicht auf langsame Erkennung. Quelle: user (Annahme A5, bestätigt).

## Acceptance criteria
### AC-QUALITY-01
```gherkin
Given Anna hat eine normale Mobilfunkverbindung
When Anna ein Belegfoto hochlädt
Then erscheint der Vorschlag in höchstens 5 Sekunden
```

## Failure cases in real use
- Der Erkennungsdienst antwortet langsam → [OQ-RECOGNITION-01](REQUIREMENTS.md#oq-recognition-01)

## References
[OQ-RECOGNITION-01](REQUIREMENTS.md#oq-recognition-01)
