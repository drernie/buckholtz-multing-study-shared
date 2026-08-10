"""xi_2: the quadrupolar component of the matter distribution around a halo pair.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10 · supplies item 2 of the shopping list in
FINDING_quadrupole_channel_kernels.md, without needing simulations.

WHY NO SIMULATION IS NEEDED AT LEADING ORDER. The density around halo A, given a
companion B at separation r, is at leading (Gaussian) order just the sum of the two
individual correlation contributions:

    <delta(x) | A at 0, B at r>  =  b [ xi(|x|) + xi(|x - r|) ]  +  (connected 3pt)

The first term is isotropic about A and contributes only to l = 0. **Every bit of
the quadrupole comes from the second term**, which is a known function of the
measured xi. So xi_2 follows from xi_0 by a projection:

    xi_l(s | r) = (2l+1)/2 * int_-1^1 xi( sqrt(s^2 + r^2 - 2 s r u) ) P_l(u) du

This is the leading term of the hierarchy, not the whole answer: the connected
three-point function adds a correction that this calculation does not contain and
cannot bound. Labelled accordingly wherever the result is used.

CONTROL WITH AN INDEPENDENTLY KNOWN ANSWER. Expanding the projection for s << r
gives, analytically,

    xi_2(s|r)  ->  (s^2/3) [ xi''(r) - xi'(r)/r ]

derived by Taylor-expanding the argument and projecting onto P_2 (the O(s^0) and
O(s^1) terms are annihilated by the projection). The numerical projection must
reproduce this. It is a real control: it tests the quadrature, the Legendre
convention and the geometry at once, against an answer obtained a different way.

THE TWO CUTOFFS, BOTH OF WHICH MATTER AND ARE THEREFORE MEASURED. The projection
samples xi from |s - r| up to s + r. The data (xi_zbin2.dat) run 3.69-262 Mpc, and
beyond ~230 Mpc they oscillate in sign at the 1e-4 level -- noise, not signal. Below
3.69 Mpc nothing is measured at all, and the s^5 weight in the kernel pushes the
integral toward s -> r where the sampled separation |x - r| -> 0. So both ends are
extrapolations, and the sensitivity to each is printed rather than assumed away.
"""

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy.special import eval_legendre

H_LITTLE = 0.6774
DATA = "experiments/20260802-ksz-force-law/artifacts/xi_zbin2.dat"
R_NOISE = 230.0  # Mpc: beyond this xi oscillates in sign at |xi| ~ 1e-4


def build_xi(r_max: float, slope: float | None):
    """xi(x) with an explicit choice at both ends.

    slope=None -> hold xi flat below the first data point; otherwise extrapolate as
    a power law x^slope. Above r_max, xi = 0.
    """
    d = np.loadtxt(DATA)
    r, x = d[:, 0] / H_LITTLE, d[:, 1]
    keep = r <= r_max
    r, x = r[keep], x[keep]
    lin = interp1d(r, x, bounds_error=False, fill_value=0.0)
    r0, x0 = r[0], x[0]

    def xi(s: float) -> float:
        if s >= r0:
            return float(lin(s))
        return x0 if slope is None else x0 * (s / r0) ** slope

    return xi, r0


def xi_l(xi, s: float, r: float, ell: int) -> float:
    """(2l+1)/2 * int du xi(|x - r|) P_l(u)  -- the anisotropy induced by the companion."""

    def f(u: float) -> float:
        return xi(np.sqrt(max(s * s + r * r - 2 * s * r * u, 0.0))) * eval_legendre(ell, u)

    return (2 * ell + 1) / 2 * quad(f, -1, 1, limit=400)[0]


def moments(xi, r: float, n_s: int = 120) -> tuple[float, float]:
    """(I3, I2) = int xi_2 s^3 ds and int xi_2 s^4 ds over 6..r.

    Evaluated on a fixed s-grid rather than by nesting quad inside quad: the nested
    version is O(10^5) inner integrations per row and does not finish. The grid is
    refined toward s -> r, where xi_2 rises steeply because the sampled separation
    to the companion goes to zero.
    """
    t = np.linspace(0.0, 1.0, n_s) ** 1.6  # denser near s = r
    s = 6.0 + (r - 6.0) * t
    v = np.array([xi_l(xi, float(x), r, 2) for x in s])
    return float(np.trapezoid(v * s**3, s)), float(np.trapezoid(v * s**4, s))


