# FR-DIALOG-02 – Nur Wichtiges fragen, Rest als Annahme
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Die KI muss nur fragen, was weder Vorgaben noch Standards beantworten und was Umfang, Kosten, Machbarkeit oder Prüfbarkeit ändert, und alles andere als markierte Annahme setzen, die der Mensch gesammelt bestätigt.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-03
```gherkin
Given ein Punkt, den eine Vorgabe oder ein Standard beantwortet
When die KI ihn behandelt
Then stellt sie dazu keine Frage.
```
### AC-DIALOG-04
```gherkin
Given ein offener Punkt ohne Einfluss auf Umfang, Kosten, Machbarkeit oder Prüfbarkeit
When die KI ihn behandelt
Then setzt sie eine markierte Annahme statt einer Frage.
```
### AC-DIALOG-05
```gherkin
Given mehrere Annahmen
When die KI sie vorlegt
Then kann der Mensch sie gesammelt bestätigen.
```
### AC-DIALOG-06
```gherkin
Given ein bereits beantworteter Punkt
When das Gespräch weitergeht
Then fragt die KI ihn nicht erneut.
```
## Failure cases in real use
- widersprüchliche Wünsche → [FR-DIALOG-05](FR-DIALOG-05.md)
## References
[FR-DIALOG-01](FR-DIALOG-01.md)
