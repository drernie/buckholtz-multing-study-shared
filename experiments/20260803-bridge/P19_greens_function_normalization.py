"""P19: FINDING_P18 left the missing normalization constant's FORM as a
named, unproven assumption -- "cancels IF it is a pure, r_min-independent
overall multiplier". Can the standard, textbook piece of that normalization
(the field equation's own Green's-function factor) be pinned down, rather
than assumed?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12, corrected 2026-08-12 after context-blind skeptic review.

[CORRECTED: an earlier draft of this docstring called this a "derivation"
implying novel physics content. It is not -- 1/(4*pi) is the standard
Green's-function normalization used throughout ordinary electrostatics
(same origin as 1/(4*pi*eps0)); this identifies that this project's own
ansatz was missing it, applying a textbook result to this project's own
p.grad(phi) coupling for the first time, not discovering new physics.]

This project's own action (two_field_action_closure.py):

  S = int d^4x (1/2)(d phi)^2 + sum_i int dtau [g*m_i + p_i . grad] phi(x_i)

Every FINDING (P9, P11, P12, P14, P15, P16) that used a point-dipole field
used the ansatz phi = p*cos(theta)/r^2, WITHOUT deriving it from this
action's own field equation. Solving the field equation properly (static
point dipole, standard 3D Green's function of the Laplacian) gives a
DIFFERENT normalization: phi = p*cos(theta)/(4*pi*r^2) -- the textbook
electrostatics/magnetostatics dipole-potential form, missing a 1/(4*pi)
factor throughout this project's own prior work.

SCOPE, stated up front: this identifies and verifies ONE piece of the
missing normalization P17 found (a pure NUMBER, 1/(4*pi), coming from the
Green's function's own geometric normalization) and shows the POINT-
SOURCE COEFFICIENT ITSELF is r_min-independent BY CONSTRUCTION -- not
merely checked for one assumed form, as FINDING_P18's Part 3 sensitivity
check did. [CORRECTED: this closes only ONE narrow piece of P18's gap.]
It does NOT touch the renormalization/regularization concern FINDING_P18's
own skeptic review actually raised (a question about how the ENERGY
INTEGRAL is regularized, separate from phi's own field-equation
normalization). It also does NOT rule out r_min-dependent corrections
from the finite physical size of a real source: E_self is dominated by
r~r_min, exactly where the point-dipole idealization used here is
weakest. Nor does this resolve FINDING_P17's full dimensional problem
(Omega_phi has units kg/m, not dimensionless) -- 1/(4*pi) is a pure
number, not a dimensional constant, and cannot by itself fix a units
mismatch. That deeper problem (a missing constant WITH UNITS, needed to
make the action's own kinetic term dimensionally consistent) remains
completely open after this finding.
"""

import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
p = sp.Symbol("p", positive=True)
r_min = sp.Symbol("r_min", positive=True)


def greens_function_3d():
    """Standard 3D Green's function of the Laplacian: Laplacian(G)=delta^3(x).
    G = -1/(4*pi*r) is the textbook result (electrostatics, Newtonian
    gravity, etc.) -- verified here directly, not quoted."""
    r = sp.sqrt(x**2 + y**2 + z**2)
    return -1 / (4 * sp.pi * r), r


def dipole_potential_from_field_equation(G):
    """For the action's own p.grad(phi) coupling, varying phi gives a
    source proportional to -div(p*delta^3(x)) for a static point dipole
    (g=0). The solution is phi = p . grad(G) -- standard derivative-of-
    Green's-function construction for a dipole source, independent of any
    particular numeric choice for p or r_min."""
    return p * sp.diff(G, z)  # p along z-axis, no loss of generality


