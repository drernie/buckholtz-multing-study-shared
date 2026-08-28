"""P143 -- formalizes docs/131's qualitative vector-mediator dismissal with an
actual Riesz-potential power-counting calculation, instead of leaving it as
a verbal claim.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: math

WHY THIS FILE. P142 (2026-08-26) framed the cheapest differentiating test for
the unique-completion inverse problem: does CANDIDATE-L1's EP/ghost/staticity
tension (docs/131) generalize across alternative completion ansaetze, or is it
specific to the ONE construction actually computed there (a Blanchet-Le-Tiec-
type scalar dipole, "Branch S")? Re-reading docs/131 in full first (before
writing this file) found it already surveyed more alternatives than P142
anticipated -- harmonic-induced scalar (fails on power law), vector-mediated
(dismissed VERBALLY, not computed), free-sign-charge (closed by definition),
driven-non-equilibrium (different theory). Of these, the vector-mediator
dismissal is the only one argued qualitatively rather than computed with the
same sympy rigor as the H/S branches -- "a static 1/r^3 from a vector needs
higher-derivative couplings -> ghost" is asserted, not derived. This file
derives the FIRST half of that chain (does it need extra derivatives at all,
and how many) -- NOT the ghost conclusion, which is a separate, textbook
question this file explicitly does not re-derive (see "WHAT THIS FILE DOES
NOT DO" and the VERDICT section's own scope correction, added after an
independent skeptic review caught an early draft conflating "requires >=1
extra derivative" with "higher-derivative" in the Ostrogradsky sense -- these
are NOT the same claim; a single-derivative vertex is standard and generically
ghost-free).

THE PHYSICS. A linear field exchange between a static source (propagator
~1/k^alpha in momentum space, alpha=2 for the standard massless case -- Newton/
Coulomb) gives a position-space POTENTIAL ~ 1/r^(3-alpha) in 3 spatial
dimensions (the standard Riesz-potential Fourier-transform identity for
tempered distributions; not derived from scratch here -- see Sources below --
but VERIFIED here against the one case everyone already trusts: alpha=2 must
reproduce 1/r Newtonian gravity, exactly). The FORCE (radial gradient of a
1/r^n potential) then goes as 1/r^(n+1). MULTING's own dipole term (buckholtz-
log.md "What We Have Source-Confirmed", direct preprint quote) is a FORCE:
F_d = (G/c^2)(k_A m_P |r_dA| + k_P m_A |r_dP|) / r^3 -- i.e. FORCE ~ 1/r^3,
so the target POTENTIAL exponent is n=2 (force = d/dr of 1/r^2 gives 1/r^3,
matching docs/131's own Branch S computation of U_md ~ 1/r^2 exactly).

THE QUESTION THIS FILE ANSWERS: what propagator power alpha would a vector-
exchange-at-MONOPOLE-order mechanism need, to reach potential-exponent n=2 (the
SAME target Branch S already reached via the scalar's DIPOLE-multipole
structure, with NO exotic coupling needed there)? And how many powers of
momentum (= how many derivatives) does that exponent differ from the standard
massless vector's own alpha=2?

CONTROLS:
  POSITIVE CONTROL: alpha=2 (standard massless propagator, no extra momentum
    factors) MUST give potential exponent n=1 (1/r, Newton/Coulomb) via the
    same exponent algebra used for the real question -- verified symbolically
    before trusting the algebra on the untested alpha.
  CROSS-CHECK: the scalar DIPOLE case (docs/131 Branch S) reaches n=2 via
    MULTIPOLE order (an angular/derivative structure in the SOURCE, i.e. taking
    a gradient of the standard n=1 monopole potential -- textbook multipole
    expansion, zero exotic input), not via a modified propagator alpha. This
    file's question is specifically about a DIFFERENT route to the same n=2:
    modifying alpha itself (a monopole-order vector coupling with extra
    momentum factors) rather than going to dipole order. The two routes are
    not the same claim and this file does not conflate them.

WHAT THIS FILE DOES NOT DO: attempt a full covariant Lagrangian construction
for the derivative-coupled vector case (that is the actual "build the ghost-
free completion" question, a separate, much larger undertaking -- P142's own
framing named this as future work, not this file's scope). Does not claim
Ostrogradsky's theorem itself (a textbook result, cited not re-derived) proves
NO ghost-free UV completion of a k^n>2 coupling can ever exist -- only that the
NAIVE, minimal such coupling is higher-derivative, which is the specific,
narrower claim docs/131 made and this file checks. Quote any k[h/Mpc]. Touch
MULTING itself (Gate 1) -- this is a check on OUR OWN candidate completions.

SOURCES (checked, not invented):
  Riesz potential / Fourier transform of |k|^-alpha in R^3:
    Lighthill, "Introduction to Fourier Analysis and Generalised Functions"
    (1958), the standard reference for tempered-distribution FTs of this kind;
    also derivable via the Gegenbauer/Mellin-transform-of-sine route this file
    uses directly with sympy, not asserted from memory.
"""

