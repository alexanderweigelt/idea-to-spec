# P07 – Entscheidungen und Spezifikationsbaseline

## Anleitung

**Ziel:** Blockierende Entscheidungen schließen und einen prüfbaren Startstand herstellen.

Der Agent nutzt bisherige Antworten und Delegationen, klärt verbleibende Entscheidungen und prüft die Spezifikation. Die Baseline erhält einen tatsächlichen Git-Bezug.

**Eingaben:** Konsolidierte Fachdateien, Entscheidungen und verfügbare Prüfwerkzeuge.

**Ergebnis:** Aktualisierte Fachdateien, dokumentierte manuelle Spezifikationsprüfung und ein kurzer Baselinebericht mit Prüfbedarf für P10.

**Danach:** [P08](08-readme.md).

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

STAGE — P07 DECISIONS AND SPECIFICATION BASELINE
Input check: consolidated owners and recorded findings from P06, plus docs/clarifications.md.

Read docs/clarifications.md and relevant owners. Reuse answers and delegation;
never restart the interview merely because this is a new session. Distinguish
missing facts from reversible choices. Resolve only real implementation blockers;
a later production check is not an unanswered specification decision.

For each answer write the outcome/basis into its owner, check dependants and
then close the OQ. Ask one consequential decision at a time with choices,
recommendation, delegation or pause. Preserve unresolved facts honestly.

Review specification structure manually now: canonical record readability and
JSON syntax, unique FR/AC IDs, required criterion fields, owner/reference
consistency and any already-listed test files. Empty test_refs before code exists
mean pending tests. Record the inspected records, method and actual findings.
Do not install a runtime, checker or CI here. P10/WP-001 installs the selected
runtime first, then creates/runs the dependency-free spec checker and CI.
Record automated verification as pending P10, not as a passed check.

Write docs/baseline-review.md with scope, actual commands/results, remaining
runtime checks, unresolved blockers and readiness. Baseline means a real Git
commit/tag (or the merged baseline PR commit) plus this report. Record the actual
reference; never invent a tag, merge or successful CI execution. Use existing
commit authority; if establishing a Git reference is not authorized/possible,
report ready for baseline with the reference pending. P10 must not claim it exists.
README/AGENTS may be added in P08/P09 without a separate immutable hash layer;
a changed specification gets a new reviewed Git reference.

Check each FR, goal, diagram, ADR and SEC against its owner, IDs and planned gates.
The manual baseline review establishes specification readiness; P10 automatic
checks may discover blockers and must update the report before product work.
Neither establishes code quality or production readiness by itself.

Do not create application functionality, publish issues or open empty PRs.
Writable: existing specifications/journal and docs/baseline-review.md.
Next: P08 project README.
```
