# P05 – Projektbezogene Sicherheit

## Anleitung

**Ziel:** Aus den tatsächlichen Risiken konkrete Sicherheitsanforderungen und Nachweise ableiten.

Nutze die Architektur und ihre Diagramme. Sicherheitsziele gelten auch für kleine Websites; ihr konkreter Umfang folgt den tatsächlichen Angriffsflächen.

**Eingaben:** Anforderungen, Design, Architektur, Daten und Integrationen.

**Ergebnis:** SECURITY.md mit Projektzielen, Kontrollen, Prüfplan und einem Bedrohungsmodell.

**Danach:** [P06](06-konsolidierung-und-threat-modeling.md).

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

STAGE — P05 PROJECT SECURITY
Input check: requirements, DESIGN.md and ARCHITECTURE.md from P04; read its ADRs when relevant.

Primary security and secure-development references:
TLS RFC 8446: https://www.rfc-editor.org/rfc/rfc8446
TLS recommendations RFC 9325: https://www.rfc-editor.org/rfc/rfc9325.html
CSP guidance: https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html
HTTP headers: https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
NIST SSDF 1.1: https://csrc.nist.gov/pubs/sp/800/218/final
Threat modeling: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
STRIDE: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats

Create SECURITY.md from actual assets, entry points, resources, data, origins,
actors, trust boundaries and deployment. A static site still has browser,
transport, build/dependency and publication risks. Do not invent authentication,
persistence or services to fill a checklist.

Create one threat model here, using OWASP Threat Modeling and STRIDE as prompts
for plausible abuse, not mandatory sixfold duplication per element. Each T ID
links relevant components/flows, threat, consequence, mitigation SEC IDs and
remaining gap. Reference P04's diagrams; request changes in ARCHITECTURE.md when
the model discovers a real technical omission. Do not create competing diagrams.

Derive SEC goals from these risks. For each SEC record include measurable
criterion, enforcement location, test/manual evidence, blocking gate and primary
source with version and verified control ID. Verify selected ASVS 5.0.0 IDs and
text using the embedded URL and pinned digest; select as many controls as actual
project obligations need. No fixed level, quota or full catalogue is required.
Record considered risk areas and why absent capabilities exclude particular
controls. A missing required implementation is a gap, not not_applicable.
If source access fails, retain a draft mapping and the explicit verification gap.

Assess secure transport; browser delivery CSP, MIME/nosniff, referrer leakage,
framing and origin policies; actual input/output handling, identity/authorization,
sessions, sensitive data, storage, logging, resource limits and supply chain.
Set a project-appropriate Referrer-Policy with a sensitive-referrer criterion.
For relevant production HTTPS responses, define HSTS and TLS tests; local HTTP
is a development environment, not evidence that production transport passes.
Do not impose preload, ECH or hardware authentication without a project reason.

Include secret scanning, dependency review/audit, safe release and vulnerability
handling as applicable SSDF practices. For product AI assess its own boundaries;
AI-assisted coding alone does not imply an AI endpoint in the product.
Automated tests inspect served responses and negative cases, not just copied
configuration. Manual security gates need a named owner, procedure and evidence.
Release requires the agreed project criteria to be verified and material
blockers resolved. Explicit accepted changes to goals require rationale and
updated owners/gates, never a claim that a failed criterion passed.

Check every threat/SEC/reference for ownership and planned verification. Report
specified versus implemented/verified. No code or blanket conformity claim.
Writable: SECURITY.md, necessary architecture/ADR corrections and journal.
Next: P06 consolidation and threat-model review.
```
