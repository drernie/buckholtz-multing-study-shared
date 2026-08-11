"""F5 — H1's partial correlation r(delta_M, E_ICM | M_WL) = -0.70 survived
two independent attacks (H1c: control for morphology/wX; H1d: split by mass)
before dissolving once T_X was controlled for (NR-015): it turned out T_X is
a literal multiplicative factor of E_ICM's own definition, so this was
correlation with a shared variable, not a real physical signal.

Data: experiments/20260713-h1e-agn-feedback-confound/artifacts/
cccp_mahdavi2013_merged.csv (Mahdavi et al. 2013). Same residualize/
partial_corr method as h1e_partial_correlation_test.py, reimplemented here
directly against the checked-in CSV so this figure has no import-path
dependency on that script.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION -- this is a
DESCRIPTIVE correlation history, not a causal claim; the whole point of
this figure is that a plausible-looking correlation dissolved.
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parents[3]
CSV = (
    HERE
    / "experiments"
    / "20260713-h1e-agn-feedback-confound"
    / "artifacts"
    / "cccp_mahdavi2013_merged.csv"
)
OUT = Path(__file__).parent / "f5_h1_correlation_dissolves.png"


def residualize(y, controls):
    x = np.column_stack([controls, np.ones(len(y))])
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return y - x @ beta


def partial_corr(x, y, controls):
    rx = residualize(x, controls)
    ry = residualize(y, controls)
    return stats.pearsonr(rx, ry)


with CSV.open(encoding="utf-8") as f:
    all_rows = list(csv.DictReader(f))
print(f"loaded {len(all_rows)} clusters from {CSV.name}")


def col(rows, key):
    return np.array([float(r[key]) for r in rows])


# Baseline / H1d (mass-threshold split): needs delta_M, E_ICM, M_WL only.
rows_base = [
    r for r in all_rows if r["delta_M_1e14Msun"] and r["E_ICM_proxy_MgasTx"] and r["M_WL_1e14Msun"]
]
dM, eICM, mWL = (
    col(rows_base, "delta_M_1e14Msun"),
    col(rows_base, "E_ICM_proxy_MgasTx"),
    col(rows_base, "M_WL_1e14Msun"),
)
r_base, p_base = partial_corr(dM, eICM, mWL.reshape(-1, 1))

# H1c: control for wX too.
rows_wx = [r for r in rows_base if r["wX"]]
dM_w, eICM_w, mWL_w, wX = (
    col(rows_wx, "delta_M_1e14Msun"),
    col(rows_wx, "E_ICM_proxy_MgasTx"),
    col(rows_wx, "M_WL_1e14Msun"),
    col(rows_wx, "wX"),
)
r_h1c, p_h1c = partial_corr(dM_w, eICM_w, np.column_stack([mWL_w, wX]))

# NR-015: control for T_X too -- the dissolution. TWO versions, distinctly
# labelled: the EXACT pre-registration (M_Gas, per null_results/20260718-
# nr015-...md "KEY TEST (exact pre-registration, pearl row 34)") and the
# closely-related E_ICM version this file originally plotted alone. Phase D
# (Agent(skeptic), context-blind, 2026-08-11) found the chapter text had
# cited the E_ICM number as if it were the pre-registered result. Both shown
# now rather than silently picking one.
rows_tx = [r for r in rows_base if r["T_X_keV"]]
dM_t, eICM_t, mgas_t, mWL_t, tx = (
    col(rows_tx, "delta_M_1e14Msun"),
    col(rows_tx, "E_ICM_proxy_MgasTx"),
    col(rows_tx, "M_Gas_1e14Msun"),
    col(rows_tx, "M_WL_1e14Msun"),
    col(rows_tx, "T_X_keV"),
)
r_tx_eicm, p_tx_eicm = partial_corr(dM_t, eICM_t, np.column_stack([mWL_t, tx]))
r_tx_mgas, p_tx_mgas = partial_corr(dM_t, mgas_t, np.column_stack([mWL_t, tx]))

print(
    f"baseline               r(dM,E_ICM|M_WL)     = {r_base:+.4f}  p={p_base:.2e}  n={len(rows_base)}"
)
print(
    f"H1c                    r(dM,E_ICM|M_WL,wX)  = {r_h1c:+.4f}  p={p_h1c:.2e}  n={len(rows_wx)}"
)
print(
    f"NR-015 (E_ICM)         r(dM,E_ICM|M_WL,T_X) = {r_tx_eicm:+.4f}  p={p_tx_eicm:.2e}  n={len(rows_tx)}"
)
print(
    f"NR-015 (M_Gas, EXACT pre-registration) r(dM,M_Gas|M_WL,T_X) = {r_tx_mgas:+.4f}  p={p_tx_mgas:.2e}  n={len(rows_tx)}"
)

labels = [
    "baseline\n|M_WL",
    "H1c survives\n|M_WL, wX",
    "NR-015 (E_ICM)\n|M_WL, T_X",
    "NR-015 (M_Gas,\npre-registered)\n|M_WL, T_X",
]
vals = [r_base, r_h1c, r_tx_eicm, r_tx_mgas]
colors = ["#8aa8c8", "#3b6ea5", "#c0392b", "#8b0000"]

fig, ax = plt.subplots(figsize=(7.5, 5))
ax.bar(labels, vals, color=colors, edgecolor="none")
ax.axhline(0, color="black", lw=0.8)
ax.set_ylabel("partial correlation r")
ax.set_title(
    "H1: a partial correlation that survived two attacks,\n"
    "then dissolved once the shared variable was controlled for"
)
for i, v in enumerate(vals):
    ax.text(i, v + (0.03 if v >= 0 else -0.05), f"{v:+.3f}", ha="center", fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
