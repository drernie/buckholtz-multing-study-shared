"""P21_shared_phi_normalization_constraint.py -- does the action's OWN
requirement that a single scalar phi carries BOTH the monopole coupling
(g*m*phi) and the dipole coupling (p.grad(phi)) pin down anything about
the missing dimensional normalization constant P14/P17/P19 left open?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive

CONTEXT: P17 found Omega_phi (built from P14's formula) has units kg/m,
not dimensionless -- a missing dimensional constant, separate from P19's
already-derived geometric 1/(4*pi) Green's-function normalization. This
script asks: does demanding phi be simultaneously consistent for BOTH of
P1's own coupling terms (g*m*phi and p.grad(phi), same field, same
kinetic term) constrain that missing constant's UNITS and give a
structural equation relating it to the monopole coupling g?

METHOD: pure dimensional/structural analysis via symbolic (M,L,T)
exponent bookkeeping (sympy), not a numeric fit. Positive control:
reproduce that a canonical scalar kinetic term (1/2)(d phi)^2 already
fixes what units energy-coupling terms must carry, cross-checked against
each of P1's TWO couplings independently, then checked for internal
consistency (do they demand the SAME [phi]?).
"""

from __future__ import annotations

import sympy as sp

M, L, T = sp.symbols("M L T")  # exponents of kg, m, s


def dim(mass=0, length=0, time=0):
    return sp.Matrix([mass, length, time])


def show(name, exponents):
    m, ln, t = exponents
    print(f"  [{name}] = kg^{m} * m^{ln} * s^{t}")


def main() -> int:
    print("=" * 78)
    print("P21 -- shared-phi normalization constraint from P1's two couplings")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    energy = dim(1, 2, -2)  # kg m^2 s^-2
    mass = dim(1, 0, 0)
    length = dim(0, 1, 0)
    p_dipole = dim(1, 1, 0)  # kg*m, established in FINDING_P14 (kappa dimensionless)

    print("\n[STEP 1] Required [phi] from EACH coupling independently")
    print("  (a) monopole: g*m*phi = energy  =>  [phi] = [energy]-[mass]  (g dimensionless)")
    phi_from_monopole = energy - mass
    show("phi]_monopole", phi_from_monopole)

    print("  (b) dipole:   p.grad(phi) = energy  =>  [phi] = [energy]-[p]+[length]")
    phi_from_dipole = energy - p_dipole + length
    show("phi]_dipole", phi_from_dipole)

    match = phi_from_monopole == phi_from_dipole
    print(f"\n  -> SAME requirement from both couplings: {match}")
    if not match:
        print("  STOP -- action is not even internally dimensionally consistent.")
        return 1

    phi_true_dim = phi_from_monopole
    print(
        f"  => phi must carry [phi] = kg^{phi_true_dim[0]} m^{phi_true_dim[1]} s^{phi_true_dim[2]}"
        f"  (m^2/s^2)"
    )

    print("\n[STEP 2] Units of phi as computed 'raw' throughout P9-P20")
    print("  (Green's function G(x)=-c_G/r solves grad^2 G=delta^3(x); P19 derived")
    print("  c_G=1/(4*pi) -- a pure number, contributes no units.)")
    print("  phi_raw,mono(r) = g * m * c_G / r   (g dimensionless, c_G dimensionless)")
    phi_raw_dim = mass - length
    show("phi_raw]_monopole", phi_raw_dim)

    print("\n[STEP 3] Missing constant A := phi_true / phi_raw -- solve for its units")
    a_dim = phi_true_dim - phi_raw_dim
    show("A", a_dim)
    g_si_dim = dim(-1, 3, -2)  # m^3 kg^-1 s^-2, Newton's G
    print(f"  Newton's G units:      kg^{g_si_dim[0]} m^{g_si_dim[1]} s^{g_si_dim[2]}")
    print(f"  A units == G units: {a_dim == g_si_dim}")
    if a_dim != g_si_dim:
        print("  STOP -- A does not carry G's units; the 'renormalises G' reading fails.")
        return 1

    print("\n[STEP 4] Force-matching -- monopole exchange must reproduce Newton's law")
    print("  (per P1's own text: the g-sector 'renormalises G, absorbed')")
    print("  phi_true,mono(r) = A * g * m * c_G / r")
    print("  F(r) = -grad[ g*m2*phi_true,1(r) ] , magnitude = A * c_G * g^2 * m1*m2 / r^2")
    print("  Newton:  F(r) = G * m1*m2 / r^2")
    print("  =>  A * c_G * g^2 = G   , with c_G = 1/(4*pi) (P19)")
    print("  =>  A * g^2 = 4*pi*G")

    print("\n[STEP 5] Degrees of freedom")
    print("  1 equation (A*g^2 = 4*pi*G), 2 unknowns (A, g).")
    print("  Dimensional analysis + force-matching narrows the space but does NOT")
    print("  by itself fix either A or g numerically -- a genuinely independent")
    print("  second constraint is required.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (structural, not numeric): the action's two couplings")
    print("independently demand the SAME [phi] (internal consistency, not assumed).")
    print("The missing normalization constant A is thereby FORCED to carry exactly")
    print("Newton's-G units, and satisfies A*g^2 = 4*pi*G via the monopole/gravity")
    print("self-consistency P1's own text asserts qualitatively. This is a genuine")
    print("narrowing (units + one equation), not a numeric fix -- g and A remain")
    print("individually undetermined without a second, independent input.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
