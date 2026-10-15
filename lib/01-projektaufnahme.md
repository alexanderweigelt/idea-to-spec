# P01 – Projektaufnahme und Anforderungen

## Anleitung

**Ziel:** Aus der Projektidee eine fachliche, nachvollziehbare Anforderungsbasis erstellen.

Beginne mit der Idee und dem vorhandenen Kontext. Der Agent ermittelt bekannte Angaben selbst und klärt nur notwendige Lücken. Die gemeinsame Qualitätsgrundlage gilt bereits; konkrete Technik wird erst in P04 entschieden.

**Eingaben:** Projektidee, vorhandene Dateien und bekannte Nutzeraufgaben.

**Ergebnis:** REQUIREMENTS.md, erste Anforderungsdatensätze und ein kurzes Entscheidungsjournal.

**Danach:** [P02](02-anforderungsvorlage.md).

## Kopierbarer Prompt

```text
COMMON CONTRACT — PL-WEB-4.0
Apply this embedded contract to browser-based websites, web applications and PWAs.
Work in the project directory; Git and hosted services are optional.
Check file, source and command access first.
Stages run sequentially in the same or fresh sessions. Start by reading
this stage's input files and docs/clarifications.md; do not depend on chat history.
P01 initializes the journal when absent. Later stages require it and their inputs;
if a required input is missing or unusable, stop dependent work and name the
prerequisite stage. Preserve useful drafts without claiming stage completion.
Use the user's language for conversation and choices; inherit the documentation
language, otherwise use the user's language. Keep identifiers in English.

DECISIONS AND CONTINUITY
Research and execute settled work autonomously; reuse answers.
For each open project decision, ask one choice: two or three options, consequences
and recommendation; use clickable UI when supported. Decide only within explicit,
recorded decision delegation; start/continue permission is not delegation.
Accept only user answers or in-scope delegated decisions, never preselection.
Offer delegation/pause; free text only for unsuitable options or essential details.
Keep docs/clarifications.md short: delegation scope, explicit permissions and
limits with their human source, active question, questions with IDs/owner locations,
answers with basis, unresolved topics, stage status and next step.
Record permissions when granted or changed; the journal preserves authority,
but cannot create it. Never infer commit, push or publication rights from a draft.
Use UNKNOWN with OQ references for gaps. Distinguish supplied facts, observations,
proposals and delegated decisions. Base question premises and recommendations on
cited evidence; label assumptions and clarify decisive missing facts first.
Never invent historical facts.
Before pausing save the next step. On resume read this journal and relevant owners.
Close a question only after updating its owner and checking affected references.

OWNERS AND CHANGE
Canonical product requirements live in docs/requirements/FR-*.md; REQUIREMENTS.md
is their linked overview. Keep FR, AC, OQ, ADR, SEC, T and FIND IDs stable.
DESIGN.md owns presentation; ARCHITECTURE.md and ADRs own technical decisions
and diagrams; SECURITY.md owns controls and the single threat model.
README.md navigates; AGENTS.md carries short engineering rules and real commands.
Do not maintain duplicate normative statements or add features without a basis.
For each later implementation slice review affected FRs, tests, specialist owners
and whether README.md's phase notice or owner table changed.
Update changed specifications and necessary tests in the same PR or local slice;
an unchanged correct FR need not be edited just because code changed.
Record this review as a PR checklist item or local review note, not a blocking
file-change quota. Structural ID/reference checks remain blocking.
Use UTF-8 Markdown, one title, unique IDs and working relative file references.
Make small reviewable slices; create PRs or external artifacts only when authorized.
P01–P10 cover specification and work planning only. Initial setup is the first
planned package, WP-001; no template executes it or any other package.
Implementation needs a separate request. Planning or issue-publication authority
never authorizes implementation. Local projects require no hosted repository.

GOALS, CRITERIA AND EVIDENCE
For each project goal record goal -> measurable criterion -> evidence -> gate
-> versioned primary source in the responsible file. AGENTS.md summarizes gates.
Required goals: correct specified behavior, usable accessible interaction,
secure delivery and data handling, maintainable code and reproducible changes.
Accessibility target: WCAG 2.2 AA, https://www.w3.org/TR/WCAG22/; automated scans
cover all routes and relevant states, supplemented by owned manual checks.
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
arc42/C4, MADR 4.0.0 and OWASP Threat Modeling/STRIDE in their owning stages.
For real APIs or embedded product AI, add relevant primary interface/security
specifications. AI-generated code requires the same review and checks.
Honor actual customer, legal and organizational obligations; map accessible
requirements to gates rather than implying ISO certification from norm names.

EXECUTABLE GATES
After stack selection specify concrete strict type/checkJs, lint, build,
AC-linked unit/integration/browser tests, accessibility scans, deployed-response
header tests, secret scan and dependency audit commands. Test CSP, nosniff,
Referrer-Policy and production HTTPS/HSTS where applicable, not just config files.
Plan mandatory local checks and, when CI is used, blocking CI and supported hooks.
Document manual gates with owner, procedure and evidence; an installed or verified
gate requires later execution evidence, never a planning document alone.
Production readiness depends on verified project criteria and resolved blockers,
not a universal hosting feature list. Keep specified, implemented and verified
separate; report actual commands/results and anything not run or not applicable.
STAGE CLOSE AND REVIEW GATE
At every stage end write completed work, actual checks, gaps, review status,
permissions and next step to docs/clarifications.md. Save before a question or pause.
Summarize the diff and propose a stage-scoped commit or PR when Git authority
exists; execute only within recorded authority and exclude unrelated changes.
State whether review was self-review or human review; do not invent approval.
Advance only within P01–P10 when prerequisites and existing review authority allow
it. P10 stops after planning and authorized optional issue synchronization, even
under earlier general delegation. Record the separate implementation request as
the next step; never start WP-001 automatically. Preserve pending review status
without asking for permission already given.
Saved files remain across sessions in the same checkout without a commit.
A different checkout needs an explicit transfer of any uncommitted work.
END COMMON CONTRACT

STAGE — P01 PROJECT FOUNDATION
Input check: project idea or accessible existing product context, and project-directory access.
Reuse an existing journal; P01 creates it only when absent.

Create the product foundation without choosing a stack, hosting provider or
technical architecture. Read accessible project context and preserve known work.
Capture purpose, actors, intended outcomes, confirmed scope, exclusions and known
data/flows. Describe unknown facts as unknown; do not infer permissions from roles.

Create REQUIREMENTS.md with a short overview and links to canonical records.
Create docs/requirements/FR-*.md for known atomic behaviors now; do not postpone
canonical ownership until P02. Use a title plus one fenced JSON object containing:
id, title, status, statement, basis, source_refs, acceptance_criteria,
open_question_ids. status is draft or ready; basis is supplied, observed,
proposal or delegated. Each criterion contains id, given, when, then, test_refs.
test_refs is an array of relative paths from this record; it stays empty until
an actual test file exists. A ready record needs an observable criterion and
no unresolved implementation-blocking question. P02 refines this same format.
Use EARS-style trigger/response statements where a trigger is known.

Initialize docs/clarifications.md with actual delegation, active question,
OQ IDs, owner paths, known answers and the next step. A template example is not
an unanswered product question. Do not force an interview when the context
already establishes a decision. Technical questions belong to P04, unless an
existing externally imposed constraint must be recorded as a fact now.

Record accessibility, correctness, safety and maintainability as shared goals;
do not ask the user to pick standards or repeat the embedded contract. Later
owners turn these goals into project criteria and executable gates.
Resolve open product decisions through the shared selection dialog.
Preserve previously supplied content and identify any real contradiction.

Check scope coverage, unique FR/AC/OQ IDs, observable criteria and relative links.
Report which inputs were observed and which remain draft. Save the journal before
asking or pausing. Do not create application code or publish external artifacts.
Writable: REQUIREMENTS.md, docs/requirements/FR-*.md, docs/clarifications.md.
Next: P02 requirement template.
```
