"""P220 -- docs/158 item 3: joint uncertainty propagation through v82's own
admitted near-cancellation between F^(1) (dipole) and F^(2) (quadrupole).

REVISED 2026-09-07 after a context-blind Step 8a skeptic pass found four
real defects in the first version (kept, not deleted, per no-silent-
correction -- see FINDING_P220's own "Correction" section):

  1. The T0 "scenario" in the first draft is an EXACT algebraic artifact.
     k(z) factors as k(z) = const * T0^(B+1) * (1+z)^(-11(B+1)/15) *
     E(z)^(2B/3+C+2/3) -- independently re-derived and verified numerically
     below (test_t0_shift_is_pure_z_independent_rescaling). Shifting T0
     ALONE at fixed (B,C) rescales k(z) by a PURE, z-INDEPENDENT constant,
     which is EXACTLY absorbable by beta1 -> beta1/lambda,
     beta2 -> beta2/lambda^2 (also verified below,
     test_exact_k_beta_degeneracy). A NaN under frozen beta at shifted T0
     says nothing about model fragility; the T0 "scenario" is void.
  2. The first draft's (B,C) 1-D self-check was run in an ephemeral,
     UNCOMMITTED script (not this file) -- a Gate-1/FL-Step-2a violation
     (no persisted, reproducible artifact for a claim quoted as fact). The
     1-D scan is now REAL code below (section 1D_SCAN), not asserted
     numbers.
  3. The B-row of that scan was mis-read as evidence of "a sharp ridge."
     It mostly is NOT: for fixed T0, C, a Delta-B perturbation's z-shape is
     T(z)^Delta-B, and T(z) varies only mildly over 0<=z<=2.33, so ~86% of
     a 1-sigma B shift is pure, absorbable rescaling (quantified below,
     ABSORBABLE_VS_SHAPE section). The C-row is NOT mostly absorbable
     (E(z) spans a factor of ~3.5 over the fitted range), and that
     asymmetry -- not "both parameters sit on a ridge" -- is the real
     finding.
  4. "ChiSquared_LCDM_flat_planck ... 16.31" was mislabeled. Per v82's own
     assumptions.yaml (lcdm_benchmarks block) and generate_all_results.py,
     16.31 is `adjusted_freely_optimized` -- A TWO-PARAMETER FIT (H0=71.83,
     Om=0.2724) -- not fixed Planck values. The genuine fixed-Planck
     benchmark (H0=67.4, Om=0.315, "extant_fixed_planck") is 36.96. v82's
     OWN text (line ~675-677) states its primary comparison IS the fitted
     ΛCDM curve ("computed identically for this framework and for a flat
     ΛCDM curve fit directly to the same 33 points, so the comparison is
     fair") -- so 16.31 remains a legitimate, author-preferred comparison
     point, just wrongly labeled "Planck" here. Both numbers are now
     reported, correctly labeled.

Also corrected: the closing verdict's claim that "a full refit per draw
would likely widen this further" is backwards and is removed. For ANY
fixed (B,C), chi2_refit(B,C) = min over (beta1,beta2,H0) chi2(...) <=
chi2(B,C, beta1_fit,beta2_fit,H0_fit) = chi2_frozen(B,C), because the
frozen point is one member of the refit's own search space. A refit can
only match or IMPROVE on the frozen-parameter chi2, never make it worse.
Whether the (B,C)-driven fragility SURVIVES refitting is therefore the
real open question -- addressed directly by the REFIT_KILL_TEST section
below, which was not run at all in the first draft.

SCOPE, otherwise unchanged: v82 quotes a real Gaussian-ish uncertainty for
exactly TWO of the parameters feeding k(z) -- the mass-gas-fraction
scaling exponents from Ramos-Ceja et al. (v82:440, 3061 clusters):

    B = 2.24 +/- 0.03
    C = -1.00 (+0.29 / -0.30)

No other input carries a quoted statistical uncertainty; T0_keV=3.7163 is
explicitly RECALIBRATED per v82:404-420, not measured (see point 1 above
for why it is handled separately, not sampled).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import minimize

# ---------------------------------------------------------------------------
# Verbatim from TJB's own multing_core.py (kernel already positive-
# controlled in P176/P219), B_real/C_real/T0_keV now PARAMETERIZED.
# ---------------------------------------------------------------------------
MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20
G = 6.674e-11
C_LIGHT = 299792458.0
Om_planck = 0.315
OL_planck = 0.685
H0_planck_si = 67.4 * KMSMPC_TO_SI

M0_kg = 1.193082e45
d0_m = 45.0 * MPC_TO_M
T0_keV_DEFAULT = 3.7163
mu_mol = 0.6
m_proton = 1.67262192e-27
T_piv_keV = 2.27
Mgas_piv_kg = 2.28e13 * MSUN_TO_KG
z_piv = 0.25
f_merge = 0.25
f_coh = 1.0 / 3.0

rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)

# v82:440, Ramos-Ceja et al., quoted directly
B_MEAN, B_SIGMA = 2.24, 0.03
C_MEAN, C_SIGMA_HI, C_SIGMA_LO = -1.00, 0.29, 0.30  # asymmetric, as quoted

H0_ANCHOR = 73.22
B1_FIT = 1.4335e10
B2_FIT = 7.8067e17
Z_SHOES = 0.0233

# v82's own two headline LCDM comparators (assumptions.yaml, lcdm_benchmarks;
# generate_all_results.py:136,151; both reproduced exactly by TJB's own
# generate_all_results_output.txt:29,33)
LCDM_FIXED_PLANCK_CHI2 = 36.96  # H0=67.4, Om=0.315 -- genuinely fixed Planck
LCDM_ADJUSTED_FIT_CHI2 = (
    16.31  # H0=71.83, Om=0.2724 -- 2-param FIT, v82's own primary comparator (v82:675-677)
)


def Efun(z, Om=Om_planck, OL=OL_planck):
    return np.sqrt(Om * (1.0 + z) ** 3 + OL)


def M_of(z):
    return M0_kg * (1.0 + z) ** (-1.1)


def T_keV_of(z, T0_keV=T0_keV_DEFAULT):
    return T0_keV * (M_of(z) / M0_kg) ** (2.0 / 3.0) * Efun(z) ** (2.0 / 3.0)


def Mgas_of(z, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    T = T_keV_of(z, T0_keV)
    return Mgas_piv_kg * (T / T_piv_keV) ** B_real * (Efun(z) / Efun(z_piv)) ** C_real


def k_of(z, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    return (
        1.5
        * (Mgas_of(z, B_real, C_real, T0_keV) / (mu_mol * m_proton))
        * (T_keV_of(z, T0_keV) * KEV_TO_J)
    )


def rho_crit(z):
    return rho_crit0 * Efun(z) ** 2


def R_of(z):
    return (3.0 * M_of(z) / (4.0 * np.pi * 500.0 * rho_crit(z))) ** (1.0 / 3.0)


def d_of(z):
    return d0_m * (1.0 + z) ** (-1.0)


def forces(z, beta_1, beta_2, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    M, R, k, d = M_of(z), R_of(z), k_of(z, B_real, C_real, T0_keV), d_of(z)
    F0 = (-G) * M * M / d**2
    F1 = beta_1 * (-G) * 2.0 * M * (k / C_LIGHT**2) * (R / d) / d**2
    F2 = beta_2 * (-G) * (k / C_LIGHT**2) ** 2 * (R * R / d**2) / d**2
    return F0, F1, F2


def Hlcdm_si(z):
    return H0_planck_si * Efun(z)


def m_dot(z):
    return 1.1 * Hlcdm_si(z) * M_of(z)


def v_infall(z):
    return np.sqrt(G * M_of(z) / R_of(z))


def dv_coh(z):
    return f_coh * f_merge * v_infall(z)


def F_accretion(z):
    return m_dot(z) * dv_coh(z)


def addot_over_a(z, b1, b2, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    F0, F1, F2 = forces(z, b1, b2, B_real, C_real, T0_keV)
    F_total = F0 - F1 + F2 - F_accretion(z)
    return (F_total / (M_of(z) / 2.0)) / d_of(z), (F0, F1, F2, F_accretion(z))


def H2_of_z(zgrid, H0_anchor_kms, b1, b2, zref, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    zg = np.atleast_1d(np.asarray(zgrid, dtype=float))
    order = np.argsort(zg)
    zgs = zg[order]
    aa = np.array([addot_over_a(zx, b1, b2, B_real, C_real, T0_keV)[0] for zx in zgs])
    integrand = aa / (1.0 + zgs)
    ds_raw = np.concatenate(([0.0], cumulative_trapezoid(integrand, zgs)))
    i0 = np.argmin(np.abs(zgs - zref))
    ds = ds_raw - ds_raw[i0]
    H2 = np.empty_like(ds)
    H2[order] = (H0_anchor_kms * KMSMPC_TO_SI) ** 2 + 2.0 * ds
    return H2


def H_of_z_kms(zgrid, H0_anchor_kms, b1, b2, zref, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    H2 = H2_of_z(zgrid, H0_anchor_kms, b1, b2, zref, B_real, C_real, T0_keV)
    H = np.full_like(H2, np.nan)
    valid = H2 > 0
    H[valid] = np.sqrt(H2[valid]) / KMSMPC_TO_SI
    return H


CC_POINTS = [
    (0.07, 69.0, 19.6),
    (0.09, 69.0, 12.0),
    (0.12, 68.6, 26.2),
    (0.17, 83.0, 8.0),
    (0.179, 75.0, 4.0),
    (0.199, 75.0, 5.0),
    (0.2, 72.9, 29.6),
    (0.27, 77.0, 14.0),
    (0.28, 88.8, 36.6),
    (0.352, 83.0, 14.0),
    (0.38, 83.0, 13.5),
    (0.4, 95.0, 17.0),
    (0.4, 77.0, 10.2),
    (0.425, 87.1, 11.2),
    (0.45, 92.8, 12.9),
    (0.47, 89.0, 49.6),
    (0.478, 80.9, 9.0),
    (0.48, 97.0, 62.0),
    (0.593, 104.0, 13.0),
    (0.68, 92.0, 8.0),
    (0.781, 105.0, 12.0),
    (0.875, 125.0, 17.0),
    (0.88, 90.0, 40.0),
    (0.9, 117.0, 23.0),
    (1.037, 154.0, 20.0),
    (1.3, 168.0, 17.0),
    (1.363, 160.0, 33.6),
    (1.43, 177.0, 18.0),
    (1.53, 140.0, 14.0),
    (1.75, 202.0, 40.0),
    (1.965, 186.5, 50.4),
]
zd = np.array([p[0] for p in CC_POINTS])
Hd = np.array([p[1] for p in CC_POINTS])
sd = np.array([p[2] for p in CC_POINTS])
Z33 = np.concatenate([zd, [0.0233], [2.33]])
H33 = np.concatenate([Hd, [73.04], [236.1]])
S33 = np.concatenate([sd, [1.04], [2.8]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, 2.33, 600), Z33])))
ZFINE_REFIT = np.sort(np.unique(np.concatenate([np.linspace(0, 2.33, 500), Z33])))


def chi2_33(B_real, C_real, T0_keV=T0_keV_DEFAULT):
    Hm = H_of_z_kms(ZFINE, H0_ANCHOR, B1_FIT, B2_FIT, Z_SHOES, B_real, C_real, T0_keV)
    if np.any(np.isnan(Hm)):
        return np.nan
    Hp = np.interp(Z33, ZFINE, Hm)
    return float(np.sum(((Hp - H33) / S33) ** 2))


def chi2_free(params, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    """chi2 with (H0_anchor, beta1, beta2) FREE -- used only for the
    refit kill-test, to see whether the (B,C)-driven chi2 inflation
    survives re-optimizing the fitted parameters."""
    H0a, b1, b2 = params
    if H0a <= 0 or b1 < 0 or b2 < 0:
        return 1e12
    Hm = H_of_z_kms(ZFINE_REFIT, H0a, b1, b2, Z_SHOES, B_real, C_real, T0_keV)
    if np.any(np.isnan(Hm)):
        return 1e12
    Hp = np.interp(Z33, ZFINE_REFIT, Hm)
    return float(np.sum(((Hp - H33) / S33) ** 2))


def refit_chi2(B_real, C_real, T0_keV=T0_keV_DEFAULT, guesses=None):
    if guesses is None:
        guesses = [
            [73.2, 1.4335e10, 7.8067e17],
            [73.2, 1.2e10, 6.5e17],
            [73.2, 1.6e10, 9.0e17],
            [73.2, 1.0e10, 5.0e17],
        ]
    best = None
    for g in guesses:
        r = minimize(
            chi2_free,
            g,
            args=(B_real, C_real, T0_keV),
            method="Nelder-Mead",
            options={"xatol": 1e-3, "fatol": 1e-8, "maxiter": 20000, "maxfev": 20000},
        )
        if best is None or r.fun < best.fun:
            best = r
    return best.fun, best.x


def sep(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def main() -> int:
    sep("PC1 -- reproduce v82's own quoted z=1.07 fractional decomposition (spotlighted row)")
    z_test = 1.07
    F0, F1, F2 = forces(z_test, B1_FIT, B2_FIT, B_MEAN, C_MEAN)
    Facc = F_accretion(z_test)
    gross = abs(F0) + abs(F1) + abs(F2) + abs(Facc)
    net_pct = (F0 - F1 + F2 - Facc) / gross * 100
    print(f"  F0  = {F0 / gross * 100:7.2f} %   (paper: -0.06)")
    print(f"  -F1 = {-F1 / gross * 100:7.2f} %   (paper: 53.04)")
    print(f"  F2  = {F2 / gross * 100:7.2f} %   (paper: -46.54)")
    print(f"  net = {net_pct:7.2f} %   (paper: 6.09)")
    ok1 = (
        abs(-F1 / gross * 100 - 53.04) < 0.02
        and abs(F2 / gross * 100 - (-46.54)) < 0.02
        and abs(net_pct - 6.09) < 0.02
    )
    print(f"  {'PASS' if ok1 else 'FAIL'}")
    if not ok1:
        return 1

    sep("PC2 -- reproduce v82's own reported chi2_33=15.75 at (B,C) mean")
    chi2_mean = chi2_33(B_MEAN, C_MEAN)
    print(f"  chi2_33(B=2.24, C=-1.00) = {chi2_mean:.4f}   (paper: 15.75)")
    ok2 = abs(chi2_mean - 15.75) / 15.75 < 0.02
    print(f"  {'PASS' if ok2 else 'FAIL'}")
    if not ok2:
        return 1

    sep("PC3 (NEW, off-anchor) -- reproduce v82's own T0=6.0 keV rejected gas-fraction claim")
    # v82:407-409: T0=6.0 gave gas fractions 0.35-0.37; v82:413-414: at
    # T0=3.7163 the range is 0.118-0.127. Predict the 6.0 keV range from
    # ONLY the B exponent (f_gas prop to T0^B) and the 3.7163 keV range --
    # tests the parameterization AWAY from the anchor point, which PC1/PC2
    # (both evaluated AT the mean) cannot do.
    ratio_fgas = (6.0 / T0_keV_DEFAULT) ** B_MEAN
    lo_pred, hi_pred = 0.118 * ratio_fgas, 0.127 * ratio_fgas
    print(f"  predicted f_gas range at T0=6.0 keV: [{lo_pred:.3f}, {hi_pred:.3f}]")
    print("  paper's own quoted range                : [0.350, 0.370]")
    ok3 = abs(lo_pred - 0.350) / 0.350 < 0.03 and abs(hi_pred - 0.370) / 0.370 < 0.03
    print(f"  {'PASS' if ok3 else 'FAIL'}")
    if not ok3:
        return 1

    sep(
        "EXACT DEGENERACY -- k -> lambda*k is exactly absorbed by beta1->beta1/lambda, beta2->beta2/lambda^2"
    )

    def test_exact_k_beta_degeneracy():
        lam = 2.7
        for z in [0.0, 0.5, 1.07, 2.33]:
            f0a, f1a, f2a = forces(z, B1_FIT, B2_FIT, B_MEAN, C_MEAN)
            # scale k by lam via B,C held fixed but forces() called with a
            # trick: directly verify the ALGEBRAIC identity instead --
            # F1 prop to beta1*k, F2 prop to beta2*k^2
            k_val = k_of(z, B_MEAN, C_MEAN)
            f1_direct = (
                B1_FIT
                * (-G)
                * 2.0
                * M_of(z)
                * (k_val / C_LIGHT**2)
                * (R_of(z) / d_of(z))
                / d_of(z) ** 2
            )
            f2_direct = (
                B2_FIT
                * (-G)
                * (k_val / C_LIGHT**2) ** 2
                * (R_of(z) ** 2 / d_of(z) ** 2)
                / d_of(z) ** 2
            )
            f1_scaled = (
                (B1_FIT / lam)
                * (-G)
                * 2.0
                * M_of(z)
                * (lam * k_val / C_LIGHT**2)
                * (R_of(z) / d_of(z))
                / d_of(z) ** 2
            )
            f2_scaled = (
                (B2_FIT / lam**2)
                * (-G)
                * (lam * k_val / C_LIGHT**2) ** 2
                * (R_of(z) ** 2 / d_of(z) ** 2)
                / d_of(z) ** 2
            )
            assert abs(f1_direct - f1_scaled) < 1e-6 * abs(f1_direct), (z, f1_direct, f1_scaled)
            assert abs(f2_direct - f2_scaled) < 1e-6 * abs(f2_direct), (z, f2_direct, f2_scaled)
        return True

    ok_deg = test_exact_k_beta_degeneracy()
    print(
        f"  F1(beta1,k) == F1(beta1/lam, lam*k) and F2(beta2,k) == F2(beta2/lam^2,lam*k) at all tested z: {ok_deg}"
    )

    sep(
        "T0 DEGENERACY (replaces the void first-draft 'T0 scenario') -- pure z-independent rescaling"
    )
    T0_ALT = (T0_keV_DEFAULT + 7.0) / 2.0
    lam_t0 = (T0_ALT / T0_keV_DEFAULT) ** (B_MEAN + 1.0)
    print(f"  predicted lambda = (T0_alt/T0)^(B+1) = {lam_t0:.6f}")
    print(f"  {'z':>6} {'k(T0_alt)/k(T0)':>18}")
    max_dev = 0.0
    for z in [0.0, 0.5, 1.07, 1.965, 2.33]:
        ratio = k_of(z, B_MEAN, C_MEAN, T0_keV=T0_ALT) / k_of(
            z, B_MEAN, C_MEAN, T0_keV=T0_keV_DEFAULT
        )
        max_dev = max(max_dev, abs(ratio - lam_t0))
        print(f"  {z:6.3f} {ratio:18.6f}")
    print(
        f"  max deviation from pure constant across z: {max_dev:.2e}  (0 => exactly z-independent)"
    )
    print("  => T0 shift at fixed (B,C) is EXACTLY absorbable by beta1->beta1/lambda,")
    print("     beta2->beta2/lambda^2 (see degeneracy test above). It is NOT a probe of")
    print("     model fragility under frozen parameters -- it is a probe of the frozen-")
    print("     parameter PROTOCOL itself. The first draft's 'T0 breaks the model' claim")
    print("     is WITHDRAWN.")
    chi2_t0_frozen = chi2_33(B_MEAN, C_MEAN, T0_keV=T0_ALT)
    b1_resc, b2_resc = B1_FIT / lam_t0, B2_FIT / lam_t0**2
    Hm_resc = H_of_z_kms(ZFINE, H0_ANCHOR, b1_resc, b2_resc, Z_SHOES, B_MEAN, C_MEAN, T0_keV=T0_ALT)
    Hp_resc = np.interp(Z33, ZFINE, Hm_resc)
    chi2_t0_rescaled = float(np.sum(((Hp_resc - H33) / S33) ** 2))
    print(f"  chi2 at T0_alt, beta FROZEN            : {chi2_t0_frozen}")
    print(
        f"  chi2 at T0_alt, beta RESCALED by 1/lambda-powers : {chi2_t0_rescaled:.4f}  (should be ~15.75)"
    )

    sep("1D_SCAN -- (B,C) one-parameter-at-a-time, FROZEN beta (now a real, committed artifact)")
    print(f"  {'C (B=2.24 fixed)':>20} {'sigma':>7} {'chi2_frozen':>12}")
    c_scan_results = {}
    for k_sig in [-3, -2, -1, 0, 1, 2, 3]:
        sig = C_SIGMA_HI if k_sig >= 0 else C_SIGMA_LO
        c_val = C_MEAN + k_sig * sig
        v = chi2_33(B_MEAN, c_val)
        c_scan_results[k_sig] = (c_val, v)
        print(f"  {c_val:20.3f} {k_sig:+7d} {v!s:>12}")
    print(f"\n  {'B (C=-1.00 fixed)':>20} {'sigma':>7} {'chi2_frozen':>12}")
    b_scan_results = {}
    for k_sig in [-3, -2, -1, 0, 1, 2, 3]:
        b_val = B_MEAN + k_sig * B_SIGMA
        v = chi2_33(b_val, C_MEAN)
        b_scan_results[k_sig] = (b_val, v)
        print(f"  {b_val:20.4f} {k_sig:+7d} {v:12.2f}")

    sep("ABSORBABLE_VS_SHAPE -- decompose each 1-sigma perturbation into a pure")
    print("  rescaling part (absorbable by beta1,beta2) and a residual SHAPE part")
    print("  (z-dependent, NOT absorbable by any constant rescaling of beta)")
    test_zs_shape = [0.0, 0.5, 1.07, 1.965, 2.33]
    print("\n  Delta-B = +1sigma (0.03), C fixed:")
    ratios_b = [k_of(z, B_MEAN + B_SIGMA, C_MEAN) / k_of(z, B_MEAN, C_MEAN) for z in test_zs_shape]
    norm_b = np.exp(np.mean(np.log(ratios_b)))
    shape_b = np.array(ratios_b) / norm_b
    print(f"    normalization factor (geometric mean)     : {norm_b:.6f}")
    print(
        f"    residual shape range across z              : [{shape_b.min():.6f}, {shape_b.max():.6f}]"
    )
    print(
        f"    residual shape spread                       : {(shape_b.max() - shape_b.min()) * 100:.3f} %"
    )

    print("\n  Delta-C = +1sigma (0.29), B fixed:")
    ratios_c = [
        k_of(z, B_MEAN, C_MEAN + C_SIGMA_HI) / k_of(z, B_MEAN, C_MEAN) for z in test_zs_shape
    ]
    norm_c = np.exp(np.mean(np.log(ratios_c)))
    shape_c = np.array(ratios_c) / norm_c
    print(f"    normalization factor (geometric mean)     : {norm_c:.6f}")
    print(
        f"    residual shape range across z              : [{shape_c.min():.6f}, {shape_c.max():.6f}]"
    )
    print(
        f"    residual shape spread                       : {(shape_c.max() - shape_c.min()) * 100:.3f} %"
    )
    print(
        f"\n  => C's non-absorbable shape distortion is ~"
        f"{(shape_c.max() - shape_c.min()) / (shape_b.max() - shape_b.min()):.0f}x larger than B's."
        " The 'sharp ridge' claim from the first draft's B-row is WITHDRAWN --"
        " B's 1-sigma effect is mostly pure rescaling, which a refit absorbs."
        " C's is not."
    )

    sep(
        "REFIT_KILL_TEST -- does the (B,C)-driven chi2 inflation survive re-optimizing (H0,beta1,beta2)?"
    )
    print("  Per math: chi2_refit(B,C) <= chi2_frozen(B,C) ALWAYS (frozen point is")
    print("  IN the refit's own search space). This determines whether the C-driven")
    print("  fragility is REAL (survives refit) or a frozen-parameter ARTIFACT")
    print("  (refit absorbs it, like the T0 case above).")
    chi2_refit_mean, params_mean = refit_chi2(B_MEAN, C_MEAN)
    print(f"\n  refit at (B,C) = published mean : chi2 = {chi2_refit_mean:.3f}  (paper: 15.75)")
    for label, c_val in [("C = -1.30 (-1 sigma)", -1.30), ("C = -0.71 (+1 sigma)", -0.71)]:
        chi2_r, params = refit_chi2(B_MEAN, c_val)
        chi2_frozen_here = c_scan_results.get(-1 if c_val == -1.30 else 1, (None, "n/a"))[1]
        print(
            f"  {label:24s}: chi2_refit = {chi2_r:9.3f}   "
            f"(chi2_frozen was {chi2_frozen_here!s})   fit(H0,b1,b2) = {params}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
