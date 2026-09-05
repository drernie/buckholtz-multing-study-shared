"""P196 Addendum 2 -- substitutes real, X-ray-measured concentration-mass
relations (Buote et al. 2007, Schmidt & Allen 2007) for Duffy et al.
(2008)'s simulated median, in P196's own Delta=178->500 NFW shape-correction
pipeline.

Both real relations are defined at THEIR OWN virial overdensity convention,
different from Delta=200 (Duffy+08's own convention, and HeCS-SZ's own
M200c column):
  - Buote et al. (2007), astro-ph/0610135: Bryan & Norman (1998) Delta_vir(z)
  - Schmidt & Allen (2007), astro-ph/0610038: Lahav et al. (1991)
    Delta_c(z)=178*Om(z)^0.45

For each cluster, solves (via brentq) for the (M_vir, c_vir) pair such that
(a) c_vir is given by that paper's own fitted c(M_vir,z), and (b) the
resulting NFW halo's Delta=200-enclosed mass equals the REAL M200c from the
catalog -- avoids the M_vir~=M200c approximation.

See CLAIM_P196_ADDENDUM2_real_xray_concentration.md for the full protocol.

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
    OM,
    duffy2008_concentration,
    efun,
    girardi_r_vir_mpc,
    r_delta_from_nfw_mpc,
    r_delta_mpc,
    rho_crit,
    step2a_reference_density_correction,
)
from scipy.optimize import brentq

MPC_TO_M_LOCAL = 3.0856775814913673e22

# [VERIFIED-arXiv:astro-ph/0610135] Buote et al. (2007), full-sample BCES fit
# (39 real X-ray systems): c0=(1+z)c = c14*(M/M14)^alpha, M14=1e14 h^-1 Msun,
# at their own Bryan & Norman (1998) virial Delta(z).
BUOTE_ALPHA = -0.172
BUOTE_C14 = 9.0
BUOTE_M14_H_MSUN = 1.0e14

# [VERIFIED-arXiv:astro-ph/0610038] Schmidt & Allen (2007), free (c0,a,b) fit
# (34 real Chandra clusters): c_vir(z) = c0/(1+z)^b * (Mvir/Mpivot)^a,
# Mpivot=8e14 h^-1 Msun, at their own Lahav et al. (1991) Delta_c(z).
SA_C0 = 7.55
SA_A = -0.45
SA_B = 0.71
SA_MPIVOT_H_MSUN = 8.0e14


def omega_m_z(z):
    return OM * (1.0 + z) ** 3 / efun(z) ** 2


def delta_bryan_norman(z):
    """[VERIFIED-arXiv:astro-ph/0610135]: Buote et al.'s own quoted
    Delta=101.1 at z=0 for this exact formula -- independently re-derived
    below and checked in test_positive_control_delta_bryan_norman_z0."""
    x = omega_m_z(z) - 1.0
    return 18.0 * np.pi**2 + 82.0 * x - 39.0 * x**2


def delta_lahav(z):
    """[VERIFIED-arXiv:astro-ph/0610038]: quoted directly, Lahav et al. 1991."""
    return 178.0 * omega_m_z(z) ** 0.45


def buote_concentration(m_vir_msun, z, h_local=0.7):
    m14_msun = BUOTE_M14_H_MSUN / h_local
    c0 = BUOTE_C14 * (m_vir_msun / m14_msun) ** BUOTE_ALPHA
    return c0 / (1.0 + z)


def schmidt_allen_concentration(m_vir_msun, z, h_local=0.7):
    mpivot_msun = SA_MPIVOT_H_MSUN / h_local
    return SA_C0 / (1.0 + z) ** SA_B * (m_vir_msun / mpivot_msun) ** SA_A


def _nfw_m_shape(x):
    return np.log(1.0 + x) - x / (1.0 + x)


def solve_halo_matching_m200c(m200c_msun, z, concentration_func, delta_obs_func):
    """Find (M_vir, c_vir) such that c_vir=concentration_func(M_vir,z) AND
    the resulting NFW halo's Delta=200-enclosed mass equals m200c_msun.
    Returns (rho_s [kg/m^3], rs_mpc, c_vir, m_vir_msun)."""
    delta_obs = delta_obs_func(z)
    rc = rho_crit(z)

    def build(m_vir_msun):
        c_vir = concentration_func(m_vir_msun, z)
        r_vir = r_delta_mpc(m_vir_msun, z, delta_obs)
        rs_mpc = r_vir / c_vir
        m_vir_kg = m_vir_msun * MSUN_TO_KG
        rho_s = m_vir_kg / (4.0 * np.pi * (rs_mpc * MPC_TO_M_LOCAL) ** 3 * _nfw_m_shape(c_vir))
        return rho_s, rs_mpc, c_vir

    def residual(log10_m_vir):
        m_vir_msun = 10.0**log10_m_vir
        rho_s, rs_mpc, _c_vir = build(m_vir_msun)
        r200_implied = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, _DELTA_200)
        m200_implied_kg = (
            (4.0 / 3.0) * np.pi * _DELTA_200 * rc * (r200_implied * MPC_TO_M_LOCAL) ** 3
        )
        return (m200_implied_kg / MSUN_TO_KG) - m200c_msun

    log10_m_vir_sol = brentq(residual, np.log10(m200c_msun) - 1.0, np.log10(m200c_msun) + 1.0)
    m_vir_msun = 10.0**log10_m_vir_sol
    rho_s, rs_mpc, c_vir = build(m_vir_msun)
    return rho_s, rs_mpc, c_vir, m_vir_msun


def ratio_2b_from_halo(rho_s, rs_mpc, z, r_vir_2a_mpc):
    r500 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, DELTA_500)
    r178 = r_delta_from_nfw_mpc(rho_s, rs_mpc, z, DELTA_VIR)
    shape_ratio = r500 / r178
    return (r_vir_2a_mpc * shape_ratio) / r500


def test_positive_control_delta_bryan_norman_z0():
    """Buote et al.'s own quoted conversion reference: Delta_vir(z=0)=101.1
    for this cosmology -- independently re-derived here, not copied."""
    delta_0 = delta_bryan_norman(0.0)
    rel_err = abs(delta_0 - 101.1) / 101.1
    assert rel_err < 0.01, f"Bryan-Norman Delta(0)={delta_0:.2f}, expected ~101.1"
    return True


def test_positive_control_duffy_roundtrip_is_identity():
    """Round-tripping Duffy et al. (2008)'s OWN relation through this file's
    NEW root-finding machinery (at Delta=200, where Duffy's own c is already
    defined) must reproduce P196's own nfw_from_m200c results exactly --
    validates the new machinery against a known-correct baseline before
    trusting it on Buote/Schmidt&Allen's different-Delta relations."""
    from P196_girardi_r_vir_vs_r200_check import nfw_from_m200c

    m_test, z_test = 3.0e14, 0.1
    rho_s_expected, rs_expected, _c200_expected = nfw_from_m200c(m_test, z_test)

    rho_s_rt, rs_rt, _c_rt, m_vir_rt = solve_halo_matching_m200c(
        m_test, z_test, duffy2008_concentration, lambda z: _DELTA_200
    )

    rel_err_rho = abs(rho_s_rt - rho_s_expected) / rho_s_expected
    rel_err_rs = abs(rs_rt - rs_expected) / rs_expected
    rel_err_m = abs(m_vir_rt - m_test) / m_test
    assert rel_err_rho < 1e-4, f"rho_s round-trip off by {rel_err_rho:.2e}"
    assert rel_err_rs < 1e-4, f"rs round-trip off by {rel_err_rs:.2e}"
    assert rel_err_m < 1e-4, f"m_vir round-trip off by {rel_err_m:.2e}"
    return True


