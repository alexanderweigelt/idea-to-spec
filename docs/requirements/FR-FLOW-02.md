# FR-FLOW-02 – Einheitliche Vorlage je Prompt
Owner: REQUIREMENTS.md · Group: FLOW · Status: confirmed
## Statement
Jeder Prompt muss derselben Vorlage folgen: Rolle, Ziel, Eingabe, Ausgabe und wann der Schritt fertig ist.
## Rationale
source: user
## Acceptance criteria
### AC-FLOW-03
```gherkin
Given ein beliebiger Prompt
When man seine Teile prüft
Then enthält er Rolle, Ziel, Eingabe, Ausgabe und die Bedingung, wann der Schritt fertig ist.
```
### AC-FLOW-04
```gherkin
Given zwei beliebige Prompts
When man ihre Gliederung vergleicht
Then folgen beide derselben Vorlage.
```
## Failure cases in real use
- keine benannt
## References
none
