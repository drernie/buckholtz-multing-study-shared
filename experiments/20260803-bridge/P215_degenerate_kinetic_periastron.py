"""P215 -- the periastron bound for the ONE energy neither version excludes:
degenerate kinetic energy.

WHY THIS EXISTS. FINDING_unsuppressed_observable_periastron computed the
double-pulsar bound on beta_d for two choices of the neutron star's
internal energy:

    virial/binding energy (E/Mc^2 = 0.105)  ->  beta_d < 1.2e-5
    rotational energy only (P = 22.7 ms)    ->  beta_d < 6.0e-2

and concluded that "any version of MULTING in which k includes bulk
internal energy (binding, rotational, degeneracy) is excluded at the
1e-5 level". But a Step 8a skeptic pass on 2026-09-07 established, from
the source documents, that:

  - BINDING energy is explicitly excluded by BOTH versions
    (v6:601-602 "potential energies that ... bind sub-objects into
    objects"; v82:1381-1383 "de-emphasize ... potential energies within
    objects").
  - ROTATIONAL energy is excluded by v6's own definition of k
    ("energies of LINEAR motion", v6:640).
  - DEGENERACY is named in that conclusion but was NEVER COMPUTED, and
    appears nowhere in either document.

So both computed rows use energies the corpus excludes, and the one
energy that could survive -- degenerate kinetic energy of the neutron
Fermi sea, which is kinetic, not potential, not bulk, not rotational --
has no row. This supplies it.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np

# --- constants (SI) -------------------------------------------------------
C = 299792458.0
HBAR = 1.054571817e-34
M_N = 1.67492749804e-27  # neutron mass, kg
MSUN = 1.98847e30
MEV = 1.602176634e-13  # J

# --- J0737-3039, the double pulsar ---------------------------------------
# [MEMORY] textbook values; the ORDER OF MAGNITUDE is what this script is
# for, and the two positive controls below pin the arithmetic to the
# existing finding rather than to these being exact.
M_A = 1.338 * MSUN
M_B = 1.249 * MSUN
P_SPIN_A = 22.70e-3  # s
R_NS_DEFAULT = 11.0e3  # m -- back-solved from the existing binding row, see PC1

ELL_D_LIMIT = 0.055  # m -- |ell_d| < 5.5 cm, from omega_dot at 2.4e-6 fractional
F_BIND = 0.105  # E_binding / Mc^2, the existing finding's value


def beta_bound(u_a, u_b, ell_limit=ELL_D_LIMIT):
    """ell_d = 2 beta_d (u_A + u_B)  =>  beta_d < ell_limit / (2(u_A+u_B))."""
    return ell_limit / (2.0 * (u_a + u_b))


def u_from_fraction(frac, r_ns):
    """u = (k/(m c^2)) * r  -- the finding's own definition."""
    return frac * r_ns


# --- degenerate Fermi gas ------------------------------------------------
def ke_fraction_degenerate(n_number_density):
    """Kinetic-energy fraction K/(N m c^2) of a cold, relativistic,
    ideal degenerate neutron gas at number density n.

        x   = p_F/(m c),   p_F = hbar (3 pi^2 n)^(1/3)
        eps = (m^4 c^5 / (pi^2 hbar^3)) * (1/8)[ x sqrt(1+x^2)(1+2x^2)
                                                 - asinh(x) ]
        K   = eps - n m c^2
    """
    p_f = HBAR * (3.0 * np.pi**2 * n_number_density) ** (1.0 / 3.0)
    x = p_f / (M_N * C)
    pref = M_N**4 * C**5 / (np.pi**2 * HBAR**3)
    eps = pref * 0.125 * (x * np.sqrt(1.0 + x * x) * (1.0 + 2.0 * x * x) - np.arcsinh(x))
    rest = n_number_density * M_N * C * C
    return (eps - rest) / rest, x


def ke_fraction_nonrel(n_number_density):
    """Non-relativistic limit, (3/5) p_F^2/(2 m), as a check on the above."""
    p_f = HBAR * (3.0 * np.pi**2 * n_number_density) ** (1.0 / 3.0)
    return 0.6 * p_f * p_f / (2.0 * M_N) / (M_N * C * C)


def mean_number_density(mass, radius):
    return mass / M_N / ((4.0 / 3.0) * np.pi * radius**3)


def sep(t):
    print("\n" + "=" * 74 + "\n" + t + "\n" + "=" * 74)


