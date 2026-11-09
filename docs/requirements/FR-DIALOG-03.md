# FR-DIALOG-03 – Form der Fragen
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Wenn die KI eine Frage stellt, muss sie 2–4 nummerierte Möglichkeiten mit markierter Empfehlung und kurzer Begründung vorschlagen, eine Antwort per Nummer oder eigenem Text annehmen und höchstens 3 Fragen pro Runde stellen, die wichtigsten zuerst.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-07
```gherkin
Given eine Frage der KI
When man die Möglichkeiten prüft
Then sind es 2–4, nummeriert, mit markierter Empfehlung und kurzer Begründung.
```
### AC-DIALOG-08
```gherkin
Given eine Frage der KI
When der Mensch mit einer Nummer oder eigenem Text antwortet
Then übernimmt die KI die Antwort.
```
### AC-DIALOG-09
```gherkin
Given eine Fragerunde
When man ihre Fragen zählt
Then sind es höchstens 3, die wichtigste zuerst.
```
### AC-DIALOG-10
```gherkin
Given ein Vorschlag der KI
When man ihn liest
Then ist er als Vorschlag erkennbar.
```
## Failure cases in real use
- keine benannt
## References
none
