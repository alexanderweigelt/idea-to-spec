# Projekt-README

## Anleitung

**Ziel:** Eine stabile Einstiegsseite mit Projektzweck, Phase und Dokumentnavigation schaffen.

**Liest:** Projektzweck, Phase und die vorhandenen Projektdokumente.

**Ergebnis:** README.md mit Dokumententabelle.

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

TASK — PROJECT README
Output: README.md.
Input: project purpose, scope and phase, and the existing project documents.

Write README.md in the documentation language with this structure:

# <Project name>
<One short paragraph: purpose, users and confirmed scope.>

**Phase:** <specification / implementation / release>

## Documents

| Document | Purpose |
| --- | --- |
| [Requirements](REQUIREMENTS.md) | Product requirements |
| [Design](DESIGN.md) | Presentation and interaction |
| [Architecture](ARCHITECTURE.md) | Technical structure and diagrams |
| [ADRs](docs/adr/) | Architecture decisions |
| [Security](SECURITY.md) | Controls and threat model |
| [Specification review](docs/specification-review.md) | Review findings |
| [Baseline review](docs/baseline-review.md) | Reviewed specification state |
| [Work plan](docs/work-plan.md) | Packages and progress |
| [Clarifications](docs/clarifications.md) | Questions, decisions and current state |
| [Agent instructions](AGENTS.md) | Engineering rules and commands |

List only existing targets; adapt labels and paths. Change the page only when the
phase or the stable navigation changes. Keep baseline references, tasks, open
questions, progress and commands out of README.md; their owners hold them. Keep
useful existing content; claim no unavailable features, deployment or compliance.
Check the structure, phase, links and absence of volatile state.
Writable: README.md, docs/clarifications.md.
```
