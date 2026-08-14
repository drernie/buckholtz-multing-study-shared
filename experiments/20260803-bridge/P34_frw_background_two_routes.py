"""P34 -- first step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md): explicitly add a gravitational sector
(flagged as an assumption -- standard, unmodified Einstein-Hilbert
gravity, chosen as the simplest possible closure, per P33's own
corrected lesson never to assume this silently) to MULTING's own
reconstructed matter+scalar action, reduce to the homogeneous FRW
background, and derive the background equations via TWO derivation
routes -- Bianchi/energy-conservation vs direct Euler-Lagrange variation
of the reduced (minisuperspace) action.

CORRECTED 2026-08-14, after context-blind skeptic review, same day.
THREE real issues fixed, none core-predicate-false (the derived equation
itself, phi''+3H*phi'=g_hat*rho0, is correct and unchanged):
  (1) "Two independent routes, non-tautological cross-check" OVERCLAIMED.
      Both routes derive from the SAME action -- Route A's rho_phi,
      p_phi, rho_m,eff are definitions read directly off S_phi/S_matter,
      the very same action Route B varies. By Noether's theorem, the
      Euler-Lagrange equations and the stress-energy conservation law of
      a consistently-varied action are NOT independent facts -- agreement
      between them is REQUIRED by the theorem, not evidence FOR it. This
      is the FIFTH occurrence this session of the "two routes agree, but
      they share the same underlying input" failure pattern (after P22,
      P29, P30, and P33's sympy-tautology cousin) -- caught this time by
      a skeptic explicitly asked to check for exactly this. Relabeled
      throughout: this is a genuine ALGEBRAIC CONSISTENCY CHECK (it does
      catch typos, sign errors, and arithmetic slips -- both routes
      passed independent hand-transcription of the same physics into
      different formalisms, which is not nothing) -- NOT a
      "non-tautological positive control" in the Perelman-audit sense,
      which requires an INDEPENDENT oracle for the correct answer.
  (2) Section 3's claim "the background Friedmann equation uses
      unmodified G_N" is TRUE BY THE CHOICE MADE IN SECTION 1 (standard,
      minimally-coupled EH gravity was explicitly CHOSEN, not derived)
      -- the original prose read as if this were an independently
      confirmed fact rather than a direct, immediate consequence of that
      choice. Any f(phi)*R non-minimal coupling would give a DIFFERENT,
      modified background. Fixed: explicit "by the choice made in
      Section 1" qualifier added throughout.
  (3) THE CONSEQUENTIAL ONE: "Delta G (P21-22) is a linear-perturbation
      effect, not a background-level G_N replacement" was an UNSUPPORTED
      LEAP. This finding's own Section 4 (What this does NOT establish)
      explicitly excludes any linear-perturbation analysis -- so the
      claim about WHERE Delta G lives cannot be concluded FROM this
      finding's own background-only calculation. What IS established:
      Delta G is NOT present in THIS background reduction, under minimal
      coupling. WHERE it lives is a separate question this finding does
      not answer on its own. (Addendum, added after the correction was
      applied: P35, built the same day, independently performs the
      missing static/perturbative calculation and DOES establish this --
      but that is P35's result, not P34's, and P34 must not borrow it.)

UNITS NOTE (found by re-reading two_field_action_closure.py directly
before starting, not from memory): the project's own stated action,
"S = int d^4x (1/2)(d phi)^2 + sum_i int dtau [g m_i + ...] phi(x_i)",
has never been dimensionally fixed end-to-end anywhere in this project --
it appears only as a print statement (lines 111-116 of that file), never
symbolically encoded or unit-checked. This finding does NOT inherit a
units convention from the source (none was ever fixed); it FIXES one
explicitly here (c=1 units for the derivation, i.e. time and length
measured in the same units, standard practice in this literature), flags
it as a new, explicit choice, and defines g_hat := g/c as a single
symbol throughout to sidestep re-litigating the source's own unfixed
c-bookkeeping. Restoring explicit c-factors to match P21-P33's own SI-like
convention is deferred, flagged as future work.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def route_a_bianchi(t, a, phi, rho0, ghat, H):
    """Route A: assume the STANDARD (unmodified) Friedmann + total energy
    conservation law rho_dot_total = -3H(rho_total+p_total) -- forced by
    the Bianchi identity IF Einstein's equations G_munu=8*pi*G_N*T_munu
    hold for this matter+scalar content with the standard, minimally-
    coupled T_munu (a standard, textbook consequence of varying S_EH+
    S_phi+S_matter, but NOT independently re-derived or verified in this
    script -- CORRECTED 2026-08-14: flagged explicitly per skeptic
    review, this is an assumed, standard premise, not a proven one here)
    -- and solve it for the scalar's own source term. This uses: (1) bare
    mass conservation rho0_dot=-3H*rho0 (particle number conservation,
    unmodified by phi), (2) the definitions rho_m_eff=rho0*(1-ghat*phi),
    rho_phi=phi_dot^2/2, p_phi=phi_dot^2/2 (standard canonical scalar, no
    potential), p_m=0 (dust) -- ALL of these are definitions read
    directly off the SAME S_phi/S_matter that route_b_euler_lagrange
    varies directly below; this route is NOT independent of Route B in
    the sense of using different physical inputs, only a different
    FORMALISM (energy bookkeeping vs. direct field variation) -- see the
    module docstring's correction note (1)."""
    rho_m_eff = rho0 * (1 - ghat * phi)
    rho_phi = sp.Rational(1, 2) * sp.diff(phi, t) ** 2
    p_total = rho_phi
    rho_total = rho_m_eff + rho_phi

    rho0_dot = sp.diff(rho0, t)
    # bare mass conservation is an INPUT here, not derived -- substitute it in
    rho0_dot_law = -3 * H * rho0

    lhs = sp.diff(rho_total, t).subs(rho0_dot, rho0_dot_law)
    rhs = -3 * H * (rho_total + p_total)
    # solve lhs - rhs = 0 for phi_ddot (the only second-time-derivative present)
    residual = sp.expand(lhs - rhs)
    return residual


