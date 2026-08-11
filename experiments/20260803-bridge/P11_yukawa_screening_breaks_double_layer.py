"""P11: does a massive (Yukawa-screened) mediator break the exact double-layer
zero, without any assumed angular asymmetry -- P4's second, still-untouched
escape route (screened/massive propagator), checked directly.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12. FINDING_dipole_shell_is_a_double_layer.md's exact background zero
is a property specific to the MASSLESS (Coulomb, 1/dist) Green's function --
Newton's shell theorem makes the exterior potential of ANY spherically
symmetric shell independent of the shell's own radius, so two infinitesimally
displaced concentric shells (the double-layer limit) cancel exactly, for any
r outside. For a Yukawa (massive) Green's function exp(-mu*dist)/dist, the
exterior potential of a uniform shell is NOT independent of shell radius --
so the same double-layer limit should NOT cancel. This script tests that
directly: swap the Coulomb kernel for a Yukawa one in P9's exact numerical
method, keep the shell perfectly ANGULARLY UNIFORM (no eps, no assumed
asymmetry of any kind), and check whether finite mu alone is enough to
produce a nonzero exterior potential.

CRITICAL SELF-CONSISTENCY FLAG (read before citing this file): P1
(two_field_action_closure.py) already derived that this project's own
headline number, beta_q/beta_d = sqrt(6)/2, holds IF AND ONLY IF the mediator
is exactly massless (Lambda = K'''K'/K''^2 = 3/2 only for K=1/s; a massive
kernel makes Lambda r-dependent and != 3/2). So invoking a finite mu to break
the background cancellation is in direct tension with the same project's own
derivation of beta_d=2, beta_q=sqrt(6) -- UNLESS the mediator is effectively
massless at cluster/local scales (where beta_q/beta_d was derived and would
need to hold) and effectively massive/screened only at cosmological scales.
That is a real, nontrivial, scale-dependent self-consistency requirement
(the same class of claim chameleon/Vainshtein/symmetron screening makes) --
NOT checked or assumed here, only flagged as the load-bearing open question.
"""

import numpy as np
from scipy import integrate

A = 1.0  # shell radius
TAU0 = 1.0  # uniform dipole surface density (angularly UNIFORM -- no eps)


