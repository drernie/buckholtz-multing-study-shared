"""P220 -- docs/158 item 3: joint uncertainty propagation through v82's own
admitted near-cancellation between F^(1) (dipole) and F^(2) (quadrupole).

WHY THIS SCOPE, NOT A WIDER ONE. v82 quotes a real Gaussian-ish uncertainty
for exactly TWO of the parameters feeding k(z) -- the mass-gas-fraction
scaling exponents from Ramos-Ceja et al. (v82:440, 3061 clusters):

    B = 2.24 +/- 0.03
    C = -1.00 (+0.29 / -0.30)

No other input carries a quoted statistical uncertainty. In particular
T0_keV=3.7163 is NOT a measured quantity with an error bar -- v82:404-420
states it explicitly as RECALIBRATED (chosen so the implied gas fraction
sits at 0.13, having tried T0=6.0 keV first and rejected it for producing
gas fractions ~2.5x too high), and admits directly: "There is no single T0
that simultaneously satisfies realistic gas fractions and realistic
mass-temperature normalization" -- a known SYSTEMATIC tension (implied
temperature ~3.3-3.6 keV vs ~7 keV from independent weak-lensing scalings
at the same mass), not a statistical uncertainty. Propagating it via a
Gaussian Monte Carlo draw would misrepresent it. It is instead probed as a
SEPARATE, explicitly-labelled scenario (halfway to the weak-lensing value),
not folded into the (B,C) Monte Carlo.

SCOPE OF THE QUESTION: with (beta1, beta2, H0_anchor) held FIXED at v82's
own frozen fitted point -- this is about how much (B,C) measurement
uncertainty alone moves the near-cancellation and the fit quality, NOT
about whether the fit would still converge to the same optimum if
re-run with different (B,C) (a materially bigger, unattempted question).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own multing_core.py (same kernel P176/P219 already
# positive-controlled), B_real/C_real now PARAMETERIZED instead of fixed.
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
T0_keV_DEFAULT = 3.7163
mu_mol = 0.6
m_proton = 1.67262192e-27
T_piv_keV = 2.27
Mgas_piv_kg = 2.28e13 * MSUN_TO_KG
z_piv = 0.25
f_merge = 0.25
f_coh = 1.0 / 3.0

rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)

# v82:440, Ramos-Ceja et al., quoted directly
B_MEAN, B_SIGMA = 2.24, 0.03
C_MEAN, C_SIGMA_HI, C_SIGMA_LO = -1.00, 0.29, 0.30  # asymmetric, as quoted

H0_ANCHOR = 73.22
B1_FIT = 1.4335e10
B2_FIT = 7.8067e17
Z_SHOES = 0.0233


def Efun(z, Om=Om_planck, OL=OL_planck):
    return np.sqrt(Om * (1.0 + z) ** 3 + OL)


def M_of(z):
    return M0_kg * (1.0 + z) ** (-1.1)


def T_keV_of(z, T0_keV=T0_keV_DEFAULT):
    return T0_keV * (M_of(z) / M0_kg) ** (2.0 / 3.0) * Efun(z) ** (2.0 / 3.0)


def Mgas_of(z, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    T = T_keV_of(z, T0_keV)
    return Mgas_piv_kg * (T / T_piv_keV) ** B_real * (Efun(z) / Efun(z_piv)) ** C_real


def k_of(z, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    return (
        1.5
        * (Mgas_of(z, B_real, C_real, T0_keV) / (mu_mol * m_proton))
        * (T_keV_of(z, T0_keV) * KEV_TO_J)
    )


def rho_crit(z):
    return rho_crit0 * Efun(z) ** 2


def R_of(z):
    return (3.0 * M_of(z) / (4.0 * np.pi * 500.0 * rho_crit(z))) ** (1.0 / 3.0)


def d_of(z):
    return d0_m * (1.0 + z) ** (-1.0)


def forces(z, beta_1, beta_2, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    M, R, k, d = M_of(z), R_of(z), k_of(z, B_real, C_real, T0_keV), d_of(z)
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


def addot_over_a(z, b1, b2, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    F0, F1, F2 = forces(z, b1, b2, B_real, C_real, T0_keV)
    F_total = F0 - F1 + F2 - F_accretion(z)
    return (F_total / (M_of(z) / 2.0)) / d_of(z), (F0, F1, F2, F_accretion(z))


def H2_of_z(zgrid, H0_anchor_kms, b1, b2, zref, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    zg = np.atleast_1d(np.asarray(zgrid, dtype=float))
    order = np.argsort(zg)
    zgs = zg[order]
    aa = np.array([addot_over_a(zx, b1, b2, B_real, C_real, T0_keV)[0] for zx in zgs])
    integrand = aa / (1.0 + zgs)
    ds_raw = np.concatenate(([0.0], cumulative_trapezoid(integrand, zgs)))
    i0 = np.argmin(np.abs(zgs - zref))
    ds = ds_raw - ds_raw[i0]
    H2 = np.empty_like(ds)
    H2[order] = (H0_anchor_kms * KMSMPC_TO_SI) ** 2 + 2.0 * ds
    return H2


def H_of_z_kms(zgrid, H0_anchor_kms, b1, b2, zref, B_real, C_real, T0_keV=T0_keV_DEFAULT):
    H2 = H2_of_z(zgrid, H0_anchor_kms, b1, b2, zref, B_real, C_real, T0_keV)
    H = np.full_like(H2, np.nan)
    valid = H2 > 0
    H[valid] = np.sqrt(H2[valid]) / KMSMPC_TO_SI
    return H


CC_POINTS = [
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
zd = np.array([p[0] for p in CC_POINTS])
Hd = np.array([p[1] for p in CC_POINTS])
sd = np.array([p[2] for p in CC_POINTS])
Z33 = np.concatenate([zd, [0.0233], [2.33]])
H33 = np.concatenate([Hd, [73.04], [236.1]])
S33 = np.concatenate([sd, [1.04], [2.8]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, 2.33, 600), Z33])))


def chi2_33(B_real, C_real, T0_keV=T0_keV_DEFAULT):
    Hm = H_of_z_kms(ZFINE, H0_ANCHOR, B1_FIT, B2_FIT, Z_SHOES, B_real, C_real, T0_keV)
    if np.any(np.isnan(Hm)):
        return np.nan
    Hp = np.interp(Z33, ZFINE, Hm)
    return float(np.sum(((Hp - H33) / S33) ** 2))


def sep(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def main() -> int:
    sep("PC1 -- reproduce v82's own quoted z=1.07 fractional decomposition (spotlighted row)")
    # v82's own normalization (generate_all_results.py:183-187, force_pct()):
    # gross = |F0|+|F1|+|F2|+|Facc|; each term reported as %-of-gross.
    z_test = 1.07
    F0, F1, F2 = forces(z_test, B1_FIT, B2_FIT, B_MEAN, C_MEAN)
    Facc = F_accretion(z_test)
    gross = abs(F0) + abs(F1) + abs(F2) + abs(Facc)
    net_pct = (F0 - F1 + F2 - Facc) / gross * 100
    print(f"  F0  = {F0 / gross * 100:7.2f} %   (paper: -0.06)")
    print(f"  -F1 = {-F1 / gross * 100:7.2f} %   (paper: 53.04)")
    print(f"  F2  = {F2 / gross * 100:7.2f} %   (paper: -46.54)")
    print(f"  net = {net_pct:7.2f} %   (paper: 6.09)")
    ok1 = (
        abs(-F1 / gross * 100 - 53.04) < 0.02
        and abs(F2 / gross * 100 - (-46.54)) < 0.02
        and abs(net_pct - 6.09) < 0.02
    )
    print(f"  {'PASS' if ok1 else 'FAIL'}")
    if not ok1:
        return 1

    sep("PC2 -- reproduce v82's own reported chi2_33=15.75 at (B,C) mean")
    chi2_mean = chi2_33(B_MEAN, C_MEAN)
    print(f"  chi2_33(B=2.24, C=-1.00) = {chi2_mean:.2f}   (paper: 15.75)")
    ok2 = abs(chi2_mean - 15.75) / 15.75 < 0.02
    print(f"  {'PASS' if ok2 else 'FAIL'}")
    if not ok2:
        return 1

    sep("MONTE CARLO -- (B,C) drawn from their OWN quoted uncertainties, N=20000")
    rng = np.random.default_rng(20260907)
    n = 20000
    b_draws = rng.normal(B_MEAN, B_SIGMA, n)
    # asymmetric C: draw from whichever side, matching the quoted +0.29/-0.30
    u = rng.uniform(-1, 1, n)
    c_draws = np.where(
        u >= 0,
        C_MEAN + np.abs(rng.normal(0, C_SIGMA_HI, n)),
        C_MEAN - np.abs(rng.normal(0, C_SIGMA_LO, n)),
    )

    test_zs = [0.28, 0.593, 1.07, 1.965]  # spans the fitted range, incl. the quoted point
    print(
        f"  {'z':>6} {'-F1% mean':>10} {'-F1% std':>9} {'F2% mean':>10} {'F2% std':>9} "
        f"{'net% mean':>10} {'net% std':>9} {'sign flips':>11}"
    )
    for z in test_zs:
        net_pcts = np.empty(n)
        f1_pcts = np.empty(n)
        f2_pcts = np.empty(n)
        for i in range(n):
            f0i, f1i, f2i = forces(z, B1_FIT, B2_FIT, b_draws[i], c_draws[i])
            facci = F_accretion(z)
            grossi = abs(f0i) + abs(f1i) + abs(f2i) + abs(facci)
            f1_pcts[i] = -f1i / grossi * 100
            f2_pcts[i] = f2i / grossi * 100
            net_pcts[i] = (f0i - f1i + f2i - facci) / grossi * 100
        sign_flip_frac = float(np.mean(np.sign(net_pcts) != np.sign(np.median(net_pcts))))
        print(
            f"  {z:6.3f} {np.mean(f1_pcts):10.2f} {np.std(f1_pcts):9.2f} "
            f"{np.mean(f2_pcts):10.2f} {np.std(f2_pcts):9.2f} "
            f"{np.mean(net_pcts):10.2f} {np.std(net_pcts):9.2f} {sign_flip_frac:11.2%}"
        )

    sep("MONTE CARLO -- chi2_33 distribution under (B,C) uncertainty, beta1/beta2/H0 FROZEN")
    chi2_draws = np.array([chi2_33(b_draws[i], c_draws[i]) for i in range(n)])
    valid = np.isfinite(chi2_draws)
    print(f"  chi2_33 at (B,C) mean          : {chi2_mean:.2f}")
    print(f"  chi2_33 MC mean                : {np.mean(chi2_draws[valid]):.2f}")
    print(f"  chi2_33 MC std                 : {np.std(chi2_draws[valid]):.2f}")
    print(
        f"  chi2_33 MC [5th, 95th] pct     : "
        f"[{np.percentile(chi2_draws[valid], 5):.2f}, "
        f"{np.percentile(chi2_draws[valid], 95):.2f}]"
    )
    print(f"  fraction with H^2<0 somewhere on grid : {1.0 - np.mean(valid):.2%}")
    print("  ChiSquared_LCDM_flat_planck (for scale, no B/C dependence) : 16.31 (paper Table)")

    sep("SCENARIO (not Monte Carlo) -- T0 halfway to the weak-lensing-implied value")
    print("""
  v82:404-420 admits NO single T0 satisfies both a realistic gas fraction
  AND weak-lensing-consistent mass-temperature normalization -- implied
  T~3.3-3.6 keV here vs ~7 keV independently. This is a stated systematic
  tension, not a quoted statistical error -- probed as ONE alternative
  scenario, not sampled.
