"""P219 -- docs/158 item 2: DESI-DR1 Cosmic Chronometers as an out-of-sample
check on v82's frozen fitted parameters -- BOUNDED version.

WHY BOUNDED, NOT THE FULL TEST. The full test docs/158 specified needs
DESI-DR1 CC's own 45-point H(z) array (z=0.36..0.80, step 0.01) and its
full covariance matrix C_H = C_stat + C_sys (their Eq. 12-13). That data
is described in the paper (arXiv:2608.13178) as "provided as additional
material" -- but a direct WebFetch of the arXiv abstract page (2026-09-07)
returned: "Supplementary material will be provided in the journal version
of the article, currently under correction." The array is NOT yet public.

Per falsification-ladder.md Step 2a (Substrate Gate): this is
BLOCKED-INFRASTRUCTURE, not evidence about anything. Guessing correlations
to approximate the missing covariance matrix would be exactly the kind of
fabricated-precision move this project's own rules forbid.

What IS available, quoted directly from the paper's own text (verified via
mcp__arxiv__download_paper and search_paper_text, 2026-09-07):

  - Central cosmographic value at the pivotal redshift z0~=0.57:
      H = 95.1 (+10.9/-6.0 stat) +/- 11.3 (syst) km/s/Mpc
  - Two ADDITIONAL, EXPLICITLY UNCORRELATED local finite-difference points
    (paper's own words: "two additional local and uncorrelated
    measurements... should not be interpreted as two continuations in
    redshift... but rather as two separate estimations"):
      H(z~=0.55) = 104.5 (+13.2/-7.6 stat) +/- 22.4 (syst) km/s/Mpc
      H(z~=0.61) =  88.5 (+6.7/-12.6 stat) +/-  8.1 (syst) km/s/Mpc

This script freezes MULTING's own fitted parameters at v82's own reported
"unconstrained_spotlighted" Table II row (H0_anchor=73.22, beta1=1.4335e10,
beta2=7.8067e17 -- verbatim from generate_all_results.py, already
positive-controlled against TJB's own reported chi2/r in
FINDING_P176_...md) -- NO REFIT -- and evaluates H_MULTING(z) at these
three DESI points, alongside flat LCDM at Planck values (H0=67.4,
Om=0.315), also frozen, also not refit.

LABEL, per docs/158's own instruction: this is a "frozen-parameter,
out-of-sample scoring against a different galaxy sample using the SAME
cosmic-chronometer method" -- NOT a post-freeze prediction (P218's sibling
provenance check found the archive was last updated 2026-08-11, 2 days
before this DESI paper; the preprint itself was posted 2026-08-19, 6 days
AFTER). NOT independent of the 31 already-fitted CC points' systematics
(same stellar-population-synthesis method, same z-range). This is a
bounded sanity check with n=3, not a decisive test -- the decisive
version needs the full covariance array and is BLOCKED pending its
publication.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own multing_core.py, same subset FINDING_P176 already
# positive-controlled against his own reported chi2_33/r_33 values.
# ---------------------------------------------------------------------------
MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20
G = 6.674e-11
C_LIGHT = 299792458.0
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
    F1 = beta_1 * (-G) * 2.0 * M * (k / C_LIGHT**2) * (R / d) / d**2
    F2 = beta_2 * (-G) * (k / C_LIGHT**2) ** 2 * (R * R / d**2) / d**2
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


def H_lcdm_kms(z, H0_kms=67.4, Om=Om_planck):
    return H0_kms * Efun(z, Om=Om)


# ---------------------------------------------------------------------------
# v82's own frozen fit -- "unconstrained_spotlighted" row, Table II,
# verbatim from generate_all_results.py's TABLE_II dict
# (already positive-controlled in FINDING_P176_...md against TJB's own
# reported chi2_33=15.75, r_33=0.9659)
# ---------------------------------------------------------------------------
H0_ANCHOR = 73.22
B1_FIT = 1.4335e10
B2_FIT = 7.8067e17
Z_SHOES = 0.0233  # zref -- H0_ANCHOR is defined AT this z, not at z=0
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, 2.33, 800), [0.55, 0.57, 0.61]])))

# ---------------------------------------------------------------------------
# DESI-DR1 CC (arXiv:2608.13178), quoted verbatim -- fetched 2026-09-07
# ---------------------------------------------------------------------------
DESI_POINTS = {
    "z0~0.57 (central cosmographic MAP)": (0.57, 95.1, (6.0, 10.9), 11.3),
    "z~0.55 (local, uncorrelated, super-massive subgroup)": (0.55, 104.5, (7.6, 13.2), 22.4),
    "z~0.61 (local, uncorrelated, reddest/purest subgroup)": (0.61, 88.5, (12.6, 6.7), 8.1),
}


def sep(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def main() -> int:
    sep("SUBSTRATE GATE -- what this script can and cannot do")
    print("""
  The full DESI-DR1 CC test needs their 45-point H(z) array + full
  covariance C_H = C_stat + C_sys. WebFetch of the arXiv abstract page
  (2026-09-07) returned: "Supplementary material will be provided in the
  journal version of the article, currently under correction."
  -> STATUS: BLOCKED-INFRASTRUCTURE for the full test.
  -> NOT evidence for or against anything (falsification-ladder.md Step 2a).
  This script does the bounded n=3 check that IS possible from the paper's
  own printed text, clearly labelled as such.
