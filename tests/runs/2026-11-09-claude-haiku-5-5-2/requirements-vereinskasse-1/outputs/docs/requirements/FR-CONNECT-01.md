# FR-CONNECT-01 – Lokale Speicherung ohne Verbindung
Owner: REQUIREMENTS.md · Group: CONNECT · Status: confirmed
## Statement
Wenn keine Verbindung besteht, muss die App den Beleg lokal speichern und hochladen, sobald wieder eine Verbindung besteht, und nach erfolgreichem Hochladen die lokale Kopie löschen.
## Rationale
Kein Verlust bei schlechtem Empfang; Belegdaten bleiben nicht auf dem Gerät. Quelle: user (OQ-CONNECT-01, ASSUME-07).
## Acceptance criteria
### AC-CONNECT-01
```gherkin
Given das Mitglied hat keine Verbindung
When es einen Beleg einreicht
Then ist der Beleg lokal gespeichert, und die App meldet, dass er hochgeladen wird, sobald Verbindung besteht
```
### AC-CONNECT-02
```gherkin
Given ein lokal gespeicherter Beleg wurde erfolgreich hochgeladen
When der Upload abgeschlossen ist
Then ist die lokale Kopie vom Gerät gelöscht
```
## Failure cases in real use
- App wird geschlossen, bevor der Upload fertig ist → [AC-CONNECT-01](#ac-connect-01)
- Verbindung bricht während des Uploads ab → [AC-CONNECT-01](#ac-connect-01)
## References
[OQ-CONNECT-01](../../REQUIREMENTS.md#oq-connect-01)
