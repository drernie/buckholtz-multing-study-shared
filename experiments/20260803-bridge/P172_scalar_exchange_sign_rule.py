"""P172 -- CORRECTION (2026-08-31, skeptic-caught): this script's own
original docstring and FINDING_P172 both overclaimed this as an
"independent verification." Re-examined: given a bilinear linear
coupling U ~ q1*q2, flipping one charge's sign mechanically flips U's
sign once the convention is calibrated to match a known fact -- this is
a correct, real algebraic consistency check, but a near-tautological
consequence of the bilinear-coupling ansatz, not an independent
physical derivation of the opposite-branch-repulsion claim. Relabeled
accordingly; kept because the check is still real and not vacuous (it
confirms the repulsion claim needs no assumption beyond ordinary linear
scalar coupling), but it does not prove anything the calibration step
did not already assume.

Confirms the scalar-exchange sign rule cited in FINDING_P172: for a
canonically-normalized (ghost-free) massless scalar field linearly
coupled to a point "charge," same-sign charges attract and opposite-
sign charges repel, once the overall coupling convention is calibrated
against this project's own already-established fact (FINDING_P162/
docs/130: "stable scalar-scalar exchange is attractive" for same-sign/
same-composition sources -- i.e. ordinary positive-energy matter
behaves like ordinary attractive gravity under scalar exchange).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sympy as sp

r = sp.Symbol("r", positive=True)
q = sp.Symbol("q", positive=True)


def _phi_sourced_by(charge, coupling_sign):
    """Static, spherically symmetric Green's-function solution of the
    canonical (ghost-free) massless Klein-Gordon equation, box(phi) =
    coupling_sign * charge * delta^3(x), i.e. phi(r) = coupling_sign *
    charge / (4*pi*r).
    """
    return coupling_sign * charge / (4 * sp.pi * r)


def interaction_energy(q1, q2, coupling_sign):
    """U(r) = q2 * phi_1(r) -- the interaction energy of a second charge
    sitting in the field sourced by the first, for the SAME linear
    coupling L_int = coupling_sign * q * phi on both ends (a single
    theory, evaluated symmetrically)."""
    phi1 = _phi_sourced_by(q1, coupling_sign)
    return q2 * phi1


def test_calibration_matches_docs130_same_sign_attractive():
    """docs/130's own already-established fact: same-sign (same
    composition, ordinary positive-energy) scalar exchange is
    ATTRACTIVE, matching ordinary gravity's own sign. An attractive
    1/r potential is NEGATIVE (bound state convention, U->0 as r->inf,
    U<0 at finite r -- same convention as U=-Gm1m2/r for Newtonian
    gravity). Only ONE of the two possible coupling-sign conventions
    (L_int = +q*phi or L_int = -q*phi) reproduces this; calibrate to
    it rather than assume.
    """
    u_plus = sp.simplify(interaction_energy(q, q, +1))
    u_minus = sp.simplify(interaction_energy(q, q, -1))
    # same-sign charges (q,q): exactly one convention gives U<0
    assert u_plus.subs(r, 1) > 0
    assert u_minus.subs(r, 1) < 0
    return -1  # the calibrated coupling_sign matching docs/130's own fact


def test_opposite_sign_charges_are_repulsive_under_calibrated_convention():
    """With the coupling sign calibrated in the test above (same-sign
    attractive, matching docs/130), opposite-sign charges must give
    U>0 (repulsive) -- this is the claim FINDING_P172 relies on for
    the scalarization opposite-branch mechanism.
    """
    coupling_sign = test_calibration_matches_docs130_same_sign_attractive()
    u_same = sp.simplify(interaction_energy(q, q, coupling_sign))
    u_opposite = sp.simplify(interaction_energy(q, -q, coupling_sign))
    assert u_same.subs(r, 1) < 0  # attractive, matches docs/130
    assert u_opposite.subs(r, 1) > 0  # repulsive
    return u_same, u_opposite


if __name__ == "__main__":
    coupling_sign = test_calibration_matches_docs130_same_sign_attractive()
    print(
        f"Calibrated coupling sign (matching docs/130's same-sign-attractive fact): {coupling_sign:+d}"
    )

    u_same, u_opposite = test_opposite_sign_charges_are_repulsive_under_calibrated_convention()
    print(f"\nU_same(r)     = {u_same}   [negative for all r>0 -> ATTRACTIVE, matches docs/130]")
    print(f"U_opposite(r) = {u_opposite}   [positive for all r>0 -> REPULSIVE]")
    print(
        "\nConclusion: under the SAME bilinear (U~q1*q2) linear scalar coupling that "
        "reproduces docs/130's own established same-sign-attractive fact, opposite-sign "
        "scalar charges mechanically give a repulsive interaction. This is a real, "
        "correctly-executed consistency check -- but a near-tautological algebraic "
        "consequence of the bilinear-coupling ansatz once calibrated, not an independent "
        "physical derivation (see FINDING_P172's own Correction section)."
    )
