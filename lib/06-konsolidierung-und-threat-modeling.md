# P06 – Konsolidierung und Modellreview

## Anleitung

**Ziel:** Die Fachdateien auf Konsistenz, prüfbare Ziele und verbleibende Lücken prüfen.

Reviewe die vorhandenen Fachdateien zusammen. Die bestehende Bedrohungsanalyse wird geprüft und verbessert, nicht ein zweites Mal angelegt.

**Eingaben:** Anforderungen, Design, Architektur, Sicherheit und offene Fragen.

**Ergebnis:** Abgeglichene Fachdateien und kurze, nachvollziehbare Reviewbefunde.

**Danach:** [P07](07-entscheidungen-und-baseline.md).

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

STAGE — P06 CONSOLIDATION AND THREAT-MODEL REVIEW
Input check: canonical requirements, DESIGN.md, ARCHITECTURE.md/ADRs and SECURITY.md from P01–P05.

Review the existing specification set without adding another policy layer.
Check canonical FR records against REQUIREMENTS.md links, DESIGN.md criteria,
ARCHITECTURE.md/ADRs and SECURITY.md's single threat model. Review only relevant
owners and dependencies; do not require rereading an entire standards catalogue.

Check each project goal's chain: goal, observable criterion, evidence, gate,
primary source. Find missing ownership, contradictory decisions, hidden assumed
features, dangling IDs and proposed commands that do not test their claimed
criterion. Ensure manual checks complement automation where required.
Confirm diagrams belong to architecture and SECURITY refers to the same flows.

Challenge the existing threat model with boundary/abuse scenarios. Review whether
selected ASVS IDs actually support each SEC goal; avoid translating a control
into a weaker criterion. Treat provider/tool limitations as project gaps when
an agreed requirement depends on them, not grounds for a blanket vendor mandate.
Confirm explicit small-project exclusions against actual absence of a capability.

Record FIND ID, severity, location, motivating problem, proposed fix, status and
evidence in a short review section of the owning file or journal. Fix reversible
consistency errors autonomously; changes to accepted behavior need existing
authority or one guided decision. Close a finding only after correcting its
owner and checking affected references. Do not silently downgrade a goal.

Describe who actually performed the review. Self-review is not an independent
assessment. Do not spawn another agent or send another task a message without
applicable authorization. Mark missing sources/checks as gaps, not success.

Check FR/AC uniqueness, links, threat-to-SEC coverage, goal-to-gate completeness
and coherent decision status. Separate implementation blockers from later runtime
or production evidence. Save the journal with the next useful step.
Writable: existing specification owners, FR records and docs/clarifications.md.
No new application code, profile, full matrix or external publication.
Next: P07 decisions and specification baseline.
```
