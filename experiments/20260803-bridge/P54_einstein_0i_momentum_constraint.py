"""P54 -- Step B1 of the user's refined "Euler/G_matter" milestone: the
Einstein 0i MOMENTUM CONSTRAINT, G_0i=8*pi*G_N*T_0i, extracted from the
SAME exact perturbed-FRW machinery FINDING_P48 already built and verified
(christoffels_exact, ricci_exact, the metric ansatz, the G(mu,nu) helper)
-- reused verbatim, not reinvented, per this campaign's established
anti-hand-algebra discipline.

USER'S OWN CORRECTION, adopted here: G_0i is the Einstein momentum
CONSTRAINT (part of the LHS geometry), not the matter Euler equation.
Conflating the two is explicitly named as a kill-gate for this whole
"Step B" milestone -- this file supplies ONLY the geometry side. The
matter Euler equation (from varying the coupled matter+phi action, giving
nabla_mu T_m^munu = Q^nu with Q sourced by the g*rho*phi coupling) is a
SEPARATE, not-yet-started step (B2). Comparing B1's G_0i to B2's matter
momentum-conservation equation, and extracting G_matter(a,k), is a THIRD,
also not-yet-started step (the compatibility check). This file's own
scope ends at the geometry.

PRE-REGISTERED claim for THIS file specifically (narrower than the
user's own H0/H1/H2, which apply to the eventual B1+B2 compatibility
check, not to B1 alone -- matching this campaign's established
granularity, cf. the P46/P47/P48/P49 split for the same reason):
  C1 -- G_0i^(1), for this scalar-only perturbation ansatz (no vector
        d.o.f. anywhere in P38-P53's own metric convention), has the
        REQUIRED gradient/curl-free structure: G_0i^(1) = d_i[F(t,x,y,z)]
        for some scalar F built from Phi,Psi and their time-derivatives.
        This is forced by general covariance (Bianchi identity) whenever
        the metric perturbation itself carries no vector mode -- checked
        directly (d_y[G_0x]-d_x[G_0y]=0), not merely cited.
  C2 -- FAILS: some sign/coefficient/structural inconsistency is found
        (e.g. the curl does not vanish, signaling either an algebra
        error or a genuinely vector-sourced piece this ansatz should not
        have).

KILL-GATES (subset of the user's own seven, applicable to THIS file):
  KG-B1a: do not mistake G_0i for the matter Euler equation itself --
          stated explicitly throughout, this is geometry only.
  KG-B1b: continuity/momentum-constraint conventions must not silently
          mix gauges -- this file stays in the SAME conformal-Newtonian
          gauge P46-P53 have used throughout (h_00=-2*Phi, h_ii=-2*Psi,
          zero shear/vector modes), stated explicitly.
  KG-B1c: theta=0 (irrotational dust) must not be substituted here --
          not applicable, this file contains no matter-sector variable
          at all, only the metric/geometry side.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48's own already-verified helper."""
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


