# Idea to Spec – Prompt-Library

Kopierbare, rollenbasierte Prompts, die ein Webprojekt Schritt für Schritt von einer unvollständigen Idee zu einer abgestimmten, widerspruchsfreien Spezifikation führen. Daraus entstehen prüfbare Arbeitspakete für Spec-Driven Development: Die Spezifikation ist so konkret, dass ihre Erfüllung prüfbar ist, und dient als Grundlage für Planung, Umsetzung, Test, Review und Abnahme.

## Reihenfolge

Fest ist nur: zuerst die Anforderungen. Danach wird diese Reihenfolge empfohlen:

| # | Prompt | Wozu | Erzeugt |
|---|---|---|---|
| 1 | [requirements.md](requirements.md) | Idee zu prüfbaren Anforderungen klären | REQUIREMENTS.md, docs/REQUIREMENT_TEMPLATE.md |
| – | [legal.md](legal.md) | optional: Datenschutz, Lizenzen, Regeln Dritter (keine Rechtsberatung) | LEGAL.md |
| 2 | [design.md](design.md) | Gestaltung und Barrierefreiheit, nur mit Benutzeroberfläche | DESIGN.md |
| 3 | [architecture.md](architecture.md) | Aufbau, Technik, Betrieb und Entscheidungen | ARCHITECTURE.md, ADRs |
| 4 | [security.md](security.md) | Bedrohungen und Sicherheitsanforderungen, prüft alle Beiträge | SECURITY.md |
| 5 | [review.md](review.md) | Widersprüche und Lücken finden, Freigabe durch einen Menschen | Befunde als OQ in den Fachdokumenten, Freigabe im README |
| 6 | [work-packages.md](work-packages.md) | Freigegebene Spezifikation in prüfbare Pakete schneiden | WORK_PACKAGES.md |
| 7 | [agents.md](agents.md) | Regeln und Prüfbefehle für die Umsetzung | AGENTS.md |

Recht empfiehlt sich vor Design und Architektur, sobald personenbezogene Daten, fremde Inhalte oder Dienste Dritter im Spiel sind.

## Offene Fragen

Was die KI nicht sicher weiß, schreibt sie als offene Frage (OQ) mit Empfehlung auf, statt etwas zu erfinden; Annahmen bestätigst du gesammelt. Was nur ein Versuch klären kann, wird das erste Arbeitspaket (Machbarkeitsprobe). Die Prüfung gibt erst frei, wenn keine Frage mehr offen oder jede bewusst akzeptiert ist.

## Kleine und große Vorhaben

Bei kleinen Vorhaben Rollen und Rechte einfach weglassen. Große Projekte starten mit einem Vorgabendokument und klären die Anforderungen in Teilbereichen nacheinander.

## Änderungen

Eine Änderung geht über den zuständigen Prompt, der nur das Betroffene ändert und alle IDs behält; danach die Prüfung erneut ausführen.

## Chats

Empfohlen: ein neuer Chat je Prompt; ein gemeinsamer Chat funktioniert ebenfalls.

## Übergang zur Umsetzung

AGENTS.md sagt dem umsetzenden Entwickler oder KI-Agenten, welche Datei er wofür liest, welche Sicherheitsregeln gelten und welche Prüfbefehle jedes Arbeitspaket bestehen muss.
