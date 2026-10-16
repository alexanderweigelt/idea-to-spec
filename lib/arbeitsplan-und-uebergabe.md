# Arbeitsplan

## Anleitung

**Ziel:** Die Spezifikation in prüfbare Arbeitspakete mit Abhängigkeiten und geplanten Prüfungen zerlegen.

**Liest:** Anforderungen, technische Entscheidungen und Rahmenbedingungen; Reviews und AGENTS.md, falls vorhanden.

**Ergebnis:** docs/work-plan.md mit Paketen, Abhängigkeiten, Zuordnung zu Kriterien und geplanten Prüfungen.

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

TASK — WORK PLAN
Output: docs/work-plan.md.
Deliver work packages only. Creating issues is outside this task.
Input: agreed scope, requirements, technical decisions and delivery constraints;
reviews and AGENTS.md when present.

PACKAGE CUT
Requirements and packages may relate many-to-many.
Start from one package per FR with its SEC criteria; merge FRs only when they
cannot be accepted separately. Split when removing some ACs leaves an outcome
that would be accepted on its own; keep failure, boundary and permission cases
with their outcome. If an FR splits into independent groups, record a
specification finding. Each package is accepted as one coherent PR or local
review. Do not cut by UI, API or data layer, or per criterion. A mechanism that
several packages need is a prework package with its own check and named
dependants. Plan an investigation only when a technical unknown blocks the cut:
question, evidence, exit; it never settles a product decision. Size figures are
hints, not limits. When the cut depends on an unsettled priority, ask one bundled
choice.

PACKAGES
Each package has a WP ID, goal, scope and exclusions, FR/AC/SEC references,
affected CMP IDs, dependencies, priority, status and planned checks. When an AC
spans packages, name the package that completes it. Each planned check gives the
command or manual procedure, the IDs or technical condition it covers and the
expected result. List technical subtasks only where order or handover needs them.
A package is done when its checks actually return the expected results and the
ACs it completes pass. Link criteria instead of copying them. Packages that depend
on open decisions stay draft; the others can be ready.

SETUP
WP-001 starts the setup and may be split into further setup packages under the
same rules. Plan only the environment, minimal structure and checks the goals
need; an existing project gets an adjustment plan, not a reset. A needed spec
checker is dependency-free Node.js or Python 3 with its runtime noted. Plan CI and
hooks only when chosen.

CHECK AND STOP
Check that every in-scope AC is completed by a package or listed as a gap, that
dependencies are acyclic and that all IDs resolve. Keep existing delivery evidence
on repeat runs. Write the next step
as a separate implementation request for WP-001.
Writable: docs/work-plan.md, docs/clarifications.md. Do not install, scaffold,
create test or CI files, run setup or product commands, or begin any package.
```
