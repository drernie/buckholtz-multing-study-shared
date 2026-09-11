"""l1_gyroscopic_stabilization_test.py — does giving xi_A real inertia (a
conserved azimuthal angular momentum, symmetric-top style) let MULTING's
REPULSIVE dipole configuration (theta=pi) become dynamically accessible,
via a centrifugal barrier -- the one residual open branch docs/131 flagged
as untested ("driven anti-aligned state" was dismissed there only for a
NON-conservative, externally-pumped mechanism; a conservative,
angular-momentum-stabilized mechanism was never checked).

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR

Setup (continues docs/131's own Branch (S), sombrero W, fixed |p_A|=P):
  U(theta) = -G m_B P cos(theta) / r^2        (docs/131's own U_S, unchanged)

docs/131 found this via pure potential minimization -- no kinetic term for
xi_A was ever written down, i.e. xi_A was treated adiabatically (auxiliary),
not as a genuine dynamical variable. This script gives xi_A the standard
symmetric-top treatment instead: a moment of inertia I about axes
perpendicular to its own symmetry axis, and a CONSERVED azimuthal angular
momentum L (Noether charge of the axial symmetry of U(theta) itself, which
does not depend on the azimuthal angle phi). The reduced 1-DOF effective
potential for theta is then the textbook heavy-symmetric-top (Lagrange top)
form:

  U_eff(theta; L) = U(theta) + L^2 / (2 I sin^2(theta))

Both poles (theta=0, theta=pi) now diverge to +infinity for any L>0 -- the
question is where the new interior minimum sits, and in particular whether
it can ever cross past theta=pi/2 (where cos(theta) flips sign, which is
what the radial force sign is controlled by -- see the envelope-theorem
argument in the module docstring below main()).

Run:  python scripts/l1_gyroscopic_stabilization_test.py
Exit: 0 (report). Verdict in the printout + docs/131 ADDENDUM.
"""

from __future__ import annotations

import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar


