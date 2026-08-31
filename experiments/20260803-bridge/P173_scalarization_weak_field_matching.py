"""P173 -- weak-field matching calculation for FINDING_P172's own named
next step: does a scalarization-type "k_A redefinition" completion
reproduce MULTING's own F^(1) dipole term's radial form (1/s^3, per
P161_v82_beta_identifiability.py's own f1 = -G*beta1*2*k_x*m_x*r_x/s**3)
and sign?

Two candidate constructions, both built from the SAME calibrated linear
scalar coupling convention as P172_scalar_exchange_sign_rule.py (same-
sign charges attract, matching FINDING_P162/docs/130's own established
fact):

  Case 1 -- SIMPLE isotropic scalarization charge (P172's own literal
  proposal): both nodes couple via an ordinary monopole coupling
  L_int = q*phi, q = q(k) a function of thermal energy. Standard
  monopole-monopole scalar exchange.

  Case 2 -- MONOPOLE-DIPOLE: one node (P) sources an ordinary monopole
  field via its mass (q_P ~ m_P, matching v82's own F^(0) Newtonian
  monopole); the OTHER node (A) couples via the FIELD GRADIENT rather
  than the field value (L_int = p_A . grad(phi)), with p_A = f(k_A) *
  n_hat -- magnitude from A's own thermal energy, direction supplied
  EXTERNALLY by the separation vector. This external-axis structure is
  not invented for this file -- it is v82's own explicit claim, quoted
  in FINDING_P162 Sec.3: "a node's own thermal energy has no intrinsic
  axis... the line connecting the two nodes... supplies the direction,
  with a node's thermal energy setting only the magnitude."

ADJUDICATION NOTE (2026-08-31): a context-blind skeptic review flagged
Case 2's sign (u = -p_A*dphi_ds) as backward, claiming the correct sign
was repulsive. Independently re-derived four separate ways (direct
point-charge limit, charge-density/Green's-function convolution,
recalibrated textbook point-dipole formula, and a second, independently
-briefed skeptic agent working from scratch) -- all four confirm THIS
FILE'S ORIGINAL SIGN WAS CORRECT (attractive). The reviewing skeptic's
own derivation conflated d(phi)/ds (s = distance from the source,
outward direction) with the properly-oriented spatial gradient dotted
into p_A's own direction (toward the source) -- these differ by exactly
one sign. See FINDING_P173.md's own "Adjudication note" for the full
account. No code change was needed; this note documents that the
disagreement was investigated and resolved in the code's favor, not
silently ignored.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sympy as sp

s = sp.Symbol("s", positive=True)
q_A, q_P, p_A = sp.symbols("q_A q_P p_A", positive=True)


def phi_sourced_by(charge, r):
    """Static Green's-function solution, calibrated (per P172's own
    script) so that SAME-sign charges give an ATTRACTIVE monopole-
    monopole force, matching docs/130's own established fact."""
    return -charge / (4 * sp.pi * r)


def case1_monopole_monopole():
    """Simple isotropic scalarization charge on both nodes."""
    phi_p = phi_sourced_by(q_P, s)
    u = q_A * phi_p
    f = -sp.diff(u, s)
    return sp.simplify(u), sp.simplify(f)


def case2_monopole_dipole():
    """Node P: ordinary monopole charge q_P (~ m_P). Node A: effective
    dipole p_A = f(k_A)*n_hat, coupled via the field GRADIENT."""
    phi_p = phi_sourced_by(q_P, s)
    dphi_ds = sp.diff(phi_p, s)
    u = -p_A * dphi_ds
    f = -sp.diff(u, s)
    return sp.simplify(u), sp.simplify(f)


def test_case1_matches_docs130_calibration():
    """Positive control: same-sign charges (q_A=q_P=+) must be
    attractive (U<0), matching docs/130's own established fact --
    confirms this file's calibration is consistent with P172's own
    already-verified convention before trusting anything derived from
    it.
    """
    u, _ = case1_monopole_monopole()
    assert u.subs(s, 1) < 0