def main() -> None:
    xi, r0 = build_xi(R_NOISE, -1.8)
    print("=" * 78)
    print("xi_2 FROM THE CORRELATION FUNCTION (leading, Gaussian order)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)
    print(f"  xi data: {DATA}, used to {R_NOISE:.0f} Mpc; below {r0:.2f} Mpc extrapolated")

    # WHY the control uses an analytic xi instead of the data. A first version
    # differenced the measured xi to get xi'' and compared against that. It failed,
    # but the failure was in the CONTROL: the data are sampled every ~7.4 Mpc and
    # interpolated linearly, so a second derivative taken with h = 2 Mpc reads the
    # interpolant's own kinks, not the correlation function's curvature. A control
    # must test the machinery against a known answer -- so the known answer is
    # supplied analytically, and the data's smoothness is not part of the test.
    print("\n[CONTROL] projection vs its analytic small-s limit, on a power-law xi")
    print("  xi = A x^n  ->  xi_2 -> (s^2/3) A n(n-2) r^(n-2), exactly")
    print(f"  {'n':>6}{'r':>6}{'s':>6}{'numeric':>14}{'analytic':>14}{'ratio':>9}")
    okall = True
    for n in (-1.8, -2.5):

        def pw(x: float, n: float = n) -> float:
            return (x / 5.0) ** n

        for r in (60.0, 120.0):
            for s in (1.0, 3.0):
                num = xi_l(pw, s, r, 2)
                ana = s * s / 3 * n * (n - 2) * (r / 5.0) ** n / r**2
                okall &= abs(num / ana - 1) < 0.02
                print(f"  {n:>6.1f}{r:>6.0f}{s:>6.1f}{num:>14.4e}{ana:>14.4e}{num / ana:>9.4f}")
    print(f"  -> control {'PASSED' if okall else 'FAILED'} (agreement within 2%)")
    if not okall:
        print("  *** projection disagrees with its own analytic limit. STOP. ***")
        return

    print("\n[xi_2 PROFILE]  quadrupole of the pair environment, at three separations")
    print(f"  {'s/r':>6}" + "".join(f"{'r=' + str(int(q)):>15}" for q in (50, 100, 200)))
    for frac in (0.1, 0.3, 0.5, 0.7, 0.9, 0.99):
        row = "".join(f"{xi_l(xi, frac * q, q, 2):>15.4e}" for q in (50.0, 100.0, 200.0))
        print(f"  {frac:>6.2f}{row}")
    print("  -> xi_2 is positive and rises steeply toward s -> r: the quadrupole of the")
    print("     environment is dominated by matter near the companion, as it must be.")

    print("\n[KERNEL WEIGHTS]  the l=2 channel needs two moments of xi_2:")
    print("    I3(r) = int xi_2 s^3 ds   (k.m tier)      I2(r) = int xi_2 s^4 ds  (mass tier)")
    print("    fractional size of the dipole correction = ell_d * l/2 * I3/I2 = ell_d/<a>")
    print(f"\n  {'r [Mpc]':>9}{'I3':>13}{'I2':>13}{'<a> [Mpc]':>12}{'ell_d for 10% effect':>22}")
    for r in (50.0, 75.0, 100.0, 150.0, 200.0):
        i3, i2 = moments(xi, r)
        a_eff = i2 / i3
        print(f"  {r:>9.0f}{i3:>13.4e}{i2:>13.4e}{a_eff:>12.2f}{0.1 * a_eff:>22.2f}")

    print("\n[SENSITIVITY TO THE TWO EXTRAPOLATIONS]  r = 100 Mpc, <a> recomputed")
    for lab, rmax, slope in (
        ("baseline", R_NOISE, -1.8),
        ("steeper small-scale xi ~ s^-2.2", R_NOISE, -2.2),
        ("flat below the first point", R_NOISE, None),
        ("xi truncated at 150 Mpc", 150.0, -1.8),
        ("xi kept to 262 Mpc (noisy tail)", 262.0, -1.8),
    ):
        xj, _ = build_xi(rmax, slope)
        i3, i2 = moments(xj, 100.0)
        print(f"  {lab:<34} <a> = {i2 / i3:7.2f} Mpc")
    print("\n  -> if <a> is stable across these, the forecast below does not rest on")
    print("     an unmeasured part of xi; if it moves, it does, and that must be said.")


if __name__ == "__main__":
    main()
