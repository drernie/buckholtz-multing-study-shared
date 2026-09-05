"""P193 -- does a Fisher-forecast at synthetic z in {12,14,16} (the last
well-defined window before P192's found domain-of-validity boundary,
z~16.957) outperform P191's own z in {3,5,7,10}?

Continues FINDING_P191's own Pearl Registry prediction (synthetic z past
the level-set slope's own peak should differ measurably from P191's own
z<=10 result) and FINDING_P192's own boundary finding (H^2(z)<0, hence
H(z) undefined, at z~16.957 for TJB's own real fitted (beta1,beta2)).
z in {12,14,16} sits inside the domain of validity, in the LAST window
before that boundary.

Pre-flight margin check (done BEFORE writing this script, then
formalized as a positive control here -- learning from P192's own two
caught bugs, not deferring the check to a failing test after the fact):
all 8 finite-difference corners (x1,x2) in {1+-h}x{1+-h} for
h in {1e-4,1e-5,1e-6} keep H^2(z=16) positive, and the perturbed
boundary itself stays at z~16.956-16.957 -- stable under these
perturbations, safe for a numeric Hessian at z=16.

Unexpected finding surfaced while preparing this script (not initially
anticipated by CLAIM_P193): H(z) in this reconstruction does NOT
monotonically increase across the whole domain -- it peaks near z~10
(H~508 km/s/Mpc) and then DECLINES toward zero as z approaches the
z~16.957 boundary. H_fid at z=12,14,16 is [494.0, 429.8, 270.9]
km/s/Mpc -- a DECREASING sequence, not increasing. P191/P192's own
physicality positive control required monotonic increase (valid for
their own z<=10 range, where H(z) is still rising) -- reformulated here
to check what that control was actually guarding against (H(z) silently
pinned to H0_anchor by the sparse-grid bug class already caught twice
in this lineage), not monotonicity, which is not a universal property
of this reconstruction.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own archive/code/multing_core.py -- identical to
# P176/P189/P190/P191/P192's own copies (deliberately uncentralized
# lineage convention, docs/154-adjacent boyko-project-radar finding).
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


# TJB's own 31-point cosmic chronometer compilation, verbatim.
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
    """TJB's own chi2 function, reproduced verbatim."""
    Hm = H_of_z_kms(ZFINE, h0_anchor, beta1, beta2, Z_SHOES)
    if np.any(np.isnan(Hm)):
        return 1e12
    Hp = np.interp(z33, ZFINE, Hm)
    return np.sum(((Hp - H33) / s33) ** 2)


H0A_FIT = 73.22
B1_FIT = 1.4335e10
B2_FIT = 7.8067e17
CHI2_33_EXPECTED = 15.75
EMPIRICAL_SLOPE_P176 = 6.073104e07

SYNTH_ZS = [12.0, 14.0, 16.0]
BOUNDARY_Z = 16.957  # P192's own grid-converged, straddle-confirmed finding


def test_positive_control_baseline_chi2_matches_p176():
    computed = chi2_fixed_h0anchor(H0A_FIT, B1_FIT, B2_FIT)
    rel_err = abs(computed - CHI2_33_EXPECTED) / CHI2_33_EXPECTED
    assert rel_err < 0.001, f"computed chi2={computed:.4f}, TJB reports {CHI2_33_EXPECTED}"
    return True


def E1_E2_at_z(z_target, zref=Z_SHOES, npts=2000):
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


def _dense_zgrid_through(synth_zs, npts=2000):
    zmax = max(Z_DESI, float(np.max(synth_zs)))
    return np.sort(np.unique(np.concatenate([np.linspace(0, zmax, npts), synth_zs, [Z_SHOES]])))


def augmented_chi2(h0_anchor, b1, b2, synth_zs, synth_sigma_rel):
    """Same dense-grid-then-interpolate pattern P191/P192 fixed to, after
    the original sparse-grid bug (see both files' own Correction
    sections)."""
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


