# FR-DIALOG-05 – Fachprüfung vor dem Festschreiben
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Bevor ein Prompt einen Wunsch oder eine Entscheidung festschreibt, muss er sie in seinem Fach prüfen (machbar, Kosten, Störfälle in echter Nutzung, Widerspruch zu Plattform, Recht, Regeln Dritter oder anderen Anforderungen, einfacherer Weg) und nur Befunde melden, die Umfang, Kosten oder Machbarkeit spürbar ändern, die wichtigsten zuerst und mit Empfehlung.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-13
```gherkin
Given ein Wunsch mit Widerspruch zu Plattform, Recht, Regeln Dritter oder einer anderen Anforderung
When der zuständige Prompt ihn bearbeitet
Then meldet er den Widerspruch ungefragt, bevor er festschreibt.
```
### AC-DIALOG-14
```gherkin
Given ein Wunsch mit Störfällen in echter Nutzung, die Umfang, Kosten oder Machbarkeit spürbar ändern
When der zuständige Prompt ihn bearbeitet
Then meldet er sie ungefragt.
```
### AC-DIALOG-15
```gherkin
Given ein Wunsch mit einem einfacheren Weg
When der zuständige Prompt ihn bearbeitet
Then nennt er den einfacheren Weg.
```
### AC-DIALOG-16
```gherkin
Given mehrere Befunde
When der Prompt sie meldet
Then sind es nur spürbare, die wichtigsten zuerst, jeder mit Empfehlung.
```
## Failure cases in real use
- Grenze der Plattform → [AC-DIALOG-13](#ac-dialog-13)
- rechtliche Folge → [AC-DIALOG-13](#ac-dialog-13)
- widersprüchliche Wünsche → [AC-DIALOG-13](#ac-dialog-13)
- Sicherheitsfolgen → [OQ-DIALOG-03](../../REQUIREMENTS.md#oq-dialog-03)
## References
[OQ-DIALOG-01](../../REQUIREMENTS.md#oq-dialog-01), [OQ-DIALOG-03](../../REQUIREMENTS.md#oq-dialog-03)
