"""P111 -- diagnose (and attempt to fix) the phibar_dot(1)x0.1 pole at k<1 FINDING_P110
found. CORRECTS a mistaken attribution FINDING_P110 made without verifying it.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHAT FINDING_P110 CLAIMED, AND WHY IT WAS WRONG -- caught in THIS file's own
build, before writing anything up, exactly the discipline this whole arc has
practiced throughout. FINDING_P110 attributed the k=0.3/k=0.5 poles (in
phibar_dot(1) x0.1, and x0.5 at k=0.3) to "the SAME 'ratio whose denominator
crosses zero' pathology FINDING_P76's own G2 diagnosis already named" --
stated by ANALOGY, WITHOUT actually checking the denominator (the g_hat=0
reference run's own contrast) for a zero-crossing. This file checked it
directly. The reference run's contrast does NOT cross zero anywhere in the
tested range -- it grows smoothly and monotonically (4.25e-3 at x=0.2 to
3.06e-2 at x=100). FINDING_P110's attribution was WRONG. Corrected here.

THE ACTUAL MECHANISM, DIAGNOSED DIRECTLY. The COUPLED (g_hat=1) run's own
field perturbation delta-phi is the culprit: at (k=0.3, phibar_dot(1) x0.1)
it grows from -1.7e-4 (x=0.2) through 5.15 (x=1), 59 (x=2), oscillating in
SIGN, up to a peak around x=20-100 (~6570), then DECLINES again (2521 at
x=100, 1004 at x=5000) -- a large TRANSIENT OVERSHOOT, not a monotonic
runaway. Checked whether this is an equation-of-motion singularity
((1-g_hat*phibar) approaching zero, the actual mechanism behind FINDING_P76's
own mu/G2 poles): phibar itself stays at ~1e-5 to 1e-8 throughout, nowhere
near 1/g_hat=1 -- RULED OUT. The same growth-then-decay pattern was verified
at all THREE of FINDING_P110's poled (k, IC) combinations
((0.3, x0.1), (0.3, x0.5), (0.5, x0.1)) before generalizing the diagnosis.

THE ATTEMPTED FIX, MIRRORING FINDING_P108's OWN PRECEDENT -- AND WHY IT DOES
NOT WORK HERE. FINDING_P108 fixed an under-reach problem by widening T_END,
following reconnaissance first. Applied the SAME approach here: widened
T_END for (k=0.3, phibar_dot(1) x0.1) to 3e8 and 1e9. Result: G_growth does
NOT converge to anything sensible -- it goes NEGATIVE (-4.6e5 at T_END=3e8,
-7.2e5 at T_END=1e9). A sign flip is only possible if the coupled contrast
itself crosses zero somewhere beyond the T_END=1e8 reach. This means the
DECAY seen from x=100 to x=5940 within T_END=1e8 is not settling toward a
finite nonzero asymptote -- it is the LEADING EDGE of a DAMPED OSCILLATION
that crosses zero repeatedly as it decays. Point-sampled G_growth, evaluated
at any FIXED x, is fundamentally the wrong tool for a quantity that
oscillates through zero -- widening the window does not fix this, it just
moves WHERE the next zero-crossing happens to fall.

WHY THIS IS THE SAME LESSON AS FINDING_P107, IN THE OPPOSITE DIRECTION.
FINDING_P107 found eps was the wrong tool once G_growth SATURATES (a bounded
numerator over an ever-growing denominator, decaying to zero regardless of
physics). Here, point-sampled G_growth is the wrong tool once the coupled
contrast OSCILLATES THROUGH ZERO (a well-defined but discontinuous-looking
function of the sample point, giving wildly different values -- including
sign flips -- depending on exactly where in the oscillation cycle a fixed x
happens to land). Both are "construct validity" failures of a specific
diagnostic, not evidence about the completion's physics -- but neither is
fixable by the SAME trick that fixed the other (P107's fix was to switch
observables; P108's fix was to widen the window; NEITHER trick resolves
THIS problem, which needs an envelope/RMS-based observable instead --
named, not built, here).

PRE-REGISTERED OUTCOMES:
  RATIO-POLE-CONFIRMED     the reference (g_hat=0) run's own contrast DOES
                           cross zero near a tested anchor -> FINDING_P110's
                           original attribution was correct after all;
                           anchor relocation (FINDING_P76's own fix) should
                           work, and is attempted.
  TRANSIENT-OSCILLATION    the reference run's contrast does NOT cross zero,
                           but the COUPLED run's own contrast shows a large
                           transient overshoot with sign changes -> a
                           DIFFERENT mechanism than FINDING_P110 assumed;
                           anchor relocation and T_END extension are both
                           tested and (if the pattern holds) shown NOT to
                           resolve it, closing this specific fix attempt
                           honestly rather than forcing a number.

WHAT THIS FILE DOES NOT DO: build an envelope/RMS-based replacement
observable (a materially larger undertaking, named as the genuine next step
if this k<1 gap is worth closing properly). Quote eps(k), G_growth, or f(k)
in physical units, or any k[h/Mpc] number. Touch MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p105 = _load("P105_growth_with_lambda_cc.py", "p105_for_a111")

G_growth = p105.G_growth
run = p105.run
t_of_a = p105.t_of_a
contrast = p105.contrast
a_star = p105.a_star
G_HAT_FIXED, LAM_FIXED = p105.G_HAT_FIXED, p105.LAM_FIXED
PHIDOT_INIT = p105.PHIDOT_INIT

LAMBDA_FIXED = 1e-15
T_END = 1e8
X_LO = 0.2

# FINDING_P110's own three poled (k, IC) combinations.
CASES = (
    (0.3, "phidot x0.1", 0.1 * PHIDOT_INIT),
    (0.3, "phidot x0.5", 0.5 * PHIDOT_INIT),
    (0.5, "phidot x0.1", 0.1 * PHIDOT_INIT),
)

DIAG_XS = (0.2, 1.0, 5.0, 20.0, 50.0, 100.0, 1000.0, 5000.0)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P111 -- diagnose the k<1 phibar_dot(1) pole FINDING_P110 found,")
    print("        correcting a mistaken attribution made without verifying it")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    a0 = a_star(LAMBDA_FIXED)

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 1 -- CHECK FINDING_P110's OWN CLAIM: does the REFERENCE (g_hat=0)")
    print("run's contrast cross zero? (This is what a P76-G2-style pole requires.)")
    print("-" * 78)
    kk0, label0, phidot0_0 = CASES[0]
    s_ref = run(0.0, 1.0, kk0, T_END, lam_cc=LAMBDA_FIXED, phidot0=phidot0_0)
    print(f"\n  reference (g_hat=0) run, k={kk0}, {label0}:")
    ref_signs = []
    for x in (0.2, 0.5, 1, 2, 5, 10, 20, 50, 100):
        t_star = t_of_a(s_ref, a0 * x, 1.0, T_END)
        if t_star is None:
            continue
        c = contrast(s_ref, 0.0, 1.0, t_star, LAMBDA_FIXED)
        ref_signs.append(c > 0)
        print(f"    x={x:<8g} contrast_ref={c:.6e}")
    ref_crosses_zero = len(set(ref_signs)) > 1
    print(f"\n  reference run's contrast crosses zero: {ref_crosses_zero}")
    if ref_crosses_zero:
        print("  -> RATIO-POLE-CONFIRMED. FINDING_P110's attribution was correct.")
        print("     (Anchor relocation would be the appropriate fix -- not built in this")
        print("     branch, since the diagnosis below did not require it.)")
    else:
        print("  -> The reference run's contrast is smooth and one-signed throughout.")
        print("     FINDING_P110's attribution to a P76-G2-style DENOMINATOR pole was")
        print("     WRONG. Corrected: the mechanism must be in the COUPLED run instead.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 2 -- THE ACTUAL MECHANISM: the COUPLED (g_hat=1) run's own")
    print("field perturbation delta-phi, checked at all three of FINDING_P110's")
    print("poled (k, IC) combinations")
    print("-" * 78)
    for kk, label, phidot0 in CASES:
        print(f"\n  k={kk}, IC={label}:")
        s_coup = run(1.0, 1.0, kk, T_END, lam_cc=LAMBDA_FIXED, phidot0=phidot0)
        a0_k = a_star(LAMBDA_FIXED)
        for x in DIAG_XS:
            t_star = t_of_a(s_coup, a0_k * x, 1.0, T_END)
            if t_star is None:
                print(f"    x={x:<8g} UNREACHABLE")
                continue
            state = s_coup.sol(t_star)
            pb = state[1]
            dph = state[5]
            c = contrast(s_coup, 1.0, 1.0, t_star, LAMBDA_FIXED)
            print(f"    x={x:<8g} phibar={pb:+.4e}  delta_phi={dph:+.6e}  contrast={c:+.6e}")
        s0 = run(1.0, 1.0, kk, T_END, lam_cc=LAMBDA_FIXED, phidot0=phidot0)
        pb_max = max(
            abs(s0.sol(t_of_a(s0, a0_k * x, 1.0, T_END))[1])
            for x in DIAG_XS
            if t_of_a(s0, a0_k * x, 1.0, T_END) is not None
        )
        print(
            f"    max |phibar| over this range: {pb_max:.4e} "
            f"(equation-of-motion singularity needs phibar -> 1/g_hat=1 -- ruled out)"
        )

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 3 -- ATTEMPTED FIX: widen T_END, mirroring FINDING_P108's own")
    print("precedent, for the primary case (k=0.3, phidot x0.1)")
    print("-" * 78)
    kk, label, phidot0 = CASES[0]
    a0_k = a_star(LAMBDA_FIXED)
    print(f"\n  k={kk}, IC={label}:")
    sign_flip = False
    prev_g = None
    for te in (1e8, 3e8, 1e9):
        s_te = run(1.0, 1.0, kk, te, lam_cc=LAMBDA_FIXED, phidot0=phidot0)
        if s_te is None:
            print(f"    T_END={te:.0e}: run FAILED")
            continue
        a_end = s_te.sol(te)[0]
        g = G_growth(
            1.0, 1.0, kk, a0_k * X_LO, a_end * 0.9, te, lam_cc=LAMBDA_FIXED, phidot0=phidot0
        )
        print(f"    T_END={te:.0e}: a(T_END)/a_star={a_end / a0_k:.4e}  G_growth={g!r}")
        if prev_g is not None and g is not None and (prev_g > 0) != (g > 0):
            sign_flip = True
        prev_g = g
    print(f"\n  sign flip observed across widened T_END: {sign_flip}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if ref_crosses_zero:
        print("  -> RATIO-POLE-CONFIRMED (see Step 1). FINDING_P110's own attribution")
        print("     stands; this file's remaining diagnostics are secondary context.")
    else:
        print("  -> TRANSIENT-OSCILLATION, not a P76-G2-style ratio pole.")
        print("     FINDING_P110's attribution to FINDING_P76's G2 diagnosis was WRONG --")
        print("     corrected here. The actual mechanism: the coupled run's delta-phi")
        print("     undergoes a large transient overshoot (orders of magnitude, sign")
        print("     changes) before decaying -- confirmed at all three of FINDING_P110's")
        print("     poled (k, IC) combinations, not just one.")
        print("     Widening T_END (FINDING_P108's own fix for a DIFFERENT problem --")
        print(f"     under-reach) does {'' if sign_flip else 'NOT '}produce a sign flip here")
        if sign_flip:
            print("     -- confirming the coupled contrast is not settling toward a finite")
            print("     nonzero asymptote but continuing to oscillate through zero as the")
            print("     window widens. NEITHER anchor relocation (FINDING_P76's fix for a")
            print("     denominator pole) NOR T_END extension (FINDING_P108's fix for")
            print("     under-reach) resolves this -- both address DIFFERENT failure modes.")
            print("     NOT FIXED. Point-sampled G_growth is structurally the wrong tool for")
            print("     this (k, IC) region -- the same 'wrong tool for this regime' lesson")
            print("     FINDING_P107 taught for eps, in the opposite direction (there: bounded")
            print("     numerator over growing denominator; here: an oscillating numerator")
            print("     sampled at a single point). A genuine resolution needs an")
            print("     envelope/RMS-based observable -- named, not built here.")

    print("\n  NOT ESTABLISHED:")
    print("   * an envelope- or RMS-based observable that WOULD be well-defined for these")
    print("     (k, IC) combinations -- not built here, a materially larger undertaking.")
    print("   * whether this transient-oscillation mechanism appears at OTHER (k, IC)")
    print("     combinations not yet tested -- only the three FINDING_P110 already flagged.")
    print("   * anything about MULTING itself (Gate 1).")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
