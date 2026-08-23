"""P133 -- Formal identifiability audit for H3 (absolute-scale / observable
mapping): given the SPECIFIC observable channels this project has actually
identified so far (O1=A*g^2 from growth-rate data, O2=A*kappa^2 from a
hypothetical Omega_phi external bound, O3=kappa/g from P24's own
cross-sector force-ratio eta), can theta=(A,g,kappa) be uniquely recovered?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed. After the hypothesis-arbiter's own H4
(P132) closed cleanly, informal analysis of H3's own named candidate
(P42's shared A/c^2 constant) found: (a) P14 section 1's own self-energy-
vs-cancellation tension is unresolved (does the Omega_phi channel even
exist physically?); (b) P39's own "Reading 1 vs Reading 2" ambiguity for
[g] is unresolved (P42's A/c^2 result is Reading-1-specific); (c) even
setting both aside, combining O1 and a hypothetical O2 gives 2 equations
for 3 unknowns (A,g,kappa) -- underdetermined by simple counting. The
user asked for something stronger than "2 equations, 3 unknowns" prose:
a FORMAL audit that (1) explicitly checks whether a hidden third relation
already exists somewhere in this project's own registered findings before
concluding degeneracy, and (2) computes the actual Jacobian rank, not
just counts equations.

THE HIDDEN RELATION CHECK, done before building anything else (matching
this project's own "not postfactum" discipline): grepped every
FINDING_P*.md for a kappa<->g relation. Found one -- FINDING_P24 already
introduces eta:=kappa/g as the SOLE parameter controlling every
cross-sector force ratio (chi_d, chi_q), with A cancelling identically
(symbolically verified there, sympy). This is exactly a candidate THIRD
observable, O3=kappa/g, independent of A by construction. This file
tests whether adding O3 to O1, O2 actually breaks the degeneracy.

THE RESULT (spoiler, verified below, not asserted): it does NOT. O2 is an
EXACT algebraic consequence of O1 and O3 (O2 = O1*O3^2, holding for ALL
values of A, g, kappa, not just generically) -- so even with all three
"observables" combined, only 2 independent pieces of information exist.
The Jacobian of (O1,O2,O3) w.r.t. (A,g,kappa) is EXACTLY singular
(det=0, verified symbolically, not floating-point). A clean, general
criterion falls out along the way: since O1, O2, O3 are all MONOMIALS in
(A,g,kappa), their identifiability rank equals the rank of the matrix of
their EXPONENT VECTORS (a classical fact -- log-linearization of
power-law observables) -- giving reusable machinery for checking any
FUTURE candidate observable before chasing it externally.

CONTROLS:
  POSITIVE CONTROL: a synthetic 3-observable set with a KNOWN, non-
    degenerate exponent matrix (rank 3) must be correctly classified as
    IDENTIFIABLE by the same method -- validates the rank-check machinery
    on a case with a known answer before trusting it on the real one.
  CROSS-CHECK: the symbolic determinant is verified against TWO
    independent methods (cofactor expansion via sympy's own .det(), and
    the exponent-matrix determinant) -- must agree exactly.

WHAT THIS FILE DOES NOT DO: resolve P14 section 1's own channel-existence
tension or P39's own Reading 1/2 ambiguity -- named, per the user's own
prioritization (P14's question is logically prior, since if the Omega_phi
channel doesn't exist physically, O2 is moot regardless of this file's
own algebra), as the concrete next step IF H3 is ever reopened, not
attempted here. Search for a genuinely new, non-monomial observable, or
for a theoretical kappa=F(g) relation, or a theory-fixed value of A --
named as the three classes of information that COULD reopen H3, per the
user's own taxonomy, not attempted here. Vary Lambda, G_N, or C_MATTER.
Quote any k[h/Mpc]. Touch MULTING itself (Gate 1).
"""

