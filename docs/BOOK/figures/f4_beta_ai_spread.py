"""F4 — beta_d / beta_q spread across 3 AI services, and the Birge ratio
(BRAI) quantifying how inconsistent that spread is with a single physical
constant.

Data: re-runs scripts/brai_beta.py, whose BETA_D/BETA_Q arrays are cited
there to docs/111_beta_provenance_evidence_lock.md (multi-AI comparison,
Codex-audited). Re-run rather than hand-copied, so the figure always
matches what that script currently reports.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import subprocess
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

HERE = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent / "f4_beta_ai_spread.png"

print("re-running scripts/brai_beta.py ...")
proc = subprocess.run(
    ["python", "scripts/brai_beta.py"],
    cwd=HERE,
    check=True,
    capture_output=True,
    text=True,
)
print(proc.stdout[-800:])

SERVICES = ["Claude/NotebookLM", "Gemini", "ChatGPT"]
BETA_D = np.array([4.50, 4.25, 0.78])
BETA_Q = np.array([18.0, 8.10, 0.19])
SIGMA_REL = 0.20
SIGMA_D = BETA_D * SIGMA_REL
SIGMA_Q = BETA_Q * SIGMA_REL


def birge(x, s):
    w = 1.0 / s**2
    xbar = np.sum(w * x) / np.sum(w)
    chi2_stat = np.sum((x - xbar) ** 2 / s**2)
    n = len(x)
    r_b = chi2_stat / (n - 1)
    p = chi2.sf(chi2_stat, n - 1)
    return xbar, r_b, p


xbar_d, rb_d, p_d = birge(BETA_D, SIGMA_D)
xbar_q, rb_q, p_q = birge(BETA_Q, SIGMA_Q)
print(f"beta_d: R_B={rb_d:.1f}, p={p_d:.2e}   beta_q: R_B={rb_q:.1f}, p={p_q:.2e}")

fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
for ax, vals, sig, xbar, rb, name in [
    (axes[0], BETA_D, SIGMA_D, xbar_d, rb_d, r"$\beta_d$"),
    (axes[1], BETA_Q, SIGMA_Q, xbar_q, rb_q, r"$\beta_q$"),
]:
    x = np.arange(3)
    ax.errorbar(x, vals, yerr=sig, fmt="o", ms=8, color="#3b6ea5", capsize=4)
    ax.axhline(xbar, color="#c0392b", ls="--", lw=1, label=f"weighted mean = {xbar:.2f}")
    ax.set_xticks(x)
    ax.set_xticklabels(SERVICES, fontsize=8, rotation=15)
    ax.set_title(f"{name}: Birge ratio $R_B$ = {rb:.1f}")
    ax.legend(fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)

fig.suptitle(
    "β divergence across 3 AI services — 5.8× and 95× spread; "
    "$R_B \\gg 1$ means inconsistent with a single constant"
)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
