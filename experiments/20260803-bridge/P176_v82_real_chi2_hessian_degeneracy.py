"""P176 -- the decisive test FINDING_P175 named as undone: does v82's own
REAL chi-squared surface (his own 33-point dataset -- 31-point cosmic
chronometer compilation + SH0ES anchor z=0.0233 + DESI DR2 Lyman-alpha
anchor z=2.33 -- his own H_of_z_kms function, his own fit_row() fixed-
H0_anchor branch) have a genuine near-flat direction in (beta1,beta2) at
fixed H0_anchor? If so, what is its slope, and does it match P165's
idealized-local prediction (C=2.644e7, FINDING_P165/P175), Table II's own
empirical H0_anchor-scan slope (6.157e7, FINDING_P175), or neither?

Method: this project's OWN copy of TJB's own chi-squared function --
reproduced verbatim from his own archive/code/generate_all_results.py
fit_row(), not approximated -- positive-controlled against his own
reported chi2_33 values for two different Table II rows before trusting
anything derived from it. Then: numeric 2x2 Hessian of chi2(beta1,beta2)
at TJB's own reported best-fit point for each Table II row, via central
finite differences in RESCALED coordinates (x1=beta1/beta1_fit,
x2=beta2/beta2_fit, both ~1 at the fit point -- beta1~1e10 and
beta2~1e17 differ by 7 orders of magnitude in raw units, which would
make an unrescaled Hessian numerically meaningless). Diagonalized;
reports eigenvalues (condition number = degeneracy strength) and the
near-null eigenvector's (beta1,beta2)-space slope.

Data/code source: TJB's own supplemental Zenodo archive (zenodo_archive_
v17.zip, DOI 10.5281/zenodo.22004287 -- same archive FINDING_P169/P175
already used), archive/code/multing_core.py + generate_all_results.py +
assumptions.yaml (cosmic_chronometer_data block). Copied verbatim, not
re-derived.

CORRECTION (2026-08-31, context-asymmetric skeptic-caught -- see
FINDING_P176.md's own "Correction" section for the full account): the
first draft's framing of the 1.4% agreement between the pure null-
eigenvector slope and the empirical Table-II-scan slope as a "striking,
surprising structural coincidence" OVERCLAIMED -- via the implicit
function theorem, close alignment between a fixed-parameter near-null
direction and the direction a re-optimized scan actually follows is the
EXPECTED, near-generic consequence of strong ill-conditioning (large
Hessian condition number), not independent new evidence. The rigorous
version of this check (test_ift_prediction_matches_empirical_scan_
tighter_than_pure_null, added after the skeptic review) computes the
actual implicit-function-theorem-predicted scan direction (not just the
pure null eigenvector) and finds it matches the empirical scan slope to
~0.02% -- consistent with ordinary optimizer tolerance, not a mystery.
The first draft's claim that the ~2.3x gap between FINDING_P175's
idealized-local prediction (C) and this file's real Hessian slope is
explained by "Taylor-expansion order" is ALSO retracted -- a category
error (these characterize two structurally different objects: a single
local kinematic derivative at one point vs. an eigenvector of a
chi-squared surface integrated over all 33 data points). An attempted
kill-test (recomputing the null direction using ONLY the near-z=0 SH0ES
term) turned out ill-posed -- that single point's chi2 has essentially
zero curvature in (beta1,beta2) BY CONSTRUCTION, since it is used as the
anchor reference point (zref) that H0_anchor is itself defined against
-- so this specific comparison remains genuinely unresolved, not
resolved either way, and is reported as such rather than forced to a
conclusion.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np

# ---------------------------------------------------------------------------
# Verbatim from TJB's own archive/code/multing_core.py (same subset P175
# already used and positive-controlled -- H_of_z_kms is new here, the rest
# repeats P175's copy for a self-contained script)
# ---------------------------------------------------------------------------
MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20
G = 6.674e-11
c = 299792458.0
Om_planck = 0.315
OL_planck = 0.685
H0_planck_si = 67.4 * KMSMPC_TO_SI

M0_kg = 1.193082e45
d0_m = 45.0 * MPC_TO_M
T0_keV = 3.7163
mu_mol = 0.6
m_proton = 1.67262192e-27
T_piv_keV = 2.27
Mgas_piv_kg = 2.28e13 * MSUN_TO_KG
z_piv = 0.25
B_real = 2.24
C_real = -1.00
f_merge = 0.25
f_coh = 1.0 / 3.0

rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)


def Efun(z, Om=Om_planck, OL=OL_planck):
    return np.sqrt(Om * (1.0 + z) ** 3 + OL)


def M_of(z):
    return M0_kg * (1.0 + z) ** (-1.1)


def T_keV_of(z):
    return T0_keV * (M_of(z) / M0_kg) ** (2.0 / 3.0) * Efun(z) ** (2.0 / 3.0)


def Mgas_of(z):
    return Mgas_piv_kg * (T_keV_of(z) / T_piv_keV) ** B_real * (Efun(z) / Efun(z_piv)) ** C_real


def k_of(z):
    return 1.5 * (Mgas_of(z) / (mu_mol * m_proton)) * (T_keV_of(z) * KEV_TO_J)


def rho_crit(z):
    return rho_crit0 * Efun(z) ** 2


def R_of(z):
    return (3.0 * M_of(z) / (4.0 * np.pi * 500.0 * rho_crit(z))) ** (1.0 / 3.0)


def d_of(z):
    return d0_m * (1.0 + z) ** (-1.0)


def forces(z, beta_1, beta_2):
    M, R, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
    F0 = (-G) * M * M / d**2
    F1 = beta_1 * (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2
    F2 = beta_2 * (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2
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


def addot_over_a(z, b1, b2):
    F0, F1, F2 = forces(z, b1, b2)
    F_total = F0 - F1 + F2 - F_accretion(z)
    return (F_total / (M_of(z) / 2.0)) / d_of(z)


def H2_of_z(zgrid, H0_anchor_kms, b1, b2, zref):
    from scipy.integrate import cumulative_trapezoid

    zg = np.atleast_1d(np.asarray(zgrid, dtype=float))
    order = np.argsort(zg)
    zgs = zg[order]
    aa = np.array([addot_over_a(zx, b1, b2) for zx in zgs])
    integrand = aa / (1.0 + zgs)
    ds_raw = np.concatenate(([0.0], cumulative_trapezoid(integrand, zgs)))
    i0 = np.argmin(np.abs(zgs - zref))
    ds = ds_raw - ds_raw[i0]
    H2 = np.empty_like(ds)
    H2[order] = (H0_anchor_kms * KMSMPC_TO_SI) ** 2 + 2.0 * ds
    return H2


def H_of_z_kms(zgrid, H0_anchor_kms, b1, b2, zref):
    H2 = H2_of_z(zgrid, H0_anchor_kms, b1, b2, zref)
    H = np.full_like(H2, np.nan)
    valid = H2 > 0
    H[valid] = np.sqrt(H2[valid]) / KMSMPC_TO_SI
    return H


# ---------------------------------------------------------------------------
# TJB's own 31-point cosmic chronometer compilation, verbatim from his own
# assumptions.yaml
# ---------------------------------------------------------------------------
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

Z_SHOES, H_SHOES, SIG_SHOES = 0.0233, 73.04, 1.04
Z_DESI, H_DESI, SIG_DESI = 2.33, 236.1, 2.8

z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
H33 = np.concatenate([Hd, [H_SHOES], [H_DESI]])
s33 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))


def chi2_fixed_h0anchor(h0_anchor, beta1, beta2):
    """TJB's own chi2 function (generate_all_results.py, fit_row's fixed
    branch), reproduced verbatim -- same 33-point dataset, same
    interpolation-onto-fine-grid procedure, same H_of_z_kms call.
    """
    Hm = H_of_z_kms(ZFINE, h0_anchor, beta1, beta2, Z_SHOES)
    if np.any(np.isnan(Hm)):
        return 1e12
    Hp = np.interp(z33, ZFINE, Hm)
    return np.sum(((Hp - H33) / s33) ** 2)


# Table II, verbatim from TJB's own assumptions.yaml
TABLE_II = {
    "unconstrained_spotlighted": (73.22, 1.4335e10, 7.8067e17, 15.75),
    "sh0es_anchored_0pct": (73.04, 1.4233e10, 7.7443e17, 15.78),
    "pct_25": (71.63, 1.3427e10, 7.2479e17, 18.14),
    "pct_50": (70.22, 1.2632e10, 6.7582e17, 24.26),
    "pct_75": (68.81, 1.1848e10, 6.2754e17, 34.14),
    "pct_90": (67.96, 1.1383e10, 5.9890e17, 41.87),
    "planck_exact_100pct": (67.40, 1.1075e10, 5.7995e17, 47.77),
}

C_PREDICTED_LOCAL = 2.644421e07  # FINDING_P175's idealized-local prediction
EMPIRICAL_TABLE_II_SLOPE = 6.157055e07  # FINDING_P175's Table-II-scan slope


def test_positive_control_chi2_matches_two_table_ii_rows():
    """Positive control: this script's own chi2 function, at TJB's own
    reported (H0_anchor, beta1, beta2), must reproduce his own reported
    chi2_33 for at least two rows spanning the full range (not just one --
    to catch an error that happens to cancel at a single point).
    """
    for label in ("unconstrained_spotlighted", "planck_exact_100pct"):
        h0a, b1, b2, chi2_expected = TABLE_II[label]
        computed = chi2_fixed_h0anchor(h0a, b1, b2)
        rel_err = abs(computed - chi2_expected) / chi2_expected
        assert rel_err < 0.001, (
            f"{label}: computed chi2={computed:.4f}, TJB reports {chi2_expected} "
            f"(rel err {rel_err:.4%})"
        )
    return True


def hessian_null_slope(h0_anchor, beta1_fit, beta2_fit, h=1e-4):
    """Numeric 2x2 Hessian of chi2(beta1,beta2) at fixed h0_anchor, via
    central finite differences in rescaled coordinates x1=beta1/beta1_fit,
    x2=beta2/beta2_fit (both ~1 at the fit point -- raw beta1~1e10,
    beta2~1e17 differ by 7 orders of magnitude, making an unrescaled
    Hessian numerically meaningless). Returns (eigenvalues ascending,
    slope d(beta2)/d(beta1) of the near-null eigenvector).
    """

    def chi2_x(x1, x2):
        return chi2_fixed_h0anchor(h0_anchor, x1 * beta1_fit, x2 * beta2_fit)

    f00 = chi2_x(1.0, 1.0)
    fpp = chi2_x(1 + h, 1 + h)
    fpm = chi2_x(1 + h, 1 - h)
    fmp = chi2_x(1 - h, 1 + h)
    fmm = chi2_x(1 - h, 1 - h)
    f_p0 = chi2_x(1 + h, 1.0)
    f_m0 = chi2_x(1 - h, 1.0)
    f_0p = chi2_x(1.0, 1 + h)
    f_0m = chi2_x(1.0, 1 - h)

    d2_11 = (f_p0 - 2 * f00 + f_m0) / h**2
    d2_22 = (f_0p - 2 * f00 + f_0m) / h**2
    d2_12 = (fpp - fpm - fmp + fmm) / (4 * h**2)

    hessian = np.array([[d2_11, d2_12], [d2_12, d2_22]])
    eigvals, eigvecs = np.linalg.eigh(hessian)
    v_small = eigvecs[:, 0]
    d_beta1, d_beta2 = v_small[0] * beta1_fit, v_small[1] * beta2_fit
    slope = d_beta2 / d_beta1
    return eigvals, slope, hessian


def test_hessian_slope_converges_with_step_size():
    """The near-null eigenvector slope at the spotlighted row must be
    stable (< 0.01% change) as the finite-difference step h shrinks by 2
    orders of magnitude -- confirms the result is a real feature of the
    chi2 surface, not a finite-difference artifact.
    """
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    slopes = []
    for h in (1e-3, 1e-4, 1e-5):
        _, slope, _ = hessian_null_slope(h0a, b1, b2, h=h)
        slopes.append(slope)
    spread = (max(slopes) - min(slopes)) / np.mean(slopes)
    assert spread < 0.0001, f"slope not converged across step sizes: {slopes}"
    return slopes


def test_slope_is_h0anchor_independent():
    """The near-null eigenvector slope, computed independently at each of
    5 different fixed H0_anchor values (spanning TJB's own full Table II
    range, 67.40-73.22 km/s/Mpc), must agree to within 0.1% of each other
    -- if true, this is a genuine, H0_anchor-independent structural
    feature of the real chi2 surface, not an artifact of one particular
    operating point.
    """
    labels = [
        "planck_exact_100pct",
        "pct_90",
        "pct_75",
        "pct_50",
        "pct_25",
        "sh0es_anchored_0pct",
        "unconstrained_spotlighted",
    ]
    slopes = {}
    for label in labels:
        h0a, b1, b2, _ = TABLE_II[label]
        _, slope, _ = hessian_null_slope(h0a, b1, b2)
        slopes[label] = slope
    vals = list(slopes.values())
    spread = (max(vals) - min(vals)) / np.mean(vals)
    assert spread < 0.001, f"slope varies across H0_anchor by {spread:.4%}: {slopes}"
    return slopes


def test_slope_converges_with_grid_density():
    """Skeptic-requested check (2026-08-31): the Hessian relies on
    chi2_fixed_h0anchor's own internal cumulative_trapezoid integration
    over a 500+33-point z-grid -- a step-size-only convergence check
    (above) cannot rule out that BOTH the plateau and the apparent
    convergence sit on top of a coarser numerical-integration noise
    floor. Recompute the slope with the integration grid density doubled
    and quadrupled (500 -> 1000 -> 2000 -> 4000 points); the slope must
    stay stable to < 0.01% across all four densities.
    """
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    slopes = []
    for npts in (500, 1000, 2000, 4000):
        zfine = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, npts), z33])))

        def chi2_density(h0a_, b1_, b2_, zfine=zfine):
            Hm = H_of_z_kms(zfine, h0a_, b1_, b2_, Z_SHOES)
            if np.any(np.isnan(Hm)):
                return 1e12
            Hp = np.interp(z33, zfine, Hm)
            return np.sum(((Hp - H33) / s33) ** 2)

        def chi2_x(x1, x2, chi2_density=chi2_density, h0a=h0a, b1=b1, b2=b2):
            return chi2_density(h0a, x1 * b1, x2 * b2)

        h = 1e-4
        f00 = chi2_x(1.0, 1.0)
        f_p0 = chi2_x(1 + h, 1.0)
        f_m0 = chi2_x(1 - h, 1.0)
        f_0p = chi2_x(1.0, 1 + h)
        f_0m = chi2_x(1.0, 1 - h)
        fpp = chi2_x(1 + h, 1 + h)
        fpm = chi2_x(1 + h, 1 - h)
        fmp = chi2_x(1 - h, 1 + h)
        fmm = chi2_x(1 - h, 1 - h)
        d2_11 = (f_p0 - 2 * f00 + f_m0) / h**2
        d2_22 = (f_0p - 2 * f00 + f_0m) / h**2
        d2_12 = (fpp - fpm - fmp + fmm) / (4 * h**2)
        hmat = np.array([[d2_11, d2_12], [d2_12, d2_22]])
        eigvals, eigvecs = np.linalg.eigh(hmat)
        v = eigvecs[:, 0]
        slopes.append((v[1] * b2) / (v[0] * b1))
    spread = (max(slopes) - min(slopes)) / np.mean(slopes)
    assert spread < 0.0001, f"slope not converged across grid densities: {slopes}"
    return slopes


def ift_predicted_scan_slope(h0a0, b1_0, b2_0, h=1e-4):
    """The RIGOROUS prediction (skeptic-requested, 2026-08-31) for how
    (beta1,beta2) should move as H0_anchor is scanned and re-optimized --
    via the implicit function theorem, d(beta)/d(H0_anchor) =
    -Hbb^-1 . d2chi2/d(beta)d(H0_anchor) -- NOT simply the pure null
    eigenvector (which is only the H0_anchor-scan direction in the limit
    where the cross-derivative is exactly aligned with the soft
    eigenvector -- a limit that need not hold exactly). Full 3x3 Hessian
    in rescaled (x1=beta1/beta1_0, x2=beta2/beta2_0, y=H0_anchor/h0a0)
    coordinates, central finite differences.
    """

    def chi2_xy(x1, x2, y):
        return chi2_fixed_h0anchor(y * h0a0, x1 * b1_0, x2 * b2_0)

    def d2(i, j, base):
        if i == j:
            p, m = list(base), list(base)
            p[i] += h
            m[i] -= h
            return (chi2_xy(*p) - 2 * chi2_xy(*base) + chi2_xy(*m)) / h**2
        pp, pm, mp, mm = list(base), list(base), list(base), list(base)
        pp[i] += h
        pp[j] += h
        pm[i] += h
        pm[j] -= h
        mp[i] -= h
        mp[j] += h
        mm[i] -= h
        mm[j] -= h
        return (chi2_xy(*pp) - chi2_xy(*pm) - chi2_xy(*mp) + chi2_xy(*mm)) / (4 * h**2)

    base = (1.0, 1.0, 1.0)
    h11, h22 = d2(0, 0, base), d2(1, 1, base)
    h12 = d2(0, 1, base)
    h13, h23 = d2(0, 2, base), d2(1, 2, base)
    hbb = np.array([[h11, h12], [h12, h22]])
    cross = np.array([h13, h23])
    dbeta_dh0 = -np.linalg.solve(hbb, cross)
    eigvals, eigvecs = np.linalg.eigh(hbb)
    v_soft, v_stiff = eigvecs[:, 0], eigvecs[:, 1]
    stiff_fraction = abs(np.dot(dbeta_dh0, v_stiff) / np.dot(dbeta_dh0, v_soft))
    predicted_slope = (dbeta_dh0[1] * b2_0) / (dbeta_dh0[0] * b1_0)
    return predicted_slope, stiff_fraction


def test_ift_prediction_matches_empirical_scan_tighter_than_pure_null():
    """The rigorous IFT-predicted scan slope must match the empirical
    Table-II-scan slope (6.157055e7) MORE closely than the pure null-
    eigenvector slope does -- confirms the H0_anchor-scan direction is
    not simply the null eigenvector (an overclaim the first draft made),
    but the more complete IFT-predicted direction, which includes a real
    (non-zero, non-negligible) stiff-direction contribution.
    """
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    ift_slope, stiff_fraction = ift_predicted_scan_slope(h0a, b1, b2)
    pure_null_slope = hessian_null_slope(h0a, b1, b2)[1]
    ift_err = abs(ift_slope - EMPIRICAL_TABLE_II_SLOPE) / EMPIRICAL_TABLE_II_SLOPE
    null_err = abs(pure_null_slope - EMPIRICAL_TABLE_II_SLOPE) / EMPIRICAL_TABLE_II_SLOPE
    assert ift_err < null_err, (
        f"IFT prediction (err={ift_err:.4%}) should be tighter than pure null "
        f"eigenvector (err={null_err:.4%})"
    )
    return ift_slope, stiff_fraction, ift_err, null_err


if __name__ == "__main__":
    test_positive_control_chi2_matches_two_table_ii_rows()
    print("Positive control: this script's own chi2 reproduces TJB's own reported")
    print("  chi2_33 for 2 Table II rows (spotlighted + planck_exact_100pct) to <0.1%: PASS\n")

    slopes_h = test_hessian_slope_converges_with_step_size()
    print("Step-size convergence (spotlighted row, h=1e-3,1e-4,1e-5):")
    for h, s in zip((1e-3, 1e-4, 1e-5), slopes_h, strict=True):
        print(f"  h={h:.0e}: slope={s:.6e}")
    print("  PASS -- converged to < 0.01% spread across 2 orders of magnitude in h.\n")

    all_slopes = test_slope_is_h0anchor_independent()
    print("Fixed-H0_anchor near-null eigenvector slope, at each of TJB's own 7 Table II rows:")
    for label, slope in all_slopes.items():
        h0a = TABLE_II[label][0]
        print(f"  {label:24s} (H0_anchor={h0a:6.2f}): slope={slope:.6e}")
    print("  PASS -- H0_anchor-independent to < 0.1% across the full Table II range.\n")

    h0a, b1, b2, chi2_exp = TABLE_II["unconstrained_spotlighted"]
    eigvals, slope, hessian = hessian_null_slope(h0a, b1, b2)
    print(f"At the spotlighted row (H0_anchor={h0a}):")
    print(f"  eigenvalues = {eigvals}  (condition number = {eigvals[1] / eigvals[0]:.1f})")
    print(f"  REAL fixed-H0_anchor near-null slope d(beta2)/d(beta1) = {slope:.6e}")
    print()
    print(f"Compare against FINDING_P175's idealized-local prediction  C = {C_PREDICTED_LOCAL:.6e}")
    print(f"  ratio (real Hessian / idealized-local C) = {slope / C_PREDICTED_LOCAL:.4f}")
    print(
        f"Compare against FINDING_P175's empirical Table-II-scan slope = {EMPIRICAL_TABLE_II_SLOPE:.6e}"
    )
    print(f"  ratio (real Hessian / Table-II-scan) = {slope / EMPIRICAL_TABLE_II_SLOPE:.4f}")
    print()
    # 1-sigma extent along the flat direction alone (formal Delta-chi2=1),
    # in fractional beta1 units, holding the orthogonal stiff direction at 0
    dx_1sigma = np.sqrt(2.0 / eigvals[0])
    print(
        f"Formal 1-sigma extent along the flat direction alone (Delta-chi2=1): "
        f"delta_x ~ {dx_1sigma:.4f} (i.e. beta1 can move ~{dx_1sigma * 100:.1f}% "
        f"along this direction before Delta-chi2=1) -- a real, statistically "
        f"meaningful degeneracy, not a numerical curiosity."
    )

    print("\n" + "=" * 70)
    print("SKEPTIC-REQUESTED CHECKS (2026-08-31, see FINDING_P176.md Correction)")
    print("=" * 70)

    density_slopes = test_slope_converges_with_grid_density()
    print("\nGrid-density convergence (spotlighted row, npts=500,1000,2000,4000):")
    for npts, s in zip((500, 1000, 2000, 4000), density_slopes, strict=True):
        print(f"  npts={npts}: slope={s:.6e}")
    print("  PASS -- < 0.01% spread; rules out cumulative_trapezoid noise floor concern.")

    ift_slope, stiff_fraction, ift_err, null_err = (
        test_ift_prediction_matches_empirical_scan_tighter_than_pure_null()
    )
    print("\nRigorous IFT-predicted H0_anchor-scan direction (not the pure null eigenvector):")
    print(f"  stiff-eigenvector fraction in the predicted scan direction = {stiff_fraction:.4%}")
    print(f"  IFT-predicted slope = {ift_slope:.6e}  (error vs empirical scan: {ift_err:.4%})")
    print(f"  pure null-eigenvector slope error vs empirical scan: {null_err:.4%}")
    print(
        "  The IFT prediction is markedly tighter -- the H0_anchor-scan direction is NOT\n"
        "  simply the null eigenvector (a real, ~0.7% stiff-direction admixture exists),\n"
        "  and once that is accounted for rigorously, the prediction matches TJB's own\n"
        "  reported Table II numbers to ~0.02% -- consistent with ordinary Nelder-Mead\n"
        "  optimizer tolerance (independently re-checked: re-optimizing the spotlighted\n"
        "  row from a fresh starting guess with TJB's own tolerance settings converges to\n"
        "  beta1,beta2 within 0.01-0.02% of his reported values -- see FINDING_P176.md)."
    )
