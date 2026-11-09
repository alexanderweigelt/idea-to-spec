# FR-FLOW-03 – Dokumentbezüge je Prompt
Owner: REQUIREMENTS.md · Group: FLOW · Status: confirmed
## Statement
Jeder Prompt muss nennen, welche Dokumente er zwingend braucht, welche er nutzt, falls vorhanden, und welches er erzeugt.
## Rationale
source: user
## Acceptance criteria
### AC-FLOW-05
```gherkin
Given ein beliebiger Prompt
When man ihn liest
Then nennt er die zwingend benötigten Dokumente, die genutzten, falls vorhanden, und das erzeugte Dokument.
```
## Failure cases in real use
- Benötigtes Dokument fehlt → [FR-USE-01](FR-USE-01.md)
## References
[FR-USE-01](FR-USE-01.md)
