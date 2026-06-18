"""
beta_cv.py — 5-fold cross-validation of MULTING polynomial stability
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Test:
  Is the dipole coefficient B in H(z) = A(1+z)² + B(1+z)³ + C(1+z)⁴
  stable across data splits, or is it an overfitting artifact?

MULTING predicts: A > 0, B < 0 (dipole repels), C > 0
If B changes sign across folds → sign pattern is data-driven, not physics-driven.

Compared against: flat ΛCDM H(z) = H0 √(Ωm(1+z)³ + ΩΛ)
"""

import numpy as np
from scipy.optimize import curve_fit

np.random.seed(42)

# ── Moresco CC H(z) data ──────────────────────────────────────────────────────
# 27-point compilation (cosmic chronometers).
# Sources: Simon+2005, Stern+2010, Moresco+2012, Zhang+2014, Moresco+2015,
#          Moresco+2016, Moresco+2022 (arXiv:2201.07241).
# OUR_RECONSTRUCTION — cross-check against published tables before citing.
z_obs = np.array(
    [
        0.07,
        0.09,
        0.12,
        0.17,
        0.179,
        0.199,
        0.20,
        0.27,
        0.28,
        0.352,
        0.38,
        0.40,
        0.4004,
        0.4247,
        0.4497,
        0.47,
        0.4783,
        0.48,
        0.593,
        0.68,
        0.781,
        0.875,
        0.88,
        0.90,
        1.037,
        1.30,
        1.363,
    ]
)
H_obs = np.array(
    [
        69.0,
        69.0,
        68.6,
        83.0,
        75.0,
        75.0,
        72.9,
        77.0,
        88.8,
        83.0,
        83.0,
        95.0,
        77.0,
        87.1,
        92.8,
        89.0,
        80.9,
        97.0,
        104.0,
        92.0,
        105.0,
        125.0,
        90.0,
        117.0,
        154.0,
        168.0,
        160.0,
    ]
)
sigma_obs = np.array(
    [
        19.6,
        12.0,
        26.2,
        8.0,
        4.0,
        5.0,
        29.6,
        14.0,
        36.6,
        14.0,
        13.5,
        17.0,
        10.2,
        11.2,
        12.9,
        50.0,
        9.0,
        62.0,
        13.0,
        8.0,
        12.0,
        17.0,
        40.0,
        23.0,
        20.0,
        17.0,
        33.6,
    ]
)
N = len(z_obs)
assert N == 27, f"Expected 27 data points, got {N}"


# ── Model definitions ─────────────────────────────────────────────────────────
def multing_poly(z, A, B, C):
    """Unconstrained MULTING polynomial. Signs let free to data.
    MULTING theory predicts: A > 0, B < 0, C > 0.
    """
    x = 1.0 + z
    return A * x**2 + B * x**3 + C * x**4


def lcdm(z, H0, omega_m):
    """Flat ΛCDM: H(z) = H0 sqrt(Ωm(1+z)³ + ΩΛ)."""
    return H0 * np.sqrt(omega_m * (1.0 + z) ** 3 + (1.0 - omega_m))


# ── Full-data baseline fit ────────────────────────────────────────────────────
print("=" * 65)
print("MULTING β-stability test via 5-fold cross-validation")
print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
print("=" * 65)

try:
    popt_m, pcov_m = curve_fit(
        multing_poly,
        z_obs,
        H_obs,
        sigma=sigma_obs,
        absolute_sigma=True,
        p0=[50.0, -10.0, 5.0],
        maxfev=20000,
    )
    A0, B0, C0 = popt_m
    perr_m = np.sqrt(np.diag(pcov_m))
    H_m_full = multing_poly(z_obs, *popt_m)
    chi2_m_full = np.sum(((H_obs - H_m_full) / sigma_obs) ** 2)
    aic_m = chi2_m_full + 2 * 3  # 3 free parameters
except RuntimeError as exc:
    raise RuntimeError(f"Full-data MULTING fit failed: {exc}") from exc

try:
    popt_l, _ = curve_fit(
        lcdm,
        z_obs,
        H_obs,
        sigma=sigma_obs,
        absolute_sigma=True,
        p0=[70.0, 0.30],
        bounds=([50.0, 0.05], [100.0, 1.0]),
    )
    H0_full, Om_full = popt_l
    H_l_full = lcdm(z_obs, *popt_l)
    chi2_l_full = np.sum(((H_obs - H_l_full) / sigma_obs) ** 2)
    aic_l = chi2_l_full + 2 * 2  # 2 free parameters
except RuntimeError as exc:
    raise RuntimeError(f"Full-data ΛCDM fit failed: {exc}") from exc

sign_ok = A0 > 0 and B0 < 0 and C0 > 0
sign_label = (
    "[+,−,+] ✓ MULTING"
    if sign_ok
    else f"[{'+' if A0 > 0 else '−'},{'+' if B0 > 0 else '−'},{'+' if C0 > 0 else '−'}] ✗ not MULTING"
)

