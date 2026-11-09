# FR-SPEC-05 – Jede Aussage hat eine ID
Owner: REQUIREMENTS.md · Group: SPEC · Status: confirmed
## Statement
Jede Aussage muss zu einer Anforderung, Entscheidung oder offenen Frage gehören, ausgenommen der Wegweiser-Abschnitt im README.md und AGENTS.md.
## Rationale
source: user
## Acceptance criteria
### AC-SPEC-11
```gherkin
Given ein Dokument außer dem Wegweiser-Abschnitt im README.md und AGENTS.md
When man jede Aussage prüft
Then gehört sie zu einer Anforderung, Entscheidung oder offenen Frage.
```
## Failure cases in real use
- keine benannt
## References
[FR-SPEC-04](FR-SPEC-04.md)
