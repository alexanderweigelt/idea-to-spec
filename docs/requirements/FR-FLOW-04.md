# FR-FLOW-04 – Ein Kopierblock, vorbelegt, anpassbare Stellen markiert
Owner: REQUIREMENTS.md · Group: FLOW · Status: confirmed
## Statement
Jeder Prompt muss sich als ein Block unverändert kopieren und nutzen lassen, mit anerkannten Standards vorbelegt sein und seine anpassbaren Stellen klar markieren.
## Rationale
source: user
## Acceptance criteria
### AC-FLOW-06
```gherkin
Given ein beliebiger Prompt
When man seinen Block unverändert in einen KI-Chat kopiert
Then lässt sich der Schritt ohne Bearbeitung des Blocks durchführen.
```
### AC-FLOW-07
```gherkin
Given ein beliebiger Prompt
When man seine Vorgaben prüft
Then ist jede mit einem anerkannten Standard vorbelegt.
```
### AC-FLOW-08
```gherkin
Given ein beliebiger Prompt
When man die anpassbaren Stellen sucht
Then sind sie klar markiert.
```
## Failure cases in real use
- keine benannt
## References
[OQ-FLOW-01](../../REQUIREMENTS.md#oq-flow-01), [OQ-FLOW-02](../../REQUIREMENTS.md#oq-flow-02)