def main() -> int:
    sep("PC1 -- reproduce the EXISTING binding-energy row (1.15e3 m, 1.2e-5)")
    u_bind = u_from_fraction(F_BIND, R_NS_DEFAULT)
    b_bind = beta_bound(u_bind, u_bind)
    print(f"  f_binding = {F_BIND}, R_NS = {R_NS_DEFAULT / 1e3:.1f} km")
    print(f"  u_NS      = {u_bind:.3e} m      (finding: 1.15e3 m)")
    print(f"  beta_d    < {b_bind:.3e}        (finding: 1.2e-5)")
    ok1 = abs(u_bind - 1.15e3) / 1.15e3 < 0.02 and abs(b_bind - 1.2e-5) / 1.2e-5 < 0.05
    print(f"  {'PASS -- arithmetic understood' if ok1 else 'FAIL -- formula not reproduced'}")
    if not ok1:
        return 1

    sep("PC2 -- reproduce the EXISTING rotational row (0.23 m, 6.0e-2)")
    # rotational KE of a uniform sphere: (1/2) I omega^2, I = (2/5) M R^2
    omega = 2.0 * np.pi / P_SPIN_A
    inertia = 0.4 * M_A * R_NS_DEFAULT**2
    f_rot = 0.5 * inertia * omega**2 / (M_A * C * C)
    u_rot = u_from_fraction(f_rot, R_NS_DEFAULT)
    b_rot = beta_bound(u_rot, u_rot)
    print(f"  P_spin = {P_SPIN_A * 1e3:.2f} ms, uniform sphere I = 0.4 M R^2")
    print(f"  f_rot  = {f_rot:.4e}")
    print(f"  u_NS   = {u_rot:.3e} m          (finding: 0.23 m)")
    print(f"  beta_d < {b_rot:.3e}            (finding: 6.0e-2)")
    print("  (order-of-magnitude agreement is the bar here; the finding does")
    print("   not state its moment-of-inertia convention)")

    sep("NC1 -- the degenerate formula must reduce to (3/5)p_F^2/2m at low x")
    for n_test in (1e42, 1e43, 1e44):
        f_rel, x = ke_fraction_degenerate(n_test)
        f_nr = ke_fraction_nonrel(n_test)
        rel = abs(f_rel - f_nr) / f_nr
        print(
            f"  n={n_test:.0e} m^-3  x={x:.4f}  rel={f_rel:.4e}  nonrel={f_nr:.4e}  diff={rel:.1%}"
        )
    print("  -> the two must converge as x -> 0; divergence at large x is the")
    print("     relativistic correction, not an error")

    sep("THE MISSING ROW -- degenerate kinetic energy")
    print("  Uniform-density approximation, as the existing finding also used.")
    print(
        f"  {'R_NS [km]':>10} {'n [m^-3]':>12} {'x=p_F/mc':>10} {'f_deg':>10} {'u_NS [m]':>10} {'beta_d <':>11}"
    )
    results = []
    for r_km in (10.0, 11.0, 12.0, 13.0, 14.0):
        r = r_km * 1e3
        n_a = mean_number_density(M_A, r)
        n_b = mean_number_density(M_B, r)
        f_a, x_a = ke_fraction_degenerate(n_a)
        f_b, _ = ke_fraction_degenerate(n_b)
        u_a, u_b = u_from_fraction(f_a, r), u_from_fraction(f_b, r)
        bd = beta_bound(u_a, u_b)
        results.append(bd)
        print(f"  {r_km:10.1f} {n_a:12.3e} {x_a:10.4f} {f_a:10.4f} {u_a:10.2f} {bd:11.3e}")

    sep("VERDICT")
    lo, hi = min(results), max(results)
    print(f"  degenerate-kinetic bound on beta_d : {lo:.2e} - {hi:.2e}")
    print(f"  existing binding-energy row        : {b_bind:.2e}")
    print("  Table A1's fitted beta_d           : 4.5")
    print(
        f"  orders of magnitude below Table A1 : {np.log10(4.5 / hi):.1f} - {np.log10(4.5 / lo):.1f}"
    )
    print(f"""
  Degeneracy is the ONE internal energy neither version of the corpus
  excludes: it is KINETIC (Fermi motion of neutrons), not potential, not
  bulk, not rotational. Binding is excluded by both (v6:601-602,
  v82:1381-1383); rotational by v6's own "linear motion" definition.

  So the periastron bound, restricted to the energy the corpus actually
  admits, still lands at the {np.log10(1.0 / hi):.0f}-order level and still sits far below
  Table A1's fitted 4.5.

  CAVEATS, both real: (1) uniform density is a crude NS model -- a
  realistic profile concentrates mass centrally, RAISING the mean Fermi
  momentum and therefore f_deg, so this is if anything conservative;
  (2) an ideal neutron Fermi gas ignores strong-interaction corrections,
  which at these densities are not small. Neither moves the result by the
  ~5 orders that would be needed to matter.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
