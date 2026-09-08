"""F1 -- the 5 case studies are not 6 independent artifacts. They are two
lineages: P214 (root) plus three findings extracted from its own retraction
(P215, P216, P217), and P220 (a separate, unrelated lineage).

This is the correction methodology_paper_draft_v0.md's own Sec.4.1 makes
(see the paper's Sec.8/Sec.11 for the full history of that correction).
Every label and citation below is taken verbatim from the paper's own
Sec.4.1 table and the provenance quotes in
paper/METHODOLOGY_PAPER_DRAFT_CORRECTIONS_after_step8a.md Sec.1 -- this
script does not introduce any claim the text does not already make.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).parent / "f1_case_study_lineage.png"

LINEAGE_A_COLOR = "#3b6ea5"
LINEAGE_B_COLOR = "#c0392b"
BOX_STYLE = "round,pad=0.15"
BOX_LINEWIDTH = 1.2

# (id, x, y, width, verdict, taxonomy) -- positions are hand-tuned for
# a clean tree layout, not derived from data (this is a structure diagram,
# not a data plot).
ROOT = ("P214", 5.0, 8.6, 2.6, "root of lineage A\n4/5 sub-claims falsified", "Cat. 9")
CHILDREN = [
    ("P215", 1.6, 5.6, 2.6, "from P214 §7's survivors\nconclusion inverted", "Cat. 2 + Cat. 6"),
    ("P216", 5.0, 5.6, 2.6, "from P214 §7.1\nhierarchy misread as conflict", "Cat. 8"),
    ("P217", 8.4, 5.6, 2.6, "from P214 §7.2\none-sided search", "Cat. 3"),
]
SEPARATE = (
    "P220",
    5.0,
    2.2,
    2.8,
    "separate lineage\n4 real defects, all counted",
    "Cat. 4 + Cat. 11",
)

EXPECTED_IDS = {"P214", "P215", "P216", "P217", "P220"}
found = {ROOT[0], *[c[0] for c in CHILDREN], SEPARATE[0]}
assert found == EXPECTED_IDS, (
    f"lineage diagram must show exactly the 5 case-study artifacts from the paper's own "
    f"Sec.4.1 table -- got {found}, expected {EXPECTED_IDS}"
)

fig, ax = plt.subplots(figsize=(10, 7.5))


def draw_box(node, color, fontsize=9.5):
    label, x, y, w, verdict, tax = node
    box = FancyBboxPatch(
        (x - w / 2, y - 0.8),
        w,
        1.6,
        facecolor="white",
        edgecolor=color,
        boxstyle=BOX_STYLE,
        linewidth=BOX_LINEWIDTH,
    )
    ax.add_patch(box)
    ax.text(
        x, y + 0.5, label, ha="center", va="center", fontsize=13, fontweight="bold", color=color
    )
    ax.text(
        x, y + 0.02, verdict, ha="center", va="center", fontsize=fontsize - 1.5, linespacing=1.4
    )
    ax.text(x, y - 0.55, tax, ha="center", va="center", fontsize=8, style="italic", color="#555555")


draw_box(ROOT, LINEAGE_A_COLOR)
for child in CHILDREN:
    draw_box(child, LINEAGE_A_COLOR)
    arrow = FancyArrowPatch(
        (ROOT[1] + (child[1] - ROOT[1]) * 0.15, ROOT[2] - 0.85),
        (child[1], child[2] + 0.85),
        arrowstyle="-|>",
        mutation_scale=14,
        color=LINEAGE_A_COLOR,
        linewidth=1.3,
    )
    ax.add_patch(arrow)

draw_box(SEPARATE, LINEAGE_B_COLOR)

ax.text(
    0.3,
    9.6,
    "Lineage A -- one root, three extracted findings\n"
    '(3 of the paper\'s original "6 independent artifacts" claim\n'
    "were downstream of P214's own retraction)",
    fontsize=9,
    color=LINEAGE_A_COLOR,
    va="top",
)
ax.text(
    0.3,
    1.0,
    "Lineage B -- unrelated to lineage A\n"
    "(no project record attributes P220 to lineage A's\n"
    "search-asymmetry mechanism)",
    fontsize=9,
    color=LINEAGE_B_COLOR,
    va="top",
)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10.3)
ax.set_title(
    "5 case-study artifacts, 2 lineages -- not 6 independent samples",
    fontsize=12,
    fontweight="bold",
)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
