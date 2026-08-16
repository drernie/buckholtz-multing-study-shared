"""P44 -- twelfth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), second of three symmetry/action-theoretic
checks the user authorized in sequence ("го все по очереди") after
reviewing background material on the principle of least action.

Second variation delta^2(S) of P35's own action around a static solution:
is the field's kinetic operator ghost-free (ok), and does this actually say
anything about the SPECIFIC solution phi(r)=g_hat*M/(4*pi*r), or is it a
structural fact about the whole theory?

Honest scoping applied FROM THE START (learning directly from P43's own
same-day correction, where a check that held for ANY static field was
initially, wrongly, presented as new evidence about ONE specific field):
before claiming this check says anything about the specific static
solution, PART 1 explicitly tests whether delta^2(S) depends on the
background at all, using a GENERIC symbolic background phi_bg(t,x,y,z),
not yet the specific radial profile. If it does not depend on phi_bg,
that is stated as the headline, not buried as a caveat.

PART 1 -- expand L(phi_bg + eps*delta) to O(eps^2) for a GENERIC phi_bg,
extract the quadratic-in-delta term, check whether it contains phi_bg at
all.

PART 2 -- no-ghost check: is the resulting quadratic form's associated
Hamiltonian density positive-definite (standard criterion; a ghost has a
kinetic term that lets the Hamiltonian run to -infinity)?

PART 3 -- connect the background-independence to P34's own "no V(phi)"
finding, and check EXACTLY what kind of V(phi) would break it.
[CORRECTED after context-blind skeptic review, 2026-08-14]: the ORIGINAL
Part 3 claimed "a nonzero V(phi) is precisely what would introduce a
V''(phi_bg)*delta^2 term, making stability background-dependent" without
checking this against the simplest possible V(phi): a MASS term
V=m^2*phi^2/2. Skeptic showed by direct computation that V''=m^2 is a
CONSTANT (independent of phi_bg) for any quadratic V -- so a mass term is
a "nonzero V(phi)" that does NOT make stability background-dependent,
contradicting the original claim as worded. Independently re-verified
below (now computed explicitly, not just asserted in prose): only a V
with V'''!=0 (cubic or higher, i.e. genuine self-interaction beyond a
mass term) actually introduces phi_bg-dependence. The P45 link survives
ONLY if P45's "minimal V(phi)" is understood to mean cubic-or-higher --
this is now stated explicitly rather than left ambiguous.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    ghat = sp.Symbol("g_hat", positive=True)
    eps = sp.Symbol("epsilon", real=True)

    print("=" * 78)
    print("P44 -- second variation delta^2(S) and no-ghost check")
    print("(P34/P35's own S = S_EH + S_phi + S_matter; this checks S_phi+S_matter")
    print("only, on a flat background -- NOT a coupled metric-phi stability")
    print("analysis, same scope limit as every prior finding in this sub-arc)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- does delta^2(S) depend on the background at all?")
    print("(tested FIRST, with a GENERIC symbolic background, before")
    print("substituting the specific solution -- avoids P43's own mistake)")
    print("-" * 78)
    rho = sp.Function("rho")(x, y, z)
    phibg = sp.Function("phi_bg")(t, x, y, z)
    delta = sp.Function("delta")(t, x, y, z)

    def lagrangian(phi):
        phi_dot = sp.diff(phi, t)
        grad_sq = sum(sp.diff(phi, c) ** 2 for c in (x, y, z))
        return sp.Rational(1, 2) * phi_dot**2 - sp.Rational(1, 2) * grad_sq - rho * (1 - ghat * phi)

    L_expanded = lagrangian(phibg + eps * delta)
    d2L_deps2 = sp.diff(L_expanded, eps, 2)
    d2L_at_0 = sp.simplify(d2L_deps2.subs(eps, 0))
    print(f"  d^2(density L)/d(epsilon)^2 |_(epsilon=0) = {d2L_at_0}")
    # [CORRECTED, skeptic-caught] direct derivative check, not atom-membership --
    # atom-tracking would pass even on an unsimplified residual term
    dependence = sp.simplify(sp.diff(d2L_at_0, phibg))
    print(f"  d/d(phi_bg) of the above (direct dependence check) = {dependence}")
    assert dependence == 0, "second variation unexpectedly depends on the background"
    print("  -> CONFIRMED: the density-level second variation is COMPLETELY")
    print("     INDEPENDENT of the background phi_bg (note: this is delta^2 of the")
    print("     LAGRANGIAN DENSITY, not literally delta^2(S) -- the two coincide by")
    print("     integration once boundary terms drop, but the object computed here")
    print("     is pointwise; phi_bg is NOT required to satisfy any field equation")
    print("     for this specific density-level result). This is verified for THIS")
    print("     ONE Lagrangian, not proven as a general theorem: the sharper general")
    print("     condition is 'L at most quadratic in phi with phi-independent")
    print("     coefficients' (linear-in-phi is sufficient but not necessary -- a")
    print("     constant-coefficient mass term m^2*phi^2/2 would ALSO give a")
    print("     background-independent result, see Part 3). Any check built on this")
    print("     second variation is a check of THIS action as a whole, not of the")
    print("     specific static solution phi(r)=g_hat*M/(4*pi*r).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- no-ghost check: is the resulting quadratic form's")
    print("Hamiltonian density positive-definite?")
    print("-" * 78)
    print(f"  delta^2(L) (from Part 1) = {d2L_at_0}")
    # delta^2(L) = delta_dot^2 - sum(d_i(delta))^2 ; the associated quadratic
    # Lagrangian density is L_2 = (1/2)*delta^2(L) by the usual 1/2 convention
    L2 = sp.Rational(1, 2) * d2L_at_0
    delta_dot = sp.diff(delta, t)
    print(f"  L_2 (quadratic fluctuation Lagrangian) = {L2}")
    pi_delta = sp.diff(L2, delta_dot)
    print(f"  canonical momentum pi_delta = dL_2/d(delta_dot) = {pi_delta}")
    H2 = sp.expand(pi_delta * delta_dot - L2)
    print(f"  Hamiltonian density H_2 = pi_delta*delta_dot - L_2 = {H2}")
    grad_delta_sq = sum(sp.diff(delta, c) ** 2 for c in (x, y, z))
    H2_expected = sp.Rational(1, 2) * delta_dot**2 + sp.Rational(1, 2) * grad_delta_sq
    assert sp.simplify(H2 - H2_expected) == 0, (
        "Hamiltonian density does not match expected sum-of-squares form"
    )
    print("  -> H_2 = (1/2)*delta_dot^2 + (1/2)*(grad delta)^2 : a SUM OF SQUARES,")
    print("     manifestly >= 0 for every field configuration, zero only at")
    print("     delta=const. PASSES: no ghost (a ghost has a kinetic term with the")
    print("     WRONG relative sign, making H unbounded below).")
    print("  [CORRECTED, skeptic-caught] This result is actually STRONGER than 'no")
    print("  ghost' alone -- H_2's exact sum-of-squares form also rules out a")
    print("  tachyon (no wrong-sign mass term -- there is no mass term at all here)")
    print("  and a gradient instability (no wrong-sign spatial-gradient term).")
    print("  'At this order' is also slightly misleading: L is EXACTLY quadratic in")
    print("  phi, so L_2 is exact, not a leading-order truncation -- O(eps^3) and")
    print("  higher vanish identically, so there is no nonlinear correction to")
    print("  worry about at any order for the LINEARIZED fluctuation. (This check")
    print("  says nothing about Ostrogradsky-type higher-derivative ghosts, since L")
    print("  has only first derivatives of phi -- not applicable here, but would")
    print("  need separate treatment if a future step added higher derivatives.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- what this does and does not mean for the specific solution")
    print("phi(r)=g_hat*M/(4*pi*r), and connection to P34/P45")
    print("-" * 78)
    print("  Does NOT mean: 'the static solution phi(r)=g_hat*M/(4*pi*r) is")
    print("  linearly stable' in any sense specific to that solution -- Part 1")
    print("  showed delta^2(S) doesn't know which solution (or even whether a")
    print("  solution at all) sits at phi_bg. The same H_2>=0 result would hold")
    print("  for phi_bg=0, or any other static or non-static configuration.")
    print("  Does mean: THIS action (matter coupling included) has no ghost/tachyon/")
    print("  gradient instability at quadratic order, full stop -- a genuine, if")
    print("  near-tautological, fact given the coupling is exactly quadratic.")

    print("\n  [CORRECTED, skeptic-caught] The ORIGINAL claim here was: 'a nonzero")
    print("  V(phi) is precisely what would introduce a V''(phi_bg)*delta^2 term,")
    print("  making stability background-dependent.' This was checked against only")
    print("  ONE class of V(phi) in prose, not computed -- and is FALSE for the")
    print("  simplest case. Computed explicitly for two cases:")
    m = sp.Symbol("m", positive=True)
    lam = sp.Symbol("lambda")

    def d2_of_minus_V(V_of_phi):
        V_expanded = V_of_phi.subs(sp.Symbol("PHI_PLACEHOLDER"), phibg + eps * delta)
        return sp.simplify(sp.diff(-V_expanded, eps, 2).subs(eps, 0))

    phi_ph = sp.Symbol("PHI_PLACEHOLDER")
    V_mass = sp.Rational(1, 2) * m**2 * phi_ph**2
    d2_mass = d2_of_minus_V(V_mass)
    mass_depends = sp.simplify(sp.diff(d2_mass, phibg)) != 0
    print(f"    mass term V=(1/2)m^2*phi^2:   d^2(-V)/d(eps)^2|_0 = {d2_mass}")
    print(f"      depends on phi_bg? {mass_depends}")
    assert not mass_depends, "mass term should NOT introduce phi_bg-dependence"

    V_cubic = lam * phi_ph**3 / 6
    d2_cubic = d2_of_minus_V(V_cubic)
    cubic_depends = sp.simplify(sp.diff(d2_cubic, phibg)) != 0
    print(f"    cubic term V=lambda*phi^3/6: d^2(-V)/d(eps)^2|_0 = {d2_cubic}")
    print(f"      depends on phi_bg? {cubic_depends}")
    assert cubic_depends, "cubic term SHOULD introduce phi_bg-dependence"

    print("  -> A quadratic V (mass term) is a 'nonzero V(phi)' that does NOT make")
    print("     stability background-dependent (V''=m^2 is a CONSTANT). Only a V")
    print("     with V'''!=0 (cubic or higher -- genuine self-interaction beyond a")
    print("     mass term) actually introduces phi_bg-dependence. The link to P45")
    print("     survives ONLY if P45's 'minimal V(phi)' means cubic-or-higher --")
    print("     stated explicitly here rather than left ambiguous as it was before")
    print("     this correction. This motivates P45 SPECIFICALLY exploring a")
    print("     non-quadratic V(phi), not 'any V(phi) at all.'")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Density-level delta^2(L) is exactly background-independent for THIS")
    print("action -- CONFIRMED by direct symbolic computation on a GENERIC")
    print("background, not assumed, and by a direct-derivative check (not just")
    print("atom membership). The resulting quadratic form is a sum of squares")
    print("(H_2>=0): no ghost/tachyon/gradient instability, exact at all orders")
    print("for the fluctuation (L is exactly quadratic in phi). This is NOT")
    print("evidence that the specific solution phi(r)=g_hat*M/(4*pi*r) is stable")
    print("in any sense particular to it -- the check has zero solution-specific")
    print("content, exactly the failure mode P43's Part B was corrected for,")
    print("caught here BEFORE writing the headline rather than after a skeptic")
    print("pass. [CORRECTED] The link to P45 requires a NON-QUADRATIC V(phi)")
    print("(cubic or higher) -- a mass term alone would NOT create a solution-")
    print("specific stability question, verified explicitly above, not assumed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
