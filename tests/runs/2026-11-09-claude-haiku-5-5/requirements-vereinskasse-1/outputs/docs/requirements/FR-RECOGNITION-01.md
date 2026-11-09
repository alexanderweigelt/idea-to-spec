# FR-RECOGNITION-01 – Vorschlag für Betrag und Datum aus dem Foto
Owner: REQUIREMENTS.md · Group: RECOGNITION · Status: confirmed

## Statement
Wenn ein Mitglied ein Belegfoto hochlädt, schlägt das System Betrag und Datum aus dem Foto vor, soweit der Dienst sie erkennt.

## Rationale
Spart Eingabeaufwand. Die Erkennung übernimmt Google Cloud Vision. Quelle: given (Vorlage) und user (Entscheidung Erkennung, Frage 2).

## Acceptance criteria
### AC-RECOGNITION-01
```gherkin
Given ein Belegfoto zeigt den Betrag 12,40 € und das Datum 03.05.2025
When Anna das Foto hochlädt
Then zeigt das System 12,40 € und 03.05.2025 als Vorschlag
```

## Failure cases in real use
- Die erkannte Zahl ist falsch → [OQ-RECOGNITION-01](REQUIREMENTS.md#oq-recognition-01)
- Auf dem Foto ist nichts lesbar → [AC-RECOGNITION-02](FR-RECOGNITION-02.md#ac-recognition-02)

## References
[FR-RECOGNITION-02](FR-RECOGNITION-02.md), [OQ-RECOGNITION-01](REQUIREMENTS.md#oq-recognition-01)
