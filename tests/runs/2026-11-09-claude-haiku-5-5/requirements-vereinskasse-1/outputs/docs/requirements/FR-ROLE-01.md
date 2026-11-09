# FR-ROLE-01 – Mitglied sieht nur eigene Einreichungen
Owner: REQUIREMENTS.md · Group: ROLES · Status: confirmed

## Statement
Wenn ein Mitglied seine Einreichungen aufruft, zeigt das System ausschließlich Einreichungen dieses Mitglieds.

## Rationale
Belege anderer Mitglieder sind persönliche Daten. Quelle: user (Entscheidung Rollen, Frage 1).

## Acceptance criteria
### AC-ROLE-01
```gherkin
Given Anna hat die Einreichung E1 und Ben hat die Einreichung E2
When Anna ihre Einreichungen aufruft
Then sieht Anna E1 und sieht E2 nicht
```

## Failure cases in real use
- Anna ruft E2 über eine direkte Adresse auf → [OQ-ROLE-01](REQUIREMENTS.md#oq-role-01)

## References
[OQ-ROLE-01](REQUIREMENTS.md#oq-role-01)
