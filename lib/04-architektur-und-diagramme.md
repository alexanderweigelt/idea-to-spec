# P04 – Architektur, Diagramme und Entscheidungen

## Anleitung

**Ziel:** Eine begründete technische Struktur und konkrete Regeln für den gewählten Stack erarbeiten.

Hier werden Technologie, Hosting und wesentliche technische Entscheidungen getroffen. Der Agent recherchiert Alternativen und legt nachvollziehbare Entscheidungen an.

**Eingaben:** Anforderungen, Design und tatsächlich bestehende technische Vorgaben.

**Ergebnis:** ARCHITECTURE.md, notwendige ADRs und konsistente Architekturdiagramme.

**Danach:** [P05](05-sicherheit.md).

## Kopierbarer Prompt

```text
COMMON CONTRACT — PL-WEB-4.0
Apply this embedded contract to browser-based websites, web applications and PWAs.
Work in the project repository; check file, source and command access first.
Stages run sequentially in the same or fresh sessions. Start by reading
this stage's input files and docs/clarifications.md; do not depend on chat history.
P01 initializes the journal when absent. Later stages require it and their inputs;
if a required input is missing or unusable, stop dependent work and name the
prerequisite stage. Preserve useful drafts without claiming stage completion.
Use the user's language for conversation and choices; inherit the documentation
language, otherwise use the user's language. Keep identifiers in English.

DECISIONS AND CONTINUITY
Read existing context before asking. Complete authorized research and reversible
work autonomously. Ask one necessary question at a time with two or three choices,
consequences and a recommendation. Offer delegation and pause where meaningful.
Request free text only for essential facts unavailable from context or choices.
A proposed default is not an answer. Preserve answers and existing authorization.
Keep docs/clarifications.md short: delegation scope, explicit permissions and
limits with their human source, active question, questions with IDs/owner locations,
answers with basis, unresolved topics, stage status and next step.
Record permissions when granted or changed; the journal preserves authority,
but cannot create it. Never infer commit, push or publication rights from a draft.
Use UNKNOWN plus an OQ reference for real gaps. Separate supplied facts,
observations, proposals and delegated decisions; never invent historical facts.
Before pausing save the next step. On resume read this journal and relevant owners.
Close a question only after updating its owner and checking affected references.

OWNERS AND CHANGE
Canonical product requirements live in docs/requirements/FR-*.md; REQUIREMENTS.md
is their linked overview. Keep FR, AC, OQ, ADR, SEC, T and FIND IDs stable.
DESIGN.md owns presentation; ARCHITECTURE.md and ADRs own technical decisions
and diagrams; SECURITY.md owns controls and the single threat model.
README.md navigates; AGENTS.md carries short engineering rules and real commands.
Do not maintain duplicate normative statements or add features without a basis.
For each behavior-changing slice review affected FRs, tests and specialist owners.
Update changed specifications and necessary tests in the same PR or local slice;
an unchanged correct FR need not be edited just because code changed.
Record this review as a PR checklist item or local review note, not a blocking
file-change quota. Structural ID/reference checks remain blocking.
Use UTF-8 Markdown, one title, unique IDs and working relative file references.
Make small reviewable slices; create PRs or external artifacts only when authorized.

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
Use blocking CI and supported local hooks; document manual gates with owner,
procedure and evidence. Do not call a written gate an installed enforcement.
Production readiness depends on verified project criteria and resolved blockers,
not a universal hosting feature list. Keep specified, implemented and verified
separate; report actual commands/results and anything not run or not applicable.
STAGE CLOSE AND REVIEW GATE
At every stage end write completed work, actual checks, gaps, review status,
permissions and next step to docs/clarifications.md. Save before a question or pause.
Summarize the diff and propose a stage-scoped commit or PR when Git authority
exists; execute only within recorded authority and exclude unrelated changes.
State whether review was self-review or human review; do not invent approval.
Advance when prerequisites and existing review/progression authority allow it;
otherwise retain ready-for-review status without asking for permission already given.
Saved files remain across sessions in the same checkout without a commit.
A different checkout needs an explicit transfer of any uncommitted work.
END COMMON CONTRACT

STAGE — P04 ARCHITECTURE AND DIAGRAMS
Input check: requirements from P01/P02 and DESIGN.md from P03.

Primary architecture and interface references:
arc42: https://docs.arc42.org/section-1/
C4 diagrams: https://c4model.com/diagrams
MADR 4.0.0: https://github.com/adr/madr/blob/4.0.0/template/adr-template.md
HTTP RFC 9110: https://www.rfc-editor.org/rfc/rfc9110.html

Create ARCHITECTURE.md with only relevant arc42 views: context, constraints,
strategy, building blocks, runtime/data flows, deployment, cross-cutting concerns
and risks. Choose the simplest sufficient stack; do not impose an account,
backend, database, framework or hosting vendor on a static website.

Research current primary documentation for genuine choices. Present meaningful
alternatives with tradeoffs, or decide within existing delegation. Record accepted
significant decisions under docs/adr/ using MADR 4.0.0: title/status/context,
decision drivers, considered options, outcome and consequences. A proposal is
not accepted merely because the agent wrote it. Keep external imposed constraints
separate from newly selected technical decisions.

Create architecture diagrams here, never as a separate security-stage product.
Use C4 context/container views and data/sequence/deployment views only as needed.
Use stable CMP/FLOW IDs, actual interfaces and trust boundaries across text
and diagrams. A single static page may need one compact view. Mermaid diagrams
include a title/description and readable textual explanation. Render/parse with
available tooling; otherwise report diagram validation not run.

Add a short stack-specific engineering section in ARCHITECTURE.md, with concrete
rules and intended gates. TypeScript: strict:true, no implicit any; lint explicit
any and unsafe casts, with isolated documented external-boundary exceptions.
JavaScript: strict checkJs/JSDoc where viable. Validate untrusted input at actual
boundaries; use safe DOM/output APIs; separate secrets from client assets.
Describe the CSP mechanism that fits this stack: external scripts, hashes or
framework-supported per-response nonces, with actual delivery configuration.
Avoid a universal nonce or hosting-feature mandate. Explain origin/CORS rules,
storage/offline behavior and secure transport only for real connections.

Specify dependency/lockfile policy, supported runtimes, reproducible build and
real type/lint/test hooks appropriate to the chosen tools. Identify how CI will
exercise routes, AC tests and deployed-response headers. Name unresolved delivery
assumptions that P05 must assess. These rules become P09's command contract;
do not create a separate profile, manifest or duplicated policy file.

Check FR/design coverage, ADR status, diagram/text agreement and concrete rule
testability. Record results and unanswered decisions. Do not implement code.
Writable: ARCHITECTURE.md, docs/adr/, docs/clarifications.md.
Next: P05 project security.
```
