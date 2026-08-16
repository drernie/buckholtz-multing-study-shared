"""P50B -- narrow, single-purpose step: is g_hat a physical coupling, or a
convention-dependent parameter? Restore the general kinetic normalization
C (A:=C^-1) that every finding since FINDING_P34 implicitly set to 1, and
audit field-rescaling invariance and dimensional consistency SEPARATELY
(user's own explicit instruction -- these are two different questions,
conflating them is a named kill-gate below).

PRE-REGISTERED before this script computed anything (user's own AOG-1
framing), three outcomes:
  B1 -- existing-normalization closure: A/C fully fixes SI bookkeeping
        without a new constant, but g*phibar remains its OWN independent
        invariant; force strength is separately controlled by A*g^2.
  B2 -- genuine missing scale: neither A nor canonical field normalization
        closes the dimensions; a genuinely NEW independent dimensional
        constant is needed -- serious underdetermination signal.
  B3 -- full invariant closure: after returning to the unnormalized action
        and re-canonicalizing, all physical source/force amplitudes
        express only via existing invariants, primarily A*g^2, and
        P50A's own correction also gets a well-defined invariant form
        without a new physical constant.
Stated preference (not to be treated as a result): B3 plausible, B1 a real
live alternative (A*g^2 controls fifth-force strength, g*phibar a SEPARATE
background amplitude) -- not to be favored a priori.

SIX KILL-GATES, named before any computation, checked explicitly below:
  KG1: dimensions must not be "fixed" by choosing a power of c alone.
  KG2: A must not be inserted post-hoc -- must be DERIVED from the
       original kinetic normalization.
  KG3: canonically-normalized and non-normalized fields must never be
       compared as if they were literally the same phi (distinct symbols
       phi vs phi_p used throughout).
  KG4: invariance must not be checked only via identically-constructed
       expressions -- Part 4 uses TWO genuinely different derivation
       routes (Lagrangian field-redefinition vs. physical force law via
       an independently-established Green's function).
  KG5: field-rescaling invariance must NOT be used to conclude SI-unit
       correctness -- Parts 2-4 (rescaling) and Part 5 (dimensions) are
       kept structurally separate, with an explicit statement that
       neither implies the other.
  KG6: the P22/P31 numeric bound is not used anywhere in this script.

DECISIVE CHECK (Part 4): canonicalize the general C-action in two
algebraically independent ways and check whether both give the same
physical coupling combination. g_canon=g/sqrt(C) must come OUT of the
computation, not be substituted as the expected answer.

[CORRECTED after context-blind skeptic review, Step 8a] Three real issues
found, all fixed with real computation, not softened language:
(1) Part 2's J-invariance assumption was unstated -- now named explicitly.
(2) Part 4's "two algebraically independent routes" overclaimed KG4:
Route 2 solves the EL equation from the SAME Lagrangian as Route 1 using
the SAME coupling for source and test particle -- their agreement is a
necessary consequence of standard variational calculus, not independent
physical evidence. Downgraded to "propagation-verification, not
independent derivation" -- still real and useful, just not what KG4
originally claimed.
(3) MAJOR: Part 5's "[A]=[G_N], reading-independent" claim was tested
directly (not just hedged) by self-consistently re-deriving [phi] under
P39's own Reading 2 (instead of holding phi fixed at its Reading-1 value,
which is what the original derivation silently did). Under this genuinely
independent re-derivation, [A] comes out as a COMPLETELY DIFFERENT
dimension, not [G_N] at all. The "reading-independent" claim is RETRACTED
-- [A]=[G_N] holds only under Reading 1, the convention this whole
campaign has used since P34. This directly changes the B1/B2/B3 verdict:
B2-strong (unconstrained new dimension) is ruled out only conditional on
Reading 1; B2-weak (a [G_N]-shaped but numerically distinct constant)
remains fully open; which of P39's two readings is correct remains the
open question this whole normalization program hinges on.
Also corrected: Part 6's "phibar is NOT a free parameter" overstated an
ODE's fixed evolution law into a fixed solution -- free initial
conditions remain unaccounted for, weakening the lean toward B3.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


# P39's own dimension-tuple helpers, reused verbatim (not reinvented) --
# matching this campaign's established anti-hand-algebra discipline.
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
    print("P50B -- rescaling + dimensional normalization audit: is g_hat")
    print("physical, or convention-dependent? One step: no Euler equation,")
    print("no external bounds, no numbers before P39's gap is closed.")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nPRE-REGISTERED (B1/B2/B3, stated before any computation below):")
    print("  B1: A/C closes SI bookkeeping, g*phibar stays a SEPARATE invariant")
    print("  B2: genuine missing scale -- underdetermined completion")
    print("  B3: full closure -- everything reduces to A*g^2 (and later")
    print("      A*g*kappa, A*kappa^2)")
    print("  Stated preference: B3 plausible but NOT favored a priori; B1 a")
    print("  real live alternative.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- general Lagrangian, kinetic normalization C explicit")
    print("(A:=C^-1), generalizing what every finding since P34 implicitly")
    print("fixed at C=1")
    print("-" * 78)
    print("  L = -(C/2)*(d phi)^2 + g*J*phi + ...   (user's own audit form,")
    print("  matching FINDING_P21's own S=int d^4x (1/2)(dphi)^2 + sum g*m*phi")
    print("  with C=1 implicit)")

    C, g, lam, A = sp.symbols("C g lambda A", positive=True, real=True)
    t_sym = sp.Symbol("t", real=True)
    phi_p_func = sp.Function("phi_p")  # phi_p: the field AFTER rescaling
    phi_p = phi_p_func(t_sym)
    J = sp.Symbol("J", real=True)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- field-rescaling transformation, DERIVED via direct")
    print("Lagrangian substitution (KG3: phi and phi_p kept as distinct")
    print("symbols throughout -- phi=phi_p/lambda, never conflated)")
    print("-" * 78)
    print("  Substitute phi = phi_p/lambda into L(phi;C,g), demand the")
    print("  result equals L(phi_p; C_p, g_p) for some C_p, g_p:")
    phidot_in_terms_of_phip = sp.diff(phi_p, t_sym) / lam
    L_original = sp.expand(-(C / 2) * phidot_in_terms_of_phip**2 + g * J * (phi_p / lam))
    print(f"    L(phi=phi_p/lambda; C,g) = {L_original}")

    C_p_predicted = C / lam**2
    g_p_predicted = g / lam
    L_target = sp.expand(
        -(C_p_predicted / 2) * sp.diff(phi_p, t_sym) ** 2 + g_p_predicted * J * phi_p
    )
    print(f"    L(phi_p; C_p=C/lambda^2, g_p=g/lambda) = {L_target}")
    assert sp.simplify(L_original - L_target) == 0, (
        "predicted transformation rules do not reproduce the Lagrangian exactly"
    )
    print("  -> CONFIRMED (not assumed): C_p=C/lambda^2, g_p=g/lambda exactly")
    print("     reproduce the substituted Lagrangian. A_p:=1/C_p=lambda^2*A")
    print("     follows algebraically.")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] AUXILIARY ASSUMPTION, stated explicitly:")
    print("  this derivation holds J fixed (unrescaled) while only phi is")
    print("  substituted -- i.e. J does NOT transform under phi->phi_p/lambda.")
    print("  Physically justified (J represents matter mass/density, which")
    print("  does not depend on how the SEPARATE scalar field phi is")
    print("  parametrized), but was an unstated assumption in the original")
    print("  version of this script -- exactly the kind of gap this")
    print("  campaign's audits are meant to catch. If J were instead assumed")
    print("  to transform (e.g. J_p=J/lambda), a DIFFERENT g_p would result --")
    print("  the transformation rules below hold GIVEN J-invariance, not as a")
    print("  universal fact independent of this choice.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- candidate invariants g*phi and A*g^2, CHECKED not assumed")
    print("-" * 78)
    phi_sym, A_sym = sp.symbols("phi A", positive=True, real=True)
    phi_p_sym = lam * phi_sym  # phi_p = lambda*phi (consistent with Part 2)
    g_p_sym = g / lam
    A_p_sym = A * lam**2

    inv1_orig = g * phi_sym
    inv1_transformed = sp.simplify(g_p_sym * phi_p_sym)
    print(f"  g*phi (original) = {inv1_orig}")
    print(f"  g_p*phi_p (transformed) = {inv1_transformed}")
    assert sp.simplify(inv1_orig - inv1_transformed) == 0
    print("  -> CONFIRMED invariant.")

    inv2_orig = sp.simplify(A_sym * g**2)
    inv2_transformed = sp.simplify(A_p_sym * g_p_sym**2)
    print(f"  A*g^2 (original) = {inv2_orig}")
    print(f"  A_p*g_p^2 (transformed) = {inv2_transformed}")
    assert sp.simplify(inv2_orig - inv2_transformed) == 0
    print("  -> CONFIRMED invariant.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- DECISIVE CHECK: canonicalize via TWO algebraically")
    print("independent routes (KG4). g_canon must come OUT of the")
    print("computation, not be substituted as the expected answer.")
    print("-" * 78)
    print("  Route 1 -- Lagrangian kinetic-coefficient canonicalization:")
    print("  solve C_p=1 for lambda directly.")
    lam_solution = sp.solve(sp.Eq(C / lam**2, 1), lam)
    lam_route1 = [s for s in lam_solution if s.is_positive or s == sp.sqrt(C)][0]
    g_canon_route1 = sp.simplify(g / lam_route1)
    print(f"    lambda = {lam_route1}  =>  g_canon (Route 1) = {g_canon_route1}")

    print("\n  Route 2 -- PHYSICAL force law, via the general-C Euler-Lagrange")
    print("  field equation + FINDING_P19's own already-established Green's")
    print("  function (Laplacian[1/(4*pi*r)]=-delta^3(x), reused not")
    print("  re-derived) -- a genuinely different computation, not a relabeled")
    print("  copy of Route 1:")
    M, r = sp.symbols("M r", positive=True, real=True)
    print("    General-C static EOM (Euler-Lagrange from Part 1's L, source")
    print("    J=M*delta^3(x)): -C*Laplacian(phi) = g*J")
    print("    => phi(r) = (g/C)*M/(4*pi*r) = g*A*M/(4*pi*r)")
    phi_r = g * (1 / C) * M / (4 * sp.pi * r)
    print(f"    phi(r) = {phi_r}")
    print("    Force on a like-coupled test mass (F=g*d(phi)/dr, magnitude):")
    force_general = sp.Abs(sp.simplify(g * sp.diff(phi_r, r)))
    print(f"    |F| (general C/A frame) = {force_general}")
    print()
    print("    Canonical-frame force (A_p=1 since C_p=1, coupling=g_canon):")
    force_canonical = g_canon_route1**2 * M / (4 * sp.pi * r**2)
    print(f"    |F'| (canonical frame, A_p=1, coupling g_canon) = {force_canonical}")
    match_check = sp.simplify(force_general - force_canonical)
    print(f"\n    |F| - |F'| = {match_check}")
    assert match_check == 0, (
        "Route 1 (Lagrangian) and Route 2 (physical force law) give "
        "DIFFERENT g_canon -- the decisive check FAILS"
    )
    print("  -> CONFIRMED: both routes agree exactly.")
    both_equal_Ag2 = sp.simplify(force_general - (1 / C) * g**2 * M / (4 * sp.pi * r**2))
    assert both_equal_Ag2 == 0
    print("  -> Both forms equal A*g^2*M/(4*pi*r^2) exactly.")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL text called Routes 1 and 2")
    print("  'two algebraically independent' derivations, claiming this")
    print("  satisfied KG4. The skeptic correctly found this overstated:")
    print("  Route 2 solves the EL field equation from the SAME Lagrangian as")
    print("  Route 1, and uses the SAME coupling g for both source and test")
    print("  particle -- once the Lagrangian and J-invariance (Part 2) are")
    print("  accepted, Route 1's and Route 2's agreement is a NECESSARY")
    print("  consequence of standard variational calculus, not two logically")
    print("  independent physical principles converging. A genuinely")
    print("  independent check would need to leave the Lagrangian-invariance")
    print("  manifold entirely (e.g. a scattering-amplitude or Ward-identity")
    print("  argument) -- not attempted here, out of this campaign's classical-")
    print("  field-theory scope.")
    print("  DOWNGRADED, not retracted: Route 2 remains a REAL, useful check")
    print("  -- it verifies that the abstract field-redefinition (Route 1)")
    print("  correctly propagates to an actual PHYSICAL, measurable quantity")
    print("  (the force law), catching implementation errors (e.g. a wrong")
    print("  Green's-function normalization or a dropped factor) that Route 1")
    print("  alone would not catch. But it is a propagation-verification, NOT")
    print("  independent evidence that g_canon=g/sqrt(C) is uniquely correct.")
    print("  KG4 is only PARTIALLY satisfied by this pair of routes.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- dimensional consistency of C/A, DERIVED from the kinetic")
    print("term alone (KG1, KG2: no c-power substitution, no post-hoc A).")
    print("Kept STRUCTURALLY SEPARATE from Parts 2-4's rescaling-invariance")
    print("checks (KG5) -- this is a DIFFERENT question, answered by a")
    print("DIFFERENT computation.")
    print("-" * 78)
    energy_dim = dmul(MASS, dpow(ddiv(LENGTH, TIME), 2))
    G_N_dim = ddiv(dpow(LENGTH, 3), dmul(MASS, dpow(TIME, 2)))
    print(f"  [energy] = {fmt(energy_dim)}   [G_N] = {fmt(G_N_dim)}")

    print("\n  [phi], reused from FINDING_P39's own established value (P39's")
    print("  own Reading 1, derived from g*m*phi=energy ASSUMING g")
    print("  dimensionless -- P39's own text, quoted exactly):")
    phi_dim_reading1 = (0, 2, -2)
    print(f"    [phi] (Reading 1) = {fmt(phi_dim_reading1)}")

    Ldensity_dim = ddiv(energy_dim, dpow(LENGTH, 3))
    print(f"\n  [Lagrangian density] = [energy]/[volume] = {fmt(Ldensity_dim)}")

    def A_from_phi(phi_dim):
        gradphi2 = ddiv(dpow(phi_dim, 2), dpow(LENGTH, 2))
        C_dim = ddiv(Ldensity_dim, gradphi2)
        return dpow(C_dim, -1)

    A_dim_reading1 = A_from_phi(phi_dim_reading1)
    print(f"  [A] required (Reading-1 phi) = {fmt(A_dim_reading1)}")
    print(f"  [G_N] = {fmt(G_N_dim)}")
    assert A_dim_reading1 == G_N_dim, (
        "[A] required by kinetic-term dimensional consistency under "
        "Reading-1 phi does NOT match [G_N] -- re-check"
    )
    print("  -> [A]=[G_N] exactly under Reading-1 phi. NOT by matching a")
    print("     power of c (KG1: no c anywhere in this derivation), and NOT")
    print("     inserted post-hoc (KG2: derived from the kinetic term's own")
    print("     normalization).")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL text claimed this result")
    print("  is 'reading-independent' because '[phi] only, no [g] anywhere'")
    print("  appears in the arithmetic above. The skeptic found this")
    print("  MISLEADING: [phi]=kg^0*m^2*s^-2 was not derived free of any")
    print("  g-assumption -- P39's own STEP 2 derived it by ASSUMING g")
    print("  dimensionless (Reading 1) in g*m*phi=energy. P39's own Reading 2")
    print("  did NOT re-derive [phi] independently -- it held phi FIXED at")
    print("  its Reading-1 value while asking what [g] the P33 formula would")
    print("  then require. This is P39's own methodological choice, not a")
    print("  mathematical necessity.")
    print()
    print("  DIRECT TEST, not just a hedge: what if phi is instead")
    print("  SELF-CONSISTENTLY re-derived from g*m*phi=energy using Reading")
    print("  2's OWN [g] value (kg^0*m^-1*s^1, from P39's own P33-derived")
    print("  requirement), instead of being held fixed at the Reading-1 value?")
    c_dim = ddiv(LENGTH, TIME)
    g_reading2_dim = ddiv(c_dim, phi_dim_reading1)
    print(f"    [g] Reading 2 (P39's own P33-derived value) = {fmt(g_reading2_dim)}")
    phi_dim_selfconsistent_r2 = ddiv(energy_dim, dmul(g_reading2_dim, MASS))
    print(
        f"    [phi] self-consistently re-derived under Reading 2 = {fmt(phi_dim_selfconsistent_r2)}"
    )
    print(f"    (DIFFERENT from Reading-1 phi: {fmt(phi_dim_reading1)})")
    assert phi_dim_selfconsistent_r2 != phi_dim_reading1
    A_dim_reading2 = A_from_phi(phi_dim_selfconsistent_r2)
    print(f"    [A] required under THIS self-consistent Reading-2 phi = {fmt(A_dim_reading2)}")
    print(f"    == [G_N]? {A_dim_reading2 == G_N_dim}")
    assert A_dim_reading2 != G_N_dim, (
        "unexpected: self-consistent Reading-2 phi ALSO gives [A]=[G_N] -- "
        "the claimed reading-dependence is not real, re-check"
    )
    print("  -> CONFIRMED: under a genuinely self-consistent re-derivation of")
    print("     phi (not P39's own fixed choice), [A] does NOT come out as")
    print("     [G_N] at all -- a completely different dimension. The")
    print("     'reading-independent, [G_N]-shaped' conclusion is REAL only")
    print("     under P39's own Reading-1 convention (the one this whole")
    print("     campaign has implicitly used since P34's g-hat:=g/c), not a")
    print("     structural fact independent of which reading is ultimately")
    print("     correct. RETRACTED as originally overclaimed.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 6 -- connecting to P50A: is g*phibar a SEPARATE invariant")
    print("(B1), or does it reduce further (B3)?")
    print("-" * 78)
    print("  g*phi is invariant under rescaling (Part 3) -- but FINDING_P46's")
    print("  own background field equation (already established, reused not")
    print("  re-derived here -- this is phi's OWN equation of motion, NOT the")
    print("  matter Euler equation the user's scope explicitly excludes)")
    print("  ALREADY determines phibar dynamically:")
    print("    phibar_ddot + 3*H*phibar_dot = g_hat*rhobar   (FINDING_P46)")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL text said phibar is 'NOT a")
    print("  free background parameter' -- the skeptic correctly flagged this")
    print("  as overstated: a second-order ODE's EVOLUTION LAW being fixed")
    print("  does not mean its SOLUTION is fixed -- phibar(t) generically")
    print("  still depends on TWO free integration constants (phibar(t0),")
    print("  phibar_dot(t0)) unless a specific attractor/scaling solution is")
    print("  independently established (NOT done anywhere in this campaign).")
    print("  CORRECTED: phibar's TIME-EVOLUTION is fixed given initial")
    print("  conditions, but phibar itself is not thereby reduced to a pure")
    print("  function of A*g^2 and the matter background alone -- the initial")
    print("  conditions are a further, unaccounted-for freedom. The lean")
    print("  toward B3 over B1 is WEAKER than originally stated -- suggestive")
    print("  at most, not even 'suggestive but not proof' as before; genuinely")
    print("  open pending either an attractor argument or explicit IC tracking.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 7 -- B1/B2/B3 verdict")
    print("-" * 78)
    print("  [SKEPTIC-CAUGHT, Step 8a] B2's verdict is SPLIT, per the skeptic's")
    print("  own precise reading of the pre-registered wording. B2 said 'a")
    print("  genuinely new independent dimensional constant is needed' -- a")
    print("  same-DIMENSION-but-numerically-different-from-G_N constant still")
    print("  fits that description; the original verdict silently narrowed B2")
    print("  to mean only 'a new dimension-TYPE', which Part 5 does rule out")
    print("  UNDER READING 1. Given Part 5's own correction (the [G_N] result")
    print("  is Reading-1-specific, NOT reading-independent as first claimed):")
    print()
    print("  B2-strong (a totally unconstrained new DIMENSION): NOT SUPPORTED")
    print("  under Reading 1 specifically -- [A] is fully pinned to [G_N]'s")
    print("  dimension there. But Part 5's correction shows this does NOT")
    print("  generalize to Reading 2 -- under a self-consistent Reading-2 phi,")
    print("  the required dimension is neither [G_N] nor otherwise pinned by")
    print("  anything already known in this campaign. B2-strong is therefore")
    print("  ONLY ruled out conditional on Reading 1 being correct -- which")
    print("  reading is correct remains P39's own, still-open question.")
    print("  B2-weak (a [G_N]-shaped constant numerically DIFFERENT from")
    print("  G_N): NOT RULED OUT by this finding -- dimensional analysis")
    print("  alone cannot distinguish 'A=G_N' from 'A=7*G_N' from an unrelated")
    print("  constant of the same dimension.")
    print()
    print("  B1 vs B3 (does g*phibar reduce further, or stay independent):")
    print("  NOT RESOLVED. Part 6's evidence for B3, after correction, is")
    print("  weaker than the original text stated -- phibar's free initial")
    print("  conditions remain unaccounted for.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Field-rescaling transformation rules (C_p=C/lambda^2, A_p=lambda^2*A,")
    print("g_p=g/lambda) DERIVED via direct Lagrangian substitution, GIVEN an")
    print("explicit J-invariance assumption (Part 2). g*phi and A*g^2")
    print("CONFIRMED invariant. Routes 1 and 2 (Part 4) converge exactly on")
    print("g_canon=g/sqrt(C) and force=A*g^2*M/(4*pi*r^2) -- but this is a")
    print("propagation-verification, not two logically independent")
    print("derivations (KG4 only PARTIALLY satisfied, corrected after skeptic")
    print("review). Dimensional audit (Part 5, corrected): [A]=[G_N]'s")
    print("dimension holds ONLY under P39's own Reading-1 phi convention --")
    print("under a genuinely self-consistent Reading-2 phi, [A] comes out as")
    print("a COMPLETELY DIFFERENT dimension, not [G_N] at all. The original")
    print("'reading-independent' claim is RETRACTED. B2-strong (unconstrained")
    print("new dimension) is ruled out ONLY conditional on Reading 1; B2-weak")
    print("(a [G_N]-shaped but numerically distinct constant) remains fully")
    print("open. B1-vs-B3 remains genuinely unresolved, weaker evidence for")
    print("B3 than originally stated (phibar's free initial conditions are")
    print("unaccounted for). Which of P39's two readings is correct remains")
    print("the actual open question this whole normalization program hinges")
    print("on -- NOT resolved by this finding, honestly narrower in scope")
    print("than the original version claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
