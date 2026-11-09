# AGENTS.md

Instructions for anyone – human or AI agent – working on this repository.

## Orientation

| Task | Read |
|---|---|
| Decide whether a change is right | [REQUIREMENTS.md](REQUIREMENTS.md) – the single benchmark of this project |
| Look up one requirement | `docs/requirements/<ID>.md` |
| Write a new requirement | [docs/REQUIREMENT_TEMPLATE.md](docs/REQUIREMENT_TEMPLATE.md) |
| Work on the prompts (the product) | [lib/](lib/README.md) |
| Understand IDs and the state of the specification | [README.md](README.md) (sections "IDs lesen" and "Specification") |

Open points are recorded as OQ in REQUIREMENTS.md, never in this file.

## Rules for collaboration

1. REQUIREMENTS.md is the benchmark and the blueprint; lib/ is generated from it. Never fix lib/ directly: adjust, add or remove requirements instead, preferring a careful change to an existing entry, so that a rebuild of lib/ meets every requirement again. Measure every change against REQUIREMENTS.md, not against the previous version.
2. Check first, then implement. If a request harms the goal, state your concern in one sentence and ask. The human decides.
3. Cause, not patch. When there is a problem, name the cause first. Rework the affected part instead of appending something.
4. No growth without reason. Before every addition, check whether something can be replaced or removed instead.
5. Complete passes, not micro-steps. Collect change requests and apply them in one pass, followed by a full check against REQUIREMENTS.md.
6. Restart signal. If a part has been patched twice, propose rebuilding it.
7. Do not tailor to the test project. Rules must apply in general; examples are symptoms, not the benchmark.

## Way of working

- Signal word "Zwischenfrage: …": add the point to the list in one sentence and keep working. No discussion and no implementation until the current work block is finished.
- One chat per work block. At the end, a compact handover (benchmark, rules, status, open interjections, next steps). In an incognito chat, everything needed must be in the handover.
- Questions of principle about the way of working belong in a separate chat.
- Test phase: after the project, the human decides which rules move into their global working rules.

## House rule

- Never record the name of the person who made a decision – not in this repository and not in anything produced with the prompts in lib/. Record the source as a role: user, given, standard or delegated.
