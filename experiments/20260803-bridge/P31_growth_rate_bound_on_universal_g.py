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
    Poisson equation (an algebraic/elliptic relation for phi at fixed time,
    sourced by the density perturbation), not itself a growth equation.
  - Abstract + Table 1: for the time-independent, scale-independent case
    (their notation: s=0, k_c=infinity), "Q-1 <~ 3%" at 95% CL, from CMB
    (dominant constraint) + growth-rate + lensing data combined. Table 1:
    Q in [0.97, 1.01] at 95% CL -- an ASYMMETRIC interval.

CORRECTED 2026-08-13, after context-blind skeptic review, same day. TWO
real issues fixed, not just framing:
  (1) THE CONSEQUENTIAL ONE -- the original version used the WRONG edge of
      Table 1's asymmetric interval. Q in [0.97, 1.01] allows Q < 1
      (Delta_G < 0, a REPULSIVE modification) just as much as Q > 1
      (Delta_G > 0, attractive). But MULTING's own action structure forces
      Delta_G >= 0 ALWAYS: A*g^2 = 4*pi*Delta_G (P21, corrected), and both
      A and g^2 are structurally non-negative (A carries G's units,
      established positive; g^2 is a square) -- a scalar-mediated exchange
      force between like "charges" (masses) is always attractive, exactly
      like gravity itself. The physically-relevant one-sided bound is
      therefore Q-1 <= 0.01 (the UPPER edge), not |Q-1| <= 0.03 (which used
      the wrong, physically-excluded lower edge). Independently re-derived
      before accepting this correction: confirmed Delta_G>=0 is forced by
      the ALREADY-established A*g^2=4*pi*Delta_G relation (P21), not a new
      assumption. Fixed below -- this changes the numeric result from
      2.52e-11 to ~8.39e-12, essentially IDENTICAL to FINDING_P22's own
      corrected ceiling, overturning the original "3x looser" headline.
  (2) The "Q === G_eff/G_N, verified by direct equation comparison"
      framing conflated a Poisson equation (B&T's eq. 6, an algebraic
      relation for phi) with a growth equation (P30's own dynamical
      equation for delta_m) as if comparing them directly were valid. The
      identification IS physically correct -- Q genuinely plays the role
      of G_eff/G_N once propagated through the standard Poisson-source ->
      Friedmann-identity -> growth-equation derivation chain (the same
      chain P30 itself used) -- but "direct equation comparison" overstated
      the licensing. Corrected language below.
"""

import sympy as sp


def main():
    G_N, Q = sp.symbols("G_N Q", positive=True)

    print("=" * 78)
    print("P31 -- real growth-of-structure bound on universal Delta_G/G_N (CORRECTED)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Bean & Tangmatitham (2010) eq. 6 -- a Poisson equation, not")
    print("  itself a growth equation:")
    print("  k^2*phi = -4*pi*G_N*Q*a^2*sum_i(rho_i*Delta_i)")
    print("  Q plays the role of G_eff/G_N once propagated through the standard")
    print("  Poisson-source -> Friedmann-identity -> growth-equation chain (the")
    print("  SAME chain P30 itself used, not a direct structural comparison of")
    print("  two different KINDS of equation).")

    print("\n[STEP 2] Their reported bound (Table 1, time- and scale-independent")
    print("  case, CMB+growth+lensing combined, 95% CL) -- an ASYMMETRIC interval:")
    print("  Q in [0.97, 1.01]")
    print("  Two possible one-sided readings:")
    q_lower_edge = sp.Rational(97, 100) - 1  # Q=0.97 -> Delta_G<0, repulsive
    q_upper_edge = sp.Rational(101, 100) - 1  # Q=1.01 -> Delta_G>0, attractive
    print(f"    lower edge: Q-1 = {float(q_lower_edge)} (Delta_G<0, REPULSIVE)")
    print(f"    upper edge: Q-1 = {float(q_upper_edge)} (Delta_G>0, ATTRACTIVE)")

    print("\n[STEP 3] Which edge is physically relevant for MULTING's g?")
    print("  P21's own corrected relation: A*g^2 = 4*pi*Delta_G. Both A ([G]-units,")
    print("  established positive) and g^2 (a square) are structurally")
    print("  non-negative -- Delta_G >= 0 is FORCED, not assumed. A scalar-mediated")
    print("  exchange force between like masses is always attractive, exactly like")
    print("  gravity itself.")
    delta_g_over_gn_bound = q_upper_edge  # the physically-relevant, tighter edge
    assert delta_g_over_gn_bound >= 0
    print(f"  Physically-relevant one-sided bound: Delta_G/G_N <= {float(delta_g_over_gn_bound)}")

    print("\n[STEP 4] Map onto MULTING's A*g^2 via P21/P30's own derived relation:")
    G_N_val = sp.Float(6.6743e-11)
    delta_g_bound = delta_g_over_gn_bound * G_N_val
    a_g2_bound = 4 * sp.pi * delta_g_bound
    print(f"  Delta_G <= {float(delta_g_bound):.5e} (SI, m^3 kg^-1 s^-2)")
    print(f"  A*g^2 <= 4*pi*Delta_G = {float(a_g2_bound):.4e} (SI) -- arithmetic")
    print("  checked with sympy, not a physics 'verification'.")

    print("\n[STEP 5] Compare to FINDING_P22's corrected Archidiacono-based ceiling")
    print("  (A*g^2 <~ 8.39e-12 SI):")
    p22_ceiling = sp.Float(8.39e-12)
    ratio = sp.simplify(a_g2_bound / p22_ceiling)
    print(f"  Ratio (this corrected growth-route bound / P22's ceiling) = {float(ratio):.4f}")
    print("  ESSENTIALLY IDENTICAL (within 0.1%) -- NOT 3x looser, as the original")
    print("  version of this finding claimed using the wrong interval edge.")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED after context-blind skeptic review, same day")
    print("=" * 78)
    print("A REAL, externally-sourced bound (Bean & Tangmatitham 2010, Table 1)")
    print("maps onto A*g^2 <~ 8.39e-12 (SI) via P21/P30's own derived chain, using")
    print("the physically-relevant one-sided edge of an asymmetric interval --")
    print("essentially IDENTICAL to FINDING_P22's own Archidiacono-based ceiling,")
    print("a striking numerical coincidence between two independently-derived")
    print("bounds from different mechanisms and eras of data, not a deeper")
    print("physical connection (not claimed as one). This bound's target (Q, a")
    print("universal Poisson-equation modifier summed over ALL matter species) is")
    print("structurally closer to MULTING's universal g than Archidiacono's")
    print("DM-only beta -- but this project's own (Q,R)-parametrization")
    print("universality is a MODELING CHOICE by the source paper, not a proof that")
    print("any mechanism producing this phenomenology is automatically universal;")
    print("applying it to MULTING's g still assumes g produces a species-uniform,")
    print("scale-independent, time-independent Poisson modification (P23's")
    print("reading), not an unconditional fact. This is a 2010-era result; more")
    print("recent DESI-era analyses were not searched for, an open precision gap.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