def test_positive_control_nontrivial_delta_roundtrip():
    """Step 8a skeptic pass (2026-09-06) correctly found that
    test_positive_control_duffy_roundtrip_is_identity only exercises the
    Delta=200 case, where the root-find is trivial (residual=0 at the first
    guess) -- it never actually tests solve_halo_matching_m200c's brentq
    search or its delta_obs_func threading at a Delta DIFFERENT from 200,
    which is exactly the machinery Buote/Schmidt&Allen's own Delta(z)!=200
    conventions rely on. This closes that real gap: build a mock halo at a
    genuinely non-trivial Delta (150, neither 178, 200 nor 500), with a
    KNOWN, fixed (not mass-dependent) concentration, compute its TRUE M200
    from first principles (independent of solve_halo_matching_m200c), then
    feed that M200 back in and confirm the halo is recovered exactly."""
    c_mock = 5.0
    delta_mock = 150.0
    m_vir_true_msun = 5.0e14
    z_test = 0.15

    def mock_concentration(_m_vir_msun, _z):
        return c_mock

    r_vir_true = r_delta_mpc(m_vir_true_msun, z_test, delta_mock)
    rs_true_mpc = r_vir_true / c_mock
    m_vir_true_kg = m_vir_true_msun * MSUN_TO_KG
    rho_s_true = m_vir_true_kg / (
        4.0 * np.pi * (rs_true_mpc * MPC_TO_M_LOCAL) ** 3 * _nfw_m_shape(c_mock)
    )
    r200_true = r_delta_from_nfw_mpc(rho_s_true, rs_true_mpc, z_test, _DELTA_200)
    m200_true_kg = (
        (4.0 / 3.0) * np.pi * _DELTA_200 * rho_crit(z_test) * (r200_true * MPC_TO_M_LOCAL) ** 3
    )
    m200_true_msun = m200_true_kg / MSUN_TO_KG

    rho_s_rt, rs_rt, c_rt, m_vir_rt = solve_halo_matching_m200c(
        m200_true_msun, z_test, mock_concentration, lambda z: delta_mock
    )

    rel_err_rho = abs(rho_s_rt - rho_s_true) / rho_s_true
    rel_err_rs = abs(rs_rt - rs_true_mpc) / rs_true_mpc
    rel_err_m = abs(m_vir_rt - m_vir_true_msun) / m_vir_true_msun
    rel_err_c = abs(c_rt - c_mock) / c_mock
    assert rel_err_rho < 1e-6, f"rho_s not recovered: {rel_err_rho:.2e}"
    assert rel_err_rs < 1e-6, f"rs not recovered: {rel_err_rs:.2e}"
    assert rel_err_m < 1e-6, f"m_vir not recovered: {rel_err_m:.2e}"
    assert rel_err_c < 1e-6, f"c_vir not recovered: {rel_err_c:.2e}"
    return True


