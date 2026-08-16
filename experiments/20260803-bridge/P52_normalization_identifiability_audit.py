"""P52 -- full-action field-normalization identifiability audit. Asks a
STRONGER question than P50B/P51: not "can the formulas be rewritten after
phi->s*phi" (near-trivial), but "does the ACTUALLY COMMITTED action fix an
absolute normalization for phi at all?"

TERMINOLOGY, corrected per user's own note: this is FIELD-REDEFINITION
COVARIANCE (or field-normalization redundancy), NOT "gauge covariance" --
there is no local gauge symmetry here, just a reparametrization freedom of
one scalar field's normalization. FINDING_P50B and FINDING_P51 both used
the imprecise term; this finding uses the corrected one throughout.

SCOPE: the ACTUALLY COMMITTED monopole (g-sector) action only --
  - kinetic term:     -(C/2)*(d phi)^2       (FINDING_P46, C=1 implicit)
  - matter coupling:  g*J*phi                 (FINDING_P46/P21)
  - P45's potential:  (lambda4/4)*phi^4       (FINDING_P45)
The kappa (dipole) sector has NEVER been covariantized into this action
(every finding through P51 states "monopole g-sector only") -- explicitly
marked ABSENT / NOT TESTABLE below, not extrapolated to.

PRE-REGISTERED outcomes:
  N1 -- one-dimensional normalization redundancy: all committed terms
        have consistent scaling weights, nullspace of the weight system
        is exactly 1-dimensional, and no committed coefficient is fixed
        independently. Verdict: C, g, lambda4, phi are not separately
        identifiable as absolute normalization quantities; physics must
        be stated via invariants.
  N2 -- redundancy broken: at least one committed term/definition does
        NOT admit the same rescaling s. That term is the normalization
        anchor.
  N3 -- incomplete specification: the check runs into a coefficient/term
        that exists conceptually but is not defined in the committed
        action. Applies EXPLICITLY to the kappa-sector question -- it
        bounds transferability to the full MULTING completion, does not
        affect the monopole-only N1/N2 verdict.

TWO KILL-GATES, checked explicitly:
  KG1 (anti-circularity): do not derive transformation rules "so each
      term becomes invariant" and then present that invariance as proof
      of redundancy without a rank/nullspace argument -- this would repeat
      FINDING_P51's own circularity.
  KG2 (form invariance != value determined): even if N1 holds structurally,
      an invariant combination's NUMERICAL value (e.g. g*phibar) still
      depends on background/initial-condition information -- not
      established by this finding, stated explicitly in the verdict.

[CORRECTED after context-blind skeptic review, Step 8a -- the ORIGINAL
version of this script claimed the Part 4 "adversarial control" (adding a
term with a coefficient given NO column, i.e. declared fixed by omission)
validated that the method can distinguish genuine physical anchors from
non-anchors, licensing an unconditional "N1 CONFIRMED" headline. The
skeptic found this FALSE, independently re-verified before accepting:
adding the EXACT SAME new term but giving its coefficient its OWN column
(i.e. treating it as ALSO free to co-transform) leaves nullity=1 --
redundancy PRESERVED. The N1-vs-N2 outcome is therefore determined
ENTIRELY by the auditor's own choice of which coefficients get a free
column, not by anything the mathematics discovers about the physics. This
is the SAME underlying limitation already found in FINDING_P50B (a
dimensionless prefactor alpha undetermined by pure dimensional analysis)
and FINDING_P51 (E1-vs-E3 undetermined by a test that passes regardless
of which is true) -- recurring a THIRD time, now as "which coefficients
are free to co-transform is an INPUT this method needs, not an OUTPUT it
can derive." The headline is corrected accordingly: N1 holds ONLY as a
CONDITIONAL statement (algebraic consistency GIVEN the stipulation that
C, g, lambda4 are all free), not as an unconditional physical fact.]

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    print("=" * 78)
    print("P52 -- full-action field-normalization identifiability audit")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nTERMINOLOGY CORRECTION (per user's own note, adopted throughout):")
    print("  FIELD-REDEFINITION COVARIANCE / field-normalization redundancy --")
    print("  NOT 'gauge covariance' (no local gauge symmetry here; P50B and")
    print("  P51 both used the imprecise term).")
    print("\nPRE-REGISTERED: N1 (1-dim redundancy) / N2 (anchor found) /")
    print("N3 (incomplete specification -- applies to kappa-sector explicitly).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- committed action terms, stated exactly, kappa-sector")
    print("explicitly marked ABSENT")
    print("-" * 78)
    print("  L_phi = -(C/2)*(d phi)^2 + g*J*phi - (lambda4/4)*phi^4")
    print("  (FINDING_P46: kinetic + matter coupling, C=1 implicit throughout")
    print("  this campaign; FINDING_P45: quartic potential, lambda4>0 declared,")
    print("  NEVER numerically fixed anywhere in this campaign.)")
    print()
    print("  [KAPPA-SECTOR: ABSENT / NOT TESTABLE] Every finding through P51")
    print("  states 'monopole (g) sector only' -- kappa has never been")
    print("  covariantized into this action. This finding CANNOT test whether")
    print("  a kappa-dependent term would break the redundancy, because that")
    print("  term does not exist in the committed action. Any verdict below")
    print("  applies to the MONOPOLE action only -- N3 for the full")
    print("  MULTING-completion question, stated explicitly, not silently")
    print("  skipped.")
    print()
    print("  [COMPLETENESS CAVEAT] The '3-term list' above was checked by a")
    print("  targeted grep across experiments/20260803-bridge (confirming via")
    print("  FINDING_P44 line 71 'there is no mass term at all here', and no")
    print("  'nonminimal' matches anywhere) -- a SPOT-CHECK, not an exhaustive")
    print("  line-by-line audit of all 50+ prior findings. Stated as a")
    print("  limitation, not implied to be a closed inventory.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- scaling-weight system, built as an ACTUAL rank/nullspace")
    print("computation (KG1: not a term-by-term substitution check)")
    print("-" * 78)
    print("  Under phi'=s*phi (s: rescaling parameter, kept distinct from")
    print("  P45's own lambda4 symbol per the user's own naming fix), each")
    print("  committed term contributes ONE constraint: (field power)*w(phi)")
    print("  + w(coefficient) = 0, for the term to keep its algebraic form.")
    print("  J (matter source) does NOT transform -- established in")
    print("  FINDING_P50B/P51, reused not re-derived.")
    print()
    print("  [CAVEAT] Reusing w(J)=0 without re-deriving it is a BIGGER concern")
    print("  here than it was for P50B/P51's narrower covariance claims: an")
    print("  IDENTIFIABILITY verdict (this finding) leans on every column of M")
    print("  being right, not just one invariance relation. Not re-derived in")
    print("  this finding -- flagged, not fixed.")
    print()
    print("  Columns: [w(phi), w(C), w(g), w(lambda4)]")
    M = sp.Matrix(
        [
            [2, 1, 0, 0],  # kinetic:  C*(d phi)^2      -- phi^2
            [1, 0, 1, 0],  # coupling: g*J*phi           -- phi^1
            [4, 0, 0, 1],  # quartic:  lambda4*phi^4     -- phi^4
        ]
    )
    print(f"  Weight matrix M =\n{M}")
    rank_M = M.rank()
    nullspace_M = M.nullspace()
    print(f"\n  rank(M) = {rank_M}")
    print(f"  nullity = {len(nullspace_M)}")
    assert rank_M == 3, "unexpected rank for the committed 3-term system"
    assert len(nullspace_M) == 1, "nullity is not exactly 1 -- N1 is not supported"
    null_vec = nullspace_M[0]
    null_vec_normalized = null_vec / null_vec[0]
    print(f"  null vector (normalized to w(phi)=1): {null_vec_normalized.T}")
    w_phi, w_C, w_g, w_lam4 = null_vec_normalized
    assert (w_phi, w_C, w_g, w_lam4) == (1, -2, -1, -4)
    print("  -> CONFIRMED: nullity=1 for the committed monopole action.")
    print("     w(phi)=1, w(C)=-2, w(g)=-1, w(lambda4)=-4 -- matching the")
    print("     hand-derived weights exactly, now via genuine linear algebra,")
    print("     not asserted.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- what this DOES and DOES NOT yet establish (before the")
    print("adversarial control)")
    print("-" * 78)
    print("  nullity=1 means: the committed 3-term system is CONSISTENT with")
    print("  a 1-parameter redundancy family -- but this alone does not prove")
    print("  the METHOD would have caught a real anchor if one were present")
    print("  (KG1's concern). Part 4 tests this directly.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- the 'adversarial control', and why the ORIGINAL version")
    print("of it was WRONG about what it establishes (SKEPTIC-CAUGHT, Step 8a)")
    print("-" * 78)
    print("  ORIGINAL claim: add q*phi^3 with q given NO column (declared")
    print("  'fixed' by omission) -- redundancy collapses to nullity=0. This")
    print("  was PRESENTED as proof the method can distinguish real anchors")
    print("  from non-anchors, licensing trust in the Part 2 nullity=1 result.")
    M2_fixed = sp.Matrix(
        [
            [2, 1, 0, 0],
            [1, 0, 1, 0],
            [4, 0, 0, 1],
            [3, 0, 0, 0],  # q*phi^3, q given NO column
        ]
    )
    rank_fixed = M2_fixed.rank()
    nullity_fixed = len(M2_fixed.nullspace())
    print(f"  q*phi^3, q with NO column: rank={rank_fixed}, nullity={nullity_fixed}")
    assert rank_fixed == 4 and nullity_fixed == 0

    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] DECISIVE COUNTER-SCENARIO, independently")
    print("  re-verified before accepting: add the EXACT SAME term q*phi^3, but")
    print("  give q its OWN column (i.e. treat it as ALSO free to co-transform,")
    print("  exactly like C, g, lambda4 already were):")
    M2_free = sp.Matrix(
        [
            [2, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [4, 0, 0, 1, 0],
            [3, 0, 0, 0, 1],  # q*phi^3, q given its OWN column this time
        ]
    )
    rank_free = M2_free.rank()
    ns_free = M2_free.nullspace()
    print(f"  q*phi^3, q WITH its own column: rank={rank_free}, nullity={len(ns_free)}")
    assert rank_free == 4
    assert len(ns_free) == 1, (
        "the SAME new term, given a free column, should preserve nullity=1 "
        "-- if not, the counter-scenario itself is wrong, re-check"
    )
    print(f"  null vector (normalized): {(ns_free[0] / ns_free[0][0]).T}")
    print()
    print("  -> THE SAME TERM gives EITHER nullity=0 (redundancy destroyed)")
    print("     OR nullity=1 (redundancy preserved), depending ENTIRELY on")
    print("     whether the AUDITOR chooses to grant the new coefficient a")
    print("     free column -- not on anything the mathematics discovers")
    print("     about the physics. The ORIGINAL 'adversarial control' did NOT")
    print("     establish what it claimed: it demonstrated a tautology (an")
    print("     omitted column forces that variable's weight to zero), not a")
    print("     method capable of independently distinguishing 'genuine")
    print("     physical anchor' from 'another free, co-transforming")
    print("     coefficient'. RETRACTED as originally presented.")
    print()
    print("  [STRUCTURAL POINT] This is the SAME underlying limitation")
    print("  already found in FINDING_P50B (a dimensionless prefactor alpha")
    print("  undetermined by pure dimensional analysis) and FINDING_P51")
    print("  (E1-vs-E3 undetermined by a criterion that passes regardless of")
    print("  which is true) -- recurring a THIRD time: which coefficients are")
    print("  free to co-transform is an INPUT this method NEEDS from outside")
    print("  itself (an independent physical derivation/definition of each")
    print("  term), not an OUTPUT the rank/nullspace computation can derive.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- invariants derived FROM the null vector, not asserted by")
    print("pattern-matching")
    print("-" * 78)
    w_A = -w_C  # A := C^-1
    print(f"  w(A) := -w(C) = {w_A}  (A=C^-1)")

    def total_weight(exponents):
        weights = {"phi": w_phi, "C": w_C, "g": w_g, "lambda4": w_lam4, "A": w_A}
        return sum(weights[var] * power for var, power in exponents.items())

    candidates = {
        "A*g^2": {"A": 1, "g": 2},
        "g*phi": {"g": 1, "phi": 1},
        "lambda4*A^2": {"lambda4": 1, "A": 2},
    }
    for name, exps in candidates.items():
        w = total_weight(exps)
        print(f"    weight({name}) = {w}")
        assert w == 0, f"{name} is NOT invariant under the found null direction"
    print("  -> CONFIRMED: A*g^2, g*phi, lambda4*A^2 all have EXACTLY zero")
    print("     total weight under the null vector found in Part 2 -- derived")
    print("     from the computed nullspace, not pattern-matched from prior")
    print("     findings. A*g^2 matches FINDING_P50B/P51's own force-strength")
    print("     invariant; g*phi matches the interaction invariant already")
    print("     established.")
    print()
    print("  [CORRECTED framing for lambda4*A^2] Originally called 'NEW' --")
    print("  overstated. With a 1-dimensional null space spanned by a single")
    print("  vector, EVERY invariant is a rational power of any one of them:")
    print("  once A*g^2 and g*phi are known to be the first two independent")
    print("  weight-zero generators, lambda4*A^2 is the mathematically FORCED")
    print("  third generator of the same 1-dimensional invariant lattice, not")
    print("  an independent discovery. Its physical content (lambda4 alone is")
    print("  convention-dependent, lambda4*A^2 is the meaningful combination)")
    print("  is still a real, correctly-derived statement -- only the 'NEW'")
    print("  framing is corrected.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 6 -- KG1 (anti-circularity): what actually distinguishes this")
    print("from FINDING_P51's circularity, and what does NOT [CORRECTED]")
    print("-" * 78)
    print("  FINDING_P51's Part 2 checked whether TWO ALREADY-MATCHING NUMBERS")
    print("  (phi_R2/phi_R1 and g_R1/g_R2) agreed -- both reduced to the")
    print("  literal same forced expression, a tautology by construction.")
    print("  P52's rank/nullspace computation does NOT repeat that SPECIFIC")
    print("  failure: nullity=1 is a genuine, non-forced linear-algebra fact")
    print("  about 3 independently-stated term-constraints on 4 columns")
    print("  (rank=3 was computed, not assumed -- rank<3 was a live logical")
    print("  possibility the sympy call could have returned).")
    print()
    print("  [CORRECTED] The ORIGINAL text here claimed Part 4's adversarial")
    print("  control PROVED this rank/nullspace method is 'sensitive to")
    print("  genuine anchors' -- Part 4 itself now shows that claim is FALSE:")
    print("  the same new term gives nullity=0 or nullity=1 depending only on")
    print("  whether the auditor grants its coefficient a free column. So KG1")
    print("  is only PARTIALLY addressed: P52 avoids P51's specific tautology")
    print("  (forced numerical equality), but shares a DEEPER version of the")
    print("  SAME underlying limitation -- whether the 4 columns [phi,C,g,")
    print("  lambda4] are the CORRECT and COMPLETE set of physically-free")
    print("  coefficients is an assumption fed INTO the matrix, not a fact")
    print("  the matrix's rank can verify about itself. Nullity=1 is a sound")
    print("  computation GIVEN that assumption; it is not independent proof")
    print("  that the assumption is correct.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 7 -- KG2 (form invariance != value determined), stated")
    print("explicitly")
    print("-" * 78)
    print("  Even given N1: A*g^2, g*phi, lambda4*A^2 being INVARIANT under")
    print("  field redefinition does NOT mean their NUMERICAL VALUES are")
    print("  determined by this finding. g*phibar (hence P50A's")
    print("  mu_metric=1-g_hat*phibar) is invariant (FINDING_P51), but phibar")
    print("  itself is sourced by FINDING_P46's own background field equation,")
    print("  which has free initial conditions -- N1 says WHICH combinations")
    print("  are physically meaningful to ask about, not WHAT their values")
    print("  are. Not established here, stated explicitly, not smuggled past.")

    print("\n" + "=" * 78)
    print("VERDICT [CORRECTED after context-blind skeptic review, Step 8a]")
    print("=" * 78)
    print("N1 holds only as a CONDITIONAL statement, not an unconditional")
    print("physical fact: GIVEN the stipulation that C, g, lambda4 (alongside")
    print("phi) are ALL free to co-transform under field redefinition, the")
    print("scaling-weight system for the committed monopole action (kinetic +")
    print("matter coupling + P45 quartic potential) has nullity EXACTLY 1")
    print("(Part 2, genuine rank/nullspace computation, not asserted).")
    print()
    print("The ORIGINAL headline ('N1 CONFIRMED', unconditional) is RETRACTED.")
    print("The Part 4 adversarial control does NOT license that stronger")
    print("claim: it shows the SAME new term gives nullity=0 or nullity=1")
    print("depending entirely on whether the auditor grants its coefficient a")
    print("free column -- i.e. whether a term's coefficient is 'genuinely")
    print("fixed' vs 'free to co-transform' is an INPUT this method needs")
    print("from outside itself, not an OUTPUT the computation can certify.")
    print("This is the THIRD occurrence this session of the same underlying")
    print("limitation (P50B: undetermined numerical prefactor; P51: forced")
    print("tautological criterion; P52: auditor-choice-dependent modeling).")
    print()
    print("What SURVIVES intact: IF C, g, lambda4, phi are all free (a")
    print("stipulation consistent with every prior finding in this campaign,")
    print("but not independently proven here), THEN A*g^2 (force strength,")
    print("matching P50B/P51), g*phi (interaction, matching P51), and")
    print("lambda4*A^2 (self-interaction, forced third generator of the same")
    print("null direction) are the physically meaningful invariant")
    print("combinations -- individual C, g, lambda4, phi are not.")
    print()
    print("KAPPA-SECTOR: explicitly N3 (absent from the committed action) --")
    print("this verdict does NOT extend to the full MULTING completion,")
    print("stated as a scope boundary, not glossed over.")
    print()
    print("KG2: form invariance of A*g^2, g*phi, lambda4*A^2 does NOT")
    print("determine their numerical values -- background/initial-condition")
    print("information (e.g. for phibar) remains genuinely open, not")
    print("established here.")
    print()
    print("P17/P42 CONNECTION: explicitly DEFERRED as a testable prediction,")
    print("not included in this headline -- IF N1 is the correct structural")
    print("picture, FINDING_P17's Omega_phi 'kg/m' mismatch and FINDING_P42's")
    print("shared missing constant MAY be projections of the SAME null")
    print("direction found here, but this requires an independent mapping of")
    print("their own specific dimensional gaps onto this null direction --")
    print("NOT attempted here, genuinely a separate, future check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