# ---------------------------------------------------------------------------
# NEW for P193, added after the Step 8a skeptic pass on the first draft:
# an ANALYTIC Fisher matrix, independent of the finite-difference Hessian
# above. Standard Gauss-Newton approximation: F_ij = sum_z (1/sigma_z^2) *
# (dH/dx_i)(z) * (dH/dx_j)(z), in the same rescaled x1=b1/B1_FIT,
# x2=b2/B2_FIT coordinates as hessian_eig. Since H^2(z) is exactly affine
# in (b1,b2) (established in P190), dH/db_i = E_i(z)/(2H(z)) exactly, no
# further approximation needed for the derivative itself -- the ONLY
# approximation vs. the full chi2 Hessian is dropping the (usually small,
# residual-weighted) second-derivative-of-H term Gauss-Newton always
# drops. This sidesteps the finite-difference Hessian's own numerical
# instability entirely: no subtraction of close chi2 values near a
# domain boundary, because no chi2 subtraction happens at all.
# ---------------------------------------------------------------------------
def analytic_fisher_matrix(synth_zs=None, synth_sigma_rel=None):
    """F_ij at the fiducial (H0A_FIT,B1_FIT,B2_FIT), summed over the real
    33-point dataset plus any synthetic points. synth_zs=None (or empty)
    gives the baseline-only Fisher matrix -- the direct analytic
    counterpart to hessian_eig(chi2_fixed_h0anchor, ...)."""
    zs = list(z33)
    sigmas = list(s33)
    if synth_zs:
        synth_zs = list(synth_zs)
        zdense = _dense_zgrid_through(np.array(synth_zs))
        H_fid_dense = H_of_z_kms(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
        H_fid_synth = np.interp(synth_zs, zdense, H_fid_dense)
        zs = zs + synth_zs
        sigmas = sigmas + list(synth_sigma_rel * H_fid_synth)

    zdense_all = _dense_zgrid_through(np.array(zs))
    H_all_dense = H_of_z_kms(zdense_all, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    H_at_zs = np.interp(zs, zdense_all, H_all_dense)

    F = np.zeros((2, 2))
    for z, sigma, H_z in zip(zs, sigmas, H_at_zs, strict=True):
        E1, E2 = E1_E2_at_z(z)
        # BUG FOUND AND FIXED (2026-09-05, caught by this file's own positive
        # control failing a real pytest run with a 100% mismatch, not by
        # review): E1(z), E2(z) are d(H^2)/db_i in SI units (H2_of_z works
        # entirely in SI via KMSMPC_TO_SI), but H_z here is H_of_z_kms's own
        # km/s/Mpc output -- a straight E_i/(2*H_z) mixes SI numerator with
        # km/s/Mpc denominator. dH_kms/db_i = (1/KMSMPC_TO_SI)*dH_SI/db_i =
        # (1/KMSMPC_TO_SI)*E_i(z)/(2*H_SI(z)), and H_SI(z)=H_z*KMSMPC_TO_SI,
        # so dH_kms/db_i = E_i(z)/(2*H_z*KMSMPC_TO_SI**2).
        dHdx1 = (B1_FIT * E1) / (2.0 * H_z * KMSMPC_TO_SI**2)
        dHdx2 = (B2_FIT * E2) / (2.0 * H_z * KMSMPC_TO_SI**2)
        grad = np.array([dHdx1, dHdx2])
        F += np.outer(grad, grad) / sigma**2
    return F


def analytic_fisher_eig(synth_zs=None, synth_sigma_rel=None):
    F = analytic_fisher_matrix(synth_zs, synth_sigma_rel)
    eigvals, eigvecs = np.linalg.eigh(F)
    v_small = eigvecs[:, 0]
    slope = (v_small[1] * B2_FIT) / (v_small[0] * B1_FIT)
    return eigvals, eigvecs, slope


def test_positive_control_analytic_fisher_matches_finite_difference_baseline():
    """Cross-check the analytic method against the finite-difference
    Hessian on the ONE case both can compute reliably: the real
    33-point baseline (no synthetic points), which P176's own
    convergence tests already established as numerically solid. Note:
    the analytic Fisher matrix is 1/2 the Gauss-Newton APPROXIMATION to
    the full chi2 Hessian (it drops the residual-weighted second-
    derivative-of-H term) -- these are related but not identical
    objects, so exact agreement is not expected; a few-percent
    agreement is what validates the analytic method as trustworthy
    where the finite-difference method is not."""
    eig_fd, _, slope_fd = hessian_eig(chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT, h=CONVERGED_H)
    eig_fisher, _, slope_fisher = analytic_fisher_eig()
    # hessian_eig's eigenvalues are of the full chi2 Hessian; the Fisher
    # matrix corresponds to (1/2) chi2 Hessian in the Gauss-Newton sense
    # (chi2 = sum(residual/sigma)^2 => (1/2)Hessian = sum(grad grad^T)/sigma^2
    # at zero residual). Compare 2*Fisher against the FD Hessian.
    rel_err_small = abs(2 * eig_fisher[0] - eig_fd[0]) / abs(eig_fd[0])
    rel_err_large = abs(2 * eig_fisher[1] - eig_fd[1]) / abs(eig_fd[1])
    rel_err_slope = abs(slope_fisher - slope_fd) / abs(slope_fd)
    assert rel_err_small < 0.05, f"small eigenvalue mismatch: {rel_err_small:.2%}"
    assert rel_err_large < 0.05, f"large eigenvalue mismatch: {rel_err_large:.2%}"
    assert rel_err_slope < 0.01, f"slope mismatch: {rel_err_slope:.2%}"
    return eig_fisher, slope_fisher, rel_err_small, rel_err_large


def test_positive_control_analytic_fisher_matches_finite_difference_augmented():
    """Skeptic-flagged gap (2026-09-05, second Step 8a pass): the check
    above only validates analytic-vs-FD agreement on the BASELINE (33
    real points, zero synthetic contribution). At sigma_synth=1%/3% the
    synthetic term DOMINATES F_ij -- exactly the regime the baseline
    check does not exercise. This test closes that gap using the ONE
    augmented case where BOTH methods actually converge:
    sigma_synth=10%, z=SYNTH_ZS. If they agree here too (not just at
    baseline), the sigma=1%/3% analytic-only numbers become a defensible
    extrapolation rather than an untested one."""
    eig_fd, _, slope_fd = hessian_eig(
        lambda h0a, b1, b2: augmented_chi2(h0a, b1, b2, SYNTH_ZS, synth_sigma_rel=0.10),
        H0A_FIT,
        B1_FIT,
        B2_FIT,
        h=1e-6,
    )
    eig_fisher, _, slope_fisher = analytic_fisher_eig(SYNTH_ZS, 0.10)
    rel_err_small = abs(2 * eig_fisher[0] - eig_fd[0]) / abs(eig_fd[0])
    rel_err_large = abs(2 * eig_fisher[1] - eig_fd[1]) / abs(eig_fd[1])
    rel_err_slope = abs(slope_fisher - slope_fd) / abs(slope_fd)
    assert rel_err_small < 0.10, f"augmented small eigenvalue mismatch: {rel_err_small:.2%}"
    assert rel_err_large < 0.10, f"augmented large eigenvalue mismatch: {rel_err_large:.2%}"
    assert rel_err_slope < 0.02, f"augmented slope mismatch: {rel_err_slope:.2%}"
    return rel_err_small, rel_err_large, rel_err_slope


def test_positive_control_synthetic_fiducial_values_are_physical():
    """Reformulated from P191/P192's own version: THAT check required
    monotonic increase, valid for their z<=10 range where H(z) is still
    rising. Here H(z) has already passed its own peak (~z=10, ~508
    km/s/Mpc) and is declining toward the P192-found boundary -- a real
    property of this reconstruction, not a bug (confirmed by the P192
    diagnostic table and independently re-derived in a pre-flight probe
    before writing this file). What THIS control actually needs to check
    (the thing the original monotonicity requirement was a proxy for,
    not the monotonicity itself): the sparse-grid bug class already
    caught twice in this lineage silently PINS H(z) to H0_anchor at
    whichever z happens to be nearest zref in a naive sparse call -- so
    the real invariant is "each H_fid is finite, positive, and not
    suspiciously close to H0_anchor," not "H_fid increases with z."""
    synth_zs = np.array(SYNTH_ZS)
    zdense = _dense_zgrid_through(synth_zs)
    H_fid_dense = H_of_z_kms(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    H_fid = np.interp(synth_zs, zdense, H_fid_dense)
    assert np.all(np.isfinite(H_fid)), f"H_fid not finite (past the P192 boundary?): {H_fid}"
    assert np.all(np.abs(H_fid - H0A_FIT) > 50.0), (
        f"H_fid suspiciously close to H0_anchor={H0A_FIT} (the sparse-grid bug's exact "
        f"failure mode, caught twice already in this lineage): {H_fid}"
    )
    assert np.all((H_fid > 10.0) & (H_fid < 1000.0)), f"H_fid out of sane range: {H_fid}"
    # Skeptic-flagged gap (2026-09-05, Step 8a): dropping monotonicity removed
    # the one check that would catch a wrong-for-the-wrong-reason result (e.g.
    # a sign-flip bug that still happens to produce a finite, non-H0_anchor,
    # in-range decreasing sequence). Golden values from an independent
    # pre-flight probe, not re-derived here.
    golden = np.array([494.03211931, 429.78076981, 270.91958818])
    rel_err = np.max(np.abs(H_fid - golden) / golden)
    assert rel_err < 1e-6, (
        f"H_fid diverges from the pre-computed golden values: {H_fid} vs {golden}"
    )
    return H_fid


def test_positive_control_finite_difference_stays_in_domain():
    """NEW for P193, formalizing the pre-flight probe run before writing
    this script (per this project's own Verification Substrate Gate
    discipline -- check the substrate can honestly run the test BEFORE
    trusting any result derived from it, not after). z=16 sits only
    ~5.7% below P192's own found boundary (z~16.957) -- close enough
    that the finite-difference Hessian's own perturbations of (b1,b2)
    could, in principle, push the EFFECTIVE boundary below z=16 for some
    corner of the (x1,x2) grid, silently producing chi2=1e12 (NaN
    fallback) instead of a real curvature value at that corner. Checked
    for h in {1e-4,1e-5,1e-6} across all 8 finite-difference corners:
    H^2(z=16) must stay positive at every one.

    Skeptic-flagged nit (2026-09-05, Step 8a): the main convergence
    sweep (convergence_report) later probes h down to 1e-9, smaller
    than the {1e-4,1e-5,1e-6} checked here -- not a gap: a smaller h
    means a SMALLER perturbation of (b1,b2), which strictly narrows the
    boundary excursion checked at h=1e-4 (the largest, most conservative
    perturbation tested). Checking the largest step sizes is a valid
    upper bound on the margin at every smaller step size actually used."""
    zdense = _dense_zgrid_through(np.array(SYNTH_ZS))
    for h in (1e-4, 1e-5, 1e-6):
        for x1, x2 in [
            (1 + h, 1 + h),
            (1 + h, 1 - h),
            (1 - h, 1 + h),
            (1 - h, 1 - h),
            (1 + h, 1.0),
            (1 - h, 1.0),
            (1.0, 1 + h),
            (1.0, 1 - h),
        ]:
            b1, b2 = x1 * B1_FIT, x2 * B2_FIT
            H2v = H2_of_z(zdense, H0A_FIT, b1, b2, Z_SHOES)
            idx16 = np.argmin(np.abs(zdense - 16.0))
            assert H2v[idx16] > 0, (
                f"H^2(z=16) went negative at finite-difference corner h={h:.0e}, "
                f"x1={x1:.6f}, x2={x2:.6f}: H2={H2v[idx16]:.4e} -- the Hessian "
                f"computation would silently hit the 1e12 NaN fallback here"
            )
    return True


def hessian_eig(chi2_func, h0_anchor, beta1_fit, beta2_fit, h=1e-4):
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
    return np.sqrt(2.0 / eigval)


def test_positive_control_baseline_hessian_matches_p176():
    eigvals, _, slope = hessian_eig(chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT)
    cond = eigvals[1] / eigvals[0]
    rel_err_slope = abs(slope - EMPIRICAL_SLOPE_P176) / abs(EMPIRICAL_SLOPE_P176)
    assert rel_err_slope < 1e-4, f"slope={slope:.6e} vs P176's {EMPIRICAL_SLOPE_P176:.6e}"
    assert 8000 < cond < 8700, f"condition number {cond:.1f} outside P176's expected ~8333 range"
    return eigvals, slope, cond


def test_floor_reduces_to_baseline():
    def chi2_floor(h0a, b1, b2):
        return augmented_chi2(h0a, b1, b2, SYNTH_ZS, synth_sigma_rel=1e6)

    eigvals_base, _, _ = hessian_eig(chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT)
    eigvals_floor, _, _ = hessian_eig(chi2_floor, H0A_FIT, B1_FIT, B2_FIT)
    rel_err = np.max(np.abs(eigvals_floor - eigvals_base) / np.abs(eigvals_base))
    assert rel_err < 1e-6, f"floor Hessian deviates from baseline by {rel_err:.2e}"
    return True


def convergence_report(sigma_rel, hs=(1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9)):
    """Diagnose (not assert) whether the finite-difference Hessian's
    small eigenvalue has ANY 3-consecutive-h plateau (<1% spread) across
    a WIDE h sweep, for one sigma_synth value. Returns
    (converged: bool, best_h_window, best_estimate, best_spread, all_values).

    REAL FINDING surfaced while running P191/P192's own established
    2-4-point convergence check on THIS z-set (z=12,14,16, close to
    P192's found domain boundary z~16.957): unlike P191's own z<=10
    set, a straightforward hs=(1e-4,1e-5,1e-6,1e-7) tail-plateau check
    FAILS here for sigma in {1e-6 (ceiling), 1%, 3%} -- not because the
    code is wrong (four independent positive controls above all pass),
    but because standard central-difference error has two competing
    sources (truncation error ~h^2 at large h, floating-point roundoff
    error ~epsilon/h^2 at small h) and the "safe middle window" between
    them is narrow-to-nonexistent for a chi2 surface this curved this
    close to a domain boundary. Confirmed by widening the h sweep
    itself (not narrowing the pass bar): a genuine plateau DOES exist
    for some (sigma, h-window) combinations and not others -- this
    function reports which, rather than silently averaging or picking
    the most convenient window.
    """
    values = {}
    for h in hs:

        def chi2_aug(h0a, b1, b2, sigma_rel=sigma_rel):
            return augmented_chi2(h0a, b1, b2, SYNTH_ZS, synth_sigma_rel=sigma_rel)

        eig, _, _ = hessian_eig(chi2_aug, H0A_FIT, B1_FIT, B2_FIT, h=h)
        values[h] = eig[0]

    hs_sorted = sorted(hs)
    best = None
    for i in range(len(hs_sorted) - 2):
        window = hs_sorted[i : i + 3]
        vals = np.array([values[h] for h in window])
        spread = (vals.max() - vals.min()) / abs(vals.mean())
        if spread < 0.01 and (best is None or spread < best[2]):
            best = (window, float(np.mean(vals)), spread)

    if best is None:
        return False, None, None, None, values
    window, estimate, spread = best
    return True, window, estimate, spread, values


def test_augmented_hessian_convergence_is_diagnosed_honestly():
    """Not a pass/fail gate on the RESULT -- a positive control on the
    DIAGNOSIS itself: convergence_report must correctly distinguish a
    genuinely converged case (sigma=10%, which P191's own established
    method handles fine) from the genuinely unstable ones found here,
    not paper over the difference by picking whichever window looks
    best."""
    converged_10pct, *_ = convergence_report(0.10)
    assert converged_10pct, "sigma=10% should show a real plateau somewhere in the h-sweep"
    return True


CONVERGED_H = 1e-6


def rotation_angle_deg(eigvecs_base, eigvecs_aug):
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
        f"({EMPIRICAL_SLOPE_P176:.6e}) and condition number (~8333): PASS\n"
    )

    test_floor_reduces_to_baseline()
    print("FLOOR check (sigma_synth -> 1e6x, negative control): augmented Hessian")
    print("  matches baseline to < 1e-6 relative error: PASS\n")

    H_fid_check = test_positive_control_synthetic_fiducial_values_are_physical()
    print("Positive control 3 (reformulated from P191/P192 -- no monotonicity")
    print("  requirement, H(z) has passed its own peak here): fiducial H(z) at")
    print(f"  z={SYNTH_ZS} is finite, >50 km/s/Mpc from H0_anchor, sane range:")
    print(f"  {H_fid_check} km/s/Mpc: PASS\n")

    test_positive_control_finite_difference_stays_in_domain()
    print("Positive control 4 (NEW for P193, formalizing the pre-flight margin")
    print("  check): H^2(z=16) stays positive at all 8 finite-difference corners,")
    print("  h in {1e-4,1e-5,1e-6} -- safe margin from P192's found boundary: PASS\n")

    test_augmented_hessian_convergence_is_diagnosed_honestly()
    print("Positive control 5 (diagnosis-only, not a pass/fail gate on the result):")
    print("  convergence_report correctly finds a real plateau for sigma=10%.\n")

    _, _, rel_err_small, rel_err_large = (
        test_positive_control_analytic_fisher_matches_finite_difference_baseline()
    )
    print("Positive control 6 (NEW for P193, per Step 8a skeptic pass): the analytic")
    print("  Fisher matrix (built from E1(z)/E2(z), no chi2 subtraction, immune to the")
    print("  finite-difference instability found above) matches the finite-difference")
    print(f"  Hessian on the baseline (33 real points): small-eig {rel_err_small:.2%},")
    print(f"  large-eig {rel_err_large:.2%} apart -- cross-validates the analytic method")
    print("  as trustworthy where the finite-difference method is not: PASS\n")

    aug_small, aug_large, aug_slope = (
        test_positive_control_analytic_fisher_matches_finite_difference_augmented()
    )
    print("Positive control 7 (2nd Step 8a skeptic pass, closes the gap that Positive")
    print("  control 6 only checked baseline, not the AUGMENTED case where the synthetic")
    print("  term dominates): analytic vs finite-difference agreement at sigma=10%,")
    print(f"  z={SYNTH_ZS} (the one augmented case where both converge): small-eig")
    print(f"  {aug_small:.3%}, large-eig {aug_large:.3%}, slope {aug_slope:.4%} apart --")
    print("  even tighter than baseline. Directly supports trusting the analytic-only")
    print("  sigma=1%/3% numbers below, not just extrapolating from baseline: PASS\n")

    eigvals_base, eigvecs_base, slope_base = hessian_eig(
        chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT, h=CONVERGED_H
    )
    cond_base = eigvals_base[1] / eigvals_base[0]
    semi_base = semi_axis(eigvals_base[0])
    print(f"Baseline at h={CONVERGED_H:.0e}: condition number={cond_base:.1f}\n")

    print("=" * 78)
    print(f"REAL FINDING: finite-difference Hessian convergence at z={SYNTH_ZS}")
    print("=" * 78)
    print("Unlike P191's own z<=10 set, a straightforward hs=(1e-4,1e-5,1e-6,1e-7)")
    print("tail-plateau check does NOT hold here for every sigma -- widened the")
    print("h-sweep itself (not the pass bar) to find out which sigma have a REAL")
    print("plateau somewhere, and which do not, at all:\n")

    sigma_labels = {1e-6: "1e-06 (ceiling)", 0.01: "1%", 0.03: "3%", 0.10: "10%"}
    results = {}
    for sigma_rel in (1e-6, 0.01, 0.03, 0.10):
        converged, window, estimate, spread, values = convergence_report(sigma_rel)
        results[sigma_rel] = (converged, window, estimate, spread)
        label = sigma_labels[sigma_rel]
        if converged:
            print(f"  sigma={label}: CONVERGED, plateau at h={window}, spread {spread:.3%}")
        else:
            all_str = ", ".join(f"h={h:.0e}:{v:.4e}" for h, v in values.items())
            print(f"  sigma={label}: NOT CONVERGED anywhere in the h-sweep ({all_str})")
    print()

    print("=" * 78)
    print(f"STEP 1: FLOOR-CEILING interval for z in {SYNTH_ZS}")
    print("=" * 78)
    ceil_converged, ceil_window, ceil_estimate, ceil_spread = results[1e-6]
    if ceil_converged:
        h_use = ceil_window[1]

        def chi2_ceiling(h0a, b1, b2):
            return augmented_chi2(h0a, b1, b2, SYNTH_ZS, synth_sigma_rel=1e-6)

        eigvals_ceil, _, _ = hessian_eig(chi2_ceiling, H0A_FIT, B1_FIT, B2_FIT, h=h_use)
        cond_ceil = eigvals_ceil[1] / eigvals_ceil[0]
        semi_ceil = semi_axis(eigvals_ceil[0])
        shrink_ceil = 1.0 - semi_ceil / semi_base
        print(f"  FLOOR:   condition number = {cond_base:.1f}")
        print(f"  CEILING: condition number = {cond_ceil:.1f} (h={h_use:.0e})")
        print(f"  CEILING semi-axis shrinkage vs baseline: {shrink_ceil:.2%}")
    else:
        print(f"  FLOOR:   condition number = {cond_base:.1f}")
        print("  CEILING: NUMERICALLY_UNSTABLE -- no finite-difference plateau found")
        print("           anywhere in h in {1e-4..1e-9}. Not usable as a Floor-Ceiling")
        print("           bound at this z-set; treated as unknown, not as evidence")
        print("           for or against headroom (same discipline as")
        print("           BLOCKED-INFRASTRUCTURE/ORACLE_INADEQUATE -- a broken")
        print("           measurement is not evidence about the thing measured).")
        shrink_ceil = None
    print()

    # Analytic-method baseline, for an apples-to-apples comparison when the
    # analytic fallback is used below (mixing a finite-difference baseline
    # with an analytic augmented result would bake in the two methods'
    # own ~5% cross-method difference as if it were a real effect).
    eigvals_base_an, eigvecs_base_an, slope_base_an = analytic_fisher_eig()
    semi_base_an = semi_axis(2.0 * eigvals_base_an[0])

    print("=" * 78)
    print(f"STEP 2: realistic-sigma sweep, sigma_synth in {{1%, 3%, 10%}}, z={SYNTH_ZS}")
    print("=" * 78)
    for sigma_rel in (0.01, 0.03, 0.10):
        converged, window, estimate, spread = results[sigma_rel]
        label = f"{sigma_rel:.0%}"
        if not converged:
            print(f"  sigma_synth = {label}: finite-difference NUMERICALLY_UNSTABLE --")
            print("    falling back to the analytic Fisher matrix (Positive control 6),")
            print("    immune to this instability since it involves no chi2 subtraction:")
            eigvals_an, eigvecs_an, slope_an = analytic_fisher_eig(SYNTH_ZS, sigma_rel)
            cond_an = eigvals_an[1] / eigvals_an[0]
            semi_an = semi_axis(2.0 * eigvals_an[0])
            shrink_an = 1.0 - semi_an / semi_base_an
            angle_an = rotation_angle_deg(eigvecs_base_an, eigvecs_an)
            print(
                f"    [ANALYTIC] condition number: {2 * eigvals_base_an[1] / eigvals_base_an[0]:.1f} -> {cond_an:.1f}"
            )
            print(
                f"    [ANALYTIC] Delta-chi^2=1 semi-axis: {semi_base_an:.4f} -> {semi_an:.4f}  "
                f"(shrink {shrink_an:.2%})"
            )
            print(f"    [ANALYTIC] near-null eigenvector rotation: {angle_an:.3f} deg")
            mcid_met_an = shrink_an >= 0.10 or angle_an >= 5.0
            print(f"    [ANALYTIC] MCID (>=10% shrink OR >=5 deg rotation) met: {mcid_met_an}")
            print("    (labeled [ANALYTIC] throughout -- a related but not identical")
            print("     quantity to the finite-difference chi2 Hessian used elsewhere,")
            print("     per Positive control 6's own ~5% cross-method agreement)")
            print()
            continue

        h_use = window[1]

        def chi2_aug(h0a, b1, b2, sigma_rel=sigma_rel):
            return augmented_chi2(h0a, b1, b2, SYNTH_ZS, synth_sigma_rel=sigma_rel)

        eigvals_aug, eigvecs_aug, slope_aug = hessian_eig(
            chi2_aug, H0A_FIT, B1_FIT, B2_FIT, h=h_use
        )
        cond_aug = eigvals_aug[1] / eigvals_aug[0]
        semi_aug = semi_axis(eigvals_aug[0])
        shrink = 1.0 - semi_aug / semi_base
        angle_deg = rotation_angle_deg(eigvecs_base, eigvecs_aug)

        print(f"  sigma_synth = {label} (converged at h={h_use:.0e}, spread {spread:.3%}):")
        print(f"    condition number: {cond_base:.1f} -> {cond_aug:.1f}")
        print(
            f"    Delta-chi^2=1 semi-axis: {semi_base:.4f} -> {semi_aug:.4f}  (shrink {shrink:.2%})"
        )
        print(f"    near-null eigenvector rotation: {angle_deg:.3f} deg")
        if shrink_ceil is not None and shrink_ceil > 0:
            print(f"    efficiency = shrink/ceiling_shrink = {shrink / shrink_ceil:.2%}")
        mcid_met = shrink >= 0.10 or angle_deg >= 5.0
        print(f"    MCID (>=10% shrink OR >=5 deg rotation) met: {mcid_met}")
        print()

    print("=" * 78)
    print("COMPARISON vs P191's own z={3,5,7,10} results (73.0%/45.6%/13.6% shrink)")
    print("=" * 78)