import sympy as sp


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P133 -- formal identifiability audit: theta=(A,g,kappa),")
    print("        O1=A*g^2, O2=A*kappa^2, O3=kappa/g")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    A, g, k = sp.symbols("A g kappa", positive=True)

    # ==================================================================
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- a synthetic, KNOWN-non-degenerate 3-observable set")
    print("must be correctly classified as IDENTIFIABLE (rank 3)")
    print("-" * 78)
    # A synthetic set whose exponent vectors are trivially independent
    # (the identity matrix): P1=A, P2=g, P3=kappa. Trivially identifiable.
    synthetic = sp.Matrix([A, g, k])
    J_synth = synthetic.jacobian([A, g, k])
    det_synth = sp.simplify(J_synth.det())
    pc_ok = det_synth != 0
    print(f"    synthetic Jacobian det = {det_synth}")
    print(f"  POSITIVE CONTROL {'PASSES' if pc_ok else 'FAILS'} (det != 0 expected)")
    if not pc_ok:
        print("  *** STOP -- the rank-check machinery itself is broken.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("HIDDEN-RELATION CHECK -- FINDING_P24's own eta=kappa/g, confirmed")
    print("A-independent there (symbolically, this project's own prior result)")
    print("-" * 78)
    print("    FINDING_P24 section 2: chi_d, chi_q (cross-sector force ratios)")
    print("    depend on eta=kappa/g ALONE -- A cancels identically. Used here")
    print("    as candidate O3 = kappa/g.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- the real observable set: O1=A*g^2 (growth-rate,")
    print("P22/P31/P132), O2=A*kappa^2 (P14's own kappa^2 scaling, IF the")
    print("Omega_phi channel exists), O3=kappa/g (P24)")
    print("-" * 78)
    O1 = A * g**2
    O2 = A * k**2
    O3 = k / g
    obs = sp.Matrix([O1, O2, O3])
    print(f"    O1 = {O1}")
    print(f"    O2 = {O2}")
    print(f"    O3 = {O3}")

    J = obs.jacobian([A, g, k])
    print("\n    Jacobian J = d(O1,O2,O3)/d(A,g,kappa):")
    sp.pprint(J)

    det_J = sp.simplify(J.det())
    print(f"\n    det(J) = {det_J}")
    rank_J = J.rank()
    print(f"    rank(J) = {rank_J}  (need 3 for full identifiability of 3 unknowns)")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CROSS-CHECK 1 -- exact algebraic identity: is O2 a function of O1,O3 alone?")
    print("-" * 78)
    candidate_identity = sp.simplify(O2 - O1 * O3**2)
    print(f"    O2 - O1*O3^2 = {candidate_identity}")
    identity_confirmed = candidate_identity == 0
    print(
        f"    EXACT IDENTITY O2 = O1*O3^2 confirmed (holds for ALL A,g,kappa): {identity_confirmed}"
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("CROSS-CHECK 2 -- exponent-matrix method (log-linearization):")
    print("rank of Jacobian of monomial observables = rank of their exponent matrix")
    print("-" * 78)
    # O1=A^1 g^2 k^0, O2=A^1 g^0 k^2, O3=A^0 g^-1 k^1
    exponent_matrix = sp.Matrix([[1, 2, 0], [1, 0, 2], [0, -1, 1]])
    print("    exponent matrix (rows=O1,O2,O3; cols=A,g,kappa):")
    sp.pprint(exponent_matrix)
    det_exp = exponent_matrix.det()
    rank_exp = exponent_matrix.rank()
    print(f"    det(exponent matrix) = {det_exp}")
    print(f"    rank(exponent matrix) = {rank_exp}")
    methods_agree = (rank_exp == rank_J) and (det_exp == 0) == (det_J == 0)
    print(
        f"    both methods agree (Jacobian rank == exponent-matrix rank, "
        f"det==0 <=> det==0): {methods_agree}"
    )

    # Explicit linear dependency among rows, found not asserted.
    row1, row2, row3 = exponent_matrix.row(0), exponent_matrix.row(1), exponent_matrix.row(2)
    dependency_check = sp.simplify(row1 - row2 + 2 * row3)
    print(f"\n    explicit row dependency: row1 - row2 + 2*row3 = {dependency_check}")
    print("    (i.e. log(O1) - log(O2) + 2*log(O3) = const -- exactly the O2=O1*O3^2 identity)")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if rank_J < 3 and identity_confirmed and methods_agree:
        print("  -> H3-NOT-IDENTIFIABLE-AS-CURRENTLY-POSED (not REFUTED --")
        print("     BLOCKED BY STRUCTURAL UNDERDETERMINATION).")
        print(f"     rank(J) = {rank_J} < 3 = number of unknowns (A, g, kappa), verified")
        print("     symbolically (exact, not floating-point) via two independent")
        print("     methods (direct Jacobian determinant, and the exponent-matrix")
        print("     determinant for these monomial observables -- they agree).")
        print("     The THIRD candidate relation this file went looking for")
        print("     (FINDING_P24's own eta=kappa/g, A-independent) is REAL but does")
        print("     NOT rescue identifiability: it satisfies the EXACT identity")
        print("     O2 = O1*O3^2 for ALL (A,g,kappa), meaning O2 carries ZERO")
        print("     information beyond O1 and O3 combined. Even O1+O3 alone leave a")
        print("     1-parameter family of (A,g,kappa) solutions -- a genuine,")
        print("     provable, 1-dimensional continuous degeneracy that no amount of")
        print("     precision on THESE THREE specific observable types can close.")
        print("\n     REUSABLE CRITERION for any future candidate observable O4:")
        print("     if O4 is a monomial A^a*g^b*kappa^c, it breaks the degeneracy")
        print("     ONLY IF its exponent vector (a,b,c) is linearly independent of")
        print("     the current two-dimensional row space (spanned by, e.g., O1's")
        print("     and O3's own exponent vectors) -- checkable BEFORE spending any")
        print("     effort chasing external data for it.")
    else:
        print("  -> UNEXPECTED: the degeneracy was NOT confirmed as expected.")
        print("     Re-derive by hand before trusting this file's own conclusion.")
        return 1

    print("\n  NOT ESTABLISHED:")
    print("   * whether FINDING_P14's own Omega_phi self-energy channel physically")
    print("     exists at all (section 1's cancellation tension, unresolved) --")
    print("     per the user's own prioritization, logically PRIOR to this file's")
    print("     own question: if the channel doesn't exist, O2 is moot regardless")
    print("     of this file's algebra.")
    print("   * FINDING_P39's own Reading 1 vs Reading 2 ambiguity for [g] --")
    print("     P42's own A/c^2 result (which this file's O2 relies on for its")
    print("     dimensional form) is Reading-1-specific.")
    print("   * a resolution via any of the three classes of new information that")
    print("     COULD reopen H3 (user's own taxonomy): a theoretical kappa=F(g)")
    print("     relation; a genuinely NEW, non-monomial-in-these-3-vars observable;")
    print("     or a theory-fixed value of A. None searched for or attempted here.")
    print("   * anything about MULTING itself (Gate 1). Any k[h/Mpc].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
