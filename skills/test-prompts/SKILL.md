---
name: test-prompts
description: Test the prompts in lib/ against REQUIREMENTS.md – static check (free) and automatic scenario runs with a simulated user and a hard cost limit. Use when lib/ or a scenario changed, or when asked to test a prompt.
---

# Test the prompts

Works with any agent or by hand: every step is a plain shell command. The agent never takes part in the test conversations; only `tests/run.py` talks to the models, in separate message lists, so the tested prompt cannot see the hidden traps.

## Steps

1. **Stage 1 – static check (no AI, no cost).**
   `python tests/static_check.py`
   If it reports failures: stop and report them. No paid run while stage 1 fails (the script enforces this too).

2. **Cost estimate (no API call).**
   `python tests/run.py <scenario> --dry-run [--model <id>]`
   Show the estimate to the human and wait for their go-ahead before any paid run.

3. **Smoke test with the small model** (default model in `tests/config.json`).
   `python tests/run.py <scenario>`

4. **Target model, only after the human agrees.**
   `python tests/run.py <scenario> --model <id>`

5. **Report.** Read only `tests/runs/<latest>/summary.md` (not the transcripts – they cost tokens). Report: passed runs, unmet checks with their AC IDs and quotes, cost. The human reviews samples in `transcript.jsonl` and `outputs/`.

## In CI (GitHub Actions)

`.github/workflows/prompt-tests.yml` runs stage 1 on every push and pull request. Stage 2 runs only by hand (Actions → Prompt tests → Run workflow): dry run first, then smoke test, then target model. It signs in without an API key via Workload Identity Federation (repository variables `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`) and commits `tests/runs` to the branch. The run's summary appears on the workflow page.

## Rules

- Hard limits (`tests/config.json` → `limits_usd`) are never raised without the human's word.
- Requires `pip install -r tests/requirements.txt` and an API key in the environment (`ANTHROPIC_API_KEY`).
- Unchanged prompt + scenario + models → the script reuses the last result (`--force` to rerun).
- A new trap or project is a new folder in `tests/scenarios/` with `scenario.json` (prompt, INPUT, ACs for the judge), `persona.md` (what the simulated user wants and knows – never the trap) and `expected.md` (traps, expected finding, warning words – seen only by the judge after the run). No code change.
- Findings are fixed in REQUIREMENTS.md, never directly in lib/ (AGENTS.md).

## Scenarios

| Scenario | Prompt | Traps |
|---|---|---|
| `requirements-vereinskasse` | lib/requirements.md | platform limit (PWA in the App Store), legal consequence (receipt photos at a non-EU service) |
