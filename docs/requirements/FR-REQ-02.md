# FR-REQ-02 – Erlaubte ID-Arten, sprechend und stabil
Owner: REQUIREMENTS.md · Group: REQ · Status: confirmed
## Statement
Die Prompt-Library muss nur die ID-Arten FR, AC, OQ, ADR, SEC, DES und WP verwenden, IDs sprechend aus Art plus Themengruppe bilden (z. B. SEC-AUTH-01), wobei die Themengruppe aus REQUIREMENTS.md oder dem Standard des jeweiligen Prompts stammt, und eine vergebene ID nie ändern oder neu vergeben.
## Rationale
source: user
## Acceptance criteria
### AC-REQ-03
```gherkin
Given alle Dokumente einer Spezifikation
When man die ID-Arten sammelt
Then kommen nur FR, AC, OQ, ADR, SEC, DES und WP vor.
```
### AC-REQ-04
```gherkin
Given eine beliebige ID
When man sie liest
Then besteht sie aus Art plus einer Themengruppe, die in REQUIREMENTS.md oder im Standard des zuständigen Prompts vorkommt und im Abschnitt „IDs lesen“ erklärt ist.
```
### AC-REQ-05
```gherkin
Given eine Spezifikation vor und nach einer Änderung
When man die IDs vergleicht
Then ist keine vergebene ID geändert oder neu vergeben.
```
## Failure cases in real use
- gestrichene Anforderung → [OQ-SPEC-04](../../REQUIREMENTS.md#oq-spec-04)
## References
[OQ-REQ-01](../../REQUIREMENTS.md#oq-req-01), [OQ-REQ-02](../../REQUIREMENTS.md#oq-req-02), [OQ-SPEC-04](../../REQUIREMENTS.md#oq-spec-04), [OQ-SPEC-07](../../REQUIREMENTS.md#oq-spec-07)
