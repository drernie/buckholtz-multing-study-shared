"""P135 -- WHY is eps/the P78 separation IC-sensitive at low k? Diagnosis,
not a new observable.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE. User-directed, after P134's own synthesis of bottleneck 2
(completion uniqueness) found it genuinely open, with P79's own stated
prerequisite for reopening it being "a better-conditioned low-k
observable" -- not a rescan of eps(k) at some untested k (P78's own data
shows the separation simply decays to zero by k=30; there is no separate
"transition scale" apart from the low-k region already tested). Before
attempting to DESIGN a new observable (real work, not attempted here), the
user asked for the cheaper, logically prior step: diagnose WHY the
current eps/separation is unstable at low k in the first place.

THE STANDING (INFORMAL) HYPOTHESIS, already in the record but never
quantitatively confirmed. FINDING_P76 states directly: "the contrast
passes near zero at an anchor, so the ratio has a pole -- the same
disease that made mu ill-posed in P74. A defect of the measurement... not
a physical divergence." But FINDING_P76's own Skeptic Verdict (#6)
records that the one detector built to confirm this (counting zero-
crossings of contrast(t) over the FULL trajectory) does NOT discriminate:
"P77's sign-count is 1 at every k, including the clean ones" -- accepted
as "an open item, not a result." The pole hypothesis was diagnosed, but
the confirming test failed to confirm it.

THE GAP THIS FILE CLOSES. eps(k) := d ln G / d ln a with
G_g := contrast(t2)/contrast(t1) for coupling g, evaluated at FIXED
scale-factor anchors (a1, a2), computed by P78's own eps()/sep(). A
whole-trajectory crossing count is the wrong detector -- it asks "does
the contrast oscillate anywhere", not "is the SPECIFIC anchor point close
to a zero of THIS run's contrast". This file measures the second
question directly: contrast(t1) and contrast(t2) for every sub-run
P79's own G1/G3 gates already use, and tests whether proximity to zero
AT THE ANCHOR correlates with the instability P79 measured (magnitude
spread for G1, and specifically the SIGN FLIP at k=3 for G3).

CLOSENESS METRIC (fixed before the run that produced the numbers below,
after an earlier window-based version was caught contaminated by growth
-- see the correction note on anchor_diagnostics()): for contrast c(t) at
an anchor t, close(t) := |c(t)| / (|dc/dt|(t) * t) -- the number of
e-folds in t, at the LOCAL linear rate, to the nearest zero of c. Small
(<0.2) means the anchor sits close to a crossing; large means it does
not, whether because |c| is large or because c is barely moving there.

PRE-REGISTERED OUTCOMES (before any number is computed):
  POLE-AT-ANCHOR-CONFIRMED  at the (k, lever) combinations where P79's
      G1/G3 failed, at least one sub-run's contrast at t1 or t2 has
      close(t)<0.2 AND/OR changes sign across the lever sweep --
      correlating with where the instability/sign-flip actually occurs.
      The positive control (k=10, known CLEAN in FINDING_P76) must show
      no such near-zero anchor and no sign flips, or this diagnostic
      does not discriminate either and the hypothesis is not confirmed.
  POLE-AT-ANCHOR-REFUTED  no such correlation -- contrast stays well
      away from zero at every tested anchor, even where G1/G3 failed.
      The informal diagnosis in FINDING_P76 would then be wrong, and
      the real mechanism is still unidentified.
  PARTIAL  correlates for some gates/k but not others (e.g. explains
      the k=3 sign flip but not the k=1/k=2 magnitude drift, or the
      reverse).

CONTROLS:
  POSITIVE CONTROL: k=10 (FINDING_P76's own "CLEAN" point -- eps
      converged, lever-stable, ~scan-stable) must show contrast staying
      well clear of zero at both anchors, across the same lever sweep.
      If the diagnostic flags k=10 as pole-adjacent too, it does not
      discriminate (repeats P76's own detector failure) and nothing
      below can be trusted.
  REUSE, NOT REDERIVE: run/contrast/t_of_a/eps/sep are imported directly
      from P79's own module (which itself imports P78's), not
      reimplemented -- avoids a transcription error creating a fake
      signal.

WHAT THIS FILE DOES NOT DO: design a replacement observable (a real,
separate task, only attempted if this diagnosis motivates a specific
fix). Rerun G2 (anchor-A1) or G4/G5 -- G1 and G3 are the two gates that
most directly probe growth-window and IC sensitivity respectively, and
G3's sign flip is the single most informative failure to explain. Vary
Lambda, G_N, or any external constant. Quote any k[h/Mpc]. Touch MULTING
itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location("p79_ref", os.path.join(_HERE, "P79_low_k_window.py"))
p79 = importlib.util.module_from_spec(_sp)
sys.modules["p79_ref"] = p79
_sp.loader.exec_module(p79)

run, contrast, t_of_a = p79.run, p79.contrast, p79.t_of_a
sep, PHIDOT, LAM, GH = p79.sep, p79.PHIDOT, p79.LAM, p79.GH


def anchor_diagnostics(name, gh, kk, a1, a2, rtol=1e-10, **ic):
    """For one sub-run: contrast at t1/t2, plus a LOCAL 'distance to a zero
    crossing' at each anchor -- |c(t)| / (|dc/dt|(t) * t), a dimensionless
    number of e-folds (in t) to the nearest zero AT THE LOCAL LINEAR RATE.
    Small (<<1) means the anchor sits right next to where c(t) crosses
    zero; large (>>1) means c is far from any crossing there, whether
    because it is large or because it is barely moving (e.g. a smooth,
    monotonic growth regime, not an oscillation).

    CORRECTION (same run, before any verdict): a first version used the
    max|contrast| over a wide [0.3t, 3t] window as the 'local scale' --
    dominated by later, larger growth-regime values rather than proximity
    to a crossing, so it read near-machine-zero everywhere INCLUDING the
    k=10 positive control. That is not a real signal, it is the window
    picking up growth. Replaced with a genuinely local derivative.
    """
    s = run(name, gh, LAM, kk, rtol=rtol, **ic) if ic else run(name, gh, LAM, kk, rtol=rtol)
    t1, t2 = t_of_a(s, a1), t_of_a(s, a2)
    if t1 is None or t2 is None:
        return None

    def local_dist(t):
        c = contrast(s, name, gh, LAM, t)
        dt = t * 1e-4
        dcdt = (contrast(s, name, gh, LAM, t + dt) - contrast(s, name, gh, LAM, t - dt)) / (2 * dt)
        if dcdt == 0:
            return c, float("inf")
        return c, abs(c) / (abs(dcdt) * t)

    c1, close1 = local_dist(t1)
    c2, close2 = local_dist(t2)
    return {"t1": t1, "t2": t2, "c1": c1, "c2": c2, "close1": close1, "close2": close2}


SUBRUNS = [
    ("exponential", GH),
    ("linear", GH),
    ("exponential", 0.0),
    ("linear", 0.0),
]


def main() -> int:  # noqa: PLR0915 - one linear diagnostic report
    print("=" * 78)
    print("P135 -- diagnosis: why is eps/the P78 separation IC-sensitive at low k?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    s_ref = run("linear", 0.0, LAM, 1.0)
    A1, A2 = s_ref.sol(1e4)[0], s_ref.sol(8e7)[0]

    # ------------------------------------------------------------ Part A
    print("\n" + "-" * 78)
    print("PART A -- G3 lever sweep (k in {1,2,3}, POSITIVE CONTROL k=10),")
    print("closeness-to-zero at the t1/t2 anchors for all 4 sub-runs")
    print("-" * 78)

    KS = (1.0, 2.0, 3.0, 10.0)
    LEVERS = (0.1, 0.5, 1.0, 2.0)

    any_signflip = {}
    min_close = {}
    for kk in KS:
        print(f"\n  k = {kk}")
        print(f"    {'law/g':<16}{'lever':<8}{'close1':<12}{'close2':<12}{'c1':<14}{'c2'}")
        c1_by_run = {sr: [] for sr in SUBRUNS}
        mins = []
        for f in LEVERS:
            for law, g in SUBRUNS:
                d = anchor_diagnostics(law, g, kk, A1, A2, phidot0=f * PHIDOT)
                if d is None:
                    print(f"    {law + '/' + str(g):<16}{f:<8}{'--anchor unreachable--'}")
                    continue
                c1_by_run[(law, g)].append((f, d["c1"]))
                mins.append(d["close1"])
                mins.append(d["close2"])
                print(
                    f"    {law + '/' + str(g):<16}{f:<8}{d['close1']:<12.3e}"
                    f"{d['close2']:<12.3e}{d['c1']:<14.6e}{d['c2']:.6e}"
                )
        min_close[kk] = min(mins) if mins else float("nan")
        # sign-flip check: does c1 (or c2, checked implicitly via close~0) change
        # sign across the lever sweep, for any of the 4 sub-runs?
        flips = []
        for sr, vals in c1_by_run.items():
            signs = {np.sign(v) for _, v in vals if v != 0}
            if len(signs) > 1:
                flips.append(sr)
        any_signflip[kk] = flips
        print(f"    -> sub-runs with a SIGN FLIP in c1 across the lever sweep: {flips or 'none'}")
        print(f"    -> smallest closeness-to-zero seen at this k: {min_close[kk]:.3e}")

    # ------------------------------------------------------------ Part B
    print("\n" + "-" * 78)
    print("PART B -- cross-check against P79's own G1/G3 verdicts")
    print("-" * 78)
    # G3 spreads/flip, reusing P79's own sep() so the numbers match exactly
    print(f"\n    {'k':<8}{'separation spread (G3, x0.1..x2)':<38}{'sign flip in sep?'}")
    g3_summary = {}
    for kk in KS:
        vals = [sep(kk, A1, A2, phidot0=f * PHIDOT) for f in LEVERS]
        spread = (
            max(vals) / min(vals)
            if all(v > 0 for v in vals) or all(v < 0 for v in vals)
            else float("inf")
        )
        sign_flip = len({np.sign(v) for v in vals}) > 1
        g3_summary[kk] = (spread, sign_flip)
        print(
            f"    {kk:<8}{spread if spread != float('inf') else 'N/A (sign flip)':<38}{sign_flip}"
        )

    # ------------------------------------------------------------ Verdict
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)

    CLOSE_THRESHOLD = 0.2  # e-folds-in-t to the nearest zero, at the local linear rate
    control_clean = len(any_signflip[10.0]) == 0 and min_close[10.0] > CLOSE_THRESHOLD
    print(
        f"\n  POSITIVE CONTROL (k=10): sign flips = {any_signflip[10.0] or 'none'}, "
        f"min closeness = {min_close[10.0]:.3e}"
    )
    print(
        f"  Control {'PASSES' if control_clean else 'FAILS'} "
        f"(expect no sign flip, closeness not pole-like, threshold={CLOSE_THRESHOLD})"
    )

    if not control_clean:
        print("\n  *** The diagnostic itself does not discriminate clean k=10 from")
        print("      unstable low-k -- same failure as P76's own crossing-count.")
        print("      POLE-AT-ANCHOR: NOT CONFIRMABLE by this file's own method.")
        return 0

    unstable_ks = [1.0, 2.0, 3.0]
    correlates = []
    for kk in unstable_ks:
        flip_here = len(any_signflip[kk]) > 0
        sep_flip_here = g3_summary[kk][1]
        small_close = min_close[kk] < CLOSE_THRESHOLD
        correlates.append((kk, flip_here, sep_flip_here, small_close))
        print(
            f"\n  k={kk}: sub-run contrast sign-flip = {flip_here}, "
            f"P79 separation sign-flip = {sep_flip_here}, "
            f"anchor near pole (closeness<{CLOSE_THRESHOLD}) = {small_close}"
        )

    k3_explained = correlates[2][1] == correlates[2][2] and correlates[2][1] is True
    low_k_explained = any(c[3] for c in correlates)

    if k3_explained and low_k_explained:
        print("\n  -> POLE-AT-ANCHOR-CONFIRMED. A sub-run's contrast at the anchor")
        print("     changes sign across the IC lever exactly where P79's own")
        print("     separation sign-flips (k=3), and at least one low-k anchor sits")
        print("     measurably close to a pole (closeness<<1) where the positive")
        print("     control (k=10) does not. The informal FINDING_P76 diagnosis is")
        print("     confirmed quantitatively, at the anchor rather than by counting")
        print("     crossings over the whole trajectory (which could not discriminate).")
    elif k3_explained or low_k_explained:
        print("\n  -> PARTIAL. Some but not all of P79's instability signatures line")
        print("     up with anchor-proximity-to-zero. See the k-by-k breakdown above")
        print("     for which gate is explained and which is not.")
    else:
        print("\n  -> POLE-AT-ANCHOR-REFUTED. Anchor contrast values do not show the")
        print("     sign-flip/near-zero pattern needed to explain P79's own G1/G3")
        print("     failures. The mechanism is real (G1/G3 do fail) but its cause is")
        print("     NOT simply anchor-proximity to a contrast zero-crossing.")

    print("\n  NOT ESTABLISHED regardless of outcome:")
    print("   * a replacement, IC-robust observable -- a separate design task,")
    print("     only motivated (not attempted) by this file's own verdict.")
    print("   * anything about G2 (anchor-A1 spread) or G4/G5 -- not rerun here.")
    print("   * anything observational -- internal units, NO_BRIDGE_FITTING in force")
    print("   * anything about MULTING itself (Gate 1): both completions are OURS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
