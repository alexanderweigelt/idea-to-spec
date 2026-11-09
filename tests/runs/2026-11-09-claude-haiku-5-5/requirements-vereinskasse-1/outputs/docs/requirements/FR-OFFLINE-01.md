# FR-OFFLINE-01 – Zwischenspeichern und automatisches Senden ohne Doppelanlage
Owner: REQUIREMENTS.md · Group: OFFLINE · Status: confirmed

## Statement
Wenn keine Netzverbindung besteht, speichert das System eine Einreichung lokal und sendet sie automatisch genau einmal, sobald eine Verbindung besteht.

## Rationale
Belege dürfen beim Fotografieren ohne Netz nicht verloren gehen. Quelle: user (Entscheidung Verbindung, Frage 6).

## Acceptance criteria
### AC-OFFLINE-01
```gherkin
Given Anna hat im Flugmodus eine Einreichung E1 erstellt
When die Verbindung wiederhergestellt ist
Then erscheint E1 genau einmal beim Kassenwart
```

## Failure cases in real use
- Die Sendung bricht während des Hochladens ab → [AC-OFFLINE-01](FR-OFFLINE-01.md#ac-offline-01)
- Der lokale Speicher ist voll oder das Foto ist sehr groß → [OQ-OFFLINE-01](REQUIREMENTS.md#oq-offline-01)

## References
[OQ-OFFLINE-01](REQUIREMENTS.md#oq-offline-01)
