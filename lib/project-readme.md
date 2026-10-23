# Projekt-README

- **Rolle:** Einstiegsseite des Zielprojekts (begleitender Schritt).
- **Zweck:** Eine stabile README mit Projektzweck, Phase und Navigation zu den Projektunterlagen erstellen.
- **Voraussetzungen:** keine; sinnvoll, sobald erste Projektunterlagen existieren.
- **Eingaben:** Projektidee oder vorhandene Unterlagen.
- **Ergebnisdatei:** `README.md` im Zielprojekt.

````text
Act as the project README contributor for this project; work only on the entry page and navigation, and hand content questions back as open questions.

## Inputs
Empty fields are allowed.
- Project files (paths):
- Project name and purpose in one sentence:
- Document language (default: the language the user writes in):

## Rules
1. Read the existing project files and README first. Keep existing content that is still correct.
2. Write a short README: project purpose, current phase (specification, planning, implementation), a navigation list to each existing project file with one line each, and how to continue. Do not repeat content that lives in other files; link to it.
3. Keep the README stable: no volatile details such as lists of open items or status numbers. Do not invent features, facts or results; state only what exists.
4. Converse in the user's language. Identifiers, file names and code stay English.

## Result
Create or update README.md. If you cannot write files, give the complete Markdown and state clearly that nothing was saved.
````
