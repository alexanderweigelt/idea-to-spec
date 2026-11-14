# FR-ROLE-02 – Kassenwart sieht alle Einreichungen und setzt den Status
Owner: REQUIREMENTS.md · Group: ROLES · Status: confirmed

## Statement
Wenn der Kassenwart die Einreichungen aufruft, zeigt das System alle Einreichungen und erlaubt ihm, deren Status zu setzen.

## Rationale
Der Kassenwart prüft und erstattet alle Auslagen. Quelle: user (Entscheidung Rollen, Frage 1).

## Acceptance criteria
### AC-ROLE-02
```gherkin
Given Anna hat die Einreichung E1 und Ben hat die Einreichung E2
When der Kassenwart die Einreichungen aufruft
Then sieht er E1 und E2 und kann bei beiden den Status setzen
```

## Failure cases in real use
- Der Kassenwart wechselt, der Nachfolger braucht Zugriff → [OQ-ROLE-02](REQUIREMENTS.md#oq-role-02)

## References
[OQ-ROLE-02](REQUIREMENTS.md#oq-role-02)
