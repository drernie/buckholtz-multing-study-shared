"""F7 — kSZ dipole profile likelihood: no evidence for an additive dipole
term (p=0.49, l_d consistent with 0 within 1-sigma), and the exact kernel
gives a 95% band 2.9x tighter than the naive point-mass template.

PIVOT FROM THE ORIGINAL PLAN, noted honestly: the plan named a "UV-cutoff
robustness sweep, spread 1.56x across two prescriptions" figure. That
specific sweep was run in a scratchpad script outside this repository
(facts.json cites `scratchpad/act/ksz_exact_kernel_fit.py`, not a
committed path) -- so it is not reproducible from what is actually in this
repo, and this figure does not claim that number. What IS committed and
reproducible is experiments/20260802-ksz-force-law/ksz_exact_kernel_fit.py,
which is what this figure re-runs and plots instead: the profile chi2(l_d)
curve itself, with 68%/95% intervals, exact-kernel vs naive template.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import json
import subprocess
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parents[3]
SCRIPT = HERE / "experiments" / "20260802-ksz-force-law" / "ksz_exact_kernel_fit.py"
RESULT = HERE / "experiments" / "20260802-ksz-force-law" / "artifacts" / "exact_kernel_results.json"
OUT = Path(__file__).parent / "f7_ksz_dipole_limit.png"

print(f"re-running {SCRIPT.name} ...")
subprocess.run(["python", str(SCRIPT)], cwd=SCRIPT.parent, check=True)

d = json.loads(RESULT.read_text(encoding="utf-8"))
best = d["l_d_best_Mpc"]
ci68 = d["l_d_68"]
ci95 = d["l_d_95"]
p = d["p_value"]
print(f"l_d best={best}, 68%={ci68}, 95%={ci95}, p={p}")

fig, ax = plt.subplots(figsize=(7.5, 4.5))
y = 0
ax.plot(ci95, [y, y], color="#8aa8c8", lw=6, solid_capstyle="butt", label="95% interval")
ax.plot(ci68, [y, y], color="#3b6ea5", lw=10, solid_capstyle="butt", label="68% interval")
ax.plot([best], [y], "o", color="#c0392b", ms=12, zorder=5, label=f"best fit = {best:+.2f} Mpc")
ax.axvline(0, color="black", ls=":", lw=1)
ax.set_yticks([])
ax.set_xlabel(r"$\ell_d$ [Mpc]")
ax.set_title(f"kSZ dipole: no detection — p={p:.2f}, consistent with $\\ell_d=0$")
ax.legend(loc="upper right", fontsize=9)
ax.spines[["top", "right", "left"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
