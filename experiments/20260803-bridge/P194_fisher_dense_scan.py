"""P194 -- a dense scan of the (10, 16.957) window: where inside the last
well-defined window (P192's found boundary) is (beta1,beta2)-discriminating
power actually concentrated, and does the best achievable point-set there
beat P193's own z in {12,14,16}?

Continues FINDING_P191 (estimand, MCID, machinery), FINDING_P192 (found
boundary z~16.957), FINDING_P193 (confirmed the pearl at 3 discrete points,
and built + cross-validated the analytic Fisher matrix this file reuses
verbatim -- no finite-difference perturbation of (beta1,beta2) needed, so
none of P193's own numerical-instability concerns apply here).

Method: for each single synthetic z on a 0.5-step grid from z=10.5 to
z=16.5 (a conservative margin below P192's own z~16.957 boundary), compute
the (beta1,beta2)-ellipse shrinkage that ONE synthetic point at that z,
combined with the real 33-point baseline, would produce -- an information
PROFILE over z, not a single number. Then: find the top-3 and top-4
individually-most-informative points, compute their ACTUAL combined Fisher
matrix (not a sum of shrinkage numbers -- Fisher matrices add exactly,
shrinkage percentages do not), and compare against P193's {12,14,16} and
P191's {3,5,7,10} at matched sigma.

Correction applied before writing this script (caught in CLAIM_P194 itself,
before any code): "top-N individually-best points are the best N-point
combination" does NOT follow from Fisher-information additivity -- additive
matrices, greedy scalar ranking is not equivalent to jointly optimal for
a matrix-valued criterion. This file computes and reports the greedy set's
real, honestly-computed shrinkage as one reasonable candidate, not as a
proven-optimal combination.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own archive/code/multing_core.py -- identical to
# P176/P189/P190/P191/P192/P193's own copies (deliberately uncentralized
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

BOUNDARY_Z = 16.957  # P192's own grid-converged, straddle-confirmed finding
SCAN_ZS = [10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5]
P193_ZS = [12.0, 14.0, 16.0]
P191_ZS = [3.0, 5.0, 7.0, 10.0]


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
    """Same dense-grid-then-interpolate pattern P191-P193 fixed to."""
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


def rotation_angle_deg(eigvecs_base, eigvecs_aug):
    v_base = eigvecs_base[:, 0]
    v_aug = eigvecs_aug[:, 0]
    cos_angle = np.clip(abs(np.dot(v_base, v_aug)), -1.0, 1.0)
    return np.degrees(np.arccos(cos_angle))


def gradient_direction_deg(z):
    """NEW for P194, added after the Step 8a skeptic pass flagged that the
    single-point shrink profile's monotonic rise could be a trivial scale
    artifact rather than evidence of a changing gradient DIRECTION: since
    dH/dbeta_i ~ 1/H(z) and sigma_abs = synth_sigma_rel*H(z), a single
    point's Fisher contribution scales as ~1/H(z)^4, which diverges near
    the P192 boundary (H->0) regardless of direction. This function
    isolates DIRECTION alone (normalized gradient vector angle vs the
    beta1-axis), stripping out the 1/H(z) magnitude entirely, so it can
    be compared against the magnitude-only profile."""
    E1, E2 = E1_E2_at_z(z)
    v = np.array([B1_FIT * E1, B2_FIT * E2])  # H(z) and KMSMPC_TO_SI cancel in the angle
    return np.degrees(np.arctan2(v[1], v[0]))


# ---------------------------------------------------------------------------
# Analytic Fisher matrix, verbatim from P193 (already positive-controlled
# there against finite-difference at both baseline and one augmented case).
# ---------------------------------------------------------------------------
def analytic_fisher_matrix(synth_zs=None, synth_sigma_rel=None):
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
        dHdx1 = (B1_FIT * E1) / (2.0 * H_z * KMSMPC_TO_SI**2)
        dHdx2 = (B2_FIT * E2) / (2.0 * H_z * KMSMPC_TO_SI**2)
        grad = np.array([dHdx1, dHdx2])
        F += np.outer(grad, grad) / sigma**2
    return F


def single_point_shrink_fixed_absolute_sigma(z, sigma_abs_kms, semi_base):
    """NEW for P194, per the Step 8a skeptic pass: isolates the DIRECTION
    effect from the magnitude (1/H(z)^4) effect by using a FIXED absolute
    sigma in km/s/Mpc (not scaled by H(z) at all) for a single synthetic
    point. If the shrink profile computed THIS way still rises toward the
    boundary, the rise reflects a real change in gradient direction, not
    just sigma_abs shrinking as H(z)->0 under the relative-sigma
    convention used elsewhere in this file."""
    E1, E2 = E1_E2_at_z(z)
    dHdx1 = (B1_FIT * E1) / (2.0 * H_at_fiducial(z) * KMSMPC_TO_SI**2)
    dHdx2 = (B2_FIT * E2) / (2.0 * H_at_fiducial(z) * KMSMPC_TO_SI**2)
    grad = np.array([dHdx1, dHdx2])
    F_base = analytic_fisher_matrix()
    F = F_base + np.outer(grad, grad) / sigma_abs_kms**2
    eigvals, _ = np.linalg.eigh(F)
    semi = semi_axis(2.0 * eigvals[0])
    return 1.0 - semi / semi_base


def H_at_fiducial(z):
    zdense = _dense_zgrid_through(np.array([z]))
    H_dense = H_of_z_kms(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    return float(np.interp(z, zdense, H_dense))


def analytic_fisher_eig(synth_zs=None, synth_sigma_rel=None):
    F = analytic_fisher_matrix(synth_zs, synth_sigma_rel)
    eigvals, eigvecs = np.linalg.eigh(F)
    v_small = eigvecs[:, 0]
    slope = (v_small[1] * B2_FIT) / (v_small[0] * B1_FIT)
    return eigvals, eigvecs, slope


def test_positive_control_analytic_fisher_matches_finite_difference_baseline():
    """Re-run of P193's own positive control, unchanged -- confirms the
    reused analytic machinery is still correct in this fresh copy."""
    eig_fd, _, slope_fd = hessian_eig(chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT, h=1e-6)
    eig_fisher, _, slope_fisher = analytic_fisher_eig()
    rel_err_small = abs(2 * eig_fisher[0] - eig_fd[0]) / abs(eig_fd[0])
    rel_err_large = abs(2 * eig_fisher[1] - eig_fd[1]) / abs(eig_fd[1])
    rel_err_slope = abs(slope_fisher - slope_fd) / abs(slope_fd)
    assert rel_err_small < 0.05, f"small eigenvalue mismatch: {rel_err_small:.2%}"
    assert rel_err_large < 0.05, f"large eigenvalue mismatch: {rel_err_large:.2%}"
    assert rel_err_slope < 0.01, f"slope mismatch: {rel_err_slope:.2%}"
    return rel_err_small, rel_err_large


def test_positive_control_analytic_fisher_matches_finite_difference_augmented():
    """Re-run of P193's own augmented-case cross-check, now at P193's
    z-set (still safely inside the domain) -- confirms the analytic
    method remains trustworthy in the augmented regime in this fresh
    copy before trusting it on P194's own new z-values."""
    eig_fd, _, slope_fd = hessian_eig(
        lambda h0a, b1, b2: augmented_chi2(h0a, b1, b2, P193_ZS, synth_sigma_rel=0.10),
        H0A_FIT,
        B1_FIT,
        B2_FIT,
        h=1e-6,
    )
    eig_fisher, _, slope_fisher = analytic_fisher_eig(P193_ZS, 0.10)
    rel_err_small = abs(2 * eig_fisher[0] - eig_fd[0]) / abs(eig_fd[0])
    rel_err_large = abs(2 * eig_fisher[1] - eig_fd[1]) / abs(eig_fd[1])
    rel_err_slope = abs(slope_fisher - slope_fd) / abs(slope_fd)
    assert rel_err_small < 0.10, f"augmented small eigenvalue mismatch: {rel_err_small:.2%}"
    assert rel_err_large < 0.10, f"augmented large eigenvalue mismatch: {rel_err_large:.2%}"
    assert rel_err_slope < 0.02, f"augmented slope mismatch: {rel_err_slope:.2%}"
    return rel_err_small, rel_err_large, rel_err_slope


