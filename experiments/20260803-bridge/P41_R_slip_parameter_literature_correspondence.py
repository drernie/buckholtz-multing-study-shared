"""P41 -- eighth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction. FINDING_P31 cited
Bean & Tangmatitham (arXiv:1002.4197) for their Q parameter (already
mapped to this project's own Delta_G), but explicitly flagged their OWN
slip parameter R as unverified: "the surrounding machinery (eq. 7, the
anisotropic-stress/lensing-slip parameter R... is not independently
re-derived." This step closes exactly that flagged gap -- and, doing so
carefully, finds a real notation-inversion trap: their R is NOT simply
equal to this project's own gamma (P40), it is gamma's RECIPROCAL, once
the two papers' metric conventions are correctly matched (verified by
direct WebFetch of their own eq. 1, not assumed).

Deliberately does NOT attempt a numeric comparison to their reported
R in [0.99, 1.02] bound -- that is blocked by the SAME SI-units gap
FINDING_P39 already identified (ghat has no established SI value), not a
new blocker. This step is a literature-correspondence and notation-
translation registration only.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    ghat, M, r, G_N = sp.symbols("g_hat M r G_N", positive=True)

    print("=" * 78)
    print("P41 -- does Bean & Tangmatitham's own R correspond to this project's")
    print("own gamma (P40), and if so, how exactly?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Verified quotes (direct WebFetch, arxiv.org/html/1002.4197,")
    print("  not paraphrased from memory):")
    print("  Their eq. 1 (metric): ds^2 = -a(tau)^2[1+2*psi(x,t)]*dtau^2")
    print("                              + a(tau)^2[1-2*phi(x,t)]*dx^2")
    print("  -> psi multiplies the TIME-TIME term, phi multiplies the SPATIAL")
    print("     term -- exactly this project's own P38 convention")
    print("     (ds^2=-(1+2*Phi)dt^2+(1-2*Psi)dx^2): their psi <-> this")
    print("     project's Phi; their phi <-> this project's Psi.")
    print("  Their eq. 7 (slip relation, no-anisotropic-stress limit):")
    print("     psi = R*phi   =>   R := psi/phi")
    print("  Their Table 1 (time-/scale-independent case, 95% CL, all data):")
    print("     R in [0.99, 1.02]")

    print("\n[STEP 2] Translate their R into THIS project's own Phi,Psi notation")
    print("  (their psi=our Phi, their phi=our Psi):")
    Phi, Psi = sp.symbols("Phi Psi")
    R_literature = Phi / Psi
    print(f"  R (Bean & Tangmatitham, in this project's notation) = {R_literature}")

    print("\n[STEP 3] Compare to this project's OWN gamma (P40, skeptic-confirmed")
    print("  standard PPN convention: gamma := Psi/Phi):")
    gamma_def = Psi / Phi
    print(f"  gamma := Psi/Phi = {gamma_def}")
    relation = sp.simplify(R_literature - 1 / gamma_def)
    print(f"  R - 1/gamma = {relation}")
    assert relation == 0, "R does not equal 1/gamma -- re-check the algebra"
    print("  -> R = 1/gamma EXACTLY. NOT R = gamma. This is a genuine notation")
    print("     inversion between the two conventions (PPN gamma:=Psi/Phi vs.")
    print("     Bean&Tangmatitham's own R:=psi/phi=Phi/Psi in this project's")
    print("     labels) -- confirmed algebraically, not assumed.")

    print("\n[SANITY CHECK, added after skeptic review -- honestly labeled, NOT a")
    print("  positive control] The R=1/gamma relation above is a tautology given")
    print("  its own premises (R and gamma are just two named ratios of the same")
    print("  two symbols) and cannot by itself catch a transcription error in which")
    print("  symbol was assigned to which literature quantity -- that direction was")
    print("  instead checked by independently re-fetching the primary source a")
    print("  second time, with differently-worded queries, both returning the same")
    print("  literal 'psi-R*phi=...' equation (see finding doc Sec.1). What THIS")
    print("  check adds is narrower: applying the R:=1/gamma mapping to a REAL,")
    print("  well-known reference theory (Brans-Dicke, PPN gamma=(1+omega)/(2+omega),")
    print("  omega=the BD coupling constant) gives a well-defined, finite,")
    print("  positive-for-omega>0 result -- ruling out the mapping producing")
    print("  something structurally absurd. [CORRECTED, self-caught before commit:]")
    print("  this does NOT independently verify the ψ/φ direction (no separately-")
    print("  published R_BD value is compared against -- the 'independently-")
    print("  published form' would just be the same formula computed the same way)")
    print("  -- an earlier draft of this check overclaimed exactly that, corrected")
    print("  here rather than left in:")
    omega = sp.Symbol("omega", positive=True)
    gamma_BD = (1 + omega) / (2 + omega)
    R_BD_via_mapping = sp.simplify(1 / gamma_BD)
    print(f"  gamma_BD (published PPN result, Will 1993/Damour) = {gamma_BD}")
    print(f"  R_BD, via this finding's own R=1/gamma mapping = {R_BD_via_mapping}")
    numeric_check = R_BD_via_mapping.subs(omega, 5)
    print(f"  numeric spot-check at omega=5: R_BD = {numeric_check}")
    assert numeric_check > 0, "R_BD mapping gives a non-physical (negative) result"
    print("  -> well-defined and positive, as expected for a real theory -- a weak")
    print("     but genuine sanity check, correctly scoped as such.")

    print("\n[STEP 4] Substitute P40's own gamma=1-g_hat^2*M/(16*pi*r) to get this")
    print("  project's own reconstruction's PREDICTED functional form for R,")
    print("  expressed in Bean & Tangmatitham's own literature quantity:")
    gamma_p40 = 1 - ghat**2 * M / (16 * sp.pi * r)
    R_predicted = sp.simplify(1 / gamma_p40)
    print(f"  gamma (P40) = {gamma_p40}")
    print(f"  R (this project's own prediction, exact) = 1/gamma = {R_predicted}")
    R_series = sp.series(R_predicted, ghat, 0, 3).removeO()
    print(f"  R, leading order in g_hat^2 (series expansion) = {R_series}")

    print("\n[STEP 5] Sanity check -- does R come out on the correct SIDE of 1")
    print("  (R>1), consistent with gamma<1 (P40's own established sign)?")
    leading_correction = sp.simplify(R_series - 1)
    print(f"  R - 1 (leading order) = {leading_correction}")
    is_positive = leading_correction.is_positive
    print(f"  Is this positive (R>1)?  {is_positive}")
    assert is_positive, "expected R>1 at leading order, given gamma<1"
    print("  -> Confirmed: R>1 at leading order, the correct sign given gamma<1.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Bean & Tangmatitham's own R (arXiv:1002.4197, eq. 7, R:=psi/phi in")
    print("their notation) is, once their metric convention is correctly matched")
    print("to this project's own (verified, not assumed), the RECIPROCAL of this")
    print("project's own gamma (P40) -- R=1/gamma, not R=gamma. Substituting P40's")
    print("own result gives this project's own reconstruction's predicted R, at")
    print(f"leading order: R = {R_series}, i.e. R>1 (not R<1), the opposite")
    print("direction from gamma's own <1 result -- same physics, correctly")
    print("translated, not a contradiction.")
    print()
    print("NOT attempted here: any numeric comparison to their reported R in")
    print("[0.99, 1.02] (95% CL) -- blocked by the same g_hat SI-units gap")
    print("FINDING_P39 already identified, not a new blocker introduced here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