print(f"\nFull-data fit (n={N}):")
print(
    f"  MULTING: A={A0:.2f}±{perr_m[0]:.1f},  B={B0:.2f}±{perr_m[1]:.1f},  C={C0:.3f}±{perr_m[2]:.3f}"
)
print(f"  Sign pattern: {sign_label}")
print(f"  χ²(MULTING)={chi2_m_full:.1f} / {N - 3} dof = {chi2_m_full / (N - 3):.2f}")
print(f"  χ²(ΛCDM)  ={chi2_l_full:.1f} / {N - 2} dof = {chi2_l_full / (N - 2):.2f}")
print(f"  ΔAIC(MULTING−ΛCDM) = {aic_m - aic_l:.2f}  (+ = ΛCDM preferred)")

# ── 5-fold cross-validation ───────────────────────────────────────────────────
perm = np.random.permutation(N)
fold_size = N // 5
n_folds = 5

B_folds = []
chi2_m_cv = []
chi2_l_cv = []

print(f"\n5-fold cross-validation (seed=42, fold_size≈{fold_size}):")
print(f"{'Fold':>4} | {'B (dipole)':>12} | {'sign':>8} | {'χ²_test M':>10} | {'χ²_test Λ':>10}")
print("-" * 60)

for fold in range(n_folds):
    test_mask = np.zeros(N, dtype=bool)
    start, end = fold * fold_size, (fold + 1) * fold_size
    test_mask[perm[start:end]] = True
    train_mask = ~test_mask

    z_tr, H_tr, s_tr = z_obs[train_mask], H_obs[train_mask], sigma_obs[train_mask]
    z_te, H_te, s_te = z_obs[test_mask], H_obs[test_mask], sigma_obs[test_mask]

    # MULTING fit on train
    try:
        pm, _ = curve_fit(
            multing_poly,
            z_tr,
            H_tr,
            sigma=s_tr,
            absolute_sigma=True,
            p0=[A0, B0, C0],
            maxfev=20000,
        )
        B_folds.append(pm[1])
        c2m = np.sum(((H_te - multing_poly(z_te, *pm)) / s_te) ** 2)
        chi2_m_cv.append(c2m)
        b_label = f"{pm[1]:>12.2f}"
        s_label = "✓ (<0)" if pm[1] < 0 else "✗ (>0)"
        c2m_label = f"{c2m:>10.2f}"
    except RuntimeError:
        B_folds.append(np.nan)
        chi2_m_cv.append(np.nan)
        b_label = f"{'FAILED':>12}"
        s_label = "?"
        c2m_label = "?"

    # ΛCDM fit on train
    try:
        pl, _ = curve_fit(
            lcdm,
            z_tr,
            H_tr,
            sigma=s_tr,
            absolute_sigma=True,
            p0=[H0_full, Om_full],
            bounds=([50.0, 0.05], [100.0, 1.0]),
        )
        c2l = np.sum(((H_te - lcdm(z_te, *pl)) / s_te) ** 2)
        chi2_l_cv.append(c2l)
        c2l_label = f"{c2l:>10.2f}"
    except RuntimeError:
        chi2_l_cv.append(np.nan)
        c2l_label = "?"

    print(f"{fold + 1:>4} | {b_label} | {s_label:>8} | {c2m_label} | {c2l_label}")

# ── Stability verdict ─────────────────────────────────────────────────────────
B_arr = np.array([b for b in B_folds if not np.isnan(b)])
c2m_arr = np.array([c for c in chi2_m_cv if not np.isnan(c)])
c2l_arr = np.array([c for c in chi2_l_cv if not np.isnan(c)])

n_sign_changes = int(np.sum(np.diff(np.sign(B_arr)) != 0))
cv_B = abs(B_arr.std() / B_arr.mean()) if B_arr.mean() != 0 else np.inf

if n_sign_changes > 0:
    stability = "UNSTABLE — B changes sign across folds → dipole term is data-driven artifact"
elif cv_B > 0.5:
    stability = f"MARGINAL — sign stable but high variance (CV={cv_B:.0%}) → weak constraint on B"
else:
    stability = f"STABLE — B consistently {'<' if B_arr.mean() < 0 else '>'}0 (CV={cv_B:.0%})"

print("\nβ-coefficient stability:")
print(f"  B across folds: {np.round(B_arr, 2)}")
print(f"  mean={B_arr.mean():.2f}, std={B_arr.std():.2f}, CV={cv_B:.0%}")
print(f"  Sign changes: {n_sign_changes}")
print(f"\n  VERDICT: {stability}")

print("\nOut-of-sample χ² comparison:")
print(f"  MULTING mean χ²_test = {c2m_arr.mean():.2f} ± {c2m_arr.std():.2f}")
print(f"  ΛCDM    mean χ²_test = {c2l_arr.mean():.2f} ± {c2l_arr.std():.2f}")
ratio = c2m_arr.mean() / c2l_arr.mean() if c2l_arr.mean() > 0 else np.nan
if c2l_arr.mean() < c2m_arr.mean():
    oos_verdict = f"ΛCDM generalizes better (MULTING χ²_test is {ratio:.2f}× larger)"
else:
    oos_verdict = "MULTING generalizes as well or better than ΛCDM"
print(f"  OOS verdict: {oos_verdict}")

print("\n[OUR_RECONSTRUCTION] Data embedded from standard CC compilation.")
print("Cross-check z/H/sigma values against Moresco+2022 (arXiv:2201.07241) Table 1.")
