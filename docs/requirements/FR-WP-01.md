# FR-WP-01 – Verweise und Abdeckung
Owner: REQUIREMENTS.md · Group: WP · Status: confirmed
## Statement
Jedes Arbeitspaket muss auf die IDs seiner Anforderungen verweisen, und jede Anforderung muss in mindestens einem Arbeitspaket stecken.
## Rationale
source: user
## Acceptance criteria
### AC-WP-01
```gherkin
Given ein beliebiges Arbeitspaket
When man es prüft
Then verweist es auf die IDs seiner Anforderungen.
```
### AC-WP-02
```gherkin
Given alle Anforderungen und alle Arbeitspakete
When man die Abdeckung prüft
Then steckt jede Anforderung in mindestens einem Arbeitspaket.
```
## Failure cases in real use
- keine benannt
## References
[OQ-WP-01](../../REQUIREMENTS.md#oq-wp-01), [OQ-WP-02](../../REQUIREMENTS.md#oq-wp-02)
