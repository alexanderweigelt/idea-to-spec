# Mitwirken an Idea to Spec

Danke für Ihr Interesse. Die oberste Grundlage ist [REQUIREMENTS.md](REQUIREMENTS.md): Was dort steht, gilt. Prüfen Sie jede Änderung daran.

## Regeln für Prompts

- Jeder Prompt liegt in einer eigenen Datei in `lib/` und ist eigenständig kopierbar. Kein Prompt setzt einen anderen voraus.
- Dateinamen: englisch, Kleinbuchstaben, mit Bindestrich, ohne Nummern.
- Aufbau: kurzer deutscher Kopf (Rolle, Zweck, Voraussetzungen, Eingaben, Ergebnisdatei), darunter genau ein englischer Prompt-Block. Der Block beginnt mit einem Rollensatz, der Auftrag und Grenze nennt, danach folgt der Eingabeblock mit benannten Feldern.
- Einen gemeinsamen Grundtext, der in jeden Prompt kopiert wird, gibt es nicht. Jeder Prompt enthält nur die Regeln, die er braucht.
- Standards und Qualitätsziele gehören in den zuständigen Fachprompt, mit Version.
- Keine Entstehungsgeschichte, Schulungsbezüge oder Änderungshistorien in Prompts.
- Nichts erfinden: keine Funktionen, Fakten, Standardkennungen oder Prüfergebnisse. Was nicht geprüft werden konnte, wird als ungeprüft gekennzeichnet.

## Sprache und Kennungen

- Anweisungen für Agenten (Prompts, `AGENTS.md`, `CLAUDE.md`), Dateinamen und Code sind englisch.
- Beschreibungen und der Leitfaden sind deutsch.
- Kennungen (FR, AC, OQ, ADR, SEC, T, WP) werden nie neu vergeben.
- Die Version steht nur in `lib/README.md`.
- Formulierungen werden wörtlich gelesen: „sollte“ ist optional, „muss“ ist Pflicht. Nicht verschärfen.

## Branch-Modell (Gitflow)

- `main` enthält nur veröffentlichte, stabile Stände. Es wird nicht direkt darauf gearbeitet.
- `develop` sammelt fertige Änderungen für die nächste Version.
- `feature/<short-name>` für jede Änderung, abgezweigt von `develop` und dorthin zurückgeführt.
- `release/<version>` zur Vorbereitung einer Version, danach nach `main` und `develop`.
- `hotfix/<short-name>` für dringende Korrekturen, abgezweigt von `main`, danach nach `main` und `develop`.
- Branch-Namen sind immer englisch, Kleinbuchstaben, mit Bindestrichen, zum Beispiel `feature/legal-prompt`.

## Commits (Conventional Commits)

- Commit-Nachrichten folgen [Conventional Commits](https://www.conventionalcommits.org/) und sind immer englisch: `<type>: <description>`, zum Beispiel `feat: add legal prompt`.
- Erlaubte Typen: `feat`, `fix`, `docs`, `refactor`, `chore`.
- Die Beschreibung steht im Imperativ, ohne Punkt am Ende. Ein Hinweis auf eine Anforderung kann in den Nachrichtentext.
- Eine logische Änderung pro Commit. Ein Breaking Change wird mit `!` hinter dem Typ und `BREAKING CHANGE:` im Nachrichtentext gekennzeichnet.

## Änderungen einreichen

- Halten Sie Änderungen klein und begründen Sie sie mit einer Anforderung aus `REQUIREMENTS.md`. Weniger ist besser: Lassen Sie weg, was keinen Nutzen hat.
- Ändert sich ein Prompt, prüfen Sie, ob der Leitfaden in `lib/README.md` angepasst werden muss.
- Neue Prompts oder Änderungen sollten Sie in einer neuen KI-Session per Copy-and-paste ausprobieren. Nur Angewendetes gilt als geprüft.
- Für Vergleichstests sollten Eingabe, erwartetes Ergebnis, Modellversion und tatsächliches Ergebnis festgehalten und dieselben Beispiele nach Prompt- oder Modelländerungen erneut geprüft werden. Bei Promptänderungen sollten alte und neue Fassung mit derselben Modellversion verglichen werden.
- Bestehenskriterien sollten beobachtbares Verhalten beschreiben, zum Beispiel: fehlende Angaben werden als offen markiert; bestätigte Entscheidungen bleiben erhalten; ohne Dateizugriff wird ein vollständiger Entwurf mit Speicherhinweis geliefert. Wortgleiche Antworten sind kein sinnvolles Bestehenskriterium. Vorhandene echte Projektbeispiele können wiederverwendet werden.

## Mit Agenten arbeiten

Agenten, die an diesem Repository arbeiten, folgen [AGENTS.md](AGENTS.md) und den Branch- und Commit-Regeln oben. Sie committen, pushen oder löschen nicht ohne ausdrücklichen Auftrag.

## Lizenz

Mit Ihrem Beitrag stimmen Sie zu, dass er unter der [MIT-Lizenz](LICENSE) steht.
