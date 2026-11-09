# FR-REVIEW-01 – Status der Einreichung
Owner: REQUIREMENTS.md · Group: REVIEW · Status: confirmed
## Statement
Die App muss dem Mitglied für jede Einreichung den Status „eingereicht“ oder „erstattet“ anzeigen.
## Rationale
Das Mitglied soll wissen, wann es sein Geld bekommt. Quelle: user (OQ-REVIEW-01, ASSUME-04).
## Acceptance criteria
### AC-REVIEW-01
```gherkin
Given das Mitglied hat einen Beleg eingereicht
When der Kassenwart den Beleg erstattet hat
Then zeigt die App dem Mitglied für diesen Beleg den Status „erstattet“
```
## Failure cases in real use
- Status wird nicht aktualisiert, wenn das Mitglied offline ist → [AC-REVIEW-01](#ac-review-01)
## References
[OQ-REVIEW-01](../../REQUIREMENTS.md#oq-review-01)
