# FR-DIALOG-07 – Themenliste je Fragerunde
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Die KI muss jede Fragerunde mit einer kurzen nummerierten Themenliste, nach Wichtigkeit geordnet, beginnen, sie der Reihe nach abarbeiten, neue Themen ans Ende stellen und die Runde beenden, wenn die Liste leer ist.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-19
```gherkin
Given der Beginn einer Fragerunde
When die KI antwortet
Then steht am Anfang eine kurze nummerierte Themenliste nach Wichtigkeit.
```
### AC-DIALOG-20
```gherkin
Given eine laufende Runde
When ein neues Thema auftaucht
Then kommt es ans Ende der Liste.
```
### AC-DIALOG-21
```gherkin
Given eine laufende Runde
When man prüft, wann sie endet
Then endet sie erst, wenn die Liste leer ist.
```
## Failure cases in real use
- Weitermachen in neuem Chat → [OQ-DIALOG-04](../../REQUIREMENTS.md#oq-dialog-04)
## References
[OQ-DIALOG-04](../../REQUIREMENTS.md#oq-dialog-04)
