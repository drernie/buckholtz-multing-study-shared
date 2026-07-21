"""l1_weakfield_matching.py — CANDIDATE-L1 exact weak-field matching (docs/131).

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

The real matching test (docs/130): take a Blanchet-Le Tiec-type polarizable point
particle — position x_A, mass m_A, internal dipole vector xi_A with internal potential
W(xi_A) — solve xi_A's equation of motion, substitute back, read off the effective
two-body potential, and check WITHOUT hand-tuning: r-powers, SIGN, A<->B symmetry.

Two natural internal potentials W give two branches:
  (H) HARMONIC W = (1/2) kappa xi^2   (minimum at xi=0)  -> INDUCED dipole xi ∝ g
  (S) SOMBRERO W (minimum at |xi|=xi0 ∝ k_A)             -> FIXED magnitude, free orient.

Monopole-dipole interaction (gravitational analog of charge-dipole):
  U_md = -G m_B (p_A . r_hat)/r^2 ,   p_A = m_A xi_A   (dipole moment).

Run:  python scripts/l1_weakfield_matching.py
Exit: 0 (report). Verdict (PASS/FAIL/BLOCKED) in the printout + docs/131.
"""

from __future__ import annotations

import sympy as sp


def main() -> int:
    G, mA, mB, r, kappa, P, theta, xi0, kA = sp.symbols(
        "G m_A m_B r kappa P theta xi0 k_A", positive=True
    )

    print("=" * 70)
    print("CANDIDATE-L1 weak-field matching — solve xi EoM, substitute back")
    print("=" * 70)

    # ---- Branch (H): HARMONIC W = (1/2) kappa xi^2 -> induced dipole ------------
    # EoM: kappa xi_A = m_A g_B  (dipole driven by B's field g_B = G m_B / r^2, radial)
    gB = G * mB / r**2
    xi_ind = mA * gB / kappa  # induced dipole magnitude (radial, along r_hat)
    p_ind = mA * xi_ind  # dipole moment p_A = m_A xi_A
    # substitute back: U_md = -G m_B (p_A . r_hat)/r^2, p_A radial so (p_A.r_hat)=p_ind
    U_ind = sp.simplify(-G * mB * p_ind / r**2)
    F_ind = sp.simplify(-sp.diff(U_ind, r))
    print("\n(H) HARMONIC W  -> INDUCED dipole (xi ∝ g):")
    print(f"    xi_A = {sp.simplify(xi_ind)}   (radial, ∝ 1/r^2)")
    print(f"    U_md = {U_ind}      <- 1/r^4 potential (NOT MULTING's 1/r^2)")
    print(f"    F    = {F_ind}    <- 1/r^5 force, ∝ m_A^2 m_B^2 (WRONG power AND scaling)")
    print("    => branch (H) FAILS: induced dipole gives 1/r^4, not MULTING's 1/r^2.")

    # ---- Branch (S): SOMBRERO W -> fixed magnitude |xi|=xi0 (∝ k_A), free orient -
    # dipole moment magnitude P = m_A xi0 (∝ k_A). Orientation angle theta to r_hat.
    U_S = -G * mB * P * sp.cos(theta) / r**2  # monopole-dipole, fixed |p_A|=P
    # EoM for ORIENTATION: minimize U_S over theta (energy minimization, NOT assumed)
    dU_dtheta = sp.diff(U_S, theta)
    print("\n(S) SOMBRERO W  -> fixed |p_A|=P (∝ k_A), orientation free:")
    print(f"    U_md(theta) = {U_S}")
    print(f"    dU/dtheta   = {dU_dtheta}   -> stationary at theta=0 and theta=pi")
    U_min = U_S.subs(theta, 0)  # theta=0: n_hat ∥ r_hat
    U_max = U_S.subs(theta, sp.pi)  # theta=pi: n_hat anti ∥ r_hat
    d2 = sp.diff(U_S, theta, 2)
    print(f"    theta=0  : U={U_min}  (2nd deriv {sp.simplify(d2.subs(theta, 0))}) -> STABLE MIN")
    print(
        f"    theta=pi : U={sp.simplify(U_max)}  (2nd deriv {sp.simplify(d2.subs(theta, sp.pi))}) -> UNSTABLE MAX"
    )
    F_min = sp.simplify(-sp.diff(U_min, r))
    print(f"    at the stable minimum (theta=0): F = {F_min}")
    print("      -> 1/r^3 force, CENTRAL, ∝ P m_B ∝ k_A m_B  <- RIGHT structure!")
    print(f"      -> but F = {F_min} < 0  =>  ATTRACTIVE (pulls A,B together).")

    print("\n" + "=" * 70)
    print("SIGN CONFRONTATION with MULTING")
    print("=" * 70)
    print("  MULTING: F_oP = F_m - F_d + F_q. The dipole is SUBTRACTED (-F_d) ->")
    print("  MULTING's dipole is REPULSIVE (reduces attraction, pushes P away from A).")
    print("  Branch (S) energy-minimized dipole is ATTRACTIVE (theta=0, stable).")
    print("  MULTING's repulsion would need theta=pi (anti-aligned) = the UNSTABLE")
    print("  energy MAXIMUM -> a stable dipole cannot sit there. Flipping the coupling")
    print("  sign (repulsive monopole-dipole) requires negative gravitational mass or a")
    print("  wrong-sign kinetic term -> GHOST.")

    print("\n" + "=" * 70)
    print("VERDICT — CANDIDATE-L1 weak-field matching")
    print("=" * 70)
    print("  Branch (H) harmonic/induced : FAIL  (1/r^4, not 1/r^2; ∝ m^2 m^2).")
    print("  Branch (S) sombrero/fixed   : reproduces MULTING's dipole STRUCTURE")
    print("     (central, 1/r^3 force, ∝ k_A m_B) with alignment DERIVED (not assumed)")
    print("     -- BUT the stable (energy-minimizing) alignment is ATTRACTIVE, whereas")
    print("     MULTING's dipole is REPULSIVE. Repulsion = the unstable energy maximum,")
    print("     or a wrong-sign/ghost coupling.")
    print("  => VERDICT: FAIL on SIGN (skeptic-reviewed, scope-bounded). MULTING's")
    print("     repulsive dipole needs internal kinetic energy k_A/c^2 (positive mass-")
    print("     energy -- the 1/c^2 in F_d IS that factor) to ANTI-gravitate, against")
    print("     the equivalence principle. Structure matchable (branch S); repulsive")
    print("     sign not, without negative mass / tachyon (kappa<0) / ghost / driven")
    print("     non-equilibrium. Escapes closed: k_A-as-distinct-charge (k_A IS energy,")
    print("     EP fixes its sign); vector mediator (gives 1/r or Yukawa, not 1/r^3).")
    print("  (docs/131 -- skeptic corrected an 'ANY medium' overreach; verdict survives")
    print("   for EP-respecting, positive-energy, ghost-free, static local realizations.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
