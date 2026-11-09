# FR-WP-03 – Teilungsregeln
Owner: REQUIREMENTS.md · Group: WP · Status: confirmed
## Statement
Wenn ein Arbeitspaket den Aufwand „groß“ hat, sein Ziel ein „und“ braucht, es mehr als 5 Abnahmekriterien hat oder mehr als einen Systemteil berührt, muss es geteilt werden, wobei 5 und 1 Startwerte sind.
## Rationale
source: user
## Acceptance criteria
### AC-WP-05
```gherkin
Given ein Arbeitspaket mit Aufwand „groß“
When die Pakete fertig geschnitten sind
Then ist es geteilt.
```
### AC-WP-06
```gherkin
Given ein Arbeitspaket, dessen Ziel ein „und“ braucht
When die Pakete fertig geschnitten sind
Then ist es geteilt.
```
### AC-WP-07
```gherkin
Given ein Arbeitspaket mit mehr Abnahmekriterien oder Systemteilen als die Startwerte 5 und 1
When die Pakete fertig geschnitten sind
Then ist es geteilt.
```
### AC-WP-08
```gherkin
Given geänderte Teilungswerte
When die Pakete geschnitten werden
Then gelten die geänderten Werte statt 5 und 1.
```
## Failure cases in real use
- keine benannt
## References
[FR-WP-02](FR-WP-02.md), [OQ-WP-02](../../REQUIREMENTS.md#oq-wp-02)