""")

    sep("PC1 -- reproduce v82's own reported chi2_33/r_33 at this frozen point")
    # positive control inherited from FINDING_P176 -- re-verified inline
    cc_points = [
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
    zd = np.array([p[0] for p in cc_points])
    Hd = np.array([p[1] for p in cc_points])
    sd = np.array([p[2] for p in cc_points])
    z33 = np.concatenate([zd, [0.0233], [2.33]])
    H33 = np.concatenate([Hd, [73.04], [236.1]])
    s33 = np.concatenate([sd, [1.04], [2.8]])
    Hm_fine = H_of_z_kms(ZFINE, H0_ANCHOR, B1_FIT, B2_FIT, Z_SHOES)
    Hp = np.interp(z33, ZFINE, Hm_fine)
    chi2_33 = float(np.sum(((Hp - H33) / s33) ** 2))
    print(f"  computed chi2_33 = {chi2_33:.2f}   (paper Table II: 15.75)")
    ok1 = abs(chi2_33 - 15.75) / 15.75 < 0.02
    print(f"  {'PASS' if ok1 else 'FAIL'}")
    if not ok1:
        return 1

    sep("THE BOUNDED n=3 CHECK -- frozen MULTING vs frozen LCDM, no refit either side")
    print(
        f"  {'DESI point':<52} {'z':>5} {'H_DESI':>9} {'sig':>6} "
        f"{'H_MULT':>8} {'z_MULT':>7} {'H_LCDM':>8} {'z_LCDM':>7}"
    )
    for label, (z, h_obs, (sig_lo, sig_hi), sig_sys) in DESI_POINTS.items():
        sig_stat = 0.5 * (sig_lo + sig_hi)  # symmetrized, noted as an approximation
        sig_tot = float(np.hypot(sig_stat, sig_sys))
        h_mult = float(np.interp(z, ZFINE, Hm_fine))
        h_lcdm = float(H_lcdm_kms(z))
        z_mult = (h_mult - h_obs) / sig_tot
        z_lcdm = (h_lcdm - h_obs) / sig_tot
        print(
            f"  {label:<52} {z:5.2f} {h_obs:9.1f} {sig_tot:6.1f} "
            f"{h_mult:8.1f} {z_mult:7.2f} {h_lcdm:8.1f} {z_lcdm:7.2f}"
        )

    print("""
  z_MULT / z_LCDM = (model - observed) / sigma_total, sigma_total = stat
  (symmetrized from the paper's own asymmetric interval) added in
  quadrature with syst. This is a per-point sanity check, NOT a joint
  chi-squared -- with only 3 points and no covariance, a joint statistic
  would overstate precision exactly where none exists.
""")

    sep("VERDICT")
    print("""
  This is a BOUNDED, n=3, no-refit sanity check -- not the decisive OOS
  test docs/158 specified, which needs the full 45-point covariance array
  and is BLOCKED pending journal publication (see header).

  Frozen parameters: MULTING (H0_anchor=73.22, beta1=1.4335e10,
  beta2=7.8067e17, v82's own "unconstrained_spotlighted" row) and flat
  LCDM (H0=67.4, Om=0.315, Planck) -- neither refit against DESI.

  Label per docs/158: out-of-sample (the fit's own DESI point is a DR2
  Lyman-alpha BAO measurement, not a chronometer), NOT independent (same
  CC method/systematics, overlapping z-range with the 31 fitted points),
  NOT post-freeze (archive updated 2026-08-11, this DESI paper posted
  2026-08-13 -- a 2-day margin only).
""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
