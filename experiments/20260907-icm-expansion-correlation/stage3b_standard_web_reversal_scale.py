"""Stage 3b -- at what scale does the STANDARD picture reverse, and is it
the same derivative MULTING reverses?

Stage 1 found MULTING-at-TJB's-fit flips the sign of d(addot/a)/dk at
d_flip = 92.67 Mpc. The obvious comparison is the turnaround radius --
"the scale where the attraction due to its mass is balanced by the
repulsion due to dark energy" (Bhattacharya, Dialektopoulos, Romano,
Skordis & Tomaras, arXiv:1611.05055, abstract).

But that comparison is a CATEGORY ERROR, and this script's main job is to
show it is one, not to perform it:

    MULTING flips   d(addot/a)/dk   -- the RESPONSE to thermal energy
    turnaround is   addot/a = 0     -- the QUANTITY itself

Different derivatives. The correct comparison is response-to-response.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "20260803-bridge"))

from _v82_shared_physics import (  # noqa: E402
    MPC_TO_M,
    G,
    H0_planck_si,
    M_of,
    OL_planck,
    R_of,
)

D_FLIP_MPC = 92.67  # Stage 1, at TJB's own fit


def r_turnaround_max(mass_kg: float) -> float:
    """r_ta,max = (3GM/(Lambda c^2))^(1/3);  Lambda c^2 = 3 OL H0^2
    => r_ta,max = (G M / (OL H0^2))^(1/3)."""
    return (G * mass_kg / (OL_planck * H0_planck_si**2)) ** (1.0 / 3.0)


def main() -> int:
    M0 = M_of(0.0)
    print("=" * 74)
    print("1. TURNAROUND SCALE for TJB's own node mass")
    print("=" * 74)
    print(f"  M0                 = {M0:.4e} kg = {M0 / 1.98847e30:.3e} Msun")
    print(f"  R500 (kernel)      = {R_of(0.0) / MPC_TO_M:.3f} Mpc")
    for label, m in (("one node  M0", M0), ("pair     2*M0", 2 * M0)):
        r = r_turnaround_max(m)
        print(f"  r_ta,max({label}) = {r / MPC_TO_M:7.3f} Mpc")
    r_pair = r_turnaround_max(2 * M0) / MPC_TO_M
    print(f"\n  MULTING d_flip     = {D_FLIP_MPC:7.3f} Mpc")
    print(f"  ratio d_flip / r_ta,max(pair) = {D_FLIP_MPC / r_pair:.2f}x")

    print("\n" + "=" * 74)
    print("2. BUT THIS IS THE WRONG COMPARISON -- different derivatives")
    print("=" * 74)
    print("""  Point mass M in a Lambda background, test particle at r:

      rddot/r = -G M / r^3 + Lambda c^2 / 3

  QUANTITY reverses at r_ta = (3GM/Lambda c^2)^(1/3)   <- computed above
  RESPONSE to mass:   d(rddot/r)/dM = -G / r^3

  The response is NEGATIVE FOR ALL r AND NEVER CHANGES SIGN.
  It decays as 1/r^3; it does not flip. So in the uncompensated
  point-mass + Lambda picture the standard response has NO reversal
  at any scale -- there is nothing to compare d_flip against.""")

    print("=" * 74)
    print("3. WHY MULTING HAS ONE AND THE POINT-MASS MODEL DOES NOT")
    print("=" * 74)
    print("""  MULTING's response has TWO terms of OPPOSITE sign and DIFFERENT
  radial slopes:

      dipole      + b1 R   / (c^2 d^4)     ~ d^-4   (repulsive)
      quadrupole  - b2 k R^2/(M c^4 d^5)   ~ d^-5   (attractive)

  The attractive term falls FASTER, so it dominates at small d and
  loses at large d -- hence exactly one crossing. The standard
  point-mass response has a single term and therefore no crossing.

  The reversal is a STRUCTURAL consequence of having two tiers with
  different powers of d, not a tuned coincidence.""")

    print("=" * 74)
    print("4. THE LIVE UNKNOWN -- compensation")
    print("=" * 74)
    print("""  A real cosmic-web overdensity is COMPENSATED: mass gathered into a
  knot leaves its surroundings underdense, and underdense regions
  expand FASTER than average (Bolejko, Nazer & Wiltshire,
  arXiv:1512.07364). A compensated perturbation can therefore give a
  POSITIVE d(H_local)/dM outside its compensation radius -- i.e. a
  reversal of its own, from ordinary physics.

  [UNKNOWN] at what scale. That scale, not r_ta, is the number that
  must be compared with 92.67 Mpc. It is set by the compensation
  radius of the structure, not by the Lambda balance.""")

    print("=" * 74)
    print("5. INTERNAL CONSISTENCY -- where does d_flip sit vs the model's OWN scale?")
    print("=" * 74)
    d0_mpc = 45.0
    n_implied = (1.0 / d0_mpc) ** 3
    print(f"  TJB's own node separation d0        = {d0_mpc:.2f} Mpc")
    print(f"  implied node number density n=1/d0^3 = {n_implied:.3e} Mpc^-3")
    print(f"  MULTING d_flip                       = {D_FLIP_MPC:.2f} Mpc")
    print(f"  d_flip / d0                          = {D_FLIP_MPC / d0_mpc:.2f}x")
    print(
        """
  d_flip sits at MORE THAN TWICE the model's own node separation. At
  that distance a "representative pair" has other nodes between its
  members -- FINDING_P157 already established that v82 evaluates ONE
  representative pair, not a population, so the single-pair picture is
  not valid there.

  A compensated standard structure, by contrast, cannot compensate
  beyond roughly half the mean separation to its neighbours (past that
  you are inside the next cell), i.e. [INFERRED] <~ d0/2 = %.1f Mpc.

  So the two reversals plausibly sit on OPPOSITE sides of d0 -- but
  MULTING's own lands where its own construction does not hold."""
        % (d0_mpc / 2)
    )

    print("=" * 74)
    print("VERDICT")
    print("=" * 74)
    print(f"""  r_ta,max(pair) = {r_pair:.2f} Mpc is {D_FLIP_MPC / r_pair:.1f}x below d_flip, BUT it answers
  a different question and must NOT be quoted as the floor's reversal.

  Uncompensated standard response: NO reversal -> shape IS discriminating.
  Compensated standard response:   reversal scale [UNKNOWN] -> undecided.

  Stage 3's CRITERION_INVALID verdict on the MONOTONE test stands.
  The SHAPE test is NOT yet criterion-invalid, and is not yet valid either.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
