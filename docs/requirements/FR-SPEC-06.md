# FR-SPEC-06 – Eine Datei je Anforderung, höchstens ca. 40 Zeilen
Owner: REQUIREMENTS.md · Group: SPEC · Status: confirmed
## Statement
Jede Anforderung muss in einer eigenen Datei von höchstens einer Bildschirmseite (ca. 40 Zeilen) stehen, sonst muss sie geteilt werden.
## Rationale
source: user
## Acceptance criteria
### AC-SPEC-12
```gherkin
Given eine beliebige Anforderung
When man ihren Ort prüft
Then steht sie in einer eigenen Datei.
```
### AC-SPEC-13
```gherkin
Given eine beliebige Anforderungsdatei
When man ihre Zeilen zählt
Then sind es höchstens ca. 40.
```
## Failure cases in real use
- kein Dateizugriff → [OQ-USE-01](../../REQUIREMENTS.md#oq-use-01)
## References
[OQ-USE-01](../../REQUIREMENTS.md#oq-use-01)
