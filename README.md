# Idea to Spec

Von der Projektidee zu einer prüfbaren Spezifikation: kopierbare, rollenbasierte Prompts für Webprojekte.

Idea to Spec führt ein Webprojekt schrittweise von einer noch unvollständigen Idee zu einer abgestimmten, widerspruchsfreien Spezifikation und daraus abgeleiteten, prüfbaren Arbeitspaketen. Das ist die Grundlage für Spec-Driven Development: Planung, Umsetzung, Tests, Review und Abnahme richten sich nach der Spezifikation.

## Was du hier findest

- **Fachprompts** für Anforderungen, Recht (optional), Design, Architektur, Sicherheit, Prüfung und Arbeitspakete sowie einen Prompt für AGENTS.md als Übergang in die Umsetzung. Jeder Prompt ist ein eigenständiger Arbeitsauftrag, den du in einen KI-Chat kopierst. Die KI erarbeitet den Beitrag gemeinsam mit dir und legt ihn in einer Projektdatei ab.
- **Einen Leitfaden**, der Reihenfolge und Anwendung der Prompts erklärt, einschließlich Änderungen, kleiner und großer Vorhaben und des Übergangs in die Umsetzung.

Die Prompts funktionieren in jedem KI-Chat und sind für Entwicklerinnen, Entwickler und Produktverantwortliche gedacht.

## Einstieg

**Der Leitfaden mit Prompt-Übersicht steht in [lib/README.md](lib/README.md).** Dort findest du auch alle Prompts.

Die Anforderungen an dieses Projekt selbst stehen in [REQUIREMENTS.md](REQUIREMENTS.md); jede Anforderung hat eine eigene Datei in [docs/requirements/](docs/requirements/).

## IDs lesen

Jede ID hat die Form Art-Gruppe-Nummer, zum Beispiel FR-FLOW-01: Anforderung Nr. 01 in der Gruppe FLOW. Eine vergebene ID ändert sich nie; der Dateiname einer Anforderung ist ihre ID.

| Art | Bedeutung |
|---|---|
| FR | Anforderung (Functional Requirement) |
| AC | Abnahmekriterium einer Anforderung (Acceptance Criterion) |
| OQ | offene Frage (Open Question); mit Haken: getroffene Entscheidung |
| ADR | Architekturentscheidung (Architecture Decision Record) |
| SEC | Sicherheitsanforderung (Security) |
| DES | Designanforderung (Design) |
| WP | Arbeitspaket (Work Package) |

Themengruppen dieses Projekts:

| Gruppe | Thema |
|---|---|
| SCOPE | Zweck und Abgrenzung |
| FLOW | Ablauf und Aufbau |
| DIALOG | Gesprächsführung und Prüftiefe |
| REQ | Anforderungen |
| SPEC | Spezifikation und Prüfung |
| WP | Arbeitspakete |
| USE | Nutzung |

## Specification

| Document | Responsibility | Status |
|---|---|---|
| [REQUIREMENTS.md](REQUIREMENTS.md) | Anforderungen an die Prompt-Library | confirmed |
