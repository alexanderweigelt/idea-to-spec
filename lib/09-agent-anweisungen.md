# P09 – Agent-Anweisungen und Prüfvertrag

## Anleitung

**Ziel:** Kompakte Entwicklungsregeln und konkrete Prüfkommandos für die weitere Umsetzung festlegen.

Die Architekturregeln und Projektziele werden in kurze, ausführbare Arbeitsanweisungen übersetzt. Das tatsächliche Laden durch den verwendeten Agenten wird geprüft.

**Eingaben:** Fachdateien, gewählter Stack und vorhandene Prüfkonfiguration.

**Ergebnis:** AGENTS.md mit Kommando- und Gate-Vertrag sowie bei Bedarf ein geprüfter Adapter.

**Danach:** [P10](10-arbeitsplan-und-uebergabe.md).

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

STAGE — P09 AGENT INSTRUCTIONS AND COMMAND CONTRACT
Input check: P07 baseline report, P08 README.md and the stack/goal owners from P03–P05.

Agent entry-file convention:
https://agents.md/

Write an agent-neutral AGENTS.md, normally <=100 lines. Keep it useful at code
time: short stack rules, owner-file routing, actual commands and mandatory gates.
Do not copy the whole common contract or ask the agent to read every document
for every edit. Load the FR and specialist owners relevant to the current task.

Carry P04's concrete engineering rules: strict types/checkJs, safe boundary
validation, safe output, CSP implementation, dependency/lockfile rules and
necessary framework conventions. Point to the owning architecture section.
Require a PR checklist item or local review note confirming review of affected
FRs, tests, specialist files and README.md's phase notice or owner table.
Update them when needed; a bug fix may leave an already correct FR unchanged. A source-file change without an FR edit is not
itself a blocking CI failure. Keep actual syntax/ID/reference failures blocking.

Create a command/gate table: goal, exact repository command, when to run,
blocking failure, evidence and source-owner link. Mandatory categories are:
- lean spec/ID/reference check; documentation impact is a review checklist item;
- strict type or checkJs check, lint and reproducible build;
- meaningful unit/integration plus browser tests with FR/AC references;
- automated accessibility scans for all routes/relevant states;
- served-response CSP, nosniff, Referrer-Policy and applicable HTTPS/HSTS tests;
- secret scan and dependency audit including build/test dependencies.
Use actual scripts or exact installation targets for the future WP-001, never placeholders such
as 'run security checks'. An unavailable command is pending, not passed. No
applicable gate is silently optional; name a reason for true nonapplicability.

Add manual gates with named owner, procedure, evidence location and timing:
keyboard/zoom/assistive-technology/content review, security/design review and
production delivery checks not possible locally. Local success cannot complete
these gates. Summarize release criteria without an ASVS level or vendor list.

Specify mandatory local checks; add blocking CI and supported hooks when those
mechanisms are chosen. Verify existing hook and agent discovery
against actual tools/primary documentation; do not claim a Markdown instruction
is a technical block. If the current agent uses another entry file, add only a
short verified pointer to AGENTS.md. If discovery cannot be verified, provide an
explicit manual load instruction and record that limitation.

Once AGENTS.md exists, add or update its README.md owner-table entry with a real
relative link and its stable purpose. Remove any superseded planned entry.
Do not copy command availability, stage progress or other volatile state there.

Check table-to-goal coverage, command/config agreement, <=100-line readability
and the README.md link to the existing AGENTS.md.
P10 only plans installation and gates in WP-001; keep their execution pending
until a separate implementation request actually performs that package.
State the scope boundary explicitly: no implementation, setup, tool installation
or planned package execution in P01–P10. A later implementation request loads
AGENTS.md and the work plan before starting WP-001.
Require later requests to read docs/clarifications.md, docs/work-plan.md and,
when linked, docs/issue-map.md before dependent edits, so recorded permissions,
tracking mode and unresolved conflicts survive a fresh session.
Follow the work plan's tracking rules, including synchronization when issues are
linked; local-only work requires no external service.
Report actual discovery/check results, not assumed integrations.
Writable: AGENTS.md, necessary short agent adapter, journal and the README.md
owner-table entry for AGENTS.md.
Next: P10 work planning and handoff; no implementation.
```
