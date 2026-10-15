# Entscheidungen und Spezifikationsbaseline

## Anleitung

**Ziel:** Blockierende Entscheidungen schließen und einen prüfbaren Startstand herstellen.

Der Agent nutzt bisherige Antworten und Delegationen, klärt verbleibende Entscheidungen und prüft die Spezifikation. Mit Git erhält die Baseline einen tatsächlichen Commit-Bezug, sonst einen datierten lokalen Reviewstand.

**Eingaben:** Zu prüfende Spezifikationen, bestätigter Umfang und vorhandene Entscheidungen oder Befunde.

**Ergebnis:** docs/baseline-review.md mit manuellem Prüfergebnis und offenem Prüfbedarf; nötige Korrekturen an bestehenden Fachdateien.

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

TASK — DECISIONS AND SPECIFICATION BASELINE
Input: specifications to baseline, agreed scope and existing decisions or findings.

Read the journal when present and relevant owners. Reuse answers and delegation;
never restart the interview merely because this is a new session. Distinguish
missing facts from reversible choices. Resolve only real implementation blockers;
a later production check is not an unanswered specification decision.

For each answer write the outcome/basis into its owner, check dependants and
then close the OQ. Ask one consequential decision at a time with choices,
recommendation, delegation or pause. Preserve unresolved facts honestly.

Review the supplied specification structure manually: record readability and
applicable syntax/IDs, required criteria, owner/reference consistency and
any already-listed test files. Empty test_refs before code exists
mean pending tests. Record the inspected records, method and actual findings.
Do not install a runtime, checker or CI here. Record required runtime checks as
pending implementation work, including any runtime prerequisites. A plan is not
a passed automatic check.

Write docs/baseline-review.md with scope, actual review methods/results, remaining
runtime checks, unresolved blockers and readiness. With Git, reference a real
commit/tag or merged baseline commit under existing Git authority; never invent
it. If the reference is pending, record why and how to verify it in the journal;
it can be filled once the actual commit is known. Without Git, use a dated
manual specification-review checkpoint naming the reviewed files and limitations;
do not claim immutable Git history or block local planning because Git is absent.
Distinguish a valid local checkpoint from a pending Git reference.
Navigation or agent instructions can be added without a separate immutable hash
layer; a changed specification gets a new reviewed reference or local checkpoint.

Check each FR, goal, diagram, ADR and SEC against its owner, IDs and planned gates.
The manual baseline review establishes specification readiness. Automatic checks
remain pending the separately authorized setup; new blockers must update this report
and be resolved before product work continues.
Neither establishes code quality or production readiness by itself.

Do not create application functionality, publish issues or open empty PRs.
Writable: existing specifications/journal and docs/baseline-review.md.
```
