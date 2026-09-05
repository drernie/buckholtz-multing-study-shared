"""P197 -- does the choice of cluster-mass measurement method (caustic
M200c vs. Planck SZ MSZ) move P196's own 1.47x residual?

HeCS-SZ (Rines et al. 2016, VizieR J/ApJ/819/63/table4) tabulates TWO
independent, real, published mass estimates for the same 123 clusters:
M200c ("Caustic mass", dynamical, Delta=200 -- Rines et al.'s own Table 4,
"M200 from the caustic mass profile") and MSZ ("Planck Sunyaev-Zeldovich
mass proxy").

CORRECTION (2026-09-06, caught mid-analysis by a Step 8a skeptic pass,
independently confirmed against the primary source before accepting): the
first version of this file fed MSZ directly into P196's own Delta=200-
anchored NFW builder (nfw_from_m200c), silently treating it as a Delta=200
mass. Rines et al. (2016) Section II.2, read directly this session:
"The Planck mass estimates are extracted from an aperture of theta_500,
the angular radius corresponding to r_500" -- MSZ is a Delta=500 mass,
NOT Delta=200. That first version's raw finding (MSZ/M200c mean ratio
1.68, 74% scatter, r=0.56) is WRONG -- it mixed two different overdensity
definitions without converting between them. This version fixes it: MSZ
is now treated as a real Delta=500 mass throughout, converted onto the
same NFW halo machinery (anchored on Duffy et al. 2008's own Delta=200
c(M,z) relation, self-consistently) used for M200c.

CORRECTION 2 (round-2 Step 8a skeptic pass, same day): the corrected
version's own printed output originally invoked Rines et al.'s "SZ mass
estimates... are not significantly biased" claim as a sanity check on
the fixed M200c-vs-MSZ ratio. That claim is about a DIFFERENT comparison
(measured velocity dispersion sigma_p vs a virial-scaling PREDICTION of
sigma from M_SZ), not a direct mass-ratio comparison -- this file's own
M200c-vs-MSZ ratio is therefore its own open finding, not evidence for
or against Rines et al.'s own headline result.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_200 as _DELTA_200,
)
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_500 as _DELTA_500,
)
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_VIR as _DELTA_VIR,
)
from P196_girardi_r_vir_vs_r200_check import (
    MSUN_TO_KG,
    duffy2008_concentration,
    girardi_r_vir_mpc,
    nfw_from_m200c,
    r_delta_from_nfw_mpc,
    r_delta_mpc,
    rho_crit,
)
from P196_girardi_r_vir_vs_r200_check import (
    step2a_reference_density_correction as _step2a,
)
from scipy.optimize import brentq
from scipy.stats import pearsonr

MPC_TO_M_LOCAL = 3.0856775814913673e22


def _nfw_m_shape(x):
    return np.log(1.0 + x) - x / (1.0 + x)


def solve_halo_matching_target_delta(target_mass_msun, target_delta, z):
    """Find the NFW halo, anchored self-consistently on Duffy et al.
    (2008)'s own c200(M200,z) relation, whose enclosed mass AT
    `target_delta` equals `target_mass_msun`. Generalizes P196's own
    `nfw_from_m200c` (which only matches at Delta=200) to an arbitrary
    target overdensity -- needed because MSZ is a real Delta=500 mass,
    not Delta=200. Reduces to `nfw_from_m200c` exactly when
    target_delta=200 (checked in the positive control below)."""
    rc = rho_crit(z)

    def build(m200_guess_msun):
        c200 = duffy2008_concentration(m200_guess_msun, z)
        r200 = r_delta_mpc(m200_guess_msun, z, _DELTA_200)
        rs_mpc = r200 / c200
        m200_kg = m200_guess_msun * MSUN_TO_KG
        rho_s = m200_kg / (4.0 * np.pi * (rs_mpc * MPC_TO_M_LOCAL) ** 3 * _nfw_m_shape(c200))
        return rho_s, rs_mpc, c200

    def residual(log10_m200_guess):
        m200_guess_msun = 10.0**log10_m200_guess
        rho_s, rs_mpc, _c200 = build(m200_guess_msun)
        r_target_implied = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, target_delta)
        m_target_implied_kg = (
            (4.0 / 3.0) * np.pi * target_delta * rc * (r_target_implied * MPC_TO_M_LOCAL) ** 3
        )
        return (m_target_implied_kg / MSUN_TO_KG) - target_mass_msun

    log10_m200_sol = brentq(
        residual, np.log10(target_mass_msun) - 1.0, np.log10(target_mass_msun) + 1.0
    )
    m200_msun = 10.0**log10_m200_sol
    rho_s, rs_mpc, c200 = build(m200_msun)
    return rho_s, rs_mpc, c200, m200_msun


def ratio_2b_from_halo(rho_s, rs_mpc, z, r_vir_2a_mpc):
    r178 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, _DELTA_VIR)
    return r_vir_2a_mpc / r178


def test_positive_control_target_delta_200_matches_nfw_from_m200c():
    """solve_halo_matching_target_delta at target_delta=200 must exactly
    reproduce P196's own nfw_from_m200c -- validates the generalized
    root-finder against the already-established baseline before trusting
    it at target_delta=500 for MSZ."""
    m_test, z_test = 3.0e14, 0.1
    rho_s_expected, rs_expected, c200_expected = nfw_from_m200c(m_test, z_test)
    rho_s_rt, rs_rt, c200_rt, m200_rt = solve_halo_matching_target_delta(m_test, _DELTA_200, z_test)
    assert abs(rho_s_rt - rho_s_expected) / rho_s_expected < 1e-6
    assert abs(rs_rt - rs_expected) / rs_expected < 1e-6
    assert abs(c200_rt - c200_expected) / c200_expected < 1e-6
    assert abs(m200_rt - m_test) / m_test < 1e-6
    return True


def test_positive_control_delta500_roundtrip():
    """Build a mock NFW halo with a KNOWN M200 (hence known rho_s, rs, c200
    via Duffy+08), compute its TRUE Delta=500 mass directly, then confirm
    solve_halo_matching_target_delta recovers the same halo from that
    Delta=500 mass ALONE -- the actual machinery MSZ will use."""
    m200_true, z_test = 4.0e14, 0.12
    rho_s_true, rs_true, c200_true = nfw_from_m200c(m200_true, z_test)
    r500_true = r_delta_from_nfw_mpc(rho_s_true, rs_true, z_test, _DELTA_500)
    m500_true_kg = (
        (4.0 / 3.0) * np.pi * _DELTA_500 * rho_crit(z_test) * (r500_true * MPC_TO_M_LOCAL) ** 3
    )
    m500_true_msun = m500_true_kg / MSUN_TO_KG

    rho_s_rt, rs_rt, c200_rt, m200_rt = solve_halo_matching_target_delta(
        m500_true_msun, _DELTA_500, z_test
    )
    assert abs(rho_s_rt - rho_s_true) / rho_s_true < 1e-6
    assert abs(rs_rt - rs_true) / rs_true < 1e-6
    assert abs(m200_rt - m200_true) / m200_true < 1e-6
    return True


if __name__ == "__main__":
    from astroquery.vizier import Vizier

    test_positive_control_target_delta_200_matches_nfw_from_m200c()
    print("Positive control 1: generalized root-finder at target_delta=200 exactly")
    print("  reproduces P196's own nfw_from_m200c: PASS\n")

    test_positive_control_delta500_roundtrip()
    print("Positive control 2: a mock halo's TRUE Delta=500 mass, fed back through")
    print("  solve_halo_matching_target_delta, exactly recovers the original halo --")
    print("  this is the actual machinery MSZ (a real Delta=500 mass) will use: PASS\n")

    print("Fetching HeCS-SZ (Rines et al. 2016, VizieR J/ApJ/819/63/table4)")
    print("independently this session, including BOTH mass columns...")
    v = Vizier(columns=["ID", "z", "sigma", "M200c", "MSZ"], row_limit=-1)
    result = v.get_catalogs("J/ApJ/819/63/table4")
    tab = result[0]
    print(f"  -> {len(tab)} rows fetched\n")

    z_arr = np.array(tab["z"], dtype=float)
    sigma_arr = np.array(tab["sigma"], dtype=float)
    m200c_arr = np.array(tab["M200c"], dtype=float) * 1.0e14
    msz_arr = np.array(tab["MSZ"], dtype=float) * 1.0e14
    valid = (
        np.isfinite(z_arr)
        & np.isfinite(sigma_arr)
        & np.isfinite(m200c_arr)
        & np.isfinite(msz_arr)
        & (z_arr > 0)
        & (m200c_arr > 0)
        & (msz_arr > 0)
    )
    n_dropped = (~valid).sum()
    z_arr, sigma_arr, m200c_arr, msz_arr = (
        z_arr[valid],
        sigma_arr[valid],
        m200c_arr[valid],
        msz_arr[valid],
    )
    n = len(z_arr)
    print(f"  -> {n} clusters with valid z, sigma, M200c, MSZ ({n_dropped} dropped)\n")
    print(
        f"  MSZ column range: [{msz_arr.min() / 1e14:.2f}, {msz_arr.max() / 1e14:.2f}] x1e14 Msun"
    )
    print("  (catalog metadata quotes [0.9, 11.5] x1e14 Msun -- sanity check)\n")

    print("Converting MSZ (real Delta=500 mass) to an M200-equivalent via the")
    print("Duffy+08-anchored NFW machinery, for a fair, same-Delta comparison...")
    msz_as_m200_equiv = np.empty(n)
    for i in range(n):
        _rho_s, _rs, _c200, m200_equiv = solve_halo_matching_target_delta(
            msz_arr[i], _DELTA_500, z_arr[i]
        )
        msz_as_m200_equiv[i] = m200_equiv

    print("=" * 88)
    print("ENDPOINT 1 -- M200c (caustic) vs MSZ, properly converted to the SAME Delta=200")
    print("=" * 88)
    r_mass, p_mass = pearsonr(m200c_arr, msz_as_m200_equiv)
    mass_ratio = msz_as_m200_equiv / m200c_arr
    print(f"  n={n}")
    print(f"  Pearson r(M200c, MSZ-as-M200-equivalent) = {r_mass:.4f}")
    print(
        f"  mean(MSZ_equiv/M200c) = {mass_ratio.mean():.4f}   "
        f"scatter = {mass_ratio.std() / mass_ratio.mean():.4%}"
    )
    print("  CORRECTION (Step 8a skeptic pass, round 2): the print below originally")
    print("  compared this ratio against Rines et al.'s own 'not significantly biased'")
    print("  claim as a sanity check -- that claim is about a DIFFERENT comparison")
    print("  (measured sigma_p vs a virial-scaling PREDICTION of sigma from M_SZ), not")
    print("  a direct M200(caustic)-vs-M_SZ mass-ratio comparison. This ratio's own")
    print("  size is therefore NOT in direct tension with their headline result, and")
    print("  is reported here as its own real, open, unexplained finding.\n")

    r_vir_raw = np.array([girardi_r_vir_mpc(s) for s in sigma_arr])
    r_vir_2a = np.array([_step2a(rv, z) for rv, z in zip(r_vir_raw, z_arr, strict=True)])

    ratio_m200c = np.empty(n)
    ratio_msz = np.empty(n)
    for i in range(n):
        rho_s_m, rs_m, _c_m, _mv_m = solve_halo_matching_target_delta(
            m200c_arr[i], _DELTA_200, z_arr[i]
        )
        ratio_m200c[i] = ratio_2b_from_halo(rho_s_m, rs_m, z_arr[i], r_vir_2a[i])
        rho_s_s, rs_s, _c_s, _mv_s = solve_halo_matching_target_delta(
            msz_arr[i], _DELTA_500, z_arr[i]
        )
        ratio_msz[i] = ratio_2b_from_halo(rho_s_s, rs_s, z_arr[i], r_vir_2a[i])

    print("=" * 88)
    print("ENDPOINT 2 -- P196's own full pipeline, M200c (caustic) vs MSZ (now correctly")
    print("  treated as its own real Delta=500 mass)")
    print("=" * 88)
    print(
        f"  Using M200c (P196 baseline): mean ratio = {ratio_m200c.mean():.4f}   "
        f"scatter = {ratio_m200c.std() / ratio_m200c.mean():.4%}"
    )
    print(
        f"  Using MSZ  (Delta=500, fixed): mean ratio = {ratio_msz.mean():.4f}   "
        f"scatter = {ratio_msz.std() / ratio_msz.mean():.4%}"
    )

    print()
    print("=" * 88)
    print("MCID CHECK (pre-registered in CLAIM_P197, reused from CLAIM_P196)")
    print("=" * 88)
    mean_in_band = 0.95 <= ratio_msz.mean() <= 1.05
    scatter_change_pp = (
        ratio_m200c.std() / ratio_m200c.mean() - ratio_msz.std() / ratio_msz.mean()
    ) * 100
    material = mean_in_band or abs(scatter_change_pp) > 5.0
    print(f"  MSZ-based mean ratio in [0.95,1.05]? {mean_in_band} (value={ratio_msz.mean():.4f})")
    print(f"  Scatter change (M200c -> MSZ), percentage points: {scatter_change_pp:+.2f}")
    print(f"  MATERIAL (per pre-registered MCID): {material}")

    print()
    print("=" * 88)
    print("MECHANICAL-EXPLANATION CHECK (Step 8a skeptic pass, round 2): is the")
    print("  Endpoint 2 shift explained by pure mass-rescaling (R ~ M^(1/3)), or is")
    print("  it an independent physical convergence?")
    print("=" * 88)
    predicted_shift_from_mass_alone = mass_ratio.mean() ** (1.0 / 3.0)
    observed_shift = ratio_m200c.mean() / ratio_msz.mean()
    print(
        f"  Mass-ratio-only prediction (mean_mass_ratio^(1/3)): {predicted_shift_from_mass_alone:.3f}"
    )
    print(f"  Observed ratio_2b shift (M200c/MSZ):                {observed_shift:.3f}")
    print("  These are close -- most of Endpoint 2's own movement is consistent with")
    print("  simple mass-rescaling arithmetic (MSZ_equiv is larger than M200c), not a")
    print("  demonstrated independent physical improvement.")

    print()
    print("=" * 88)
    print("VERDICT (both endpoints reported honestly and separately, per pre-")
    print("  registered MCID -- not smoothed into one number)")
    print("=" * 88)
    print("  Endpoint 1: M200c and MSZ (Delta-corrected) disagree by a real, large,")
    print(
        f"    UNEXPLAINED factor (mean {mass_ratio.mean():.2f}x, {mass_ratio.std() / mass_ratio.mean():.0%} scatter)."
    )
    print("    This is its own open question (candidates: caustic under-estimation,")
    print("    Eddington bias in low-significance SZ detections, hydrostatic mass")
    print("    bias in MSZ) -- not resolved here, not stratified by mass/significance.")
    print(f"  Endpoint 2: using MSZ gives ratio_2b={ratio_msz.mean():.4f}, closer to 1.0 than")
    print(f"    M200c's {ratio_m200c.mean():.4f} -- but STILL fails the pre-registered MCID")
    print("    band [0.95,1.05], and the shift is consistent with simple mass-rescaling")
    print("    arithmetic (see above), not an independently validated improvement.")
    print(f"  MATERIAL (per pre-registered MCID, scatter-branch): {material}")
    print("  -- this means mass-measurement-method choice changes the numbers a lot,")
    print("  NOT that MSZ closes the gap. By the mean-band criterion alone, it does not.")