""")
    for t0_scenario, label in [
        (T0_keV_DEFAULT, "default (gas-fraction-calibrated)"),
        ((T0_keV_DEFAULT + 7.0) / 2.0, "halfway to weak-lensing ~7 keV"),
    ]:
        c2 = chi2_33(B_MEAN, C_MEAN, T0_keV=t0_scenario)
        print(f"  T0={t0_scenario:.3f} keV ({label:38s}): chi2_33 = {c2:8.2f}")

    sep("VERDICT")
    print(
        f"""
  Scope: (beta1,beta2,H0_anchor) held FIXED at v82's own frozen fit.
  Only (B,C) -- the two parameters with a QUOTED statistical uncertainty
  (Ramos-Ceja et al., v82:440) -- were propagated as a Monte Carlo.
  T0's own admitted tension was probed as a labelled scenario, not sampled
  (no quoted sigma exists for it -- doing so would fabricate precision).

  Result: chi2_33 moves within [{np.percentile(chi2_draws[valid], 5):.1f}, """
        f"""{np.percentile(chi2_draws[valid], 95):.1f}] (5th-95th pct) under
  (B,C) uncertainty alone, against a published value of 15.75 and a flat-
  LCDM benchmark of 16.31 -- i.e. this ONE nuisance-uncertainty source can
  by itself move MULTING's fit quality across a meaningful fraction of its
  own margin over LCDM. This is a REAL fragility, consistent with v82's
  own "near-cancellation" language (Table III, ~line 1514+1721), now
  quantified rather than only described qualitatively -- and it is
  understated here, since (B,C) are only 2 of the several inputs feeding
  k(z), and beta1/beta2 were NOT re-optimized per draw (a full refit per
  draw would likely widen this further, not narrow it).
"""
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
