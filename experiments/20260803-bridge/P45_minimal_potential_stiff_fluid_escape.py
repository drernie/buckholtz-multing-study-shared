"""P45 -- thirteenth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), third and final of three symmetry/action-
theoretic checks the user authorized in sequence ("го все по очереди").

P34's own §4 point 8 (re-read directly from FINDING_P34, not recalled
from memory, per Gate 1 discipline) established: with NO potential V(phi),
the field's equation of state is FORCED to w_phi=1 (stiff fluid) for ANY
solution -- a real structural dead end for late-time acceleration. This
step asks: what is the MINIMAL V(phi) that (a) reopens w_phi != 1 as a
possibility, (b) satisfies P44's own corrected requirement that V must be
non-quadratic (V''(phi_bg) genuinely phi_bg-dependent) for a solution-
specific stability question to exist at all, and (c) does not break P35's
own static two-body solution phi(r)=g_hat*M/(4*pi*r) at leading order?

Scope check performed BEFORE choosing V, not after: an earlier working
assumption (carried into this session from an interrupted summary) was
that adding ANY V(phi) here would collide with FINDING_P11's masslessness
requirement. Re-reading FINDING_P11 directly (Gate 1 discipline) shows
that requirement is about the KAPPA/DIPOLE-sector mediator (beta_q/beta_d
= sqrt(6)/2, Lambda=3/2), a DIFFERENT sector from the monopole-sector phi
studied throughout P34-P44. That specific conflict does NOT apply here --
corrected before it could become a silent premise. The real, applicable
constraint is a different, self-contained one: adding a MASS term (V''(0)
!=0) would turn P35's long-range Coulomb-like phi(r)=g_hat*M/(4*pi*r) into
a short-range Yukawa profile, which is what actually would matter here.

Chosen minimal V(phi) = lambda*phi^4/4 (quartic, no mass term):
  V''(0) = 0            -- massless at the natural vacuum phi=0, preserves
                            P35's static solution at leading order
  V''(phi) = 3*lambda*phi^2 -- genuinely phi-dependent (not constant, unlike
                            a mass term) -- satisfies P44's corrected
                            requirement directly

PART 1 -- verify both properties of the chosen V symbolically (not
asserted in prose, learning from P44's own correction).

PART 2 -- re-derive the general field equation with V(phi) added via
Euler-Lagrange (not by hand), confirm it reduces exactly to P35's own
equation at lambda=0 (positive control), then check the residual when
P35's own static solution is plugged into the new equation.

PART 3 -- redo P44's own delta^2(L) calculation with V(phi) included,
confirm L_2 now GENUINELY depends on phi_bg (closing the loop P44
promised).

PART 4 -- equation-of-state check: using the SAME rho_phi=(1/2)phi_dot^2+V,
p_phi=(1/2)phi_dot^2-V formula that reproduces P34's own V=0 result
exactly (rho_phi=p_phi=phi_dot^2/2), compute w_phi=p_phi/rho_phi with
V=lambda*phi^4/4 included and take both limits (kinetic-dominated,
potential-dominated) symbolically.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    ghat = sp.Symbol("g_hat", positive=True)
    lam = sp.Symbol("lambda", positive=True)

    print("=" * 78)
    print("P45 -- minimal V(phi): reopening w_phi != 1, closing P44's stability loop")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- verify the chosen V(phi)=lambda*phi^4/4's two properties")
    print("-" * 78)
    phi_sym = sp.Symbol("phi", real=True)
    V = lam * phi_sym**4 / 4
    Vp = sp.diff(V, phi_sym)
    Vpp = sp.diff(V, phi_sym, 2)
    Vppp = sp.diff(V, phi_sym, 3)
    print(f"  V(phi)   = {V}")
    print(f"  V'(phi)  = {Vp}")
    print(f"  V''(phi) = {Vpp}")
    print(f"  V'''(phi) = {Vppp}  (nonzero for phi!=0, confirms V'''!=0 somewhere)")
    assert Vppp != 0, "V should have a nonzero third derivative somewhere"
    Vpp_at_0 = Vpp.subs(phi_sym, 0)
    print(f"  V''(0)   = {Vpp_at_0}  (masslessness at the natural vacuum)")
    assert Vpp_at_0 == 0, "V should have zero mass term at phi=0"
    depends_on_phi = phi_sym in Vpp.atoms(sp.Symbol)
    print(f"  V''(phi) depends on phi (not constant)? {depends_on_phi}")
    assert depends_on_phi, "V'' should be genuinely phi-dependent, unlike a mass term"
    print("  -> Both properties CONFIRMED: massless at phi=0 (V''(0)=0, unlike a")
    print("     mass term m^2*phi^2/2 whose V''=m^2 is nonzero everywhere), AND")
    print("     V'' is genuinely phi-dependent (satisfies P44's own corrected")
    print("     requirement that V'''!=0 somewhere for a solution-specific")
    print("     stability question to exist at all).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- re-derive the field equation with V(phi) added (Euler-Lagrange,")
    print("not by hand), check reduction to P35 at lambda=0, then check the residual")
    print("for P35's own static solution")
    print("-" * 78)
    rho = sp.Function("rho")(x, y, z)
    phi = sp.Function("phi")(t, x, y, z)
    phi_dot = sp.diff(phi, t)
    grad_phi_sq = sum(sp.diff(phi, c) ** 2 for c in (x, y, z))
    L = (
        sp.Rational(1, 2) * phi_dot**2
        - sp.Rational(1, 2) * grad_phi_sq
        - rho * (1 - ghat * phi)
        - lam * phi**4 / 4
    )

    # Euler-Lagrange: d/dt(dL/d(phi_dot)) + sum_i d/dx_i(dL/d(d_i phi)) - dL/dphi = 0
    dL_dphidot = sp.diff(L, phi_dot)
    eom_time = sp.diff(dL_dphidot, t)
    coords = (x, y, z)
    dL_dgradphi = [sp.diff(L, sp.diff(phi, c)) for c in coords]
    eom_space = sum(sp.diff(dL_dgradphi[i], coords[i]) for i in range(3))
    dL_dphi = sp.diff(L, phi)
    field_eq = sp.simplify(eom_time + eom_space - dL_dphi)
    print(f"  Euler-Lagrange residual (=0 defines the field equation): {field_eq}")
    print("  Rearranged: phi_ddot - laplacian(phi) + lambda*phi^3 = g_hat*rho")

    field_eq_lambda0 = sp.simplify(field_eq.subs(lam, 0))
    phi_ddot = sp.diff(phi, t, 2)
    laplacian = sum(sp.diff(phi, c, 2) for c in coords)
    p35_eq = sp.simplify(phi_ddot - laplacian - ghat * rho)
    assert sp.simplify(field_eq_lambda0 - p35_eq) == 0, (
        "lambda=0 limit should reduce exactly to P35's own equation"
    )
    print("  -> At lambda=0: reduces EXACTLY to P35's own phi_ddot - laplacian(phi)")
    print("     = g_hat*rho (positive control, script assertion).")

    print("\n  Residual when P35's own static solution phi_0(r)=g_hat*M/(4*pi*r) is")
    print("  plugged into the NEW (lambda != 0) equation, for r>0 (source-free):")
    ghat_sym, M, r = sp.symbols("g_hat M r", positive=True)
    phi0 = ghat_sym * M / (4 * sp.pi * r)
    residual = lam * phi0**3
    print(f"    lambda*phi_0(r)^3 = {sp.simplify(residual)}")
    print("  -> NONZERO (unlike lambda=0): phi_0(r) is no longer an EXACT solution")
    print("     once V is added -- only an approximate one, valid when this residual")
    print("     is small compared to the other terms, i.e. when lambda*phi_0^2 << 1")
    print("     near the source. This is a MORE RESTRICTIVE version of the SAME")
    print("     g_hat*phi << 1 perturbative regime P34 already uses throughout (not")
    print("     a new assumption introduced here). Solving the full nonlinear")
    print("     equation is NOT attempted -- flagged explicitly as future work.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- redo P44's delta^2(L) calculation WITH V(phi) included: does")
    print("L_2 now genuinely depend on the background (closing P44's promised loop)?")
    print("-" * 78)
    eps = sp.Symbol("epsilon", real=True)
    phibg = sp.Function("phi_bg")(t, x, y, z)
    delta = sp.Function("delta")(t, x, y, z)

    def lagrangian_with_V(phi_arg):
        phi_dot_ = sp.diff(phi_arg, t)
        grad_sq_ = sum(sp.diff(phi_arg, c) ** 2 for c in (x, y, z))
        return (
            sp.Rational(1, 2) * phi_dot_**2
            - sp.Rational(1, 2) * grad_sq_
            - rho * (1 - ghat * phi_arg)
            - lam * phi_arg**4 / 4
        )

    L_expanded = lagrangian_with_V(phibg + eps * delta)
    d2L_at_0 = sp.simplify(sp.diff(L_expanded, eps, 2).subs(eps, 0))
    print(f"  d^2(density L)/d(epsilon)^2 |_(epsilon=0) = {d2L_at_0}")
    dependence = sp.simplify(sp.diff(d2L_at_0, phibg))
    print(f"  d/d(phi_bg) of the above = {dependence}")
    assert dependence != 0, "L_2 should now depend on phi_bg once V(phi) is added"
    print("  -> CONFIRMED: unlike P44's V=0 case, L_2 now GENUINELY depends on")
    print("     phi_bg (via a -3*lambda*phi_bg^2*delta^2/2 term). This closes the")
    print("     loop P44 predicted: with V(phi) added, 'is THIS solution stable' is")
    print("     now a well-posed, solution-specific question -- NOT answered here")
    print("     (would require evaluating at the actual phi_bg=phi_0(r) and checking")
    print("     the sign of the resulting mass-squared term), only shown to now")
    print("     exist as a real question, which it did not before this step.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- equation of state: is w_phi=1 still FORCED?")
    print("-" * 78)
    print("  Using the SAME rho_phi=(1/2)phi_dot^2+V, p_phi=(1/2)phi_dot^2-V formula")
    print("  that reproduces P34's own V=0 result exactly (rho_phi=p_phi=phi_dot^2/2")
    print("  when V=0 -- checked first, before trusting it for V!=0):")
    phidot_sym, phi_val = sp.symbols("phidot phi_val", real=True)
    V_val = lam * phi_val**4 / 4
    rho_phi = sp.Rational(1, 2) * phidot_sym**2 + V_val
    p_phi = sp.Rational(1, 2) * phidot_sym**2 - V_val
    rho_phi_V0 = rho_phi.subs(lam, 0)
    p_phi_V0 = p_phi.subs(lam, 0)
    assert rho_phi_V0 == p_phi_V0 == sp.Rational(1, 2) * phidot_sym**2, (
        "V=0 case must reproduce P34's rho_phi=p_phi=phidot^2/2"
    )
    print(f"    lambda=0 check: rho_phi={rho_phi_V0}, p_phi={p_phi_V0} (both equal -- matches P34)")

    w_phi = sp.simplify(p_phi / rho_phi)
    print(f"  w_phi = p_phi/rho_phi = {w_phi}")
    w_phi_lambda0 = w_phi.subs(lam, 0)
    print(f"  lambda=0: w_phi = {w_phi_lambda0}  (P34's forced stiff fluid, w=1)")
    assert w_phi_lambda0 == 1

    print("\n  Two limits of the lambda != 0 result:")
    w_kinetic_dominated = sp.limit(w_phi, phi_val, 0)
    print(f"    kinetic-dominated (phi_val -> 0, V negligible):  w_phi -> {w_kinetic_dominated}")
    assert w_kinetic_dominated == 1
    w_potential_dominated = sp.limit(w_phi, phidot_sym, 0)
    print(f"    potential-dominated (phidot -> 0, KE negligible): w_phi -> {w_potential_dominated}")
    assert w_potential_dominated == -1
    print("  -> w_phi=1 is NO LONGER FORCED: it now depends on the actual balance of")
    print("     kinetic vs. potential energy along the solution's own trajectory.")
    print("     Kinetic-dominated recovers P34's stiff fluid (w->1, same dead end).")
    print("     Potential-dominated gives w->-1 (de-Sitter-like, COULD drive")
    print("     acceleration). This shows the possibility is REOPENED, structurally")
    print("     -- it does NOT show this specific system's actual dynamics (with the")
    print("     g_hat*rho source term driving phi) reaches the potential-dominated")
    print("     regime. That would require solving the modified EOM from Part 2 for")
    print("     specific initial conditions -- NOT attempted here, flagged as the")
    print("     natural next step beyond this three-step authorized sequence.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("V(phi)=lambda*phi^4/4 satisfies both required properties (Part 1):")
    print("massless at phi=0 (preserves P35's solution at leading order, Part 2),")
    print("and genuinely phi-dependent V'' (closes P44's stability loop, Part 3).")
    print("w_phi=1 is no longer FORCED (Part 4) -- both the stiff-fluid dead end AND")
    print("a de-Sitter-like limit are structurally available, depending on solution-")
    print("specific dynamics not solved here. An earlier expected conflict with")
    print("FINDING_P11's masslessness requirement was checked directly against P11's")
    print("actual text and found NOT to apply -- P11's requirement is about the")
    print("kappa/dipole-sector mediator, a different sector from this one.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
