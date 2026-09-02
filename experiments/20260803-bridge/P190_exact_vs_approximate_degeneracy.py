"""P190 -- is v82's own (beta1,beta2) degeneracy (FINDING_P176) an EXACT
parametrization redundancy, or an approximate, data-range-limited
near-degeneracy?

forces(z,b1,b2) (TJB's own multing_core.py, verbatim -- reproduced already
in P176's own script) is LINEAR in (b1,b2) at each fixed z:
  F1(z,b1) = b1 * (-G) * 2*M(z) * (k(z)/c^2) * (R(z)/d(z)) / d(z)^2
  F2(z,b2) = b2 * (-G) * (k(z)/c^2)^2 * (R(z)^2/d(z)^2) / d(z)^2
addot_over_a(z,b1,b2) = (F0(z) - F1(z,b1) + F2(z,b2) - F_acc(z)) / (M(z)/2) / d(z)
is therefore AFFINE in (b1,b2) at each z, and H^2(z) (built by cumulative-
trapezoid integration of addot_over_a(z)/(1+z), a LINEAR operation) is
therefore also affine in (b1,b2) at each z:
  H^2(z; H0_anchor, b1, b2) = P(z) + b1*E1(z) + b2*E2(z)
An EXACT degeneracy direction exists iff E1(z)/E2(z) is the SAME number
for every z (a symmetry of the full functional form) -- not just locally
flat at one fit point, which is all P176's numeric Hessian checked.

E1(z), E2(z) come directly from differentiating F1, F2 w.r.t. b1, b2 and
propagating through the SAME cumulative integral H2_of_z uses -- since
integration is linear, d(H^2)/db1 (z) = 2 * cumtrapz[ -dF1/db1(z')/(1+z') /
(M(z')/2) / d(z') ] evaluated the same way P176's H2_of_z does it, i.e.
E1(z) is itself an integral, not a pointwise ratio -- see Method below for
why the "ratio of two z-dependent functions" framing in the claim.md is
evaluated as the ratio of two INTEGRALS (cumulative from zref to z), not a
pointwise force ratio, to correctly capture what determines H(z) itself
(not just addot_over_a(z) itself).

Positive control: symbolic E1(z), E2(z) (via sympy, evaluated numerically
at test z-values) must match a finite-difference dH^2/db1, dH^2/db2 taken
directly on P176's own (already positive-controlled) numeric H2_of_z
function, before anything derived from the symbolic version is trusted.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own archive/code/multing_core.py, same constants and
# functions P176's own script already positive-controlled.
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


def dF1_db1(z):
    """d(F1)/d(b1) -- the b1-linear coefficient of forces(), z-dependent only."""
    M, R, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
    return (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2


def dF2_db2(z):
    """d(F2)/d(b2) -- the b2-linear coefficient of forces(), z-dependent only."""
    R, k, d = R_of(z), k_of(z), d_of(z)
    return (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2


def d_addot_db1(z):
    """d(addot_over_a)/d(b1) at fixed z -- note the MINUS sign in
    addot_over_a = (F0 - F1 + F2 - F_acc)/(M/2)/d, so this is -dF1/db1."""
    return -dF1_db1(z) / (M_of(z) / 2.0) / d_of(z)


def d_addot_db2(z):
    """d(addot_over_a)/d(b2) at fixed z -- PLUS sign (F2 enters with +)."""
    return dF2_db2(z) / (M_of(z) / 2.0) / d_of(z)


# ---------------------------------------------------------------------------
# Reproduce P176's own H2_of_z EXACTLY (verbatim), so the finite-difference
# positive control is checking the identical function P176 already trusts.
# ---------------------------------------------------------------------------
Z_SHOES = 0.0233


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


# TJB's own real fit point (spotlighted row, Table II, verbatim from P176).
H0A_FIT = 73.22
B1_FIT = 1.4335e10
B2_FIT = 7.8067e17
EMPIRICAL_SLOPE = 6.073104e07  # P176's own found near-null slope at this row


def test_positive_control_finite_diff_matches_analytic_E1E2():
    """The analytic d(addot)/db1, d(addot)/db2 (pointwise, no integration
    yet) must match a finite-difference derivative of H2_of_z's own
    integrand at several individual z -- confirms the coefficient
    functions are correctly extracted from forces() before propagating
    them through the integral.
    """
    test_zs = [0.07, 0.5, 1.0, 1.965, 2.33]
    h = 1e-3  # relative step on b1, b2 (both O(1e10)/O(1e17), so scale h*B)
    for z in test_zs:
        # finite-difference d(addot_over_a)/db1 at fixed z
        db1 = h * B1_FIT
        fd_db1 = (addot_over_a(z, B1_FIT + db1, B2_FIT) - addot_over_a(z, B1_FIT - db1, B2_FIT)) / (
            2 * db1
        )
        an_db1 = d_addot_db1(z)
        rel_err1 = abs(fd_db1 - an_db1) / abs(an_db1)
        assert rel_err1 < 1e-6, (
            f"z={z}: d(addot)/db1 mismatch, fd={fd_db1:.6e} analytic={an_db1:.6e}"
        )

        db2 = h * B2_FIT
        fd_db2 = (addot_over_a(z, B1_FIT, B2_FIT + db2) - addot_over_a(z, B1_FIT, B2_FIT - db2)) / (
            2 * db2
        )
        an_db2 = d_addot_db2(z)
        rel_err2 = abs(fd_db2 - an_db2) / abs(an_db2)
        assert rel_err2 < 1e-6, (
            f"z={z}: d(addot)/db2 mismatch, fd={fd_db2:.6e} analytic={an_db2:.6e}"
        )
    return True


def E1_E2_at_z(z_target, zref=Z_SHOES, npts=2000):
    """E1(z_target) = d(H^2(z_target))/d(b1), E2(z_target) = d(H^2(z_target))/d(b2),
    computed by propagating the pointwise derivatives d_addot_db1/db2 through
    the SAME cumulative-trapezoid integration H2_of_z uses (integration is
    linear, so this is exact -- no finite-differencing of the full pipeline
    needed once the pointwise derivatives are confirmed correct above).
    """
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


def test_E1_E2_match_full_finite_difference_on_H2_of_z():
    """Second positive control: E1(z), E2(z) from the linear-propagation
    shortcut above must match a DIRECT finite-difference derivative of
    P176's own actual H2_of_z function (the one used in chi2), at several
    z -- the real end-to-end check, not just the pointwise one above.

    H2_of_z's cumulative_trapezoid integration is degenerate on a
    single-point zgrid (nothing to integrate against -- it silently
    returns H2=H0_anchor^2, nonsense for this check), so this must call
    it on a dense grid (matching how P176's own chi2 actually uses it)
    and interpolate at the target z, not call it on `np.array([z])` alone.
    """
    test_zs = [0.5, 1.965]
    h = 1e-4
    dense_zg = np.sort(np.unique(np.concatenate([np.linspace(0, 2.33, 2000), test_zs, [Z_SHOES]])))
    for z in test_zs:
        E1, E2 = E1_E2_at_z(z)
        db1 = h * B1_FIT
        H2_plus = np.interp(z, dense_zg, H2_of_z(dense_zg, H0A_FIT, B1_FIT + db1, B2_FIT, Z_SHOES))
        H2_minus = np.interp(z, dense_zg, H2_of_z(dense_zg, H0A_FIT, B1_FIT - db1, B2_FIT, Z_SHOES))
        fd_E1 = (H2_plus - H2_minus) / (2 * db1)
        rel_err1 = abs(fd_E1 - E1) / abs(E1)
        assert rel_err1 < 1e-3, (
            f"z={z}: E1 mismatch, fd={fd_E1:.6e} propagated={E1:.6e} (rel {rel_err1:.4%})"
        )

        db2 = h * B2_FIT
        H2_plus = np.interp(z, dense_zg, H2_of_z(dense_zg, H0A_FIT, B1_FIT, B2_FIT + db2, Z_SHOES))
        H2_minus = np.interp(z, dense_zg, H2_of_z(dense_zg, H0A_FIT, B1_FIT, B2_FIT - db2, Z_SHOES))
        fd_E2 = (H2_plus - H2_minus) / (2 * db2)
        rel_err2 = abs(fd_E2 - E2) / abs(E2)
        assert rel_err2 < 1e-3, (
            f"z={z}: E2 mismatch, fd={fd_E2:.6e} propagated={E2:.6e} (rel {rel_err2:.4%})"
        )
    return True


if __name__ == "__main__":
    test_positive_control_finite_diff_matches_analytic_E1E2()
    print("Positive control 1: analytic d(addot_over_a)/db1, db2 match finite-difference")
    print("  at 5 test z-values to < 1e-6 relative error: PASS\n")

    test_E1_E2_match_full_finite_difference_on_H2_of_z()
    print("Positive control 2: E1(z), E2(z) (propagated through the cumulative-trapezoid")
    print("  integral) match a direct finite-difference on P176's own H2_of_z function")
    print("  at z=0.5, 1.965 to < 0.1% relative error: PASS\n")

    print("=" * 70)
    print("MAIN CHECK: is -E1(z)/E2(z) (the level-set slope d(beta2)/d(beta1)")
    print("            holding H^2(z) fixed at THIS z alone) constant across z")
    print("            (exact symmetry) or does it vary (approximate)?")
    print("=" * 70)
    test_zs = [0.07, 0.09, 0.2, 0.5, 0.9, 1.3, 1.965, 2.33]
    slopes = []
    for z in test_zs:
        E1, E2 = E1_E2_at_z(z)
        # H^2(z) = P(z) + b1*E1(z) + b2*E2(z); holding H^2(z) fixed at THIS z
        # alone: Delta_b1*E1(z) + Delta_b2*E2(z) = 0  =>  Delta_b2/Delta_b1 = -E1(z)/E2(z)
        slope = -E1 / E2
        slopes.append(slope)
        print(f"  z={z:6.3f}:  E1(z)={E1: .6e}  E2(z)={E2: .6e}  -E1/E2={slope: .6e}")

    slopes = np.array(slopes)
    spread = (slopes.max() - slopes.min()) / np.mean(np.abs(slopes))
    print(f"\n  Spread of -E1(z)/E2(z) across z=0.07..2.33: {spread:.4%}")
    print(f"  Compare: P176's own found near-null slope d(beta2)/d(beta1) = {EMPIRICAL_SLOPE:.6e}")
    print(f"  Range of single-z slopes above: [{slopes.min():.4e}, {slopes.max():.4e}]")

    if spread < 0.001:
        print("\n  VERDICT: -E1(z)/E2(z) is CONSTANT across z (< 0.1% spread) -- this IS an")
        print("  EXACT symmetry direction of H^2(z), not just a local numerical coincidence.")
    else:
        print(
            f"\n  VERDICT: -E1(z)/E2(z) VARIES with z ({spread:.4%} spread) -- NOT an exact symmetry."
        )
        print("  P176's found near-flat direction is a real but data-range-specific")
        print("  near-degeneracy of the actual 33-point weighted chi-squared surface, not a")
        print("  structural redundancy in the (beta1,beta2) parametrization itself.")
