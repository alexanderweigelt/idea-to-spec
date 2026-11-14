# FR-DIALOG-04 – Delegation „entscheide selbst“
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Wenn der Mensch für ein Thema „entscheide selbst“ sagt, muss die KI nach ihren Empfehlungen mit Quelle „delegated“ entscheiden und Befunde nach [FR-DIALOG-05](FR-DIALOG-05.md) trotzdem vorlegen.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-11
```gherkin
Given „entscheide selbst“ für ein Thema
When die KI darin entscheidet
Then entspricht jede Entscheidung ihrer Empfehlung und trägt die Quelle „delegated“.
```
### AC-DIALOG-12
```gherkin
Given ein delegiertes Thema mit einem Befund nach FR-DIALOG-05
When die KI entscheidet
Then legt sie den Befund dem Menschen vor.
```
## Failure cases in real use
- keine benannt
## References
[FR-DIALOG-05](FR-DIALOG-05.md), [OQ-DIALOG-02](../../REQUIREMENTS.md#oq-dialog-02)
