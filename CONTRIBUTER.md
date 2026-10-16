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

## Änderungen einreichen

- Halten Sie Änderungen klein und begründen Sie sie mit einer Anforderung aus `REQUIREMENTS.md`. Weniger ist besser: Lassen Sie weg, was keinen Nutzen hat.
- Arbeiten Sie auf einem eigenen Branch, nicht direkt auf `main`.
- Commit-Nachrichten folgen [Conventional Commits](https://www.conventionalcommits.org/) und sind englisch, zum Beispiel `feat: add legal prompt` oder `docs: fix guide step order`. Eine logische Änderung pro Commit.
- Ändert sich ein Prompt, prüfen Sie, ob der Leitfaden in `lib/README.md` angepasst werden muss.
- Neue Prompts oder Änderungen sollten Sie in einer neuen KI-Session per Copy-and-paste ausprobieren. Nur Angewendetes gilt als geprüft.

## Mit Agenten arbeiten

Agenten, die an diesem Repository arbeiten, folgen [AGENTS.md](AGENTS.md). Sie committen, pushen oder löschen nicht ohne ausdrücklichen Auftrag.

## Lizenz

Mit Ihrem Beitrag stimmen Sie zu, dass er unter der [MIT-Lizenz](LICENSE) steht.
