# FR-PLATFORM-03 – Deutsche Oberfläche, Beträge in Euro
Owner: REQUIREMENTS.md · Group: PLATFORM · Status: confirmed
## Statement
Die App muss alle Texte auf Deutsch anzeigen und Beträge in Euro darstellen.
## Rationale
Der Verein ist deutsch. Quelle: user (OQ-GOAL-02, ASSUME-06).
## Acceptance criteria
### AC-PLATFORM-03
```gherkin
Given das Mitglied öffnet die App
When es einen Beleg mit einem Betrag ansieht
Then sind alle Texte auf Deutsch und der Betrag endet mit „€“
```
## Failure cases in real use
- Erkennung liefert Betrag mit Punkt statt Komma → [AC-CAPTURE-01](../../docs/requirements/FR-CAPTURE-01.md#ac-capture-01)
## References
[OQ-GOAL-02](../../REQUIREMENTS.md#oq-goal-02)
