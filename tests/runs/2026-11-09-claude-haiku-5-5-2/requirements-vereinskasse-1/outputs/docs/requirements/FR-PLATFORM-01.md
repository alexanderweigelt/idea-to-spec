# FR-PLATFORM-01 – Installierbare Web-App
Owner: REQUIREMENTS.md · Group: PLATFORM · Status: confirmed
## Statement
Die App muss als Web-App laufen, die das Mitglied auf dem Startbildschirm seines Smartphones ablegen kann.
## Rationale
Kein Store, keine Store-Gebühren vorerst. Quelle: user (OQ-PLATFORM-01).
## Acceptance criteria
### AC-PLATFORM-01
```gherkin
Given das Mitglied hat die Web-App im Browser auf dem Smartphone geöffnet
When es die App auf dem Startbildschirm ablegt
Then startet die App vom Startbildschirm aus
```
## Failure cases in real use
- Browser erlaubt keine Installation → [AC-PLATFORM-01](#ac-platform-01); die App bleibt im Browser nutzbar
## References
[OQ-PLATFORM-01](../../REQUIREMENTS.md#oq-platform-01)
