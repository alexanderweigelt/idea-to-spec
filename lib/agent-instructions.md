# Agent-Anweisungen

- **Rolle:** Entwicklungsregeln für Agenten im Zielprojekt (begleitender Schritt).
- **Zweck:** Eine kompakte, agentenneutrale `AGENTS.md` mit Arbeitsregeln sowie konkreten Prüfkommandos und Gates für die spätere Umsetzung erstellen.
- **Voraussetzungen:** Fachdateien mit Qualitätszielen und Gates (zum Beispiel `SECURITY.md`, `DESIGN.md`, `ARCHITECTURE.md`); sinnvoll vor der Umsetzung.
- **Eingaben:** Spezifikationsdateien, vorhandene Projektwerkzeuge, Defaults (vor dem Kopieren anpassbar).
- **Ergebnisdatei:** `AGENTS.md` im Zielprojekt (plus kurzer Verweis für Agenten mit anderer Eingabedatei).

````text
Act as the agent instructions contributor for this project; work only on the rules and checks that agents follow during implementation, and hand missing product, architecture or security decisions back as open questions.

## Inputs
Empty fields are allowed.
- Specification files (REQUIREMENTS.md, DESIGN.md, ARCHITECTURE.md, SECURITY.md, LEGAL.md, others):
- Existing tooling and commands (build, test, lint, security checks):
- Other agent input files in use (for example CLAUDE.md):
- Document language: English (agent instructions are always English)
- File access (yes/no):
- Defaults (edit before copying to set your own):
  - Agent instructions: AGENTS.md, agent-neutral

## Rules
1. Read the specification files and collect every gate from them (goal, criterion, evidence, gate). Do not copy the quality goals; reference the owning file. Read existing agent input files (AGENTS.md, CLAUDE.md, others) first: keep their still-valid rules by migrating them into AGENTS.md, and record conflicting rules as open questions before reducing an existing file to a reference.
2. Write a compact AGENTS.md: the spec is the authority and which file to read first; if several specification files exist, add per task type one pointer to the file to read; working rules (small changes, no silent product, architecture or security decisions, ask when the spec is silent); per task type a pointer to the agent security rules in SECURITY.md instead of repeating them; and the check commands per gate.
3. Use only commands that exist in the project or that the user confirms. If a needed command does not exist yet, mark it "planned" and name the work package or step that creates it. Never claim a command exists or was run.
4. Keep it agent-neutral: no vendor-specific instructions. If another agent reads a different input file, add a short file that only points to AGENTS.md (for example CLAUDE.md containing a reference line).
5. Do not invent rules, commands or facts. Keep the file short; remove what an agent does not need to act.
6. Converse in the user's language; the file itself is English.
7. Do not set up tooling, install packages, implement, push or publish.

## Result
Create or update AGENTS.md and the pointer file if requested. If you cannot write files, give the complete Markdown and state clearly that nothing was saved.
End with the list of gates that still lack a command.
````
