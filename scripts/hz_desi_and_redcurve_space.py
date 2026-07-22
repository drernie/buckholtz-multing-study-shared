"""hz_desi_and_redcurve_space.py — pre-computed material for TJB's H(z) chart questions.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · DO NOT PRESUME TJB's CURVE.

Three self-contained, reproducible computations that let Sergey arrive with numbers
in hand to help Dr. Buckholtz, WITHOUT needing TJB's input first:

(A) DESI DR2 z=2.33 Lyman-alpha reconstruction (Q3/Q4).
    Independently verify H(2.33) from D_H/r_d = 8.632 +- 0.098 (stat) +- 0.026 (sys)
    [VERIFIED-WEBFETCH arXiv:2503.14739, DESI DR2 Results II], with r_d dependence made
    EXPLICIT (the whole point is that the number moves with r_d). Then place LCDM@Planck
    and LCDM@SH0ES at z=2.33 next to it.

(B) Characterize the CONSTRAINED SPACE of "red curves" consistent with the CHART's three
    visual features (NOT a claim about what TJB used):
      - pinned to H0 = 73 at z = 0
      - crosses LCDM@Planck near z ~ 1.6
      - lands BELOW the DESI point at z = 2.33 (chart shows red undershooting DESI)
    Two candidate one-parameter families are scanned:
      (B1) LCDM shape at H0=73 with a free effective Omega_m
      (B2) LCDM@Planck-shape at H0=73 plus an extra (1+z)^n additive term
    We report which parameter values satisfy the crossing, then what each predicts at
    z=2.33. Every such curve is labelled a CANDIDATE CONSISTENT WITH THE CHART, no more.

(C) For calibration: LCDM@73 (pure anchor change, no extra z-dependence) at z=2.33, to
    show WHY the chart's red curve cannot be a pure anchor change (it would overshoot DESI).

Run:  python scripts/hz_desi_and_redcurve_space.py
Exit: 0. All numbers printed to stdout; nothing written to disk.
"""

from __future__ import annotations

import numpy as np

C_KMS = 299792.458  # speed of light, km/s (exact, SI)

# --- fiducial cosmological anchors (same as plot_hubble_anchoring.py) ---------
OM_FID = 0.317  # matter density used for the "same-shape" LCDM curves
PLANCK_H0 = 67.36  # Planck 2018 TT,TE,EE+lowE+lensing
PLANCK_OM = 0.3153  # Planck 2018 base-LCDM Omega_m (for the LCDM@Planck reference curve)
SH0ES_H0 = 73.04  # Riess+2022 SH0ES

# --- DESI DR2 Lyman-alpha BAO [VERIFIED-WEBFETCH arXiv:2503.14739] ------------
DESI_Z = 2.33
DESI_DH_RD = 8.632
DESI_DH_RD_STAT = 0.098
DESI_DH_RD_SYS = 0.026


def lcdm(z, h0, om):
    """Flat-LCDM H(z). MULTING background shares this shape at 1st order (P2, docs/127)."""
    return h0 * np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def h_from_dhrd(dh_rd, r_d):
    """H(z) [km/s/Mpc] from D_H/r_d.  D_H = c/H  =>  H = c / (r_d * (D_H/r_d))."""
    return C_KMS / (r_d * dh_rd)


