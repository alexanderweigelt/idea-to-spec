# FR-SPEC-03 – Änderungen einarbeiten ohne Neuaufbau
Owner: REQUIREMENTS.md · Group: SPEC · Status: confirmed
## Statement
Wenn eine Änderung ansteht, muss sie sich in eine bestehende Spezifikation einarbeiten lassen, ohne alles neu zu machen.
## Rationale
source: user
## Acceptance criteria
### AC-SPEC-06
```gherkin
Given eine bestehende Spezifikation und eine Änderung
When die Änderung eingearbeitet wird
Then bleiben die davon nicht betroffenen Dokumente unverändert.
```
## Failure cases in real use
- gestrichene Anforderung → [OQ-SPEC-04](../../REQUIREMENTS.md#oq-spec-04)
## References
[FR-REQ-02](FR-REQ-02.md), [OQ-SPEC-01](../../REQUIREMENTS.md#oq-spec-01), [OQ-SPEC-03](../../REQUIREMENTS.md#oq-spec-03), [OQ-SPEC-04](../../REQUIREMENTS.md#oq-spec-04)
