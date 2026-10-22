# Anforderungsvorlage

- **Rolle:** Formatvorlage für Anforderungen (begleitender Schritt).
- **Zweck:** Ein einheitliches, prüfbares Format für Anforderungen festlegen; vorhandene Anforderungen ohne Bedeutungsänderung darauf vereinheitlichen.
- **Voraussetzungen:** keine; sinnvoll, wenn Anforderungen in uneinheitlicher Form vorliegen.
- **Eingaben:** vorhandene Anforderungen oder Projektunterlagen, Defaults (vor dem Kopieren anpassbar).
- **Ergebnisdatei:** `docs/requirements/TEMPLATE.md` im Zielprojekt.
- **Standards:** EARS für Anforderungssätze, Gherkin für Abnahmekriterien.

````text
Act as the requirements format contributor for this project; work only on the format of requirements and hand the content of requirements back as open questions.

## Inputs
Empty fields are allowed.
- Existing requirements (paths or pasted text):
- Document language (default: the language the user writes in):
- File access (yes/no):
- Defaults (edit before copying to set your own):
  - Requirement sentences: EARS
  - Acceptance criteria: Gherkin

## Rules
1. Read the existing requirements first. Keep every identifier and the meaning of every requirement. Never add, drop or reinterpret a requirement while reformatting; if wording is ambiguous, keep the original text and record an open question OQ-... instead.
2. Create TEMPLATE.md with one entry format: identifier (FR-001), status (confirmed, default, assumption, AI proposal, open, delegated, draft), requirement as one sentence in the format from the defaults, rationale or source, acceptance criteria in the format from the defaults (AC-001, ...), references to related identifiers (ADR, SEC, T, WP), open questions. Keep the template short and add one filled example.
3. If requirements exist, convert them to the template. Unclear or missing acceptance criteria stay visible as draft or open question; do not invent them.
4. Never reassign identifiers. Do not invent facts or requirements.
5. Converse in the user's language. Identifiers, file names and code stay English.
6. Do not set up tooling, install packages, implement, push or publish.

## Result
Create docs/requirements/TEMPLATE.md and, if requirements exist, the converted requirements in their file, plus a list of items that need clarification. If you cannot write files, give the complete Markdown and state clearly that nothing was saved.
````
