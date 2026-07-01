#!/usr/bin/env python3
"""Generate an EDITABLE .docx revision proposal for Dr. Buckholtz (English version).

English translation of make_revision_proposal_ru.py, same structure: cover note +
3-column comparison table (Was / Suggest / Why, where 'Why' draws on the reviewer
HATE/LOVE pattern) + ranked open questions + a 'what we verified' block.
Reproducible: re-run to regenerate the .docx.

Output: paper/revision_proposal_for_TJB_EN.docx
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor


def shade_cell(cell, hex_fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.makeelement(qn("w:shd"), {qn("w:fill"): hex_fill})
    tc_pr.append(shd)


def h(doc, text, size=14, color=(0x1F, 0x4E, 0x79)):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor(*color)
    return p


doc = Document()
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

# ---- Title ----
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Preprint Revision Proposal — Draft for Your Review")
r.bold = True
r.font.size = Pt(16)
sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sr = sub.add_run(
    "Independent number-checking and supporting material for Dr. Thomas J. Buckholtz\n"
    "(preprint v6, preprints202511.0598.v6). NOT a claim to co-authorship."
)
sr.italic = True

# ---- Cover note ----
h(doc, "Cover Note")
cover = (
    "Dear Dr. Buckholtz,\n\n"
    "Most important thing first: I am NOT claiming co-authorship or any share of "
    "authorship — none whatsoever. Everything below is offered as your independent "
    "assistant, and all of this material is yours: use it in your preprint however "
    "you see fit, or not at all.\n\n"
    "What I did. I independently re-verified the numerical relations in your v6 "
    "preprint — every number is reproduced by a runnable script, so any reviewer or "
    "colleague can check it. Along the way, a few new things came up as well "
    "(Section 3) — I offer these simply as material you may find useful to include.\n\n"
    "Why. The goal is simple: combine three resources — current AI tools, my "
    "computational work with them, and your years of experience in physics — to "
    "bring the material to as rigorous, 'reference-grade' a form as possible, one "
    "that stands confidently through review.\n\n"
    "How this is organized. (1) A comparison table 'was → suggest → why', where "
    "'why' draws directly on the reasons reviewers typically reject work. "
    "(2) Open questions — flagged honestly; for any of them, if you point me toward "
    "a direction or a specific option, I can check it numerically right away. "
    "(3) What has already been re-verified and could be included in the preprint.\n\n"
    "An optional idea, entirely at your discretion: the material could be split "
    "into a short, rigorous note on the verified mass relations (nothing overclaims, "
    "a real shot at review) and a separate, program-level paper on MULTING "
    "cosmology. But that is entirely your call.\n\n"
    "This is a draft for you to edit — please mark it up directly in the file.\n\n"
    "With respect and thanks for your work,\nSergey Boyko · Ronin Institute"
)
for para in cover.split("\n\n"):
    doc.add_paragraph(para)

# ---- Comparison table ----
h(doc, "1. Comparison Table of Proposed Changes")
rows = [
    ("Was (v6)", "Suggest", "Why"),
    (
        "9+ tables; equations embedded inside table cells.",
        "Equations pulled out into separate numbered formulas; tables reserved for data only.",
        "A reviewer should see the formula immediately, not hunt for it inside a cell. "
        "'Hidden' equations read as a lack of rigor.",
    ),
    (
        "Non-standard structure; a section titled 'Authority that our work suggests'.",
        "Standard structure: Abstract -> Introduction -> Formalism -> Results -> "
        "Discussion (limitations) -> Conclusions.",
        "Reviewers HATE: non-standard presentation and phrasing that reads as a claim "
        "to 'authority'. LOVE: a familiar framework they can judge the work against.",
    ),
    (
        "Terms MESI / IDM / OM / MULTING used without definitions on first mention.",
        "Every term defined on first use; jargon kept to a minimum.",
        "Readability is the first thing that gets a paper rejected. Unfamiliar jargon "
        "without definitions creates a barrier on page 1.",
    ),
    (
        "Verified relations and speculative cosmology presented together.",
        "Section A -- Verified (Eq.32, 7:9:17, fermion spectrum). Section B -- "
        "Program (cosmology, beta parameters).",
        "Reviewers LOVE an honest separation of solid results from speculative ones. "
        "A strong result should not be dragged down by unresolved hypotheses nearby.",
    ),
    (
        "beta_d, beta_q introduced as given quantities (Eqs. 18-20).",
        "beta parameters moved into an explicit 'Open Question' block with our "
        "Fisher-analysis of their non-identifiability.",
        "Reviewers HATE hidden/fitted parameters. An honest 'this is an open "
        "question, here is the analysis' is stronger than presenting a parameter as known.",
    ),
    (
        "Numbers given without a reproducible source.",
        "Every number linked to a runnable script (verify_all_claims.py etc.); code "
        "in an open repository.",
        "Reviewers LOVE reproducibility (GitHub). This removes half of the 'where "
        "does this number come from?' objections before they're even raised.",
    ),
]
table = doc.add_table(rows=len(rows), cols=3)
table.style = "Table Grid"
table.alignment = WD_TABLE_ALIGNMENT.CENTER
for j, txt in enumerate(rows[0]):
    c = table.rows[0].cells[j]
    c.text = ""
    rr = c.paragraphs[0].add_run(txt)
    rr.bold = True
    rr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    shade_cell(c, "1F4E79")
for i, row in enumerate(rows[1:], start=1):
    for j, txt in enumerate(row):
        table.rows[i].cells[j].text = txt

# ---- Open questions ----
h(doc, "2. Open Questions")
doc.add_paragraph(
    "These are not being hidden but stated explicitly -- a reviewer will ask about "
    "them regardless, and an honest acknowledgment is stronger than silence. Ranked "
    "by severity (CRITICAL = a rejection risk without an answer). For any of these: "
    "if you point me toward a physical direction or a specific option, I can check "
    "it numerically right away (AI tools + computation) -- so your experience sets "
    "the hypothesis and the check is near-instant."
)
oq = [
    (
        "[CRITICAL] Lagrangian / action for the F_oP force law",
        "The force law is currently postulated by analogy with electromagnetism. A "
        "reviewer will ask: 'show a derivation from an action, or cite one.' "
        "Suggestion: flag this honestly as an open question and place it in "
        "Section B (program).",
    ),
    (
        "[CRITICAL] Deriving beta_d, beta_q from first principles",
        "Currently 2 free parameters. Our Fisher analysis: they are not identifiable "
        "from Table A1 alone. Suggestion: mark as an open question; show the "
        "analysis -- this is both more honest and stronger than the alternative.",
    ),
    (
        "[CRITICAL] Analytical bridge F_oP -> H(z)",
        "No explicit derivation exists (Appendix A.1 is a procedure, not a "
        "derivation). Suggestion: present H(z) as a phenomenological consequence, "
        "not a prediction of the theory.",
    ),
]
for title, body in oq:
    p = doc.add_paragraph()
    p.add_run(title).bold = True
    doc.add_paragraph(body)

# ---- What we verified ----
h(doc, "3. What Has Already Been Re-Verified -- and Could Be Included")
doc.add_paragraph(
    "Everything below is reproducible (a runnable script backs every number) and is "
    "offered to you as ready-to-use material. Bold marks what came up newly during "
    "verification."
)
ver = [
    (
        "",
        "Eq.32 (4/3)(m_tau/m_e)^12 = alpha_EM/alpha_G: deviation 0.0135% (0.17 sigma); "
        "the exponent 12 is unique (1 of 5040 simple combinations); the relation is "
        "not found in the literature. Script: verify_all_claims.py.",
    ),
    (
        "NEW -- ",
        "the 7:9:17 relation (m_W^2 : m_Z^2 : m_H^2) in its scale-free form "
        "m_W/m_H = sqrt(7/17) is anchor-independent (holds to <0.05%) and predicts a "
        "heavy W: consistent only with CDF-II/CMS (chi^2=2.0), excludes the light "
        "combination (chi^2=39). This is a falsifiable discriminant for the W-mass "
        "anomaly -- a concrete prediction that future W measurements will confirm or "
        "reject. Script: c6_mass_preference.py.",
    ),
    (
        "",
        "Fermion spectrum (Eqs. 21-24): muon 0.47%, quark geometric means <0.31% "
        "(PDG 2024). Script: idm_masses.py.",
    ),
    (
        "correction -- ",
        "N_opt = omega_cdm/omega_b = 5.366: the deviation from the integer 5 is "
        "5.67 sigma (the original error-propagation formula gave ~259 sigma due to "
        "a unit mismatch; this has been corrected).",
    ),
]
for tag, body in ver:
    p = doc.add_paragraph(style="List Bullet")
    if tag:
        p.add_run(tag).bold = True
    p.add_run(body)

doc.add_paragraph()
foot = doc.add_paragraph()
foot.add_run(
    "This draft was prepared following reviewer-defense and pre-submission QA "
    "protocols (Ronin Institute). Translated from the Russian original at your request."
).italic = True

out = Path(__file__).resolve().parent.parent / "paper" / "revision_proposal_for_TJB_EN.docx"
doc.save(str(out))
print(f"Saved: {out}")
print(
    f"Sections: cover + comparison table ({len(rows) - 1} rows) + {len(oq)} open questions + {len(ver)} verified items"
)
