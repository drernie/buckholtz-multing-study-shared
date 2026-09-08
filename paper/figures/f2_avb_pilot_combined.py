"""F2 -- the adversarial-verification-benchmark (AVB) pilot, both results:
the still-inconclusive primary detection-rate comparison (panel A), and the
more substantively interesting secondary finding, a reproduced defect in the
corpus's own clean-control construction (panel B).

All numbers are taken directly from methodology_paper_draft_v0.md Sec.5
(itself verified against experiments/adversarial-verification-benchmark/
result_summary.md, result_summary_extension.md, and
independent_verification_report.md) -- this script does not compute
anything new, it only visualizes numbers the paper already states, and
it asserts internal consistency (the two batches must sum to the combined
figures) before trusting the plot.

NOT_VALIDATION - NOT_REFUTATION -- this figure shows an inconclusive
primary result and a real corpus-construction finding, not a validated
claim that the treatment protocol outperforms baseline.
"""

from pathlib import Path

import matplotlib.pyplot as plt

OUT = Path(__file__).parent / "f2_avb_pilot_combined.png"

BASELINE_COLOR = "#7f8c8d"
TREATMENT_COLOR = "#2e7d32"

# --- Panel A data: detection rate, per methodology_paper_draft_v0.md Sec.5 ---
# (label, baseline_hit, baseline_n, treatment_hit, treatment_n)
GROUPS = [
    ("Batch 1\n(corrected, n=12)", 12, 12, 12, 12),
    ("Batch 2\n(extension, n=13)", 12, 13, 13, 13),
    ("Combined\n(n=25)", 24, 25, 25, 25),
]

# Internal consistency check -- the two batches must sum to the combined row,
# per the paper's own Sec.5 combined-reading table.
b1_hit, b1_n = GROUPS[0][1], GROUPS[0][2]
b2_hit, b2_n = GROUPS[1][1], GROUPS[1][2]
comb_hit, comb_n = GROUPS[2][1], GROUPS[2][2]
assert (b1_hit + b2_hit, b1_n + b2_n) == (comb_hit, comb_n), (
    "Batch 1 + Batch 2 baseline detections must equal the combined row -- "
    f"got {b1_hit}+{b2_hit}={b1_hit + b2_hit} of {b1_n}+{b2_n}={b1_n + b2_n}, "
    f"paper states {comb_hit}/{comb_n}"
)
t1_hit, t1_n = GROUPS[0][3], GROUPS[0][4]
t2_hit, t2_n = GROUPS[1][3], GROUPS[1][4]
tcomb_hit, tcomb_n = GROUPS[2][3], GROUPS[2][4]
assert (t1_hit + t2_hit, t1_n + t2_n) == (tcomb_hit, tcomb_n), (
    "Batch 1 + Batch 2 treatment detections must equal the combined row -- "
    f"got {t1_hit}+{t2_hit}={t1_hit + t2_hit} of {t1_n}+{t2_n}={t1_n + t2_n}, "
    f"paper states {tcomb_hit}/{tcomb_n}"
)

# --- Panel B data: clean-control finding, per Sec.5 ---
CLEAN_TASKS = ["027", "028", "029", "030", "031", "032"]
FOUND_ACTUALLY_CLEAN = 0

fig, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5.6), gridspec_kw={"width_ratios": [1.6, 1]})

# Panel A -- grouped bar chart
x = range(len(GROUPS))
width = 0.32
baseline_pct = [100 * h / n for _, h, n, _, _ in GROUPS]
treatment_pct = [100 * h / n for _, _, _, h, n in GROUPS]

bars_b = axA.bar(
    [i - width / 2 for i in x],
    baseline_pct,
    width,
    color=BASELINE_COLOR,
    label="Baseline (ambient-default)",
)
bars_t = axA.bar(
    [i + width / 2 for i in x],
    treatment_pct,
    width,
    color=TREATMENT_COLOR,
    label="Treatment (explicit FL protocol + skeptic)",
)

for i, (_, bh, bn, th, tn) in enumerate(GROUPS):
    axA.text(i - width / 2, baseline_pct[i] + 1.5, f"{bh}/{bn}", ha="center", fontsize=9)
    axA.text(i + width / 2, treatment_pct[i] + 1.5, f"{th}/{tn}", ha="center", fontsize=9)

axA.set_ylim(0, 112)
axA.set_xticks(list(x))
axA.set_xticklabels([g[0] for g in GROUPS], fontsize=9)
axA.set_ylabel("Defect detection rate (%)")
axA.set_title(
    "Primary comparison: inconclusive\n(McNemar p=1.0, n=25, 1 discordant pair)", fontsize=10
)
axA.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.22))
axA.text(
    0.5,
    -0.60,
    "Original (pre-Addendum-3) Batch-1 reading, not shown above:\n"
    "baseline 13/13=100%, treatment 12/13=92.3% -- treatment underperformed. See Sec.5.",
    transform=axA.transAxes,
    ha="center",
    fontsize=7.5,
    color="#555555",
    style="italic",
)
for spine in ("top", "right"):
    axA.spines[spine].set_visible(False)

# Panel B -- clean-control finding
axB.bar(
    ["clean-control\ntasks (n=6)"],
    [FOUND_ACTUALLY_CLEAN],
    color="#2e7d32",
    width=0.5,
    label="found actually clean",
)
axB.bar(
    ["clean-control\ntasks (n=6)"],
    [len(CLEAN_TASKS) - FOUND_ACTUALLY_CLEAN],
    bottom=[FOUND_ACTUALLY_CLEAN],
    color="#c0392b",
    width=0.5,
    label="flagged by both arms,\nanswer key says non-defect",
)
axB.set_ylim(0, len(CLEAN_TASKS) + 0.5)
axB.set_yticks(range(len(CLEAN_TASKS) + 1))
axB.set_ylabel("tasks")
axB.text(
    0,
    len(CLEAN_TASKS) / 2,
    f"0 of {len(CLEAN_TASKS)}",
    ha="center",
    va="center",
    fontsize=16,
    fontweight="bold",
    color="white",
)
axB.set_title(
    "Secondary finding: reproduced,\nnot inconclusive\n(0/6 clean-control tasks were clean)",
    fontsize=10,
)
axB.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.22))
axB.text(
    0.5,
    -0.60,
    "tasks: " + ", ".join(CLEAN_TASKS),
    transform=axB.transAxes,
    ha="center",
    fontsize=7.5,
    color="#555555",
)
for spine in ("top", "right"):
    axB.spines[spine].set_visible(False)

fig.suptitle(
    "AVB pilot, full N=32 design (2 batches) -- inconclusive primary result, reproduced corpus finding",
    fontsize=11.5,
    fontweight="bold",
)
fig.subplots_adjust(left=0.07, right=0.97, top=0.80, bottom=0.42, wspace=0.28)
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
