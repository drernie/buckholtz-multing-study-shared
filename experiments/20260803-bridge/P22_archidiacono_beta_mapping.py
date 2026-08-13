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
    from Planck + BAO (no DESI in this version), for m_phi <~ H0 (the same
    long-range regime this project's own mu~H0/c mechanism, P11, lives in).
  - NOT independently confirmed at this session's precision: the tighter
    "beta<0.0054" figure FINDING_P13a originally cited. Section 5's precise
    tables were not accessible (PDF mirror returned HTTP 403; HTML excerpt
    insufficient). Flagged as an open precision gap, not assumed.

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
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (structural + conditional numeric): Archidiacono's own")
    print("beta<~0.01 (Planck+BAO, m_phi<~H0, DM-only coupling -- source text")
    print("independently verified this session) maps, via the identification")
    print("Delta_G==G_s, onto A*g^2 <~ 1.05e-10 (SI). This bounds the PRODUCT")
    print("A*g^2 only -- g and A remain individually unbounded, and Omega_phi")
    print("(built from kappa, not g) is NOT thereby fixed. The mapping is")
    print("CONDITIONAL on treating MULTING's g-coupling as comparably")
    print("constrained to Archidiacono's DM-only coupling -- NOT the same")
    print("measurement, not verified here, and Archidiacono's own paper")
    print("explicitly excludes baryon coupling entirely (not just weakly).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
