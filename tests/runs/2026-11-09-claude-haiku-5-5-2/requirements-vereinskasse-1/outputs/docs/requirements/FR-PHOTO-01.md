# FR-PHOTO-01 – Verkleinerung vor dem Hochladen
Owner: REQUIREMENTS.md · Group: PHOTO · Status: confirmed
## Statement
Bevor ein Foto hochgeladen wird, muss die App es auf höchstens 2 MB verkleinern und dabei die lange Seite auf mindestens 1600 Pixel lassen.
## Rationale
Begrenzt das Datenvolumen und hält die Zahlen lesbar. Quelle: user (OQ-PHOTO-01); Startwerte, siehe OQ-ASSUME-08.
## Acceptance criteria
### AC-PHOTO-01
```gherkin
Given ein Foto ist 8 MB groß mit 4000 Pixeln auf der langen Seite
When das Foto hochgeladen wird
Then ist die Datei höchstens 2 MB groß und die lange Seite mindestens 1600 Pixel
```
## Failure cases in real use
- Verkleinerung macht Zahlen unlesbar → [AC-PHOTO-01](#ac-photo-01); Grenzwert wird im Test geprüft (OQ-ASSUME-08)
- Foto ist von Haus aus kleiner als 1600 Pixel → [AC-PHOTO-01](#ac-photo-01)
## References
[OQ-PHOTO-01](../../REQUIREMENTS.md#oq-photo-01)
