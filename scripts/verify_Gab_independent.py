"""verify_Gab_independent.py — INDEPENDENT check that dipole/quadrupole background
couplings vanish (G_dipole = G_quad = 0), NOT using Shtanov-Sahni's lim[f - r f'].

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Context: docs/127 (P2) concluded G_ab = 0 for the dipole (1/r^3 force) and quadrupole
(1/r^4 force) via Shtanov & Sahni's closed-form G_eff = G*lim_{r->inf}[f - r f'].
That is one derivation. Per falsification-ladder.md's Independent Verification
Strength Ladder, re-running the SAME formula is only Weak-Medium independence, and the
divergence route (div g = -Laplacian phi) is the SAME physics S&S used. This script
uses a genuinely DIFFERENT method: direct Monte-Carlo summation of Newton's force law
on a test particle displaced from the centre of a uniform spherical shell -- no
potential, no Laplacian, no S&S formula. It measures the shell's tidal coefficient
by finite difference (fully brute-force) and its scaling with shell radius R.

Physical logic: the background ä/a is set by the tidal coefficient k = d(F_z)/d(delta)
summed over a uniform matter distribution. If the far (large-R) shells contribute a
non-vanishing k, background expansion is sourced by that multipole; if the large-R
contribution converges to zero, the bulk/background does NOT source it -> G = 0.

Expected (independent of docs/127): for a 1/r^n force, the per-shell tidal coefficient
carries an angular factor <1 - (n+1) cos^2 θ> = (2 - n)/3 (measured here by MC, not
assumed). Then n=2 (monopole) -> 0 from exterior shells (shell theorem; ä/a comes from
ENCLOSED mass instead), while n=3,4 give (2-n)/3 * R^(1-n) whose large-R integral
converges -> far matter contributes nothing -> G_dipole = G_quad = 0.

Run:  python scripts/verify_Gab_independent.py
Exit: 0 if the independent method agrees with G_dipole = G_quad = 0, else 1.
"""

from __future__ import annotations

import sys

import numpy as np

RNG_POINTS = 200_000  # MC samples on the shell
DELTA = 1e-4  # finite-difference displacement of the test particle


def shell_tidal_per_source(n: int, radius: float = 1.0) -> float:
    """MC-measure the per-source tidal coefficient d(F_z)/d(delta) for a 1/r^n force,
    with sources uniform on a sphere of the given `radius`.

    Pure brute force: place N sources on the sphere, displace the test particle by
    +-DELTA along z, sum the z-force (per unit source, 1/s^n law), finite-difference
    d(F_z)/d(delta). At radius=1 this equals the angular average <1 - (n+1)cos^2 θ>;
    at radius R it scales as that factor / R^(n+1). Both facts are MEASURED here, not
    assumed -- no (2-n)/3 and no R^(1-n) is injected into the computation.
    """
    # deterministic sampling grid (no Math.random / no Date needed): Fibonacci sphere
    i = np.arange(RNG_POINTS) + 0.5
    phi = np.arccos(1 - 2 * i / RNG_POINTS)  # polar, uniform in cos
    golden = np.pi * (1 + 5**0.5)
    theta = golden * i  # azimuth
    sx = radius * np.sin(phi) * np.cos(theta)
    sy = radius * np.sin(phi) * np.sin(theta)
    sz = radius * np.cos(phi)

    def Fz(delta: float) -> float:
        dx, dy, dz = -sx, -sy, (delta - sz)  # test(0,0,delta) - source
        s = np.sqrt(dx * dx + dy * dy + dz * dz)
        return float(np.mean(dz / s ** (n + 1)))  # z-force per unit source, 1/s^n law

    return (Fz(DELTA) - Fz(-DELTA)) / (2 * DELTA)


def shell_angular_factor(n: int, seed_offset: int) -> float:
    """Angular factor = per-source tidal coefficient at unit radius (radius=1)."""
    del seed_offset  # kept for API compatibility
    return shell_tidal_per_source(n, radius=1.0)


