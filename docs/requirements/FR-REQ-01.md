# FR-REQ-01 – ID und Ja/Nein-Prüfbarkeit
Owner: REQUIREMENTS.md · Group: REQ · Status: confirmed
## Statement
Jede Anforderung muss eine ID haben und mit Ja/Nein prüfbar sein.
## Rationale
source: user
## Acceptance criteria
### AC-REQ-01
```gherkin
Given eine beliebige Anforderung
When man sie prüft
Then hat sie eine ID.
```
### AC-REQ-02
```gherkin
Given eine beliebige Anforderung
When man ihre Erfüllung prüft
Then lässt sich das mit Ja oder Nein beantworten.
```
## Failure cases in real use
- keine benannt
## References
[OQ-SCOPE-09](../../REQUIREMENTS.md#oq-scope-09)
