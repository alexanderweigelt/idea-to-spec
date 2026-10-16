# AGENTS.md

Working instructions for agents on the "Idea to Spec" repository (version 1.0). They apply to work on this repository, not to projects created with its prompts.

## Authority
- `REQUIREMENTS.md` is the top-level source of requirements. If it conflicts with existing files in `lib/`, it wins.
- Existing prompts in `lib/` are material only until they are rebuilt from `REQUIREMENTS.md`.

## Rules for prompts (Q-003, Q-007)
- A prompt is a self-contained, copyable file in `lib/`. No prompt depends on another.
- There is no shared base text (no "COMMON CONTRACT").
- File names: English, lowercase, hyphenated, no numbers. Header in German, exactly one English prompt block, input block with named fields.
- Standards and quality goals live only in the responsible role prompt (Q-005, Q-006).
- No origin history, training references or provenance notes in prompts.
- Never invent identifiers, facts or check results (Q-002).

## Language and identifiers
- Descriptions and the guide are German. All instructions for agents (prompts, this file, CLAUDE.md), file names and code are English.
- Identifiers (FR, AC, OQ, ADR, SEC, T, WP) are never reassigned.
- The version is kept only in `lib/README.md`.

## Working style
- Read wording literally: "should" is optional, "must" is mandatory. Do not tighten.
- Weigh effort against benefit, choose the simplest solution, park details instead of losing them.
- Do not commit, push or delete files without an explicit request.
