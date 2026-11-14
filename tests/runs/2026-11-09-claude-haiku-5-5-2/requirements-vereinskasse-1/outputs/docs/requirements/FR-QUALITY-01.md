# FR-QUALITY-01 – Erkennung in höchstens 10 Sekunden
Owner: REQUIREMENTS.md · Group: QUALITY · Status: confirmed
## Statement
Bei guter Verbindung muss die App den Vorschlag für Betrag und Datum innerhalb von 10 Sekunden nach der Aufnahme des Fotos anzeigen.
## Rationale
Das Mitglied wartet nicht unnötig. Quelle: user (OQ-QUALITY-01).
## Acceptance criteria
### AC-QUALITY-01
```gherkin
Given eine gute Verbindung besteht
When das Mitglied ein Foto aufgenommen hat
Then erscheint der Vorschlag für Betrag und Datum spätestens nach 10 Sekunden
```
## Failure cases in real use
- Cloud-Dienst antwortet langsam → [AC-QUALITY-01](#ac-quality-01)
- Schlechte Verbindung → [OQ-CONNECT-01](../../REQUIREMENTS.md#oq-connect-01)
## References
[OQ-QUALITY-01](../../REQUIREMENTS.md#oq-quality-01)