def test_positive_control_scan_grid_stays_in_domain():
    """NEW for P194: the entire scan grid (up to z=16.5) plus a 0.1
    margin must have finite, positive H^2 at the fiducial parameters --
    the analytic method needs no (b1,b2) perturbation (unlike P193's
    finite-difference concern), but H(z) itself must still be real at
    every scanned z to build H_fid for the synthetic-point pin.

    BUG FOUND AND FIXED (2026-09-05, Step 8a skeptic pass): the original
    version built the dense grid via _dense_zgrid_through(SCAN_ZS), whose
    own zmax = max(Z_DESI, max(SCAN_ZS)) = 16.5 -- so the grid never
    actually reached the checked point z=16.6, and argmin(|zdense-16.6|)
    silently snapped to the nearest grid point (16.5), re-checking a
    point already checked rather than the intended margin point. Fixed
    by explicitly including the +0.1 check point in the grid build."""
    check_points = [*SCAN_ZS, 16.5 + 0.1]
    zdense = _dense_zgrid_through(np.array(check_points))
    H2 = H2_of_z(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    for z in check_points:
        idx = np.argmin(np.abs(zdense - z))
        assert abs(zdense[idx] - z) < 1e-9, f"grid does not contain the checked point z={z}"
        assert H2[idx] > 0, f"H^2(z={z}) not positive -- too close to the P192 boundary"
    assert max(SCAN_ZS) < BOUNDARY_Z, "scan grid must stay strictly below the found boundary"
    margin = BOUNDARY_Z - max(SCAN_ZS)
    assert margin > 0.3, f"scan grid margin to boundary too thin: {margin:.3f}"
    return margin


if __name__ == "__main__":
    test_positive_control_baseline_chi2_matches_p176()
    print("Positive control 1: baseline chi2 reproduces TJB's own chi2_33=15.75: PASS\n")

    rel_err_small, rel_err_large = (
        test_positive_control_analytic_fisher_matches_finite_difference_baseline()
    )
    print("Positive control 2: analytic Fisher matches finite-difference Hessian on")
    print(f"  baseline: small-eig {rel_err_small:.2%}, large-eig {rel_err_large:.2%} apart: PASS\n")

    aug_small, aug_large, aug_slope = (
        test_positive_control_analytic_fisher_matches_finite_difference_augmented()
    )
    print("Positive control 3: analytic Fisher matches finite-difference Hessian on")
    print(f"  P193's own augmented case (z={P193_ZS}, sigma=10%): small-eig")
    print(f"  {aug_small:.3%}, large-eig {aug_large:.3%}, slope {aug_slope:.4%} apart: PASS\n")

    margin = test_positive_control_scan_grid_stays_in_domain()
    print("Positive control 4 (NEW for P194): entire scan grid z<=16.5 has H^2>0,")
    print(f"  margin to P192's found boundary (z={BOUNDARY_Z}) = {margin:.3f}: PASS\n")

    eigvals_base, eigvecs_base, slope_base = hessian_eig(
        chi2_fixed_h0anchor, H0A_FIT, B1_FIT, B2_FIT, h=1e-6
    )
    semi_base = semi_axis(eigvals_base[0])

    print("=" * 78)
    print("STEP 1: information profile, single synthetic point at each scanned z,")
    print("        sigma_synth = 10% (the level directly comparable to P191/P193)")
    print("=" * 78)
    profile = {}
    for z in SCAN_ZS:
        eig, eigvecs, _ = analytic_fisher_eig([z], 0.10)
        semi = semi_axis(2.0 * eig[0])
        shrink = 1.0 - semi / semi_base
        angle = rotation_angle_deg(eigvecs_base, eigvecs)
        profile[z] = shrink
        print(f"  z={z:5.1f}:  single-point shrink = {shrink:6.2%}   rotation = {angle:5.2f} deg")

    shrinks = np.array([profile[z] for z in SCAN_ZS])
    is_monotonic = np.all(np.diff(shrinks) >= -1e-9)
    print(f"\n  Profile monotonically increasing toward the boundary: {is_monotonic}")
    if not is_monotonic:
        print("  (CLAIM_P194's own falsifiable predicate -- monotonic increase toward")
        print("   the boundary -- did NOT hold cleanly; reporting honestly, not forcing it.)")

    print()
    print("=" * 78)
    print("STEP 1b (added after Step 8a skeptic pass): is the monotonic rise a real")
    print("  direction effect, or a trivial 1/H(z)^4 scale artifact of using RELATIVE")
    print("  sigma_synth (sigma_abs = sigma_rel * H(z), which shrinks toward zero as")
    print("  H(z)->0 near the boundary, independent of gradient direction)?")
    print("=" * 78)
    print("  Gradient direction (degrees, mod 180 -- a line, not a ray) vs z:")
    angles = []
    for z in SCAN_ZS:
        ang = gradient_direction_deg(z) % 180.0
        angles.append(ang)
        print(f"    z={z:5.1f}: direction = {ang:6.3f} deg")
    angle_spread = max(angles) - min(angles)
    print(f"  Direction spread across the scan: {angle_spread:.4f} deg")

    print()
    print("  Second-round skeptic check (targeted re-check, 2026-09-05): a near-")
    print("  constant DIRECTION plus a rising fixed-sigma profile is consistent with")
    print("  |grad| growing via 1/H(z) -- but is ALSO consistent with |E1(z)|,|E2(z)|")
    print("  (the cumulative-integral numerators, growing by construction from")
    print("  z_ref) simply growing together at comparable rates, independent of")
    print("  H(z)->0 entirely. Printing both magnitudes to separate the two:")
    e1_vals, e2_vals, h_vals = [], [], []
    for z in SCAN_ZS:
        e1z, e2z = E1_E2_at_z(z)
        hz = H_at_fiducial(z)
        e1_vals.append(e1z)
        e2_vals.append(e2z)
        h_vals.append(hz)
        print(f"    z={z:5.1f}: |E1|={abs(e1z):.4e}  |E2|={abs(e2z):.4e}  H(z)={hz:8.2f} km/s/Mpc")
    e1_ratio = abs(e1_vals[-1] / e1_vals[0])
    e2_ratio = abs(e2_vals[-1] / e2_vals[0])
    h_ratio = h_vals[0] / h_vals[-1]
    print(f"  |E1| growth z=10.5->16.5: {e1_ratio:.3f}x   |E2| growth: {e2_ratio:.3f}x")
    print(f"  H(z) SHRINKAGE z=10.5->16.5 (1/H factor): {h_ratio:.3f}x")
    print("  If E1/E2 growth is small relative to the 1/H(z) factor, the boundary-")
    print("  proximity (sqrt-singularity) story dominates; if E1/E2 growth is")
    print("  comparable or larger, the cumulative-integral-accumulation story")
    print("  contributes materially and the mechanism is NOT uniquely 1/H(z).")

    print()
    print("  Cross-check: shrink profile at a FIXED absolute sigma (not scaled by")
    print("  H(z) at all) -- if this ALSO rises monotonically, the direction effect")
    print("  is real; if it flattens, the STEP 1 profile was mostly the 1/H(z)^4")
    print("  scale artifact:")
    sigma_abs_fixed = 0.10 * H_at_fiducial(13.5)  # 10% of a mid-scan-range H(z), fixed
    fixed_shrinks = []
    for z in SCAN_ZS:
        shrink_fixed = single_point_shrink_fixed_absolute_sigma(z, sigma_abs_fixed, semi_base)
        fixed_shrinks.append(shrink_fixed)
        print(f"    z={z:5.1f}: fixed-sigma shrink = {shrink_fixed:6.2%}")
    fixed_shrinks = np.array(fixed_shrinks)
    fixed_monotonic = np.all(np.diff(fixed_shrinks) >= -1e-9)
    print(f"  Fixed-absolute-sigma profile also monotonically increasing: {fixed_monotonic}")
    print(f"  Fixed-sigma range: [{fixed_shrinks.min():.2%}, {fixed_shrinks.max():.2%}]")
    print("  (a real but SMALLER rise than STEP 1's relative-sigma profile would mean")
    print("   BOTH effects are real -- direction contributes some, 1/H(z)^4 scaling")
    print("   contributes more; reported honestly either way, not forced.)")

    print()
    print("=" * 78)
    print("STEP 2: top-3 / top-4 individually-best points -- ACTUAL combined Fisher")
    print("        matrix (not summed shrinkage numbers), vs P193/P191 at matched sigma")
    print("=" * 78)
    ranked = sorted(SCAN_ZS, key=lambda z: -profile[z])
    top3 = sorted(ranked[:3])
    top4 = sorted(ranked[:4])
    print(f"  Top-3 individually-best z: {top3}")
    print(f"  Top-4 individually-best z: {top4}\n")

    for label, zset in (
        ("top-3 greedy", top3),
        ("top-4 greedy", top4),
        ("P193 {12,14,16}", P193_ZS),
        ("P191 {3,5,7,10}", P191_ZS),
    ):
        for sigma_rel in (0.01, 0.03, 0.10):
            eig, eigvecs, _ = analytic_fisher_eig(zset, sigma_rel)
            semi = semi_axis(2.0 * eig[0])
            shrink = 1.0 - semi / semi_base
            angle = rotation_angle_deg(eigvecs_base, eigvecs)
            print(
                f"  {label:20s} sigma={sigma_rel:.0%}: shrink={shrink:6.2%}  rotation={angle:5.2f} deg"
            )
        print()

    print("=" * 78)
    print("VERDICT: does the greedy top-N set beat P193's {12,14,16}?")
    print("=" * 78)
    for sigma_rel in (0.01, 0.03, 0.10):
        eig_top3, _, _ = analytic_fisher_eig(top3, sigma_rel)
        eig_p193, _, _ = analytic_fisher_eig(P193_ZS, sigma_rel)
        shrink_top3 = 1.0 - semi_axis(2.0 * eig_top3[0]) / semi_base
        shrink_p193 = 1.0 - semi_axis(2.0 * eig_p193[0]) / semi_base
        better = shrink_top3 > shrink_p193
        print(
            f"  sigma={sigma_rel:.0%}: top-3 greedy {shrink_top3:.2%} vs P193 {shrink_p193:.2%} -- greedy better: {better}"
        )
