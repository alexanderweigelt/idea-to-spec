"""Cut generated files out of the model's text answer and check them (no AI, no cost)."""
import re

from .common import ID_KINDS, ID_LIKE, check

PATH = re.compile(r"([\w.\-/]*[\w\-]+\.md)\b")
FENCE = re.compile(r"^(`{3,}|~{3,})\s*([\w-]*)\s*$")


def extract_files(text):
    """Find code blocks preceded (within 3 lines) by a file path. Handles ```gherkin inside ```markdown."""
    lines = text.splitlines()
    files = {}
    i = 0
    while i < len(lines):
        m = FENCE.match(lines[i])
        if not m:
            i += 1
            continue
        fence, lang = m.group(1), m.group(2)
        path = None
        for k in range(i - 1, max(-1, i - 4), -1):
            pm = PATH.search(lines[k].replace("`", " ").replace("*", " "))
            if pm:
                path = pm.group(1).lstrip("./")
                break
        depth, j = 0, i + 1
        while j < len(lines):
            mj = FENCE.match(lines[j])
            if mj and mj.group(1)[0] == fence[0] and len(mj.group(1)) >= len(fence):
                if mj.group(2):          # nested opener like ```gherkin
                    depth += 1
                elif depth:
                    depth -= 1
                else:
                    break
            j += 1
        if path and lang in ("", "markdown", "md"):
            files[path] = "\n".join(lines[i + 1:j])
        i = j + 1
    return files


def find(files, suffix):
    for p, c in files.items():
        if p == suffix or p.endswith("/" + suffix):
            return c
    return None