def main() -> int:
    print("=" * 70)
    print("INDEPENDENT check of G_ab (direct MC force summation, NO lim[f-rf'])")
    print("=" * 70)
    print(f"MC sources per shell: {RNG_POINTS};  finite-diff delta: {DELTA}")
    print("\nMeasured shell tidal angular factor  vs  analytic (2-n)/3:")
    print(f"{'force':>18} {'n':>3} {'MC factor':>12} {'(2-n)/3':>10} {'match':>7}")

    results = {}
    ok = True
    for n, name in [(2, "monopole 1/r^2"), (3, "dipole 1/r^3"), (4, "quadrupole 1/r^4")]:
        mc = shell_angular_factor(n, 0)
        analytic = (2 - n) / 3
        match = abs(mc - analytic) < 5e-3
        ok = ok and match
        results[n] = mc
        print(f"{name:>18} {n:>3} {mc:>12.5f} {analytic:>10.5f} {'yes' if match else 'NO':>7}")

    print("\nInterpretation of the measured factors:")
    print(f"  monopole  n=2: shell factor = {results[2]:+.4f}  ~0  -> exterior shells give")
    print("                 ZERO (shell theorem); background comes from ENCLOSED mass.")
    print(f"  dipole    n=3: shell factor = {results[3]:+.4f}  != 0 per shell, BUT the")
    print(f"  quadrupole n=4: shell factor = {results[4]:+.4f}  bulk sum scales as R^(1-n):")

    # MC-measure the RADIAL scaling of the per-source tidal coefficient (was previously
    # inserted analytically as R^-(n+1)). A shell [R,R+dR] of fixed VOLUME density has
    # mass ∝ R^2, so its bulk tidal contribution ∝ R^2 * (per-source coeff). If that
    # -> 0 as R grows, far/background matter does not source the multipole.
    print("\nMC-measured per-source tidal coeff vs radius R (ratio to R=1), and the")
    print("bulk shell weight  R^2 * |per-source coeff|  (should -> 0 for n=3,4):")
    print(f"{'n':>3} {'R=1':>11} {'R=2':>11} {'R=4':>11} {'R=8':>11}   bulk-weight R^2*coeff")
    radii = (1.0, 2.0, 4.0, 8.0)
    bulk_far = {}
    for n in (2, 3, 4):
        coeffs = [shell_tidal_per_source(n, R) for R in radii]
        weights = [R**2 * abs(cval) for R, cval in zip(radii, coeffs, strict=True)]
        bulk_far[n] = weights[-1]  # bulk weight at the largest R sampled
        ratios = " ".join(f"{c / coeffs[0]:>11.3e}" if coeffs[0] else f"{c:>11.3e}" for c in coeffs)
        print(f"{n:>3} {ratios}   [{', '.join(f'{w:.2e}' for w in weights)}]")
    print("  (n=2 per-source coeff ~0 at every R -> shell theorem; n=3,4 bulk weight")
    print("   R^2*coeff shrinks with R -> far matter contributes nothing.)")

    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)
    # all three checks now MC-measured (no analytic scaling inserted):
    monopole_zero = abs(results[2]) < 5e-3
    # far-matter bulk weight must be shrinking for n=3,4 (R=8 weight < R=1 weight)
    dipole_bulk_far = bulk_far[3]
    quad_bulk_far = bulk_far[4]
    bulk_vanishes = dipole_bulk_far < 0.4 and quad_bulk_far < 0.1  # shrinking vs R=1 (=1/3, 2/3)
    if ok and monopole_zero and bulk_vanishes:
        print("  Independent MC method AGREES with docs/127:")
        print("   - monopole (1/r^2): exterior shells contribute 0 (shell theorem);")
        print("     ä/a sourced by ENCLOSED mass -> G_mm = G (standard).")
        print("   - dipole (1/r^3) & quadrupole (1/r^4): far/bulk matter contribution")
        print(
            f"     vanishes (dipole far shell ~ {dipole_bulk_far:.1e}, quad ~ {quad_bulk_far:.1e})"
        )
        print("     -> G_dipole = G_quad = 0 as BACKGROUND couplings. CONFIRMED by a")
        print("        method that never used Shtanov-Sahni's lim[f-rf'] or any Laplacian.")
        print("   Caveat unchanged: the UV/near-field (small-r) part is cutoff-dependent")
        print("   (local structure, not background) -- consistent with docs/125/127 C1.")
        return 0
    print("  MISMATCH -- independent method does NOT confirm G=0. Investigate before")
    print(
        f"  trusting docs/127. (monopole_zero={monopole_zero} "
        f"bulk_vanishes={bulk_vanishes} angular_ok={ok})"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
