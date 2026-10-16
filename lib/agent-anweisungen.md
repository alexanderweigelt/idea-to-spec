# Agent-Anweisungen

## Anleitung

**Ziel:** Kompakte Entwicklungsregeln und konkrete Prüfkommandos für die spätere Umsetzung festlegen.

**Liest:** ARCHITECTURE.md, SECURITY.md, DESIGN.md, docs/work-plan.md und vorhandene Prüfkonfiguration, soweit vorhanden.

**Ergebnis:** AGENTS.md mit Kommando- und Gate-Tabelle, bei Bedarf ein kurzer Verweis für den eingesetzten Agenten.

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

TASK — AGENT INSTRUCTIONS AND COMMANDS
Output: AGENTS.md, following https://agents.md/.
Input: agreed technical context and goals; architecture, security, design, work
plan and existing check configuration when present.

Write an agent-neutral AGENTS.md, normally <=100 lines and useful while coding:
short stack rules, where each kind of rule lives, real commands and mandatory
gates. Link owners instead of copying them or this contract; later work loads only
the FR and owner files relevant to the current change.
Rules for later work: with each change review the affected FRs, tests and owner
files and note it in the PR or local review (a correct FR stays unchanged; this
is no blocking file quota); update specifications and tests in the same change;
AI-generated code gets the same review and checks; follow docs/work-plan.md.

Command table: goal, exact command, when to run, blocking failure, evidence and
owner link. Choose from the goals and the stack: spec, ID and reference check;
type or checkJs check, lint and reproducible build; unit, integration and browser
tests with FR/AC references; accessibility scans of routes and states; CSP,
nosniff, Referrer-Policy and HTTPS/HSTS on served responses; secret scan and
dependency audit. Use real script names or exact targets, never "run security
checks"; a command that does not exist yet is pending. Give the reason for each
gate that does not apply.
Manual gates name owner, procedure, evidence and timing (keyboard, zoom, screen
reader, content, security and production checks). Plan local checks; add blocking
CI and hooks when chosen. Do not claim that a Markdown rule blocks anything.
If the current agent reads another entry file, add only a verified short pointer;
if discovery cannot be verified, say how to load AGENTS.md manually.
If README.md has a document table, add the AGENTS.md row.
Check gate coverage of the goals, agreement of commands and configuration, and length.
Writable: AGENTS.md, a short agent pointer file, the AGENTS.md row in README.md,
docs/clarifications.md.
```