def ricci_exact(coords, Gamma, mu, nu, n=4):
    """Reused VERBATIM from FINDING_P48's own already-verified helper."""
    term1 = sum(sp.diff(Gamma[lam][mu][nu], coords[lam]) for lam in range(n))
    term2 = sum(sp.diff(Gamma[lam][mu][lam], coords[nu]) for lam in range(n))
    term3 = sum(Gamma[lam][lam][sig] * Gamma[sig][mu][nu] for lam in range(n) for sig in range(n))
    term4 = sum(Gamma[lam][nu][sig] * Gamma[sig][mu][lam] for lam in range(n) for sig in range(n))
    return term1 - term2 + term3 - term4


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eps = sp.Symbol("epsilon", real=True)
    a = sp.Function("a")(t)
    Phi = sp.Function("Phi")(t, x, y, z)
    Psi = sp.Function("Psi")(t, x, y, z)

    print("=" * 78)
    print("P54 -- Step B1: Einstein 0i momentum constraint (geometry only)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nKG-B1a: this is the Einstein MOMENTUM CONSTRAINT, NOT the matter")
    print("Euler equation. That is a separate, not-yet-started step (B2).")
    print("KG-B1b: same conformal-Newtonian gauge as P46-P53 throughout --")
    print("h_00=-2*Phi, h_ii=-2*Psi, zero shear/vector modes, stated explicitly.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- SAME exact perturbed FRW metric as FINDING_P48, reused")
    print("verbatim (not reinvented)")
    print("-" * 78)
    print("  ds^2 = -(1+2*eps*Phi)*dt^2 + a^2*(1-2*eps*Psi)*(dx^2+dy^2+dz^2)")
    g = sp.diag(
        -(1 + 2 * eps * Phi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
    )
    ginv = g.inv()
    n = 4

    Gamma = christoffels_exact(coords, g, ginv, n)
    R_components = {}
    for mu in range(4):
        for nu in range(mu, 4):
            R_components[(mu, nu)] = ricci_exact(coords, Gamma, mu, nu, n)
    Rscalar = sum(ginv[mu, mu] * R_components[(mu, mu)] for mu in range(4))

    def G(mu, nu):
        Rmn = R_components[(mu, nu)] if mu <= nu else R_components[(nu, mu)]
        gmn = g[mu, nu] if mu == nu else 0
        return Rmn - sp.Rational(1, 2) * gmn * Rscalar

    print("  Christoffels/Ricci/G(mu,nu) rebuilt from the EXACT (unexpanded)")
    print("  metric -- same machinery, same positive controls (background")
    print("  Ricci vs textbook FRW; G_00/G_12 already verified in P48) apply")
    print("  unchanged; not re-run here to avoid duplicating P48's own work.")
    print("  NOTE: FINDING_P48 computed the full upper-triangle R_components")
    print("  dict (all mu<=nu pairs, including (0,1)) but only EXTRACTED")
    print("  G_00 and G_12 -- G_01 was already implicitly available, simply")
    print("  never pulled out. This file pulls it out.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- extract linearized G_01 (general FRW, not yet reduced)")
    print("-" * 78)
    G01_lin = sp.simplify(sp.diff(G(0, 1), eps).subs(eps, 0))
    print(f"  G_01^(1) = {G01_lin}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- C1/C2: gradient/curl-free structure, checked directly")
    print("(Bianchi-identity consequence for a scalar-only perturbation, not")
    print("just asserted)")
    print("-" * 78)
    print("  For this metric ansatz (no vector mode anywhere), G_0i^(1) must")
    print("  be a pure gradient of some scalar F(t,x,y,z): G_0i^(1)=d_i[F].")
    print("  A genuine vector-sourced piece would show up as a non-zero curl.")
    print("  G_02^(1), computed independently (not via a symbol-swap trick --")
    print("  sympy's subs on Function/Derivative objects is unreliable for")
    print("  that; computed fresh from the same G(mu,nu) machinery instead):")
    G02_lin = sp.simplify(sp.diff(G(0, 2), eps).subs(eps, 0))
    print(f"  G_02^(1) = {G02_lin}")
    print("  Expected form by the SAME physical structure as G_01 (isotropic")
    print("  ansatz -- x and y enter identically), checked directly:")
    expected_G02 = 2 * sp.diff(sp.diff(Psi, t), y) + 2 * (sp.diff(a, t) / a) * sp.diff(Phi, y)
    assert sp.simplify(G02_lin - expected_G02) == 0, (
        "G_02 does not match 2*d_y(Psi_dot)+2*H*d_y(Phi) -- unexpected "
        "anisotropy or an algebra error, re-check before proceeding"
    )
    print("  -> CONFIRMED: G_02^(1) = 2*d_y(Psi_dot) + 2*H*d_y(Phi), the same")
    print("     structure as G_01^(1) with x->y, exactly as isotropy requires.")
    print("  Curl check: d(G_01)/dy - d(G_02)/dx must vanish identically if")
    print("  G_0i is a pure gradient (necessary, not sufficient, condition):")
    curl_check = sp.simplify(sp.diff(G01_lin, y) - sp.diff(G02_lin, x))
    print(f"  d(G_01)/dy - d(G_02)/dx = {curl_check}")
    assert curl_check == 0, (
        "C2: G_0i's curl does NOT vanish -- either an algebra error, or a "
        "genuine vector-sourced piece this scalar-only ansatz should not "
        "produce. Do not proceed to B2/compatibility until resolved."
    )
    print("  [CORRECTED after context-blind skeptic review, Step 8a] The")
    print("  curl vanishing here is NOT independent evidence beyond the")
    print("  isotropy assertion just above: once G_02 is asserted to equal")
    print("  G_01's own pattern with x->y (a real, non-trivial check on its")
    print("  own, verified against the independently-computed G(0,2)), the")
    print("  curl vanishing is then a Schwarz-theorem TAUTOLOGY")
    print("  (d_y*d_x[F] - d_x*d_y[F] = 0 for ANY scalar F, whether F is the")
    print("  physically correct one or not) -- it cannot fail once isotropy")
    print("  is confirmed, and therefore adds ZERO independent evidence for")
    print("  the FORMULA'S correctness beyond what the isotropy check above")
    print("  already established. Retracted as originally overclaimed.")
    print("  -> C1 PARTIALLY addressed: curl-free structure and isotropy are")
    print("     confirmed, but this alone does not verify the formula's own")
    print("     coefficients/signs are correct. Part 5 (revised) addresses")
    print("     that separately, with a genuinely discriminating check.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- explicit scalar potential F such that G_01=d_x(F)")
    print("-" * 78)
    print("  Integrate G_01^(1) with respect to x to find F (up to a")
    print("  y,z,t-dependent integration 'constant', checked to be genuinely")
    print("  x-independent, not assumed):")
    F_candidate = sp.integrate(G01_lin, x)
    residual = sp.simplify(sp.diff(F_candidate, x) - G01_lin)
    assert residual == 0, "integration failed to reproduce G_01 by direct differentiation"
    print(f"  F (candidate, up to a function of t,y,z) = {F_candidate}")
    print("  Integration-consistency check: d(F)/dx - G_01 = 0 (script")
    print("  assertion above) -- confirms the integration correctly inverts")
    print("  the derivative, nothing more (F itself is expected to retain")
    print("  its own x-dependence through Phi(t,x,y,z) and Psi(t,x,y,z) --")
    print("  a d^2(F)/dx^2=0 check would be WRONG here, not a real test;")
    print("  [CORRECTED, skeptic-caught] removed a misleading printout that")
    print("  implied otherwise in the original version of this script.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- [CORRECTED after context-blind skeptic review, Step 8a]")
    print("direct independence checks, replacing a substitution-based static")
    print("check shown to have ~zero discriminating power")
    print("-" * 78)
    print("  ORIGINAL version of this script used")
    print("  'G01_lin.subs({d(Psi)/dt:0, d(Phi)/dt:0, d(a)/dt:0})' as a")
    print("  'static limit' check, claimed to catch spurious extra terms.")
    print("  Independently re-verified (standalone sympy check, BEFORE")
    print("  accepting the skeptic's critique) that this claim was WRONG: in")
    print("  sympy 1.14.0, .subs() on a first-derivative Derivative object")
    print("  propagates through NESTED/higher derivatives in a way that")
    print("  silently zeroes out terms it should NOT catch -- tested six")
    print("  deliberately-wrong variants of the formula (wrong coefficient,")
    print("  wrong sign, missing term, an extra Psi_ddot term, an extra")
    print("  a_ddot term) and ALL SIX passed the substitution-based check")
    print("  trivially, including cases the skeptic itself did not expect to")
    print("  pass. The check had ESSENTIALLY ZERO discriminating power, not")
    print("  merely 'weaker than claimed'. Retracted, not merely reframed.")
    print()
    print("  REPLACED with the SAME direct-independence-assertion pattern")
    print("  FINDING_P48 already established (after ITS OWN skeptic review)")
    print("  for G_12 -- checking the coefficient of each higher-derivative")
    print("  atom directly via sp.diff(), not via a substitution that can")
    print("  silently propagate through nested Derivative objects:")
    dG01_dPsiddot = sp.diff(G01_lin, sp.diff(Psi, t, 2))
    dG01_dPhiddot = sp.diff(G01_lin, sp.diff(Phi, t, 2))
    dG01_daddot = sp.diff(G01_lin, sp.diff(a, t, 2))
    print(f"    d(G_01^(1))/d(Psi_ddot) = {dG01_dPsiddot}")
    print(f"    d(G_01^(1))/d(Phi_ddot) = {dG01_dPhiddot}")
    print(f"    d(G_01^(1))/d(a_ddot)   = {dG01_daddot}")
    assert dG01_dPsiddot == 0
    assert dG01_dPhiddot == 0
    assert dG01_daddot == 0
    print("  -> CONFIRMED, all three: G_01^(1) has zero dependence on any")
    print("     second time-derivative of Psi, Phi, or a -- genuinely")
    print("     discriminating (a formula WITH such a term, e.g. the")
    print("     'extra Psi_ddot' variant tested above, would have a nonzero")
    print("     derivative here and FAIL this specific check).")
    print()
    print("  [HONEST LIMITATION, stated explicitly, not smuggled past] These")
    print("  independence checks, LIKE the retracted substitution check, do")
    print("  NOT by themselves rule out a wrong COEFFICIENT or wrong SIGN on")
    print("  the surviving Psi_dot/H*Phi terms (e.g. '5*H*Phi_,x' instead of")
    print("  '2*H*Phi_,x' would pass every check in this file identically).")
    print("  The strongest evidence for the formula's correctness remains:")
    print("  (a) it is derived from FINDING_P48's own already-verified exact")
    print("  Christoffel/Ricci machinery, reused verbatim, not hand-typed;")
    print("  (b) no EXTERNAL (textbook-citation) check is attempted here,")
    print("  deliberately, per FINDING_P48's own convention-labeling caveat")
    print("  (Phi/Psi role assignment is not universal across sources) --")
    print("  this is a real, stated gap, not resolved by this finding.")

    print("\n" + "=" * 78)
    print("VERDICT [CORRECTED after context-blind skeptic review, Step 8a]")
    print("=" * 78)
    print("C1 CONFIRMED, with two evidentiary corrections applied: G_0i^(1)=")
    print("2*d_x(Psi_dot+H*Phi), derived from the SAME exact-metric +")
    print("eps-linearization machinery FINDING_P48 already verified (reused")
    print("verbatim), has the required curl-free gradient structure for a")
    print("scalar-only perturbation (Part 3) -- though the curl check itself")
    print("is a Schwarz-theorem tautology given the isotropy assertion, not")
    print("independent evidence (retracted from the original overclaim). The")
    print("formula has zero dependence on any second time-derivative (Part 5,")
    print("REPLACING a substitution-based static-limit check independently")
    print("shown to have ~zero discriminating power in this sympy version).")
    print("Neither check rules out a wrong coefficient or sign on the")
    print("surviving terms -- stated as an honest, unresolved limitation, not")
    print("smuggled past. The strongest evidence for correctness remains")
    print("reuse of P48's own already-verified exact Christoffel/Ricci")
    print("machinery. No genuinely EXTERNAL (textbook-citation) check is")
    print("attempted here, deliberately, per P48's own convention-labeling")
    print("caveat -- a real, stated gap for a future step to close if needed.")
    print()
    print("This supplies ONLY the Einstein momentum-CONSTRAINT side (LHS")
    print("geometry) of the user's refined Step B milestone. It is explicitly")
    print("NOT the matter Euler equation (KG-B1a) -- that requires varying")
    print("the coupled matter+phi action directly (nabla_mu T_m^munu=Q^nu,")
    print("Q sourced by the g*rho*phi coupling), a separate, not-yet-started")
    print("step (B2). Comparing B1's G_0i to B2's matter momentum-")
    print("conservation equation to extract G_matter(a,k) and test the")
    print("user's own pre-registered H0/H1/H2 split is a THIRD, also")
    print("not-yet-started step (the compatibility check) -- none of that")
    print("is attempted here, kept out of scope per this campaign's")
    print("established granularity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
