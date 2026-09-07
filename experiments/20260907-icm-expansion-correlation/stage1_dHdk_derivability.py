"""Stage 1 -- is d(addot/a)/dk derivable without resolving bottleneck 1?

The claim.md verdict was REFUSE(no_falsifiable_predicate_yet): MULTING's
corpus states no quantitative version of "local expansion responds to
thermal energy." This script asks the narrower, cheaper question that
gates the whole route:

    Which parts of the response -- SIGN, RADIAL LAW, MAGNITUDE -- can be
    read off the force law WITHOUT the absolute F->H(z) normalisation
    that bottleneck 1 blocks?

Method: differentiate TJB's own force law analytically w.r.t. k, verify
against finite differences on the REAL kernel (positive control), check
a mechanism-free limit gives exactly zero (negative control), then
evaluate the sign at TJB's own published fit.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "20260803-bridge"))

from _v82_shared_physics import (  # noqa: E402
    MPC_TO_M,
    F_accretion,
    G,
    M_of,
    R_of,
    c,
    d_of,
    k_of,
)

# TJB's own real fit point (spotlighted row, Table II) -- verbatim from
# P190, which took it verbatim from P176.
B1_FIT = 1.4335e10
B2_FIT = 7.8067e17


def addot_over_a_k(z, b1, b2, k):
    """TJB's own addot_over_a with k passed EXPLICITLY instead of taken
    from k_of(z). k = k_of(z) reproduces the published law exactly."""
    M, R, d = M_of(z), R_of(z), d_of(z)
    F0 = (-G) * M * M / d**2
    F1 = b1 * (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2
    F2 = b2 * (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2
    return ((F0 - F1 + F2 - F_accretion(z)) / (M / 2.0)) / d


def d_addot_dk_analytic(z, b1, b2, k):
    """d(addot/a)/dk, derived by hand:

    addot/a = [F0 - F1 + F2 - F_acc] * 2 / (M d)
    dF1/dk  = -G b1 2 M R / (c^2 d^3)
    dF2/dk  = -G b2 2 k R^2 / (c^4 d^4)
    =>  d(addot/a)/dk = 4G[ b1 R/(c^2 d^4) - b2 k R^2/(M c^4 d^5) ]
    """
    M, R, d = M_of(z), R_of(z), d_of(z)
    dip = 4.0 * G * b1 * R / (c**2 * d**4)
    quad = -4.0 * G * b2 * k * R * R / (M * c**4 * d**5)
    return dip, quad, dip + quad


def q_discriminant(z, b1, b2, k):
    """Q := (b2/b1) * k R / (M c^2 d).

    FIX 1 (Step 8a skeptic, 2026-09-07). The original docstring read
    "Sign is POSITIVE iff Q < 1" with no condition. That is FALSE for
    b1 < 0 and UNDEFINED for b1 = 0. Original wording kept here so the
    correction is visible.

    The exact statement is

        d(addot/a)/dk = [4G R/(c^2 d^4)] * ( b1 - b2 k R/(M c^2 d) )
        => sign = sign( b1 - b2 k R/(M c^2 d) ),  NOT sign(1 - Q)

    and the two coincide only for b1 > 0. Verified counterexample, z=0,
    b1 = -1.4335e10, b2 = +7.8067e17:
        Q      = -2.0594  (so Q < 1, the old wording predicts '+')
        actual = -1.4215e-90  ->  '-'

    So: sign is POSITIVE iff Q < 1 **AND b1 > 0**.
    """
    if b1 == 0.0:
        raise ValueError("Q is undefined at b1 = 0; use sign_of_response() instead")
    M, R, d = M_of(z), R_of(z), d_of(z)
    return (b2 / b1) * k * R / (M * c**2 * d)


def sign_of_response(z, b1, b2, k):
    """Sign of d(addot/a)/dk, valid for ANY b1 including 0 and negative.

    Added by FIX 1 -- this is what q_discriminant should have been, and
    what any caller outside the fitted b1>0 regime must use.
    """
    M, R, d = M_of(z), R_of(z), d_of(z)
    return float(np.sign(b1 - b2 * k * R / (M * c**2 * d)))


ZS = [0.0, 0.07, 0.25, 0.5, 1.0, 1.5, 1.965, 2.33]


def main() -> int:
    print("=" * 74)
    print("PC1 -- analytic derivative vs finite difference on the REAL kernel")
    print("=" * 74)
    worst = 0.0
    for z in ZS:
        k0 = k_of(z)
        h = 1e-6 * k0
        fd = (
            addot_over_a_k(z, B1_FIT, B2_FIT, k0 + h) - addot_over_a_k(z, B1_FIT, B2_FIT, k0 - h)
        ) / (2 * h)
        _, _, an = d_addot_dk_analytic(z, B1_FIT, B2_FIT, k0)
        rel = abs(fd - an) / abs(an)
        worst = max(worst, rel)
        print(f"  z={z:6.3f}  analytic={an:+.6e}  fd={fd:+.6e}  rel_err={rel:.2e}")
    print(f"\n  worst relative error: {worst:.3e}  ->  {'PASS' if worst < 1e-6 else 'FAIL'}")
    if worst >= 1e-6:
        return 1

    print("\n" + "=" * 74)
    print("NC1 -- mechanism removed (b1=b2=0): response must be EXACTLY zero")
    print("=" * 74)
    for z in (0.0, 1.0, 2.33):
        _, _, an = d_addot_dk_analytic(z, 0.0, 0.0, k_of(z))
        k0 = k_of(z)
        fd = (addot_over_a_k(z, 0.0, 0.0, k0 * 1.5) - addot_over_a_k(z, 0.0, 0.0, k0 * 0.5)) / (k0)
        print(f"  z={z:5.2f}  analytic={an:+.3e}  fd_over_wide_range={fd:+.3e}")
        if an != 0.0 or fd != 0.0:
            print("  FAIL -- k leaks into a mechanism-free construction")
            return 1
    print("  PASS -- exactly zero, both analytically and numerically")

    print("\n" + "=" * 74)
    print(f"SIGN at TJB's own published fit (b1={B1_FIT:.4e}, b2={B2_FIT:.4e})")
    print("=" * 74)
    print(f"  {'z':>6}  {'dipole(+)':>13}  {'quad(-)':>13}  {'total':>13}  {'Q':>8}  sign")
    signs = []
    for z in ZS:
        k0 = k_of(z)
        dip, quad, tot = d_addot_dk_analytic(z, B1_FIT, B2_FIT, k0)
        Q = q_discriminant(z, B1_FIT, B2_FIT, k0)
        s = "+" if tot > 0 else "-"
        signs.append(s)
        print(f"  {z:6.3f}  {dip:+13.4e}  {quad:+13.4e}  {tot:+13.4e}  {Q:8.4f}  {s}")

    print("\n  Q := (b2/b1) * k R / (M c^2 d);  total > 0  <=>  Q < 1")
    print(f"  signs across z: {''.join(signs)}")
    print(
        f"  Q range: {min(q_discriminant(z, B1_FIT, B2_FIT, k_of(z)) for z in ZS):.4f}"
        f" .. {max(q_discriminant(z, B1_FIT, B2_FIT, k_of(z)) for z in ZS):.4f}"
    )

    print("\n" + "=" * 74)
    print("RADIAL LAW -- d treated as a free variable, not d_of(z)")
    print("  *** THIS SECTION IS OUR EXTENSION, NOT THE MODEL (FIX 6) ***")
    print("  Stage 4 later claimed 'd is not a free variable in this")
    print("  construction'. The skeptic correctly pointed out that THIS")
    print("  very block treats it as free, and that the 92.67 Mpc figure")
    print("  comes from here. Both are true and not in conflict once")
    print("  stated properly: the MODEL never varies d independently;")
    print("  WE do, here, as a labelled extension. Numbers below are")
    print("  ours, not MULTING's.")
    print("=" * 74)
    print("  dipole contribution  ~ b1 R / d^4      (slope -4)")
    print("  quad   contribution  ~ b2 k R^2 / d^5  (slope -5)")
    print("  => effective slope is a MIX, set by which term dominates,")
    print("     i.e. by Q(d) which itself scales as 1/d.\n")
    z0 = 0.0
    k0, M, R = k_of(z0), M_of(z0), R_of(z0)
    print(f"  {'d [Mpc]':>10}  {'Q':>10}  sign")
    for d_mpc in (5.0, 10.0, 22.5, 45.0, 90.0, 180.0):
        d = d_mpc * MPC_TO_M
        dip = 4.0 * G * B1_FIT * R / (c**2 * d**4)
        quad = -4.0 * G * B2_FIT * k0 * R * R / (M * c**4 * d**5)
        Q = (B2_FIT / B1_FIT) * k0 * R / (M * c**2 * d)
        print(f"  {d_mpc:10.1f}  {Q:10.4f}  {'+' if dip + quad > 0 else '-'}")

    print("\n" + "=" * 74)
    print("NORMALISATION-DEPENDENCE VERDICT")
    print("=" * 74)
    print("  SIGN        : depends on b2/b1  -> NOT normalisation-free")
    print("  RADIAL LAW  : mix of d^-4 and d^-5, weighted by Q(d) -> NOT free")
    print("  MAGNITUDE   : needs b1, b2 absolutely             -> NOT free")
    print("\n  All three inherit the beta-calibration. The response is NOT")
    print("  structurally determined; it is a fitted quantity.")
    print()
    print("  FIX 2 (Step 8a skeptic) -- WHAT THIS RESPONSE IS, AND IS NOT:")
    print("  d(addot/a)/dk has units s^-2 per Joule. It is the response of")
    print("  ACCELERATION. Any sentence of the form 'more thermal energy")
    print("  means less local EXPANSION' is about H (s^-1) and DOES NOT")
    print("  FOLLOW without integrating over history and initial")
    print("  conditions. That inference is WITHDRAWN wherever this")
    print("  experiment made it. stage3b calls this exact move a CATEGORY")
    print("  ERROR for a different pair of quantities -- it is the same")
    print("  move here, in the opposite direction.")
    print()
    print("  FIX 3 -- PARTIAL vs TOTAL. Everything above is the PARTIAL")
    print("  derivative at fixed M, R, d. Inside the construction k cannot")
    print("  move alone, so the realisable quantity is the TOTAL derivative")
    print("  along the trajectory. Measured at z=0:")
    print("      partial = -4.9224e-91      total = -9.3492e-92")
    print("      ratio   = 5.265x           same sign")
    print("  The DIRECTION survives; the MAGNITUDE quoted must say which.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
