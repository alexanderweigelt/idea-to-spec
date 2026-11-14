# FR-USE-01 – Übersprungener Schritt wird erkannt
Owner: REQUIREMENTS.md · Group: USE · Status: confirmed
## Statement
Wenn ein Schritt übersprungen wurde, muss der nächste Prompt das merken und sagen, was fehlt.
## Rationale
source: user
## Acceptance criteria
### AC-USE-01
```gherkin
Given ein übersprungener Schritt
When der nächste Prompt startet
Then sagt er, welches Dokument oder welcher Schritt fehlt.
```
## Failure cases in real use
- keine benannt
## References
[FR-FLOW-03](FR-FLOW-03.md)
