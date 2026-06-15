"""
Fairness Diagnostics — Direction 3
Compares H_MULT vs ΛCDM fit quality after correcting for degrees of freedom.

KEY QUESTION: Does H_MULT's better χ² survive AIC/BIC after accounting for:
  (a) H_MULT being fitted to THIS data (β_d, β_q optimized against H_obs)
  (b) H_MULT being anchored to SH0ES H₀=73.0 while ΛCDM uses Planck H₀=67.4
  (c) The z=0 row giving σ_MULT=0 by construction (anchor point)

DATA: claude_approximate_matches.csv (Table A1, Claude AI, β_d=4.5, β_q=18.0)
"""

import numpy as np
from scipy.optimize import minimize, minimize_scalar

# --- Table A1 data (claude_approximate_matches.csv) ---
# z, H_obs, sigma_H, H_FLRW, sigma_FLRW, H_MULT, sigma_MULT
TABLE = [
    (0.00, 73.0, 1.0, 67.4, -5.6, 73.0, 0.00),  # anchor row
    (0.06, 69.0, 3.0, 68.1, -0.3, 70.2, 0.40),
    (0.14, 74.0, 4.0, 69.3, -1.2, 73.5, -0.10),
    (0.25, 79.0, 4.5, 71.5, -1.7, 78.8, -0.04),
    (0.40, 82.0, 5.0, 75.0, -1.4, 83.1, 0.20),
    (0.65, 92.0, 7.0, 83.0, -1.3, 91.4, -0.10),
    (1.00, 105.0, 8.0, 95.7, -1.2, 104.2, -0.10),
    (1.50, 125.0, 15.0, 114.8, -0.7, 126.5, 0.10),
    (2.10, 150.0, 20.0, 140.3, -0.5, 151.8, 0.10),
    (3.20, 195.0, 30.0, 187.6, -0.2, 197.3, 0.10),
    (5.00, 270.0, 50.0, 265.2, -0.1, 271.5, 0.03),
    (8.50, 420.0, 90.0, 398.5, -0.2, 418.1, -0.02),
]

z_arr = np.array([r[0] for r in TABLE])
H_obs = np.array([r[1] for r in TABLE])
sigma_H = np.array([r[2] for r in TABLE])
H_FLRW = np.array([r[3] for r in TABLE])
s_FLRW = np.array([r[4] for r in TABLE])
H_MULT = np.array([r[5] for r in TABLE])
s_MULT = np.array([r[6] for r in TABLE])

n = len(TABLE)
H0_SH0ES = 73.0
H0_PLANCK = 67.4


# --- Model functions ---
def H_lcdm(z, H0, Om):
    """Flat ΛCDM, matter + Λ only."""
    return H0 * np.sqrt(Om * (1 + z) ** 3 + (1 - Om))


# --- Chi^2 helpers ---
def chi2_from_residuals(sigma_arr):
    return float(np.sum(sigma_arr**2))


def chi2_lcdm(H0, Om):
    pred = H_lcdm(z_arr, H0, Om)
    return float(np.sum(((pred - H_obs) / sigma_H) ** 2))


# --- AIC / BIC ---
def aic(chi2, k):
    return chi2 + 2 * k


def bic(chi2, k, n):
    return chi2 + k * np.log(n)


# ============================================================
# MODEL 1: ΛCDM vanilla (Planck H0=67.4, Om=0.3 — not fitted)
# ============================================================
chi2_lcdm_planck = chi2_from_residuals(s_FLRW)
k_lcdm_planck = 0  # no parameters fitted to THIS data
rms_lcdm_planck = np.sqrt(np.mean(s_FLRW**2))

# ============================================================
# MODEL 2: H_MULT reported (β_d=4.5, β_q=18.0, H0 fixed=73.0)
# Anchor: σ_MULT(z=0) = 0 by construction (1 DoF "spent")
# ============================================================
chi2_mult_reported = chi2_from_residuals(s_MULT)
k_mult_reported = 2  # β_d, β_q fitted to this data; H0 fixed
rms_mult_reported = np.sqrt(np.mean(s_MULT**2))

# ============================================================
# MODEL 3: ΛCDM anchored to SH0ES H0=73.0, Ω_m free (k=1)
# "Fair" baseline: same H0 anchor as H_MULT
# ============================================================
res_shoes = minimize_scalar(lambda Om: chi2_lcdm(H0_SH0ES, Om), bounds=(0.1, 0.9), method="bounded")
Om_shoes_best = res_shoes.x
chi2_lcdm_shoes = res_shoes.fun
k_lcdm_shoes = 1

