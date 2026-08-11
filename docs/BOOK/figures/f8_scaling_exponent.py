"""F8 — the mass-scaling exponent d ln(u)/d ln(M): pure-gravity self-similar
theory predicts exactly +1 (same as the single-field completion needs), but
BOTH the marginal (0.555) and the deconfounded, z-controlled (0.393) measured
exponents fall well short of it -- and the deconfounded value is FURTHER
from +1, not closer, once the flux-limited sample's own M-z selection is
removed. This is the adversarial audit's central negative result: the gap
is ordinary baryonic-feedback astrophysics, not gravitational content
either completion modeled.

Data: data/clusters_clean.csv, n=548 (MCXC-I intersect PSZ2, thermal-energy
subsample) -- same file, same subsample used throughout this thread.
Regression method: log-log OLS of u = k*R/M against M, controlling for
E(z)=H(z)/H0 -- reused directly from
experiments/20260803-bridge/adversarial_p1/microphysical_u_scaling.py.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.cosmology import Planck18

HERE = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent / "f8_scaling_exponent.png"

df = pd.read_csv(HERE / "data" / "clusters_clean.csv")
sub = df[df["Ethermal_c2_Msun"].notna()].copy()
n = len(sub)
print(f"n = {n} clusters (thermal-energy subsample)")

M = sub["M500c_Msun"].to_numpy()
R = sub["R500c_Mpc"].to_numpy()
k = sub["Ethermal_c2_Msun"].to_numpy()
z = sub["z"].to_numpy()
u_arr = k * R / M

lnM, lnU = np.log(M), np.log(u_arr)
lnEz = np.log(Planck18.efunc(z))
X = np.column_stack([np.ones(n), lnM, lnEz])
coef_U, *_ = np.linalg.lstsq(X, lnU, rcond=None)
slope_deconfounded = coef_U[1]

# marginal (uncontrolled) slope, for comparison -- the originally-quoted 0.555
X_marg = np.column_stack([np.ones(n), lnM])
coef_marg, *_ = np.linalg.lstsq(X_marg, lnU, rcond=None)
slope_marginal = coef_marg[1]

print(f"marginal slope (no z control)     = {slope_marginal:.3f}")
print(f"deconfounded slope (E(z) control) = {slope_deconfounded:.3f}")

fig, ax = plt.subplots(figsize=(8, 5.5))
ax.scatter(lnM, lnU, s=6, alpha=0.35, color="#3b6ea5", label=f"clusters (n={n})")

x_line = np.linspace(lnM.min(), lnM.max(), 50)
ax.plot(
    x_line,
    coef_marg[0] + slope_marginal * x_line,
    color="#8aa8c8",
    lw=2,
    label=f"marginal fit, slope={slope_marginal:.3f}",
)
ax.plot(
    x_line,
    coef_U[0] + slope_deconfounded * x_line + coef_U[2] * lnEz.mean(),
    color="#c0392b",
    lw=2,
    label=f"deconfounded fit, slope={slope_deconfounded:.3f}",
)

# +1 prediction line, anchored at the sample mean for visual comparison
mean_lnM, mean_lnU = lnM.mean(), lnU.mean()
ax.plot(
    x_line,
    mean_lnU + 1.0 * (x_line - mean_lnM),
    color="black",
    ls="--",
    lw=1.3,
    label="pure-gravity prediction, slope=1.000",
)

ax.set_xlabel(r"$\ln M_{500c}$")
ax.set_ylabel(r"$\ln u_i = \ln(k_i R_i / m_i)$")
ax.set_title(
    "Mass-scaling exponent: deconfounding moves AWAY from the +1 prediction, not toward it"
)
ax.legend(fontsize=8.5, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
