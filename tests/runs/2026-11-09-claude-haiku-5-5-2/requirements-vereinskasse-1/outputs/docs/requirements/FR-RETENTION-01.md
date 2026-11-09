# FR-RETENTION-01 – Löschung zum Jahresende
Owner: REQUIREMENTS.md · Group: RETENTION · Status: confirmed
## Statement
Nach dem Ende des Kalenderjahres, in dem ein Beleg erstattet wurde, muss die App den Beleg automatisch löschen.
## Rationale
Datensparsamkeit. Die gesetzliche Frist prüft der Legal-Prompt (OQ-LEGAL-02). Quelle: user (OQ-RETENTION-01).
## Acceptance criteria
### AC-RETENTION-01
```gherkin
Given ein Beleg wurde im Jahr 2025 erstattet
When das Jahr 2025 endet
Then ist der Beleg spätestens am 1. Januar 2026 gelöscht
```
## Failure cases in real use
- Erstattung im Dezember, Jahreswechsel bei der Verarbeitung → [AC-RETENTION-01](#ac-retention-01)
- Gesetzliche Frist ist länger → [OQ-LEGAL-02](../../REQUIREMENTS.md#oq-legal-02)
## References
[OQ-RETENTION-01](../../REQUIREMENTS.md#oq-retention-01)
