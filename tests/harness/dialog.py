"""Dialog checks a script can count, plus the leak check for the hidden trap.

The counts are heuristics on free text; the judge checks the same ACs with quotes.
"""
import re

from .common import check

RECOMMENDED = re.compile(r"\((empfohlen|recommended|Empfehlung)\)|\bempfohlen\b|\brecommended\b", re.I)
NUMBERED = re.compile(r"^\s*(\*\*)?\d+[.)]\s+\S")


def check_dialog(turns, status):
    """turns: list of AI messages before the final result. status: how the conversation ended."""
    r = []
    check(r, "dlg:has-dialog", "AC-DIALOG-01 FR-DIALOG-02", len(turns) >= 1,
          "kein Dialog: Ergebnis sofort ohne eine Frage")
    check(r, "dlg:ends", "FR-DIALOG-07", status != "max_rounds",
          "Endlosgespräch: Rundengrenze ohne Endergebnis erreicht")
    too_many, no_rec, no_list = [], [], []
    for n, t in enumerate(turns, 1):
        if "?" not in t:
            continue
        recs = len(RECOMMENDED.findall(t))
        if recs > 3:
            too_many.append(n)
        if recs == 0:
            no_rec.append(n)
        head = t.split("?")[0].splitlines()
        if sum(1 for l in head if NUMBERED.match(l)) < 2:
            no_list.append(n)
    check(r, "dlg:max-3-questions", "AC-DIALOG-09", not too_many, f"Runden mit mehr als 3 Empfehlungen: {too_many}", level="warn")
    check(r, "dlg:recommendation", "AC-DIALOG-07", not no_rec, f"Fragerunden ohne markierte Empfehlung: {no_rec}", level="warn")
    check(r, "dlg:topic-list", "AC-DIALOG-19", not no_list, f"Runden ohne nummerierte Themenliste vor der ersten Frage: {no_list}", level="warn")
    return r


def mentions(text, words):
    low = text.lower()
    return [w for w in words if w.lower() in low]


class LeakGuard:
    """A user message that names a warning word before the AI raised that trap contaminates the run."""

    def __init__(self, traps):
        self.traps = traps                    # {trap_id: [warn words]}
        self.raised = {t: False for t in traps}

    def ai_said(self, text):
        for t, words in self.traps.items():
            if mentions(text, words):
                self.raised[t] = True

    def user_said(self, text):
        for t, words in self.traps.items():
            hit = mentions(text, words)
            if hit and not self.raised[t]:
                return f"{t}: Nutzer nannte {hit} bevor die KI das Thema ansprach"
        return None
