# FR-CAPTURE-02 – Manuelle Eingabe bei fehlender Erkennung
Owner: REQUIREMENTS.md · Group: CAPTURE · Status: confirmed
## Statement
Wenn die Erkennung keinen Betrag oder kein Datum liefert, muss die App das Mitglied auffordern, Betrag und Datum von Hand einzugeben, bevor eingereicht wird.
## Rationale
Ohne Betrag und Datum ist der Beleg nicht prüfbar. Quelle: user (OQ-CAPTURE-01, ASSUME-02).
## Acceptance criteria
### AC-CAPTURE-02
```gherkin
Given die Erkennung liefert keinen Betrag
When das Mitglied den Beleg einreichen will
Then verlangt die App eine manuelle Betragseingabe und reicht erst danach ein
```
## Failure cases in real use
- Mitglied lässt das Feld leer → [AC-CAPTURE-02](#ac-capture-02)
## References
[OQ-CAPTURE-01](../../REQUIREMENTS.md#oq-capture-01)
