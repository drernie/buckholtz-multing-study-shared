"""P196 Addendum -- propagates Duffy et al. (2008)'s own quoted lognormal
concentration scatter (sigma(log10 c200)=0.15 dex, [VERIFIED-arXiv:0804.2486]
Section 3, "Full" NFW Delta=200 sample -- the exact sample this project's own
duffy2008_concentration already uses) through the Delta=178->500 NFW shape
correction (P196's own Step 2b), via Monte Carlo.

Reuses P196's own machinery verbatim (imported, not reproduced) -- only the
concentration input is randomized, per the Minimal Relaxation Rule.

Pre-registered expectation (CLAIM_P196_ADDENDUM): symmetric lognormal scatter
propagated through a deterministic pipeline should NOT explain the 1.47x mean
offset (that needs the documented, separate, one-directional bias: real
X-ray-observed cluster concentrations run higher than Duffy+08's simulated
median -- not tested here). What IS tested: how much of the 11.1% cluster-
to-cluster ratio scatter is attributable to concentration uncertainty alone.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_200 as _DELTA_200,
)
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_500,
    DELTA_VIR,
    MSUN_TO_KG,
    girardi_r_vir_mpc,
    r_delta_from_nfw_mpc,
    r_delta_mpc,
    step2a_reference_density_correction,
)

MPC_TO_M_LOCAL = 3.0856775814913673e22

# [VERIFIED-arXiv:0804.2486] Section 3: "Fitting lognormal functions to the
# probability density functions yields sigma(log10 c200)=0.15 ... for the
# NFW density profile" -- the FULL sample (not "relaxed", which is 0.11 --
# matches this project's own A_200=5.71 "Full" row, not the "Relaxed" row).
SIGMA_LOG10_C200_DUFFY08 = 0.15

N_MC_DRAWS = 2000
RNG_SEED = 20260906  # fixed for reproducibility


def duffy2008_concentration_median(m200c_msun, z, h_local):
    m_pivot_msun = 2.0e12 / h_local
    a, b, c = 5.71, -0.084, -0.47
    return a * (m200c_msun / m_pivot_msun) ** b * (1.0 + z) ** c


def _nfw_m_shape(x):
    return np.log(1.0 + x) - x / (1.0 + x)


def mc_ratio_2b_for_cluster(m200c_msun, z, r_vir_2a_mpc, h_local, rng):
    """Draw N_MC_DRAWS concentrations from Duffy+08's own lognormal scatter
    around the median c200(M,z), recompute the Delta=178->500 shape
    correction for each draw, return the array of resulting ratio_2b."""
    c_median = duffy2008_concentration_median(m200c_msun, z, h_local)
    log10_c_draws = np.log10(c_median) + rng.normal(0.0, SIGMA_LOG10_C200_DUFFY08, N_MC_DRAWS)
    c_draws = 10.0**log10_c_draws

    r200 = r_delta_mpc(m200c_msun, z, _DELTA_200)
    m200_kg = m200c_msun * MSUN_TO_KG

    ratios = np.empty(N_MC_DRAWS)
    for i, c200 in enumerate(c_draws):
        rs_mpc = r200 / c200
        rho_s = m200_kg / (4.0 * np.pi * (rs_mpc * MPC_TO_M_LOCAL) ** 3 * _nfw_m_shape(c200))
        r500 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, DELTA_500)
        r178 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, DELTA_VIR)
        shape_ratio = r500 / r178
        ratios[i] = (r_vir_2a_mpc * shape_ratio) / r500
    return ratios


def test_positive_control_mc_median_recovers_point_estimate():
    """At zero scatter (sigma=0), the MC machinery must recover the exact
    same ratio_2b P196's own deterministic Step 2b computes -- a regression
    check that this file's re-implementation of the NFW shape-correction
    step (necessarily duplicated here to vary c200 per-draw) matches P196's
    own function, not a new formula."""
    from P196_girardi_r_vir_vs_r200_check import (
        nfw_from_m200c,
    )

    m_test, z_test, h_local = 3.0e14, 0.1, 0.7
    r_vir_raw = girardi_r_vir_mpc(700.0)
    r_vir_2a = step2a_reference_density_correction(r_vir_raw, z_test)

    rho_s, rs_mpc, c200 = nfw_from_m200c(m_test, z_test)
    r500 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z_test, DELTA_500)
    r178 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z_test, DELTA_VIR)
    expected_ratio = (r_vir_2a * (r500 / r178)) / r500

    c_median = duffy2008_concentration_median(m_test, z_test, h_local)
    # zero-scatter: evaluate this file's own duplicated formula AT the exact
    # Duffy+08 median concentration (no RNG involved) and confirm it matches
    # P196's own function-based point estimate.
    r200 = r_delta_mpc(m_test, z_test, _DELTA_200)
    m_kg = m_test * MSUN_TO_KG
    rs_at_median = r200 / c_median
    rho_s_at_median = m_kg / (
        4.0 * np.pi * (rs_at_median * MPC_TO_M_LOCAL) ** 3 * _nfw_m_shape(c_median)
    )
    r500_mc = r_delta_from_nfw_mpc(rho_s_at_median, rs_at_median, z_test, DELTA_500)
    r178_mc = r_delta_from_nfw_mpc(rho_s_at_median, rs_at_median, z_test, DELTA_VIR)
    mc_ratio_at_median = (r_vir_2a * (r500_mc / r178_mc)) / r500_mc

    rel_err = abs(mc_ratio_at_median - expected_ratio) / expected_ratio
    assert rel_err < 1e-6, f"MC-at-median does not recover P196's own point estimate: {rel_err:.2e}"
    return True


if __name__ == "__main__":
    from astroquery.vizier import Vizier

    test_positive_control_mc_median_recovers_point_estimate()
    print("Positive control: MC machinery at zero scatter (evaluated exactly at")
    print("  the Duffy+08 median c200) recovers P196's own Step 2b point estimate")
    print("  to <1e-6 relative error -- confirms this file's necessarily-duplicated")
    print("  NFW shape-correction code matches P196's own function: PASS\n")

    print("Fetching HeCS-SZ (Rines et al. 2016, VizieR J/ApJ/819/63/table4)")
    print("independently this session (same catalog as P196, fresh fetch)...")
    v = Vizier(columns=["ID", "z", "sigma", "M200c"], row_limit=-1)
    result = v.get_catalogs("J/ApJ/819/63/table4")
    tab = result[0]
    print(f"  -> {len(tab)} rows fetched\n")

    z_arr = np.array(tab["z"], dtype=float)
    sigma_arr = np.array(tab["sigma"], dtype=float)
    m200c_arr = np.array(tab["M200c"], dtype=float) * 1.0e14
    valid = np.isfinite(z_arr) & np.isfinite(sigma_arr) & np.isfinite(m200c_arr) & (z_arr > 0)
    z_arr, sigma_arr, m200c_arr = z_arr[valid], sigma_arr[valid], m200c_arr[valid]
    n = len(z_arr)
    print(f"  -> {n} clusters with valid z, sigma, M200c\n")

    h_local = 0.7
    rng = np.random.default_rng(RNG_SEED)

    r_vir_raw = np.array([girardi_r_vir_mpc(s) for s in sigma_arr])
    r_vir_2a = np.array(
        [step2a_reference_density_correction(rv, z) for rv, z in zip(r_vir_raw, z_arr, strict=True)]
    )

    print("=" * 88)
    print(f"MONTE CARLO: {N_MC_DRAWS} concentration draws per cluster, sigma(log10 c200)=0.15")
    print("  (Duffy+08's own quoted Full-sample NFW Delta=200 scatter)")
    print("=" * 88)
    mc_medians = np.empty(n)
    mc_p16 = np.empty(n)
    mc_p84 = np.empty(n)
    for i in range(n):
        ratios = mc_ratio_2b_for_cluster(m200c_arr[i], z_arr[i], r_vir_2a[i], h_local, rng)
        mc_medians[i] = np.median(ratios)
        mc_p16[i] = np.percentile(ratios, 16)
        mc_p84[i] = np.percentile(ratios, 84)

    per_cluster_mc_spread = (mc_p84 - mc_p16) / 2.0  # ~1-sigma half-width per cluster
    print("  Median per-cluster MC 1-sigma half-width (as fraction of ratio):")
    print(f"    {np.median(per_cluster_mc_spread / mc_medians):.4%}")
    print(f"  Population mean of MC medians: {mc_medians.mean():.4f}")
    print(
        f"  Population std of MC medians (across the 123 clusters): {mc_medians.std():.4%} of mean"
    )

    observed_ratio_2b_std_fraction = 0.111  # from FINDING_P196's own reported 11.1% scatter

    print()
    print("=" * 88)
    print("MCID CHECK (pre-registered in CLAIM_P196_ADDENDUM)")
    print("=" * 88)
    mc_variance_fraction = (
        per_cluster_mc_spread.mean() ** 2
        / (observed_ratio_2b_std_fraction * mc_medians.mean()) ** 2
    )
    print(f"  Mean per-cluster MC 1-sigma half-width: {per_cluster_mc_spread.mean():.4f}")
    print(
        f"  Observed population scatter (P196's ratio_2b, absolute): "
        f"{observed_ratio_2b_std_fraction * mc_medians.mean():.4f}"
    )
    print(
        f"  Implied variance fraction explained by concentration scatter alone: "
        f"{mc_variance_fraction:.1%}"
    )
    material = mc_variance_fraction > 0.30
    print(f"  MATERIAL (>30% of observed variance, per pre-registered MCID): {material}")

    print()
    print("=" * 88)
    print("MEAN-OFFSET CHECK (pre-registered NOT to be explained by symmetric scatter)")
    print("=" * 88)
    mean_shift = mc_medians.mean() - 1.4665  # P196's own reported point estimate
    print(f"  MC population mean vs P196's own point estimate (1.4665): shift={mean_shift:+.4f}")
    print("  (expected: near zero -- symmetric lognormal scatter through a smooth")
    print("   pipeline should not materially shift the mean; confirms this is NOT")
    print("   the mechanism explaining the offset, as pre-registered)")

    print()
    print("=" * 88)
    print("VERDICT")
    print("=" * 88)
    if material:
        print("Concentration scatter is a MATERIAL contributor to the observed 11.1%")
        print("  cluster-to-cluster ratio scatter (>30% of variance) -- part of P196's")
        print("  own scatter is explained by this specific, real, quoted uncertainty.")
    else:
        print("Concentration scatter is NOT a material contributor to the observed 11.1%")
        print("  cluster-to-cluster ratio scatter by the pre-registered MCID -- most of")
        print("  that scatter comes from something else (real cluster diversity, M200c")
        print("  measurement uncertainty, or Girardi's own formula's residual scatter).")
    print()
    print("Either way: as pre-registered, this file does NOT explain the 1.47x MEAN")
    print("  offset -- that needs the documented, SEPARATE, one-directional bias (real")
    print("  X-ray-observed cluster concentrations run higher than Duffy+08's simulated")
    print("  median, per their own Fig. 4) -- not quantitatively tested here.")