if __name__ == "__main__":
    from astroquery.vizier import Vizier

    test_positive_control_delta_bryan_norman_z0()
    print("Positive control 1: Bryan & Norman (1998) Delta_vir(z=0)=101.1")
    print("  independently re-derived, matches Buote et al.'s own quoted value: PASS\n")

    test_positive_control_duffy_roundtrip_is_identity()
    print("Positive control 2: round-tripping Duffy et al. (2008)'s own relation")
    print("  through this file's new root-finding machinery (at Delta=200, an")
    print("  identity case) exactly reproduces P196's own nfw_from_m200c: PASS\n")

    test_positive_control_nontrivial_delta_roundtrip()
    print("Positive control 3 (added after Step 8a skeptic pass, 2026-09-06):")
    print("  a mock halo built at a genuinely non-trivial Delta=150 (!=178,200,500)")
    print("  with known (M_vir,c_vir) is exactly recovered by solve_halo_matching_m200c")
    print("  from its own true M200 alone -- exercises the brentq root-find and the")
    print("  delta_obs_func!=200 branch Buote/Schmidt&Allen actually rely on, which")
    print("  positive control 2 alone (trivial at Delta=200) could not test: PASS\n")

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

    r_vir_raw = np.array([girardi_r_vir_mpc(s) for s in sigma_arr])
    r_vir_2a = np.array(
        [step2a_reference_density_correction(rv, z) for rv, z in zip(r_vir_raw, z_arr, strict=True)]
    )

    sources = {
        "Duffy+08 (P196 baseline)": (duffy2008_concentration, lambda z: _DELTA_200),
        "Buote+07 (real X-ray)": (buote_concentration, delta_bryan_norman),
        "Schmidt&Allen+07 (real X-ray)": (schmidt_allen_concentration, delta_lahav),
    }

    results = {}
    for label, (cfunc, dfunc) in sources.items():
        ratios = np.empty(n)
        c_used = np.empty(n)
        for i in range(n):
            rho_s, rs_mpc, c_vir, _m_vir = solve_halo_matching_m200c(
                m200c_arr[i], z_arr[i], cfunc, dfunc
            )
            ratios[i] = ratio_2b_from_halo(rho_s, rs_mpc, z_arr[i], r_vir_2a[i])
            c_used[i] = c_vir
        results[label] = (ratios, c_used)
        print("=" * 88)
        print(f"SOURCE: {label}")
        print("=" * 88)
        print(f"  mean ratio = {ratios.mean():.4f}   scatter = {ratios.std() / ratios.mean():.4%}")
        print(f"  median concentration used = {np.median(c_used):.2f}")
        in_band = 0.95 <= ratios.mean() <= 1.05
        print(f"  In pre-registered MCID band [0.95,1.05]? {in_band}\n")

    duffy_ratios, _ = results["Duffy+08 (P196 baseline)"]
    print("=" * 88)
    print("CROSS-CHECK vs P196's own reported point estimate (1.4665)")
    print("=" * 88)
    print(f"  This file's own Duffy+08 baseline mean ratio: {duffy_ratios.mean():.4f}")
    print("  (should match P196's own 1.4665 closely -- same relation, same data,")
    print("   different code path via the new root-finder, at Delta=200 an identity)")

    print()
    print("=" * 88)
    print("VERDICT")
    print("=" * 88)
    buote_ratios, buote_c = results["Buote+07 (real X-ray)"]
    sa_ratios, sa_c = results["Schmidt&Allen+07 (real X-ray)"]
    print(
        f"  Duffy+08 (simulated):        mean ratio {duffy_ratios.mean():.4f}, median c~{np.median(results['Duffy+08 (P196 baseline)'][1]):.2f}"
    )
    print(
        f"  Buote+07 (real X-ray):       mean ratio {buote_ratios.mean():.4f}, median c~{np.median(buote_c):.2f}"
    )
    print(
        f"  Schmidt&Allen+07 (real X-ray): mean ratio {sa_ratios.mean():.4f}, median c~{np.median(sa_c):.2f}"
    )
    print()
    print("  Buote's own c14=9.0 and Schmidt&Allen's own c0=7.55 are both HIGHER")
    print("  than Duffy+08's simulated normalization -- consistent with the")
    print("  documented direction (real concentrations run higher than simulated).")
    print("  Whether this closes P196's own 1.47x gap is read directly from the")
    print("  mean-ratio numbers above, not asserted.")
