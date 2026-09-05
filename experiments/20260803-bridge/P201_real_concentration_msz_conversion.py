"""P201 -- does real X-ray concentration (Buote+07, Schmidt&Allen+07),
instead of Duffy+08's simulated relation, change P197's own MSZ-to-
M200-equivalent conversion, and hence its 2.5x MSZ_equiv/M200c residual?

Connects two already-established findings that were never previously
combined: P196_ADDENDUM2 found real X-ray concentrations run 2-3.4x
higher than Duffy+08's simulated relation; P197's own MSZ->M200
conversion (solve_halo_matching_target_delta) is anchored on Duffy+08
alone. This file generalizes ADDENDUM2's own real-concentration solver
(which only matched at Delta=200) to match at an ARBITRARY target
Delta (500, for MSZ), so real concentration can be tested in exactly
the step where P196_ADDENDUM2 never tried it.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from P196_addendum2_real_xray_concentration import (
    buote_concentration,
    delta_bryan_norman,
    delta_lahav,
    schmidt_allen_concentration,
)
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_200 as _DELTA_200,
)
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_500 as _DELTA_500,
)
from P196_girardi_r_vir_vs_r200_check import (
    MSUN_TO_KG,
    duffy2008_concentration,
    r_delta_from_nfw_mpc,
    r_delta_mpc,
    rho_crit,
)
from scipy.optimize import brentq
from scipy.stats import pearsonr

MPC_TO_M_LOCAL = 3.0856775814913673e22


def _nfw_m_shape(x):
    return np.log(1.0 + x) - x / (1.0 + x)


def solve_halo_matching_arbitrary_target(
    target_mass_msun, target_delta, z, concentration_func, delta_obs_func
):
    """Generalizes P196_ADDENDUM2's own solve_halo_matching_m200c (which
    only matched at Delta=200) to match at an ARBITRARY target_delta --
    needed to test a real concentration source against MSZ (Delta=500),
    which ADDENDUM2 never did (it only ever matched against M200c).
    Find (M_vir, c_vir) such that c_vir=concentration_func(M_vir,z) (at
    that source's own delta_obs_func(z) convention) AND the resulting
    NFW halo's enclosed mass AT target_delta equals target_mass_msun.
    Returns (rho_s [kg/m^3], rs_mpc, c_vir, m_vir_msun)."""
    rc = rho_crit(z)

    def build(m_vir_guess_msun):
        c_vir = concentration_func(m_vir_guess_msun, z)
        delta_obs = delta_obs_func(z)
        r_vir_at_own_delta = r_delta_mpc(m_vir_guess_msun, z, delta_obs)
        rs_mpc = r_vir_at_own_delta / c_vir
        m_vir_kg = m_vir_guess_msun * MSUN_TO_KG
        rho_s = m_vir_kg / (4.0 * np.pi * (rs_mpc * MPC_TO_M_LOCAL) ** 3 * _nfw_m_shape(c_vir))
        return rho_s, rs_mpc, c_vir

    def residual(log10_m_vir_guess):
        m_vir_guess_msun = 10.0**log10_m_vir_guess
        rho_s, rs_mpc, _c_vir = build(m_vir_guess_msun)
        r_target_implied = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, target_delta)
        m_target_implied_kg = (
            (4.0 / 3.0) * np.pi * target_delta * rc * (r_target_implied * MPC_TO_M_LOCAL) ** 3
        )
        return (m_target_implied_kg / MSUN_TO_KG) - target_mass_msun

    log10_m_vir_sol = brentq(
        residual, np.log10(target_mass_msun) - 1.5, np.log10(target_mass_msun) + 1.5
    )
    m_vir_msun = 10.0**log10_m_vir_sol
    rho_s, rs_mpc, c_vir = build(m_vir_msun)
    return rho_s, rs_mpc, c_vir, m_vir_msun


def _m200_equivalent(rho_s, rs_mpc, z):
    r200 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, _DELTA_200)
    m200_kg = (4.0 / 3.0) * np.pi * _DELTA_200 * rho_crit(z) * (r200 * MPC_TO_M_LOCAL) ** 3
    return m200_kg / MSUN_TO_KG


def test_positive_control_duffy_matches_p197_baseline():
    """This file's own generalized solver, run with Duffy+08's concentration
    at target_delta=500 (MSZ's own convention), must reproduce P197's own
    already-verified solve_halo_matching_target_delta results exactly --
    validates the generalization before trusting it on real concentration."""
    from P197_mass_measurement_systematics import (
        solve_halo_matching_target_delta as p197_solver,
    )

    m_test, z_test = 4.0e14, 0.12
    rho_s_p197, rs_p197, c_p197, m200_p197 = p197_solver(m_test, _DELTA_500, z_test)

    rho_s_new, rs_new, c_new, m_vir_new = solve_halo_matching_arbitrary_target(
        m_test, _DELTA_500, z_test, duffy2008_concentration, lambda z: _DELTA_200
    )
    m200_new = _m200_equivalent(rho_s_new, rs_new, z_test)

    assert abs(rho_s_new - rho_s_p197) / rho_s_p197 < 1e-4
    assert abs(rs_new - rs_p197) / rs_p197 < 1e-4
    assert abs(m200_new - m200_p197) / m200_p197 < 1e-4
    return True


def test_positive_control_matches_addendum2_at_delta200():
    """This file's own generalized solver, run with a REAL concentration
    source at target_delta=200 (Delta=200's own convention), must reproduce
    P196_ADDENDUM2's own already-verified solve_halo_matching_m200c results
    exactly -- validates against the OTHER existing baseline."""
    from P196_addendum2_real_xray_concentration import (
        solve_halo_matching_m200c as addendum2_solver,
    )

    m_test, z_test = 3.5e14, 0.15
    rho_s_a2, rs_a2, c_a2, mvir_a2 = addendum2_solver(
        m_test, z_test, buote_concentration, delta_bryan_norman
    )

    rho_s_new, rs_new, c_new, mvir_new = solve_halo_matching_arbitrary_target(
        m_test, _DELTA_200, z_test, buote_concentration, delta_bryan_norman
    )

    assert abs(rho_s_new - rho_s_a2) / rho_s_a2 < 1e-4
    assert abs(rs_new - rs_a2) / rs_a2 < 1e-4
    assert abs(mvir_new - mvir_a2) / mvir_a2 < 1e-4
    return True


if __name__ == "__main__":
    from astroquery.vizier import Vizier

    test_positive_control_duffy_matches_p197_baseline()
    print("Positive control 1: generalized solver, Duffy+08 concentration,")
    print("  target_delta=500, exactly reproduces P197's own solve_halo_matching_")
    print("  target_delta results: PASS\n")

    test_positive_control_matches_addendum2_at_delta200()
    print("Positive control 2: generalized solver, real Buote+07 concentration,")
    print("  target_delta=200, exactly reproduces P196_ADDENDUM2's own")
    print("  solve_halo_matching_m200c results: PASS\n")

    print("Fetching HeCS-SZ (Rines et al. 2016, VizieR J/ApJ/819/63/table4)")
    print("independently this step, including both mass columns...")
    v = Vizier(columns=["ID", "z", "sigma", "M200c", "MSZ"], row_limit=-1)
    result = v.get_catalogs("J/ApJ/819/63/table4")
    tab = result[0]
    print(f"  -> {len(tab)} rows fetched\n")

    z_arr = np.array(tab["z"], dtype=float)
    m200c_arr = np.array(tab["M200c"], dtype=float) * 1.0e14
    msz_arr = np.array(tab["MSZ"], dtype=float) * 1.0e14
    valid = (
        np.isfinite(z_arr)
        & np.isfinite(m200c_arr)
        & np.isfinite(msz_arr)
        & (z_arr > 0)
        & (m200c_arr > 0)
        & (msz_arr > 0)
    )
    z_arr, m200c_arr, msz_arr = z_arr[valid], m200c_arr[valid], msz_arr[valid]
    n = len(z_arr)
    print(f"  -> {n} clusters with valid z, M200c, MSZ\n")

    sources = {
        "Duffy+08 (P197 baseline, simulated)": (duffy2008_concentration, lambda z: _DELTA_200),
        "Buote+07 (real X-ray)": (buote_concentration, delta_bryan_norman),
        "Schmidt&Allen+07 (real X-ray)": (schmidt_allen_concentration, delta_lahav),
    }

    results = {}
    for label, (cfunc, dfunc) in sources.items():
        m200_equiv = np.empty(n)
        c_used = np.empty(n)
        for i in range(n):
            rho_s, rs_mpc, c_vir, _m_vir = solve_halo_matching_arbitrary_target(
                msz_arr[i], _DELTA_500, z_arr[i], cfunc, dfunc
            )
            m200_equiv[i] = _m200_equivalent(rho_s, rs_mpc, z_arr[i])
            c_used[i] = c_vir
        mass_ratio = m200_equiv / m200c_arr
        results[label] = (mass_ratio, c_used)
        r_mass, _p_mass = pearsonr(m200c_arr, m200_equiv)
        print("=" * 88)
        print(f"SOURCE: {label}")
        print("=" * 88)
        print(f"  median concentration used = {np.median(c_used):.2f}")
        print(
            f"  mean(MSZ_equiv/M200c) = {mass_ratio.mean():.4f}   "
            f"scatter = {mass_ratio.std() / mass_ratio.mean():.4%}   r={r_mass:.4f}\n"
        )

    duffy_ratio, duffy_c = results["Duffy+08 (P197 baseline, simulated)"]
    buote_ratio, buote_c = results["Buote+07 (real X-ray)"]
    sa_ratio, sa_c = results["Schmidt&Allen+07 (real X-ray)"]

    print("=" * 88)
    print("CROSS-CHECK vs P197's own reported point estimate (2.5049)")
    print("=" * 88)
    rel_err_vs_p197 = abs(duffy_ratio.mean() - 2.5049) / 2.5049
    print(f"  This file's own Duffy+08 baseline mean ratio: {duffy_ratio.mean():.4f}")
    print(f"  Relative difference from P197's own reported 2.5049: {rel_err_vs_p197:.3%}")

    print()
    print("=" * 88)
    print("MCID CHECK (pre-registered in CLAIM_P201)")
    print("=" * 88)
    delta_buote = buote_ratio.mean() - duffy_ratio.mean()
    delta_sa = sa_ratio.mean() - duffy_ratio.mean()
    print("  Predicted DIRECTION (mechanistic reasoning): ratio should FALL (real")
    print("    concentration is higher -> more centrally peaked -> less extra mass")
    print("    between R500 and R200 -> smaller M200-equivalent for the same MSZ)\n")
    print(
        f"  Buote+07:        Delta(mean ratio) = {delta_buote:+.4f}   "
        f"(median c: {np.median(duffy_c):.2f} -> {np.median(buote_c):.2f})"
    )
    print(
        f"  Schmidt&Allen+07: Delta(mean ratio) = {delta_sa:+.4f}   "
        f"(median c: {np.median(duffy_c):.2f} -> {np.median(sa_c):.2f})"
    )
    material_buote = delta_buote < -0.2
    material_sa = delta_sa < -0.2
    print(f"\n  Buote+07 MATERIAL (Delta<-0.2, pre-registered MCID)? {material_buote}")
    print(f"  Schmidt&Allen+07 MATERIAL (Delta<-0.2, pre-registered MCID)? {material_sa}")

    print()
    print("=" * 88)
    print("VERDICT")
    print("=" * 88)
    if material_buote or material_sa:
        print("  Real X-ray concentration IS a material contributor to closing P197's")
        print("  MSZ_equiv/M200c residual -- direction and magnitude both support it.")
    else:
        print("  Real X-ray concentration does NOT materially change P197's residual")
        print("  via this specific conversion step, despite the correct mechanistic")
        print("  direction (if the sign above is negative) -- same 'real but")
        print("  insufficient' pattern as every other tested candidate in this line.")

    print()
    print("=" * 88)
    print("SKEPTIC FOLLOW-UP (Step 8a, round 1): restrict to clusters within")
    print("  Schmidt&Allen+07's own calibrated mass range, to test whether the")
    print("  MCID-crossing survives once the extrapolation confound is removed")
    print("=" * 88)
    # S&A's own pivot = 8e14 h^-1 Msun = 1.143e15 Msun at h=0.7; their own
    # sample (34 real Chandra clusters) spans roughly that pivot region.
    # Use MSZ >= 0.5x pivot as a conservative "mildly extrapolated" cut.
    sa_pivot_msun = 8.0e14 / 0.7
    mass_floor = 0.5 * sa_pivot_msun
    in_range = msz_arr >= mass_floor
    n_in_range = int(in_range.sum())
    print(f"  Mass floor: MSZ >= {mass_floor:.3e} Msun (0.5x Schmidt&Allen's own pivot)")
    print(f"  Clusters meeting this floor: {n_in_range}/{n}\n")

    if n_in_range >= 5:
        duffy_sub = duffy_ratio[in_range]
        buote_sub = buote_ratio[in_range]
        sa_sub = sa_ratio[in_range]
        delta_buote_sub = buote_sub.mean() - duffy_sub.mean()
        delta_sa_sub = sa_sub.mean() - duffy_sub.mean()
        print(f"  On this sub-sample (n={n_in_range}):")
        print(f"    Duffy+08 baseline mean ratio:  {duffy_sub.mean():.4f}")
        print(f"    Buote+07 Delta(mean ratio):     {delta_buote_sub:+.4f}")
        print(f"    Schmidt&Allen+07 Delta(mean ratio): {delta_sa_sub:+.4f}")
        print(
            f"\n  Schmidt&Allen+07 still MATERIAL on sub-sample (Delta<-0.2)? {delta_sa_sub < -0.2}"
        )
        print(f"  Buote+07 still MATERIAL on sub-sample (Delta<-0.2)? {delta_buote_sub < -0.2}")
        c_sa_sub = sa_c[in_range]
        print(
            f"\n  Schmidt&Allen concentration on sub-sample: median={np.median(c_sa_sub):.2f}, "
            f"fraction with c>10: {(c_sa_sub > 10).mean():.1%}"
        )
    else:
        print(f"  Too few clusters ({n_in_range}) to meaningfully sub-sample.")
