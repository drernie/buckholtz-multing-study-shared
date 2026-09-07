"""P209 -- the first numerical constraint on the invariant eta = kappa/g.

KG2 (FINDING_P52 Part 7) asks for NUMERICAL VALUES of the invariants.
FINDING_P24 established eta = kappa/g as the sole invariant controlling
every cross-sector force ratio, and states explicitly that it "does not
give eta a numeric value." FINDING_P103 proved the DERIVATION route
unavailable and left the MEASUREMENT route open. FINDING_P25 derived the
Eotvos closed form and named exactly what was missing (its own section 4
item 1): a real EP bound, and the composition contrast.

P208 supplied the missing algebra: at leading order

    eta_Eotvos = 2 * eta * |Delta_psi| / r,     psi_i = K_i r_i / (M_i c^2)

This script supplies the external number.

PRIMARY RESULT is assumption-free given P208's reduction: a bound on the
PRODUCT eta * |Delta_psi|. Converting that to a bound on eta alone needs
the composition contrast, which MULTING does not fix -- so the secondary
table below is explicitly labelled ILLUSTRATIVE and is NOT a measurement.

Gate 2 (target provenance): MICROSCOPE's number is a real published
measurement, not a fit to anything of ours, and it never saw this model.

CORRECTIONS APPLIED AFTER STEP 8a (no-silent-correction):
 - the "~2 sigma" bound is a QUADRATURE convention; the spread across
   defensible alternatives is quantified below rather than hidden;
 - the illustrative table's original top row (|Delta_psi| = 1 m) was
   UNPHYSICAL -- it needs k-energy ~10x rest energy for a lab test mass --
   and is removed; a hard physical cap is asserted instead;
 - the validity check leans on a cluster-derived proxy for psi_A, drawn
   from the same OPEN block that makes Delta_psi unknown. The factor of
   safety before it breaks is now computed, not asserted.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import math

# --- External datum, [VERIFIED-arXiv] ---------------------------------
# Touboul et al., "MICROSCOPE mission: final results of the test of the
# Equivalence Principle", arXiv:2209.15487, abstract fetched this session:
#   eta(Ti, Pt) = [-1.5 +/- 2.3 (stat) +/- 1.5 (syst)] x 10^-15 at 1 sigma
ETA_E_CENTRAL = -1.5e-15
ETA_E_STAT = 2.3e-15
ETA_E_SYST = 1.5e-15

# MICROSCOPE flew a low Earth orbit. The exact altitude is NOT quoted in
# any abstract fetched here, so r is treated as bounded rather than known:
# any LEO lies between the Earth's radius and ~1000 km above it. The 16%
# spread is negligible against the orders-of-magnitude uncertainty in
# Delta_psi, so it does not drive the result.
R_EARTH_M = 6.371e6
R_MIN_M = R_EARTH_M
R_MAX_M = R_EARTH_M + 1.0e6
R_NOMINAL_M = 7.1e6  # [WEAK] nominal LEO value used for the headline number

# Physical cap on psi. psi_i = (K_i/c^2) * r_i / M_i, so a body whose
# k-energy does not exceed its rest energy has (K_i/c^2)/M_i <= 1 and
# therefore psi_i <= r_i, its own size. MICROSCOPE's test masses are of
# order 0.1 m.
PSI_CAP_M = 0.1


def combined_sigma() -> float:
    return math.hypot(ETA_E_STAT, ETA_E_SYST)


def eta_e_upper_bound(n_sigma: float, *, quadrature: bool = True) -> float:
    """Conservative one-sided upper bound on |eta_Eotvos| at n sigma.

    For a central value of definite sign, |mu| + n*sigma equals
    max(|mu + n sigma|, |mu - n sigma|), so this does not double-count.
    """
    sigma = combined_sigma() if quadrature else (ETA_E_STAT + ETA_E_SYST)
    return abs(ETA_E_CENTRAL) + n_sigma * sigma


def product_bound(eta_e_max: float, r_m: float) -> float:
    """eta * |Delta_psi| <= eta_Eotvos^max * r / 2, in metres. From P208."""
    return eta_e_max * r_m / 2.0


def section(t: str) -> None:
    print(f"\n{'=' * 70}\n{t}\n{'=' * 70}")


def main() -> int:  # noqa: PLR0915  (linear report script, read top to bottom)
    section("P209 -- first numerical constraint on eta = kappa/g")

    sig = combined_sigma()
    print("\nMICROSCOPE final result [VERIFIED-arXiv 2209.15487]:")
    print(
        f"  eta(Ti,Pt) = {ETA_E_CENTRAL:+.1e} +/- {ETA_E_STAT:.1e}(stat) +/- {ETA_E_SYST:.1e}(syst)"
    )
    print(f"  combined 1 sigma (quadrature): {sig:.3e}")

    assert sig > max(ETA_E_STAT, ETA_E_SYST), "quadrature sum must exceed each term"
    assert sig < ETA_E_STAT + ETA_E_SYST, "quadrature sum must be below the linear sum"
    print("  PC1 [positive control] quadrature lies between max and sum. PASSES.")

    # PC2 -- the |mu| + n*sigma construction must equal the two-sided max,
    # or it would be double-counting the central value. Asserted, not argued.
    b2 = eta_e_upper_bound(2.0)
    two_sided = max(abs(ETA_E_CENTRAL + 2 * sig), abs(ETA_E_CENTRAL - 2 * sig))
    print(f"  PC2 [positive control] |mu|+2s = {b2:.4e} vs two-sided max {two_sided:.4e}")
    assert math.isclose(b2, two_sided, rel_tol=1e-12), "the bound double-counts the central value"
    print("       identical -- no double-counting. PASSES.")

    # --- PRIMARY RESULT ----------------------------------------------------
    section("PRIMARY -- bound on the PRODUCT (no extra assumptions)")
    prod = product_bound(b2, R_NOMINAL_M)
    prod_lo = product_bound(b2, R_MIN_M)
    prod_hi = product_bound(b2, R_MAX_M)
    print(f"\n  eta * |Delta_psi|  <=  {prod:.2e} m      (r = {R_NOMINAL_M:.2e} m)")
    print(f"  orbit-radius sensitivity: [{prod_lo:.2e}, {prod_hi:.2e}] m over any LEO")
    print(f"  -> a {100 * (prod_hi / prod_lo - 1):.0f}% spread. Not the limiting uncertainty.")

    lin = eta_e_upper_bound(2.0, quadrature=False)
    prod_lin = product_bound(lin, R_NOMINAL_M)
    print("\n  Convention check: adding stat+syst LINEARLY instead gives")
    print(f"  {prod_lin:.2e} m, i.e. {prod_lin / prod:.2f}x looser -- well under a factor of 2.")

    # --- Validity of the leading-order form --------------------------------
    section("Validity of P208's leading-order reduction")
    print("  P208: the kappa^2 piece is negligible while |3 * eta * psi_A / r| << 1,")
    print("  psi_A = the SOURCE body's own K r / (M c^2).")
    k_over_m = 1.00e12 / 3.16e14  # z=0 cluster row, audit/range_underdetermination.py
    psi_earth = k_over_m * R_EARTH_M
    crit = 3.0 * psi_earth / R_NOMINAL_M
    print(f"    cluster (K/c^2)/M ~ {k_over_m:.3e}  ->  psi_Earth ~ {psi_earth:.3e} m")
    print(f"    3*psi_A/r = {crit:.3e}, so the form would hold for eta << {1 / crit:.0f}")
    assert crit < 1.0, "leading-order form would not be self-consistent"

    psi_break = R_NOMINAL_M / 3.0
    margin = psi_break / psi_earth
    print("\n  CIRCULARITY CAVEAT: psi_Earth here is estimated from the CLUSTER")
    print("  (K/c^2)/M ratio -- drawn from the same OPEN block that makes")
    print("  Delta_psi unknown in the first place. The check would fail at")
    print(f"  psi_A ~ {psi_break:.2e} m, i.e. if Earth's true ratio exceeds the")
    print(f"  cluster proxy by a factor ~{margin:.0f}. For a quantity the model")
    print("  leaves OPEN that is not a large margin -- so the leading-order")
    print("  form is CONDITIONAL, not established.")

    # --- SECONDARY, EXPLICITLY ILLUSTRATIVE --------------------------------
    section("SECONDARY -- what eta would be bounded to, per assumed contrast")
    print("  ILLUSTRATIVE ONLY. Converting the product bound into a bound on eta")
    print("  needs |Delta_psi| for Ti vs Pt. MULTING does not fix it:")
    print("  MODEL_SPEC_AUDIT.md flags the k_A,k_P row as OPEN, 'postulate, not")
    print("  sharply defined'. These rows are NOT measurements of eta.")
    print(f"\n  Physical cap: |Delta_psi| <= {PSI_CAP_M} m for ~0.1 m test masses,")
    print("  since K/(M c^2) <= 1 implies psi <= the body's own radius.\n")
    print(f"  {'|Delta_psi| [m]':>18s} {'eta <=':>12s}   reading")
    rows = [
        (1.0e-1, "hard cap: k-energy = rest energy, whole-body contrast"),
        (1.0e-2, "test-mass scale, order-unity composition contrast"),
        (1.0e-4, "test-mass scale x cluster (K/c^2)/M ratio"),
        (1.0e-7, "that, times a per-mille composition effect"),
        (1.0e-9, "nanometre-scale contrast"),
    ]
    assert max(d for d, _ in rows) <= PSI_CAP_M, "a tabulated row exceeds the physical cap"
    for dpsi, reading in rows:
        print(f"  {dpsi:18.1e} {prod / dpsi:12.2e}   {reading}")

    print("\n  Read the table in the falsifying direction: a LARGE contrast gives")
    print("  a TIGHT bound on eta. The k-sector escapes MICROSCOPE only if the")
    print("  contrast is small -- which is P25's own 'K/M universality' escape,")
    print("  now quantified rather than merely named.")
    print("\n  Quote the BAND, never one row: over the physical range")
    print(f"  1e-9 m <= |Delta_psi| <= {PSI_CAP_M} m, the implied cap on eta runs")
    print(f"  from {prod / PSI_CAP_M:.1e} to {prod / 1.0e-9:.1e}. A single row lifted out")
    print("  of this table would be a fit presented as a measurement (Gate 2).")

    section("ANSWER TO KG2, FOR eta")
    print("  eta is still NOT numerically determined. But it is, for the first")
    print("  time in this project, numerically CONSTRAINED by a real experiment:")
    print()
    print(f"      eta * |Delta_psi|  <=  {prod:.2e} m")
    print("      [MICROSCOPE, ~2 sigma, stat+syst in quadrature]")
    print()
    print("  FINDING_P24 said it 'does not give eta a numeric value.' That")
    print("  remains true of P24. This is the first external number that bears")
    print("  on eta at all -- and it bears on a product, not on eta alone.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
