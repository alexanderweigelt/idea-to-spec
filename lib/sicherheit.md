# Projektbezogene Sicherheit

## Anleitung

**Ziel:** Aus den tatsächlichen Risiken konkrete Sicherheitsanforderungen und Nachweise ableiten.

**Liest:** Umfang, Daten und Integrationen; Anforderungen und ARCHITECTURE.md, falls vorhanden.

**Ergebnis:** SECURITY.md mit Bedrohungsmodell, SEC-Anforderungen und geplanten Nachweisen.

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

TASK — PROJECT SECURITY
Output: SECURITY.md.
Input: scope, assets, data, integrations and technical context; requirements,
architecture and diagrams when present.

Derive security from actual assets, entry points, data, actors, trust boundaries
and deployment. A static site still has browser, transport, dependency and
publication risks. Do not invent authentication, storage or services.

Keep one threat model here. Each T ID names components or flows, threat,
consequence, mitigating SEC IDs and remaining gap. Use STRIDE for plausible
abuse, not as a checklist. Reference existing diagrams and
record needed corrections in their owner; draw no competing diagrams.

Each SEC record has a measurable criterion, enforcement point, test or manual
evidence, blocking gate and, where a standard backs it, a verified OWASP ASVS
5.0.0 ID. Select only what the risks need; no level, quota or full matrix.
Verify IDs and text against
https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.json
If it is unreachable, keep the mapping draft and record the gap. Note considered
areas and why absent capabilities exclude controls; a missing required control is
a gap, not not-applicable.

Assess where applicable: CSP, nosniff, Referrer-Policy, framing and origin
policy; input and output handling; identity, authorization and sessions;
sensitive data, storage and logging; resource limits; HTTPS with HSTS for
production responses (local HTTP proves nothing); secret scanning, dependency
audit, release and vulnerability handling. Assess product AI only if the product
contains it. Tests inspect served responses and negative cases, not copied
configuration. Manual gates name owner, procedure and evidence. Release requires
verified criteria and resolved material blockers; a changed goal needs a reason
and updated owners, never a claim that a failed criterion passed.
Check every T and SEC for owner, references and planned verification.
Writable: SECURITY.md, needed corrections in ARCHITECTURE.md or docs/adr/,
docs/clarifications.md.
```
