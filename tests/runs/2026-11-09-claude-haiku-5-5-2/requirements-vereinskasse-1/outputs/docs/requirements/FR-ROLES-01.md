# FR-ROLES-01 – Sichtbarkeit der Belege
Owner: REQUIREMENTS.md · Group: ROLES · Status: confirmed
## Statement
Die App muss einem Mitglied nur seine eigenen Belege zeigen und dem Kassenwart alle Belege.
## Rationale
Schutz der Mitgliederdaten, Kassenarbeit bleibt möglich. Quelle: user (OQ-ROLES-01).
## Acceptance criteria
### AC-ROLES-01
```gherkin
Given Mitglied A und Mitglied B haben je einen Beleg eingereicht
When Mitglied A die Belegliste öffnet
Then sieht Mitglied A nur seinen eigenen Beleg
```
### AC-ROLES-02
```gherkin
Given Mitglied A und Mitglied B haben je einen Beleg eingereicht
When der Kassenwart die Belegliste öffnet
Then sieht er beide Belege
```
## Failure cases in real use
- Mitglied versucht, über eine direkte Adresse einen fremden Beleg aufzurufen → [AC-ROLES-01](#ac-roles-01)
## References
[OQ-ROLES-01](../../REQUIREMENTS.md#oq-roles-01)