def route_b_euler_lagrange(t, a, phi, rho0_const_times_a3, ghat):
    """Route B: reduce the matter+scalar action to a 1D (minisuperspace)
    Lagrangian for phi(t) alone, treating a(t) and the comoving bare mass
    M=rho0*a^3 (constant, particle-number conservation) as external
    background functions -- standard, valid procedure for a homogeneous
    test-scalar sourced by homogeneous dust. Derive phi's own equation of
    motion via the actual Euler-Lagrange equation -- a DIFFERENT starting
    point from Route A (direct field-theoretic variation, not energy
    bookkeeping)."""
    L_phi = a**3 * sp.Rational(1, 2) * sp.diff(phi, t) ** 2
    L_matter = -rho0_const_times_a3 * (1 - ghat * phi)
    L = L_phi + L_matter

    dL_dphidot = sp.diff(L, sp.diff(phi, t))
    eom = sp.diff(dL_dphidot, t) - sp.diff(L, phi)
    return sp.expand(eom)


def main():
    t = sp.Symbol("t", positive=True)
    a = sp.Function("a", positive=True)(t)
    phi = sp.Function("phi")(t)
    rho0 = sp.Function("rho0", positive=True)(t)
    ghat = sp.Symbol("g_hat")  # := g/c, dimensionless-in-these-units coupling
    H = sp.diff(a, t) / a
    M = sp.Symbol("M", positive=True)  # comoving bare mass, M = rho0*a^3 = const

    print("=" * 78)
    print("P34 -- FRW background, two derivation routes (consistency check, CORRECTED)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[SETUP] Single-metric action (gravitational sector EXPLICITLY added,")
    print("  flagged as an assumption -- standard unmodified Einstein-Hilbert):")
    print("  S = S_EH[g] + S_phi[phi,g] + S_matter[worldlines,phi;g]")
    print("  S_EH  = standard, unmodified -- Friedmann eq. is the ordinary one,")
    print("          H^2=(8*pi*G_N/3)*rho_total, NOT independently re-derived here")
    print("          (textbook GR result, unaffected by matter's phi-dependence,")
    print("          which enters only through rho_total's own definition below).")
    print("  S_phi = int d^4x sqrt(-g) * phi_dot^2/2   (canonical, c=1 units, flagged)")
    print("  S_matter = -sum_i int dtau_i * m_i*(1-g_hat*phi(x_i)),  g_hat := g/c")
    print("             (P33's own m_eff(phi)/m=1-(g/c)phi, re-used unchanged --")
    print("              that identification was NOT weakened by P33's correction)")

    print("\n[ROUTE A] Bianchi identity / total energy conservation")
    print("  (uses ONLY: bare mass conservation + standard rho,p definitions --")
    print("   does NOT touch the matter+scalar action directly)")
    residual_a = route_a_bianchi(t, a, phi, rho0, ghat, H)
    # residual_a should be linear in phi_ddot, with coefficient phi_dot (from
    # d/dt[(1/2)phi_dot^2] = phi_dot*phi_ddot via the chain rule)
    phi_dd = sp.diff(phi, t, 2)
    coeff_check = sp.simplify(sp.diff(residual_a, phi_dd) - sp.diff(phi, t))
    print(
        f"  coefficient of phi'' in the residual, minus phi' (sanity, should be 0): {coeff_check}"
    )
    assert coeff_check == 0, "residual's phi''-coefficient is not phi_dot as expected"
    solved_a = sp.solve(sp.Eq(residual_a, 0), phi_dd)
    assert solved_a, "Route A residual could not be solved for phi''"
    phi_dd_solution_a = sp.simplify(solved_a[0])
    print(f"  => phi'' solved from Route A: {phi_dd_solution_a}")
    claimed_a = sp.simplify(phi_dd_solution_a - (ghat * rho0 - 3 * H * sp.diff(phi, t)))
    print(f"  Route A EOM claim  phi''=g_hat*rho0-3H*phi'  <=> this expr is 0: {claimed_a}")
    assert claimed_a == 0, "Route A's solved phi'' does not match the claimed EOM"
    check_a = sp.simplify(residual_a.subs(phi_dd, 3 * H * sp.diff(phi, t) * -1 + ghat * rho0))
    print(f"  Substituting the CLAIMED solution into the Route-A residual (should be 0): {check_a}")

    print("\n[ROUTE B] Direct Euler-Lagrange on the reduced matter+scalar action")
    print("  (uses ONLY: the actual action's own kinetic + interaction terms --")
    print("   does NOT touch energy conservation / Bianchi identity)")
    eom_b_expr = route_b_euler_lagrange(t, a, phi, M, ghat)
    print(f"  raw Euler-Lagrange residual: {eom_b_expr}")
    eom_b_normalized = sp.simplify(eom_b_expr / a**3)
    print(f"  divided by a^3: {eom_b_normalized}")
    claimed_b = sp.simplify(
        a**3 * (phi_dd + 3 * H * sp.diff(phi, t) - ghat * M / a**3) - eom_b_expr
    )
    print(
        f"  Route B EOM claim  phi''+3H*phi' = g_hat*rho0 (rho0=M/a^3) <=> this is 0: "
        f"{sp.simplify(claimed_b)}"
    )

    print("\n[CONSISTENCY CHECK] Do Route A and Route B agree? (CORRECTED framing --")
    print("  NOT independent: both read rho_phi/p_phi/rho_m,eff off the SAME action")
    print("  Route B varies directly; by Noether's theorem this agreement is REQUIRED")
    print("  for any consistently-varied action, not evidence FOR the theorem. This")
    print("  is an algebraic consistency check -- catches typos/sign errors, does NOT")
    print("  independently confirm the physics)")
    agree = (check_a == 0) and (sp.simplify(claimed_b) == 0)
    print("  Route A gives:  phi'' + 3H phi' = g_hat * rho0")
    print("  Route B gives:  phi'' + 3H phi' = g_hat * rho0   (rho0 = M/a^3)")
    print(f"  Both residuals vanish identically: {agree}")
    assert agree, "Route A and Route B disagree -- STOP, do not proceed further"

    print("\n[STRUCTURAL OBSERVATION, CORRECTED] What does THIS reduction show about")
    print("  'G_eff = G_N + Delta G'?")
    print("  BY THE CHOICE MADE IN THE SETUP ABOVE (standard, minimally-coupled S_EH,")
    print("  not derived, not the only consistent choice -- see FINDING doc Sec. 4.5),")
    print("  the BACKGROUND Friedmann equation uses the UNMODIFIED G_N. The only")
    print("  background-level deviation from LCDM in THIS reduction is through")
    print("  rho_total's own content (rho_phi, and rho_m,eff's g_hat*phi correction),")
    print("  both second-order-small if g_hat*phi<<1 -- consistent with P22/P31's own")
    print("  bound. This is CONSISTENT WITH P1's own already-stated background result")
    print("  ('MULTING q-blind on background, = LCDM@73', two_field_action_closure.py")
    print("  line 128). CORRECTED (skeptic review): this finding does NOT establish")
    print("  WHERE 'Delta G' (P21-22) lives -- only that it is NOT present in THIS")
    print("  background reduction under minimal coupling. Claiming it 'lives in linear")
    print("  perturbations' requires an actual perturbative calculation, not performed")
    print("  in this script (see P35 for that calculation, done separately).")

    print("\n" + "=" * 78)
    print("VERDICT (CORRECTED after skeptic review, same day)")
    print("=" * 78)
    print("Two derivation routes (Bianchi/energy-conservation vs. direct Euler-")
    print("Lagrange variation) agree EXACTLY on the background scalar equation of")
    print("motion: phi''+3H*phi' = g_hat*rho0. This is a genuine ALGEBRAIC")
    print("CONSISTENCY CHECK, not an independent positive control -- both routes read")
    print("their inputs off the same action, so agreement is required by Noether's")
    print("theorem, not surprising information. The background Friedmann equation, BY")
    print("THE CHOICE of standard minimally-coupled gravity made in the setup (not")
    print("derived), is the standard GR result; MULTING's deviation from LCDM in THIS")
    print("reduction enters entirely through the source content, consistent with P1's")
    print("prior background-blindness claim. WITHDRAWN: the original claim that Delta")
    print("G (P21-22) is definitively a linear-perturbation effect -- this finding's")
    print("own background-only scope cannot establish that; only that Delta G is NOT")
    print("present in the background under minimal coupling.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