def test_case1_radial_power_is_inverse_square_not_inverse_cube():
    """Case 1 (simple scalarization charge) must give F ~ 1/s^2 -- the
    ordinary monopole-monopole (Coulomb/Yukawa-type) radial dependence
    -- NOT MULTING's own 1/s^3 dipole form. Checked by confirming
    F(s)*s^2 is independent of s (a pure constant).
    """
    _, f = case1_monopole_monopole()
    scaled = sp.simplify(f * s**2)
    assert scaled.free_symbols.isdisjoint({s})
    # and NOT s^3-independent (i.e. genuinely NOT 1/s^3)
    scaled_wrong_power = sp.simplify(f * s**3)
    assert s in scaled_wrong_power.free_symbols


def test_case2_radial_power_is_inverse_cube_matching_multing():
    """Case 2 (monopole-dipole, external-axis construction) must give
    F ~ 1/s^3, matching MULTING's own F^(1) radial form
    (P161_v82_beta_identifiability.py: f1 ~ k_x*m_x*r_x/s**3).
    """
    _, f = case2_monopole_dipole()
    scaled = sp.simplify(f * s**3)
    assert scaled.free_symbols.isdisjoint({s})


def test_case2_sign_is_attractive_for_ordinary_positive_quantities():
    """The decisive check: with BOTH p_A=f(k_A)>0 (ordinary positive
    thermal energy) and q_P>0 (ordinary positive mass, same convention
    as docs/130's own attractive monopole gravity), is Case 2's force
    attractive or repulsive? MULTING needs REPULSIVE for this
    construction to work.
    """
    _, f = case2_monopole_dipole()
    # F = -dU/ds; convention (verified in test_case1_matches_docs130_
    # calibration and P172's own script): negative F = attractive.
    return f.subs(s, 1) < 0  # True if attractive (i.e. NOT what MULTING needs)


if __name__ == "__main__":
    test_case1_matches_docs130_calibration()
    print(
        "Positive control: Case 1 calibration matches docs/130's own attractive-same-sign fact: PASS"
    )

    u1, f1 = case1_monopole_monopole()
    print("\n=== Case 1: simple scalarization charge (monopole-monopole) ===")
    print(f"U(s) = {u1}")
    print(f"F(s) = {f1}")
    test_case1_radial_power_is_inverse_square_not_inverse_cube()
    print(
        "Radial power check: F ~ 1/s^2 (NOT 1/s^3) -- CONFIRMED, radial-power MISMATCH with MULTING's own F^(1)"
    )

    u2, f2 = case2_monopole_dipole()
    print(
        "\n=== Case 2: monopole (node P, ~m_P) - dipole (node A, p_A=f(k_A)*n_hat, external axis) ==="
    )
    print(f"U(s) = {u2}")
    print(f"F(s) = {f2}")
    test_case2_radial_power_is_inverse_cube_matching_multing()
    print("Radial power check: F ~ 1/s^3 -- CONFIRMED, MATCHES MULTING's own F^(1) radial form")

    is_attractive = test_case2_sign_is_attractive_for_ordinary_positive_quantities()
    print(
        f"\nSign check (p_A>0, q_P>0, ordinary positive quantities): "
        f"{'ATTRACTIVE' if is_attractive else 'REPULSIVE'}"
    )
    print("MULTING's own F^(1) needs REPULSIVE for this construction to work.")
    print(
        "\n=== Conclusion ===\n"
        "Case 1 (P172's own literal 'scalarization charge' proposal) fails on RADIAL\n"
        "POWER alone (1/s^2 != 1/s^3) -- independent of any sign question.\n"
        "Case 2 (the construction that DOES fix the radial power, via an effective\n"
        "dipole with externally-supplied axis) reproduces MULTING's own F^(1) power\n"
        "exactly, but is ATTRACTIVE for ordinary positive quantities -- the SAME\n"
        "positive-energy sign obstruction docs/131's own CANDIDATE-L1 already found,\n"
        "not a new escape route. Structurally, Case 2's own 'effective dipole with\n"
        "external axis, magnitude from internal energy' IS docs/131's own vector-\n"
        "type internal-dipole medium, arrived at independently here from a\n"
        "scalarization starting point."
    )
