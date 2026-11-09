# FR-PLATFORM-01 – Installation als PWA auf dem Startbildschirm
Owner: REQUIREMENTS.md · Group: PLATFORM · Status: confirmed

## Statement
Wenn ein Mitglied die App im mobilen Browser öffnet, bietet das System die Installation auf dem Startbildschirm an.

## Rationale
Die App wird als PWA ohne Store verteilt. Quelle: user (Entscheidung Plattform, Frage 3) und user (Entscheidung Store, Frage 7).

## Acceptance criteria
### AC-PLATFORM-01
```gherkin
Given Anna öffnet die App auf einem Android-Handy in Chrome
When die Seite vollständig geladen ist
Then bietet der Browser die Installation auf dem Startbildschirm an
```

## Failure cases in real use
- Der Browser unterstützt die Installation nicht → [OQ-PLATFORM-01](REQUIREMENTS.md#oq-platform-01)

## References
[OQ-PLATFORM-01](REQUIREMENTS.md#oq-platform-01)
