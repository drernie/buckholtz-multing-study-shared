"""TASK 2 — independent 3D derivation of K_p(R), cross-checked against the shell form.

!!! THIS SCRIPT IS EXPECTED TO FAIL ITS OWN CONTROL. That failure is the result.
    The mu-quadrature converges only for n_mu ~ 4e5 (integrable sqrt singularity
    at mu -> 1), which is unreachable on a 2D grid. Two consequences, both
    recorded in docs/132:
      1. a naive 3D mu-grid is NOT a usable cross-check of the shell formula;
      2. the v = s^2 substitution converts one into the other ANALYTICALLY,
         so they were never independent implementations to begin with.
    The genuine independent check is: my numerical quad over theta vs the
    closed forms C_3, C_4 (agree to 6+ digits). Run this script to see the
    failure mode, not to obtain a kernel.


The shell-integral kernel used so far was derived one way. This derives it a
SECOND, independent way — direct 3D quadrature of

    K_p(R) = int d^3x  xi(|x|)  [ (R - x) . Rhat ] / |R - x|^(p+1)   / (normalisation)

with NO shell decomposition anywhere. Agreement between the two routes is a
Path-B check (independently written code, same physics); disagreement means one
of them is wrong.

Explicit conventions, stated because Task 2 requires them:
  - distances: comoving Mpc throughout (xi converted from Mpc/h with h=0.677)
  - the test point sits at vector R = (0,0,R); Rhat = z-hat
  - the projected (radial) component of the force is taken, i.e. the z-component
  - lower limit: |x| >= 6 Mpc (upstream choice) unless a UV model overrides it
  - normalisation: divide by R^p so that p=2 reduces to the published I(R)/R^2
  - no (1+xi) pair weighting here (upstream fit2.py omits it; fit1.py includes
    it — that inconsistency is recorded separately and NOT silently adopted)
  - symmetrisation: none needed; xi is isotropic so only the z-component survives

POSITIVE CONTROL: for p = 2 the 3D integral must reproduce
    K_2(R) = [ int_6^R xi(r) r^2 dr ] / R^2
exactly (Newton's shell theorem). If it does not, the 3D code is wrong.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE = 0.677
R_MIN = 6.0


def load_xi():
    d = np.loadtxt(HERE / "xi_zbin2.dat")
    return interp1d(d[:, 0] / H_LITTLE, d[:, 1], bounds_error=False, fill_value=0.0)


def k_shell(R: float, p: int, xi, s_min: float = 0.0, n: int = 20000) -> float:
    """1D shell route (the method used so far)."""

    def C(rho):
        if rho <= 0:
            return 1.0
        if p == 2:
            return 1.0
        if p == 3:
            return 1 / (2 * (1 - rho**2)) + np.log((1 + rho) / (1 - rho)) / (4 * rho)
        return (3 + rho**2) / (6 * (1 - rho**2) ** 2) + 1 / (2 * (1 - rho**2))

    hi = R - s_min
    if hi <= R_MIN:
        return 0.0
    r = np.linspace(R_MIN, hi, n)
    return float(np.trapezoid(xi(r) * r**2 * np.array([C(x / R) for x in r]), r) / R**p)


def k_3d(R: float, p: int, xi, s_min: float = 0.0, n_r: int = 900, n_mu: int = 900) -> float:
    """Direct 3D quadrature. No shell decomposition used anywhere.

    d^3x = 2*pi * r^2 dr dmu   (azimuthal symmetry about Rhat), mu = cos(theta).
    separation s = sqrt(R^2 + r^2 - 2 R r mu); z-component factor = (R - r*mu)/s.
    Integrand: xi(r) * (R - r mu) / s^(p+1).
    """
    r = np.linspace(R_MIN, R * 3.0, n_r)  # extend beyond R: mass outside contributes too
    mu = np.linspace(-1.0, 1.0, n_mu)
    RR, MM = np.meshgrid(r, mu, indexing="ij")
    s2 = R**2 + RR**2 - 2 * R * RR * MM
    s = np.sqrt(np.clip(s2, 1e-12, None))
    mask = s >= max(s_min, 1e-9)
    integ = np.where(mask, xi(RR) * RR**2 * (R - RR * MM) / s ** (p + 1), 0.0)
    inner = np.trapezoid(integ, mu, axis=1)
    return float(2 * np.pi * np.trapezoid(inner, r) / (4 * np.pi) / R**p * R**p / R**p * R**p)


def k_3d_clean(R: float, p: int, xi, s_min: float = 0.0, n_r=900, n_mu=900, r_max_fac=3.0):
    """Same as k_3d but with the normalisation written once, clearly.

    K_p(R) = (1/2) * int_{r} int_{mu} xi(r) r^2 (R - r mu)/s^(p+1) dmu dr / R^p
    The 1/2 comes from 2*pi/(4*pi) — i.e. angular average, not total mass.
    """
    r = np.linspace(R_MIN, R * r_max_fac, n_r)
    mu = np.linspace(-1.0, 1.0, n_mu)
    RR, MM = np.meshgrid(r, mu, indexing="ij")
    s = np.sqrt(np.clip(R**2 + RR**2 - 2 * R * RR * MM, 1e-12, None))
    integ = np.where(s >= max(s_min, 1e-9), xi(RR) * RR**2 * (R - RR * MM) / s ** (p + 1), 0.0)
    return float(0.5 * np.trapezoid(np.trapezoid(integ, mu, axis=1), r) / R**p)


def main():
    xi = load_xi()
    print("=" * 78)
    print("TASK 2 — 3D kernel derivation vs shell route  |  L0: descriptive")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION")
    print("=" * 78)

    # ---------- POSITIVE CONTROL: p=2 must give the published Newtonian kernel
    print("\n[CONTROL] p=2 : 3D quadrature vs analytic I(R)/R^2 (shell theorem)")
    print(f"  {'R[Mpc]':>8} {'3D':>13} {'analytic':>13} {'rel.diff':>11}")
    ok = True
    for R in (50.0, 100.0, 150.0):
        an = quad(lambda x: xi(x) * x**2, R_MIN, R)[0] / R**2
        n3 = k_3d_clean(R, 2, xi, s_min=0.0, n_r=1400, n_mu=1400)
        rel = abs(n3 / an - 1)
        ok &= rel < 0.02
        print(f"  {R:8.0f} {n3:13.6f} {an:13.6f} {rel:11.3e}")
    print(f"  -> 3D route {'REPRODUCES' if ok else 'DOES NOT reproduce'} the Newtonian kernel")
    if not ok:
        print("  *** 3D code disagrees with shell theorem — STOP, do not trust p=3/4 ***")
        return

    # ---------- p=3 : do the two independent routes agree?
    print("\n[CROSS-CHECK] p=3, with UV cutoff s_min (both routes, same s_min)")
    print(f"  {'s_min':>7} {'R':>6} {'shell':>12} {'3D':>12} {'ratio':>9}")
    for s_min in (1.0, 2.0, 5.0):
        for R in (50.0, 100.0):
            a = k_shell(R, 3, xi, s_min=s_min)
            b = k_3d_clean(R, 3, xi, s_min=s_min, n_r=1400, n_mu=1400)
            print(
                f"  {s_min:7.1f} {R:6.0f} {a:12.6f} {b:12.6f} {b / a if a else float('nan'):9.3f}"
            )

    print("\n  NOTE: the shell route integrates mass only INSIDE r<R (enclosed-mass")
    print("  convention, as upstream). The 3D route above also includes mass OUTSIDE")
    print("  R, which for p=2 cancels by the shell theorem but for p=3 does NOT.")
    print("  That is a genuine physical difference between the two conventions,")
    print("  not a bug — and it is exactly the ambiguity Task 2 was meant to expose.")

    # ---------- 3D restricted to r<R, to isolate the convention question
    print("\n[CONVENTION TEST] 3D restricted to r<R (same mass as the shell route)")
    print(f"  {'s_min':>7} {'R':>6} {'shell':>12} {'3D r<R':>12} {'ratio':>9}")
    for s_min in (1.0, 2.0, 5.0):
        for R in (50.0, 100.0):
            a = k_shell(R, 3, xi, s_min=s_min)
            b = k_3d_clean(R, 3, xi, s_min=s_min, n_r=1400, n_mu=1400, r_max_fac=1.0)
            print(
                f"  {s_min:7.1f} {R:6.0f} {a:12.6f} {b:12.6f} {b / a if a else float('nan'):9.3f}"
            )


if __name__ == "__main__":
    main()
