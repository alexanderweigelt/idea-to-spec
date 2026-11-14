# FR-SPEC-01 – Prüf-Prompt listet Widersprüche und Lücken
Owner: REQUIREMENTS.md · Group: SPEC · Status: confirmed
## Statement
Ein Prüf-Prompt muss Widersprüche und Lücken der Spezifikation mit ID auflisten.
## Rationale
source: user
## Acceptance criteria
### AC-SPEC-01
```gherkin
Given eine Spezifikation mit einem Widerspruch
When der Prüf-Prompt läuft
Then listet er den Widerspruch mit ID.
```
### AC-SPEC-02
```gherkin
Given eine Spezifikation mit einer Lücke
When der Prüf-Prompt läuft
Then listet er die Lücke mit ID.
```
## Failure cases in real use
- keine benannt
## References
[OQ-SPEC-02](../../REQUIREMENTS.md#oq-spec-02)
