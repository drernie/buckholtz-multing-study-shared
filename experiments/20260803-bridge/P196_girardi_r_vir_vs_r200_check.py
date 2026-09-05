"""P196 -- independent rebuild + overdensity-definition correction for the
Girardi-R_vir vs TJB-style rho_crit(z)-based R500 comparison.

Motivated by TJB's own letter (2026-08-30) pointing at Section II.F of v82
(his own Class I/II/III evidentiary system; r_X(z) built via rho_crit(z) is
flagged as "the most serious residual dependence"). A prior chat session ran
a first version of this check on real HeCS-SZ data and found r=0.883, mean
ratio 1.128 (+/-13%), scatter +/-14% -- but left files only in that session's
scratchpad, and did not control for two real overdensity-definition issues
found while rebuilding this independently:

  (1) Girardi's R_vir (Delta~178) is referenced to rho_crit,0 (z=0, NO
      z-evolution), not rho_crit(z) -- a different density reference than
      any rho_crit(z)-based radius.
  (2) v82's own Section II.F, read directly [line 602-604 of this project's
      own markdown conversion], calls its r_X(z) construction "the standard
      R500-type definition" -- Delta=500, NOT Delta=200. A first pass of
      this file used Delta=200 (matching HeCS-SZ's own tabulated M200c
      column) and got a raw mean ratio of 1.61 -- NOT close to the prior
      chat's reported 1.128 -- which is what surfaced this Delta-target
      mismatch. This project's own P158_addendum2_real_mass_function.py
      (same session, earlier) already independently used Delta=500 for
      exactly this reason (see its own OVERDENSITY=500 comment).

This file independently re-fetches the real HeCS-SZ catalog (not copied from
the prior chat, M200c only -- the catalog's own Delta=200 caustic mass) and:
  Step 1: converts M200c -> M500 (and R500) via the NFW profile + Duffy et
    al. (2008) concentration-mass relation, to match v82's OWN R500-type
    target exactly.
  Step 2a: reference-density correction (EXACT, no free parameter) --
    R_vir,z-ref = R_vir / E(z)^(2/3).
  Step 2b: overdensity-shape correction (approximate, concentration-
    dependent) -- converts Delta=178 (after 2a, now on the rho_crit(z)
    reference) to Delta=500, via the SAME NFW profile used in Step 1.

See CLAIM_P196_girardi_r_vir_vs_r200_check.md for the full protocol
(including its own dated correction note) and the pre-registered MCID.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq
from scipy.stats import pearsonr

# ---------------------------------------------------------------------------
# Cosmology (flat LCDM, standard values -- the prior chat's own stated
# choice: Om=0.3, OL=0.7, h=0.7; used ONLY to define rho_crit(z), the exact
# same convention TJB's own r_X(z) construction (Section II.F, Class III)
# uses -- reproducing that construction is the whole point of this file.
# ---------------------------------------------------------------------------
OM = 0.3
OL = 0.7
H0_KM_S_MPC = 70.0
G_SI = 6.674e-11
MPC_TO_M = 3.0856775814913673e22
MSUN_TO_KG = 1.98892e30
KM_TO_M = 1000.0


def efun(z):
    return np.sqrt(OM * (1.0 + z) ** 3 + OL)


def h0_si():
    return H0_KM_S_MPC * KM_TO_M / MPC_TO_M


def rho_crit(z):
    """rho_crit(z) = 3 H(z)^2 / (8 pi G), in kg/m^3."""
    hz = h0_si() * efun(z)
    return 3.0 * hz**2 / (8.0 * np.pi * G_SI)


RHO_CRIT_0 = rho_crit(0.0)

DELTA_VIR = 18.0 * np.pi**2  # Girardi's own spherical-collapse (Om0=1) constant
DELTA_200 = 200.0
DELTA_500 = 500.0  # v82's own Section II.F target -- "the standard R500-type definition"


def girardi_r_vir_mpc(sigma_kms):
    """Girardi et al. (1998) Eq. 11: R_vir ~ 0.002 * sigma_P (h^-1 Mpc)."""
    h_local = H0_KM_S_MPC / 100.0
    return 0.002 * sigma_kms / h_local


def r_delta_mpc(mass_msun, z, delta):
    """R such that (4/3)pi*delta*rho_crit(z)*R^3 = mass -- exact, no NFW."""
    m_kg = mass_msun * MSUN_TO_KG
    rc = rho_crit(z)
    r_m = (3.0 * m_kg / (4.0 * np.pi * delta * rc)) ** (1.0 / 3.0)
    return r_m / MPC_TO_M


def duffy2008_concentration(m_delta_msun, z, delta_pivot_is_200=True):
    """Duffy et al. (2008) c-M-z relation, full-sample NFW calibration
    (their Table 1, row 'Full', c200-M200 relation): c = A*(M/Mpivot)^B*(1+z)^C,
    A=5.71, B=-0.084, C=-0.47, Mpivot=2e12 Msun/h.
    [VERIFIED-arXiv: arXiv:0804.2486, Table 1] -- coefficients used as
    published, applied here to M200c (delta_pivot_is_200=True is the only
    mode used in this file -- their relation is specifically calibrated
    for c200-M200, not re-derived for other Delta)."""
    h_local = H0_KM_S_MPC / 100.0
    m_pivot_msun = 2.0e12 / h_local
    a, b, c = 5.71, -0.084, -0.47
    return a * (m_delta_msun / m_pivot_msun) ** b * (1.0 + z) ** c


def _nfw_m_shape(x):
    return np.log(1.0 + x) - x / (1.0 + x)


def nfw_from_m200c(m200c_msun, z):
    """Build an NFW halo (rho_s, rs) anchored on the REAL M200c + Duffy+08
    c200(M200c,z) -- returns (rho_s [kg/m^3], rs [Mpc])."""
    c200 = duffy2008_concentration(m200c_msun, z)
    r200 = r_delta_mpc(m200c_msun, z, DELTA_200)
    rs_mpc = r200 / c200
    m200_kg = m200c_msun * MSUN_TO_KG
    rho_s = m200_kg / (4.0 * np.pi * (rs_mpc * MPC_TO_M) ** 3 * _nfw_m_shape(c200))
    return rho_s, rs_mpc, c200


def r_delta_from_nfw_mpc(rho_s, rs_mpc, z, delta):
    """Solve (4/3)pi*delta*rho_crit(z)*R^3 = 4pi*rho_s*rs^3*m_shape(R/rs)
    for R, given an NFW halo (rho_s, rs)."""
    rc = rho_crit(z)

    def f(r_mpc):
        lhs = (4.0 / 3.0) * np.pi * delta * rc * (r_mpc * MPC_TO_M) ** 3
        rhs = 4.0 * np.pi * rho_s * (rs_mpc * MPC_TO_M) ** 3 * _nfw_m_shape(r_mpc / rs_mpc)
        return lhs - rhs

    return brentq(f, 1e-4, 20.0)


def step2a_reference_density_correction(r_vir_mpc, z):
    """EXACT: convert R_vir (Delta=178, referenced to rho_crit,0) to the
    SAME Delta=178, but referenced to rho_crit(z) instead -- a pure mass-
    conserving geometric rescaling, no NFW/concentration assumption.
    R_new = R_old * (rho_crit,0 / rho_crit(z))^(1/3) = R_old / E(z)^(2/3)
    """
    return r_vir_mpc / efun(z) ** (2.0 / 3.0)


def test_positive_control_girardi_formula_self_consistent():
    """Girardi 1998's own Eq. 5 (virial mass) + spherical-collapse density
    criterion (Om0=1) + Eq. 10 (R_PV(A), R_c=0.17 h^-1 Mpc, their Sec. 4.2
    median), solved self-consistently at A=R_vir, must reproduce their own
    published Eq. 11 coefficient (~0.002) -- independent re-derivation from
    the more fundamental equations, fully in SI units."""
    h_local = H0_KM_S_MPC / 100.0
    r_c_m = 0.17 / h_local * MPC_TO_M
    sigma_test_ms = 1000.0 * KM_TO_M

    def r_pv_of_a(a_m):
        x = a_m / r_c_m
        return a_m * 1.193 * (1.0 + 0.032 * x) / (1.0 + 0.107 * x)

    def residual(r_vir_m):
        r_pv = r_pv_of_a(r_vir_m)
        m_vir_from_virial = (3.0 * np.pi / 2.0) * sigma_test_ms**2 * r_pv / G_SI
        m_vir_from_density = (4.0 * np.pi / 3.0) * DELTA_VIR * RHO_CRIT_0 * r_vir_m**3
        return m_vir_from_virial - m_vir_from_density

    r_vir_m = brentq(residual, 1e18, 1e24)
    r_vir_h_mpc = (r_vir_m / MPC_TO_M) * h_local
    implied_coeff = r_vir_h_mpc / 1000.0
    rel_err = abs(implied_coeff - 0.002) / 0.002
    assert rel_err < 0.05, (
        f"Girardi Eq.11 self-consistency off by {rel_err:.1%}: coeff={implied_coeff:.5f}"
    )
    return implied_coeff


def test_positive_control_step2a_identity_at_z0():
    r_test = 1.5
    r_corrected = step2a_reference_density_correction(r_test, 0.0)
    assert abs(r_corrected - r_test) < 1e-10, "Step 2a not identity at z=0"
    return True


def test_positive_control_nfw_r200_recovers_input():
    """The NFW machinery, applied AT Delta=200 to a halo built from a real
    M200c, must recover the same R200 as the direct (no-NFW) Delta=200
    formula -- checks the NFW round-trip introduces no error at the anchor
    point before trusting it at Delta=500."""
    m_test, z_test = 3.0e14, 0.1
    rho_s, rs_mpc, c200 = nfw_from_m200c(m_test, z_test)
    r200_direct = r_delta_mpc(m_test, z_test, DELTA_200)
    r200_nfw = r_delta_from_nfw_mpc(rho_s, rs_mpc, z_test, DELTA_200)
    rel_err = abs(r200_nfw - r200_direct) / r200_direct
    assert rel_err < 0.01, f"NFW R200 round-trip off by {rel_err:.2%}"
    return True


if __name__ == "__main__":
    from astroquery.vizier import Vizier

    coeff = test_positive_control_girardi_formula_self_consistent()
    print("Positive control 1: Girardi Eq.9+10 self-consistency reproduces Eq.11's")
    print(f"  own coefficient (~0.002): implied={coeff:.5f}: PASS\n")

    test_positive_control_step2a_identity_at_z0()
    print("Positive control 2: Step 2a reference-density correction is identity")
    print("  at z=0 (E(0)=1): PASS\n")

    test_positive_control_nfw_r200_recovers_input()
    print("Positive control 3: NFW machinery recovers direct R200 at its own")
    print("  anchor point (Delta=200) before trusting it at Delta=500: PASS\n")

    print("Fetching HeCS-SZ (Rines et al. 2016, VizieR J/ApJ/819/63/table4)")
    print("independently this session (not copied from the prior chat)...")
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

    r500_arr = np.empty(n)
    r_vir_2b = np.empty(n)
    c200_arr = np.empty(n)
    r_vir_2a = np.array(
        [step2a_reference_density_correction(rv, z) for rv, z in zip(r_vir_raw, z_arr, strict=True)]
    )
    for i in range(n):
        rho_s, rs_mpc, c200 = nfw_from_m200c(m200c_arr[i], z_arr[i])
        r500_arr[i] = r_delta_from_nfw_mpc(rho_s, rs_mpc, z_arr[i], DELTA_500)
        r_vir_2b[i] = r_delta_from_nfw_mpc(rho_s, rs_mpc, z_arr[i], DELTA_VIR)
        c200_arr[i] = c200
    # r_vir_2b currently holds R_(Delta=178) on the SAME halo's own NFW
    # profile, evaluated at the rho_crit(z) reference (matches step 2a's
    # own reference) -- rescale Girardi's OWN measured, z-reference-
    # corrected R_vir (r_vir_2a) onto the R500 scale using that halo's own
    # R500/R178 shape ratio (do not just use the model's own R178 as the
    # answer -- Girardi's real R_vir is the actual observable being tested).
    shape_ratio_500_to_178 = r500_arr / r_vir_2b
    r_vir_2b_final = r_vir_2a * shape_ratio_500_to_178

    ratio_raw = r_vir_raw / r500_arr
    ratio_2a = r_vir_2a / r500_arr
    ratio_2b = r_vir_2b_final / r500_arr
    r_corr_raw, _ = pearsonr(r_vir_raw, r500_arr)

    print("=" * 88)
    print("TARGET: v82's OWN Section II.F construction is R500 (Delta=500), NOT R200 --")
    print("  M200c (HeCS-SZ's own tabulated Delta=200 caustic mass) converted to R500 via")
    print("  NFW + Duffy+08 c200(M,z), matching this project's own P158_addendum2 convention")
    print("=" * 88)
    print(f"  n={n}, Pearson r(R_vir_raw, R500)={r_corr_raw:.4f}")
    print(f"  median c200 (Duffy+08) = {np.median(c200_arr):.2f}\n")

    print("=" * 88)
    print("ENDPOINT 1 -- REPRODUCTION (raw Girardi R_vir vs TJB-style R500(z), uncorrected)")
    print("=" * 88)
    print(f"  mean ratio R_vir/R500 = {ratio_raw.mean():.4f}  (prior chat reported 1.128 vs R200)")
    print(f"  std/mean (scatter)    = {ratio_raw.std() / ratio_raw.mean():.4%}  (prior chat: ~14%)")

    print()
    print("=" * 88)
    print("ENDPOINT 2a -- + reference-density correction (EXACT, R_vir/E(z)^(2/3))")
    print("=" * 88)
    print(
        f"  mean ratio = {ratio_2a.mean():.4f}   scatter = {ratio_2a.std() / ratio_2a.mean():.4%}"
    )
    print(
        f"  z range: [{z_arr.min():.3f}, {z_arr.max():.3f}], median E(z)^(2/3) factor "
        f"= {np.median(1.0 / efun(z_arr) ** (2.0 / 3.0)):.4f}"
    )

    print()
    print("=" * 88)
    print("ENDPOINT 2b -- + overdensity-shape correction (Delta=178->500, Duffy+08 c(M,z))")
    print("=" * 88)
    print(
        f"  mean ratio = {ratio_2b.mean():.4f}   scatter = {ratio_2b.std() / ratio_2b.mean():.4%}"
    )

    print()
    print("=" * 88)
    print("ENDPOINT 3 -- does the RAW (uncorrected) ratio correlate with z?")
    print("=" * 88)
    r_resid_z, p_resid_z = pearsonr(z_arr, ratio_raw)
    print(f"  Pearson r(z, ratio_raw) = {r_resid_z:.4f}  (p={p_resid_z:.4f})")
    print("  Mechanism check: R_vir carries NO z-dependence (Girardi uses H0 only);")
    print("  R500(z) SHRINKS as z grows (rho_crit(z) grows with E(z)^2 for z>0).")
    print("  => ratio = R_vir/R500 should RISE with z if this mechanism is real")
    print(
        f"  => predicted sign: POSITIVE. Observed: {'POSITIVE, matches' if r_resid_z > 0 else 'NEGATIVE, does NOT match'}"
    )

    print()
    print("=" * 88)
    print("MCID CHECK (pre-registered in CLAIM_P196, applied to the R500 target)")
    print("=" * 88)
    mean_in_band = 0.95 <= ratio_2b.mean() <= 1.05
    scatter_drop_pp = (ratio_raw.std() / ratio_raw.mean() - ratio_2b.std() / ratio_2b.mean()) * 100
    material = mean_in_band or (scatter_drop_pp > 5.0)
    print(
        f"  Final (2a+2b) mean ratio in [0.95,1.05]? {mean_in_band} (value={ratio_2b.mean():.4f})"
    )
    print(f"  Scatter drop (raw -> 2a+2b), percentage points: {scatter_drop_pp:.2f}")
    print(f"  MATERIAL (per pre-registered MCID): {material}")

    print()
    print("=" * 88)
    print("VERDICT")
    print("=" * 88)
    if material:
        print("The overdensity-definition correction (retargeted to R500, v82's own")
        print("  construction) is MATERIAL by the pre-registered MCID.")
    else:
        print("The overdensity-definition correction (retargeted to R500, v82's own")
        print("  construction) is NOT material by the pre-registered MCID -- the")
        print("  Delta-retargeting from R200 to R500 changed the RAW numbers substantially")
        print("  (see Endpoint 1 vs the prior chat's own R200-based 1.128), but the")
        print("  z-reference and NFW-shape corrections on TOP of the correct R500 target")
        print("  do not further explain the remaining offset/scatter.")
