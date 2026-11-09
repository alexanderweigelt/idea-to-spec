# FR-USE-02 – Funktioniert in jedem KI-Chat
Owner: REQUIREMENTS.md · Group: USE · Status: confirmed
## Statement
Die Prompt-Library muss in jedem KI-Chat ohne Sonderfunktionen eines bestimmten Tools funktionieren.
## Rationale
source: user
## Acceptance criteria
### AC-USE-02
```gherkin
Given ein beliebiger Prompt
When man ihn prüft
Then setzt er keine Sonderfunktion eines bestimmten Tools voraus.
```
### AC-USE-03
```gherkin
Given ein KI-Chat ohne Dateizugriff
When man einen Prompt nutzt
Then erhält man sein Ergebnis als Text.
```
## Failure cases in real use
- kein Dateizugriff → [AC-USE-03](#ac-use-03), [OQ-USE-01](../../REQUIREMENTS.md#oq-use-01)
## References
[FR-DIALOG-08](FR-DIALOG-08.md), [OQ-USE-01](../../REQUIREMENTS.md#oq-use-01)