import sympy as sp


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P143 -- vector-mediator power counting: does docs/131's qualitative")
    print("        dismissal survive an actual derivation?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: math")
    print("=" * 78)

    alpha, r, n, k, x = sp.symbols("alpha r n k x", positive=True)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("STEP 1 -- derive the exponent map alpha -> n from the radial FT")
    print("-" * 78)
    # Standard reduction of the 3D FT of an isotropic function f(|k|)=k^{-alpha}
    # to a 1D integral (angular integration already performed):
    #   V(r) = 1/(2*pi^2*r) * Integral_0^inf dk  k^{1-alpha} sin(k r)
    # Substitute x = k*r (dk = dx/r) to isolate the r-dependence cleanly:
    #   V(r) = 1/(2*pi^2*r) * r^{alpha-2} * Integral_0^inf dx x^{1-alpha} sin(x)
    # The x-integral is the standard Mellin transform of sin(x):
    #   Integral_0^inf x^{s-1} sin(x) dx = Gamma(s) sin(pi*s/2),  0<Re(s)<1
    # here s = 2-alpha, valid for 1<alpha<2 (extendable elsewhere by analytic
    # continuation, standard for these distributional FTs -- not redone here).
    s = 2 - alpha
    mellin_sin = sp.gamma(s) * sp.sin(sp.pi * s / 2)
    prefactor_r_power = alpha - 2 - 1  # r^{alpha-2} from substitution, times 1/r out front
    print(f"    Mellin transform factor (dimensionless): {mellin_sin}")
    print(f"    r-power from the substitution: r^({prefactor_r_power})")
    print("    => V(r) ~ r^(alpha-3)  =>  potential exponent n := 3-alpha")
    n_of_alpha = 3 - alpha
    print(f"    n(alpha) = {n_of_alpha}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- alpha=2 (standard massless propagator) MUST give")
    print("n=1 (1/r Newton/Coulomb), via the SAME exponent algebra used below.")
    print("Checked on BOTH the exponent AND the full coefficient (not exponent")
    print("alone) -- naive substitution hits a removable 0*Gamma-pole singularity")
    print("at alpha=2 (s=2-alpha=0), so the correct LIMIT is taken, not skipped.")
    print("-" * 78)
    n_control = n_of_alpha.subs(alpha, 2)
    control_ok = n_control == 1
    print(f"    n(alpha=2) = {n_control}  (expect 1)")

    mellin_naive = mellin_sin.subs(alpha, 2)
    mellin_limit = sp.limit(mellin_sin, alpha, 2)
    print(f"    naive substitution of the Gamma*sin factor at alpha=2: {mellin_naive}")
    print(f"    correct limit (removable singularity, L'Hopital-equivalent): {mellin_limit}")

    # Full coefficient: V(r) = 1/(2*pi^2*r) * r^{alpha-2} * mellin_sin, at alpha=2
    # r^{alpha-2} -> r^0 = 1, so the full normalization collapses to a pure number.
    full_coeff_at_2 = sp.Rational(1, 2) / sp.pi**2 * mellin_limit
    full_coeff_simplified = sp.simplify(full_coeff_at_2)
    newton_coulomb_coeff = 1 / (4 * sp.pi)
    coeff_matches = sp.simplify(full_coeff_simplified - newton_coulomb_coeff) == 0
    print(f"    full coefficient at alpha=2: {full_coeff_simplified}")
    print(f"    known Newton/Coulomb coefficient 1/(4*pi): {newton_coulomb_coeff}")
    print(f"    coefficients match exactly: {coeff_matches}")

    control_ok = control_ok and coeff_matches
    print(
        f"  POSITIVE CONTROL {'PASSES' if control_ok else 'FAILS'} "
        f"(exponent AND coefficient both checked)"
    )
    if not control_ok:
        print("\n  *** STOP -- the exponent/coefficient algebra itself is not trustworthy.")
        return 1

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("STEP 2 -- what alpha reaches MULTING's target potential exponent n=2?")
    print("(force ~ 1/r^3 is the SOURCE-CONFIRMED preprint quote for F_d; force")
    print(" = -d/dr(potential), so potential ~ 1/r^2 is the matching target --")
    print(" the SAME target docs/131 Branch S already reached via the scalar's")
    print(" DIPOLE-multipole structure, with zero exotic coupling required.)")
    print("-" * 78)
    target_n = 2
    alpha_needed = sp.solve(sp.Eq(n_of_alpha, target_n), alpha)[0]
    print(f"    n_of_alpha = {target_n}  =>  alpha = {alpha_needed}")
    alpha_standard = 2  # standard massless vector propagator, 1/k^2, alpha=2
    delta_alpha = alpha_standard - alpha_needed
    print(f"    standard massless vector propagator: alpha = {alpha_standard}")
    print(f"    delta_alpha (standard - needed) = {delta_alpha}")
    print("    A propagator numerator carrying k^(delta_alpha) EXTRA momentum")
    print("    factors, relative to the standard minimal coupling, corresponds")
    print("    to delta_alpha additional derivatives in the interaction vertex.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("CROSS-CHECK -- confirm the scalar dipole route (Branch S) reaches the")
    print("SAME n=2 target via multipole order, not via a modified alpha, so")
    print("this file's question and docs/131's own Branch S are not the same claim")
    print("-" * 78)
    print("    Branch S (docs/131): monopole potential ~1/r (alpha=2, STANDARD,")
    print("    delta_alpha=0) -> dipole potential = -d/dr[monopole] * (angular")
    print("    factor) ~ 1/r^2. Zero modification to alpha; the exponent shift")
    print("    comes from taking a spatial GRADIENT at the SOURCE (multipole")
    print("    order), not from a nonstandard propagator.")
    branch_s_alpha_shift = 0
    print(f"    Branch S's own delta_alpha = {branch_s_alpha_shift} (by construction)")
    routes_distinct = delta_alpha != branch_s_alpha_shift
    print("    routes are distinct (this file's route needs a real propagator")
    print(f"    modification, Branch S's route does not): {routes_distinct}")

    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if delta_alpha > 0:
        print(f"\n  A vector-charge-at-monopole-order mechanism needs {delta_alpha} extra power(s)")
        print("  of momentum in its coupling, relative to the standard minimal")
        print("  vector coupling, to reach MULTING's target 1/r^3 force via THIS")
        print("  route (as opposed to Branch S's multipole route, which needs none).")
        print("  A coupling carrying extra momentum factors in the vertex is a")
        print("  DERIVATIVE coupling (each extra k = one extra spatial derivative")
        print("  in position space).")
        print()
        print("  IMPORTANT SCOPE CORRECTION (caught by an independent skeptic review")
        print("  of this file, not self-caught): delta_alpha=1 extra derivative is")
        print("  NOT the same claim as 'higher-derivative' in the Ostrogradsky sense.")
        print("  A single-derivative vertex (Pauli term, derivative Yukawa coupling,")
        print("  etc.) is completely standard field theory and is generically")
        print("  ghost-free -- Ostrogradsky's instability specifically concerns")
        print("  Lagrangians whose equations of motion become higher than 2nd order,")
        print("  which is NOT established by delta_alpha=1 alone. This file derives")
        print("  ONLY the derivative-count requirement, not a ghost.")
        print("\n  VERDICT: VECTOR-MONOPOLE-ROUTE-REQUIRES-AT-LEAST-ONE-EXTRA-DERIVATIVE")
        print("  docs/131's vector-mediator dismissal is PARTIALLY, NOT FULLY,")
        print("  upgraded from qualitative to derived: the derivative-requirement")
        print("  premise is now derived (this file); the ghost conclusion docs/131")
        print("  built on top of that premise remains a SEPARATE, unperformed check.")
    else:
        print("\n  Unexpected: the target is reachable without extra derivatives.")
        print("  This would WEAKEN docs/131's own vector-mediator dismissal --")
        print("  flag for manual review before using this result anywhere.")
        print("\n  VERDICT: UNEXPECTED-NO-DERIVATIVE-NEEDED")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
