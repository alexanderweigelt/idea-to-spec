# FR-FLOW-01 – Empfohlene Abfolge, Anforderungen zuerst
Owner: REQUIREMENTS.md · Group: FLOW · Status: confirmed
## Statement
Die Prompt-Library muss eine empfohlene Abfolge der Prompts nennen, in der nur festgelegt ist, dass zuerst die Anforderungen geklärt werden.
## Rationale
source: user
## Acceptance criteria
### AC-FLOW-01
```gherkin
Given die Library
When man ihren Leitfaden liest
Then nennt er eine empfohlene Reihenfolge aller Prompts.
```
### AC-FLOW-02
```gherkin
Given die empfohlene Reihenfolge
When man prüft, was davon verbindlich ist
Then ist nur „zuerst die Anforderungen klären“ als fest bezeichnet und alles andere als Empfehlung.
```
## Failure cases in real use
- Schritt übersprungen → [FR-USE-01](FR-USE-01.md)
## References
[FR-USE-01](FR-USE-01.md)