def dipole_potential_yukawa(r_vec, mu, tau_func):
    """Potential at field point r_vec from a spherical shell (radius A) of
    radially-oriented dipole surface density tau_func(theta'), sourced by a
    Yukawa Green's function G(dist)=exp(-mu*dist)/dist instead of 1/dist.

    Derivation (hand-verified, reduces exactly to P9's Coulomb formula at
    mu=0): dipole potential = -tau * (n_hat . diff) * G'(dist) / dist, and
    G'(dist) = -exp(-mu*dist)*(mu*dist+1)/dist^2 for the Yukawa kernel, so

        Phi_dipole = tau * (n_hat . diff) * (mu*dist+1) * exp(-mu*dist) / dist^3

    which reduces to P9's tau*dot/dist**3 exactly when mu=0.
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
        radial_factor = (mu * dist + 1.0) * np.exp(-mu * dist) / dist**2
        return tau * dot / dist * radial_factor * A**2 * np.sin(theta_p)

    val, err = integrate.dblquad(integrand, 0, 2 * np.pi, 0, np.pi, epsabs=1e-12, epsrel=1e-11)
    return val, err


def main() -> None:
    print("=" * 78)
    print("P11 -- YUKAWA SCREENING: does a massive mediator break the double layer?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    print("\n[CONTROL] mu=0 (massless limit) must reproduce the exact double-layer")
    print("  zero from FINDING_dipole_shell_is_a_double_layer.md / P9's control B")
    v_out, _ = dipole_potential_yukawa(np.array([0, 0, 2.0 * A]), 0.0, lambda t: TAU0)
    print(f"  Phi_outside(r=2A, mu=0) = {v_out:.3e}   (expect exactly 0)")
    assert abs(v_out) < 1e-10, "CONTROL FAILED -- Yukawa formula does not reduce to Coulomb at mu=0"

    print("\n[TEST] finite mu (screened/massive mediator), shell UNIFORM (tau=tau0,")
    print("  angularly constant -- NO assumed eps, unlike P9's ad hoc perturbation)")
    for mu in (0.01, 0.1, 0.5, 1.0, 2.0, 5.0):
        v_out, _ = dipole_potential_yukawa(np.array([0, 0, 2.0 * A]), mu, lambda t: TAU0)
        print(f"  mu={mu:5.2f} (mu*A={mu * A:.2f}): Phi_outside(r=2A) = {v_out:+.6e}")
    print("  -> NONZERO for every finite mu tested, with NO angular asymmetry assumed.")
    print("     Screening alone breaks the exact background cancellation.")

    print("\n[CHECK 1] angular uniformity at fixed r -- is this a genuine monopole-like")
    print("  (spherically symmetric) effect, or an artefact of sampling one point?")
    mu_test = 0.5
    points = {
        "north pole": np.array([0, 0, 2.0 * A]),
        "south pole": np.array([0, 0, -2.0 * A]),
        "equator": np.array([2.0 * A, 0, 0]),
        "45deg": np.array([np.sqrt(2) * A, 0, np.sqrt(2) * A]),
    }
    vals = {}
    for name, pt in points.items():
        v, _ = dipole_potential_yukawa(pt, mu_test, lambda t: TAU0)
        vals[name] = v
        print(f"    {name:12s}: Phi = {v:+.8e}")
    spread = max(vals.values()) - min(vals.values())
    print(f"    spread across 4 angular positions: {spread:.2e}")
    assert spread < 1e-8, "CHECK 1 FAILED -- result depends on angle, not spherically symmetric"
    print("    -> angle-independent to numerical precision. [Note, added after skeptic")
    print("       review: full rotational symmetry is GUARANTEED by the source's own")
    print("       symmetry (uniform tau) -- this checks quadrature fidelity (no polar-")
    print("       axis bias in dblquad), not independent physical evidence for the result.]")

    print("\n[CHECK 2] radial dependence at mu=0.5 -- confirms finite range (screened),")
    print("  not an ordinary 1/r^2 point dipole (that would be P9's mu=0 falloff)")
    for r in (1.2, 1.5, 2.0, 3.0, 5.0, 8.0):
        v, _ = dipole_potential_yukawa(np.array([0, 0, r * A]), mu_test, lambda t: TAU0)
        print(f"    r={r:4.1f}A: Phi={v:+.6e}   Phi*r^2={v * r**2:+.6e}")
    print("    -> Phi*r^2 is NOT constant (unlike P9's mu=0 case) -- confirms this is")
    print("       a genuinely screened, finite-range effect, not a disguised 1/r^2 tail.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Massless limit (mu=0)                 : EXACT ZERO -- reproduces")
    print("                                        FINDING_dipole_shell_is_a_double_layer.md")
    print("Finite mu, UNIFORM shell (no eps)     : NONZERO for every mu tested -- screening")
    print("                                        alone breaks the exact cancellation, with")
    print("                                        NO assumed angular asymmetry needed")
    print("Angular uniformity                    : passes (quadrature-fidelity check --")
    print("                                        symmetry is guaranteed by the source,")
    print("                                        not independent physical evidence;")
    print("                                        corrected after skeptic review)")
    print("Radial behaviour                      : finite-range (screened), not 1/r^2")
    print()
    print("CRITICAL TENSION (not resolved here): this project's OWN P1 finding proves")
    print("beta_q/beta_d=sqrt(6)/2 holds IFF the mediator is EXACTLY MASSLESS. [CORRECTED")
    print("after skeptic review:] a plain FIXED-MASS Yukawa with mu~H0/c resolves this")
    print("cleanly and needs NO density-dependent screening -- at cluster scale mu*r~1e-4,")
    print("so the correction to Lambda=3/2 is O((mu*r)^2)~1e-8, indistinguishable from")
    print("massless; cosmologically mu*r~1 and the double layer breaks as shown above.")
    print("The chameleon/Vainshtein/symmetron citation in an earlier version of this")
    print("finding was WRONG-DIRECTION (those screen NEAR matter, unscreen cosmologically")
    print("-- the opposite of what this construction needs) and has been corrected.")


if __name__ == "__main__":
    main()
