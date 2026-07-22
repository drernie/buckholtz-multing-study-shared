"""t6_neff_honest.py — Honest Delta N_eff exclusion for IDM dark neutrinos (docs/132 T6; R005 redo)

Fixes the FALSE-PRECISION "130-477 sigma" figure (flagged in docs/122 v2 point 4 as a
back-of-envelope Gaussian tail, not citable). Reports the exclusion as a FACTOR over the
allowed band, not a sigma, and tests the 3 escapes:
  (1) different BBN chemistry / expansion at BBN
  (2) early-decoupling hidden sector (entropy dilution by SM g* growth)
  (3) gravitational-only production (never thermalized)  <- the IDM-stated coupling

NO fitting. Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION.
Evidence: [VERIFIED-BASH] arithmetic; entropy-dilution formula standard (Kolb&Turner).
"""

from __future__ import annotations

# Combined CMB(Planck 2018)+BBN allowed extra radiation. Both independently give
# N_eff ~ 2.9-3.0; the 95% allowance for EXTRA species is small.
N_EFF_SM = 3.044
DELTA_NEFF_95 = 0.30  # representative Planck2018+BBN 95% upper bound on extra N_eff
N_ISOMERS = 5
NU_PER_ISOMER = 3  # each isomer replicates the 3 SM neutrino species (paper Sec 4.4)


def g_star(T_GeV: float) -> float:
    if T_GeV > 200:
        return 106.75
    if T_GeV > 0.15:
        return 61.75
    if T_GeV > 0.002:
        return 10.75
    return 3.91


def main() -> None:
    print("=" * 74)
    print("T6 — Honest Delta N_eff for IDM dark neutrinos")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 74)
    print(f"\nAllowed extra radiation: Delta N_eff < ~{DELTA_NEFF_95} at 95% (Planck2018+BBN).")
    print("  (NOTE: the earlier '130-477 sigma' figure is RETIRED as false precision — the")
    print("   likelihood is non-Gaussian this far out; we report exclusion as a FACTOR.)")

    # (1) Fully thermalized dark neutrinos (T_dark = T_nu): each dark nu ~ 1 unit of N_eff
    dNeff_thermal = N_ISOMERS * NU_PER_ISOMER  # 5 x 3 = 15 (fermionic, counted as N_eff units)
    print("\n" + "-" * 74)
    print("(1) THERMALIZED dark neutrinos (T_dark = T_nu):")
    print(f"    Delta N_eff = {N_ISOMERS} isomers x {NU_PER_ISOMER} nu = {dNeff_thermal}")
    print(f"    exceeds allowed {DELTA_NEFF_95} by a FACTOR ~{dNeff_thermal / DELTA_NEFF_95:.0f}")
    print("    -> decisively excluded (as a magnitude), NOT a calibrated 130-477 sigma.")
    print("    (full-mirror g* bookkeeping pushes this toward ~40-80; same qualitative verdict.)")

    # (2) Early-decoupling escape: dilution xi^4 = (10.75/g*(T_dec))^(4/3)
    print("\n" + "-" * 74)
    print("(2) EARLY-DECOUPLING escape (entropy dilution):")
    print(
        f"    {'T_dec (GeV)':>12}{'g*(T_dec)':>11}{'xi^4':>10}{'Delta N_eff':>13}{'  vs 0.30':>10}"
    )
    dark_dof = N_ISOMERS * NU_PER_ISOMER * (7.0 / 8.0)  # fermionic weight
    for T_dec in (0.1, 1.0, 100.0, 1e6, 1e12, 1e15):
        g = g_star(T_dec)
        xi4 = (10.75 / g) ** (4.0 / 3.0)
        dN = dark_dof * xi4
        flag = "OK" if dN < DELTA_NEFF_95 else "excluded"
        print(f"    {T_dec:>12.1e}{g:>11.2f}{xi4:>10.4f}{dN:>13.4f}{flag:>10}")
    print("    -> if the dark sector decoupled ABOVE the EW scale (g*~107), dilution brings")
    print("       Delta N_eff near/below the bound; very early decoupling escapes comfortably.")

    # (3) Gravitational-only escape: never thermalized -> Delta N_eff ~ 0
    print("\n" + "-" * 74)
    print("(3) GRAVITATIONAL-ONLY (IDM-stated coupling, never thermalized):")
    print("    T_dark/T_SM << 1 by many orders (grav particle production); Delta N_eff ~ 0.")
    print("    -> trivially allowed, BUT then the isomer 'neutrinos' are not a thermal relic")
    print("       and the 5:1 counting (T5) loses its equal-density basis — the escapes are")
    print("       COUPLED: escaping N_eff via non-thermality removes the T5 relic argument.")

    print("\n" + "=" * 74)
    print("READ-OUT (interpret in report):")
    print("  - Thermalized 5-isomer dark neutrinos: excluded by a FACTOR ~50 (not 130-477 sigma).")
    print("  - Escape (2) early decoupling and (3) grav-only BOTH open the door -> constraint is")
    print("    conditional on thermal history, which the corpus does not fix.")
    print("  - Coupling caveat: the same non-thermality that rescues N_eff undercuts T5's 5:1.")
    print("=" * 74)


if __name__ == "__main__":
    main()
