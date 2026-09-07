"""Stage 4 -- is d_flip reachable INSIDE the single-pair construction?

Stage 3b flagged d_flip/d0 = 2.06 as "outside the construction" but left
that as a qualitative objection. This resolves it exactly.

The key fact: inside v82's own construction `d` is NOT a free variable.
It is d_of(z) = d0/(1+z) with d0 = 45 Mpc.

[SUPERSEDED BY FIX 7, kept so the correction is visible] This docstring
originally continued: "So the model samples only d in (0, 45] Mpc for
z >= 0, and d_flip = 92.67 Mpc may simply not be in the reachable set."
That reachability argument is WRONG and is withdrawn: this script itself
scans down to z = -0.95, where d_of = 900 Mpc, so 92.67 Mpc IS reached,
at z = -0.5144. The conclusion survives for a different reason -- see
below and FIX 7 in the output.

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
    print("  ^ FIX 8: that location is a GRID NODE artifact. np.linspace(0,3,80)")
    print("    has step 3/79 = 0.0379747 and node 38 lands on 1.44304.")
    print("    Closed form: Q ~ u^-0.6426667 * (0.315u^3+0.685)^0.2466667,")
    print("    dQ/du = 0 at u^3 = 14.35834 => u* = 2.430533, z* = 1.430533.")
    print("    Independently confirmed by scipy minimize_scalar: z = 1.430532.")
    print("    The VALUE is unaffected (1.74835 vs 1.7484, sixth digit) --")
    print("    only the reported location moves by dz = 0.0125.")
    print("  ^ FIX 9: Q -> +inf at BOTH ends (u^-0.6427 as u->0+, u^+0.0973")
    print("    as u->inf) with a single stationary point, so 1.7484 is the")
    print("    GLOBAL minimum on all of (-1, inf) -- not merely on the")
    print("    scanned window. The claim was WEAKER than its own code shows.")
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
    print()
    print("  " + "-" * 68)
    print("  FIX 7 (Step 8a skeptic) -- THE ABOVE FRAMING WAS INCONSISTENT")
    print("  " + "-" * 68)
    print("  'Only d in (0, 45]' is true for z >= 0, but THIS SCRIPT scans")
    print("  down to z = -0.95, where d_of = 45/0.05 = 900 Mpc. Over its own")
    print("  scan the reachable set is (0, 900] Mpc, so d = 92.67 Mpc IS")
    print(f"  reachable, at z = {zneed:.4f}. The unreachability argument fails.")
    print()
    print("  THE REAL REASON, which does hold: at that very epoch")
    print(f"      Q({zneed:.4f}) = {Q_of_z(zneed):.4f}  >>  1")
    print("  because k, R and M moved along with d. So 'd_flip is not")
    print("  derivable' follows from Q(z) > 1 EVERYWHERE -- not from d")
    print("  being unreachable. The original 'so' was a non sequitur:")
    print("  the conclusion was right, the stated reason was not.")

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    flips = bool(len(below))
    print(f"""  Inside the single-pair construction, d is NOT free: d = d0/(1+z).

  Q(z) > 1 at EVERY z where the model is defined -- global minimum
  {q.min():.4f}, not merely a scanned-window minimum (FIX 9). So the
  ACCELERATION response d(addot/a)/dk is negative at every epoch the
  construction can represent, including the future branch and up to
  P192's own H^2<0 boundary at z={Z_H2_NEG}.

  Sign ever flips inside the model: {"YES" if flips else "NO"}.

  So d_flip is not a prediction of the model as constructed. It is an
  artifact of OUR extension -- treating d as a free population variable,
  which FINDING_P157 already established v82 does not do.

  FIX 7 restates WHY, because the original reason was wrong: not because
  d = 92.67 Mpc is unreachable (it is reachable, at z = -0.5144), but
  because Q > 1 THERE TOO -- k, R and M move with d. The conclusion held;
  the argument for it did not.

  FIX 2 restates WHAT: this is the response of ACCELERATION (s^-2 J^-1).
  No statement about the EXPANSION RATE H follows from it without
  integrating over history. Sentences of the form 'more thermal energy
  means less expansion' are withdrawn from this experiment.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
