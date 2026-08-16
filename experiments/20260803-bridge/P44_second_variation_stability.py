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

PART 3 -- connect the (expected) background-independence to P34's own
"no V(phi)" finding: this IS the structural reason no background-
dependent instability can appear at this order, and motivates exactly the
next step (P45: minimal V(phi)).

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
    print(f"  d^2L/d(epsilon)^2 |_(epsilon=0) = {d2L_at_0}")
    depends_on_bg = phibg in d2L_at_0.atoms(sp.Function)
    print(f"  Contains phi_bg (the background)? {depends_on_bg}")
    assert not depends_on_bg, "second variation unexpectedly depends on the background"
    print("  -> CONFIRMED: delta^2(L) is COMPLETELY INDEPENDENT of the background")
    print("     phi_bg. This is a structural consequence of the matter coupling")
    print("     being exactly LINEAR in phi (-rho*g_hat*phi, no phi^2 or higher term)")
    print("     -- P35's own action has no self-interaction and no potential V(phi)")
    print("     (already known from P34's 'stiff fluid, w=1' dead end). Any check")
    print("     of this second variation is therefore a check of the WHOLE THEORY,")
    print("     not of the specific static solution phi(r)=g_hat*M/(4*pi*r).")

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
    print("     delta=const. This IS the standard no-ghost criterion (a ghost has")
    print("     a kinetic term with the WRONG relative sign, making H unbounded")
    print("     below). PASSES: no ghost instability at this order, for any")
    print("     background -- because there IS no background-dependent term.")

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
    print("  Does mean: the THEORY as a whole (P35's action, matter coupling")
    print("  included) has no ghost at quadratic order, full stop -- a genuine,")
    print("  if structurally unsurprising, fact about the whole action.")
    print("  Direct connection to P34: this background-independence is exactly")
    print("  what 'no V(phi) exists in this action' (P34's stiff-fluid/w=1 dead")
    print("  end) predicts -- a nonzero V(phi) is precisely what would introduce a")
    print("  V''(phi_bg)*delta^2 term into L_2, making stability background-")
    print("  dependent and giving a REAL, solution-specific stability question.")
    print("  This motivates P45 (minimal V(phi)) directly: only once V(phi) exists")
    print("  does 'is THIS solution stable' become a well-posed, non-trivial")
    print("  question at all.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("delta^2(S) is exactly background-independent (structural consequence")
    print("of P35's action being linear in phi, no V(phi) term) -- CONFIRMED by")
    print("direct symbolic computation on a GENERIC background, not assumed.")
    print("The resulting quadratic form is a sum of squares (H_2>=0): no ghost at")
    print("this order, for the theory as a whole. This is NOT evidence that the")
    print("specific solution phi(r)=g_hat*M/(4*pi*r) is stable in any sense")
    print("particular to it -- the check has zero solution-specific content,")
    print("exactly the failure mode P43's Part B was corrected for, caught here")
    print("BEFORE writing the headline rather than after a skeptic pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
