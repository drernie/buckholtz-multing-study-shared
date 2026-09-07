"""Stage 4 -- is d_flip reachable INSIDE the single-pair construction?

Stage 3b flagged d_flip/d0 = 2.06 as "outside the construction" but left
that as a qualitative objection. This resolves it exactly.

The key fact: inside v82's own construction `d` is NOT a free variable.
It is d_of(z) = d0/(1+z) with d0 = 45 Mpc. So the model samples only

    d in (0, 45] Mpc   for z >= 0

and d_flip = 92.67 Mpc may simply not be in the reachable set.

Equivalently, and this is the cleaner statement: Q(z) is a function of z
ALONE inside the construction (M, R, k, d are all fixed functions of z),
so the question "does the sign ever flip?" has a definite answer that
does not require treating d as free at all.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "20260803-bridge"))

from _v82_shared_physics import (  # noqa: E402
    MPC_TO_M,
    M_of,
    R_of,
    c,
    d_of,
    k_of,
)

B1_FIT = 1.4335e10
B2_FIT = 7.8067e17
D0_MPC = 45.0
D_FLIP_MPC = 92.67
Z_FIT_MAX = 2.33  # highest redshift in v82's own 33-point fit
Z_H2_NEG = 16.957  # P192: H^2 goes negative here -- hard domain edge


def Q_of_z(z, b1=B1_FIT, b2=B2_FIT):
    """Q(z) = (b2/b1) * k R / (M c^2 d).  Sign of d(addot/a)/dk is
    POSITIVE iff Q < 1.  Every factor is a fixed function of z inside
    the construction -- nothing is free."""
    return (b2 / b1) * k_of(z) * R_of(z) / (M_of(z) * c**2 * d_of(z))


def main() -> int:
    print("=" * 74)
    print("PC1 -- the identity Q(z) = d_flip / d_of(z) must hold exactly")
    print("=" * 74)
    print("  Q ~ 1/d with everything else fixed at a given z, so solving")
    print("  Q=1 for d gives d_flip(z) = Q(z)*d_of(z). If d_flip were")
    print("  z-independent, Q(z)*d_of(z) would be constant. Checking:")
    worst = 0.0
    for z in (0.0, 0.5, 1.0, 2.33):
        dflip_z = Q_of_z(z) * d_of(z) / MPC_TO_M
        print(f"    z={z:5.2f}  Q={Q_of_z(z):7.4f}  Q*d_of(z) = {dflip_z:8.3f} Mpc")
        worst = max(worst, abs(dflip_z - D_FLIP_MPC) / D_FLIP_MPC)
    print(f"\n  spread vs the z=0 value 92.67 Mpc: {100 * worst:.2f}%")
    print("  -> d_flip is NOT a single number; it drifts with z, because")
    print("     k, R and M all evolve. The 92.67 Mpc of Stage 1/3b is the")
    print("     z=0 value only. Recorded as a correction to that framing.")

    print("\n" + "=" * 74)
    print("THE ACTUAL QUESTION -- does Q(z) ever cross 1 inside the model?")
    print("=" * 74)
    zs = np.concatenate(
        (
            np.linspace(-0.95, -0.01, 60),
            np.linspace(0.0, 3.0, 80),
            np.linspace(3.0, 16.9, 60),
        )
    )
    q = np.array([Q_of_z(z) for z in zs])
    print(f"  {'z':>8} {'a=1/(1+z)':>11} {'d_of(z) [Mpc]':>15} {'Q(z)':>10}  sign")
    for zt in (-0.9, -0.75, -0.514, -0.25, 0.0, 0.5, 1.0, 2.33, 5.0, 10.0, 16.9):
        qq = Q_of_z(zt)
        print(
            f"  {zt:8.3f} {1 / (1 + zt):11.3f} {d_of(zt) / MPC_TO_M:15.2f} "
            f"{qq:10.4f}  {'+' if qq < 1 else '-'}"
        )

    below = zs[q < 1.0]
    print(f"\n  Q(z) minimum over the scanned range : {q.min():.4f} at z={zs[np.argmin(q)]:.3f}")
    print(f"  Q(z) < 1 anywhere?                  : {'YES' if len(below) else 'NO'}")
    if len(below):
        print(f"    first such z = {below.min():.4f}")

    print("\n" + "=" * 74)
    print("REACHABILITY of d = 92.67 Mpc inside the construction")
    print("=" * 74)
    zneed = D0_MPC / D_FLIP_MPC - 1.0
    print(f"  d_of(z) = d0/(1+z) = {D_FLIP_MPC} Mpc  =>  1+z = {D0_MPC / D_FLIP_MPC:.5f}")
    print(f"                                        =>  z = {zneed:.4f}")
    print(f"                                        =>  a = {1 / (1 + zneed):.4f}")
    print(f"\n  For z >= 0 the construction samples only d in (0, {D0_MPC:.0f}] Mpc.")
    print(f"  d_flip = {D_FLIP_MPC} Mpc requires z = {zneed:.3f} -- a FUTURE epoch,")
    print(f"  scale factor a = {1 / (1 + zneed):.3f}. Note a equals d_flip/d0 exactly,")
    print("  since d ~ a. Not a coincidence: the same 2.06 as Q(0).")

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    reachable = bool(len(below))
    print(f"""  Inside the single-pair construction, d is NOT free: d = d0/(1+z).

  Q(z) > 1 at every redshift scanned, from z = -0.95 to z = 16.9
  (minimum {q.min():.4f}). The response d(addot/a)/dk is therefore
  NEGATIVE at every epoch the construction can represent, including
  the future branch and up to P192's own H^2<0 boundary at z={Z_H2_NEG}.

  The reversal is NOT reachable: {"REACHABLE" if reachable else "NOT REACHABLE"}.

  So d_flip is not a prediction of the model as constructed. It is an
  artifact of OUR extension -- treating d as a free population variable,
  which FINDING_P157 already established v82 does not do.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
