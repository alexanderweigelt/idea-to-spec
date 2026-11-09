# FR-REVIEW-02 – Keine Änderung nach Einreichung
Owner: REQUIREMENTS.md · Group: REVIEW · Status: confirmed
## Statement
Sobald ein Beleg eingereicht ist, darf das Mitglied ihn nicht mehr ändern.
## Rationale
Nur so lässt sich nachvollziehen, was geprüft wurde. Quelle: user (ASSUME-09).
## Acceptance criteria
### AC-REVIEW-02
```gherkin
Given ein Beleg ist eingereicht
When das Mitglied versucht, den Betrag zu ändern
Then lehnt die App die Änderung ab
```
## Failure cases in real use
- Mitglied möchte einen Fehler korrigieren → [AC-REVIEW-02](#ac-review-02); Korrektur läuft über den Kassenwart
## References
[OQ-ASSUME-09](../../REQUIREMENTS.md#oq-assume-09)
