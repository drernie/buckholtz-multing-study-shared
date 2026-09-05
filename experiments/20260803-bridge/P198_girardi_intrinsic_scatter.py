"""P198 -- Girardi et al. (1998)'s own internal R_c inconsistency, propagated
through their own formula's derivation, and through P196's own pipeline.

Girardi et al.'s headline R_vir=0.002*sigma coefficient (Eq. 11) is derived
(Eq. 9+10) using a core radius R_c=0.17 h^-1 Mpc, attributed to Girardi et
al. (1995, "G95") -- an earlier paper's value, from a cruder cluster-
centering method. Later in the SAME paper (Sec 4.3), applying their own
improved centering method to their own 170-cluster sample, they find a
substantially SMALLER core radius: R_c=0.05 (+0.01/-0.01) h^-1 Mpc (90% CL)
-- about 1/3 of the G95 value their own headline formula actually used.

This file substitutes Girardi's own improved R_c into the SAME Eq.9+10
self-consistency solve already built and verified in P196 (Positive
Control 1), to quantify the resulting sensitivity of the R_vir/sigma
coefficient -- an honest sensitivity test of Eq.11's own R_c-dependence,
not a claim that this substitution is the "correct" procedure (Eq.10's own
R_PV(A) formula was fit by G95 using G95's own R_c convention).

See CLAIM_P198_girardi_intrinsic_scatter.md for the full protocol,
including this caveat stated explicitly before running.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from P196_girardi_r_vir_vs_r200_check import (
    DELTA_VIR,
    G_SI,
    H0_KM_S_MPC,
    KM_TO_M,
    MPC_TO_M,
    RHO_CRIT_0,
    nfw_from_m200c,
    r_delta_from_nfw_mpc,
)
from P196_girardi_r_vir_vs_r200_check import (
    girardi_r_vir_mpc as _girardi_r_vir_mpc_published,
)
from P196_girardi_r_vir_vs_r200_check import (
    step2a_reference_density_correction as _step2a,
)
from scipy.optimize import brentq
from scipy.stats import pearsonr

# [VERIFIED-arXiv:astro-ph/9804187] Sec 4.3, quoted directly this session
# (already fetched for P196): "we find typically smaller core radii Rc
# (cf. our median Rc=0.05_{-0.01}^{+0.01} h^-1 Mpc with Rc=0.17 h^-1 Mpc
# of G95)." The published Eq.11 coefficient (0.002) used G95's Rc=0.17.
RC_G95_PUBLISHED_H_MPC = 0.17
RC_GIRARDI_OWN_MEDIAN_H_MPC = 0.05
RC_GIRARDI_OWN_90CL_LO_H_MPC = 0.04
RC_GIRARDI_OWN_90CL_HI_H_MPC = 0.06


def implied_rvir_over_sigma_coeff(r_c_h_mpc, sigma_test_kms=1000.0):
    """P196's own self-consistency solve (Eq.5 virial mass + spherical-
    collapse density criterion + Eq.10 R_PV(A), evaluated self-consistently
    at A=R_vir), reused verbatim, with R_c as the only varied input."""
    h_local = H0_KM_S_MPC / 100.0
    r_c_m = r_c_h_mpc / h_local * MPC_TO_M
    sigma_test_ms = sigma_test_kms * KM_TO_M

    def r_pv_of_a(a_m):
        x = a_m / r_c_m
        return a_m * 1.193 * (1.0 + 0.032 * x) / (1.0 + 0.107 * x)

    def residual(r_vir_m):
        r_pv = r_pv_of_a(r_vir_m)
        m_vir_from_virial = (3.0 * np.pi / 2.0) * sigma_test_ms**2 * r_pv / G_SI
        m_vir_from_density = (4.0 * np.pi / 3.0) * DELTA_VIR * RHO_CRIT_0 * r_vir_m**3
        return m_vir_from_virial - m_vir_from_density

    r_vir_m = brentq(residual, 1e17, 1e25)
    r_vir_h_mpc = (r_vir_m / MPC_TO_M) * h_local
    return r_vir_h_mpc / sigma_test_kms


def girardi_r_vir_mpc_with_coeff(sigma_kms, coeff):
    h_local = H0_KM_S_MPC / 100.0
    return coeff * sigma_kms / h_local


def ratio_2b_for_coeff(sigma_kms, coeff, m200c_msun, z):
    r_vir_raw = girardi_r_vir_mpc_with_coeff(sigma_kms, coeff)
    r_vir_2a = _step2a(r_vir_raw, z)
    rho_s, rs_mpc, _c200 = nfw_from_m200c(m200c_msun, z)
    r178 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, DELTA_VIR)
    return r_vir_2a / r178


def test_positive_control_published_rc_reproduces_0002():
    """At the PUBLISHED R_c=0.17 h^-1 Mpc, this file's own (independently
    re-imported) solver must still reproduce Eq.11's own 0.002 coefficient
    -- re-confirms P196's own Positive Control 1 before trusting the same
    machinery at the substituted R_c=0.05."""
    coeff = implied_rvir_over_sigma_coeff(RC_G95_PUBLISHED_H_MPC)
    rel_err = abs(coeff - 0.002) / 0.002
    assert rel_err < 0.05, f"published-Rc coefficient off by {rel_err:.1%}: {coeff:.5f}"
    return coeff


if __name__ == "__main__":
    from astroquery.vizier import Vizier

    coeff_published = test_positive_control_published_rc_reproduces_0002()
    print("Positive control: at G95's published Rc=0.17 h^-1 Mpc, this file's own")
    print(f"  solver reproduces Eq.11's 0.002 coefficient: implied={coeff_published:.5f}: PASS\n")

    print("=" * 88)
    print("ENDPOINT 1 -- implied R_vir/sigma coefficient: published Rc vs Girardi's own")
    print("  improved Rc (Sec 4.3, their own centering method, same paper)")
    print("=" * 88)
    coeff_median = implied_rvir_over_sigma_coeff(RC_GIRARDI_OWN_MEDIAN_H_MPC)
    coeff_lo = implied_rvir_over_sigma_coeff(RC_GIRARDI_OWN_90CL_LO_H_MPC)
    coeff_hi = implied_rvir_over_sigma_coeff(RC_GIRARDI_OWN_90CL_HI_H_MPC)
    print(f"  Published (G95 Rc=0.17):        coeff = {coeff_published:.5f}  (Eq.11's own 0.002)")
    print(f"  Girardi's own Rc=0.05 (median):  coeff = {coeff_median:.5f}")
    print(f"  Girardi's own Rc=0.04 (90% lo):  coeff = {coeff_lo:.5f}")
    print(f"  Girardi's own Rc=0.06 (90% hi):  coeff = {coeff_hi:.5f}")
    sensitivity_ratio = coeff_median / coeff_published
    print(
        f"  Sensitivity ratio (own-Rc median / this-solver's-own-published): {sensitivity_ratio:.4f}"
    )
    # Apply the SOLVER-DERIVED sensitivity ratio multiplicatively to the
    # LITERAL published 0.002 (not to this solver's own ~0.00197
    # re-derivation, which is itself only accurate to <5% per the positive
    # control above) -- keeps the "published" endpoint numerically
    # identical to P196's own established baseline (coeff=0.002 exactly),
    # so ENDPOINT 2 below is a clean, apples-to-apples comparison against
    # P196's own already-reported 1.4665/11.15% numbers.
    coeff_published_literal = 0.002
    coeff_own_rc_scaled = coeff_published_literal * sensitivity_ratio
    print(
        f"  Applied to the literal published 0.002: own-Rc-equivalent = {coeff_own_rc_scaled:.5f}\n"
    )

    print("Fetching HeCS-SZ (Rines et al. 2016, VizieR J/ApJ/819/63/table4)")
    print("independently this session (same catalog as P196/P197, fresh fetch)...")
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

    ratio_published = np.array(
        [
            ratio_2b_for_coeff(s, coeff_published_literal, m, z)
            for s, m, z in zip(sigma_arr, m200c_arr, z_arr, strict=True)
        ]
    )
    ratio_own_rc = np.array(
        [
            ratio_2b_for_coeff(s, coeff_own_rc_scaled, m, z)
            for s, m, z in zip(sigma_arr, m200c_arr, z_arr, strict=True)
        ]
    )

    r_corr_check, _ = pearsonr(
        [_girardi_r_vir_mpc_published(s) for s in sigma_arr],
        [girardi_r_vir_mpc_with_coeff(s, coeff_published_literal) for s in sigma_arr],
    )
    assert r_corr_check > 0.999, "published-coeff reproduction of P196's own R_vir formula diverged"
    ratio_published_direct = np.array(
        [
            ratio_2b_for_coeff(s, 0.002, m, z)
            for s, m, z in zip(sigma_arr, m200c_arr, z_arr, strict=True)
        ]
    )
    rel_err_vs_p196 = abs(ratio_published_direct.mean() - 1.4665) / 1.4665
    assert rel_err_vs_p196 < 0.01, (
        f"published-literal-coeff baseline ({ratio_published_direct.mean():.4f}) "
        f"does not match P196's own reported 1.4665 to <1%: off by {rel_err_vs_p196:.2%}"
    )
    print(
        f"  Cross-check: literal-0.002 baseline reproduces P196's own reported 1.4665 "
        f"to {rel_err_vs_p196:.3%}: PASS\n"
    )

    print("=" * 88)
    print("ENDPOINT 2 -- P196's own full pipeline, published Eq.11 vs Girardi's own")
    print("  improved-Rc-implied coefficient")
    print("=" * 88)
    print(
        f"  Published coeff (0.002):        mean ratio = {ratio_published.mean():.4f}   "
        f"scatter = {ratio_published.std() / ratio_published.mean():.4%}"
    )
    print(
        f"  Own-Rc-implied coeff ({coeff_own_rc_scaled:.5f}): mean ratio = {ratio_own_rc.mean():.4f}   "
        f"scatter = {ratio_own_rc.std() / ratio_own_rc.mean():.4%}"
    )

    print()
    print("=" * 88)
    print("MCID CHECK (pre-registered in CLAIM_P198, reused from CLAIM_P196)")
    print("=" * 88)
    mean_in_band = 0.95 <= ratio_own_rc.mean() <= 1.05
    scatter_change_pp = (
        ratio_published.std() / ratio_published.mean() - ratio_own_rc.std() / ratio_own_rc.mean()
    ) * 100
    material = mean_in_band or abs(scatter_change_pp) > 5.0
    print(
        f"  Own-Rc-based mean ratio in [0.95,1.05]? {mean_in_band} (value={ratio_own_rc.mean():.4f})"
    )
    print(f"  Scatter change (published -> own-Rc), percentage points: {scatter_change_pp:+.2f}")
    print(f"  MATERIAL (per pre-registered MCID): {material}")

    print()
    print("=" * 88)
    print("VERDICT")
    print("=" * 88)
    if material:
        print("Girardi's own internal Rc inconsistency IS material -- their own improved")
        print("  centering method, propagated through their own formula's derivation,")
        print("  meaningfully changes the comparison to P196's TJB-style construction.")
    else:
        print("Girardi's own internal Rc inconsistency is NOT material by the pre-")
        print("  registered MCID -- propagating their own improved Rc through their own")
        print("  formula's derivation does not meaningfully change the comparison.")
