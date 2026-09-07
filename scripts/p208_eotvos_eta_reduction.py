"""P208 -- reduce FINDING_P25's exact Eotvos expression to the invariant eta.

KG2 (FINDING_P52, Part 7) asks for NUMERICAL VALUES of the invariants,
not merely which combinations are meaningful. FINDING_P103 proved the
DERIVATION route unavailable for this completion's absolute scale, and
explicitly left the MEASUREMENT route open ("at best they could measure
it against external data -- a different, still-open question this file
does not resolve either").

FINDING_P25 derived a closed form for the Eotvos parameter of the
k-sector and named, in its own section 4 item 1, exactly what was missing
for a number: "(a) a real, independently-verified experimental EP-bound
(e.g. MICROSCOPE's actual reported sensitivity) and (b) a real or
estimated value for how K_i*r_i/M_i varies across ordinary laboratory
materials -- neither attempted here."

This script does the step that must come BEFORE any external number: it
takes P25's own accelerations and asks what the Eotvos ratio actually
depends on. If the reduction below holds, an EP bound constrains the
parameters ONLY through the invariant eta = kappa/g -- which is the
thing KG2 asks about.

WHAT IS AND IS NOT A CHECK ON FINDING_P206 (corrected after Step 8a; the
first draft overclaimed here). Every term of P25's acceleration is linear
in A, so ANY ratio of two accelerations is A-independent by construction.
"A cancels" is therefore the input structure propagated forward, NOT an
independent confirmation of anything. What IS derived, and was not
guaranteed, is that g survives only inside eta = kappa/g: both terms of
the kappa^1 piece could in principle have left g outside that ratio, and
they conspire not to.

Nothing here is fitted, and no external datum is used. Pure algebra.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import sympy as sp

# --- P25's own symbols -------------------------------------------------
A, g, kap, c, r = sp.symbols("A g kappa c r", positive=True)
M_A, K_A, r_A = sp.symbols("M_A K_A r_A", positive=True)
M1, K1, r1 = sp.symbols("M_1 K_1 r_1", positive=True)
M2, K2, r2 = sp.symbols("M_2 K_2 r_2", positive=True)


def accel(M_i: sp.Symbol, K_i: sp.Symbol, r_i: sp.Symbol) -> sp.Expr:
    """FINDING_P25 section 2's own a_1, transcribed verbatim.

    a = A M_A g^2 / r^2  - 2 A g kappa K_A r_A / (c^2 r^3)
        + K_i * [ 6 A kappa^2 K_A r_i r_A / (M_i c^4 r^4)
                  - 2 A g kappa M_A r_i / (M_i c^2 r^3) ]
    """
    comp_independent = A * M_A * g**2 / r**2 - 2 * A * g * kap * K_A * r_A / (c**2 * r**3)
    comp_dependent = K_i * (
        6 * A * kap**2 * K_A * r_i * r_A / (M_i * c**4 * r**4)
        - 2 * A * g * kap * M_A * r_i / (M_i * c**2 * r**3)
    )
    return comp_independent + comp_dependent


def section(t: str) -> None:
    print(f"\n{'=' * 70}\n{t}\n{'=' * 70}")


def main() -> int:
    a1 = accel(M1, K1, r1)
    a2 = accel(M2, K2, r2)

    section("P208 -- what does P25's Eotvos ratio actually depend on?")

    # ---- PC1: composition-independent part must cancel from the difference
    d = sp.simplify(a1 - a2)
    pc1 = sp.simplify(d.subs({K1: 0, K2: 0}))
    print(f"\nPC1 [positive control] (a1 - a2) with K_1 = K_2 = 0  ->  {pc1}")
    assert pc1 == 0, "composition-independent part failed to cancel"
    print("     reproduces P25's own stated control. PASSES.")

    # ---- PC2: universal K r / M must also cancel (P25's own second control)
    psi = sp.Symbol("psi", positive=True)  # common value of K_i r_i /(M_i c^2)
    pc2 = sp.simplify(d.subs({K1: psi * M1 * c**2 / r1, K2: psi * M2 * c**2 / r2}))
    print(f"PC2 [positive control] (a1 - a2) with K_1 r_1/M_1 = K_2 r_2/M_2  ->  {pc2}")
    assert pc2 == 0, "universal K r / M failed to cancel"
    print("     reproduces P25's own second control. PASSES.")

    # ---- The natural variable: psi_i = K_i r_i / (M_i c^2), a LENGTH -----
    psi1, psi2 = sp.symbols("psi_1 psi_2", positive=True)
    sub = {K1: psi1 * M1 * c**2 / r1, K2: psi2 * M2 * c**2 / r2}
    d_psi = sp.factor(sp.simplify((a1 - a2).subs(sub)))
    section("The difference, in terms of psi_i = K_i r_i / (M_i c^2)")
    print(f"  a1 - a2 = {d_psi}")
    collected = sp.simplify(d_psi / (psi1 - psi2))
    print(f"\n  factors as (psi_1 - psi_2) * [ {sp.factor(collected)} ]")
    assert sp.simplify(d_psi - (psi1 - psi2) * collected) == 0
    print("  => the whole composition dependence enters ONLY through Delta_psi.")

    # ---- The exact Eotvos ratio, then its leading behaviour --------------
    section("Exact ratio, and the leading term")
    s_psi = sp.simplify((a1 + a2).subs(sub))
    eta_exact = sp.simplify(2 * d_psi / s_psi)

    # Leading denominator: the F_mm term dominates a1 + a2.
    denom_lead = 2 * A * M_A * g**2 / r**2
    eta_lead = sp.simplify(2 * d_psi / denom_lead)
    print(f"  eta_Eotvos (leading denominator) = {sp.factor(eta_lead)}")

    # PC3 -- the leading denominator must actually BE the limit of the exact
    # one. Every term dropped from a1+a2 carries a positive power of kappa,
    # so the ratio exact/leading must tend to 1 as kappa -> 0. This is what
    # makes `denom_lead` a derived approximation rather than an assertion.
    lim = sp.limit(sp.simplify(eta_exact / eta_lead), kap, 0)
    print(f"\nPC3 [positive control] lim_(kappa->0) exact/leading = {lim}")
    assert lim == 1, f"leading denominator is not the kappa->0 limit: {lim}"
    print("     the dropped terms are genuinely subleading. PASSES.")

    # Now extract the kappa^1 piece of that.
    eta_h = sp.Symbol("eta", positive=True)  # the invariant kappa/g
    psi_A = sp.Symbol("psi_A", positive=True)  # K_A r_A / (M_A c^2)
    expanded = sp.expand(eta_lead)
    k1_piece = expanded.coeff(kap, 1) * kap
    k2_piece = expanded.coeff(kap, 2) * kap**2
    assert sp.simplify(expanded - k1_piece - k2_piece) == 0, "unexpected kappa powers"

    k1_in_eta = sp.simplify(k1_piece.subs(kap, eta_h * g))
    print(f"\n  kappa^1 piece, with kappa = eta * g:  {sp.factor(k1_in_eta)}")
    target = -2 * eta_h * (psi1 - psi2) / r
    print(f"  target                             :  {sp.factor(target)}")
    assert sp.simplify(k1_in_eta - target) == 0, f"reduction failed: {sp.simplify(k1_in_eta)}"
    print("\n  => eta_Eotvos ~= 2 * eta * |Delta_psi| / r      [LEADING ORDER]")
    print("     g survives only inside eta = kappa/g -- the derived part.")
    print("     (A cancels too, but that is structural, not a check: every")
    print("      term of the acceleration is linear in A. See docstring.)")

    # ---- Validity condition for dropping the kappa^2 piece ---------------
    ratio = sp.simplify(k2_piece.subs(kap, eta_h * g) / k1_in_eta)
    ratio = sp.simplify(ratio.subs(K_A, psi_A * M_A * c**2 / r_A))
    section("When may the kappa^2 piece be dropped?")
    print(f"  (kappa^2 piece) / (kappa^1 piece) = {sp.simplify(ratio)}")

    # PC4 -- WHY this assert exists. A Step 8a skeptic pointed out that PC1
    # and PC2 cannot see the kappa^2 term at all: the entire composition
    # dependence factors as (psi_1 - psi_2) * [bracket], so PC2 (psi_1 =
    # psi_2) vanishes whatever is inside the bracket, and PC1 (K_i = 0)
    # kills the bracket outright. Mutation-tested rather than argued:
    # changing the coefficient 6 -> 999, and deleting the kappa^2 term
    # entirely, BOTH left every other assertion in this file passing.
    # This is the assertion that fails on either mutant.
    assert sp.simplify(ratio - (-3 * eta_h * psi_A / r)) == 0, f"kappa^2 ratio wrong: {ratio}"
    print("  PC4 [discriminating control] ratio asserted exactly. PASSES.")
    print("  So the leading form is valid while |3 * eta * psi_A / r| << 1,")
    print("  with psi_A = K_A r_A / (M_A c^2) the SOURCE body's own length.")

    # ---- NC: a genuinely different reduction must NOT validate -----------
    section("NC -- negative control")
    wrong = -3 * eta_h * (psi1 - psi2) / r
    assert sp.simplify(k1_in_eta - wrong) != 0
    print("  A deliberately wrong coefficient (3 instead of 2) does NOT")
    print("  satisfy the same assertion -- the check discriminates. PASSES.")

    section("CONSEQUENCE FOR KG2")
    print("  An Eotvos bound constrains the parameters ONLY through the")
    print("  PRODUCT  eta * |Delta_psi|, never eta alone:")
    print()
    print("      eta * |Delta_psi|  <=  eta_Eotvos^max * r / 2")
    print()
    print("  Relation to FINDING_P206: consistent with it, but NOT an")
    print("  independent check -- A-independence is guaranteed by the")
    print("  action's linearity in A. The non-trivial part is that g")
    print("  appears only through eta.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
