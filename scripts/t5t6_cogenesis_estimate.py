"""t5t6_cogenesis_estimate.py — Order-of-magnitude T5<->T6 coupling window check.

Question (docs/132 T5+T6 joint): the 5-isomer IDM postulate needs BOTH
  (T5) a mechanism setting each dark isomer's number density so Omega_DM/Omega_b ~ 5.36
  (T6) Delta N_eff from the dark relativistic species within the Planck+BBN bound (~0.3).
The T6 script worried these ESCAPES are COUPLED: escaping N_eff via non-thermality
(regime 3) removes the shared-thermal-history that could enforce n_i ~ n_b (T5).

This toy tests whether that worry is fatal. It does NOT build a Boltzmann solver
(explicitly out of scope). It asks ONE order-of-magnitude question: if the dark
isomer sectors are REHEATED to a temperature ratio xi = T_dark/T_SM < 1 by the decay
of a common parent (NOT by thermal contact with the SM), what xi keeps Delta N_eff
within bound for 5 sectors -- and is that decoupling-not-equilibrium picture a real,
published mechanism?

Literature anchor [VERIFIED-WEBFETCH 2026-07-22, arXiv:2206.11314, Easa-Gregoire-
Stolarski-Cosme, PRD 109 075003]: a common "reheaton" (weak-scale Dirac fermion
carrying lepton number) decays into N SM-like hidden sectors, TRANSFERRING its
asymmetry to each WITHOUT thermalizing them with the SM; kinematic suppression
reheats hidden sectors to xi<1, giving Omega_DM/Omega_b~5 AND Delta N_eff >~ 0.05.
That is an existence proof that (a) asymmetry-sharing and (b) N_eff-safety coexist.

NO fitting. Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION.
Evidence: [VERIFIED-BASH] arithmetic; [WEAK] dof bookkeeping (order-of-magnitude).
"""

from __future__ import annotations

DELTA_NEFF_BOUND = 0.30  # representative Planck2018+BBN 95% cap on extra N_eff
N_ISOMERS = 5
NU_PER_ISOMER = 3  # each isomer replicates 3 SM neutrino species (paper Sec 4.4)


def delta_neff(xi: float, include_dark_photon: bool = True) -> float:
    """Delta N_eff from N_ISOMERS dark sectors at temperature ratio xi = T_dark/T_SM.

    Anchor: a FULLY thermalized dark sector (xi=1) of 5 isomers x 3 neutrinos
    contributes ~15 N_eff units (t6_neff_honest.py, regime 1). Energy density of
    relativistic species scales as T^4, so Delta N_eff(xi) ~ 15 * xi^4 for the
    neutrino content. Dark photons (2 bosonic dof per sector) add an O(1) correction;
    counted here as +N_ISOMERS * (8/7) * xi^4 in N_eff units for a rough upper edge.
    Both pieces are order-of-magnitude -- the verdict does not hinge on the 2nd decimal.
    """
    neutrino_piece = N_ISOMERS * NU_PER_ISOMER * xi**4  # 15 * xi^4
    photon_piece = N_ISOMERS * (8.0 / 7.0) * xi**4 if include_dark_photon else 0.0
    return neutrino_piece + photon_piece


def max_xi_for_bound(bound: float = DELTA_NEFF_BOUND) -> float:
    """Solve delta_neff(xi) = bound for xi (closed form: delta_neff = C * xi^4)."""
    c = delta_neff(1.0)  # coefficient of xi^4
    return (bound / c) ** 0.25


def main() -> None:
    print("=" * 74)
    print("T5<->T6 coupling window — order-of-magnitude toy (NOT a Boltzmann solver)")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 74)

    c = delta_neff(1.0)
    print(f"\nThermalized (xi=1) Delta N_eff for {N_ISOMERS} isomers = {c:.1f} N_eff units")
    print(
        f"  -> excluded by factor ~{c / DELTA_NEFF_BOUND:.0f} over the ~{DELTA_NEFF_BOUND} bound."
    )

    print(f"\n{'xi = T_dark/T_SM':>18}{'Delta N_eff':>14}{'  vs 0.30':>12}")
    for xi in (1.0, 0.6, 0.5, 0.4, 0.376, 0.3, 0.2, 0.1):
        dn = delta_neff(xi)
        flag = "OK" if dn <= DELTA_NEFF_BOUND else "excluded"
        print(f"{xi:>18.3f}{dn:>14.3f}{flag:>12}")

    xi_max = max_xi_for_bound()
    print(f"\nRequired xi_max (Delta N_eff <= {DELTA_NEFF_BOUND}) = {xi_max:.3f}")
    print("  -> the 5 dark sectors must be reheated to T_dark <~ 0.3-0.4 T_SM.")
    print("     This is a MILD suppression: a parent that dumps most of its energy into")
    print("     the SM (kinematic branching) reaches it easily.")

    print("\n" + "-" * 74)
    print("KEY POINT — the escapes are NOT mutually exclusive:")
    print("  The T6 script feared: non-thermality (needed for N_eff) removes the shared")
    print("  thermal history (needed to set n_i). But asymmetry-sharing does NOT require")
    print("  thermal EQUILIBRIUM -- it can be a one-shot TRANSFER by a decaying parent.")
    print("  A parent decaying into all 5 sectors imprints their asymmetries AND reheats")
    print(f"  them to xi<{xi_max:.2f} in the same event. Sharing != equilibration.")
    print("  Published existence proof: arXiv:2206.11314 (PRD 109 075003) does exactly")
    print("  this for N SM-like sectors -> Omega_DM/Omega_b~5 AND Delta N_eff~0.05.")

    print("\n" + "-" * 74)
    print("BUT — what 2206.11314 does NOT supply for the IDM postulate:")
    print("  Its ~5 comes from differential SPHALERON efficiency across N~1e4-1e8 sectors")
    print("  with DIFFERENT Higgs masses (N-naturalness), NOT from 5 IDENTICAL sectors")
    print("  each at n_i ~ n_b. The IDM 'each isomer = one visible baryon density' ansatz")
    print("  is a DIFFERENT internal structure than any surveyed mechanism produces.")

    print("\n" + "=" * 74)
    print("READ-OUT (interpret in report):")
    print("  - Coupling is NOT structurally fatal: a decaying-parent cogenesis threads")
    print("    both constraints (existence proof 2206.11314). -> not FAIL.")
    print("  - N_eff needs xi <~ 0.3-0.4 for 5 sectors: mild, achievable by asymmetric")
    print("    reheating that ALSO shares the asymmetry.")
    print("  - The SPECIFIC '5 identical sectors, each n_i=n_b' realization is unaddressed")
    print("    in the surveyed literature. -> verdict OPEN for the IDM ansatz.")
    print("=" * 74)


if __name__ == "__main__":
    main()
