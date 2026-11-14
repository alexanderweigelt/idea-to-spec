# FR-DIALOG-09 – Fachbegriffe erklären
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Der Anforderungs-Prompt muss in Entscheidungsfragen nötige Fachbegriffe in einem Halbsatz erklären, und alle anderen Prompts dürfen nur auf Nachfrage erklären.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-23
```gherkin
Given eine Entscheidungsfrage des Anforderungs-Prompts mit einem nötigen Fachbegriff
When man sie liest
Then erklärt ein Halbsatz den Begriff.
```
### AC-DIALOG-24
```gherkin
Given ein anderer Prompt
When er einen Fachbegriff nutzt und niemand nachfragt
Then erklärt er ihn nicht.
```
## Failure cases in real use
- keine benannt
## References
none