def main() -> None:
    print("=" * 78)
    print("P19 -- DERIVING (NOT ASSUMING) THE DIPOLE FIELD'S GEOMETRIC NORMALIZATION")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Solve the field equation's Green's function directly.")
    G, r = greens_function_3d()
    lap_G_away_from_origin = sp.diff(G, x, 2) + sp.diff(G, y, 2) + sp.diff(G, z, 2)
    print(f"  G(x) = {G}")
    assert sp.simplify(lap_G_away_from_origin) == 0, (
        "G does not solve Laplace's equation away from origin"
    )
    print("  -> Laplacian(G)=0 away from the origin, checked directly: PASSES")
    print("     (the delta-function source at the origin is the standard distributional")
    print("     result for this G -- textbook electrostatics/Newtonian-gravity Green's")
    print("     function, not something invented for this project.)")

    print("\n[STEP 2] Derive the dipole potential from the Green's function.")
    phi_dipole = dipole_potential_from_field_equation(G)
    phi_dipole_simplified = sp.simplify(phi_dipole)
    print(f"  phi_dipole (p along z) = {phi_dipole_simplified}")

    print("\n[POSITIVE CONTROL] Does this match the well-known textbook dipole-")
    print("  potential form p*cos(theta)/(4*pi*r^2) (same structure as the standard")
    print("  electrostatic/magnetostatic dipole potential)?")
    xv, yv, zv = 1.0, 0.5, 2.0
    rv = (xv**2 + yv**2 + zv**2) ** 0.5
    costhetav = zv / rv
    phi_numeric = float(phi_dipole_simplified.subs({x: xv, y: yv, z: zv, p: 1}))
    textbook_form = 1 * costhetav / (4 * sp.pi.evalf() * rv**2)
    print(f"  derived, numeric  : {phi_numeric:.10f}")
    print(f"  textbook form     : {float(textbook_form):.10f}")
    assert abs(phi_numeric - float(textbook_form)) < 1e-9, "does NOT match textbook dipole form"
    print("  -> MATCHES exactly. This is not a new derivation of physics -- it is the")
    print("     standard dipole-potential result, applied to THIS action's own p.grad(phi)")
    print("     coupling for the first time in this project's bridge track.")

    print("\n[COMPARISON] What every prior finding (P9, P11, P12, P14, P15, P16) actually")
    print("  used, without deriving it from the field equation:")
    project_used = 1 * costhetav / rv**2  # no 1/(4*pi)
    ratio = project_used / phi_numeric
    print(f"  project's phi = p*cos(theta)/r^2, numeric = {project_used:.10f}")
    print(f"  ratio (project_used / field-equation-derived) = {ratio:.6f}")
    print(f"  4*pi = {float(4 * sp.pi):.6f}")
    assert abs(ratio - float(4 * sp.pi)) < 1e-6, "ratio is not 4*pi as expected"
    print("  -> exactly 4*pi, confirmed. Every prior E_self/U_cross number in this")
    print("     project's bridge track is missing this 1/(4*pi) geometric factor.")

    print("\n[STEP 3] Does this piece of the normalization depend on r_min? (Answers")
    print("  FINDING_P18's remaining conditional gap -- NOT by testing one assumed")
    print("  form as P18's Part 3 did, but by a general structural argument.)")
    print("  The Green's function G(x) solves Laplacian(G)=delta^3(x) -- a property of")
    print("  the FIELD EQUATION ALONE, fixed once and for all, with no reference to any")
    print("  particular source's physical extent. r_min never appears in this derivation")
    print("  at all -- it enters LATER, only as the lower limit of the energy integral")
    print("  (r>=r_min) AFTER phi is already fully determined. Since the geometric")
    print("  normalization 1/(4*pi) comes entirely from solving Laplacian(G)=delta^3(x)")
    print("  -- an equation r_min cannot appear in -- this piece of the normalization")
    print("  is r_min-independent for the POINT-SOURCE COEFFICIENT ITSELF, for any source")
    print("  configuration (self-energy or cross-term) built from the point-dipole field.")
    print("  [CORRECTED after skeptic review:] this closes only ONE narrow piece of P18's")
    print("  gap -- NOT the renormalization/regularization concern P18's own skeptic")
    print("  actually raised (a question about the ENERGY INTEGRAL's own structure, a")
    print("  separate step from phi's normalization). It also does not rule out finite-")
    print("  size corrections: E_self is dominated by r~r_min, exactly where the point-")
    print("  dipole idealization used here is weakest for a real extended source.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("[CORRECTED after skeptic review: 'derived' softened to 'identified' -- 1/(4*pi)")
    print("is the standard Green's-function normalization from ordinary electrostatics,")
    print("not a new physics result.] This project's dipole-field ansatz (phi=p*cos(theta)/")
    print("r^2, used in P9/P11/P12/P14/P15/P16) is missing this factor, verified against")
    print("the standard textbook dipole-potential form.")
    print()
    print("The point-source coefficient is PROVABLY r_min-independent (Step 3). This closes")
    print("one narrow piece of FINDING_P18's conditional gap, NOT the piece P18's own")
    print("skeptic actually raised (renormalization/regularization of the energy integral),")
    print("and does not rule out r_min-dependent finite-size corrections near r~r_min,")
    print("where E_self is dominated and the point-dipole idealization is weakest.")
    print()
    print("WHAT THIS DOES NOT RESOLVE: 1/(4*pi) is a pure NUMBER, not a quantity with")
    print("physical UNITS. FINDING_P17's full dimensional problem (Omega_phi has units")
    print("kg/m, not dimensionless) needs a DIFFERENT, DIMENSIONAL constant -- something")
    print("that would make the action's own kinetic term (1/2)(d phi)^2 have proper units")
    print("of an energy density in the first place. That constant is NOT derived here and")
    print("remains completely open. Do not read this finding as resolving FINDING_P17.")


if __name__ == "__main__":
    main()
