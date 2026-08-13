"""P27_unify_normalization_constant.py -- user-redirected priority: close
the A/kappa normalization gap before attempting any frozen external
prediction. Question: are the "missing normalization constant" gaps
flagged separately across FINDING_P14 Sec.6, FINDING_P17, FINDING_P21,
FINDING_P22, FINDING_P26 actually SEPARATE unknowns, or all the SAME one?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive

HONEST SCOPE, stated up front: dimensional analysis alone can NEVER
produce a number -- only units and structural relationships between
constants. This script does not, and cannot, fix kappa or A's numeric
value. What it CAN do, and does: determine whether the several
"undetermined normalization constant" gaps flagged in five separate
findings across this project are the SAME single unknown or genuinely
independent ones, and derive the exact formula connecting that unknown
to every downstream quantity (E_self, rho_phi, Omega_phi) for the first
time.

METHOD: (1) make the action's kinetic-term prefactor C explicit (it has
always been implicitly =1 in every prior finding) and derive its
required units from action-level dimensional consistency (M,L,T exponent
bookkeeping, sympy). (2) Re-derive the field equation from the
Euler-Lagrange equations WITH C explicit, and show the resulting
Green's-function solution equals phi_raw/C. (3) Show this is EXACTLY
FINDING_P21's own phi_true=A*phi_raw convention when A=1/C -- an
independent cross-validation of P21 from action-level first principles,
not a repeat of P21's own force-matching retrofit. (4) Derive
E_self,physical = A * E_self,correct (P26's formula) and verify by two
independent routes that this has units of energy.
"""

from __future__ import annotations

import sympy as sp


def dim(mass=0, length=0, time=0):
    return sp.Matrix([mass, length, time])


