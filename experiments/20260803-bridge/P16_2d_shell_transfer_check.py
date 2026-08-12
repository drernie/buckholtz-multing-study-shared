"""P16: does P15's self-vs-cross energy scaling (ring, 1D) transfer to the
actual 2D SPHERICAL-SHELL geometry FINDING_dipole_shell_is_a_double_layer.md
(P9) computed exactly?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12. P15's own context-blind skeptic review found that its 1D ring of
radially-aligned dipoles does NOT itself satisfy P9's shell theorem (a
2D/3D-symmetric-shell result, not a 1D-ring one) -- so P15's three regimes
(A: r_min shrinks with N -> self diverges; C: r_min fixed -> self vanishes;
B: realistic, both fixed -> self dominates) tested a DIFFERENT geometry than
P9's own. "The qualitative conclusion should transfer to the full 2D case"
was asserted there, not shown. This script re-runs the same three regimes on
a genuine quasi-uniform points-on-a-sphere distribution instead of a ring,
reusing P15's own verified self-energy formula and dipole-dipole cross-term
formula unchanged (the cross-term formula was already fully general in 3D;
only P15's own ring position-generator was 1D-specific).

SCOPE LIMIT, stated up front: this tests whether the SELF-VS-CROSS FIELD-
ENERGY scaling behavior transfers across dimension. It does NOT re-verify
P9's own exterior-potential zero for a discrete (finite-N) shell -- that
would be a different calculation (summing exterior POTENTIAL contributions,
not field ENERGY), not attempted here.
"""

import math

import sympy as sp

# ---------------------------------------------------------------------------
# Reused, unchanged from P15 (already verified there: two textbook positive
# controls for the cross-term formula; self-energy formula verified in P14
# against a monopole positive control). Not re-derived here -- see P15/P14.
# ---------------------------------------------------------------------------


def e_self(p, r_min):
    """P14/P15's own verified formula: (8*pi/3)*p^2/r_min^3."""
    return sp.Rational(8, 3) * sp.pi * p**2 / r_min**3


def u_cross_numeric(p1_vec, p2_vec, sep_vec):
    """P15's own verified general dipole-dipole interaction energy -- this
    formula was never ring-specific (it takes arbitrary 3-vectors); only
    P15's position generator was 1D. Reused unchanged."""
    dist = sum(c**2 for c in sep_vec) ** 0.5
    dhat = [c / dist for c in sep_vec]
    p1_dot_p2 = sum(a * b for a, b in zip(p1_vec, p2_vec, strict=True))
    p1_dot_dhat = sum(a * b for a, b in zip(p1_vec, dhat, strict=True))
    p2_dot_dhat = sum(a * b for a, b in zip(p2_vec, dhat, strict=True))
    return (p1_dot_p2 - 3 * p1_dot_dhat * p2_dot_dhat) / dist**3


# ---------------------------------------------------------------------------
# New for P16: genuine sphere geometry (P9's own class), not a ring.
# ---------------------------------------------------------------------------


def fibonacci_sphere(n, radius):
    """Standard quasi-uniform point distribution on a sphere (Fibonacci
    lattice) -- a well-known numerical technique for approximately-equal-
    area sphere sampling, not a novel method invented for this script."""
    points = []
    golden_angle = math.pi * (3 - math.sqrt(5))
    for i in range(n):
        y = 1 - (i / (n - 1)) * 2 if n > 1 else 0.0
        r_xy = math.sqrt(max(0.0, 1 - y * y))
        theta = golden_angle * i
        x = math.cos(theta) * r_xy
        z = math.sin(theta) * r_xy
        points.append((x * radius, y * radius, z * radius))
    return points


def radial_dipole(pos, strength):
    """Radially-aligned dipole -- matches P9's own configuration (the one
    MULTING's symmetric F_d derivation selects, per two_charge_completion.py)."""
    r = math.sqrt(sum(c**2 for c in pos))
    return tuple(strength * c / r for c in pos)


def nn_spacing_estimate(n, radius):
    """Order-of-magnitude nearest-neighbor spacing for N quasi-uniform points
    on a sphere: area/point ~ 4*pi*R^2/N, so characteristic spacing
    ~ R*sqrt(4*pi/N). Used only to set realistic separation-to-size ratios,
    not as a precise nearest-neighbor computation."""
    return radius * math.sqrt(4 * math.pi / n)


