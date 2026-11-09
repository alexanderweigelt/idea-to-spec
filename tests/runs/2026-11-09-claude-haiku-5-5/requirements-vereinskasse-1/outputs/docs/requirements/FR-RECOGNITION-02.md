# FR-RECOGNITION-02 – Bestätigung oder Korrektur vor dem Absenden
Owner: REQUIREMENTS.md · Group: RECOGNITION · Status: confirmed

## Statement
Bevor ein Mitglied eine Einreichung absendet, zeigt das System die vorgeschlagenen Werte zur Bestätigung oder Korrektur, und das Mitglied kann Betrag und Datum jederzeit von Hand eingeben.

## Rationale
Fehlerhafte Erkennung darf nicht ungeprüft in die Abrechnung gelangen. Quelle: user (Entscheidung Erkennung, Frage 2).

## Acceptance criteria
### AC-RECOGNITION-02
```gherkin
Given der Vorschlag für den Betrag ist leer oder falsch
When Anna den Betrag von Hand auf 14,40 € setzt und die Einreichung absendet
Then wird die Einreichung mit 14,40 € gespeichert
```

## Failure cases in real use
- Das Mitglied sendet ohne Prüfung eine falsche Summe → [OQ-RECOGNITION-01](REQUIREMENTS.md#oq-recognition-01)

## References
[OQ-RECOGNITION-01](REQUIREMENTS.md#oq-recognition-01)
