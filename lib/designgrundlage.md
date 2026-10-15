# Designgrundlage

## Anleitung

**Ziel:** Eine konsistente, zugängliche Gestaltung für die bestätigten Nutzeraufgaben festhalten.

Nutze Anforderungen und vorhandene Gestaltung. Der Agent leitet passende Vorschläge ab und entscheidet innerhalb deiner Delegation.

**Eingaben:** Anforderungen, bekannte Nutzeraufgaben und verfügbare Assets.

**Ergebnis:** DESIGN.md mit Tokens, Komponentenregeln und prüfbaren Gestaltungskriterien.

## Kopierbarer Prompt

```text
COMMON CONTRACT — PL-WEB-4.0
Apply this embedded contract to browser-based websites, web applications and PWAs.
Work in the project directory; Git and hosted services are optional.
Check file, source and command access first.
Run only the requested task, in this or a fresh session. Inspect the filesystem
for relevant artifacts and read them and the journal when present; do not depend
on chat history. Create or update this task's own output artifact. Paths below
are defaults; reuse equivalent existing project documents.
Clarify missing essential information; no other library prompt is a prerequisite.
Skip inapplicable concerns and documents instead of creating them for completeness.
Use the user's language for conversation and choices; inherit the documentation
language, otherwise use the user's language. Keep identifiers in English.

DECISIONS AND CONTINUITY
Research and execute settled work autonomously; reuse answers.
For each open project decision, ask one choice: two or three options, consequences
and recommendation; use clickable UI when supported. Decide only within explicit,
recorded decision delegation; start/continue permission is not delegation.
Accept only user answers or in-scope delegated decisions, never preselection.
Offer delegation/pause; free text only for unsuitable options or essential details.
Keep or initialize docs/clarifications.md with delegation scope, explicit permissions
and limits with their human source, active question, question IDs/owner locations,
answers with basis, unresolved topics, task status and next useful action.
Record permissions when granted or changed; the journal preserves authority,
but cannot create it. Never infer commit, push or publication rights from a draft.
Use UNKNOWN with OQ references for gaps. Distinguish supplied facts, observations,
proposals and delegated decisions. Base question premises and recommendations on
cited evidence; label assumptions and clarify decisive missing facts first.
Never invent historical facts.
Before pausing save the next step. On resume read this journal and relevant owners.
Close a question only after updating its owner and checking affected references.

OWNERS AND CHANGE
For new product requirements use docs/requirements/FR-*.md and REQUIREMENTS.md
as their linked overview; preserve equivalent existing owners and formats.
Keep existing FR, AC, OQ, ADR, SEC, T and FIND IDs stable.
DESIGN.md owns presentation; ARCHITECTURE.md and ADRs own technical decisions
and diagrams; SECURITY.md owns controls and the single threat model.
README.md navigates; AGENTS.md carries short engineering rules and real commands.
Use project artifacts and activities in project files, not library identifiers
or instructions to run another prompt. Do not duplicate rules or invent features.
For each later implementation slice review affected FRs, tests, specialist owners
and, when present, README.md's phase notice or owner table.
Update changed specifications and necessary tests in the same PR or local slice;
an unchanged correct FR need not be edited just because code changed.
Record this review as a PR checklist item or local review note, not a blocking
file-change quota. Structural ID/reference checks remain blocking.
Use UTF-8 Markdown, one title, unique IDs and working relative file references.
Make small reviewable slices; create PRs or external artifacts only when authorized.
These templates produce specifications and plans, not implementation or setup.
Implementation needs a separate request; planning or issue-publication authority
never authorizes it. Local projects require no hosted repository.

GOALS, CRITERIA AND EVIDENCE
For goals addressed by this task record goal -> measurable criterion -> evidence
-> gate -> versioned primary source in the responsible file. Agent instructions
summarize applicable gates when present.
Goals: correct specified behavior, secure delivery and data handling,
maintainable code and reproducible changes; usable accessible interaction where
there is a user interface. Apply only standards and checks relevant to the scope.
For user interfaces target WCAG 2.2 AA, https://www.w3.org/TR/WCAG22/; automated
route/state scans complement owned manual checks.
Use OWASP ASVS 5.0.0 to derive project-specific SEC requirements from actual
assets, entry points, data and trust boundaries. No universal ASVS level or
full-control matrix is required. Record selection rationale and gaps; small
projects still assess browser, transport, supply-chain and delivery risks.
Verify selected IDs and control text against the primary versioned JSON:
https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.json
Pinned source SHA-256: bcdbec214d70abcfad9284a31d4f9e5134305831d628aad3aa85d7e26626cb35
This digest checks source integrity, not application compliance.
Use semantic WHATWG HTML, HTTP RFC 9110, TLS RFC 8446/9325 and applicable NIST
SSDF 1.1 practices. Use EARS-style requirements, Given/When/Then criteria,
Google DESIGN.md alpha at 9bf8eae67128b6cc55ad9bf86665767deb4c11cd,
arc42/C4, MADR 4.0.0 and OWASP Threat Modeling/STRIDE for the relevant artifacts.
For real APIs or embedded product AI, add relevant primary interface/security
specifications. AI-generated code requires the same review and checks.
Honor actual customer, legal and organizational obligations; map accessible
requirements to gates rather than implying ISO certification from norm names.

EXECUTABLE GATES
From agreed project goals and the actual stack derive applicable checks:
strict type/checkJs, lint, build, AC-linked tests, accessibility, delivered-response
security, secret scan and dependency audit. For applicable browser delivery tests,
check CSP, nosniff, Referrer-Policy and HTTPS/HSTS on responses, not just config.
Plan mandatory local checks and, when CI is used, blocking CI and supported hooks.
Document manual gates with owner, procedure and evidence; an installed or verified
gate requires later execution evidence, never a planning document alone.
Production readiness depends on verified project criteria and resolved blockers,
not a universal hosting feature list. Keep specified, implemented and verified
separate; report actual commands/results and anything not run or not applicable.
TASK CLOSE AND REVIEW
Record completed work, actual checks, gaps, review status, permissions and next
useful action in docs/clarifications.md. Save before a question or pause.
Summarize the diff and propose a task-scoped commit or PR when Git authority
exists; execute only within recorded authority and exclude unrelated changes.
State whether review was self-review or human review; do not invent approval.
Stop after the requested task. Do not launch another template or implementation
automatically. Preserve pending review status; reuse existing permission.
Saved files remain across sessions in the same checkout without a commit.
A different checkout needs an explicit transfer of any uncommitted work.
END COMMON CONTRACT

TASK — DESIGN FOUNDATION
Input: confirmed user tasks and scope, existing requirements, identity and assets.
If there is no user interface, report this task as inapplicable; do not create DESIGN.md.

Semantic HTML reference (Living Standard; record the read date):
https://html.spec.whatwg.org/multipage/

Create DESIGN.md from confirmed requirements and existing identity/assets.
Use Google DESIGN.md alpha at commit 9bf8eae67128b6cc55ad9bf86665767deb4c11cd:
https://github.com/google-labs-code/design.md/blob/9bf8eae67128b6cc55ad9bf86665767deb4c11cd/docs/spec.md
This experimental format is a design interchange convention, not an assurance
standard. Do not upgrade it silently. Preserve unfamiliar existing content.

Use optional YAML frontmatter bounded by ---: version: alpha, name, colors,
typography, spacing, rounded, components and justified omitted sections.
Colors are valid CSS values; dimensions use px/em/rem. Typography records actual
fontFamily/fontSize/fontWeight/lineHeight. Token references use {path.to.token}.
Tokens hold authoritative values; prose explains usage without contradictory
copies. Do not invent brand rules, research findings or unavailable assets.

Use these relevant body sections in order: Overview, Colors, Typography, Layout,
Elevation & Depth, Shapes, Components, Do's and Don'ts. Explain omitted sections.
Include only components and states required by known tasks: default, focus,
hover, disabled, loading, empty, success or error where they actually occur.
Record source/authority for design values; use the shared dialog for open
choices unless their decision scope was explicitly delegated.

Map accessibility goals to measurable criteria and checks in this file:
semantic names and roles, keyboard order and focus, normal-text contrast >=4.5:1,
large-text contrast >=3:1, applicable non-text contrast >=3:1, reflow/zoom,
non-color cues, target sizing and status announcements. Apply WCAG 2.2 A/AA to
complete pages and processes, not only individual widgets. Record automated
route/state scans plus manual keyboard, zoom, assistive-technology and content
checks with owners. An automated scan alone cannot prove full conformance.

Check token types/references, actual color pair contrast, section order and
requirement coverage. Record what was calculated, inspected or not run.
No application code, new product features or technology choices in this task.
Writable: DESIGN.md, design-related OQs in docs/clarifications.md;
provided assets only when the task authorizes their preparation.
```
