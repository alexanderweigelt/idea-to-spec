# Architektur, Diagramme und Entscheidungen

## Anleitung

**Ziel:** Eine begründete technische Struktur und konkrete Regeln für den gewählten Stack erarbeiten.

Hier werden Technologie, Hosting und wesentliche technische Entscheidungen getroffen. Der Agent recherchiert Alternativen und legt nachvollziehbare Entscheidungen an.

**Eingaben:** Bestätigter Umfang und Anforderungen, bestehende technische Vorgaben; Gestaltung, falls relevant und vorhanden.

**Ergebnis:** ARCHITECTURE.md, notwendige ADRs und konsistente Architekturdiagramme.

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

TASK — ARCHITECTURE AND DIAGRAMS
Input: confirmed scope and requirements, technical constraints and existing system
context. Use design and security specifications when relevant and available.

Primary architecture and interface references:
arc42: https://docs.arc42.org/section-1/
C4 diagrams: https://c4model.com/diagrams
MADR 4.0.0: https://github.com/adr/madr/blob/4.0.0/template/adr-template.md
HTTP RFC 9110: https://www.rfc-editor.org/rfc/rfc9110.html

Create ARCHITECTURE.md with only relevant arc42 views: context, constraints,
strategy, building blocks, runtime/data flows, deployment, cross-cutting concerns
and risks. Choose the simplest sufficient stack; do not impose an account,
backend, database, framework or hosting vendor on a static website.

Research current primary documentation for genuine choices. Use the shared
selection dialog. Record significant decisions under docs/adr/ using MADR 4.0.0:
title/status/context, drivers, options, outcome and consequences. Set accepted
only after the user's answer or a recorded in-scope delegated decision; link it.
Keep externally imposed constraints separate from new technical decisions.

Keep architecture diagrams with their owning architecture description.
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

Specify applicable dependency/lockfile policy, supported runtimes and build/test
hooks appropriate to the chosen tools. If CI is used, describe its relevant checks.
Record unresolved delivery assumptions as open questions in the relevant owner. Keep engineering rules
here for reference from agent instructions; do not duplicate them in a policy file.

Check requirement and applicable design coverage, ADR status, diagram agreement and rule
testability. Record results and unanswered decisions. Do not implement code.
Writable: ARCHITECTURE.md, docs/adr/, docs/clarifications.md.
```
