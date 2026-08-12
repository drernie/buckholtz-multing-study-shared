"""P18: FINDING_P17 found that Omega_phi (P14's cosmological energy-density
fraction) is not dimensionless -- a missing field-normalization constant is
silently assumed =1. Does that SAME gap also undermine FINDING_P15/
FINDING_P16's central conclusion (self-energy dominates cross-terms for
realistic discrete clusters), or are those -- being RATIOS -- immune?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12, corrected 2026-08-12 after context-blind skeptic review.
Direct follow-up to FINDING_P17's correction.

kappa's cancellation from the ratio is UNCONDITIONAL: p_i = kappa*k_i*r_i/
c^2 is linear in kappa, so both E_self~p_i^2 and U_cross~p_i*p_j scale as
kappa^2, and kappa drops out of the ratio regardless of anything else.
Verified symbolically, genuinely proven.

The missing-normalization-constant (C) cancellation is CONDITIONAL, not
unconditional -- [CORRECTED after skeptic review: an earlier draft of this
docstring claimed it holds for "any value of C", which oversold what a
tautological substitution actually shows]. IF the missing constant is a
pure, r_min-independent overall multiplier (phi -> C*phi uniformly), THEN
it cancels -- this is the physically plausible first guess, analogous to a
Green's-function/propagator normalization (like 1/(4*pi*eps0) in
electrostatics), which would indeed apply identically to E_self and
U_cross. But it is NOT independently derived from the action here, and it
would NOT hold if the actual missing physics is closer to a renormalization
counterterm for E_self's own UV divergence (E_self diverges as r_min->0,
the classic signature of a quantity needing renormalization) that does not
act the same way on the IR-finite, well-separated U_cross(d). Part 3 below
makes this condition explicit with a sensitivity check, rather than hiding
it inside an assumption baked into Parts 1-2's own setup.
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
    print("  -> C cancels exactly IF C acts as a pure overall multiplier on phi, as")
    print("     assumed above (E_self_true=C^2*E_self_raw, U_cross_true=C^2*U_cross_")
    print("     raw). [CORRECTED after skeptic review:] this is the setup's own")
    print("     premise, not yet a proof for an arbitrary/unknown C -- see Part 3")
    print("     for the condition under which this actually holds.")

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

    print("\n[PART 3 -- CORRECTED after skeptic review] Sensitivity check: does the")
    print("  C-cancellation in Part 1 require C to be a PURE multiplicative constant,")
    print("  or does it survive a more general fix (e.g. one that also depends on")
    print("  r_min, the way a renormalization counterterm for E_self's own UV")
    print("  divergence as r_min->0 plausibly would, without touching the IR-finite")
    print("  U_cross(d) the same way)?")
    alpha = sp.Symbol("alpha", real=True)
    e_self_alpha = C**2 * r_min**alpha * e_self_raw(p1, r_min)
    u_cross_alpha = C**2 * u_cross_collinear_raw(p1, p2, d)  # cross has no r_min dependence to fix
    ratio_alpha = sp.simplify(u_cross_alpha / e_self_alpha)
    print(f"  ratio, general r_min-power alpha in the fix: {ratio_alpha}")
    print(f"  -> r_min survives in the ratio for alpha!=0: {r_min in ratio_alpha.free_symbols}")
    print("  Part 1's cancellation is therefore CONDITIONAL on alpha=0 (a pure overall")
    print("  constant, uniform across both formulas) -- NOT proven for 'any C' in the")
    print("  unqualified sense the first draft of this script claimed.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("[CORRECTED after skeptic review.] The kappa-cancellation (Part 2) is")
    print("UNCONDITIONAL -- kappa enters both formulas linearly through p_i with no")
    print("complication, verified for real. The C-cancellation (Part 1) is")
    print("CONDITIONAL on the missing normalization constant being a pure, r_min-")
    print("independent overall multiplier (Part 3 shows this explicitly) -- a")
    print("physically plausible first guess (analogous to a Green's-function/")
    print("propagator normalization, like 1/(4*pi*eps0) in electrostatics, which")
    print("would indeed apply identically to both formulas), but NOT independently")
    print("derived from the action, and NOT true if the actual fix is closer to a")
    print("renormalization counterterm for E_self's own UV divergence (r_min->0)")
    print("that does not act the same way on the IR-finite, well-separated U_cross.")
    print("Consequence, split cleanly by claim type:")
    print()
    print("  RATIO-based claims (FINDING_P15/P16: self-energy DOMINATES cross-")
    print("  terms by such-and-such factor, at realistic cluster separations)")
    print("  -> UNAFFECTED by kappa (unconditionally). Unaffected by the missing")
    print("     constant C ONLY IF C is a pure overall multiplier -- plausible, not")
    print("     proven. If C instead carries r_min-dependent structure (Part 3), the")
    print("     ratio would NOT be immune.")
    print()
    print("  ABSOLUTE-MAGNITUDE claims (FINDING_P14's Omega_phi numeric value,")
    print("  FINDING_P17's kappa_cosmo_bound numeric value)")
    print("  -> REMAIN BLOCKED by both open problems (kappa unfixed AND C")
    print("     unfixed) -- this finding does not resolve either.")


if __name__ == "__main__":
    main()
