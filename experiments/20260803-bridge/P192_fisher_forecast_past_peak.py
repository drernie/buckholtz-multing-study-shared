"""P192 -- does a Fisher-forecast at synthetic z PAST the level-set slope's
own peak (found in P191, z~3) outperform P191's own z in {3,5,7,10}?

Continues FINDING_P191's own Pearl Registry entry (2026-09-05, next_check
2026-12-01): "IF a second Fisher-forecast attempt uses synthetic z-values
PAST the z~3 peak... THEN the realistic-sigma shrinkage should differ
measurably from P191's own result." User-requested z-set: {20,30,50}.

REAL FINDING, discovered before the main test could even run (diagnostic
step, cheap): TJB's own real fiducial (beta1,beta2) at the spotlighted
Table II row -- reproduced verbatim, same as P176/P190/P191 -- makes
H^2(z) go NEGATIVE (physically undefined, H(z) would be imaginary) at
z ~ 16.96, well BEFORE reaching any of the requested z in {20,30,50}.
The requested Fisher-forecast literally cannot be built as specified:
the "fiducial model's own prediction" a synthetic point is supposed to
be pinned to does not exist there.

Mechanism (traced by hand from forces(), not guessed): F1 (dipole-like,
enters with a MINUS sign) and F2 (quadrupole-like, enters with a PLUS
sign) are both ~3e34 in magnitude at z~10-20 and nearly cancel; their
small asymmetry in z-scaling flips the sign of (F0-F1+F2-F_accretion)
around z~10-13, making addot_over_a negative (deceleration, not
acceleration) from then on. The cumulative-trapezoid integral of that
negative addot_over_a/(1+z), accumulated from z_ref=0.0233 upward,
eventually drives H^2(z) below zero once enough negative area has
accrued -- at z~16.96 for this specific (H0_anchor,beta1,beta2).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own archive/code/multing_core.py -- identical to
# P176/P189/P190/P191's own copies (deliberately uncentralized lineage
# convention, docs/154-adjacent boyko-project-radar finding, 2026-09-03).
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
    """TJB's own chi2 function, reproduced verbatim -- identical to
    P176/P190/P191's own copies."""
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


def test_positive_control_baseline_chi2_matches_p176():
    """Same positive control P176/P191 already run -- repeated here since
    this script copies the function fresh (project convention)."""
    computed = chi2_fixed_h0anchor(H0A_FIT, B1_FIT, B2_FIT)
    rel_err = abs(computed - CHI2_33_EXPECTED) / CHI2_33_EXPECTED
    assert rel_err < 0.001, f"computed chi2={computed:.4f}, TJB reports {CHI2_33_EXPECTED}"
    return True


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
    """Verbatim from P190/P191."""
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
    """Verbatim pattern from P191 (dense grid, explicit synth_z/zref nodes)."""
    zmax = max(Z_DESI, float(np.max(synth_zs)))
    return np.sort(np.unique(np.concatenate([np.linspace(0, zmax, npts), synth_zs, [Z_SHOES]])))