H_lcdm_shoes = H_lcdm(z_arr, H0_SH0ES, Om_shoes_best)
s_lcdm_shoes = (H_lcdm_shoes - H_obs) / sigma_H
rms_lcdm_shoes = np.sqrt(np.mean(s_lcdm_shoes**2))


# ============================================================
# MODEL 4: ΛCDM free H0 + Ω_m (k=2) — same DoF as H_MULT
# ============================================================
def chi2_lcdm_free(params):
    H0, Om = params
    if Om <= 0 or Om >= 1 or H0 <= 0:
        return 1e10
    return chi2_lcdm(H0, Om)


res_free = minimize(
    chi2_lcdm_free,
    [70.0, 0.30],
    method="Nelder-Mead",
    options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 5000},
)
H0_free, Om_free = res_free.x
chi2_lcdm_free_val = res_free.fun
k_lcdm_free = 2

H_lcdm_free_pred = H_lcdm(z_arr, H0_free, Om_free)
s_lcdm_free = (H_lcdm_free_pred - H_obs) / sigma_H
rms_lcdm_free = np.sqrt(np.mean(s_lcdm_free**2))

# ============================================================
# MODEL 5: ΛCDM_SH0ES as "anchor-equivalent" — H0=73.0 fixed,
#          Om fitted. Same # of fitted params as H_MULT (k=2)
#          if we count the anchor as 0 extra params, or k=1
#          Compute both k=1 and k=2 for comparison.
# ============================================================

# ============================================================
# PRINT RESULTS
# ============================================================
DIV = "=" * 72


def row(name, chi2, k, chi2_ex0=None, rms=None):
    a = aic(chi2, k)
    b = bic(chi2, k, n)
    rms_str = f"{rms:.3f}" if rms is not None else "  ---"
    return f"  {name:<32} chi2={chi2:7.3f}  k={k}  AIC={a:7.3f}  BIC={b:7.3f}  RMS_sigma={rms_str}"


print(f"\n{DIV}")
print("  FAIRNESS DIAGNOSTICS — H_MULT vs ΛCDM")
print(f"  n={n} data points | AIC=chi2+2k | BIC=chi2+k*ln({n})")
print(DIV)

print("\n  [A] CHI^2 FROM REPORTED SIGMA COLUMNS")
print(f"  {'Model':<32} {'chi2':>8} {'k':>3} {'AIC':>8} {'BIC':>8}  RMS_sigma")
print(f"  {'-' * 68}")
print(row("ΛCDM Planck (vanilla, k=0)", chi2_lcdm_planck, k_lcdm_planck, rms=rms_lcdm_planck))
print(row("H_MULT reported (k=2)", chi2_mult_reported, k_mult_reported, rms=rms_mult_reported))

print("\n  [B] ΛCDM FITTED — fair baselines")
print(f"  {'Model':<32} {'chi2':>8} {'k':>3} {'AIC':>8} {'BIC':>8}  RMS_sigma | best params")
print(f"  {'-' * 68}")
print(
    row("ΛCDM SH0ES H0=73.0 (k=1)", chi2_lcdm_shoes, k_lcdm_shoes, rms=rms_lcdm_shoes)
    + f"  Om={Om_shoes_best:.4f}"
)
print(
    row("ΛCDM free H0+Om (k=2)", chi2_lcdm_free_val, k_lcdm_free, rms=rms_lcdm_free)
    + f"  H0={H0_free:.2f} Om={Om_free:.4f}"
)
print(row("H_MULT reported (k=2)", chi2_mult_reported, k_mult_reported, rms=rms_mult_reported))

print("\n  [C] DELTA AIC (positive = model wins vs H_MULT)")


def delta(chi2_ref, k_ref, chi2_mult, k_mult):
    return aic(chi2_ref, k_ref) - aic(chi2_mult, k_mult)


print(
    f"  ΔAIC (ΛCDM Planck vs H_MULT)    = {delta(chi2_lcdm_planck, k_lcdm_planck, chi2_mult_reported, k_mult_reported):+.2f}"
)
print(
    f"  ΔAIC (ΛCDM SH0ES k=1 vs H_MULT) = {delta(chi2_lcdm_shoes, k_lcdm_shoes, chi2_mult_reported, k_mult_reported):+.2f}"
)
print(
    f"  ΔAIC (ΛCDM free k=2 vs H_MULT)  = {delta(chi2_lcdm_free_val, k_lcdm_free, chi2_mult_reported, k_mult_reported):+.2f}"
)

