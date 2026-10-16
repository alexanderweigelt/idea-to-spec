# Projektaufnahme und Anforderungen

## Anleitung

**Ziel:** Aus der Projektidee eine fachliche, nachvollziehbare Anforderungsbasis erstellen.

**Liest:** Projektidee oder vorhandene Produktbeschreibung.

**Ergebnis:** REQUIREMENTS.md und docs/requirements/FR-*.md mit prüfbaren Akzeptanzkriterien und offenen Fragen.

## Kopierbarer Prompt

```text
COMMON CONTRACT — PL-WEB-5.0
Scope: browser-based websites, web applications and PWAs. Work in the project
directory; Git and hosted services are optional. Check file and command access first.
This prompt is self-contained and runs in a new or ongoing session. Read
docs/clarifications.md and the existing project files this task needs; do not rely
on chat history. No other prompt is required: clarify missing essential facts.
Skip concerns that do not apply. Paths are defaults; reuse equivalent documents.
Converse in the user's language, keep the existing documentation language and
write identifiers in English.

DECISIONS
Do settled and reversible work autonomously; reuse existing answers.
Ask each open project decision as one choice: two or three options with
consequences and a recommendation, plus delegate or pause; use clickable choices
when supported. Ask for free text only for essential facts.
Decide yourself only within explicit, recorded delegation; permission to start
is not delegation, and a proposal is not an answer.
Base recommendations on cited evidence, label assumptions, never invent facts.

JOURNAL
Keep docs/clarifications.md short: delegation scope, permissions with their human
source, open questions (OQ ID, owner file, answer, basis), task status, actual
checks, gaps and next useful action. Save it before asking, pausing or ending.
The journal records authority but cannot create it. Close a question only after
updating its owner file and the affected references.

OWNERS
Requirements: docs/requirements/FR-*.md, linked from REQUIREMENTS.md.
Presentation: DESIGN.md. Technical decisions and diagrams: ARCHITECTURE.md and
docs/adr/. Security controls and the single threat model: SECURITY.md.
Packages and progress: docs/work-plan.md. README.md navigates; AGENTS.md holds
short rules and real commands. Keep FR, AC, OQ, ADR, SEC, T, FIND and WP IDs
stable. Link owners instead of copying rules; do not invent features. Project
files use project terms, not template names. Use UTF-8 Markdown, one title,
unique IDs and working relative links.

REQUIREMENTS AND EVIDENCE
State each requirement as one unambiguous need with its source. Each FR criterion
names precondition, trigger and observable result (Given/When/Then). Every
in-scope failure, boundary or permission case that changes the outcome gets a
criterion or an OQ; there is no minimum count. A record is ready only when its
criteria cover its statement and no blocking OQ remains; a blocker holds back
only the affected scope.
Goals: correct behavior, secure delivery and data handling, maintainable and
reproducible code, and accessible use (WCAG 2.2 AA) where a user interface exists.
Record each goal this task touches as goal -> measurable criterion -> evidence ->
gate in its owner. Keep specified, implemented and verified apart. Report actual
commands and results; anything not run is pending, never passed. A plan or an
existing test file is not evidence of a passed check.

BOUNDARY AND CLOSE
These templates produce specifications and plans only. Setup and implementation
need a separate request; planning or publishing permission never grants it.
Create commits, PRs or other external artifacts only with recorded authority. At the end summarize the changes, state self-review or human review,
and propose a task-scoped commit or PR when Git authority exists. Stop after the
requested task.
END COMMON CONTRACT

TASK — PROJECT FOUNDATION
Output: REQUIREMENTS.md and docs/requirements/FR-*.md.
Input: the project idea or existing product context.

Capture purpose, actors, intended outcomes, confirmed scope, exclusions, known
data and flows, and imposed legal, contractual or technical constraints. Record
unknown facts as UNKNOWN with an OQ; do not infer permissions from roles. Do not
choose a stack, hosting or architecture.

REQUIREMENTS.md gives a short overview and links every record. Each new record
docs/requirements/FR-*.md has a title and one fenced JSON object with
id, title, status (draft|ready), statement, basis (supplied|observed|proposal|delegated),
source_refs, acceptance_criteria [{id, given, when, then, test_refs}] and
open_question_ids. Use one atomic behavior per record, EARS-style where a trigger
is known. test_refs lists only existing test files and stays empty until then.
Keep a suitable existing format.

Resolve open product decisions with the choice dialog; do not ask about what the
context already settles. A template example is not a product question. Preserve
existing content and name real contradictions.
Check scope coverage, unique IDs, links and every ready record against the
readiness rule.
Writable: REQUIREMENTS.md, docs/requirements/FR-*.md, docs/clarifications.md.
```
