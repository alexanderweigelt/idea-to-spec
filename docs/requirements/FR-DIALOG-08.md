# FR-DIALOG-08 – Kompakter Stand ohne Dateizugriff
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Wenn die KI keinen Dateizugriff hat, muss sie nach jedem abgeschlossenen Thema einen kompakten Stand ausgeben (Entscheidungen, Annahmen, Rest der Liste).
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-22
```gherkin
Given ein KI-Chat ohne Dateizugriff
When ein Thema abgeschlossen ist
Then gibt die KI einen kompakten Stand mit Entscheidungen, Annahmen und Rest der Liste aus.
```
## Failure cases in real use
- kein Dateizugriff → [AC-DIALOG-22](#ac-dialog-22)
## References
[FR-USE-02](FR-USE-02.md)