print("\n  Jeffreys scale: |ΔAIC| < 2 = negligible | 2–6 = positive | >10 = decisive")

print("\n  [D] ANCHOR EFFECT — z=0 row isolated")
chi2_lcdm_no0 = chi2_from_residuals(s_FLRW[1:])
chi2_mult_no0 = chi2_from_residuals(s_MULT[1:])
print(f"  χ²_ΛCDM_Planck without z=0: {chi2_lcdm_no0:.3f}  (was {chi2_lcdm_planck:.3f})")
print(f"  χ²_H_MULT      without z=0: {chi2_mult_no0:.3f}  (was {chi2_mult_reported:.3f})")
print(
    f"  z=0 row contributes {chi2_lcdm_planck - chi2_lcdm_no0:.1f} to ΛCDM chi2 ({(chi2_lcdm_planck - chi2_lcdm_no0) / chi2_lcdm_planck * 100:.0f}%)"
)
print(
    f"  z=0 row contributes {chi2_mult_reported - chi2_mult_no0:.4f} to H_MULT chi2 ({(chi2_mult_reported - chi2_mult_no0) / max(chi2_mult_reported, 1e-9) * 100:.1f}%) [anchor = 0 by construction]"
)

print("\n  ΔAIC (ΛCDM SH0ES vs H_MULT), EXCLUDING z=0:")
chi2_shoes_no0 = chi2_from_residuals(s_lcdm_shoes[1:])
chi2_free_no0 = chi2_from_residuals(s_lcdm_free[1:])
print(f"  ΛCDM SH0ES χ² excl. z=0: {chi2_shoes_no0:.3f}")
print(f"  ΛCDM free   χ² excl. z=0: {chi2_free_no0:.3f}")
# For fair n=11 comparison:
n11 = 11
print(
    f"  ΔAIC (ΛCDM SH0ES k=1 vs H_MULT k=2, n=11) = {aic(chi2_shoes_no0, 1) - aic(chi2_mult_no0, 2):+.2f}"
)
print(
    f"  ΔAIC (ΛCDM free k=2 vs H_MULT k=2, n=11)  = {aic(chi2_free_no0, 2) - aic(chi2_mult_no0, 2):+.2f}"
)

print("\n  [E] VERDICT")
delta_main = aic(chi2_lcdm_shoes, k_lcdm_shoes) - aic(chi2_mult_reported, k_mult_reported)
delta_no0 = aic(chi2_shoes_no0, 1) - aic(chi2_mult_no0, 2)

print(f"  Full dataset:  H_MULT wins vs ΛCDM_SH0ES by ΔAIC = {delta_main:.1f}")
print(f"  Excl. z=0:     H_MULT wins vs ΛCDM_SH0ES by ΔAIC = {delta_no0:.1f}")
print()
print("  z=0 ANCHOR UNFAIRNESS:")
print("    H_MULT: sigma_MULT(z=0) = 0.0 by construction (anchor placed at H_obs)")
print(f"    ΛCDM Planck: sigma_FLRW(z=0) = {s_FLRW[0]:.1f} (SH0ES tension)")
print(f"    ΛCDM SH0ES:  sigma_LCDM(z=0) = {s_lcdm_shoes[0]:.3f} (same anchor)")
print()
print(f"  ΛCDM SH0ES best Om = {Om_shoes_best:.4f}")
print(f"  ΛCDM free best: H0={H0_free:.2f}, Om={Om_free:.4f}")
print()
print("  KEY FINDING: The 'better fit' of H_MULT over vanilla ΛCDM is")
print(
    f"    {(chi2_lcdm_planck - chi2_lcdm_no0) / chi2_lcdm_planck * 100:.0f}% attributable to anchor choice (SH0ES vs Planck), not MULTING physics."
)
print(f"  After equalizing H0 anchor: ΔAIC = {delta_no0:.1f}", end="")
if delta_no0 > 10:
    print(" [H_MULT still decisive]")
elif delta_no0 > 2:
    print(" [H_MULT positive evidence]")
elif delta_no0 > -2:
    print(" [models statistically indistinguishable]")
else:
    print(" [ΛCDM competitive after anchor equalization]")

print(f"\n{DIV}\n")
