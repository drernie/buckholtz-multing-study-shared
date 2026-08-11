"""F3 — Look-elsewhere scan: Eq.32 = (4/3)(m_tau/m_e)^12 vs alpha_EM/alpha_G
ranks #1 of 83,160 candidate (reference-mass, power, coefficient) formulas,
with the next-best candidate 6.8x worse in relative error.

Data: regenerated live by running scripts/scan_reference_mass_robustness.py
(same script produces experiments/20260627-f4-eq32-synthesis/
reference_mass_scan_result.json). Re-run here rather than trusted from a
stale file, so the number in the figure is always the number the script
currently produces.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import json
import subprocess
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parents[3]
RESULT = HERE / "experiments" / "20260627-f4-eq32-synthesis" / "reference_mass_scan_result.json"
OUT = Path(__file__).parent / "f3_look_elsewhere.png"

print("re-running scripts/scan_reference_mass_robustness.py ...")
subprocess.run(["python", "scripts/scan_reference_mass_robustness.py"], cwd=HERE, check=True)

d = json.loads(RESULT.read_text(encoding="utf-8"))
top10 = d["top10"]
print(f"total trials: {d['total_trials_combined']:,}, Eq.32 rank: #{d['eq32_rank_combined']}")

labels = [f"#{c['rank']}\n{c['formula']}" for c in top10]
errs = [c["rel_err"] * 100 for c in top10]
colors = ["#c0392b" if c["rank"] == 1 else "#8aa8c8" for c in top10]

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.bar(range(len(top10)), errs, color=colors, edgecolor="none")
ax.set_xticks(range(len(top10)))
ax.set_xticklabels(labels, fontsize=7.5, rotation=0)
ax.set_ylabel("relative error (%)")
ax.set_title(
    f"Top 10 of {d['total_trials_combined']:,} candidate formulas — "
    f"Eq.32 ranks #1 (p = {d['p_empirical_combined']:.1e})"
)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
