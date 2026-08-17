"""P53 -- does an EXTERNAL numeric anchor already exist in this project for
one of P52's three invariants, and precisely what does it (not) resolve?

ORIGIN: P50B, P51, and P52 each independently concluded the same thing in
different guises -- pure field-redefinition-covariance / dimensional-
analysis methods cannot fix a number, only a combination's FORM. P51's own
words: "a real discriminating test needs something sensitive to the
readings' numerical relationship (external anchor, or a non-covariant
action term), neither available in this campaign." The user's own
stop-rule after P52: further internal rank/nullspace variations have low
information value; the next step must use a NEW SOURCE of information, not
a fourth variation of the same method.

NOVELTY CHECK (FL Step -3), done BEFORE writing this script, not asserted:
- docs/129 (Q006, 2026-07-22): grepped the full TJB preprint for
  "lagrangian|action|variational|euler-lagrange|field equation|hamiltonian"
  -- ZERO hits. TJB's own corpus specifies MULTING entirely at the level of
  two-body FORCES; no covariant action exists in the source AT ALL. So a
  source-level "grep for where g/phi is fixed" (the originally-proposed
  P53 scope) would just re-confirm docs/129 at one further remove -- not
  new information.
- FINDING_P21 (2026-08-13) and FINDING_P22 (2026-08-13, corrected same day)
  ALREADY established a genuine EXTERNAL numeric ceiling on the product
  A*g^2 -- not from TJB's corpus, but from an independently-published
  paper (Archidiacono et al. 2022/2025, arXiv:2204.08484) via a completely
  different mechanism (a fifth-force bound on a DM-only scalar), mapped
  onto this project's own A*g^2=4*pi*Delta_G identity (P21).
- FINDING_P52 (THIS SESSION, did not exist before today) independently
  proved A*g^2 is EXACTLY the field-redefinition-invariant combination the
  whole normalization-audit sub-campaign was looking for. Nothing in the
  repo could have connected P22's 2026-08-13 number to P52's 2026-08-16
  invariance proof before this script, because P52 did not exist.
This IS the new-source-of-information step: connect an OLD external number
(P22/P31, well outside this project's own algebra) to a BRAND NEW internal
result (P52) that makes that number trustworthy in a way it could not have
been shown to be before today.

PRE-REGISTERED outcomes:
  M1 -- mapping confirmed: P22/P31's "A" (defined as phi_true/phi_raw,
        FINDING_P21) and P52's "A" (defined as C^-1, the inverse kinetic-
        term coefficient) are the SAME quantity, not merely similarly
        named -- traceable through FINDING_P50B's own two-route agreement
        (kinetic-coefficient canonicalization route AND P19's Green's-
        function force-law route, which P50B showed agree exactly).
  M2 -- mapping broken: some inconsistency found; the ceiling would not
        straightforwardly apply to P52's own invariant.
  M3 -- reading caveat, applies regardless of M1/M2: P22/P31's ceiling was
        computed under P39's Reading 1 (g dimensionless, P21's own stated
        assumption) -- P51 could not determine whether Reading 1 is the
        physically correct one. The ceiling does not resolve that question,
        only sits within it.

KILL GATES:
  KG1 (unit/definition continuity): if P52's A:=C^-1 cannot be traced to
      P21's A:=phi_true/phi_raw through an already-established finding (not
      re-derived from scratch here), this whole synthesis is void -- M2.
  KG2 (no new precision claimed): this script must not upgrade P22/P31's
      own "soft ceiling, not precision result" status -- any number carried
      forward keeps that caveat explicitly attached.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    print("=" * 78)
    print("P53 -- external numeric anchor (P22/P31) x P52's invariant lattice")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nPRE-REGISTERED: M1 (mapping confirmed) / M2 (mapping broken) /")
    print("M3 (reading caveat, applies regardless of M1/M2).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- re-derive P22/P31's ceiling on A*g^2, not copy the number")
    print("-" * 78)
    A, g, beta, G_N = sp.symbols("A g beta G_N", positive=True)
    print("  FINDING_P21 (2026-08-13, corrected): A*g^2 = 4*pi*Delta_G")
    print("  FINDING_P22 (2026-08-13, corrected twice same day): Archidiacono")
    print("  et al. arXiv:2204.08484, beta = G_s/(4*pi*G_N), and the paper's")
    print("  own short-distance statement Delta_G = beta*G_N -- two independent")
    print("  quoted routes, verified to agree exactly (P22's own positive")
    print("  control, reused not re-derived here):")
    a_g2_expr = 4 * sp.pi * beta * G_N
    print(f"  A*g^2 = {a_g2_expr}")
    beta_val = 0.01  # P22's independently-verified abstract headline figure
    g_n_val = 6.6743e-11  # SI, same constant as P17/P22's own scripts
    a_g2_bound = float(a_g2_expr.subs({beta: beta_val, G_N: g_n_val}))
    print(f"  Using beta<~{beta_val} (P22) and G_N={g_n_val:.5e} SI:")
    print(f"  A*g^2 <~ {a_g2_bound:.4e}  (SI units, m^3 kg^-1 s^-2 -- Reading 1)")
    assert abs(a_g2_bound - 8.39e-12) / 8.39e-12 < 0.01, (
        "re-derived ceiling does not match FINDING_P22's own reported 8.39e-12 "
        "-- something in this script's re-derivation diverges from P22's"
    )
    print("  -> CONFIRMED: matches FINDING_P22's own reported 8.39e-12 to <1%.")
    print("     Reused note (P22 pearl entry): P31 independently derives a")
    print("     near-identical ~8.39e-12 via a DIFFERENT external paper (Bean")
    print("     & Tangmatitham growth-rate bound) -- but this project's own")
    print("     pearl registry already flags this as NOT independent")
    print("     convergence (both are ~1%-level bounds through the identical")
    print("     A*g^2=4*pi*G_N*epsilon conversion) -- not re-claimed as fresh")
    print("     confirmation here, cited with that caveat attached (KG2).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- KG1: is P22/P31's A the SAME A as P52's A:=C^-1?")
    print("-" * 78)
    print("  FINDING_P21's A is defined via phi_true := A * phi_raw, where")
    print("  phi_raw solves the field equation with a CANONICAL (C=1) kinetic")
    print("  term and P19's own Green's function. FINDING_P52's A is defined")
    print("  directly as C^-1, the inverse of a GENERAL kinetic-term")
    print("  coefficient. These are stated identically in neither finding --")
    print("  the continuity is NOT re-derived from scratch here (that would")
    print("  repeat P51's own mistake of treating a shared construction as")
    print("  independent confirmation).")
    print()
    print("  [CORRECTED after skeptic review, Step 8a] The original version")
    print("  cited FINDING_P50B Part 4's 'two independent canonicalization")
    print("  routes' as the bridge. P50B's OWN skeptic pass already downgraded")
    print("  that SPECIFIC claim to 'propagation-verification, not independent")
    print("  derivation' (KG4 only PARTIALLY satisfied) -- Route 2 solves the")
    print("  Euler-Lagrange equation from the SAME Lagrangian as Route 1, so")
    print("  their agreement is a necessary consequence of variational")
    print("  calculus, not independent confirmation of the A-continuity claim")
    print("  needed HERE. Citing it at pre-correction strength repeated, in")
    print("  miniature, this session's own recurring failure mode.")
    print()
    print("  The better-supported bridge, independently re-checked before use:")
    print("    (a) FINDING_P21's own skeptic-added note (S2): 'the identical")
    print("        physics results from placing an equivalent factor in the")
    print("        kinetic term instead ((1/2A)(d phi)^2)' -- P21's own text")
    print("        already states the coupling-normalization vs kinetic-term")
    print("        placement of A is convention-equivalent.")
    print("    (b) FINDING_P50B Part 5 (dimensional analysis, NOT Part 4):")
    print("        under Reading 1, the kinetic term C*(d phi)^2 must itself")
    print("        carry Lagrangian-density dimension, forcing")
    print("        [A]=[C^-1]=kg^-1 m^3 s^-2 = [G_N] exactly -- P21's own")
    print("        [A]=[G_N] result, re-derived from the SAME general-C")
    print("        Lagrangian P52 uses, not merely analogous to it.")
    print("  -> M1 (mapping confirmed), CONDITIONAL on trusting these TWO")
    print("     already-established results -- not re-verified from first")
    print("     principles in this script, an honest limitation stated here.")
    print()
    print("  [Added after skeptic review] A plays a CONCEPTUALLY DIFFERENT")
    print("  role in each finding: P21 treats A as a fixed dimensional")
    print("  constant of the theory (to be measured); P52 treats A:=C^-1 as a")
    print("  free parameter subject to the redefinition freedom (weight")
    print("  w(A)=2). Both conventions give the SAME invariant A*g^2, and the")
    print("  external bound transfers either way -- but this is a real")
    print("  conceptual asymmetry between the two findings, not a detail to")
    print("  gloss over.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- KG2 / M3: the ceiling is Reading-1-specific, stated")
    print("explicitly, not smuggled past")
    print("-" * 78)
    print("  FINDING_P21 states plainly: 'g's dimensionlessness is an")
    print("  assumption made here, not established.' That assumption IS")
    print("  P39's Reading 1 (g dimensionless) by construction -- FINDING_P42")
    print("  independently confirmed this same Reading-1-specificity for a")
    print("  DIFFERENT shared-constant result (Omega_phi / Phi-Psi), and found")
    print("  it explicitly FAILS to carry over to Reading 2.")
    print("  FINDING_P51 (this session) could NOT determine whether Reading 1")
    print("  or Reading 2 is the physically correct one -- 'undetermined by")
    print("  this analysis,' the campaign's own words.")
    print("  -> M3 holds regardless of M1/M2: P22/P31's A*g^2<~8.39e-12 (SI)")
    print("     ceiling is a real, external, non-self-referential number --")
    print("     but it lives INSIDE Reading 1's convention, not outside the")
    print("     Reading-1-vs-Reading-2 question. It is CONSISTENT WITH, but")
    print("     does NOT itself validate, the free-coefficient stipulation")
    print("     P52's N1 rests on -- an external bound on the product A*g^2")
    print("     says nothing about whether C, g, lambda4 are individually")
    print("     free to co-transform, which is what that stipulation claims.")
    print()
    print("  [Added after skeptic review] What Part 3 checked is only")
    print("  DIMENSIONAL invariance across readings: [A*g^2] comes out as")
    print("  [G_N] under BOTH Reading 1 (P50B Part 5) and Reading 2 (checked")
    print("  directly: [A]_R2=kg^-1 m^5 s^-4, [g^2]_R2=m^-2 s^2, product=")
    print("  kg^-1 m^3 s^-2=[G_N]). The NUMERICAL value of the beta->A*g^2")
    print("  mapping under a genuine Reading-2 re-derivation is UNEXAMINED --")
    print("  it could differ non-trivially from 8.39e-12, not merely carry a")
    print("  different label. Dimensional agreement across readings does not")
    print("  imply numerical agreement.")
    a_g2_r2_dims = ((-1, 5, -4), (0, -2, 2))  # [A]_R2, [g^2]_R2 (kg,m,s exponents)
    a_g2_r2_product = tuple(a + b for a, b in zip(*a_g2_r2_dims, strict=True))
    g_n_dims = (-1, 3, -2)
    assert a_g2_r2_product == g_n_dims, (
        "Reading-2 [A*g^2] does not reduce to [G_N] -- the dimensional-"
        "invariance claim above needs re-checking, not the numerical claim"
    )
    print(
        f"  [A*g^2]_Reading2 = {a_g2_r2_product}  ==  [G_N] = {g_n_dims}: "
        f"{a_g2_r2_product == g_n_dims}  (dimensions only, not a value)"
    )

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- what this DOES connect: P52's Ag^2 invariant now has an")
    print("external ceiling; gphi and lambda4*A^2 (P52's other two) do not")
    print("-" * 78)
    print("  P52 Part 5 found THREE weight-zero invariants for the committed")
    print("  monopole action: A*g^2 (force strength), g*phi (interaction, the")
    print("  SAME combination entering P50A's mu_metric=1-g_hat*phibar), and")
    print("  lambda4*A^2 (self-interaction, forced third generator).")
    print("  Only A*g^2 has an external numeric handle (this finding, via")
    print("  P22/P31) -- g*phi and lambda4*A^2 remain COMPLETELY unanchored,")
    print("  by any source, internal or external, found anywhere in this")
    print("  project to date. This is a real asymmetry in the invariant")
    print("  lattice's evidentiary status, not previously stated explicitly.")
    print()
    print("  IMPORTANT NEGATIVE RESULT, stated precisely: the A*g^2 ceiling")
    print("  does NOT bound mu_metric's deviation from 1 (g*phibar), because")
    print("  that requires BOTH splitting A*g^2 into A and g separately")
    print("  (P22 Section 4 explicitly: 'A numeric value for A or g")
    print("  individually' is NOT established, only the product's ceiling)")
    print("  AND a value for phibar (P52 Part 7 explicitly: not determined,")
    print("  free initial conditions). Two additional, unresolved unknowns --")
    print("  this script does NOT attempt to supply either.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- [SPECULATIVE, clearly conditional] what an EXTRA,")
    print("unestablished assumption (A ~ G_N in magnitude, not just units)")
    print("would imply for g alone -- NOT claimed as established")
    print("-" * 78)
    print("  IF (this is an ADDITIONAL assumption this campaign has NOT")
    print("  established anywhere -- flagged, not smuggled) A's numerical")
    print("  magnitude is order-1 in units of G_N (i.e. the missing")
    print("  normalization constant is not itself wildly larger or smaller")
    print("  than Newton's constant), THEN:")
    g2_speculative = a_g2_bound / g_n_val
    g_speculative = g2_speculative**0.5
    print(f"    g^2 <~ (A*g^2)/G_N ~ {g2_speculative:.4f}")
    print(f"    g   <~ {g_speculative:.4f}   (dimensionless, per Reading 1)")
    print("  -> [SPECULATIVE] under this UNESTABLISHED extra assumption, g is")
    print("     bounded to order ~0.3-0.4 -- NOT forced to be extremely tiny.")
    print("     This is a scoping exercise only: it shows the P22/P31 ceiling")
    print("     is NOT automatically in tension with P21's own working")
    print("     assumption that g is dimensionless and presumably O(1)-ish --")
    print("     it does NOT validate the A~G_N assumption itself, which has")
    print("     no independent support anywhere in this project.")
    assert 0.0 < g_speculative < 1.0, (
        "speculative g bound outside (0,1) -- would need re-examination, "
        "not necessarily wrong but the 'not extremely tiny' framing above "
        "would need to change"
    )

    print("\n" + "=" * 78)
    print("VERDICT [CORRECTED after context-blind skeptic review, Step 8a]")
    print("=" * 78)
    print("M1 (mapping confirmed), CONDITIONAL on FINDING_P21's own S2 note")
    print("(coupling-vs-kinetic-term placement of A is convention-equivalent)")
    print("PLUS FINDING_P50B's Part 5 dimensional derivation ([A]=[G_N] under")
    print("Reading 1) -- NOT, as originally cited, P50B Part 4's two-route")
    print("agreement, which P50B's own skeptic pass already downgraded to")
    print("'propagation-verification, not independent derivation' (KG4 only")
    print("partially satisfied). Citing the wrong bridge at pre-correction")
    print("strength was itself caught and fixed. P22/P31's external")
    print("A*g^2<~8.39e-12 (SI, Reading 1, soft ceiling not precision result)")
    print("ceiling applies to the SAME A*g^2 that FINDING_P52 (this session)")
    print("proved is the field-redefinition-invariant force-strength")
    print("combination -- though A plays a conceptually different role in")
    print("each finding (P21: fixed dimensional constant; P52: free")
    print("redefinition parameter) -- both give the same invariant, and the")
    print("bound transfers either way.")
    print()
    print("This is a genuine EXTERNAL anchor, in the specific sense P50B/P51/")
    print("P52 each said was missing: it comes from an independently-")
    print("published paper's fifth-force bound, not from this project's own")
    print("internal rank/nullspace or dimensional-covariance machinery.")
    print()
    print("M3 holds regardless: the ceiling is Reading-1-specific (P21's own")
    print("stated assumption) and does NOT resolve P51's separate, still-open")
    print("Reading-1-vs-Reading-2 question -- these are two logically")
    print("independent open threads, now explicitly distinguished rather than")
    print("conflated. Only DIMENSIONAL invariance across readings was checked")
    print("(Part 3) -- the NUMERICAL value of a genuine Reading-2 re-derivation")
    print("of the ceiling is unexamined, not assumed equal to 8.39e-12.")
    print()
    print("The ceiling is CONSISTENT WITH, but does NOT itself validate, the")
    print("free-coefficient stipulation P52's N1 rests on -- a bound on the")
    print("product A*g^2 says nothing about whether C, g, lambda4 are")
    print("individually free to co-transform.")
    print()
    print("Scope, stated precisely: only ONE of P52's three invariants (A*g^2)")
    print("has this external handle. g*phi (hence mu_metric) and lambda4*A^2")
    print("remain completely unanchored. The A*g^2 ceiling does NOT, by")
    print("itself, bound mu_metric's deviation from 1 -- that would require")
    print("splitting A*g^2 into A and g individually AND a value for phibar,")
    print("neither available anywhere in this project.")
    print()
    print("Part 5's g<~0.3-0.4 figure is explicitly SPECULATIVE, conditional")
    print("on an extra, unestablished assumption (A~G_N in magnitude) -- not")
    print("promoted to a project result.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
