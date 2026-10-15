# P10 – Aufgabenplanung und Projektstart

## Anleitung

**Ziel:** Aus der Baseline umsetzbare Arbeitspakete ableiten und die Prüfgrundlage tatsächlich starten.

Der Agent erstellt zuerst einen lokalen Arbeitsplan. Das erste Paket richtet Werkzeuge und Prüfungen ein. Externe Issues entstehen nur im bereits freigegebenen Umfang.

**Eingaben:** Geprüfte Baseline, Anforderungen und konkreter Prüfvertrag.

**Ergebnis:** Arbeitspakete, eingerichtete lokale Prüfungen und CI-Konfiguration; autorisierte Issues bei entsprechender Freigabe.

**Danach:** Erstes freigegebenes Arbeitspaket umsetzen.

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

STAGE — P10 WORK PACKAGES AND EXECUTABLE START
Input check: P07 baseline report and actual Git-reference status, P08 README.md,
P09 AGENTS.md, and the specification owners referenced by the planned packages.

Read the reviewed specifications, AGENTS.md command contract and real baseline
reference. Stop dependent implementation if product blockers remain; preserve
useful local planning. If the baseline reference is pending, mark planning draft
and establish it only under existing Git authority. Do not invent completed PRs.

Create docs/work-plan.md with stable WP IDs, purpose, referenced FR/AC/SEC goals,
small implementation scope, dependencies, exact gate commands and evidence.
Cover the confirmed scope without new features or artificial package quotas.
Copy acceptance criteria by reference to the canonical FR, not into competing
rules. Include a review checkbox for affected FRs, tests and specialist owners;
update their content and coverage when needed, without mandatory file-edit quotas.
Identify a first vertical slice and subsequent meaningful increments.

WP-001 actually installs/configures the chosen runtime, dependencies/lockfile,
strict type/checkJs, lint/build, unit/browser tests, accessibility scans,
served-header tests, secret scan, dependency audit and lean spec/reference checks.
Install or verify the chosen runtime before creating/running the spec checker.
Use a dependency-free Node.js or Python 3 script for JSON record parsing, unique
FR/AC IDs, required criterion fields, local file references and listed test files.
Require actual test files for implemented criteria; planned bootstrap criteria
remain visibly pending. Use explicitly delivered package/criterion status for
implementation coverage; a ready FR marks specification readiness only.
No document hashes, profile schemas or file-edit quotas.
Run a deliberate invalid-reference fixture, then restore and rerun the valid set.
Update docs/baseline-review.md with results; any newly found blocker stops product
implementation until resolved. Configure blocking CI only after the commands exist,
and install supported local hooks. Use primary
tool documentation; avoid credentials in checked-in files.
Require these checks before merge in the selected repository where authorized;
verify the rule is active, otherwise report merge enforcement pending.
Test deliberate failures in disposable fixtures to show the other gates can block.
Missing application routes/tests at bootstrap mean pending coverage, never a
claimed passing AC.

For each route/state and AC identify the real test file and required positive,
negative/boundary scenarios. Accessibility automation is supplemented by owned
manual checks. Header tests exercise the actual server and later production
responses; production TLS/HSTS cannot pass merely because local HTTP works.
Run installed commands; repair failures and report result, environment and gaps.
Update AGENTS.md/README to distinguish working commands from pending checks.
Product features beyond the agreed bootstrap/first slice remain separate work.

Default to local planning. Prepare complete issue previews before any required
publication decision. Only with explicit existing authorization create external
issues in the specified repository and scope. Use a stable library-work-package
marker with project/WP ID in each body and docs/issue-map.md for URL/status.
Before creating, reconcile both the saved map and remote open/closed issues by
marker; never infer 'not created' from a lost response. If a timeout or partial
failure occurs, refetch the remote marker before retrying. Reuse/update matching
issues within authority; do not delete or recreate them silently.

Check coverage and acyclic dependencies; report real installs/gates versus
planned/manual/production checks. No deployment, merge, messaging or publication
outside existing authority. Writable: work plan, bootstrap/tool/test/CI files,
related owner updates, journal and issue map only when actually needed.
Next: implement the first ready package in a small reviewable slice.
```
