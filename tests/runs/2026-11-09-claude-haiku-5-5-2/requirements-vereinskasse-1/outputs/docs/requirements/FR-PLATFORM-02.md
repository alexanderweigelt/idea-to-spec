# FR-PLATFORM-02 – Nutzung der Gerätekamera
Owner: REQUIREMENTS.md · Group: PLATFORM · Status: confirmed
## Statement
Die App muss die Kamera des Smartphones nutzen, um Belege zu fotografieren.
## Rationale
Der Beleg wird mit dem Handy fotografiert. Quelle: user (Eingabe, Idee).
## Acceptance criteria
### AC-PLATFORM-02
```gherkin
Given das Mitglied hat der App den Kamerazugriff erlaubt
When es einen Beleg fotografieren will
Then öffnet sich die Kamera, und das Foto wird übernommen
```
## Failure cases in real use
- Mitglied verweigert den Kamerazugriff → [AC-PLATFORM-02](#ac-platform-02); Foto über Galerie-Auswahl ist nicht Teil dieser Anforderung
- Smartphone ohne Kamera → [OQ-ASSUME-01](../../REQUIREMENTS.md#oq-assume-01)
## References
[OQ-ASSUME-01](../../REQUIREMENTS.md#oq-assume-01)
