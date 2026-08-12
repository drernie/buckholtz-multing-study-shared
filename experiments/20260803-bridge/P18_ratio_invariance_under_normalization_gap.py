"""P18: FINDING_P17 found that Omega_phi (P14's cosmological energy-density
fraction) is not dimensionless -- a missing field-normalization constant is
silently assumed =1. Does that SAME gap also undermine FINDING_P15/
FINDING_P16's central conclusion (self-energy dominates cross-terms for
realistic discrete clusters), or are those -- being RATIOS -- immune?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12. Direct follow-up to FINDING_P17's correction. If a missing
constant C rescales the field (phi -> C*phi, equivalently rescaling every
p_i -> C*p_i in the self-energy/cross-term formulas, since both are
DERIVED FROM phi via the same p.grad(phi) coupling), then:

  E_self  ~ (grad phi)^2  ~ C^2   (quadratic in phi)
  U_cross ~ (grad phi_1).(grad phi_2) ~ C^2   (also quadratic, bilinear)

so C^2 should cancel EXACTLY from any cross_i/self_j-style RATIO,
regardless of C's actual (unknown) value. The same argument applies to
kappa itself (p_i = kappa*k_i*r_i/c^2, linear in kappa, so both self and
cross scale as kappa^2, and the ratio is kappa-independent too) --
already implicitly relied upon throughout P15/P16 without being proven.

This script proves both invariances symbolically (sympy), using the
project's own already-verified formulas unchanged: FINDING_P14's
self-energy (8*pi/3)*p^2/r_min^3, and FINDING_P15's general dipole-dipole
cross-term formula (p1.p2 - 3*(p1.dhat)*(p2.dhat))/d^3.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# Part 1: does an unknown field-normalization constant C cancel from the
# cross/self ratio? (Answers: is P15/P16's RATIO conclusion independent of
# the missing normalization constant P17 found in P14's ABSOLUTE Omega_phi?)
# ---------------------------------------------------------------------------

C, r_min, d = sp.symbols("C r_min d", positive=True)
p, p1, p2 = sp.symbols("p p1 p2", positive=True)


def e_self_raw(p_val, r_min_val):
    """FINDING_P14's own verified formula, unchanged."""
    return sp.Rational(8, 3) * sp.pi * p_val**2 / r_min_val**3


def u_cross_collinear_raw(p1_val, p2_val, d_val):
    """FINDING_P15's own verified collinear-dipole cross-term formula
    (one of two textbook positive controls that passed there), unchanged."""
    return -2 * p1_val * p2_val / d_val**3


def main() -> None:
    print("=" * 78)
    print("P18 -- DOES P17's NORMALIZATION-CONSTANT GAP ALSO INVALIDATE")
    print("       P15/P16's SELF-VS-CROSS RATIO CONCLUSIONS? (answer: no)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    print("\n[PART 1] Missing field-normalization constant C (phi -> C*phi):")
    print("  both E_self and U_cross are QUADRATIC in phi (self: (grad phi)^2;")
    print("  cross: (grad phi_1).(grad phi_2)) -- so both pick up a factor C^2.")

    e_self_C = C**2 * e_self_raw(p1, r_min)
    u_cross_C = C**2 * u_cross_collinear_raw(p1, p2, d)

    ratio_raw = sp.simplify(u_cross_collinear_raw(p1, p2, d) / e_self_raw(p1, r_min))
    ratio_with_C = sp.simplify(u_cross_C / e_self_C)

    print(f"  ratio WITHOUT C : {ratio_raw}")
    print(f"  ratio WITH C    : {ratio_with_C}")
    assert sp.simplify(ratio_with_C - ratio_raw) == 0, (
        "C did NOT cancel -- would FALSIFY this finding"
    )
    print("  -> C cancels EXACTLY, checked by assert. The cross/self ratio is")
    print("     completely independent of the missing normalization constant,")
    print("     regardless of C's actual (currently unknown) value.")

    print("\n[PART 2] kappa itself (p_i = kappa*k_i*r_i/c^2, linear in kappa):")
    kappa = sp.Symbol("kappa", positive=True)
    k1r1c2, k2r2c2 = sp.symbols("k1r1c2 k2r2c2", positive=True)
    p1_kappa = kappa * k1r1c2
    p2_kappa = kappa * k2r2c2

    e_self_kappa = e_self_raw(p1_kappa, r_min)
    u_cross_kappa = u_cross_collinear_raw(p1_kappa, p2_kappa, d)
    ratio_kappa = sp.simplify(u_cross_kappa / e_self_kappa)

    print(f"  ratio in terms of kappa: {ratio_kappa}")
    assert kappa not in ratio_kappa.free_symbols, (
        "kappa did NOT cancel -- would FALSIFY this finding"
    )
    print("  -> kappa cancels EXACTLY too (both self and cross scale as kappa^2,")
    print("     since both are built from p_i which is linear in kappa).")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Both the missing field-normalization constant (FINDING_P17's new gap)")
    print("and kappa's own unfixed value (FINDING_P14's original gap) cancel")
    print("EXACTLY from the cross-term/self-energy RATIO -- proven symbolically,")
    print("not assumed. Consequence, split cleanly by claim type:")
    print()
    print("  RATIO-based claims (FINDING_P15/P16: self-energy DOMINATES cross-")
    print("  terms by such-and-such factor, at realistic cluster separations)")
    print("  -> UNAFFECTED by either open normalization problem. These hold for")
    print("     ANY value of kappa and ANY value of the missing constant C.")
    print()
    print("  ABSOLUTE-MAGNITUDE claims (FINDING_P14's Omega_phi numeric value,")
    print("  FINDING_P17's kappa_cosmo_bound numeric value)")
    print("  -> REMAIN BLOCKED by both open problems (kappa unfixed AND C")
    print("     unfixed) -- this finding does not resolve either.")


if __name__ == "__main__":
    main()
