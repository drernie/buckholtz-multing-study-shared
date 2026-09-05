"""P191 -- Fisher-information forecast: would synthetic high-z H(z) points
measurably shrink/rotate v82's own (beta1,beta2) degeneracy ellipse?

Continues FINDING_P190's own named next step (its item 5 of "What this
file does NOT establish"): a real Fisher-information/forecast calculation
was not attempted there. This file attempts it, reusing P176's own
verbatim, already-positive-controlled chi2_fixed_h0anchor/Hessian
machinery and P190's own E1(z),E2(z) propagation for the cheap diagnostic
pre-check.

Method:
1. Cheap diagnostic (no Fisher matrix needed yet): extend P190's own
   -E1(z)/E2(z) level-set-slope computation past the real dataset's
   z=2.33 maximum, to z=3,5,7,10,20 -- does the already-observed
   monotonic rise continue, or does it saturate?
2. Main test: build an AUGMENTED chi-squared function that adds synthetic
   H(z) "points" at z>2.33, each fixed EXACTLY at the fiducial (TJB's own
   real Table II best-fit) model's own prediction, with an assumed
   relative uncertainty sigma_synth -- the standard Fisher-forecast
   convention (a forecast asks "how much information WOULD a point at
   this precision add", not "what would a noisy measurement show").
   Compute the same rescaled-coordinate 2x2 Hessian eigen-decomposition
   P176 already uses, for baseline (real 33 points only) vs augmented,
   across a grid of synthetic z choices and sigma_synth values -- plus
   floor (sigma->infinity, must reduce to baseline) and ceiling
   (sigma->0, the best case at these z's) per FL Step 4a.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own archive/code/multing_core.py, same constants and
# functions P176/P190's own scripts already positive-controlled. Copied
# rather than imported -- this project's own established convention for the
# P176/P189/P190 lineage (deliberately uncentralized, see docs/154-adjacent
# boyko-project-radar finding, 2026-09-03).
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


# TJB's own 31-point cosmic chronometer compilation, verbatim (P176's copy).
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
    """TJB's own chi2 function (generate_all_results.py fit_row's fixed
    branch), reproduced verbatim -- identical to P176's own copy."""
    Hm = H_of_z_kms(ZFINE, h0_anchor, beta1, beta2, Z_SHOES)
    if np.any(np.isnan(Hm)):
        return 1e12
    Hp = np.interp(z33, ZFINE, Hm)
    return np.sum(((Hp - H33) / s33) ** 2)


# TJB's own real fit point (spotlighted row, Table II, verbatim from P176).
H0A_FIT = 73.22
B1_FIT = 1.4335e10
B2_FIT = 7.8067e17
CHI2_33_EXPECTED = 15.75  # TJB's own reported chi2_33 at this row (P176 positive control)
EMPIRICAL_SLOPE_P176 = 6.073104e07  # P176's own found near-null slope at this row


def test_positive_control_baseline_chi2_matches_p176():
    """Positive control: reused verbatim chi2_fixed_h0anchor must reproduce
    TJB's own reported chi2_33=15.75 at the spotlighted row -- same check
    P176 already ran, repeated here since this script copies the function
    fresh rather than importing it (project convention for this lineage)."""
    computed = chi2_fixed_h0anchor(H0A_FIT, B1_FIT, B2_FIT)
    rel_err = abs(computed - CHI2_33_EXPECTED) / CHI2_33_EXPECTED
    assert rel_err < 0.001, f"computed chi2={computed:.4f}, TJB reports {CHI2_33_EXPECTED}"
    return True


