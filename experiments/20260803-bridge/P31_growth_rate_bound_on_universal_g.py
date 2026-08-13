"""P31 -- maps a REAL, verified growth-of-structure/CMB bound on a constant,
scale-independent modification to Newton's constant (Bean & Tangmatitham
2010, arXiv:1002.4197, Phys. Rev. D 81, 083534) onto MULTING's own A*g^2
quantity, via P30's own derived equation.

This is the next, separate step P30's own section 3 (corrected) explicitly
deferred: a real literature search for a growth-of-structure bound on
Delta_G/G_N, using P30's derived equation
    delta_m'' + ... = 4*pi*G_eff*rho_m*a^2*delta_m,   G_eff = G_N + Delta_G
as the target functional form.

SOURCE VERIFICATION (WebFetch, this session, two targeted fetches of
arxiv.org/html/1002.4197):
  - Their eq. 6: "k^2*phi = -4*pi*G*Q*a^2*sum_i(rho_i*Delta_i)" -- a modified
    Poisson equation, Q multiplying G exactly where P30's own G_eff
    multiplies G_N. Q IS G_eff/G_N for the matter-sourced Poisson equation,
    confirmed by direct structural comparison to P30's own eq. (both are
    "4*pi*[G-type coupling]*a^2*rho*delta", nothing else differs).
  - Abstract + Table 1: for the time-independent, scale-independent case
    (their notation: s=0, k_c=infinity), "Q-1 <~ 3%" at 95% CL, from CMB
    (dominant constraint) + growth-rate + lensing data combined. Table 1:
    Q in [0.97, 1.01] at 95% CL.

IMPORTANT: unlike Archidiacono's beta (P22, P28, P29), this Q is a
UNIVERSAL modifier -- their own Poisson equation (eq. 6) sums over ALL
matter species (sum_i rho_i*Delta_i), not a DM-only subset. This is
therefore, for the first time in this project's P21-P30 arc, a bound whose
TARGET POPULATION and COUPLING TOPOLOGY genuinely match MULTING's own
universal g (P23) -- not merely a proxy requiring the P23/P28/P29 caveats.
"""

import sympy as sp


def main():
    G_N, Q, Delta_G_over_GN = sp.symbols("G_N Q Delta_G_over_GN", positive=True)

    print("=" * 78)
    print("P31 -- real growth-of-structure bound on universal Delta_G/G_N")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Bean & Tangmatitham (2010) eq. 6 vs P30's own derived equation")
    print("  Their eq. 6: k^2*phi = -4*pi*G_N*Q*a^2*sum_i(rho_i*Delta_i)")
    print("  P30's own:   S_m       =  4*pi*G_eff*rho_m*a^2*delta_m")
    print("  Structural match: Q plays the SAME role as G_eff/G_N -- both")
    print("  multiply the standard 4*pi*G*a^2*rho*delta Poisson source term.")
    print("  Identification: Q === G_eff/G_N  (verified by direct equation")
    print("  comparison, not assumed by symbol-name similarity alone).")

    print("\n[STEP 2] Their reported bound (Table 1, time- and scale-independent")
    print("  case, CMB+growth+lensing combined, 95% CL):")
    print("  Q in [0.97, 1.01]  =>  |Q-1| <~ 0.03")
    q_minus_1_bound = sp.Rational(3, 100)
    print(f"  Delta_G/G_N = Q - 1, bound: |Delta_G/G_N| <~ {float(q_minus_1_bound)}")

    print("\n[STEP 3] Map onto MULTING's A*g^2 via P30's own derived relation")
    print("  (itself built on P21's A*g^2 = 4*pi*Delta_G):")
    G_N_val = sp.Float(6.6743e-11)
    delta_g_bound = q_minus_1_bound * G_N_val
    a_g2_bound = 4 * sp.pi * delta_g_bound
    print(f"  Delta_G <~ {float(delta_g_bound):.5e} (SI, m^3 kg^-1 s^-2)")
    print(f"  A*g^2 <~ 4*pi*Delta_G = {float(a_g2_bound):.4e} (SI)")

    print("\n[STEP 4] Compare to FINDING_P22's corrected Archidiacono-based ceiling")
    print("  (A*g^2 <~ 8.39e-12 SI):")
    p22_ceiling = sp.Float(8.39e-12)
    ratio = sp.simplify(a_g2_bound / p22_ceiling)
    print(f"  Ratio (this growth-route bound / P22's ceiling) = {float(ratio):.3f}")
    if float(ratio) > 1:
        print("  This growth-of-structure bound is LOOSER (weaker) than P22's,")
        print("  despite being the topologically CORRECT bound for a universal")
        print("  coupling (unlike Archidiacono's DM-only beta) -- a real,")
        print("  non-obvious result: topological correctness does not")
        print("  automatically mean numerically tighter.")
    else:
        print("  This growth-of-structure bound is TIGHTER than P22's.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("A REAL, externally-sourced, verified bound (Bean & Tangmatitham 2010,")
    print("Table 1) maps onto A*g^2 <~ 2.52e-11 (SI) via P30's own derived")
    print("equation. Unlike FINDING_P22's Archidiacono-based ceiling, this bound's")
    print("target (Q, a universal Poisson-equation modifier summed over ALL")
    print("matter species) genuinely matches MULTING's own universal g coupling")
    print("(P23) -- no DM-only-vs-universal topology mismatch. Numerically,")
    print("however, this bound is LOOSER than P22's by roughly a factor of 3 --")
    print("topological correctness and numeric tightness are independent axes.")
    print("This is a 2010-era result; more recent DESI-era growth-rate analyses")
    print("may give different (plausibly tighter) numbers -- not chased down")
    print("here, an open precision gap flagged explicitly, not assumed closed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
