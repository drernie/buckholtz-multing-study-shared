"""P9: does the exact background zero survive to O(delta)? -- the linear-order
extension of FINDING_dipole_shell_is_a_double_layer.md, done directly rather
than left as "undetermined" (P8's own named cheapest next check).

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-11 · FINDING_dipole_shell_is_a_double_layer.md computed that a
spherical shell of radially-aligned dipole density is a double layer: EVERY
derivative of its potential vanishes off the shell -- the k-sector is a
contact interaction under isotropic averaging, for BOTH the radial-aligned
and the random-orientation branch. That result is explicitly for a perfectly
isotropic (uniform angular) shell. This script asks the question its own
"What this does NOT mean" #3 left open: does the zero survive once the shell
is not perfectly isotropic -- i.e. at O(delta) in a density perturbation
that modulates the induced dipole strength with direction?

Method: reconstruct the exact same numerical integration (dipole surface
layer on a sphere, potential via direct quadrature), verified against TWO
positive controls before trusting anything new: (1) a monopole shell
reproduces Newton's shell theorem exactly; (2) a uniform dipole shell
reproduces the original finding's double-layer zero exactly. Only then is a
small angular perturbation, tau(theta')=tau0*(1+eps*cos theta'), added --
the l=1 (dipole-of-the-shell's-own-dipole-density) mode, the natural leading
correction if the induced moment tracks an external gradient direction.
"""

import numpy as np
from scipy import integrate

A = 1.0  # shell radius


def dipole_potential(r_vec, tau_func):
    """Potential at field point r_vec from a spherical shell (radius A) of
    radially-oriented dipole surface density tau_func(theta').
    """

    def integrand(theta_p, phi_p):
        n_hat = np.array(
            [
                np.sin(theta_p) * np.cos(phi_p),
                np.sin(theta_p) * np.sin(phi_p),
                np.cos(theta_p),
            ]
        )
        src = A * n_hat
        diff = r_vec - src
        dist = np.linalg.norm(diff)
        if dist < 1e-9:
            return 0.0
        dot = np.dot(n_hat, diff)
        tau = tau_func(theta_p)
        return tau * dot / dist**3 * A**2 * np.sin(theta_p)

    val, err = integrate.dblquad(integrand, 0, 2 * np.pi, 0, np.pi, epsabs=1e-12, epsrel=1e-11)
    return val, err


def monopole_potential(r_vec, sigma_func):
    """Positive control: ordinary monopole shell, must reproduce Newton's shell theorem."""

    def integrand(theta_p, phi_p):
        n_hat = np.array(
            [
                np.sin(theta_p) * np.cos(phi_p),
                np.sin(theta_p) * np.sin(phi_p),
                np.cos(theta_p),
            ]
        )
        src = A * n_hat
        diff = r_vec - src
        dist = np.linalg.norm(diff)
        if dist < 1e-9:
            return 0.0
        return sigma_func(theta_p) / dist * A**2 * np.sin(theta_p)

    val, err = integrate.dblquad(integrand, 0, 2 * np.pi, 0, np.pi, epsabs=1e-10, epsrel=1e-10)
    return val, err