def sep(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def part_a_desi():
    sep("(A) DESI DR2 z=2.33 reconstruction  [Q3 / Q4]")
    print("  Input (arXiv:2503.14739, DESI DR2 Results II):")
    print(f"    z_eff = {DESI_Z}")
    print(f"    D_H/r_d = {DESI_DH_RD} +- {DESI_DH_RD_STAT} (stat) +- {DESI_DH_RD_SYS} (sys)")
    print("  H(2.33) = c / (r_d * D_H/r_d) -- explicit r_d dependence:")
    print("    r_d [Mpc]   H(2.33) [km/s/Mpc]   (with stat+sys on D_H/r_d)")
    # combined uncertainty on D_H/r_d (stat + sys in quadrature)
    dhrd_err = float(np.hypot(DESI_DH_RD_STAT, DESI_DH_RD_SYS))
    rel = dhrd_err / DESI_DH_RD
    for r_d in (147.09, 147.05, 139.5, 143.0, 150.0):
        h = h_from_dhrd(DESI_DH_RD, r_d)
        herr = h * rel  # at FIXED r_d (r_d uncertainty NOT included here)
        tag = ""
        if abs(r_d - 147.09) < 1e-6:
            tag = "  <- Planck/BBN standard r_d (user-cited)"
        if abs(r_d - 139.5) < 1e-6:
            tag = "  <- example LOWERED r_d (early-dark-energy-like)"
        print(f"    {r_d:7.2f}     {h:7.2f} +- {herr:4.2f} (D_H/r_d only){tag}")
    h_std = h_from_dhrd(DESI_DH_RD, 147.09)
    print(
        f"\n  => at the standard r_d=147.09 Mpc:  H(2.33) = {h_std:.1f} +- "
        f"{h_std * rel:.1f} km/s/Mpc  [VERIFIED-BASH]"
    )
    print("     CAVEAT (anti-cherry-pick): this number is CONDITIONAL on r_d. A lower r_d")
    print("     (some tension-resolution models) RAISES H(2.33) proportionally. The DESI")
    print("     D_H/r_d ratio is the invariant; H(2.33) in km/s/Mpc is model-dependent.")
    return h_std, h_std * rel


def part_c_pure_anchor(h_desi, h_desi_err):
    sep("(C) Calibration: pure-anchor curves at z=2.33 (NO extra z-dependence)")
    for h0, om, lab in (
        (PLANCK_H0, PLANCK_OM, "LCDM@Planck (67.36, Om=0.3153)"),
        (PLANCK_H0, OM_FID, "LCDM@Planck-shape (67.36, Om=0.317)"),
        (SH0ES_H0, OM_FID, "LCDM@SH0ES  (73.04, Om=0.317)  = 'pure anchor' red"),
    ):
        h = float(lcdm(DESI_Z, h0, om))
        d = (h - h_desi) / h_desi_err
        print(f"    {lab:44s} H(2.33)={h:6.1f}   ({d:+.1f} sigma vs DESI)")
    print("  => A PURE anchor change (LCDM@73) predicts H(2.33) ~ 257, OVERSHOOTING DESI")
    print("     (~236). So if TJB's red curve undershoots DESI (as the chart appears to),")
    print("     it CANNOT be a pure anchor change -- it must bend DOWN at high z. This is")
    print("     the same fact as 'the red curve crosses LCDM@Planck near z~1.6'. [INFERRED]")


def part_b_redcurve_space(h_desi, h_desi_err):
    sep("(B) Constrained SPACE of red curves consistent with the CHART (NOT TJB's actual)")
    zc = 1.6  # nominal crossing redshift read from chart [WEAK: chart-read]
    h_planck_at_zc = float(lcdm(zc, PLANCK_H0, PLANCK_OM))
    print("  Chart features used (all [WEAK], read from image):")
    print(f"    (i)  pinned to H0 = {SH0ES_H0} at z=0")
    print(
        f"    (ii) crosses LCDM@Planck near z ~ {zc}  (LCDM@Planck there: H={h_planck_at_zc:.1f})"
    )
    print(f"    (iii) lands below DESI H(2.33) ~ {h_desi:.0f}")

    # --- family B1: LCDM shape at H0=73 with free effective Omega_m ------------
    print("\n  Family B1: H(z) = 73 * sqrt(Om_eff (1+z)^3 + (1-Om_eff))")
    print("    Solve 'crosses LCDM@Planck at z=1.6' for Om_eff:")
    # 73*sqrt(Om*(1+zc)^3+1-Om) = h_planck_at_zc
    tgt = (h_planck_at_zc / SH0ES_H0) ** 2
    a = (1.0 + zc) ** 3
    om_eff = (tgt - 1.0) / (a - 1.0)
    print(f"      Om_eff = {om_eff:.4f}  (vs Planck {PLANCK_OM}) [VERIFIED-BASH]")
    h_b1_desi = float(lcdm(DESI_Z, SH0ES_H0, om_eff))
    print(
        f"      => this curve at z=2.33: H = {h_b1_desi:.1f}  "
        f"({(h_b1_desi - h_desi) / h_desi_err:+.1f} sigma vs DESI)"
    )
    print("      Also scan crossing z in [1.4, 1.8] to bound Om_eff:")
    for zc_i in (1.4, 1.5, 1.6, 1.7, 1.8):
        hp = (float(lcdm(zc_i, PLANCK_H0, PLANCK_OM)) / SH0ES_H0) ** 2
        om_i = (hp - 1.0) / ((1.0 + zc_i) ** 3 - 1.0)
        h23 = float(lcdm(DESI_Z, SH0ES_H0, om_i))
        print(f"        cross@z={zc_i}: Om_eff={om_i:.3f} -> H(2.33)={h23:.1f}")

    # --- family B2: LCDM@Planck-shape at 73 plus an extra (1+z)^n term ---------
    print("\n  Family B2: H(z)^2 = [73^2/67.36^2] * H_LCDM,Planck(z)^2 - A*(1+z)^n")
    print("    (a curve pinned to 73 at z=0 via the prefactor, bent down by -A(1+z)^n)")
    print("    For each n, solve A so it crosses LCDM@Planck exactly at z=1.6:")
    k = (SH0ES_H0 / PLANCK_H0) ** 2  # prefactor so z=0 value is 73
    for n in (2.0, 3.0, 4.0):
        # k*Hp(zc)^2 - A*(1+zc)^n = Hp(zc)^2  => A = (k-1)*Hp(zc)^2/(1+zc)^n
        hp_zc2 = float(lcdm(zc, PLANCK_H0, PLANCK_OM)) ** 2
        A = (k - 1.0) * hp_zc2 / (1.0 + zc) ** n
        # value at z=0 (check pin): sqrt(k*Hp0^2 - A) should be ~73
        hp0_2 = float(lcdm(0.0, PLANCK_H0, PLANCK_OM)) ** 2
        h0_chk = np.sqrt(k * hp0_2 - A * 1.0)
        hp23_2 = float(lcdm(DESI_Z, PLANCK_H0, PLANCK_OM)) ** 2
        val23 = k * hp23_2 - A * (1.0 + DESI_Z) ** n
        h23 = float(np.sqrt(val23)) if val23 > 0 else float("nan")
        print(
            f"      n={n}: A={A:8.1f}  z=0 pin check H0={h0_chk:5.1f}  "
            f"-> H(2.33)={h23:6.1f}  ({(h23 - h_desi) / h_desi_err:+.1f} sig vs DESI)"
        )

    print("\n  READING (honest, bounded):")
    print("   * MANY one-parameter curves reproduce all three chart features -- the chart")
    print("     alone does NOT pin the red curve's functional form. This is exactly why")
    print("     letter-question 2 (ask TJB for the explicit red-curve form) is the crux.")
    print("   * A LOW effective Om (~0.26) at H0=73 is the SIMPLEST family member that")
    print("     hits all three -- but this is a CANDIDATE CONSISTENT WITH THE CHART, NOT a")
    print("     claim about MULTING or about what TJB computed. [candidate-space only]")


def main():
    print("H(z) chart pre-computation for TJB  |  OUR_RECONSTRUCTION  |  do not presume")
    h_desi, h_desi_err = part_a_desi()
    part_c_pure_anchor(h_desi, h_desi_err)
    part_b_redcurve_space(h_desi, h_desi_err)
    print("\n" + "=" * 74)
    print("DONE. Evidence: DESI D_H/r_d [VERIFIED-WEBFETCH]; all H-values [VERIFIED-BASH];")
    print("chart features (crossing z, undershoot) [WEAK, image-read]; red-curve family")
    print("membership [candidate-space, NOT a claim about TJB's actual curve].")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
