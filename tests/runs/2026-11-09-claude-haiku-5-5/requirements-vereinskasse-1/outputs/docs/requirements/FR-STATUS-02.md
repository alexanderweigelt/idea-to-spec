# FR-STATUS-02 – Mitglied sieht den aktuellen Status
Owner: REQUIREMENTS.md · Group: STATUS · Status: confirmed

## Statement
Wenn ein Mitglied eine seiner Einreichungen aufruft, zeigt das System deren aktuelle Stufe.

## Rationale
Mitglieder sollen wissen, wo ihr Geld steht. Quelle: user (Entscheidung Kernablauf, Frage 4).

## Acceptance criteria
### AC-STATUS-02
```gherkin
Given die Einreichung E1 von Anna hat die Stufe „geprüft“
When Anna E1 aufruft
Then sieht Anna die Stufe „geprüft“
```

## Failure cases in real use
- Bei schlechter Verbindung wird ein veralteter Status angezeigt → [OQ-OFFLINE-01](REQUIREMENTS.md#oq-offline-01)

## References
[OQ-OFFLINE-01](REQUIREMENTS.md#oq-offline-01)