def total_energy(n, radius, p_strength, r_min_val):
    positions = fibonacci_sphere(n, radius)
    dipoles = [radial_dipole(pos, p_strength) for pos in positions]
    self_total = n * float(e_self(p_strength, r_min_val))
    cross_total = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            sep = tuple(positions[j][k] - positions[i][k] for k in range(3))
            cross_total += 2 * u_cross_numeric(dipoles[i], dipoles[j], sep)
    return self_total, cross_total, self_total + cross_total


def main() -> None:
    print("=" * 78)
    print("P16 -- DOES P15's RING RESULT TRANSFER TO THE ACTUAL P9 SPHERICAL SHELL?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    sphere_radius = 100.0
    p_total = 1000.0
    r_min_shrinking_base = 1.0

    print("\n[REGIME A' -- naive shrink, sphere version] p_i=p_total/N (total dipole")
    print("  moment conserved, as in P15's Regime A); r_min_i tied to the natural")
    print("  spacing decrease on a sphere (~1/sqrt(N), not ~1/N as on a ring -- a")
    print("  real geometric difference, handled explicitly here rather than reusing")
    print("  the ring's 1/N tie blindly).")
    base_spacing = nn_spacing_estimate(8, sphere_radius)
    for n in (8, 32, 128, 512):
        p_i = p_total / n
        r_min_i = r_min_shrinking_base * (nn_spacing_estimate(n, sphere_radius) / base_spacing)
        s, c, t = total_energy(n, sphere_radius, p_i, r_min_i)
        print(
            f"  N={n:4d}: self={s:+.6e}  cross={c:+.6e}  TOTAL={t:+.6e}  |total/self|={abs(t / s):.4f}"
        )
    print("  -> expect DIVERGE if the P15 pattern transfers (self-energy per element")
    print("     ~ p_i^2/r_min_i^3 grows as N grows, same mechanism as the ring case).")

    print("\n[REGIME C' -- r_min FIXED, sphere version] same p_i=p_total/N shrink, but")
    print("  r_min held fixed (a genuine physical core size, independent of N) --")
    print("  the sphere analog of P15's Regime C.")
    for n in (8, 32, 128, 512):
        p_i = p_total / n
        s, c, t = total_energy(n, sphere_radius, p_i, r_min_shrinking_base)
        nn = nn_spacing_estimate(n, sphere_radius)
        print(
            f"  N={n:4d}: self={s:+.6e}  cross={c:+.6e}  TOTAL={t:+.6e}  |total/self|={abs(t / s):.4f}"
            f"  (nn_spacing/r_min~{nn / r_min_shrinking_base:.1f})"
        )
    print("  -> expect self -> 0, cross -> some (bounded or growing) value, the")
    print("     OPPOSITE scaling from Regime A' -- if this transfers, dimension does")
    print("     not change the QUALITATIVE three-limit structure P15 found.")

    print("\n[REGIME B' -- REALISTIC, sphere version] p_i and r_min FIXED at real")
    print("  cluster values (P14/P15's own numbers), N and sphere radius grow")
    print("  together to hold the separation-to-size ratio fixed at 20:1.")
    k_over_mc2 = 1.7e-6
    r_cluster_mpc = 1.5
    u_i_mpc = k_over_mc2 * r_cluster_mpc
    m_cluster = 1.0
    p_realistic = u_i_mpc * m_cluster
    r_min_realistic = r_cluster_mpc
    sep_to_size_ratio = 20.0
    nn_target = sep_to_size_ratio * r_min_realistic

    for n in (8, 16, 32, 64, 128):
        # sphere radius s.t. nn_spacing_estimate(n, radius) == nn_target
        radius_n = nn_target / math.sqrt(4 * math.pi / n)
        s, c, t = total_energy(n, radius_n, p_realistic, r_min_realistic)
        ratio = abs(c / s)
        print(
            f"  N={n:4d}: self={s:+.6e}  cross={c:+.6e}  TOTAL={t:+.6e}  |total/self|={abs(t / s):.4f}"
            f"  cross/self={ratio:.3e}"
        )
    print("  -> if |total/self| stays close to 1 (cross/self stays small) as N grows")
    print("     at fixed separation-to-size ratio, P15's central result (self-energy")
    print("     SURVIVES/dominates for realistic discrete clusters) transfers to the")
    print("     actual P9-shell geometry class, not just the ring stand-in.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("This tests SELF-VS-CROSS FIELD-ENERGY scaling transfer across dimension.")
    print("It does NOT re-verify P9's own exterior-potential zero for a discrete")
    print("shell (a different calculation -- summing exterior POTENTIAL, not field")
    print("ENERGY -- not attempted here). See printed regime results above for the")
    print("actual outcome; do not assume transfer from P15's ring result alone.")


if __name__ == "__main__":
    main()