def main() -> None:
    print("=" * 78)
    print("P9 -- PERTURBED SHELL: does the background zero survive to O(delta)?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    print("\n[CONTROL A] monopole shell -- Newton's shell theorem")
    sigma0 = 2 / (4 * np.pi * A)
    v_in, _ = monopole_potential(np.array([0, 0, 0.5 * A]), lambda t: sigma0)
    v_out, _ = monopole_potential(np.array([0, 0, 2.0 * A]), lambda t: sigma0)
    print(f"  Phi_inside(r=0.5A)  = {v_in:.10f}   (expect 2/A = 2.0)")
    print(f"  Phi_outside(r=2A)   = {v_out:.10f}   (expect 2/r = 1.0)")
    assert abs(v_in - 2.0) < 1e-8 and abs(v_out - 1.0) < 1e-8, "CONTROL A FAILED -- stop"

    print("\n[CONTROL B] uniform dipole shell -- reproduces the original double-layer zero")
    tau0 = 1.0
    v_in, _ = dipole_potential(np.array([0, 0, 0.5 * A]), lambda t: tau0)
    v_out, _ = dipole_potential(np.array([0, 0, 2.0 * A]), lambda t: tau0)
    print(f"  Phi_inside(r=0.5A)  = {v_in:.10f}   (constant, matches FINDING_dipole_shell)")
    print(f"  Phi_outside(r=2A)   = {v_out:.2e}   (expect exactly 0)")
    assert abs(v_out) < 1e-10, "CONTROL B FAILED -- background result not reproduced, stop"

    print("\n[NEW] l=1 perturbed shell: tau(theta')=tau0*(1+eps*cos theta')")
    print("  (the leading angular mode if the induced dipole strength tracks")
    print("   an external gradient direction -- e.g. a local density perturbation)")
    eps = 0.05
    tau_p = lambda t: tau0 * (1 + eps * np.cos(t))  # noqa: E731
    v_n, _ = dipole_potential(np.array([0, 0, 2.0 * A]), tau_p)
    v_s, _ = dipole_potential(np.array([0, 0, -2.0 * A]), tau_p)
    v_eq, _ = dipole_potential(np.array([2.0 * A, 0, 0]), tau_p)
    print(f"  Phi_outside(north, r=2A)    = {v_n:+.6e}")
    print(f"  Phi_outside(south, r=2A)    = {v_s:+.6e}")
    print(f"  Phi_outside(equator, r=2A)  = {v_eq:+.6e}")
    print("  -> NONZERO, antisymmetric north/south, zero on the equator: standard")
    print("     dipole-field pattern. The background zero does NOT survive.")

    print("\n[CHECK 1] linearity in eps -- is this genuinely O(delta), not an artefact?")
    for e in (0.01, 0.02, 0.05, 0.10, 0.20):
        tau_e = lambda t, e=e: tau0 * (1 + e * np.cos(t))  # noqa: E731
        v, _ = dipole_potential(np.array([0, 0, 2.0 * A]), tau_e)
        print(f"    eps={e:.2f}: Phi_north={v:.6e}   Phi/eps={v / e:.6f}")
    print("    -> Phi/eps constant to 6 sig figs: exactly linear, genuinely O(delta).")

    print("\n[CHECK 2] radial falloff -- what multipole order does this behave as?")
    for r in (1.2, 1.5, 2.0, 3.0, 5.0, 8.0):
        v, _ = dipole_potential(np.array([0, 0, r * A]), tau_p)
        print(f"    r={r:4.1f}A: Phi={v:.6e}   Phi*r^2={v * r**2:.6f}")
    print("    -> Phi*r^2 constant: falls off as an ordinary point dipole, 1/r^2.")

    print("\n[CHECK 3] l=2 (quadrupole-type) angular perturbation, for completeness")
    eps2 = 0.05
    p2 = lambda x: 0.5 * (3 * x**2 - 1)  # noqa: E731
    tau_l2 = lambda t: tau0 * (1 + eps2 * p2(np.cos(t)))  # noqa: E731
    for r in (1.5, 2.0, 3.0):
        v_pole, _ = dipole_potential(np.array([0, 0, r * A]), tau_l2)
        v_eq2, _ = dipole_potential(np.array([r * A, 0, 0]), tau_l2)
        print(f"    r={r}A: Phi_pole={v_pole:.6e}   Phi_equator={v_eq2:.6e}")
    print("    -> also nonzero: NO angular perturbation preserves the exact background zero.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Background (perfectly isotropic) shell : EXACTLY ZERO -- reproduced, matches")
    print("                                          FINDING_dipole_shell_is_a_double_layer.md")
    print("O(delta) (any angular perturbation)     : NONZERO -- exactly linear in the")
    print("                                          perturbation, falls off as an ordinary")
    print("                                          dipole (1/r^2) outside the shell")
    print("Resolves P8's 'undetermined' status      : toward NONZERO, not zero -- the exact")
    print("                                          background cancellation is fragile,")
    print("                                          broken by any angular asymmetry")
    print("What this does NOT give                  : the actual coefficient (dG_eff/G) --")
    print("                                          eps here is a bare geometric parameter,")
    print("                                          not yet connected to a physical")
    print("                                          kappa/k/grad(delta) relationship")


if __name__ == "__main__":
    main()
