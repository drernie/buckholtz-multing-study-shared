"""t2_dipole_viability.py — MULTING dipole observational-viability window (docs/132 T2)

Question (separate from R011's H(z) fit): IF MULTING's dipole ~ Blanchet-Le Tiec dipolar DM
(0804.3518), is it observationally ALIVE? Map the window from two INHERITED constraints:
  (i)  exponential instability, characteristic time tau_g ~ 6e10 yr (0901.3114) — growth over
       a Hubble time must stay bounded;
  (ii) Planck 2nd-order primordial-dipole-field bound, s_eq <~ 1.5e-3 H^-1 (1312.6991).
beta is non-identifiable -> the amplitude edge is expressed as a constraint, not a fitted value.

NO fitting. Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_BRIDGE_FITTING.
Evidence: [VERIFIED-BASH] instability arithmetic; [WEAK-digitized] Blanchet/Planck numbers
(from literature/refs_digitized, prior-session reads — flagged for re-verification).
"""

from __future__ import annotations

from math import exp

T_HUBBLE_YR = 1.38e10  # age of universe
TAU_G_YR = 6.0e10  # Blanchet dipolar-DM instability characteristic time (0901.3114)
S_EQ_BOUND_HINV = 1.5e-3  # Planck primordial dipole-field bound, units of H^-1 (1312.6991)


def main() -> None:
    print("=" * 74)
    print("T2 — MULTING dipole observational-viability window (NO fitting)")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 74)

    # ── Constraint (i): instability growth over a Hubble time ──────────────────
    print("\n(i) INSTABILITY (Blanchet-Le Tiec dipolar DM, tau_g ~ 6e10 yr):")
    growth = exp(T_HUBBLE_YR / TAU_G_YR)
    print(
        f"    growth over one Hubble time = exp(t_H/tau_g) = exp({T_HUBBLE_YR / TAU_G_YR:.3f})"
        f" = {growth:.3f}"
    )
    print(
        f"    -> the unstable mode grows by ~{(growth - 1) * 100:.0f}% over the age of the universe;"
    )
    print("       marginally safe ONLY because tau_g > t_H. tau_g ∝ 1/sqrt(G rho) is set by the")
    print("       background density, so this edge is ~amplitude-INDEPENDENT (a yes/no, not a")
    print("       beta-tunable knob): the dipole is alive iff tau_g > t_H, which holds by ~4.3x.")
    # sensitivity: what density boost would make it unstable within t_H?
    #   tau ∝ rho^-1/2, so tau=t_H when rho boosted by (tau_g/t_H)^2
    rho_boost_to_kill = (TAU_G_YR / T_HUBBLE_YR) ** 2
    print(f"    sensitivity: local density > {rho_boost_to_kill:.0f}x background would push")
    print("       tau_g below t_H (cluster cores) -> instability could matter at small scales.")

    # ── Constraint (ii): Planck 2nd-order primordial-dipole bound ──────────────
    print("\n(ii) PLANCK 2nd-order primordial dipole bound (1312.6991):")
    print(f"    s_eq <~ {S_EQ_BOUND_HINV:.1e} H^-1  -> UPPER edge of the amplitude band.")
    print("    Dipolar DM is degenerate with LCDM at FIRST order (0804.3518) -> only the 2nd-order")
    print("    amplitude is constrained; below this bound the dipole is observationally alive.")

    # ── The band ───────────────────────────────────────────────────────────────
    print("\n" + "-" * 74)
    print("VIABILITY BAND (structure):")
    print("  lower edge : dipole non-negligible (produces a distinguishable 2nd-order signal)")
    print("  upper edge : dipole amplitude below Planck s_eq bound AND tau_g > t_H")
    print("  status     : NON-EMPTY in Blanchet's own realization — dipolar DM survives as a")
    print("               viable-but-tightly-constrained model (alive at 1st order by degeneracy,")
    print("               marginally instability-safe, primordial amplitude Planck-bounded).")
    print("\n  MULTING-SPECIFIC edges in terms of beta/eta = BLOCKED:")
    print("    mapping s_eq <-> MULTING beta_d requires the F_oP->H(z) bridge (Q005), which is")
    print("    Tier-B blocked (BETA-1, non-identifiable beta). So we can state the band EXISTS")
    print("    and inherit its Blanchet edges, but cannot place MULTING's beta inside it without")
    print("    the bridge. This is the honest partial result: window alive, beta-location blocked.")
    print("=" * 74)


if __name__ == "__main__":
    main()
