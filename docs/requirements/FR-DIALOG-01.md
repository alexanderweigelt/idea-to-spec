# FR-DIALOG-01 – Gesprächsführung ohne Erfinden, Start mit einem Satz
Owner: REQUIREMENTS.md · Group: DIALOG · Status: confirmed
## Statement
Die KI muss das Gespräch führen, nichts erfinden und mit nur einem Satz zur Idee starten können, wobei alle Eingabefelder freiwillig sind und jede Quelle eine Rolle ist, nie ein Personenname.
## Rationale
source: user
## Acceptance criteria
### AC-DIALOG-01
```gherkin
Given nur ein Satz zur Idee und sonst leere Eingabefelder
When der Prompt startet
Then führt die KI das Gespräch, ohne weitere Pflichteingaben zu verlangen.
```
### AC-DIALOG-02
```gherkin
Given ein Ergebnisdokument
When man jede Aussage prüft
Then ist jede eine Entscheidung mit Quelle (user, given, standard oder delegated, nie ein Personenname), eine markierte Annahme oder eine offene Frage.
```
## Failure cases in real use
- sehr vage Idee → [AC-DIALOG-01](#ac-dialog-01)
## References
[FR-DIALOG-02](FR-DIALOG-02.md)