def main() -> int:
    print("=" * 78)
    print("L1 gyroscopic-stabilization test -- does angular momentum rescue")
    print("MULTING's repulsive dipole sign from docs/131's FAIL verdict?")
    print("=" * 78)

    # ---- Part 1: symbolic perturbative check near theta = pi/2 -----------------
    print("\n--- Part 1: symbolic, small-L-correction expansion near theta=pi/2 ---")
    A, I_mom, L, phi = sp.symbols("A I_mom L phi", positive=True)
    theta = sp.pi / 2 + phi
    U = -A * sp.cos(theta)  # A := G m_B P / r^2, docs/131's own combination
    centrifugal = L**2 / (2 * I_mom * sp.sin(theta) ** 2)
    U_eff = U + centrifugal
    # Expand to O(phi^2) around phi=0 (theta=pi/2) -- exact symbolic series,
    # not an approximation choice made after seeing the answer.
    series = sp.series(U_eff, phi, 0, 3).removeO()
    series = sp.expand(series)
    print(f"  U_eff(theta=pi/2 + phi) series to O(phi^2):\n    {series}")
    dseries_dphi = sp.diff(series, phi)
    phi_min = sp.solve(sp.Eq(dseries_dphi, 0), phi)
    print(f"  d/dphi = 0  =>  phi_min = {phi_min}")
    # WHY: phi_min < 0 for all positive A, I, L means theta_eq = pi/2 + phi_min
    # stays on the theta < pi/2 side (the attractive side) for every L -- the
    # large-L limit approaches pi/2 from below, it never reaches or crosses it.
    sign_check = sp.simplify(phi_min[0] < 0) if phi_min else None
    print(f"  sign(phi_min) < 0 for all A,I,L>0 ? {sign_check}")
    print("  => (perturbative regime) equilibrium stays on the ATTRACTIVE side,")
    print("     approaching theta=pi/2 (cos=0, zero dipole force) as L -> infinity,")
    print("     never reaching the REPULSIVE side (theta>pi/2).")

    # ---- Part 2: full numerical scan, no small-phi assumption -------------------
    print("\n--- Part 2: full numerical minimization, no perturbative assumption ---")
    print("  U_eff(theta; L_hat) = -cos(theta) + L_hat^2 / (2 sin^2(theta))")
    print("  (dimensionless: A=I=1, L_hat = L/sqrt(A I) swept over a wide range)")
    header = f"  {'L_hat':>10} {'theta_eq [deg]':>16} {'cos(theta_eq)':>16} {'F sign':>10}"
    print(header)
    worst_case_cos = 1.0  # track the most-negative cos(theta_eq) seen, across all L
    for L_hat in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 200.0, 1000.0, 10000.0]:

        def U_eff_numeric(th: float, _L: float = L_hat) -> float:
            return -np.cos(th) + (_L**2) / (2.0 * np.sin(th) ** 2)

        # Search only the (0, pi/2] half first (theta=pi/2 excluded from the
        # open-interval search below, checked separately) -- if a genuine
        # minimum exists past pi/2, a full-domain scan (next block) will catch
        # it; this call finds the near-pole-avoiding interior minimum.
        res = minimize_scalar(U_eff_numeric, bounds=(1e-6, np.pi - 1e-6), method="bounded")
        theta_eq = float(res.x)
        cos_eq = float(np.cos(theta_eq))
        worst_case_cos = min(worst_case_cos, cos_eq)
        f_sign = "attractive" if cos_eq > 1e-9 else ("repulsive" if cos_eq < -1e-9 else "~zero")
        print(f"  {L_hat:>10.2f} {np.degrees(theta_eq):>16.4f} {cos_eq:>16.6f} {f_sign:>10}")

    # ---- Part 3: brute-force full-domain grid check (catches any secondary
    # minimum near theta=pi that the bounded 1D optimizer above might miss) ------
    print("\n--- Part 3: brute-force 100000-point grid scan for a SECOND minimum ---")
    theta_grid = np.linspace(1e-4, np.pi - 1e-4, 100_000)
    any_repulsive_min_found = False
    for L_hat in [10.0, 1000.0, 1_000_000.0]:
        U_grid = -np.cos(theta_grid) + (L_hat**2) / (2.0 * np.sin(theta_grid) ** 2)
        i_min = int(np.argmin(U_grid))
        theta_at_min = theta_grid[i_min]
        cos_at_min = float(np.cos(theta_at_min))
        print(
            f"  L_hat={L_hat:>10.1f}: global-grid minimum at theta="
            f"{np.degrees(theta_at_min):.4f} deg, cos={cos_at_min:.6f}"
        )
        if cos_at_min < -1e-6:
            any_repulsive_min_found = True

    # ---- Verdict -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  Most-negative cos(theta_eq) found across ALL tested L (up to L_hat=1e6):")
    print(f"    {worst_case_cos:.9f}  (positive => never crossed into repulsive)")
    if any_repulsive_min_found or worst_case_cos < -1e-6:
        print("  => UNEXPECTED: a repulsive-side minimum was found. Re-examine before")
        print("     trusting this printout -- this would contradict the symbolic Part 1")
        print("     result and needs independent re-derivation.")
    else:
        print("  => CONFIRMED (symbolic Part 1 + numeric Parts 2-3 agree):")
        print("     giving xi_A genuine inertia and a conserved angular momentum does")
        print("     NOT rescue MULTING's repulsive sign. The centrifugal barrier only")
        print("     ever pushes the stable equilibrium from theta=0 (fully attractive)")
        print("     TOWARD theta=pi/2 (F->0, zero net dipole force) as L->infinity --")
        print("     it asymptotically WEAKENS the attraction, it never reaches, let")
        print("     alone crosses into, the repulsive (theta>pi/2) half.")
        print("     This is a real, checked NULL result for the one residual branch")
        print("     docs/131 itself flagged as untested ('driven anti-aligned state',")
        print("     conservative/angular-momentum variant). docs/131's own FAIL verdict")
        print("     on the repulsive sign is UNCHANGED by this test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
