"""t5_relic_abundance.py — Is the 5:1 dark/baryon ratio a relic PREDICTION or arithmetic?
(docs/132 task T5; R003; facts.json Q006 cross_domain note; docs/122 v2 point 3)

The claim: Omega_DM/Omega_b = 5 x 1.074 = 5.37 ~= 5.36 (Planck).
Exact decomposition (no approximation):
    Omega_DM/Omega_b = sum_i (m_i/m_b) (n_i/n_b)      (i over dark isomers)
The isomer postulate fixes the COUNT (5) and, via masses, the m_i/m_b factors. It does NOT
fix the NUMBER-DENSITY ratios n_i/n_b — those come from a reheating/relic-abundance history
the corpus does not provide. This script quantifies how fine-tuned the n_i/n_b must be to hit
5.36, and contrasts with the asymmetric/mirror-DM route (Berezhiani) where the same number is
a derived band, not a counting coincidence.

NO fitting. Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION.
Evidence: [VERIFIED-BASH] arithmetic; [WEAK] literature comparison (cited).
"""

from __future__ import annotations

PLANCK_RATIO = 5.364  # Omega_c/Omega_b, Planck 2018
PLANCK_SIGMA = 0.065
MEAN_ISOMER_MASS = 1.074  # mean dark-isomer mass in proton-mass units (paper)
N_ISOMERS = 5


def main() -> None:
    print("=" * 74)
    print("T5 — 5:1 dark/baryon ratio: relic prediction or arithmetic?")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 74)

    counting = N_ISOMERS * MEAN_ISOMER_MASS
    pull = (counting - PLANCK_RATIO) / PLANCK_SIGMA
    print(f"\nInteger counting: {N_ISOMERS} isomers x {MEAN_ISOMER_MASS} m_p = {counting:.3f}")
    print(f"Planck Omega_c/Omega_b = {PLANCK_RATIO} +- {PLANCK_SIGMA}")
    print(f"  -> {counting - PLANCK_RATIO:+.3f}  ({pull:+.2f} sigma from Planck)")

    # What sum of number-density ratios is REQUIRED to hit Planck exactly?
    sum_n_required = PLANCK_RATIO / MEAN_ISOMER_MASS
    per_isomer_n = sum_n_required / N_ISOMERS
    print(f"\nRequired sum_i (n_i/n_b) to hit 5.364 = {sum_n_required:.4f}")
    print(f"If equal across {N_ISOMERS} isomers: each n_i/n_b = {per_isomer_n:.4f}")
    print("  -> the postulate's '5' works ONLY if every dark isomer has n_i ~= n_b (equal")
    print("     number density to the visible baryon sector). This is an ASSUMPTION, not derived.")

    # Fine-tuning: how tightly must per-isomer n_i/n_b be controlled to stay within Planck?
    # d(ratio) = N * m_bar * d(n_i/n_b)  (equal perturbation each sector)
    tol_per_isomer = PLANCK_SIGMA / (N_ISOMERS * MEAN_ISOMER_MASS)
    print(f"\nFine-tuning: to keep the ratio within Planck +-{PLANCK_SIGMA}, each n_i/n_b must be")
    print(
        f"  1.000 +- {tol_per_isomer:.4f}  (i.e. controlled to ~{tol_per_isomer * 100:.1f}% per sector)."
    )
    print("  No isomer-level baryogenesis / thermal history in the corpus supplies this")
    print("  (facts.json Q006, m7_b audit). Gravitational-only production (T6 regime 3) makes")
    print("  the sectors NON-thermal, so equal n_i is not a natural freeze-out outcome either.")

    # Asymmetric-DM / mirror-DM contrast
    print("\n" + "-" * 74)
    print("Contrast: asymmetric/mirror-DM route (Berezhiani; ADM 2512.14119 lead)")
    print("  Omega_DM/Omega_b = (m_DM/m_b) x (eta_DM/eta_b).")
    for eta in (4.0, 5.0, 6.0):
        print(f"    m_DM~m_p, eta_DM/eta_b={eta:.0f} -> ratio = {1.074 * eta:.2f}")
    print("  In mirror/ADM models eta_DM/eta_b is a DERIVED consequence of the shared")
    print("  baryon-asymmetry mechanism + temperature ratio (a predicted O(1-10) band), NOT a")
    print("  free per-sector choice. The 5-isomer counting instead POSITS eta_DM/eta_b=5 exactly")
    print("  (5 sectors each equal to visible) with no generating mechanism.")

    print("\n" + "=" * 74)
    print("READ-OUT (interpret in report):")
    print("  - Hitting 5.36 needs n_i/n_b = 1 to ~1% per sector, with no mechanism providing it.")
    print("  - That is a tuned arithmetic coincidence, NOT a relic prediction, UNLESS TJB")
    print("    supplies an isomer-level reheating/relic-abundance derivation fixing n_i = n_b.")
    print("  - Mirror/ADM already DERIVES ~5:1 from asymmetry+temperature -> a competing,")
    print("    mechanistically grounded explanation of the same number.")
    print("=" * 74)


if __name__ == "__main__":
    main()