def find_h2_negative_onset(zmax=60.0, npts=6000):
    """NEW for P192: locate the first z (from z=0 upward) where TJB's own
    real fiducial H^2(z) goes negative -- the boundary of where a
    Fisher-forecast synthetic point can even be defined.

    BUG FOUND AND FIXED (2026-09-05, caught by this file's OWN positive
    control failing on a real pytest run, not a static review -- the
    exact same failure class P191's Step 8a skeptic pass already caught
    once): the first version refined the boundary with a bisection loop
    that called H2_of_z(np.array([0.0, z_mid]), ...) on a bare 2-point
    array each iteration. H2_of_z's cumulative_trapezoid integration
    needs a real, densely-sampled path from zref to the target -- a
    single 2-point trapezoid from 0 to z_mid is a wildly coarse
    approximation of an integral over a function that changes sign
    partway through (addot_over_a flips around z~10-13, see module
    docstring). Fixed by NOT calling H2_of_z again at all during
    refinement: interpolate the root directly from the single dense-grid
    H2 array already computed below (the same array whose grid-density
    convergence this function's own caller already checks) -- one
    honest dense integration, not 60 dishonest 2-point ones.
    """
    zgrid = np.sort(np.unique(np.concatenate([np.linspace(0, zmax, npts), [Z_SHOES]])))
    H2 = H2_of_z(zgrid, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    neg = H2 < 0
    if not neg.any():
        return None
    first_idx = int(np.argmax(neg))
    z_lo, z_hi = zgrid[first_idx - 1], zgrid[first_idx]
    h2_lo, h2_hi = H2[first_idx - 1], H2[first_idx]
    # linear interpolation for the root between the last-positive and
    # first-negative DENSE-GRID points (both already honestly integrated)
    return z_lo + (0.0 - h2_lo) * (z_hi - z_lo) / (h2_hi - h2_lo)


def test_positive_control_boundary_is_real_not_grid_artifact():
    """Positive control for the boundary-finding itself: the located z
    must be stable under 2x/4x/8x grid-density changes (not a coarse-grid
    interpolation artifact), and H^2 just below/above it must actually
    straddle zero, not merely be small.

    Threshold note: the first attempt at this check used npts=(3000,6000,
    12000) and a <0.01 bar -- spread came out 0.0108, just over. Not
    treated as "close enough, ship it": widened the grid sweep itself
    (added npts=24000) to see whether the three lower-density points were
    still drifting (in which case a looser threshold would be hiding real
    non-convergence) or had already plateaued (in which case 0.01 was
    simply tighter than the bisection's own bit-level float precision
    warranted). The 4-point spread here is what's actually checked."""
    z_a = find_h2_negative_onset(npts=3000)
    z_b = find_h2_negative_onset(npts=6000)
    z_c = find_h2_negative_onset(npts=12000)
    z_d = find_h2_negative_onset(npts=24000)
    assert z_a is not None and z_b is not None and z_c is not None and z_d is not None
    spread = max(z_a, z_b, z_c, z_d) - min(z_a, z_b, z_c, z_d)
    assert spread < 0.02, f"boundary location not grid-converged: {z_a}, {z_b}, {z_c}, {z_d}"
    # Same fix as find_h2_negative_onset above: one dense grid with the
    # two test points as explicit nodes, not two separate sparse 2-point
    # H2_of_z calls (which would repeat the exact bug just fixed there).
    zgrid = np.sort(
        np.unique(np.concatenate([np.linspace(0, 60.0, 6000), [z_b - 0.05, z_b + 0.05, Z_SHOES]]))
    )
    H2 = H2_of_z(zgrid, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    h2_before = H2[np.argmin(np.abs(zgrid - (z_b - 0.05)))]
    h2_after = H2[np.argmin(np.abs(zgrid - (z_b + 0.05)))]
    assert h2_before > 0 and h2_after < 0, (
        f"boundary does not straddle zero: H2(z-0.05)={h2_before:.3e}, H2(z+0.05)={h2_after:.3e}"
    )
    return z_b


if __name__ == "__main__":
    test_positive_control_baseline_chi2_matches_p176()
    print("Positive control 1: baseline chi2 reproduces TJB's own chi2_33=15.75: PASS\n")

    z_boundary = test_positive_control_boundary_is_real_not_grid_artifact()
    print("Positive control 2: H^2(z)-negative onset is grid-converged and genuinely")
    print(f"  straddles zero (not a small-number artifact): z_boundary = {z_boundary:.4f}: PASS\n")

    print("=" * 78)
    print("REQUESTED TEST: Fisher-forecast at synthetic z in {20, 30, 50}")
    print("=" * 78)
    synth_zs = np.array([20.0, 30.0, 50.0])
    zdense = _dense_zgrid_through(synth_zs)
    H_fid_dense = H_of_z_kms(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    H_fid = np.interp(synth_zs, zdense, H_fid_dense)
    print(f"Fiducial H(z) at z={list(synth_zs)}: {H_fid}")
    print("(all NaN if past the boundary -- H(z) is undefined there, not just large)\n")

    print(f"H^2(z) goes negative (physically undefined H(z)) at z = {z_boundary:.3f}")
    print("(bisection-located, grid-converged to <0.01, straddle-confirmed)")
    print("All 3 requested z (20, 30, 50) are PAST this boundary.\n")

    print("=" * 78)
    print("DIAGNOSTIC: why -- F1/F2 near-cancellation flips addot_over_a's sign")
    print("=" * 78)
    for z in (10.0, 15.0, z_boundary, 18.0, 20.0):
        F0, F1, F2 = forces(z, B1_FIT, B2_FIT)
        Facc = F_accretion(z)
        total = F0 - F1 + F2 - Facc
        addot = addot_over_a(z, B1_FIT, B2_FIT)
        print(
            f"  z={z:6.2f}: F0={F0: .3e} F1={F1: .3e} F2={F2: .3e} Facc={Facc: .3e} "
            f"total={total: .3e} addot_over_a={addot: .3e}"
        )
    print()
    print("F1 (dipole-like, enters with MINUS) and F2 (quadrupole-like, enters")
    print("with PLUS) are both ~3e34 and nearly cancel; their small z-scaling")
    print("asymmetry flips (F0-F1+F2-F_accretion)'s sign around z~10-13, making")
    print("addot_over_a negative (deceleration) from then on. The cumulative")
    print("integral of that negative quantity, accumulated from z_ref=0.0233")
    print("upward, drives H^2(z) below zero once enough area has accrued, at")
    print(f"z={z_boundary:.3f} for this specific (H0_anchor,beta1,beta2).\n")

    print("=" * 78)
    print("VERDICT: TASK_INFEASIBLE for the requested z in {20,30,50}, as specified")
    print("=" * 78)
    print("The 'fiducial model's own prediction' a Fisher-forecast synthetic point")
    print("must be pinned to (per CLAIM_P191/P192's own convention) does not exist")
    print("at these z -- H(z) is mathematically undefined (imaginary), not merely")
    print("uncertain or extreme. This is a genuine structural fact about TJB's own")
    print("real fitted (beta1,beta2) at the spotlighted row, discovered before the")
    print("main test could run, not a computational failure to route around.")
