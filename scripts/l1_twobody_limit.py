"""l1_twobody_limit.py — CANDIDATE-L1 step 1: can standard local dipole gravity give
MULTING's central static 1/r^3 force? (the central-vs-angular kill-test, docs/130)

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

MULTING's dipole term (preprint Eqs. 14-15) is a STATIC, CENTRAL (radial) 1/r^3 force
whose magnitude ∝ k_A · m_B — i.e. the "dipole charge" of A is a FIXED property of A
alone (∝ internal kinetic energy k_A), independent of B and of r. This script checks,
symbolically, whether the two standard local mechanisms for a gravitational dipole
reproduce that structure:

  (P) PERMANENT vector dipole p_A (fixed magnitude, fixed orientation)
  (I) INDUCED dipole p_A = α_A g_A (polarization, always radial)

The MULTING requirement is the CONJUNCTION: fixed magnitude (like P) AND always radial
(like I) AND 1/r^3 force AND repulsive-capable. The test asks whether any single
standard mechanism supplies all of these without a preferred direction / fine-tuning.

Run:  python scripts/l1_twobody_limit.py
Exit: 0 (report). The scientific verdict (skeptic-reviewed) is in docs/130.
"""

from __future__ import annotations

import sympy as sp


def main() -> int:
    G, mB, r, theta, pA, alpha = sp.symbols("G m_B r theta p_A alpha", positive=True)

    print("=" * 70)
    print("CANDIDATE-L1 step 1 — 2-body limit of standard gravitational dipoles")
    print("=" * 70)

    # (P) PERMANENT dipole p_A at angle theta to the separation r_hat.
    # monopole(B)-dipole(A) interaction energy U = -G m_B (p_A . r_hat)/r^2
    U_perm = -G * mB * pA * sp.cos(theta) / r**2
    Fr_perm = sp.simplify(-sp.diff(U_perm, r))  # radial force
    print("\n(P) PERMANENT dipole (fixed magnitude p_A, orientation angle theta):")
    print(f"    U(r,theta)   = {U_perm}")
    print(f"    F_r(r,theta) = {Fr_perm}    <- 1/r^3 but ANGULAR (∝ cos theta)")
    # solid-angle average of the linear term
    avg = sp.integrate(sp.cos(theta) * sp.sin(theta), (theta, 0, sp.pi)) / 2
    print(f"    <cos theta> over sphere = {avg}   -> linear term AVERAGES TO ZERO (C1)")
    print("    => central 1/r^3 only if theta=0 ALWAYS (dipole points at B) -- impossible")
    print("       for a PERMANENT dipole facing multiple neighbours (N-body inconsistent).")

    # (I) INDUCED dipole p_A = alpha * g_A, g_A = G m_B / r^2 (radial). Always radial.
    pA_ind = alpha * G * mB / r**2
    U_ind = -G * mB * pA_ind / r**2  # radial dipole (theta=0): -G m_B p_A / r^2
    Fr_ind = sp.simplify(-sp.diff(U_ind, r))
    print("\n(I) INDUCED dipole p_A = alpha * g_A (polarization, always radial):")
    print(f"    p_A(r)  = {pA_ind}      <- magnitude depends on m_B and r (NOT fixed)")
    print(f"    U(r)    = {sp.simplify(U_ind)}")
    print(f"    F_r(r)  = {Fr_ind}    <- CENTRAL, but 1/r^5 (WRONG power)")

    print("\n" + "=" * 70)
    print("REQUIREMENT vs MECHANISMS")
    print("=" * 70)
    rows = [
        ("property", "MULTING needs", "(P) permanent", "(I) induced"),
        ("force power", "1/r^3", "1/r^3  OK", "1/r^5  FAIL"),
        ("angular structure", "central", "angular FAIL", "central OK"),
        ("magnitude", "fixed ∝ k_A", "fixed OK", "∝ m_B/r^2 FAIL"),
        ("repulsive-capable", "yes (-F_d)", "yes OK", "yes OK"),
    ]
    for a, b, cc, d in rows:
        print(f"  {a:<18} {b:<15} {cc:<15} {d}")

    print("\n" + "=" * 70)
    print("VERDICT (step 1 — kill-test result; full write-up + skeptic in docs/130)")
    print("=" * 70)
    print("  MULTING's dipole needs BOTH a FIXED magnitude (∝ k_A, a property of A alone)")
    print("  AND an always-RADIAL direction AND a 1/r^3 force. The permanent dipole gives")
    print("  fixed magnitude but is ANGULAR (and N-body inconsistent if forced radial);")
    print("  the induced dipole is radial but has the WRONG power (1/r^5) and a magnitude")
    print("  that depends on m_B, r -- not a fixed property of A. NO single standard local")
    print("  isotropic mechanism supplies the conjunction. The sign (repulsion) is NOT the")
    print("  obstruction; the CONJUNCTION of fixed-magnitude + radial + 1/r^3 is.")
    print("  => the central-vs-angular 'risk' is a REAL obstruction for the standard")
    print("     candidates. This does NOT prove no local theory exists (see docs/130")
    print("     scope caveat) -- but the burden is now on exhibiting a non-standard")
    print("     construction (constrained/derivative coupling) that evades all three.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
