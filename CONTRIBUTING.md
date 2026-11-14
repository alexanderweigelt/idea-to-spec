# Mitwirken an Idea to Spec

Danke für Ihr Interesse. Die oberste Grundlage ist [REQUIREMENTS.md](REQUIREMENTS.md): Was dort steht, gilt. Prüfen Sie jede Änderung daran. Die Arbeitsregeln für Menschen und Agenten stehen in [AGENTS.md](AGENTS.md).

## Wie eine Änderung entsteht

- `lib/` wird aus REQUIREMENTS.md erzeugt. Ändern Sie Prompts nie direkt in `lib/`. Passen Sie stattdessen die Anforderungen an, bevorzugt durch eine behutsame Änderung eines bestehenden Eintrags, und erzeugen Sie `lib/` danach neu. Ein Neuaufbau muss jede Anforderung wieder erfüllen.
- Jede Anforderung hat eine eigene Datei in [docs/requirements/](docs/requirements/), ihr Dateiname ist ihre ID. Neue Anforderungen folgen der Vorlage [docs/REQUIREMENT_TEMPLATE.md](docs/REQUIREMENT_TEMPLATE.md).
- Wie ein Prompt aufgebaut ist, welche Sprache wo gilt und welche Standards vorbelegt sind, legt REQUIREMENTS.md fest (zum Beispiel FR-FLOW-02, OQ-FLOW-04, OQ-FLOW-06). Diese Regeln werden hier nicht wiederholt.
- Halten Sie Änderungen klein und begründen Sie jede mit einer ID aus REQUIREMENTS.md. Weniger ist besser: Lassen Sie weg, was keinen Nutzen hat.

## IDs

- Welche ID-Arten und Themengruppen es gibt, erklärt der Abschnitt „IDs lesen“ in [README.md](README.md).
- Eine vergebene ID wird nie neu vergeben.
- Formulierungen werden wörtlich gelesen: „sollte“ ist optional, „muss“ ist Pflicht. Nicht verschärfen.

## Prompts testen

- Wie getestet wird, beschreibt [skills/test-prompts/SKILL.md](skills/test-prompts/SKILL.md). Die Schritte sind einfache Shell-Befehle und funktionieren mit jedem Agenten oder von Hand.
- Stufe 1 ist eine statische Prüfung ohne KI und ohne Kosten (`python tests/static_check.py`). Sie muss bestehen, bevor ein kostenpflichtiger Lauf startet.
- Stufe 2 sind automatische Szenario-Läufe mit simuliertem Nutzer und harter Kostengrenze. Vor jedem kostenpflichtigen Lauf wird die Kostenschätzung gezeigt und auf Zustimmung gewartet.
- Befunde aus Tests werden in REQUIREMENTS.md behoben, nie direkt in `lib/`.

## Branch-Modell (Gitflow)

- `main` enthält nur veröffentlichte, stabile Stände. Es wird nicht direkt darauf gearbeitet.
- `develop` sammelt fertige Änderungen für die nächste Version.
- `feature/<short-name>` für jede Änderung, abgezweigt von `develop` und dorthin zurückgeführt.
- `release/<version>` zur Vorbereitung einer Version, danach nach `main` und `develop`.
- `hotfix/<short-name>` für dringende Korrekturen, abgezweigt von `main`, danach nach `main` und `develop`.
- Branch-Namen sind immer englisch, Kleinbuchstaben, mit Bindestrichen, zum Beispiel `feature/legal-prompt`.

## Commits (Conventional Commits)

- Commit-Nachrichten folgen [Conventional Commits](https://www.conventionalcommits.org/) und sind immer englisch: `<type>: <description>`, zum Beispiel `feat: add legal prompt`.
- Erlaubte Typen: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
- Die Beschreibung steht im Imperativ, ohne Punkt am Ende. Ein Hinweis auf eine Anforderung kann in den Nachrichtentext.
- Eine logische Änderung pro Commit. Ein Breaking Change wird mit `!` hinter dem Typ und `BREAKING CHANGE:` im Nachrichtentext gekennzeichnet.

## Mit Agenten arbeiten

Agenten folgen [AGENTS.md](AGENTS.md) und den Branch- und Commit-Regeln oben. Sie committen, pushen oder löschen nicht ohne ausdrücklichen Auftrag.

## Lizenz

Mit Ihrem Beitrag stimmen Sie zu, dass er unter der [MIT-Lizenz](LICENSE) steht.
