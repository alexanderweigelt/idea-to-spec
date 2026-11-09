# FR-CAPTURE-01 – Vorschlag für Betrag und Datum
Owner: REQUIREMENTS.md · Group: CAPTURE · Status: confirmed
## Statement
Wenn ein Mitglied einen Beleg fotografiert hat, muss die App Betrag und Datum aus dem Foto als Vorschlag anzeigen und darf den Beleg erst nach Bestätigung oder Korrektur einreichen.
## Rationale
Die automatische Erkennung ist fehleranfällig. Quelle: user (OQ-CAPTURE-01); given (Erkennung über Google Cloud Vision).
## Acceptance criteria
### AC-CAPTURE-01
```gherkin
Given ein Mitglied hat einen Beleg fotografiert und die Erkennung liefert „12,50 €“
When die Erkennung abgeschlossen ist
Then zeigt die App „12,50 €“ als Vorschlag, und das Mitglied kann den Betrag ändern
```
## Failure cases in real use
- Erkennung liest falsche Zahl (z. B. 1.250 statt 12,50) → [AC-CAPTURE-01](#ac-capture-01)
- Mitglied bestätigt ohne zu prüfen → [AC-CAPTURE-01](#ac-capture-01)
## References
[OQ-CAPTURE-01](../../REQUIREMENTS.md#oq-capture-01)
