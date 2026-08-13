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

METHOD: symbolic derivation (sympy) of the mapping between this project's
own P21-corrected relation and Archidiacono's beta, to avoid a repeat of
this session's recurring hand-algebra slips.
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

    print("\n[STEP 3] Identification Delta_G == G_s -- STATED ASSUMPTION, not free.")
    print("  Both are defined the SAME way (coefficient of an inverse-square")
    print("  force law, same convention as Newton's G) -- but this equates")
    print("  MULTING's monopole-sector g-force to Archidiacono's DM-only")
    print("  fifth force. Licensed ONLY if MULTING's g-coupling can be treated")
    print("  as comparably constrained to a DM-only coupling -- NOT verified")
    print("  here (see Step 5 caveat).")
    combined = delta_g_def.subs(Delta_G, g_s_solved)
    print(f"  Delta_G = G_s  =>  {combined}")

    print("\n[STEP 4] Solve for A*g^2 in terms of beta, G_N")
    # sympy's solve() does not isolate a compound product like A*g**2 from a
    # Mul directly -- derive algebraically instead and verify by substitution.
    a_g2_expr = sp.simplify(4 * sp.pi * g_s_solved)
    print(f"  A*g^2 = 4*pi*G_s = 4*pi*(4*pi*beta*G_N) = {sp.expand(a_g2_expr)}")
    check = sp.simplify(a_g2_expr - 16 * sp.pi**2 * beta * G_N)
    print(f"  Verify A*g^2 - 16*pi^2*beta*G_N == 0 (symbolic check): {check == 0}")
    if check != 0:
        print("  STOP -- algebra does not check out.")
        return 1

    print("\n[STEP 5] Numeric evaluation -- CONDITIONAL, order-of-magnitude only")
    print("  Using beta<~0.01 (independently verified abstract headline figure,")
    print("  NOT the more precise 0.0054 this project previously cited but did")
    print("  not re-confirm) and G_N=6.6743e-11 (SI, matches this project's own")
    print("  P17_kappa_bounds_consistency_check.py G_SI constant).")
    beta_val = 0.01
    g_n_val = 6.6743e-11
    a_g2_bound = float(16 * sp.pi**2 * beta_val * g_n_val)
    print(f"  A*g^2 <~ 16*pi^2 * {beta_val} * {g_n_val:.5e} = {a_g2_bound:.4e}  (SI units)")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED after context-blind skeptic review, 2026-08-13")
    print("=" * 78)
    print("STRUCTURAL result (algebra A*g^2=16*pi^2*beta*G_N): CONFIRMED-REAL,")
    print("sympy-verified. NUMERIC result (A*g^2 <~ 1.05e-10): treat as a SOFT")
    print("CEILING, not a precise bound -- two independent, stacking sources of")
    print("uncertainty the original verdict understated: (1) beta's own defining")
    print("equation was read via WebFetch's small-model summarizer, not the raw")
    print("PDF -- convergent across multiple independent fetches (some evidence")
    print("against pure hallucination) but not PDF-verified; a wrong 4*pi")
    print("placement would shift the result by a factor of ~158. (2) Archidiacono's")
    print("phi couples ONLY to dark matter (paper's own abstract separately names")
    print("'searches for violations of the Equivalence Principle in the visible")
    print("sector' as a DIFFERENT constraint channel) -- if MULTING's g is a")
    print("genuinely universal coupling, the real bound is very plausibly many")
    print("orders of magnitude tighter than 1.05e-10, not just 'comparable'.")
    print("Bounds only the PRODUCT A*g^2 -- g and A remain individually")
    print("unbounded, and Omega_phi (built from kappa, not g) is NOT thereby")
    print("fixed regardless of which reading is correct.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
