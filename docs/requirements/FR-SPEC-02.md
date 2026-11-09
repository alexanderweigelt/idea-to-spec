# FR-SPEC-02 – Wann die Spezifikation fertig ist
Owner: REQUIREMENTS.md · Group: SPEC · Status: confirmed
## Statement
Die Spezifikation darf erst als fertig gelten, wenn die Liste nach [FR-SPEC-01](FR-SPEC-01.md) leer ist oder jeder Punkt bewusst akzeptiert wurde, kein Katalogeintrag auf „Entwurf“ steht und ein Mensch sie freigegeben hat.
## Rationale
source: user
## Acceptance criteria
### AC-SPEC-03
```gherkin
Given ein Punkt der Liste, der weder erledigt noch bewusst akzeptiert ist
When man den Stand prüft
Then gilt die Spezifikation nicht als fertig.
```
### AC-SPEC-04
```gherkin
Given ein Katalogeintrag auf „Entwurf“
When man den Stand prüft
Then gilt die Spezifikation nicht als fertig.
```
### AC-SPEC-05
```gherkin
Given keine menschliche Freigabe
When man den Stand prüft
Then gilt die Spezifikation nicht als fertig.
```
## Failure cases in real use
- keine benannt
## References
[FR-SPEC-01](FR-SPEC-01.md), [OQ-SPEC-02](../../REQUIREMENTS.md#oq-spec-02)
