"""E17 -- measure a real, sourced population scatter for M(z), to close
E16's own Pearl Registry Caveat Gate entry (F0/F_accretion also nonlinear
in M(z), un-scoped by E16's F1,F2-only correction).

Reuses, not reimplements:
  - P196_addendum_concentration_scatter.py's own duffy2008_concentration_median
    and SIGMA_LOG10_C200_DUFFY08 (real, [VERIFIED-arXiv:0804.2486] scatter).
  - Correa, Wyithe, Schaye & Duffy (2015) arXiv:1501.04382's own eqs 49-52
    (z_-2(c), alpha(c,z_-2), beta(z_-2), M(z)=M0*(1+z)^alpha*exp(beta*z)) --
    an N-body-validated error-propagation-capable MAH model, cited by v82's
    own ref [19]'s lineage (Zhao+2009 -> Correa+2015 builds directly on it).
  - E15's own Jensen's-gap closed-form machinery (exp(n^2*sigma^2/2) for
    M^n), applied here to F0~M^2 and F_accretion~M^1.5 instead of F1,F2.

See CLAIM_E17_mass_scatter_for_F0_Faccretion.md -- MCID pre-registered
before this file was run.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from P176_v82_real_chi2_hessian_degeneracy import (
    KMSMPC_TO_SI,
    MSUN_TO_KG,
    H0_planck_si,
    M0_kg,
    OL_planck,
    Om_planck,
)
from P176_v82_real_chi2_hessian_degeneracy import M_of as v82_M_ref
from P196_addendum_concentration_scatter import (
    SIGMA_LOG10_C200_DUFFY08,
    duffy2008_concentration_median,
)

H_LOCAL = (H0_planck_si / KMSMPC_TO_SI) / 100.0  # h = H0[km/s/Mpc] / 100
M0_MSUN = M0_kg / MSUN_TO_KG
A_COSMO_PLANCK = 798.0  # Correa+2015 Table 1 (their own quoted value for Planck cosmology)
N_MC = 200_000
RNG = np.random.default_rng(20260906)
REAL_DATA_ZS = (0.07, 0.25, 1.00, 2.00, 2.33)  # E15's own real data redshifts


def _Y(x):
    return np.log(1.0 + x) - x / (1.0 + x)


def formation_redshift(c, om=Om_planck, ol=OL_planck, a_cosmo=A_COSMO_PLANCK):
    """Correa+2015 eq 49. `np.cbrt` (real cube root), not `**(1/3)` (NaN on
    a negative base) -- extreme-low-c tail draws can make `inner` go
    negative, which correctly signals an UNPHYSICAL z_-2 < 0 (formation
    "before" z=0), not a numerical artifact to paper over. Callers must
    check for z_-2 < 0 explicitly (see sigma_ln_mz)."""
    inner = (200.0 / a_cosmo) * (c**3 * _Y(1.0)) / (om * _Y(c)) - ol / om
    return np.cbrt(inner) - 1.0


def alpha_beta(c, z_m2):
    """Correa+2015 eqs 50-51."""
    beta = -3.0 / (1.0 + z_m2)
    alpha = (np.log(_Y(1.0) / _Y(c)) - beta * z_m2) / np.log(1.0 + z_m2)
    return alpha, beta


def mass_history_ratio(c, z_m2, z):
    """Correa+2015 eq 52: M(z)/M0."""
    alpha, beta = alpha_beta(c, z_m2)
    return (1.0 + z) ** alpha * np.exp(beta * z)


def draw_c(sigma_log10_c, n, rng, m0_msun=M0_MSUN, z=0.0, h_local=H_LOCAL):
    c_med = duffy2008_concentration_median(m0_msun, z, h_local)
    log10_c = np.log10(c_med) + rng.normal(0.0, sigma_log10_c, n)
    return 10.0**log10_c, c_med


def decompose_offset_and_jensen(sigma_log10_c, zs, powers, n=N_MC, rng=RNG):
    """Monte Carlo, corrected TWICE after two Step 8a skeptic passes.

    Pass 1 FALSIFIED the original version (computed exp(n^2*sigma_ln(M)^2/2)
    = E[M^n]/median(M)^n under a parametric lognormal assumption, against
    the WRONG reference -- Correa's own MAH median instead of v82's own
    assumed M_ref(z)=M0*(1+z)^-1.1). Fixed to E[M^n]/M_ref(z)^n, computed
    directly from raw samples (no parametric shortcut).

    Pass 2, on that fix, verdict WEAKENED: the single combined number
    E[M^n]/M_ref(z)^n conflates TWO physically distinct effects that a
    caller MUST NOT treat as one "Jensen correction":
      offset(z)   = E[M(z)]/M_ref(z)       -- a SYSTEMATIC mismatch between
                     v82's own simple assumed mass-evolution law and this
                     real, N-body-calibrated MAH model. At z=2.33 this
                     alone is ~0.20 (a genuine ~5x divergence) -- NOT a
                     scatter/Jensen effect at all.
      jensen(n,z) = E[M(z)^n]/E[M(z)]^n    -- the ACTUAL Jensen's-gap
                     scatter correction (population-averaging vs
                     point-evaluation), the quantity E16's Pearl Registry
                     entry actually asked to close. Much smaller (order
                     1.5-3x at these redshifts, not ~12x).
      combined(n,z) = offset(z)^n * jensen(n,z) = E[M^n]/M_ref^n
    All three are returned, separately, so a caller cannot silently
    double-count or misattribute one for the other -- per the skeptic's
    own "Strongest objection" (naming/interpretation risk).

    Also per the skeptic's finding: excluding the 5.6% of draws with
    unphysical z_-2<0 (all low-c, would-be near-zero-mass at high z)
    biases E[M]/M_ref UPWARD -- the reported offset/combined numbers are
    an UPPER bound on the true (more severe) suppression, not a neutral
    estimate. Stated explicitly, not silently.

    NOT INDEPENDENTLY VALIDATED against Correa+2015's own published
    figures/tables at this M0 -- the skeptic named this as the one
    remaining real verification gap (PC1/PC2 here are structurally
    tautological, per their own review). Named as open, not closed."""
    c_draws, c_med = draw_c(sigma_log10_c, n, rng)
    zm2_draws = formation_redshift(c_draws)
    valid = zm2_draws >= 0.0
    excluded_frac = 1.0 - float(np.mean(valid))
    c_draws, zm2_draws = c_draws[valid], zm2_draws[valid]
    offset, jensen, combined = {}, {p: {} for p in powers}, {p: {} for p in powers}
    for z in zs:
        m_ratio = mass_history_ratio(c_draws, zm2_draws, z)  # M(z)/M0, per draw
        ref_ratio = float(v82_M_ref(z) / M0_kg)  # v82's own M_ref(z)/M0, a scalar
        mean_m = float(np.mean(m_ratio))
        offset[z] = mean_m / ref_ratio
        for p in powers:
            e_mp = float(np.mean(m_ratio**p))
            jensen[p][z] = e_mp / mean_m**p
            combined[p][z] = e_mp / ref_ratio**p
    return offset, jensen, combined, c_med, excluded_frac


def test_positive_control_zero_scatter_gives_unity_jensen():
    """[Tautological, per 2nd skeptic pass -- not independent physics
    verification, only an implementation-identity check.] At zero
    concentration scatter every draw is identical, so jensen(n,z) must be
    exactly 1.0 (no scatter -> no Jensen gap) and combined(n,z) must equal
    offset(z)**n exactly, for both n=2 and n=1.5."""
    offset, jensen, combined, _, _ = decompose_offset_and_jensen(
        0.0, REAL_DATA_ZS, (2.0, 1.5), n=1000
    )
    for z in REAL_DATA_ZS:
        for p in (2.0, 1.5):
            assert abs(jensen[p][z] - 1.0) < 1e-9, (z, p, jensen[p][z])
            assert abs(combined[p][z] - offset[z] ** p) < 1e-9, (z, p)


def test_positive_control_z_zero_boundary():
    """[Tautological, per 2nd skeptic pass -- both sides are 1 by
    construction at z=0.] M(0)=M0 for every draw and M_ref(0)=M0 too --
    offset, jensen, and combined must all be exactly 1.0 at z=0,
    independent of concentration scatter."""
    offset, jensen, combined, _, _ = decompose_offset_and_jensen(
        SIGMA_LOG10_C200_DUFFY08, (0.0,), (2.0, 1.5), n=5000
    )
    assert abs(offset[0.0] - 1.0) < 1e-12, offset[0.0]
    for p in (2.0, 1.5):
        assert abs(jensen[p][0.0] - 1.0) < 1e-12, jensen[p][0.0]
        assert abs(combined[p][0.0] - 1.0) < 1e-12, combined[p][0.0]


def test_positive_control_reuse_matches_p196_addendum():
    """The concentration median used here must match
    P196_addendum_concentration_scatter.py's own function exactly --
    confirms no re-implementation drift."""
    _, _, _, c_med, _ = decompose_offset_and_jensen(0.0, (1.0,), (2.0,), n=10)
    expected = duffy2008_concentration_median(M0_MSUN, 0.0, H_LOCAL)
    assert c_med == expected


if __name__ == "__main__":
    test_positive_control_zero_scatter_gives_unity_jensen()
    print("PC1 [tautological] zero scatter: jensen=1, combined=offset^n exactly: PASS")

    test_positive_control_z_zero_boundary()
    print(
        "PC2 [tautological] z=0: offset=jensen=combined=1 exactly (both sides =1 by construction): PASS"
    )

    test_positive_control_reuse_matches_p196_addendum()
    print("PC3 concentration median matches P196_addendum's own function exactly: PASS")
    print(
        "NOT DONE (named open by 2nd skeptic pass): no control cross-checks mass_history_ratio"
        " against Correa+2015's own published Fig 3/Table values at this M0 -- PC1-3 verify"
        " implementation identities, not numerical calibration against the source paper.\n"
    )

    offset, jensen, combined, c_med, excluded_frac = decompose_offset_and_jensen(
        SIGMA_LOG10_C200_DUFFY08, REAL_DATA_ZS, (2.0, 1.5)
    )
    print("=" * 100)
    print(
        f"Correa+2015 MAH model vs v82's OWN M_ref(z)=M0*(1+z)^-1.1 (Duffy+08 "
        f"sigma(log10 c)={SIGMA_LOG10_C200_DUFFY08}, c_median={c_med:.3f})"
    )
    print(f"  ({100 * excluded_frac:.3f}% of {N_MC:,} draws excluded: unphysical z_-2 < 0 --")
    print("   ALL at the low-c/near-zero-mass tail, so reported offset/combined below are an")
    print("   UPPER BOUND: the true suppression is at least this large, per 2nd skeptic pass.)")
    print("=" * 100)
    print(
        f"{'z':>6} {'offset=E[M]/Mref':>17} {'jensen(F0,n=2)':>15} {'jensen(Facc,n=1.5)':>19} "
        f"{'combined(F0)':>13} {'combined(Facc)':>15}"
    )
    for z in REAL_DATA_ZS:
        print(
            f"{z:6.2f} {offset[z]:17.4f} {jensen[2.0][z]:15.4f} {jensen[1.5][z]:19.4f} "
            f"{combined[2.0][z]:13.4f} {combined[1.5][z]:15.4f}"
        )
    print("\n  offset(z) = E[M]/M_ref: a SYSTEMATIC mismatch between v82's own simple assumed")
    print("  mass law and this real, N-body-calibrated MAH model -- NOT a scatter/Jensen effect.")
    print("  At z=2.33 this alone accounts for ~96% of the combined number's magnitude.")
    print("  jensen(n,z) = E[M^n]/E[M]^n: the ACTUAL Jensen's-gap scatter correction E16's Pearl")
    print("  Registry entry asked to close -- much smaller (~1.9x at z=2.33, not ~12x).")

    print("\n" + "=" * 100)
    print("MCID (pre-registered, reusing E15's 10% threshold), applied to the JENSEN component")
    print("ONLY -- the quantity this experiment was actually asked to measure, per its own claim")
    print("=" * 100)
    material_zs = [
        z
        for z in REAL_DATA_ZS
        if abs(jensen[2.0][z] - 1.0) > 0.10 or abs(jensen[1.5][z] - 1.0) > 0.10
    ]
    print(f"  redshifts where the JENSEN (scatter-only) correction exceeds 10%: {material_zs}")
    print(f"  -> {'MATERIAL' if material_zs else 'not material'}")
    print("\n  The OFFSET finding (v82's own M(z) law vs real MAH models) is separately reported")
    print("  above -- large, real, but a DIFFERENT claim than E16's Jensen-correction gap, and")
    print("  NOT independently validated against Correa+2015's own published values (open gap).")

    print("\n" + "=" * 100)
    print("SCOPE CAVEAT (stated in claim.md, repeated here): the JENSEN component measures ONLY")
    print("the concentration-driven channel of M(z) scatter (Correa+2015's own eq 49, applied")
    print("deterministically per draw). Correa's own paper finds real z_-2 scatter is NOT fully")
    print("explained by concentration scatter alone -- a lower-bound-flavored partial estimate.")
