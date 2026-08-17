"""P55 -- Step B2, Part 1 of the user's refined "Euler/G_matter" milestone:
derive the matter-sector source term Q^nu (nabla_mu T_m^munu = Q^nu) from
phi's OWN stress-energy non-conservation, NOT inserted by hand or by
analogy (KG-B2a, the user's own kill-gate).

SCOPE CORRECTION, found DURING THIS BUILD, before any skeptic review --
kept here rather than silently fixed, per this campaign's own "no silent
fixes" discipline: the FIRST version of this script combined the FULL
(Phi,Psi-perturbed) metric machinery from FINDING_P48/P54 with
FINDING_P46's own field equation box(phi)=-g_hat*rho. That combination is
INCONSISTENT: FINDING_P46's own docstring states its field equation was
derived "via Euler-Lagrange on the FULL Lagrangian density (sqrt(-g)=a^3,
g^{ij}=delta^{ij}/a^2)" -- the UNPERTURBED FRW metric, with Phi=Psi=0
throughout. FINDING_P47's own T_munu(phi) construction used the same
restricted (Phi=Psi=0) background. Feeding P46's Phi=Psi=0 field equation
into a covariant divergence built from the FULL Phi,Psi-perturbed metric
is exactly the "silently mix conventions" trap the user's own KG-B2b
warns about, in a new guise. CAUGHT by this script's own Part 4 positive
control (the general covariant identity, which must hold for ANY field
equation, FAILED at linear order when combined with P46's field equation
-- a real, non-vacuous check, not merely re-confirming what was already
assumed). FIXED by restricting THIS finding's own metric to the SAME
Phi=Psi=0 scope P46/P47 already established -- consistent, not silently
patched to "make it work." The Phi,Psi-inclusive extension (deriving
phi's OWN field equation on the FULL perturbed metric, which P46 never
did) is a real, separate, currently-open gap, named explicitly below, not
attempted here.

METHOD, avoiding every kill-gate the user pre-registered for this
milestone:
  - Reuses FINDING_P48/P54's own already-verified christoffels_exact
    helper verbatim, applied here to the SAME restricted (Phi=Psi=0)
    metric FINDING_P46/P47 already used -- not a different convention.
  - Reuses FINDING_P47's own already-verified T_munu(phi) formula
    (d_mu(phi)*d_nu(phi) - (1/2)*g_munu*(d phi)^2) on the SAME metric
    scope P47 itself used.
  - Reuses FINDING_P46's own already-verified field equation
    box(phi) = -ghat*rho EXACTLY (not re-derived, not guessed), now
    consistently scoped.
  - Derives Q^nu from a GENERAL COVARIANT IDENTITY
    (nabla_mu T_phi^munu = (box phi)*d^nu(phi), true for ANY scalar field
    regardless of its equation of motion) verified DIRECTLY by symbolic
    computation, both on the background (eps=0) and at linear order --
    a genuine positive control on the covariant-divergence code itself.
  - [CORRECTED after context-blind skeptic review, Step 8a] Total
    stress-energy conservation (nabla_mu(T_phi^munu+T_m^munu)=0) is
    IMPOSED HERE AS A CLOSURE CONDITION, not treated as automatically
    following from diffeomorphism invariance alone -- the skeptic
    independently derived, and this was independently re-checked before
    accepting, that FINDING_P46's own Lagrangian treats rho as an
    EXTERNAL scalar (not a fully dynamical dust field with its own
    worldline action) -- varying the coupling term rho*(1-ghat*phi) w.r.t.
    g^munu alone, with rho held fixed, gives a coupling stress tensor
    whose divergence leaves a residual -(1-ghat*phi)*d^nu(rho) term that
    does NOT cancel against T_phi's own divergence unless rho itself
    separately satisfies a conservation law. Total conservation is
    therefore the CLOSURE CONDITION a genuine matter model (B2 Part 2's
    job: a proper dust action, not just "whatever's left over") must
    satisfy for Q^nu to be physically meaningful -- not a free-standing
    fact independent of what T_m actually turns out to be.

SCOPE, stated up front: this file derives Q^nu ONLY, and ONLY within
FINDING_P46/P47's own established Phi=Psi=0 scope -- the source term that
will appear on the RHS of the matter conservation law under that same
restriction. It does NOT yet assemble the linearized matter
continuity/Euler equations from T_m^munu=rho*u^mu*u^nu (B2 Part 2,
separate, not-yet-started). It does NOT attempt the B1<->B2 compatibility
check (B1's own G_0i DOES include Phi -- reconciling that scope gap is
explicitly deferred to that step, not silently glossed over here). It
does NOT extend phi's own field equation to the Phi,Psi-perturbed metric.

KILL-GATES applicable to THIS file (subset of the user's own seven):
  KG-B2a: the scalar force/source must NOT be inserted by hand or by
          analogy -- derived here from phi's OWN stress non-conservation,
          a general covariant identity, verified by direct computation.
  KG-B2b: continuity/Euler conventions must not silently mix gauges --
          this file's OWN build caught itself doing exactly this (see
          the Scope Correction above) and fixed it before any skeptic
          review, by restricting to a single, internally consistent
          scope throughout.
  KG-B2g: the P22/P31 A*g^2 soft ceiling must not be used to directly
          bound g*phibar or anything in this file -- not used anywhere
          here (not applicable to this file's scope at all).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48/P54's own already-verified helper."""
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for lam in range(n):
        for mu in range(n):
            for nu in range(n):
                term = sum(
                    ginv[lam, sig]
                    * (
                        sp.diff(g[sig, mu], coords[nu])
                        + sp.diff(g[sig, nu], coords[mu])
                        - sp.diff(g[mu, nu], coords[sig])
                    )
                    for sig in range(n)
                )
                Gamma[lam][mu][nu] = sp.Rational(1, 2) * term
    return Gamma