# ---------------------------------------------------------------------------
# P190's own E1(z), E2(z) machinery (verbatim), for the cheap diagnostic
# pre-check of whether extending past z=2.33 is even a promising direction.
# ---------------------------------------------------------------------------
def dF1_db1(z):
    M, R, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
    return (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2


def dF2_db2(z):
    R, k, d = R_of(z), k_of(z), d_of(z)
    return (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2


def d_addot_db1(z):
    return -dF1_db1(z) / (M_of(z) / 2.0) / d_of(z)


def d_addot_db2(z):
    return dF2_db2(z) / (M_of(z) / 2.0) / d_of(z)


def E1_E2_at_z(z_target, zref=Z_SHOES, npts=2000):
    """Verbatim from P190 (already positive-controlled there to <0.1% against
    a direct finite-difference on H2_of_z)."""
    z_desi = 2.33
    zg = np.sort(
        np.unique(np.concatenate([np.linspace(0, max(z_target, z_desi), npts), [z_target, zref]]))
    )
    d1 = np.array([d_addot_db1(zx) / (1.0 + zx) for zx in zg])
    d2 = np.array([d_addot_db2(zx) / (1.0 + zx) for zx in zg])
    E1_raw = np.concatenate(([0.0], cumulative_trapezoid(d1, zg)))
    E2_raw = np.concatenate(([0.0], cumulative_trapezoid(d2, zg)))
    i0 = np.argmin(np.abs(zg - zref))
    itgt = np.argmin(np.abs(zg - z_target))
    E1 = 2.0 * (E1_raw[itgt] - E1_raw[i0])
    E2 = 2.0 * (E2_raw[itgt] - E2_raw[i0])
    return E1, E2


# ---------------------------------------------------------------------------
# NEW for P191: augmented chi2 with synthetic high-z points, and a
# generalized Hessian/eigen routine that works on any chi2 function.
# ---------------------------------------------------------------------------
def _dense_zgrid_through(synth_zs, npts=2000):
    """A dense integration grid from z=0 through the largest of DESI's
    z=2.33 and the synthetic z's, INCLUDING Z_SHOES (the zref) and every
    synth_z explicitly -- so H2_of_z's cumulative_trapezoid integration
    (which needs a real integration path, not a sparse jump straight from
    one synthetic z to the next) and its argmin(|zgrid-zref|) reference
    lookup both land on real, densely-sampled points."""
    zmax = max(Z_DESI, float(np.max(synth_zs)))
    return np.sort(np.unique(np.concatenate([np.linspace(0, zmax, npts), synth_zs, [Z_SHOES]])))


def augmented_chi2(h0_anchor, b1, b2, synth_zs, synth_sigma_rel):
    """Baseline chi2 (real 33 points) plus synthetic points at synth_zs,
    each fixed EXACTLY at the fiducial model's own prediction (standard
    Fisher-forecast convention: measures information content, not a noisy
    hypothetical measurement). synth_sigma_rel: relative uncertainty
    (e.g. 0.03 for 3%) applied to the fiducial H(z) at each synthetic z to
    get an absolute sigma -- realistic surveys report relative precision,
    not one fixed km/s/Mpc number across widely different z.

    BUG FOUND AND FIXED (2026-09-05, Step 8a skeptic pass, CONFIRMED-REAL
    via independent re-derivation before accepting): the original version
    called H_of_z_kms(synth_zs, ...) directly on the bare 4-element
    synth_zs array. H2_of_z's own cumulative-trapezoid integration needs a
    real path from zref to the target z; with only the 4 sparse synth_zs
    as the "grid" and zref=Z_SHOES=0.0233 nowhere in it,
    argmin(|zgrid-zref|) silently picked the CLOSEST sparse point (z=3) as
    the reference, making H(z=3) identically equal to h0_anchor for EVERY
    (b1,b2) -- that synthetic point contributed exactly zero Fisher
    information, and H at z=5,7,10 came from a 4-point trapezoidal
    integration between the sparse synth_zs themselves, not the real
    cosmic history. Traced and confirmed by hand: with zgs=[3,5,7,10],
    argmin(|zgs-0.0233|)=0 (z=3 is nearest to 0.0233 among those 4
    values), so ds[0]=ds_raw[0]-ds_raw[0]=0 identically. Fixed by
    following chi2_fixed_h0anchor's own already-correct, positive-
    controlled pattern exactly: build a dense grid, evaluate H2_of_z on
    it once, interpolate onto the target z's -- never call H_of_z_kms
    directly on a sparse target array.
    """
    base = chi2_fixed_h0anchor(h0_anchor, b1, b2)
    if not synth_zs:
        return base
    synth_zs = np.asarray(synth_zs, dtype=float)
    zdense = _dense_zgrid_through(synth_zs)
    H_fid_dense = H_of_z_kms(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    H_model_dense = H_of_z_kms(zdense, h0_anchor, b1, b2, Z_SHOES)
    if np.any(np.isnan(H_model_dense)):
        return 1e12
    H_fid = np.interp(synth_zs, zdense, H_fid_dense)
    H_model = np.interp(synth_zs, zdense, H_model_dense)
    sigma_abs = synth_sigma_rel * H_fid
    synth_term = np.sum(((H_model - H_fid) / sigma_abs) ** 2)
    return base + synth_term


def test_positive_control_synthetic_fiducial_values_are_physical():
    """New positive control added after the Step 8a skeptic pass caught
    the sparse-grid bug above: the fiducial H(z) values used to anchor
    the synthetic points must be (a) strictly increasing with z (basic
    Hubble-expansion sanity, not an artifact of the reference-index bug),
    (b) each notably different from H0_anchor itself (ruling out the
    exact degenerate failure mode the bug produced, where H(z=3) was
    silently pinned to H0_anchor regardless of b1,b2), and (c) in a
    physically sane order of magnitude for these redshifts."""
    synth_zs = np.array([3.0, 5.0, 7.0, 10.0])
    zdense = _dense_zgrid_through(synth_zs)
    H_fid_dense = H_of_z_kms(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    H_fid = np.interp(synth_zs, zdense, H_fid_dense)
    assert np.all(np.diff(H_fid) > 0), f"H_fid not monotonically increasing: {H_fid}"
    assert np.all(np.abs(H_fid - H0A_FIT) > 50.0), (
        f"H_fid suspiciously close to H0_anchor={H0A_FIT} (the exact bug this guards against): {H_fid}"
    )
    assert np.all((H_fid > 100.0) & (H_fid < 5000.0)), f"H_fid out of sane range: {H_fid}"
    return H_fid


def hessian_eig(chi2_func, h0_anchor, beta1_fit, beta2_fit, h=1e-4):
    """Numeric 2x2 Hessian of chi2_func(h0_anchor, x1*beta1_fit, x2*beta2_fit)
    at (x1,x2)=(1,1), rescaled coordinates -- same method P176 uses, but
    generalized to accept any chi2 function (baseline or augmented).
    Returns (eigvals ascending, eigvecs, near-null slope d(beta2)/d(beta1)).
    """

    def chi2_x(x1, x2):
        return chi2_func(h0_anchor, x1 * beta1_fit, x2 * beta2_fit)

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
    slope = (v_small[1] * beta2_fit) / (v_small[0] * beta1_fit)
    return eigvals, eigvecs, slope


def semi_axis(eigval):
    """Delta chi^2=1 semi-axis length along an eigenvector, in rescaled
    (fractional-shift) units: (1/2)*eigval*t^2 = 1 => t = sqrt(2/eigval).
    Sanity: at P176's spotlighted row, eigval_small=70.60 gives
    sqrt(2/70.60)=16.8%, matching P176's own reported "~17% fractional
    shift in beta1" -- confirms the factor-of-2 convention is right."""
    return np.sqrt(2.0 / eigval)


def test_positive_control_baseline_hessian_matches_p176():
    """The generalized hessian_eig, applied to plain chi2_fixed_h0anchor
    (synth_zs=[] case via the baseline lambda), must reproduce P176's own
    already-established numbers at the spotlighted row."""
    eigvals, _, slope = hessian_eig(chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT)
    cond = eigvals[1] / eigvals[0]
    rel_err_slope = abs(slope - EMPIRICAL_SLOPE_P176) / abs(EMPIRICAL_SLOPE_P176)
    assert rel_err_slope < 1e-4, f"slope={slope:.6e} vs P176's {EMPIRICAL_SLOPE_P176:.6e}"
    assert 8000 < cond < 8700, f"condition number {cond:.1f} outside P176's expected ~8333 range"
    return eigvals, slope, cond


def test_floor_reduces_to_baseline():
    """FL Step 4a FLOOR / negative control: synthetic points with an
    astronomically large sigma_synth (zero weight) must leave the Hessian
    numerically identical to baseline -- confirms the augmentation term
    correctly vanishes before trusting any nonzero-weight result."""
    synth_zs = [3.0, 5.0, 7.0, 10.0]

    def chi2_floor(h0a, b1, b2):
        return augmented_chi2(h0a, b1, b2, synth_zs, synth_sigma_rel=1e6)

    eigvals_base, _, slope_base = hessian_eig(chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT)
    eigvals_floor, _, slope_floor = hessian_eig(chi2_floor, H0A_FIT, B1_FIT, B2_FIT)
    rel_err = np.max(np.abs(eigvals_floor - eigvals_base) / np.abs(eigvals_base))
    assert rel_err < 1e-6, f"floor Hessian deviates from baseline by {rel_err:.2e}"
    return True


def test_augmented_hessian_converges_with_step_size():
    """The augmented chi2 surface is MORE curved than baseline (extra
    curvature ~ 1/sigma_synth^2 from the synthetic points), so P176's own
    default h=1e-4 -- fine for baseline -- is NOT automatically fine here.
    Caught empirically: at sigma_synth=1%, the small eigenvalue drifts
    ~3% between h=1e-4 and the converged h=1e-6 value, and h=1e-2 breaks
    down entirely (spurious negative eigenvalues).

    STRENGTHENED after the Step 8a skeptic pass flagged the original
    2-point (h=1e-5 vs 1e-6) check as under-restrictive -- two adjacent
    points agreeing does not rule out both sliding down the same
    truncation-error curve. Now sweeps a 4-point grid
    (1e-4, 1e-5, 1e-6, 1e-7) per sigma AND covers sigma=1e-6 (the
    CEILING value used in Step 2) in addition to the 3 realistic sigmas
    -- the ceiling's chi2 surface is far stiffer (curvature ~1/sigma^2),
    so a step size converged at realistic sigma is not automatically
    converged there too; this was flagged but not checked in the
    original version."""
    synth_zs = [3.0, 5.0, 7.0, 10.0]
    hs = (1e-4, 1e-5, 1e-6, 1e-7)
    for sigma_rel in (1e-6, 0.01, 0.03, 0.10):

        def chi2_aug(h0a, b1, b2, sigma_rel=sigma_rel):
            return augmented_chi2(h0a, b1, b2, synth_zs, synth_sigma_rel=sigma_rel)

        small_eigs = []
        for h in hs:
            eig, _, _ = hessian_eig(chi2_aug, H0A_FIT, B1_FIT, B2_FIT, h=h)
            small_eigs.append(eig[0])
        # plateau check: the LAST THREE points (1e-5,1e-6,1e-7) must all
        # agree with each other to <1% -- not just the last two -- so a
        # slow monotonic drift across all of them is caught, not just a
        # drift between the specific pair chosen.
        tail = np.array(small_eigs[1:])
        spread = (tail.max() - tail.min()) / abs(tail.mean())
        assert spread < 0.01, (
            f"sigma={sigma_rel:.0e}: small eigenvalue not in a plateau across "
            f"h=1e-5/1e-6/1e-7: {tail} (spread {spread:.2%})"
        )
    return True


CONVERGED_H = 1e-6  # per test_augmented_hessian_converges_with_step_size above


def rotation_angle_deg(eigvecs_base, eigvecs_aug):
    """Angle between the two near-null eigenvectors, compared DIRECTLY in
    the rescaled (x1,x2) coordinates eigh() already returns them in --
    NOT by converting to a raw d(beta2)/d(beta1) slope first. beta2's
    scale (~1e17) dwarfs beta1's (~1e10), so any two lines that aren't
    exactly along the beta1-axis look artificially "nearly vertical" in
    raw units, making genuine few-percent slope differences register as
    a near-zero angle -- caught by comparing against the diagnostic slope
    values directly, which visibly differed by up to 4% while the
    naively-computed raw-slope angle reported 0.000 deg at 3 decimals."""
    v_base = eigvecs_base[:, 0]
    v_aug = eigvecs_aug[:, 0]
    cos_angle = np.clip(abs(np.dot(v_base, v_aug)), -1.0, 1.0)
    return np.degrees(np.arccos(cos_angle))


if __name__ == "__main__":
    test_positive_control_baseline_chi2_matches_p176()
    print("Positive control 1: baseline chi2 reproduces TJB's own chi2_33=15.75: PASS\n")

    eigvals_base, slope_base, cond_base = test_positive_control_baseline_hessian_matches_p176()
    print(
        f"Positive control 2: baseline Hessian reproduces P176's own slope "
        f"({EMPIRICAL_SLOPE_P176:.6e}) and condition number (~8333): PASS"
    )
    print(f"  baseline eigvals={eigvals_base}, condition number={cond_base:.1f}\n")

    test_floor_reduces_to_baseline()
    print("FLOOR check (sigma_synth -> 1e6x, negative control): augmented Hessian")
    print("  matches baseline to < 1e-6 relative error: PASS\n")

    H_fid_check = test_positive_control_synthetic_fiducial_values_are_physical()
    print("Positive control 3 (added after Step 8a skeptic pass): fiducial H(z) at the")
    print("  synthetic z's is monotonically increasing, each >50 km/s/Mpc away from")
    print(f"  H0_anchor, and in a sane range: {H_fid_check} km/s/Mpc: PASS\n")

    test_augmented_hessian_converges_with_step_size()
    print("Step-size convergence check (strengthened after skeptic pass -- 4-point plateau,")
    print("  incl. the ceiling sigma=1e-6, not just the 3 realistic sigmas): PASS")
    print("  (P176's own default h=1e-4 is NOT converged for the augmented surface --")
    print(f"  all results below use h={CONVERGED_H:.0e}.)\n")

    # Recompute baseline at the converged step (P176 itself validated h=1e-4/1e-5
    # for the SMOOTHER baseline surface; re-deriving here at 1e-6 for an
    # apples-to-apples comparison against the augmented cases below).
    eigvals_base, eigvecs_base, slope_base = hessian_eig(
        chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT, h=CONVERGED_H
    )
    cond_base = eigvals_base[1] / eigvals_base[0]
    print(f"Baseline recomputed at h={CONVERGED_H:.0e}: condition number={cond_base:.1f} ", end="")
    print(f"(vs h=1e-4 value {8333.5:.1f} -- {abs(cond_base - 8333.5) / 8333.5:.2%} apart)\n")

    print("=" * 78)
    print("STEP 1 (cheap diagnostic): does -E1(z)/E2(z) keep rising past z=2.33,")
    print("        or does it saturate?")
    print("=" * 78)
    diag_zs = [0.07, 0.5, 1.0, 1.965, 2.33, 3.0, 5.0, 7.0, 10.0, 20.0, 50.0]
    diag_slopes = []
    for z in diag_zs:
        E1, E2 = E1_E2_at_z(z)
        s = -E1 / E2
        diag_slopes.append(s)
        print(f"  z={z:7.2f}:  -E1/E2 = {s: .6e}")
    diag_slopes = np.array(diag_slopes)
    print(
        f"\n  Full range z=0.07..50: [{diag_slopes.min():.4e}, {diag_slopes.max():.4e}], "
        f"spread {(diag_slopes.max() - diag_slopes.min()) / np.mean(np.abs(diag_slopes)):.4%}"
    )
    tail_spread = (diag_slopes[-1] - diag_slopes[4]) / abs(diag_slopes[4])  # z=2.33 -> z=50
    print(f"  Change from z=2.33 to z=50 alone: {tail_spread:.4%}")

    print()
    print("=" * 78)
    print("STEP 2: FLOOR-CEILING interval for adding synthetic points at")
    print("        z in {3,5,7,10} (FL Step 4a, resolved before the realistic-sigma run)")
    print("=" * 78)
    synth_zs = [3.0, 5.0, 7.0, 10.0]

    def chi2_ceiling(h0a, b1, b2):
        return augmented_chi2(h0a, b1, b2, synth_zs, synth_sigma_rel=1e-6)

    eigvals_ceil, _, slope_ceil = hessian_eig(chi2_ceiling, H0A_FIT, B1_FIT, B2_FIT, h=CONVERGED_H)
    cond_ceil = eigvals_ceil[1] / eigvals_ceil[0]
    semi_base = semi_axis(eigvals_base[0])
    semi_ceil = semi_axis(eigvals_ceil[0])
    shrink_ceil = 1.0 - semi_ceil / semi_base
    print(f"  FLOOR:   condition number = {cond_base:.1f} (== baseline, by construction)")
    print(
        f"  CEILING: condition number = {cond_ceil:.1f}  "
        f"(sigma_synth->0 at z={synth_zs}, best case at these z's)"
    )
    print(f"  CEILING semi-axis shrinkage vs baseline: {shrink_ceil:.2%}")
    if shrink_ceil < 0.10:
        print("  => TASK_INFEASIBLE at these z's: even PERFECT precision barely moves the")
        print("     ellipse -- this is a finding about the world, not evidence against the claim.")
    else:
        print("  => Real headroom exists at these z's; proceeding to realistic-sigma sweep.")

    print()
    print("=" * 78)
    print("STEP 3: realistic-sigma sweep, sigma_synth in {1%, 3%, 10%} relative,")
    print("        z in {3,5,7,10} added together as one hypothetical future survey")
    print("=" * 78)
    for sigma_rel in (0.01, 0.03, 0.10):

        def chi2_aug(h0a, b1, b2, sigma_rel=sigma_rel):
            return augmented_chi2(h0a, b1, b2, synth_zs, synth_sigma_rel=sigma_rel)

        eigvals_aug, eigvecs_aug, slope_aug = hessian_eig(
            chi2_aug, H0A_FIT, B1_FIT, B2_FIT, h=CONVERGED_H
        )
        cond_aug = eigvals_aug[1] / eigvals_aug[0]
        semi_aug = semi_axis(eigvals_aug[0])
        shrink = 1.0 - semi_aug / semi_base
        eff = shrink / shrink_ceil if shrink_ceil > 0 else float("nan")

        angle_deg = rotation_angle_deg(eigvecs_base, eigvecs_aug)

        print(f"  sigma_synth = {sigma_rel:.0%}:")
        print(f"    condition number: {cond_base:.1f} -> {cond_aug:.1f}")
        print(
            f"    Delta-chi^2=1 semi-axis: {semi_base:.4f} -> {semi_aug:.4f}  (shrink {shrink:.2%})"
        )
        print(f"    near-null eigenvector rotation: {angle_deg:.3f} deg")
        print(f"    efficiency = shrink/ceiling_shrink = {eff:.2%}")
        mcid_met = shrink >= 0.10 or angle_deg >= 5.0
        print(f"    MCID (>=10% shrink OR >=5 deg rotation) met: {mcid_met}")
        print()
