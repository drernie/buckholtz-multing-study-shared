"""E17 ADDENDUM 2 -- replace the Duffy et al. (2008) concentration-mass
extrapolation (E17's own flagged caveat: this project's M0=6e14 Msun is
6x above Duffy's own stated 1e14 Msun calibration ceiling) with Correa,
Wyithe, Schaye & Duffy (2015)'s own Paper III concentration-mass model
(arXiv:1502.00391), the SAME author lineage as the Paper II (1501.04382)
machinery E17 already reuses unchanged -- an EPS-theory-based model the
authors state explicitly "can be applied to wide ranges in mass,
redshift and cosmology," not a narrow fitted power law.

Only duffy2008_concentration_median is replaced. Everything else
(formation_redshift, alpha_beta, mass_history_ratio, v82_M_ref,
decompose_offset_and_jensen's own logic, REAL_DATA_ZS,
SIGMA_LOG10_C200_DUFFY08 as the scatter WIDTH around the new median) is
reused unchanged from E17_mass_scatter_for_F0_Faccretion.py -- isolating
the effect of the median-relation choice specifically.

See CLAIM_E17_mass_scatter_for_F0_Faccretion.md, "CLAIM ADDENDUM 2" --
MCID pre-registered before this file was run.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from E17_mass_scatter_for_F0_Faccretion import (
    M0_MSUN,
    N_MC,
    REAL_DATA_ZS,
    RNG,
    SIGMA_LOG10_C200_DUFFY08,
    formation_redshift,
    mass_history_ratio,
)
from E17_mass_scatter_for_F0_Faccretion import (
    decompose_offset_and_jensen as _e17_decompose,
)
from P176_v82_real_chi2_hessian_degeneracy import M0_kg
from P176_v82_real_chi2_hessian_degeneracy import M_of as v82_M_ref


def correa2015_paperIII_concentration_median(m_msun: float, z: float) -> float:
    """Correa, Wyithe, Schaye & Duffy (2015), arXiv:1502.00391, Section
    "Fitting functions for the c-M relation" -- their own Planck-cosmology
    fit, valid z<=4, "at all halo masses" (no narrow fitted-range ceiling
    the way Duffy et al. 2008's power-law fit has)."""
    log10_m = np.log10(m_msun)
    zp1 = 1.0 + z
    alpha = 1.7543 - 0.2766 * zp1 + 0.02039 * zp1**2
    beta = 0.2753 + 0.00351 * zp1 - 0.3038 * zp1**0.0269
    gamma = -0.01537 + 0.02102 * zp1 ** (-0.1475)
    log10_c = alpha + beta * log10_m * (1.0 + gamma * log10_m**2)
    return float(10.0**log10_c)


def draw_c_cluster_calibrated(sigma_log10_c, n, rng, m0_msun=M0_MSUN, z=0.0):
    c_med = correa2015_paperIII_concentration_median(m0_msun, z)
    log10_c = np.log10(c_med) + rng.normal(0.0, sigma_log10_c, n)
    return 10.0**log10_c, c_med


def decompose_offset_and_jensen_cluster_calibrated(sigma_log10_c, zs, powers, n=N_MC, rng=RNG):
    """Same logic as E17's own decompose_offset_and_jensen, with ONLY the
    concentration-median source swapped -- Correa Paper III instead of
    the Duffy+2008 extrapolation."""
    c_draws, c_med = draw_c_cluster_calibrated(sigma_log10_c, n, rng)
    zm2_draws = formation_redshift(c_draws)
    valid = zm2_draws >= 0.0
    excluded_frac = 1.0 - float(np.mean(valid))
    c_draws, zm2_draws = c_draws[valid], zm2_draws[valid]
    offset, jensen, combined = {}, {p: {} for p in powers}, {p: {} for p in powers}
    for z in zs:
        m_ratio = mass_history_ratio(c_draws, zm2_draws, z)
        ref_ratio = float(v82_M_ref(z) / M0_kg)
        mean_m = float(np.mean(m_ratio))
        offset[z] = mean_m / ref_ratio
        for p in powers:
            e_mp = float(np.mean(m_ratio**p))
            jensen[p][z] = e_mp / mean_m**p
            combined[p][z] = e_mp / ref_ratio**p
    return offset, jensen, combined, c_med, excluded_frac


def test_positive_control_zero_scatter_gives_unity_jensen():
    offset, jensen, combined, _, _ = decompose_offset_and_jensen_cluster_calibrated(
        0.0, REAL_DATA_ZS, (2.0, 1.5), n=1000
    )
    for z in REAL_DATA_ZS:
        for p in (2.0, 1.5):
            assert abs(jensen[p][z] - 1.0) < 1e-9, (z, p, jensen[p][z])
            assert abs(combined[p][z] - offset[z] ** p) < 1e-9, (z, p)


def test_positive_control_z_zero_boundary():
    offset, jensen, combined, _, _ = decompose_offset_and_jensen_cluster_calibrated(
        SIGMA_LOG10_C200_DUFFY08, (0.0,), (2.0, 1.5), n=5000
    )
    assert abs(offset[0.0] - 1.0) < 1e-12, offset[0.0]
    for p in (2.0, 1.5):
        assert abs(jensen[p][0.0] - 1.0) < 1e-12, jensen[p][0.0]
        assert abs(combined[p][0.0] - 1.0) < 1e-12, combined[p][0.0]


def test_positive_control_concentration_is_physically_sane():
    """Weak plausibility check only: concentration must be in a sane NFW
    range at E17's own (M0,z) points."""
    for z in REAL_DATA_ZS:
        c = correa2015_paperIII_concentration_median(M0_MSUN, z)
        assert 1.0 < c < 20.0, (z, c)


def test_positive_control_external_reproduction():
    """[Added after Step 8a skeptic FALSIFIED the control set for lacking
    any real external reproduction] Correa+2015 Paper III's own
    Discussion section (Section 4.4) states a real, directly-quoted
    number under a DIFFERENT (WMAP5) cosmology instantiation of their own
    broader model: "a 10^10 h^-1 Msun halo at z=2 has c~5.25" (h=0.72).
    This file's Planck-cosmology fitting formula (Section 11.1) is a
    different instantiation of the same underlying model -- exact
    agreement is not expected, but a real external check is: it must
    land within 25% of that real, quoted number (a genuine test the
    formula could fail, unlike the tautological PC1/PC2)."""
    h_wmap5 = 0.72
    m_msun = 1e10 / h_wmap5
    c = correa2015_paperIII_concentration_median(m_msun, 2.0)
    rel = abs(c - 5.25) / 5.25
    assert rel < 0.25, (c, rel)


if __name__ == "__main__":
    test_positive_control_zero_scatter_gives_unity_jensen()
    print("PC1 [tautological] zero scatter: jensen=1, combined=offset^n exactly: PASS")

    test_positive_control_z_zero_boundary()
    print("PC2 [tautological] z=0: offset=jensen=combined=1 exactly: PASS")

    test_positive_control_concentration_is_physically_sane()
    print("PC3 concentration stays in a physically sane range (1<c<20) at all 5 z: PASS")

    test_positive_control_external_reproduction()
    print("PC4 [real, non-tautological] Planck formula lands within 25% of a real quoted")
    print(
        "    WMAP5 number from Correa+2015's own Section 4.4 (10^10 h^-1 Msun, z=2, c~5.25): PASS\n"
    )

    offset_new, jensen_new, combined_new, c_med_new, excl_new = (
        decompose_offset_and_jensen_cluster_calibrated(
            SIGMA_LOG10_C200_DUFFY08, REAL_DATA_ZS, (2.0, 1.5)
        )
    )
    offset_old, jensen_old, combined_old, c_med_old, excl_old = _e17_decompose(
        SIGMA_LOG10_C200_DUFFY08, REAL_DATA_ZS, (2.0, 1.5)
    )

    print("=" * 100)
    print(
        f"Duffy+2008 (extrapolated, c_med={c_med_old:.3f}) vs Correa Paper III "
        f"(cluster-valid, c_med={c_med_new:.3f}) at M0={M0_MSUN:.3e} Msun"
    )
    print(f"  excluded fraction: Duffy {100 * excl_old:.2f}%  vs  Correa-III {100 * excl_new:.2f}%")
    print("=" * 100)
    print(
        f"{'z':>6} {'offset(Duffy)':>13} {'offset(C-III)':>13} {'shift offset':>12} "
        f"{'jensF0(Duffy)':>13} {'jensF0(C-III)':>13} {'shift jens':>10}"
    )
    material_zs = []
    for z in REAL_DATA_ZS:
        shift = abs(jensen_new[2.0][z] / jensen_old[2.0][z] - 1.0)
        shift_offset = abs(offset_new[z] / offset_old[z] - 1.0)
        print(
            f"{z:6.2f} {offset_old[z]:13.4f} {offset_new[z]:13.4f} {100 * shift_offset:11.1f}% "
            f"{jensen_old[2.0][z]:13.4f} {jensen_new[2.0][z]:13.4f} {100 * shift:9.1f}%"
        )
        if (z in (2.00, 2.33)) and (shift > 0.20 or shift_offset > 0.20):
            material_zs.append(z)
    print("\n  NOTE: the OFFSET shift is the larger effect (up to 75% at z=2.33) -- the")
    print("  earlier 'v82's own M(z) law diverges ~5x from a real MAH model' finding was")
    print("  itself partly an artefact of the Duffy extrapolation. Corrected arithmetic")
    print("  (per Step 8a skeptic catch -- the first draft dropped the jensen factor):")
    o_old, o_new = offset_old[2.33], offset_new[2.33]
    j_old, j_new = jensen_old[2.0][2.33], jensen_new[2.0][2.33]
    div_old = (o_old * j_old) ** -1
    div_new = (o_new * j_new) ** -1
    print(f"  divergence ~ 1/(offset*jensen): old {div_old:.2f}x -> new {div_new:.2f}x at z=2.33")
    print("  (offset-only scaling, dropping jensen, would give a DIFFERENT, wrong 2.8x.)")

    print("\n  WHY z=0 evaluation, not z_obs: v82's own M(z)=M0*(1+z)^-1.1 treats M0 as the")
    print("  z=0 ANCHOR mass of a single tracked object -- exactly Correa Paper II's own")
    print("  M(z)/M0 trajectory semantics. Evaluating Paper III's c(M0,z_obs) directly at")
    print("  each z_obs would instead ask about a DIFFERENT halo (one observed AT that z,")
    print("  not one whose z=0 mass is M0) -- internally inconsistent with the comparison")
    print("  being made. [Explicit choice, per Step 8a skeptic point 3 -- not a default.]")

    print("\n  TWO CAVEATS STILL OPEN (per Step 8a skeptic, not resolved here):")
    print("  (a) Duffy+2008's own sigma(log10 c)=0.15 scatter WIDTH is kept even though its")
    print("      MEDIAN was just rejected as out-of-range -- no sigma-sensitivity sweep run.")
    print("  (b) the exclusion-fraction change (5.65%->1.02%) is not decomposed from the")
    print("      median-swap effect -- some of the reported shift may be truncation, not")
    print("      purely the choice of c-M relation.")

    print("\n" + "=" * 100)
    print("MCID (pre-registered): MATERIAL if jensen OR offset shifts >20% at z=2.00 or z=2.33")
    print("=" * 100)
    print(f"  z in {{2.00, 2.33}} exceeding 20% shift: {material_zs}")
    print(f"  -> {'MATERIAL' if material_zs else 'not material -- Addendum 1 caveat resolved'}")
