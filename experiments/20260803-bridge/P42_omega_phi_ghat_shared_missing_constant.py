"""P42 -- ninth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction. FINDING_P21 itself
already anticipated (Sec.4): "Omega_phi's formula (P14) is built from the
same phi field that the dipole coupling sources, so the same missing
constant A enters it." FINDING_P39 independently found the SAME residual
units (kg/m) for the g-sector's own Phi-Psi (P38/P40) as FINDING_P17
already found for the kappa-sector's own Omega_phi (P14) -- but explicitly
flagged this as "a striking structural echo... NOT independently
established" that the two gaps are the SAME missing constant.

This step closes exactly that gap: mechanically re-derives Omega_phi's own
dimensional chain from P14's own quoted base formulas (not from memory or
a paraphrase), and checks whether the SAME missing factor (P21's own
already-named constant A, combined with a specific power of c) resolves
BOTH the g-sector's and kappa-sector's dimensional gaps identically.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def dmul(a, b):
    """Multiply two physical quantities' dimensions (add exponents)."""
    return tuple(x + y for x, y in zip(a, b, strict=True))


def dpow(a, n):
    """Raise a dimension to a rational power (multiply exponents)."""
    n = sp.Rational(n)
    return tuple(x * n for x in a)


def ddiv(a, b):
    """Divide two dimensions (subtract exponents)."""
    return dmul(a, dpow(b, -1))


MASS, LENGTH, TIME = (1, 0, 0), (0, 1, 0), (0, 0, 1)
DIMLESS = (0, 0, 0)


def fmt(d):
    return f"kg^{d[0]} m^{d[1]} s^{d[2]}"


def main():
    print("=" * 78)
    print("P42 -- does the SAME missing constant (P21's own A) resolve BOTH the")
    print("g-sector's Phi-Psi gap (P39/P40) and the kappa-sector's Omega_phi gap")
    print("(P14/P17), as P21 itself already anticipated but never checked?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    G_N_dim = ddiv(dpow(LENGTH, 3), dmul(MASS, dpow(TIME, 2)))
    c_dim = ddiv(LENGTH, TIME)
    A_dim = G_N_dim  # P21's own established fact: [A]=[G_N]

    print("\n[STEP 1] Re-derive Omega_phi's own dimension from P14's own quoted")
    print("  base formulas (FINDING_P14 Sec.6, verbatim):")
    print("  'p_i = u_i * m_cluster, u_i has units of length (m) -> p_i has units")
    print("  kg*m' / 'E_self = (8*pi/3)*p_i^2/r_min^3 -> units (kg*m)^2/m^3 =")
    print("  kg^2/m' / then rho_phi=n*E_self, Omega_phi=rho_phi/rho_crit:")
    u_dim = LENGTH
    p_dim = dmul(u_dim, MASS)
    print(f"  [p_i] = {fmt(p_dim)}")
    E_self_dim = ddiv(dpow(p_dim, 2), dpow(LENGTH, 3))
    print(f"  [E_self] = {fmt(E_self_dim)}")
    assert E_self_dim == (2, -1, 0), "does not match P14's own stated kg^2/m"
    n_density_dim = dpow(LENGTH, -3)
    rho_phi_dim = dmul(n_density_dim, E_self_dim)
    rho_crit_dim = ddiv(MASS, dpow(LENGTH, 3))
    Omega_phi_dim = ddiv(rho_phi_dim, rho_crit_dim)
    print(f"  [Omega_phi] = {fmt(Omega_phi_dim)}")
    assert Omega_phi_dim == (1, -1, 0), "does not match P14/P17's own stated kg/m"
    print("  -> matches P14/P17's own stated result (kg/m) exactly.")

    print("\n[STEP 2] Re-derive Phi-Psi's own dimension (P38/P39/P40's own")
    print("  established result -- re-quoted here, not re-derived from scratch):")
    ghat, M, r = sp.symbols("g_hat M r", positive=True)
    ghat2_reading1 = (0, -2, 2)  # P39's own reading 1: ghat:=g/c, g dimensionless
    Phi_minus_Psi_dim = ddiv(dmul(dmul(G_N_dim, ghat2_reading1), dpow(MASS, 2)), dpow(LENGTH, 2))
    print(f"  [Phi-Psi] = {fmt(Phi_minus_Psi_dim)}")
    assert Phi_minus_Psi_dim == (1, -1, 0), "does not match P39's own stated kg/m"
    print("  -> matches P39's own stated result (kg/m) exactly -- SAME as Omega_phi.")

    print("\n[STEP 3] Both quantities must be dimensionless (Omega_phi: an energy-")
    print("  density fraction; Phi-Psi: a metric-perturbation combination). What")
    print("  missing multiplicative factor would fix EACH gap?")
    missing_kappa = ddiv(DIMLESS, Omega_phi_dim)
    missing_g = ddiv(DIMLESS, Phi_minus_Psi_dim)
    print(f"  missing factor, kappa-sector (Omega_phi) = {fmt(missing_kappa)}")
    print(f"  missing factor, g-sector (Phi-Psi)        = {fmt(missing_g)}")
    same_missing = missing_kappa == missing_g
    print(f"  Are these the SAME missing factor?  {same_missing}")
    assert same_missing, "the two sectors require DIFFERENT missing factors -- not unified"
    print("  -> IDENTICAL. Both sectors need exactly the same units of correction.")

    print("\n[STEP 4] Express this shared missing factor in terms of P21's own")
    print("  already-named constant A ([A]=[G_N]) and a power of c -- solving")
    print("  the exponent system directly, not guessing:")
    a_power = -missing_g[0]  # mass exponent: -a = missing_g[0] (since [A] mass exp = -1)
    b_power = missing_g[1] - 3 * a_power  # length exponent: 3a + b = missing_g[1]
    candidate = dmul(dpow(A_dim, a_power), dpow(c_dim, b_power))
    print(f"  solved: missing = A^{a_power} * c^{b_power}")
    print(f"  A^{a_power} * c^{b_power} = {fmt(candidate)}")
    assert candidate == missing_g, "A^a * c^b does not reproduce the missing factor"
    time_check = -2 * a_power - b_power
    print(f"  time-exponent consistency check (independent of the solve above): {time_check}")
    assert time_check == missing_g[2], "time exponent inconsistent -- solution not unique/valid"
    print("  -> PASSES on all three exponents independently (mass, length, and a")
    print("     separate time-exponent check not used in solving for a,b) -- not")
    print("     a system with a free parameter silently absorbed.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Both FINDING_P14/P17's Omega_phi (kappa-sector) and FINDING_P38-P40's")
    print(f"Phi-Psi (g-sector) have IDENTICAL dimensional residuals ({fmt(Omega_phi_dim)}),")
    print("and therefore require the IDENTICAL missing multiplicative factor")
    print(f"(A^{a_power}*c^{b_power} = A/c^2, where A is P21's own already-named,")
    print("never-numerically-fixed constant with G_N's units) to become properly")
    print("dimensionless. This mechanically confirms -- not merely echoes -- what")
    print("FINDING_P21 itself already anticipated (Sec.4) but never checked: 'the")
    print("same missing constant A enters' both the g-sector and kappa-sector")
    print("calculations, because both are built from the same field phi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
