# FR-QUALITY-03 – Lauffähig in aktuellen Android Chrome und iOS Safari
Owner: REQUIREMENTS.md · Group: QUALITY · Status: confirmed

## Statement
Das System läuft ohne Einschränkung in den aktuellen Versionen von Android Chrome und iOS Safari.

## Rationale
Die Mitglieder nutzen überwiegend diese beiden Browser auf dem Handy. Quelle: user (Annahme A7, bestätigt).

## Acceptance criteria
### AC-QUALITY-03
```gherkin
Given Anna nutzt die aktuelle Version von Android Chrome oder iOS Safari
When Anna eine Einreichung mit Foto erstellt und absendet
Then gelingt die Einreichung ohne Fehlermeldung
```

## Failure cases in real use
- Ein älterer Browser wird genutzt → [OQ-PLATFORM-01](REQUIREMENTS.md#oq-platform-01)

## References
[OQ-PLATFORM-01](REQUIREMENTS.md#oq-platform-01)
