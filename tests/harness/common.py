"""Shared helpers: paths, config, copy block, ID patterns, results."""
import json
import re
from pathlib import Path

TESTS = Path(__file__).resolve().parent.parent
ROOT = TESTS.parent
LIB = ROOT / "lib"
REQ_DIR = ROOT / "docs" / "requirements"

ID_KINDS = ("FR", "AC", "OQ", "ADR", "SEC", "DES", "WP")
# Any ID-like token, also with a kind outside the allowed list (AC-REQ-03).
ID_LIKE = re.compile(r"\b([A-Z]{2,4})-([A-Z][A-Z0-9]*)-(\d{2})\b")


def load_config():
    return json.loads((TESTS / "config.json").read_text(encoding="utf-8"))


def copy_block(prompt_file):
    """Return the text between the ````text fences of a lib prompt, unchanged (AC-FLOW-06)."""
    lines = Path(prompt_file).read_text(encoding="utf-8").splitlines()
    starts = [i for i, l in enumerate(lines) if l.strip() == "````text"]
    if len(starts) != 1:
        raise ValueError(f"{prompt_file}: expected exactly one ````text block, found {len(starts)}")
    s = starts[0]
    for j in range(s + 1, len(lines)):
        if lines[j].strip() == "````":
            return "\n".join(lines[s + 1:j])
    raise ValueError(f"{prompt_file}: ````text block not closed")


def check(results, cid, ac, ok, detail="", level="fail"):
    """Append one check result. level: 'fail' blocks, 'warn' only reports."""
    results.append({
        "id": cid, "ac": ac,
        "status": "pass" if ok else level,
        "detail": detail,
    })
    return ok


def ac_text(ac_id):
    """Gherkin text of an AC from docs/requirements (for the judge)."""
    for f in sorted(REQ_DIR.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        m = re.search(r"^### " + re.escape(ac_id) + r"\s*\n```gherkin\n(.*?)\n```", t, re.M | re.S)
        if m:
            return m.group(1).strip()
    raise KeyError(f"{ac_id} not found in {REQ_DIR}")
