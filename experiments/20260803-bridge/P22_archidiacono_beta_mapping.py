"""P22_archidiacono_beta_mapping.py -- P21 named Archidiacono et al.'s
beta<~0.01 fifth-force bound as the natural second equation needed to turn
A*g^2=4*pi*DeltaG (P21, corrected) into an actual number, but explicitly did
NOT attempt to verify Archidiacono's own definition of beta against the real
paper. This script does that verification and derives the mapping.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive

SOURCE VERIFICATION (WebFetch, this session, arxiv.org/abs/2204.08484 +
arxiv.org/html/2204.08484, cross-checked against a second independent
fetch): Archidiacono, Castorina, Redigolo, Salvioni, "Unveiling dark fifth
forces with linear cosmology," JCAP 10 (2022) 074 (arXiv v4, Nov 2025).

VERIFIED QUOTES (not paraphrased):
  - Eq 2.10: "beta == G_s / (4*pi*G_N)"
  - Eq 2.17: "G_s = g_D^2 / m_chi^2"  (for their specific fermionic-mediator UV completion)
  - Eqs 2.15-2.16: coupling terms are "-g_D*phi*chibar*chi" (fermionic DM) and
    "-g_D*m_chi*phi*chi^2" (scalar DM) -- phi couples ONLY to the DM field chi.
  - Confirmed (TWO independent fetches): "baryons are completely unaffected
    by the scalar fifth force" -- zero baryon coupling in this model, not a
    small one.
  - Abstract headline bound: "less than a percent of gravity" -> beta ~< 0.01,
    from Planck + BAO, for m_phi <~ H0 (the same long-range regime this
    project's own mu~H0/c mechanism, P11, lives in).
  - NOT independently confirmed at this session's precision: the tighter
    "beta<0.0054" figure FINDING_P13a originally cited. Section 5's precise
    tables were not accessible (PDF mirror returned HTTP 403; HTML excerpt
    insufficient). Flagged as an open precision gap, not assumed.

  CORRECTED 2026-08-13, after context-blind skeptic review: the original
  version of this docstring claimed "no DESI in this version -- v4 predates
  DESI DR2." That explanation was WRONG (a reasoning error, not a WebFetch
  misquote) -- v4 is dated Nov 2025, well AFTER DESI DR2's release. Re-fetched
  the paper's own version changelog directly: v4's only change was "fixed
  some coefficients in analytical sub-horizon solutions (Sec 4.2.1)" -- an
  unrelated technical erratum, not a data update. The paper's constraint
  dataset (Planck+BAO, plus MICROSCOPE/atomic-clock comparisons added in
  v2/v3) was never updated with DESI across any version, for reasons the
  changelog does not state -- NOT because DESI didn't exist yet.

  CORRECTED AGAIN 2026-08-13 (SAME DAY), after a real, user-flagged 4*pi
  error, independently re-verified before accepting (fresh WebFetch, this
  session): the original STEP 3 below identified Delta_G === G_s directly.
  This double-counts a 4*pi factor. Two independently-quoted facts from the
  paper (both re-verified via a fresh, targeted WebFetch this session) show
  the correct identification is A*g^2 === G_s (NOT Delta_G === G_s):
    (i) the paper's own short-distance statement: "at distances r << 1/m_phi
        the long range force is equivalent to a shift in Newton's constant,
        G_N -> G_N(1+beta)" -- i.e. Delta_G_Archidiacono = beta*G_N DIRECTLY,
        with no G_s in the chain at all;
    (ii) the paper's own description of G_s: "a dimensionful constant
        analogous to G_N" -- i.e. G_s sits at the SAME un-normalized level as
        this project's own A*g^2 (both are "4*pi times the actual Delta_G"),
        not at the level of Delta_G itself.
  Both routes independently give A*g^2 = 4*pi*beta*G_N -- verified below they
  agree with each other, which is itself a consistency check on Archidiacono's
  own two stated facts. NOT independently re-derived: G_s = g_D^2/m_chi^2
  (Eq 2.17) from first principles -- this requires their specific fermionic-
  UV-completion non-relativistic field normalization, not attempted here to
  avoid introducing a NEW, different error; Route (i) below deliberately
  avoids this dependency.

METHOD: symbolic derivation (sympy) of the mapping between this project's
own P21-corrected relation and Archidiacono's beta, to avoid a repeat of
this session's recurring hand-algebra slips. Two independent routes are
derived and cross-checked against each other (see Steps 3a/3b).
"""

from __future__ import annotations

import sympy as sp


