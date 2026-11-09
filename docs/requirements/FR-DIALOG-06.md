# FR-DIALOG-06 – Alarme sofort, Machbarkeitsprobe zuerst
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Wenn ein Befund Machbarkeit oder Umfang gefährdet, muss der Prompt ihn dem Menschen sofort vorlegen, und was nur ein Versuch klären kann, muss als erstes Arbeitspaket eine Machbarkeitsprobe werden.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-17
```gherkin
Given ein Befund, der Machbarkeit oder Umfang gefährdet
When er auftritt
Then legt der Prompt ihn sofort vor, nicht erst am Ende der Runde.
```
### AC-DIALOG-18
```gherkin
Given eine Frage, die nur ein Versuch klären kann
When die Arbeitspakete entstehen
Then ist das erste Arbeitspaket eine Machbarkeitsprobe dazu.
```
## Failure cases in real use
- schwierige Kernfunktion → [AC-DIALOG-18](#ac-dialog-18)
## References
[OQ-DIALOG-02](../../REQUIREMENTS.md#oq-dialog-02), [OQ-SCOPE-06](../../REQUIREMENTS.md#oq-scope-06)