def check_outputs(files):
    r = []
    req = find(files, "REQUIREMENTS.md")
    check(r, "out:requirements", "AC-USE-03", req is not None, "REQUIREMENTS.md nicht als Text ausgegeben")
    check(r, "out:template", "OQ-REQ-05", find(files, "REQUIREMENT_TEMPLATE.md") is not None,
          "docs/REQUIREMENT_TEMPLATE.md fehlt")
    reqfiles = {p: c for p, c in files.items() if "requirements/" in p and not p.endswith("TEMPLATE.md")}
    check(r, "out:req-files", "AC-SPEC-12", bool(reqfiles), "keine Datei docs/requirements/<ID>.md")

    # File name is the pure ID (OQ-SPEC-07)
    bad = [p for p in reqfiles if not re.fullmatch(r"(FR|SEC|DES)-[A-Z][A-Z0-9]*-\d{2}\.md", p.split("/")[-1])]
    check(r, "out:file-names", "OQ-SPEC-07", not bad, f"{bad}")

    # At most about 40 lines (AC-SPEC-13): warn above 40, fail above 45
    long_ = {p.split("/")[-1]: c.count("\n") + 1 for p, c in reqfiles.items() if c.count("\n") + 1 > 40}
    check(r, "out:length", "AC-SPEC-13", not any(v > 45 for v in long_.values()), f"{long_}")
    if long_ and not any(v > 45 for v in long_.values()):
        check(r, "out:length-40", "AC-SPEC-13", False, f"{long_}", level="warn")

    # Each FR has an AC as gherkin block, one step per line (AC-REQ-02, OQ-REQ-06)
    no_ac, bad_g = [], []
    for p, c in reqfiles.items():
        blocks = re.findall(r"^### AC-[A-Z][A-Z0-9]*-\d{2}\s*\n```gherkin\n(.*?)\n```", c, re.M | re.S)
        if not blocks:
            no_ac.append(p.split("/")[-1])
        for b in blocks:
            steps = [l.strip().split(" ")[0] for l in b.splitlines() if l.strip()]
            if not {"Given", "When", "Then"} <= set(steps) and not {"Angenommen", "Wenn", "Dann"} <= set(steps):
                bad_g.append(p.split("/")[-1])
    check(r, "out:ac-gherkin", "AC-REQ-02 OQ-REQ-06", not no_ac and not bad_g,
          f"ohne AC: {no_ac} Gherkin unvollständig: {bad_g}")

    # Only allowed ID kinds, form KIND-GROUP-NN (AC-REQ-03, AC-REQ-04)
    alltext = "\n".join(files.values())
    kinds = sorted({m.group(1) for m in ID_LIKE.finditer(alltext)} - set(ID_KINDS))
    check(r, "out:id-kinds", "AC-REQ-03", not kinds, f"fremde ID-Arten: {kinds}")
    readme = find(files, "README.md")
    if readme is not None:
        groups = {m.group(2) for m in ID_LIKE.finditer(alltext) if m.group(1) in ID_KINDS}
        unexplained = sorted(g for g in groups if not re.search(r"\|\s*`?" + g + r"`?\s*\|", readme))
        check(r, "out:groups-explained", "AC-REQ-04", not unexplained, f"Gruppen nicht in „IDs lesen“: {unexplained}")
    check(r, "out:readme-sections", "OQ-SPEC-07", readme is not None
          and re.search(r"^#+ .*(IDs lesen|Reading IDs)", readme, re.M) is not None
          and re.search(r"^#+ .*(Specification|Spezifikation)", readme, re.M) is not None,
          "README.md mit „IDs lesen“ und „Specification“ fehlt")

    # References are links whose visible text is only the ID (AC-SPEC-09)
    bare = {}
    for p, c in files.items():
        if p.endswith("TEMPLATE.md") or p.endswith("README.md"):
            continue
        t = re.sub(r"```.*?```", "", c, flags=re.S)
        t = "\n".join(l for l in t.splitlines() if not l.lstrip().startswith("#"))
        t = re.sub(r"<a id=\"[^\"]*\"></a>\*\*[A-Z]+-[A-Z0-9]+-\d{2}\*\*", "", t)
        t = re.sub(r"\[([A-Z]+-[A-Z0-9]+-\d{2})\]\([^)]+\)", "", t)
        own = p.split("/")[-1][:-3]
        ids = [m.group(0) for m in ID_LIKE.finditer(t) if m.group(0) != own]
        if ids:
            bare[p.split("/")[-1]] = sorted(set(ids))[:5]
    check(r, "out:links", "AC-SPEC-09", not bare, f"IDs ohne Link oder mit Zusatztext: {bare}")

    if req is not None:
        # Catalog: ID | Group | Title | Status with draft/confirmed (AC-SPEC-08)
        rows = [l for l in req.splitlines() if l.startswith("|")]
        hdr = next((i for i, l in enumerate(rows) if re.match(r"\|\s*ID\s*\|", l)), None)
        ok, detail = hdr is not None, "kein Katalog mit Spalte ID"
        if ok:
            cols = [c.strip() for c in rows[hdr].strip("|").split("|")]
            vals = [l.strip().strip("|").split("|")[-1].strip() for l in rows[hdr + 2:] if re.match(r"\|\s*\[?[A-Z]+-", l)]
            ok = len(cols) == 4 and all(v in ("draft", "confirmed") for v in vals) and bool(vals)
            detail = f"Spalten {cols}, Status {sorted(set(vals))}"
        check(r, "out:catalog", "AC-SPEC-08", ok, detail)

        # OQ as checkbox list with anchor, no status field (OQ-SPEC-06)
        oq_lines = [l for l in req.splitlines() if re.search(r"\*\*OQ-[A-Z0-9]+-\d{2}\*\*", l)]
        bad = [l[:60] for l in oq_lines if not re.match(r"\s*- \[[ x]\] (assumption: )?<a id=\"oq-[a-z0-9]+-\d{2}\"></a>", l)
               and not re.match(r"\s*- \[[ x]\] <a id=", l)]
        status_field = re.search(r"^\s*-\s*status:", req, re.M | re.I) is not None
        check(r, "out:oq-format", "OQ-SPEC-06", oq_lines and not bad and not status_field,
              f"falsch: {bad[:3]} status-Feld: {status_field}" if oq_lines else "keine OQ gefunden")

    # Source is a role (AC-DIALOG-02, part that a script can see)
    srcs = re.findall(r"source:\s*([^\n;,.)]+)", alltext, re.I)
    bad = sorted({s.strip() for s in srcs
                  if not re.fullmatch(r"(user|given|standard|delegated)(\s*\|.*)?", s.strip(), re.I)})
    check(r, "out:source-role", "AC-DIALOG-02", not bad, f"Quellen, die keine Rolle sind: {bad[:5]}")
    return r