def main() -> int:
    print("=" * 78)
    print("P22 -- verifying Archidiacono's beta definition, mapping onto A*g^2")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    A, g, beta, G_N, Delta_G, G_s = sp.symbols("A g beta G_N Delta_G G_s", positive=True)

    print("\n[STEP 1] Archidiacono's own definition (verified, Eq 2.10):")
    print("  beta = G_s / (4*pi*G_N)")
    archidiacono_def = sp.Eq(beta, G_s / (4 * sp.pi * G_N))
    print(f"  {archidiacono_def}")
    g_s_solved = sp.solve(archidiacono_def, G_s)[0]
    print(f"  => G_s = {g_s_solved}")

    print("\n[STEP 2] This project's own P21-corrected force law:")
    print("  F_MULT(r) = A * c_G * g^2 * m1*m2/r^2 = (A*g^2/(4*pi)) * m1*m2/r^2")
    print("  Defining Delta_G via F_MULT(r) = Delta_G * m1*m2/r^2:")
    delta_g_def = sp.Eq(Delta_G, A * g**2 / (4 * sp.pi))
    print(f"  {delta_g_def}")

    print("\n[STEP 3a] Route 1 -- direct short-distance statement (safest route,")
    print("  no dependence on G_s's own g_D/m_chi normalization). Paper's own")
    print("  quote: 'at r<<1/m_phi, G_N -> G_N(1+beta)' => Delta_G = beta*G_N")
    print("  DIRECTLY, bypassing G_s entirely.")
    route1_delta_g = beta * G_N
    route1_a_g2 = sp.simplify(4 * sp.pi * route1_delta_g)
    print(f"  Delta_G_Archidiacono = beta*G_N = {route1_delta_g}")
    print(f"  => A*g^2 = 4*pi*Delta_G = {sp.expand(route1_a_g2)}")

    print("\n[STEP 3b] Route 2 -- structural identification A*g^2 === G_s")
    print("  (CORRECTED from the original, WRONG Delta_G === G_s). Paper's own")
    print("  quote: 'G_s is a dimensionful constant analogous to G_N' -- G_s sits")
    print("  at the SAME un-normalized level as A*g^2 (both are 4*pi*Delta_G),")
    print("  not at the level of Delta_G itself. Licensed ONLY as an identification")
    print("  of MULTING's monopole-sector g-force with Archidiacono's DM-only")
    print("  fifth force -- NOT verified that MULTING's g can be treated as")
    print("  comparably constrained to a DM-only coupling (see Step 6 caveat).")
    route2_a_g2 = sp.simplify(g_s_solved)  # A*g^2 := G_s, so A*g^2 = 4*pi*beta*G_N
    print(f"  A*g^2 = G_s = {sp.expand(route2_a_g2)}")

    print("\n[STEP 4] Cross-check: do the two independent routes agree?")
    routes_agree = sp.simplify(route1_a_g2 - route2_a_g2) == 0
    print(f"  Route 1 - Route 2 == 0 (symbolic check): {routes_agree}")
    if not routes_agree:
        print("  STOP -- the two routes disagree, do not proceed.")
        return 1
    print("  Agreement confirms Archidiacono's own two stated facts (the G_s")
    print("  definition, and the short-distance G_N->G_N(1+beta) statement)")
    print("  are mutually consistent -- this is the positive-control check for")
    print("  this correction, not an assumption.")

    print("\n[STEP 5] Final result, verified against the naive/wrong 16*pi^2 form")
    a_g2_expr = route1_a_g2
    print(f"  A*g^2 = {sp.expand(a_g2_expr)}")
    wrong_check = sp.simplify(a_g2_expr - 16 * sp.pi**2 * beta * G_N)
    print(f"  A*g^2 - 16*pi^2*beta*G_N == 0 (should be FALSE now): {wrong_check == 0}")
    if wrong_check == 0:
        print("  STOP -- still matches the old, wrong form.")
        return 1
    correct_check = sp.simplify(a_g2_expr - 4 * sp.pi * beta * G_N)
    print(f"  A*g^2 - 4*pi*beta*G_N == 0 (should be TRUE): {correct_check == 0}")
    if correct_check != 0:
        print("  STOP -- algebra does not check out.")
        return 1

    print("\n[STEP 6] Numeric evaluation -- CONDITIONAL, order-of-magnitude only")
    print("  Using beta<~0.01 (independently verified abstract headline figure,")
    print("  NOT the more precise 0.0054 this project previously cited but did")
    print("  not re-confirm) and G_N=6.6743e-11 (SI, matches this project's own")
    print("  P17_kappa_bounds_consistency_check.py G_SI constant).")
    beta_val = 0.01
    g_n_val = 6.6743e-11
    a_g2_bound = float(4 * sp.pi * beta_val * g_n_val)
    print(f"  A*g^2 <~ 4*pi * {beta_val} * {g_n_val:.5e} = {a_g2_bound:.4e}  (SI units)")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED 2026-08-13 (user-flagged 4*pi error, independently")
    print("re-verified before accepting)")
    print("=" * 78)
    print("STRUCTURAL result (algebra A*g^2=4*pi*beta*G_N): CONFIRMED-REAL,")
    print("sympy-verified, TWO independent routes agree (Step 4). NUMERIC result")
    print(f"(A*g^2 <~ {a_g2_bound:.2e}): still a SOFT CEILING, not a precise bound --")
    print("the same two stacking uncertainties as before remain: (1) beta's own")
    print("defining equation was read via WebFetch's small-model summarizer, not")
    print("the raw PDF; (2) Archidiacono's phi couples ONLY to dark matter -- if")
    print("MULTING's g is a genuinely universal coupling, the real bound is very")
    print("plausibly many orders of magnitude tighter than this number, not just")
    print("'comparable' (see P23, P28, P29 for further, independent sharpening of")
    print("this same caveat). Bounds only the PRODUCT A*g^2 -- g and A remain")
    print("individually unbounded, and Omega_phi (built from kappa, not g) is NOT")
    print("thereby fixed regardless of which reading is correct. This corrected")
    print("number is TIGHTER than the old (wrong) one by exactly 4*pi (~12.57x),")
    print("not looser -- the qualitative soft-ceiling status is unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
