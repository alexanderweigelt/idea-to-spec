# AI Prompt Library – Anleitung

Ziel ist Spec-Driven Development: Projektidee → konsistente, umsetzbare
Spezifikation → Arbeitspakete → technische Aufgaben und Prüfungen. Die Prompts
richten sich an Entwicklerinnen und Entwickler, die das jeweilige Fachgebiet
beherrschen.

## Prompts

Jeder Prompt ist ein eigenständiges Skript mit derselben gemeinsamen Grundlage
(COMMON CONTRACT). Er kann angepasst oder gekürzt werden, erzeugt seine eigene
Ergebnisdatei und liest vorhandene Projektdateien, ohne dass andere Prompts vorher
gelaufen sein müssen.

| Prompt | Ergebnisdatei |
| --- | --- |
| [Projektaufnahme und Anforderungen](projektaufnahme.md) | REQUIREMENTS.md, docs/requirements/ |
| [Anforderungsvorlage](anforderungsvorlage.md) | docs/requirements/TEMPLATE.md |
| [Designgrundlage](designgrundlage.md) | DESIGN.md (nur mit Benutzeroberfläche) |
| [Architektur und Entscheidungen](architektur-und-diagramme.md) | ARCHITECTURE.md, docs/adr/ |
| [Projektbezogene Sicherheit](sicherheit.md) | SECURITY.md |
| [Spezifikationsreview](konsolidierung-und-threat-modeling.md) | docs/specification-review.md |
| [Entscheidungen und Baseline](entscheidungen-und-baseline.md) | docs/baseline-review.md |
| [Projekt-README](projekt-readme.md) | README.md |
| [Agent-Anweisungen](agent-anweisungen.md) | AGENTS.md |
| [Arbeitsplan](arbeitsplan-und-uebergabe.md) | docs/work-plan.md |

Empfohlener Ablauf für eine neue Idee: Anforderungen; Design, Architektur und
Sicherheit; Review und Baseline; Arbeitsplan, Agent-Anweisungen und README.
Fragen, Antworten, Befugnisse und der nächste Schritt stehen in
docs/clarifications.md, sodass jede Session ohne Chat-Historie fortsetzen kann.
Die Umsetzung beginnt erst mit einem eigenen Auftrag für WP-001.

Die Arbeitsplanung liefert ausschließlich Arbeitspakete. Ob daraus später Issues
werden, wird separat in der jeweiligen Session entschieden.

## Kernregeln

- **Ready:** Die Kriterien einer Anforderung decken ihre Aussage ab, und keine
  blockierende Frage ist offen. Jeder Fehler-, Grenz- oder Berechtigungsfall, der
  das Ergebnis ändert, hat ein Kriterium oder eine offene Frage.
- **Paketzuschnitt:** Ausgangspunkt ist ein Paket je Anforderung, abgenommen
  als ein PR oder lokaler Review. Geteilt wird, wenn nach dem Weglassen einiger
  Kriterien ein gesondert abnehmbares Ergebnis bleibt; nicht nach Schichten.
  Anforderungen und Pakete dürfen m:n zusammenhängen. Es gibt keine feste
  Größengrenze.

## Prüfprotokoll für den Funktionsdurchlauf

Der Nutzer prüft die Library in einem Testprojekt (derzeit ScannerPWA). Je
angewendetem Prompt festhalten: erfüllt / nicht erfüllt / nicht geprüft / nicht
anwendbar, mit Datei als Beleg und verbleibender Lücke; dazu Anzahl der Fragen,
Freitexteingaben und Dauer. Fälle, die im Testprojekt nicht vorkommen, gelten als
nicht geprüft. Als Ergebnisprüfung je Prompt gilt seine Prüfzeile („Check …“).

| ID | Prüfung | Bestanden, wenn … |
| --- | --- | --- |
| L01 | Eigenständige Nutzung | Jeder Prompt erzeugt seine Ergebnisdatei und nutzt vorhandene Dateien, ohne andere Prompts vorauszusetzen. Mindestens ein Prompt läuft ohne seine üblichen Vorgänger. |
| L02 | Entscheidungsdialog | Offene Entscheidungen kommen als Auswahl mit Folgen und Empfehlung; Autonomie nur mit Delegation. |
| L03 | Sessionwechsel | Ein Prompt startet ohne Chat-Historie und setzt mit docs/clarifications.md fort. |
| L04 | Gemeinsame Grundlage | Alle Abschnitte COMMON CONTRACT bis END COMMON CONTRACT der Library sind wortgleich. |
| L05 | Endgrenze | Kein Prompt führt Setup oder Pakete aus; geplante Prüfungen gelten nicht als bestanden. |
| L06 | Anforderungsqualität | Eine ungeklärte Berechtigung wird zur offenen Frage. Eine Anforderung mit nur einem Erfolgskriterium und einem relevanten unbeschriebenen Fehlerfall wird nicht ready. |
| L07 | Paketzuschnitt | Unabhängig abnehmbare Ergebnisse werden geteilt; ein Ergebnis über mehrere Schichten bleibt ein Paket. Vorarbeiten und Untersuchungen haben eine eigene Prüfung. Ein Kriterium, das mehrere Pakete braucht, nennt das abschließende Paket. |