def main() -> int:
    print("=" * 78)
    print("P27 -- unifying the normalization gap: one constant, not several")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    energy_dim = dim(1, 2, -2)
    action_dim = dim(1, 2, -1)
    mass_dim = dim(1, 0, 0)
    length_dim = dim(0, 1, 0)
    time_dim = dim(0, 0, 1)

    print("\n[STEP 1] Make the action's kinetic-term prefactor C explicit --")
    print("  every prior finding (P9-P26) used it implicitly =1. Action:")
    print(
        "  S = int d^4x (C/2)(d phi)^2 + sum_i int dtau [g*m_i + kappa*(k_i r_i/c^2).grad] phi(x_i)"
    )

    # kappa dimensionless -- established project convention, kept (not re-litigated)
    g_dim = dim(0, 0, 0)  # established project convention (P21), kept
    p_dim = dim(1, 1, 0)  # established: kg*m

    print("\n[STEP 2] Required [phi] from BOTH couplings -- reproduces P21 exactly")
    phi_from_monopole = sp.Matrix(energy_dim) - g_dim - mass_dim
    phi_from_dipole = sp.Matrix(energy_dim) - p_dim + length_dim
    print(f"  [phi]_monopole = {list(phi_from_monopole)}")
    print(f"  [phi]_dipole   = {list(phi_from_dipole)}")
    match = phi_from_monopole == phi_from_dipole
    print(f"  match (P21's own result): {match}")
    if not match:
        print("  STOP")
        return 1
    phi_dim = phi_from_monopole

    print("\n[STEP 3] Required [C] from action-level dimensional consistency")
    print("  (C/2)(grad phi)^2 integrated d^4x must equal ACTION, not just energy*volume.")
    grad_phi_dim = phi_dim - length_dim
    d4x_dim = 3 * length_dim + time_dim
    c_dim = sp.Matrix(action_dim) - 2 * grad_phi_dim - d4x_dim
    g_newton_dim = dim(-1, 3, -2)
    print(f"  [C] = {list(c_dim)}")
    print(f"  [1/G] = {list(-g_newton_dim)}")
    c_is_inv_g = c_dim == -g_newton_dim
    print(f"  C carries units of 1/G: {c_is_inv_g}")
    if not c_is_inv_g:
        print("  STOP")
        return 1

    print("\n[STEP 4] Re-derive the field equation from Euler-Lagrange WITH C explicit")
    print("  (monopole term, static limit; same argument applies to the dipole term):")
    print("  delta S/delta phi(x) = -C*laplacian(phi) + g*m*delta^3(x) = 0")
    print("  =>  laplacian(phi) = (g*m/C) * delta^3(x)")
    print("  =>  phi(x) = (g*m/C) * G(x),  G(x)=-1/(4*pi*r)  [P19's own Green's function]")
    print("  Compare to phi_raw (P9-P20's OWN convention, C implicitly =1):")
    print("     phi_raw(x) = g*m*G(x)")
    print("  =>  phi_properly_normalized(x) = phi_raw(x) / C")

    print("\n[STEP 5] Does 1/C match FINDING_P21's own A (phi_true = A*phi_raw)?")
    a_dim = dim(-1, 3, -2)  # established, P21
    inv_c_dim = -c_dim
    a_matches_inv_c = a_dim == inv_c_dim
    print(f"  [A] (P21, established)  = {list(a_dim)}")
    print(f"  [1/C] (this derivation) = {list(inv_c_dim)}")
    print(f"  A == 1/C (units):        {a_matches_inv_c}")
    if not a_matches_inv_c:
        print("  STOP -- P21's own A and this derivation's C are NOT reciprocal,")
        print("  the unification claim below would be wrong.")
        return 1
    print("  -> A = 1/C reproduces P21's phi_true=A*phi_raw EXACTLY, from an")
    print("     independent starting point (action-level dimensional")
    print("     consistency + Euler-Lagrange), not P21's own force-matching")
    print("     retrofit. This is a genuine cross-validation of P21, not a repeat.")

    print("\n[STEP 6] CONCLUSION: every 'missing normalization constant' flagged")
    print("  since P14 Sec.6 (P14 Sec.6, P17, P21, P22, P26) is the SAME single")
    print("  unknown, A -- not several independent gaps.")

    print("\n[STEP 7] Derive E_self,physical -- verify by TWO independent routes")
    e_self_p26_dim = dim(2, -1, 0)  # P26's E_self,correct, kg^2/m (established)
    route1 = a_dim + e_self_p26_dim
    print(f"  Route 1: A * E_self,correct(P26)     -> {list(route1)}")

    phi_true_dim = phi_dim
    grad_phi_true_dim = phi_true_dim - length_dim
    integral_dim = 2 * grad_phi_true_dim + 3 * length_dim
    route2 = c_dim + integral_dim
    print(f"  Route 2: C * integral(grad phi_true)^2 dV -> {list(route2)}")

    both_energy = route1 == sp.Matrix(energy_dim) and route2 == sp.Matrix(energy_dim)
    routes_agree = route1 == route2
    print(f"  Both routes give ENERGY units: {both_energy}")
    print(f"  Both routes AGREE with each other: {routes_agree}")
    if not (both_energy and routes_agree):
        print("  STOP")
        return 1

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (structural, sympy-verified, cross-validated by two")
    print("independent routes): E_self,physical = A * E_self,correct(P26) =")
    print("A * p^2/(12*pi*r_min^3) -- NOW dimensionally a genuine energy, for")
    print("the first time in this project. rho_phi = n*E_self,physical and")
    print("Omega_phi = rho_phi/rho_crit are NOW dimensionally well-posed")
    print("(a true dimensionless number), ONCE A's numeric value is known.")
    print()
    print("HONEST LIMIT, stated up front and unchanged by this finding:")
    print("dimensional analysis alone NEVER produces a number. A's numeric")
    print("value remains exactly as unknown as before -- only P22's own")
    print("A*g^2 <~ 1.05e-10 (SI) soft ceiling exists, bounding a PRODUCT, not")
    print("A alone. Extracting a number for A (hence for Omega_phi) still")
    print("requires an independent estimate of g, or of kappa, from outside")
    print("this project's own internal derivations -- not attempted here.")
    print("What this finding closes is the STRUCTURAL question: how many")
    print("independent unknowns are there (answer: one, A) and exactly how")
    print("does it enter every downstream quantity (now an explicit formula,")
    print("not several disconnected 'missing constant' flags).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