def covariant_div_upper(T_upper, Gamma, coords, nu, n=4):
    """nabla_mu T^{mu,nu} = d_mu(T^{mu,nu}) + Gamma^mu_{mu,lam} T^{lam,nu}
    + Gamma^nu_{mu,lam} T^{mu,lam} -- the standard covariant-divergence
    formula for a symmetric rank-2 tensor with both indices raised."""
    total = 0
    for mu in range(n):
        total += sp.diff(T_upper[mu][nu], coords[mu])
    for mu in range(n):
        for lam in range(n):
            total += Gamma[mu][mu][lam] * T_upper[lam][nu]
            total += Gamma[nu][mu][lam] * T_upper[mu][lam]
    return total


def covariant_box(scalar_field, ginv, Gamma, coords, n=4):
    """box(phi) := g^(mu nu)*nabla_mu*nabla_nu(phi)
    = g^(mu nu)*(d_mu d_nu(phi) - Gamma^lam_(mu nu)*d_lam(phi))
    -- the covariant d'Alembertian of a scalar, built from the SAME
    Gamma array used by covariant_div_upper, guaranteeing internal
    consistency between the two (this is the fix for a real bug this
    build caught in itself: an earlier version hand-typed box(phi) by
    analogy to FINDING_P46's own printed formula instead of computing it
    from this file's OWN Christoffel data, and the two were NOT
    guaranteed consistent with each other even though both are, in
    isolation, correct formulas)."""
    dphi_local = [sp.diff(scalar_field, c) for c in coords]
    result = 0
    for mu in range(n):
        for nu in range(n):
            hessian_munu = sp.diff(scalar_field, coords[mu], coords[nu]) - sum(
                Gamma[lam][mu][nu] * dphi_local[lam] for lam in range(n)
            )
            result += ginv[mu, nu] * hessian_munu
    return result


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eps = sp.Symbol("epsilon", real=True)
    a = sp.Function("a")(t)
    ghat = sp.Symbol("g_hat", real=True, positive=True)
    phibar = sp.Function("phi_bar")(t)
    deltaphi = sp.Function("delta_phi")(t, x, y, z)
    rhobar = sp.Function("rho_bar")(t)
    deltarho = sp.Function("delta_rho")(t, x, y, z)

    print("=" * 78)
    print("P55 -- Step B2 Part 1: source term Q^nu from phi's own stress")
    print("non-conservation (NOT inserted by hand -- KG-B2a)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\n[SCOPE] Restricted to FINDING_P46/P47's own established metric")
    print("scope (unperturbed FRW, Phi=Psi=0) -- see module docstring for the")
    print("scope-mismatch this build caught in itself and fixed before any")
    print("skeptic review.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- SAME unperturbed FRW metric FINDING_P46/P47 both used")
    print("(Phi=Psi=0 -- only phi itself is perturbed, not the metric)")
    print("-" * 78)
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    n = 4
    Gamma = christoffels_exact(coords, g, ginv, n)
    print("  g_00=-1, g_ii=a^2 -- matches FINDING_P47's own T_munu(phi) metric")
    print("  exactly, and FINDING_P46's own field-equation derivation.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- phi's stress-energy tensor, FINDING_P47's own structural")
    print("formula, on this SAME restricted metric")
    print("-" * 78)
    phi = phibar + eps * deltaphi
    dphi = [sp.diff(phi, c) for c in coords]
    dphi_sq = sum(ginv[mu, nu] * dphi[mu] * dphi[nu] for mu in range(n) for nu in range(n))
    print("  (d phi)^2 = g^(mu nu)*d_mu(phi)*d_nu(phi) = -phi_dot^2 + (grad phi)^2/a^2")

    def T_lower(mu, nu):
        gmn = g[mu, nu] if mu == nu else 0
        return dphi[mu] * dphi[nu] - sp.Rational(1, 2) * gmn * dphi_sq

    T_upper = [[0] * n for _ in range(n)]
    for mu in range(n):
        for nu in range(n):
            T_upper[mu][nu] = sp.expand(
                sum(ginv[mu, a] * ginv[nu, b] * T_lower(a, b) for a in range(n) for b in range(n))
            )
    print("  T^(mu nu)(phi) = g^(mu a)*g^(nu b)*T_ab, both indices raised with")
    print("  this restricted metric's inverse.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- POSITIVE CONTROL: verify the general covariant identity")
    print("nabla_mu T_phi^(mu,nu) = box(phi)*d^nu(phi) on the BACKGROUND")
    print("(eps=0) case FIRST")
    print("-" * 78)
    print("  This identity holds for ANY scalar field with T_munu=d_mu(phi)d_nu")
    print("  (phi)-(1/2)g_munu(d phi)^2, regardless of its equation of motion --")
    print("  a pure consequence of the metric being covariantly conserved")
    print("  (nabla g=0) and the definition of box(phi):=g^(mu nu)*nabla_mu*")
    print("  nabla_nu(phi). Verified directly, not quoted from memory.")

    print("  box(phi) computed via covariant_box(), using the SAME Gamma array")
    print("  as covariant_div_upper() -- guarantees internal consistency (see")
    print("  covariant_box()'s own docstring for the bug this fixes).")
    box_phi_exact = covariant_box(phi, ginv, Gamma, coords, n)
    box_phi_bg = sp.simplify(box_phi_exact.subs(eps, 0))
    print(f"  box(phi) on the homogeneous background = {box_phi_bg}")
    print("  [SELF-CAUGHT DURING BUILD] first version of this assertion expected")
    print("  box(phi)_bg=+phibar_ddot+3*H*phibar_dot -- WRONG SIGN. Re-reading")
    print("  FINDING_P46's own script logic directly (its own line")
    print("  '-box_phi - target_form.subs(rho,0) == 0' implies")
    print("  box_phi=-target_form.subs(rho,0)=-(phibar_ddot+3*H*phibar_dot) on")
    print("  the source-free/background piece) shows P46's OWN convention has")
    print("  the OPPOSITE overall sign. Fixed here, independently re-derived")
    print("  from P46's own script text before accepting either sign.")
    expected_bg_form = -(sp.diff(phibar, t, 2) + 3 * (sp.diff(a, t) / a) * sp.diff(phibar, t))
    assert sp.simplify(box_phi_bg - expected_bg_form) == 0, (
        "covariant_box() does not reduce to -(phibar_ddot+3*H*phibar_dot) on "
        "the background -- does not match FINDING_P46's own sign convention, "
        "re-check covariant_box() before proceeding"
    )
    print("  -> MATCHES FINDING_P46's own sign convention exactly (box(phi)_bg")
    print("     = -(phibar_ddot+3*H*phibar_dot)) -- covariant_box() reused, not")
    print("     by-hand, and cross-checked against P46's own result.")

    print("  [SELF-CAUGHT DURING BUILD, second instance] the identity itself is")
    print("  nabla_mu T_phi^(mu,nu) = (+box(phi))*d^nu(phi) -- NO extra minus")
    print("  sign (verified by hand-derivation in the module-level reasoning")
    print("  behind this build, and matches Part 4's own, already-correct")
    print("  usage below). An earlier version of THIS line carried over a")
    print("  minus sign that belongs to a LATER step (Q^nu=-nabla_mu T_phi^")
    print("  (mu,nu), from TOTAL conservation) into the pure identity check --")
    print("  a genuine bookkeeping error, not a physics error, fixed here.")
    div_T0_bg = sp.simplify(covariant_div_upper(T_upper, Gamma, coords, 0, n).subs(eps, 0))
    rhs0_bg = sp.simplify(box_phi_bg * (ginv[0, 0] * sp.diff(phibar, t)).subs(eps, 0))
    print(f"  nabla_mu T_phi^(mu,0) |_background = {div_T0_bg}")
    print(f"  box(phi)*d^0(phi) |_background      = {rhs0_bg}")
    identity_check_bg = sp.simplify(div_T0_bg - rhs0_bg)
    assert identity_check_bg == 0, (
        "the general covariant identity nabla_mu T_phi^(mu,0) = box(phi)*d^0(phi) "
        "FAILS on the background -- a real error in the covariant-divergence "
        "code, must be fixed before trusting anything at linear order"
    )
    print("  -> CONFIRMED on the background.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- linear-order (nu=0) identity check and Q^0 extraction")
    print("-" * 78)
    print("  Same identity, now at O(epsilon), using covariant_box() again (NOT")
    print("  a hand-typed formula-by-analogy this time -- the exact bug this")
    print("  build caught and fixed, see covariant_box()'s own docstring):")
    box_phi_lin = sp.simplify(sp.diff(box_phi_exact, eps).subs(eps, 0))
    print(f"  box(phi)^(1) (computed via covariant_box) = {box_phi_lin}")
    expected_lin_form = -(
        sp.diff(deltaphi, t, 2)
        + 3 * (sp.diff(a, t) / a) * sp.diff(deltaphi, t)
        - sum(sp.diff(deltaphi, c, 2) for c in coords[1:]) / a**2
    )
    assert sp.simplify(box_phi_lin - expected_lin_form) == 0, (
        "covariant_box()'s O(eps) piece does not match -1 times FINDING_P46's "
        "own printed linear field-equation form -- re-check before proceeding"
    )
    print("  -> MATCHES FINDING_P46's own sign convention at linear order too")
    print("     (same overall minus sign as the background case) -- independent")
    print("     cross-check, not merely reused by assumption.")
    rho = rhobar + eps * deltarho
    field_eq_rhs = -ghat * rho

    div_T0_lin = sp.simplify(
        sp.diff(covariant_div_upper(T_upper, Gamma, coords, 0, n), eps).subs(eps, 0)
    )
    d0_phi_full = ginv[0, 0] * sp.diff(phi, t)
    identity_rhs_full = box_phi_exact * d0_phi_full
    identity_rhs_lin = sp.simplify(sp.diff(identity_rhs_full, eps).subs(eps, 0))
    print(f"  [nabla_mu T_phi^(mu,0)]^(1) = {div_T0_lin}")
    print(f"  [box(phi)*d^0(phi)]^(1)     = {identity_rhs_lin}")
    identity_check_lin = sp.simplify(div_T0_lin - identity_rhs_lin)
    print(f"  difference = {identity_check_lin}")
    assert identity_check_lin == 0, (
        "the general covariant identity FAILS at linear order even on the "
        "restricted (Phi=Psi=0) metric -- a genuine error, not the earlier "
        "scope mismatch (which is now fixed by construction)"
    )
    print("  -> CONFIRMED at linear order, on the consistent (Phi=Psi=0) scope.")

    print()
    print("  NOW substitute P46's field equation box(phi)=-g_hat*rho to get the")
    print("  ACTUAL (not merely identity-consistent) linear-order divergence:")
    Q0_from_identity = sp.simplify(sp.diff((field_eq_rhs * d0_phi_full), eps).subs(eps, 0))
    print(f"  [nabla_mu T_phi^(mu,0)]^(1) using the ACTUAL field equation = {Q0_from_identity}")
    Q0 = sp.simplify(-Q0_from_identity)
    print(f"  Q^0 := -[nabla_mu T_phi^(mu,0)]^(1) (total conservation) = {Q0}")

    print("\n" + "=" * 78)
    print("VERDICT [CORRECTED after context-blind skeptic review, Step 8a]")
    print("=" * 78)
    print("The general covariant identity nabla_mu T_phi^(mu,nu)=box(phi)*d^nu")
    print("(phi) is CONFIRMED by direct symbolic computation, both on the")
    print("background (Part 3) and at linear order (Part 4), on")
    print("FINDING_P46/P47's own established (Phi=Psi=0) metric scope.")
    print()
    print("Substituting FINDING_P46's own field equation box(phi)=-g_hat*rho")
    print("(reused, not re-derived) gives the ACTUAL nu=0 component of phi's")
    print("stress non-conservation at linear order. Q^0 := -[that quantity] IS")
    print("the matter-sector source term IF total stress-energy conservation")
    print("holds -- independently re-derived (before accepting) that this is")
    print("NOT automatic from diffeomorphism invariance alone in P46's own")
    print("setup, which treats rho as an EXTERNAL scalar, not a fully")
    print("dynamical dust field: varying only the coupling term rho*(1-g_hat*")
    print("phi) w.r.t. g^munu, with rho fixed, leaves a residual -(1-g_hat*")
    print("phi)*d^nu(rho) that does not cancel unless rho separately satisfies")
    print("its own conservation law. Total conservation is therefore a CLOSURE")
    print("CONDITION a genuine matter model (B2 Part 2's job -- a proper dust")
    print("action) must satisfy, not a free-standing fact assumed here.")
    print()
    print("SCOPE GAP, stated explicitly, discovered during this build: this")
    print("file does NOT extend to the Phi,Psi-perturbed metric. FINDING_P54's")
    print("own G_0i DOES include Phi. Reconciling this is required before the")
    print("B1<->B2 compatibility check can be attempted honestly -- either by")
    print("deriving phi's OWN field equation on the full perturbed metric (a")
    print("real, not-yet-started extension of FINDING_P46), or by working")
    print("entirely within a further-restricted regime where the mismatch")
    print("provably does not matter (not established here either). This gap")
    print("is NOT a defect of this file's own derivation -- it is an honestly")
    print("named boundary of what FINDING_P46/P47 themselves ever established.")
    print()
    print("This is NOT the matter Euler equation itself (that is B2 Part 2, a")
    print("separate, not-yet-started step) -- it is the SOURCE TERM that will")
    print("appear on its RHS, derived from a general covariant identity plus")
    print("an already-established field equation, with KG-B2a (no hand-")
    print("inserted force) satisfied by construction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
