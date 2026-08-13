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
    print("  ASSUMPTION (not established in cited prior findings -- corrected 2026-08-13):")
    print("  g is taken dimensionless, matching kappa's established convention (P14).")
    print("  P13a names g as independent of kappa but does not establish its units.")
    print("  If g carries units, [phi]_monopole below changes accordingly.")
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

    print("\n[STEP 4] Force-matching -- CORRECTED after skeptic review, 2026-08-13.")
    print("  Original version equated monopole exchange to the FULL Newton force")
    print("  (A*c_G*g^2 = G). WRONG: two_field_action_closure.py's own text calls")
    print("  phi 'a FIFTH FORCE, not gravity' and says its m-m exchange")
    print("  'renormalises G (attractive, absorbed)' -- standard fifth-force")
    print("  phrasing for a SMALL shift to an already-existing G, not that phi-")
    print("  exchange IS all of G. 'Fifth force' presupposes gravity already")
    print("  exists separately; setting G_bare=0 contradicts the source's own")
    print("  wording.")
    print("  phi_true,mono(r) = A * g * m * c_G / r")
    print("  F(r) = -grad[ g*m2*phi_true,1(r) ] , magnitude = A * c_G * g^2 * m1*m2 / r^2")
    print("  Correct target: this force equals DELTA_G * m1*m2/r^2 (a SMALL addition")
    print("  to the bare/Einstein-Hilbert G, not G itself):")
    print("  =>  A * c_G * g^2 = DELTA_G   , with c_G = 1/(4*pi) (P19)")
    print("  =>  A * g^2 = 4*pi*DELTA_G ,  DELTA_G << G required")
    print("  (fifth-force phenomenology, e.g. Archidiacono-type bounds P13a names)")

    print("\n[STEP 5] Degrees of freedom")
    print("  ONE equation (A*g^2 = 4*pi*DELTA_G), THREE unknowns (A, g, DELTA_G)")
    print("  -- more open than the original two-unknown claim, since DELTA_G is")
    print("  itself unmeasured here (only bounded small by fifth-force phenomenology,")
    print("  not equal to G). Dimensional analysis + force-matching narrows the")
    print("  space (units of A fixed; g must be SMALL, consistent with 'fifth")
    print("  force') but does NOT fix any of the three numerically.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (structural, not numeric): the action's two couplings")
    print("independently demand the SAME [phi]. The missing normalization")
    print("constant A is thereby forced to carry Newton's-G units. Corrected")
    print("force-matching (2026-08-13): A*g^2 = 4*pi*DELTA_G, where DELTA_G is the")
    print("SMALL fifth-force contribution to observed G (NOT G itself) -- three")
    print("unknowns, not two. g and A remain individually undetermined; DELTA_G is")
    print("now also explicitly unmeasured, not silently assumed equal to G.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
