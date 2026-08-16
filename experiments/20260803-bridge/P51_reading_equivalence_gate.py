"""P51 -- Reading-1/Reading-2 field-redefinition equivalence gate. Tests
whether FINDING_P39's two candidate readings of [g] are two PARAMETRIZATIONS
of the same physics (representational ambiguity) or genuinely inequivalent
theories (requiring an external physical anchor to choose between them).

PRE-REGISTERED (user's framing, refined: lambda=alpha*c, alpha a
dimensionless constant NOT assumed =1 -- must come out of the computation
or be explicitly flagged as undetermined):
  E1 -- full equivalence: a single lambda preserves S, g*phi, A*g^2,
        m_eff/m, the field equation, and F, with d_tau UNCHANGED.
        Verdict: R1/R2 ambiguity is REPRESENTATIONAL, not physical.
  E2 -- partial equivalence: dimensions and A*g^2 transform correctly, but
        at least one physical action term does not. Verdict: the finding
        localizes the REAL gap to a specific term.
  E3 -- inequivalent: no single lambda transforms g, phi, A together.
        Verdict: an external physical anchor is genuinely needed.

HARD KILL CRITERION (stated before any computation): the SAME lambda must
simultaneously transform phi, g, A, S, m_eff, F. Partial matches (some
invariants preserved, others not, under the SAME lambda) are E2, not E1.

RED-TEAM TESTS, pre-registered:
  (a) Round-trip: R1->R2->R1 (via lambda then 1/lambda) must EXACTLY
      recover phi_1, g_1, A_1.
  (b) lambda->2*lambda: does a DIFFERENT lambda value also leave both
      Reading definitions satisfied?

[CORRECTED after context-blind skeptic review, Step 8a -- FIRST TRUE-KILL-
ADJACENT VERDICT in this whole sub-arc, not a framing fix] The original
version of this script concluded "E1 confirmed at the structural/
dimensional level." The skeptic found the pre-registered test ITSELF was
mis-designed and RETRACTED that headline, for two compounding reasons,
BOTH independently re-verified symbolically before accepting:

(1) Part 2's "two independent routes to [lambda] agree" was NOT
independent evidence -- it is a FORCED ALGEBRAIC IDENTITY. Both routes
reduce, via direct substitution (g_R2:=c/phi_R1, phi_R2 self-consistently
re-derived from the SAME g*m*phi=energy template), to the LITERAL SAME
symbolic expression energy/(c*mass) -- not merely dimensionally
coincident, but algebraically identical before any numbers are computed.
The original claim "there was no a priori reason these two ratios needed
to coincide" was FALSE -- there was an exact algebraic reason, traced
explicitly in Part 2 below.

(2) Parts 3-6 (interaction, force, field equation, worldline), already
shown to hold for ANY lambda, therefore have ZERO power to discriminate
E1 from E3 -- NOT merely "not independent evidence for lambda=c
specifically" as the original text hedged, but genuinely UNINFORMATIVE
about whether R1 and R2 are related AT ALL: ANY two dimensionally-
consistent (phi,g,A) triples sharing this Lagrangian's general gauge-
covariance structure would ALSO pass Parts 3-6, whether or not they
encode the same physics. The pre-registered "hard kill criterion" itself
was not actually capable of distinguishing its own stated alternatives.

CORRECTED VERDICT: E1-vs-E3 for R1/R2 specifically is UNDETERMINED by
this analysis -- not confirmed, not refuted. What DOES survive, kept
below: the dimension arithmetic itself; the theory's general gauge-
covariance (a real, useful fact in its own right); and P50A's
ghat*phibar invariance, which does NOT depend on resolving R1 vs R2 (it
holds for the WHOLE gauge family regardless).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


# P39's own dimension-tuple helpers, reused verbatim (third time this
# sub-arc -- P39, P50B, now P51).
def dmul(a, b):
    return tuple(x + y for x, y in zip(a, b, strict=True))


def dpow(a, n):
    n = sp.Rational(n)
    return tuple(x * n for x in a)


def ddiv(a, b):
    return dmul(a, dpow(b, -1))


def dsub(a, b):
    return tuple(x - y for x, y in zip(a, b, strict=True))


MASS, LENGTH, TIME = (1, 0, 0), (0, 1, 0), (0, 0, 1)
DIMLESS = (0, 0, 0)


def fmt(d):
    return f"kg^{d[0]} m^{d[1]} s^{d[2]}"


def main():
    print("=" * 78)
    print("P51 -- Reading-1/Reading-2 field-redefinition equivalence gate")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nPRE-REGISTERED: E1 (representational) / E2 (localized gap) /")
    print("E3 (genuinely inequivalent, need external anchor).")
    print("HARD KILL: the SAME lambda must transform phi, g, A, S, m_eff, F")
    print("together. lambda=alpha*c -- alpha NOT assumed =1.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- Reading 1 / Reading 2 dimension tuples, reused from")
    print("FINDING_P39 and FINDING_P50B (not re-derived)")
    print("-" * 78)
    c_dim = ddiv(LENGTH, TIME)
    energy_dim = dmul(MASS, dpow(c_dim, 2))
    G_N_dim = ddiv(dpow(LENGTH, 3), dmul(MASS, dpow(TIME, 2)))
    phi_R1 = (0, 2, -2)
    g_R1 = DIMLESS
    # [A] under Reading 1, from P50B's own kinetic-term derivation:
    Ldensity_dim = ddiv(energy_dim, dpow(LENGTH, 3))

    def A_from_phi(phi_dim):
        gradphi2 = ddiv(dpow(phi_dim, 2), dpow(LENGTH, 2))
        C_dim = ddiv(Ldensity_dim, gradphi2)
        return dpow(C_dim, -1)

    A_R1 = A_from_phi(phi_R1)
    g_R2 = ddiv(c_dim, phi_R1)
    phi_R2 = ddiv(energy_dim, dmul(g_R2, MASS))
    A_R2 = A_from_phi(phi_R2)
    print(f"  [phi]_R1 = {fmt(phi_R1)}   [g]_R1 = {fmt(g_R1)}   [A]_R1 = {fmt(A_R1)}")
    print(f"  [phi]_R2 = {fmt(phi_R2)}   [g]_R2 = {fmt(g_R2)}   [A]_R2 = {fmt(A_R2)}")
    assert A_R1 == G_N_dim
    assert A_R2 == dmul(G_N_dim, dpow(c_dim, 2))
    print(f"  [A]_R2 == [G_N*c^2]? {A_R2 == dmul(G_N_dim, dpow(c_dim, 2))}  (CONFIRMED)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 (Steps 1-2) -- [lambda] from TWO 'routes'")
    print("-" * 78)
    lam_from_phi = dsub(phi_R2, phi_R1)
    lam_from_g = dsub(g_R1, g_R2)
    print(f"  [lambda] from phi-route (phi_R2/phi_R1) = {fmt(lam_from_phi)}")
    print(f"  [lambda] from g-route   (g_R1/g_R2)      = {fmt(lam_from_g)}")
    assert lam_from_phi == lam_from_g == c_dim
    print(f"  Both routes agree: [lambda]={fmt(c_dim)}=[c].")

    print("\n  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL text called this")
    print("  agreement independent evidence ('no a priori reason these two")
    print("  ratios needed to coincide'). FALSE -- independently re-verified")
    print("  symbolically before accepting the skeptic's claim: both routes")
    print("  reduce to the LITERAL SAME expression, by direct substitution")
    print("  of how Reading 2 was constructed FROM Reading 1 in the first")
    print("  place (g_R2:=c/phi_R1, phi_R2 self-consistently re-derived from")
    print("  the SAME g*m*phi=energy template used for phi_R1):")
    energy_s, mass_s, c_s, phi_R1_s = sp.symbols("energy mass c phi_R1", positive=True, real=True)
    phi_R1_expr = energy_s / mass_s  # g_R1=1 (dimensionless bookkeeping unit)
    g_R2_expr = c_s / phi_R1_expr
    phi_R2_expr = energy_s / (g_R2_expr * mass_s)
    route_phi_expr = sp.simplify(phi_R2_expr / phi_R1_expr)
    route_g_expr = sp.simplify(1 / g_R2_expr)
    print(f"    phi_R2/phi_R1 = {route_phi_expr}")
    print(f"    g_R1/g_R2     = {route_g_expr}")
    identity_check = sp.simplify(route_phi_expr - route_g_expr)
    assert identity_check == 0, "the two routes are NOT algebraically identical"
    print(f"    difference = {identity_check}  -- IDENTICAL, not coincidental.")
    print("  -> This is a TAUTOLOGY, not independent confirmation: BOTH")
    print("     'routes' are the SAME equation (g*m*phi=energy) rearranged,")
    print("     forced by construction the moment g_R2 was defined as")
    print("     c/phi_R1 and phi_R2 was re-derived from the same template.")
    print("     Part 2 provides ZERO discriminating evidence for E1 vs E3.")

    lam_from_A = dsub(A_R2, A_R1)
    expected_lam2 = dpow(c_dim, 2)
    assert lam_from_A == expected_lam2
    print(f"\n  [A]_R2/[A]_R1 = {fmt(lam_from_A)} == [lambda]^2 = {fmt(expected_lam2)}")
    print("  (a direct algebraic consequence of the same forced identity")
    print("  above, via A=1/C's own dependence on phi^2 -- not independent")
    print("  either.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 (Step 3) -- interaction invariant, for a GENERIC lambda")
    print("(NOT fixed to c) -- tests general covariance, not evidence")
    print("specific to lambda=c")
    print("-" * 78)
    g, phi, c_sym, lam = sp.symbols("g phi c lambda", positive=True, real=True)
    g2 = g / lam
    phi2 = lam * phi
    inv_gphi = sp.simplify(g * phi - g2 * phi2)
    assert inv_gphi == 0
    print(f"  g*phi - g2*phi2 = {inv_gphi}  (CONFIRMED invariant, any lambda)")

    meff_orig = 1 - (g / c_sym) * phi
    meff_transformed = 1 - (g2 / c_sym) * phi2
    meff_diff = sp.simplify(meff_orig - meff_transformed)
    assert meff_diff == 0
    print("  1-(g/c)*phi literal formula (P33's own m_eff/m):")
    print(f"    original = {meff_orig}")
    print(f"    transformed = {sp.simplify(meff_transformed)}")
    print(f"    difference = {meff_diff}  (CONFIRMED invariant, any lambda)")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a, STRENGTHENED correction] The ORIGINAL")
    print("  text said these checks are 'not independent evidence that")
    print("  lambda=c specifically' -- true but understated. The skeptic")
    print("  went further, correctly: since Parts 3-6 hold for ANY lambda,")
    print("  they have ZERO power to discriminate E1 from E3 AT ALL -- not")
    print("  just 'not specific to lambda=c'. ANY two dimensionally-")
    print("  consistent (phi,g,A) triples sharing this Lagrangian's general")
    print("  gauge-covariance structure would ALSO pass Parts 3-6, whether")
    print("  or not they encode the same physics. The pre-registered 'hard")
    print("  kill criterion' (same lambda transforms phi,g,A,S,m_eff,F) is")
    print("  therefore NOT capable, by construction, of distinguishing its")
    print("  own two stated alternatives (E1 vs E3) -- this is a genuine")
    print("  design flaw in the pre-registration itself, not merely an")
    print("  inconclusive result.")
    print()
    print("  [P50A CONSEQUENCE, SURVIVES the correction] Since ghat:=g/c, and")
    print("  the check above shows (g/c)*phi is invariant for ANY field")
    print("  redefinition of this type:")
    print("    ghat_2*phibar_2 = ghat_1*phibar_1   for ANY lambda")
    print("  -> P50A's mu_metric=1-ghat*phibar correction is CONFIRMED")
    print("  field-redefinition invariant, regardless of which Reading (or")
    print("  any other field normalization) is used -- this resolves the")
    print("  'is mu_metric itself convention-dependent' concern from P50A,")
    print("  independent of resolving R1 vs R2.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 (Step 4) -- force invariant, symbolic identity AND")
    print("substitution into the actual static force formula (not just a")
    print("relabeled copy of the symbolic check)")
    print("-" * 78)
    C, M, r = sp.symbols("C M r", positive=True, real=True)
    A_sym = 1 / C
    C2 = C / lam**2
    inv_Ag2 = sp.simplify(A_sym * g**2 - (1 / C2) * g2**2)
    assert inv_Ag2 == 0
    print(f"  A*g^2 - A2*g2^2 = {inv_Ag2}  (CONFIRMED invariant, any lambda)")

    def force(C_val, g_val):
        return g_val**2 * M / (4 * sp.pi * C_val * r**2)

    F1 = force(C, g)
    F2 = force(C2, g2)
    force_diff = sp.simplify(F1 - F2)
    assert force_diff == 0
    print(f"  F(C,g) = {F1}")
    print(f"  F(C2,g2) = {sp.simplify(F2)}")
    print(f"  difference = {force_diff}  (CONFIRMED identical, any lambda)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 (Step 5) -- full field equation, general C, substituted --")
    print("stronger than checking individual terms in isolation")
    print("-" * 78)
    t, x, y, z = sp.symbols("t x y z", real=True)
    a_t = sp.Function("a")(t)
    rho = sp.Function("rho")(t, x, y, z)
    phi1_field = sp.Function("phi1")(t, x, y, z)
    H = sp.diff(a_t, t) / a_t

    def EOM(phi_field, C_val, g_val):
        lap = sp.diff(phi_field, x, 2) + sp.diff(phi_field, y, 2) + sp.diff(phi_field, z, 2)
        return (
            C_val * (sp.diff(phi_field, t, 2) + 3 * H * sp.diff(phi_field, t))
            - C_val * lap / a_t**2
            - g_val * rho
        )

    EOM_R1 = EOM(phi1_field, C, g)
    phi2_field = lam * phi1_field
    EOM_R2 = EOM(phi2_field, C2, g2)
    eom_check = sp.simplify(EOM_R2 - EOM_R1 / lam)
    assert eom_check == 0, "EOM does not transform with a common nonzero factor"
    print("  EOM_R2 - EOM_R1/lambda = 0 (CONFIRMED) -- EOM_R2 = EOM_R1/lambda")
    print("  EXACTLY: a common nonzero multiplicative factor (1/lambda, which")
    print("  is nonzero for any finite lambda), not changing the solution")
    print("  set. This is a STRONGER check than verifying individual terms")
    print("  separately -- the WHOLE equation transforms together.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 6 (Step 6) -- worldline gate")
    print("-" * 78)
    print("  The transformation (phi->lambda*phi, g->g/lambda, C->C/lambda^2)")
    print("  touches ONLY field-space quantities (phi, g, C/A) -- it contains")
    print("  no reference anywhere to d_tau, x^mu, or any spacetime")
    print("  coordinate. FINDING_P21's own worldline coupling term")
    print("  (Sum_i int d_tau [g*m_i+p_i.grad] phi(x_i)) couples g*phi")
    print("  exactly as in Part 3 above (already shown invariant) -- d_tau")
    print("  itself is a property of the particle's spacetime trajectory,")
    print("  structurally independent of how the SEPARATE scalar field phi")
    print("  is normalized. PASS: no re-interpretation of d_tau, x^mu, or")
    print("  the c-convention in spacetime is required or implied anywhere")
    print("  in this transformation.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 7 -- red-team (a): round-trip R1->R2->R1")
    print("-" * 78)
    lam_inv = 1 / lam
    phi1_s = sp.Symbol("phi1", real=True)
    phi2_s = lam * phi1_s
    g2_s = g / lam
    C2_s = C / lam**2
    phi3_s = lam_inv * phi2_s
    g3_s = g2_s / lam_inv
    C3_s = C2_s / lam_inv**2
    rt_phi = sp.simplify(phi3_s - phi1_s)
    rt_g = sp.simplify(g3_s - g)
    rt_C = sp.simplify(C3_s - C)
    assert rt_phi == 0 and rt_g == 0 and rt_C == 0
    print(f"  phi3-phi1={rt_phi}, g3-g={rt_g}, C3-C={rt_C} -- ALL ZERO (CONFIRMED)")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL text called this a")
    print("  'red-team test' passing a 'negative control'. The skeptic")
    print("  correctly noted this is a TRIVIAL algebraic consequence of")
    print("  invertibility -- for ANY transformation of the form")
    print("  x->f(lambda)*x, applying f(lambda) then f(1/lambda) returns x")
    print("  by construction; this cannot fail unless the inverse-")
    print("  transformation bookkeeping itself contains an arithmetic error.")
    print("  DOWNGRADED: this is a basic correctness check on the bookkeeping")
    print("  (worth keeping -- it would have caught a sign/inverse error),")
    print("  NOT a test with genuine falsification power over the E1/E3")
    print("  question.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 8 -- red-team (b): lambda -> 2*lambda, stated honestly")
    print("-" * 78)
    # dimension of alpha*c is [c] for ANY dimensionless alpha (2, 7, pi, ...)
    # -- a pure number carries no dimension, so the tuple is identical.
    assert dpow(c_dim, 1) == c_dim  # trivial, but states the point as a check
    print("  A dimension tuple carries NO dimensionless prefactor information")
    print("  by construction -- [2*c]=[c] exactly, as a TUPLE. This means:")
    print("  the dimensional regression in Part 2 CANNOT distinguish")
    print("  lambda=c from lambda=2*c, lambda=pi*c, etc. -- ALL give the")
    print("  IDENTICAL [phi]_R2, [g]_R2, [A]_R2 predictions.")
    print()
    print("  [STATED HONESTLY, not glossed over, per pre-registration] This")
    print("  is NOT evidence of unresolved gauge freedom specific to R1/R2")
    print("  -- it is an UNAVOIDABLE, EXPECTED limitation of pure dimensional")
    print("  analysis: alpha (in lambda=alpha*c) is a genuinely FREE")
    print("  dimensionless number from THIS method's point of view. Fixing")
    print("  alpha numerically requires input beyond dimensional analysis")
    print("  (an explicit numeric convention from the original action, not")
    print("  attempted here) -- exactly as the user's own pre-registration")
    print("  anticipated ('если все формулы требуют именно alpha=1, это")
    print("  должно выйти из action/convention, а не быть принято заранее').")

    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("VERDICT [FULLY REWRITTEN after context-blind skeptic review,")
    print("Step 8a -- the ORIGINAL 'E1 confirmed' headline is RETRACTED,")
    print("not softened]")
    print("=" * 78)
    print("The pre-registered test was MIS-DESIGNED: its two load-bearing")
    print("pieces both turned out to carry ZERO power to discriminate E1")
    print("from E3, for two DIFFERENT reasons, both independently re-")
    print("verified symbolically before accepting either:")
    print("  (1) Part 2's 'two independent routes agree' is a FORCED")
    print("      algebraic identity (both routes reduce to the literal same")
    print("      expression energy/(c*mass)), not independent confirmation.")
    print("  (2) Parts 3-6, admittedly true for ANY lambda, cannot")
    print("      distinguish 'R1 and R2 are the same physics' from 'R1 and")
    print("      R2 are unrelated but each internally consistent with this")
    print("      Lagrangian's general covariance' -- the pre-registered")
    print("      'hard kill criterion' would pass for ANY two dimensionally-")
    print("      self-consistent readings, related or not.")
    print()
    print("CORRECTED VERDICT: E1-vs-E3 for R1/R2 SPECIFICALLY IS UNDETERMINED")
    print("by this analysis -- neither confirmed nor refuted. This is a")
    print("methodological finding (the test itself was uninformative), not")
    print("a null result about the physics.")
    print()
    print("WHAT SURVIVES, kept honestly:")
    print("  - The dimension arithmetic itself: [A]_R2=[G_N*c^2] exactly")
    print("    (Part 1), a correct, verified fact about P39's own numbers.")
    print("  - The theory's general gauge-covariance under field redefinition")
    print("    (Parts 3-6) -- a REAL, useful, previously only partly-")
    print("    established fact (FINDING_P50B covered gphi, Ag^2; this")
    print("    finding adds the full field-equation-level check and a")
    print("    direct force-substitution check) -- just not informative")
    print("    about R1 vs R2 specifically.")
    print("  - P50A CONSEQUENCE, UNCHANGED: ghat*phibar (hence")
    print("    mu_metric=1-ghat*phibar) is confirmed field-redefinition")
    print("    invariant for the WHOLE gauge family -- this conclusion never")
    print("    depended on resolving E1 vs E3 in the first place, since it")
    print("    holds for ANY lambda. P50A's own normalization worry remains")
    print("    resolved, entirely independent of this finding's retraction.")
    print()
    print("WHAT A GENUINELY DISCRIMINATING TEST WOULD NEED: something")
    print("sensitive to the READINGS' NUMERICAL relationship, not just their")
    print("shared dimensional template -- e.g. an independent physical")
    print("anchor (a measured force/coupling value under EITHER reading),")
    print("or a term in the action that is NOT automatically covariant under")
    print("field redefinition (this campaign has not identified one).")
    print("Pure dimensional/algebraic analysis, as attempted in P50B and")
    print("here, has reached its limit for this specific question.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
