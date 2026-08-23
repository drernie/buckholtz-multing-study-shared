"""P136 -- does the early oscillatory transient carry the IC-sensitivity
P79 found at late times? Testing the real next-hypothesis P135 named.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE. Round-2 strategic arbiter (this session, 2026-08-24) named
this the strongest surviving GO for bottleneck 2 (completion uniqueness):
cheap, reuses existing tested machinery, informative either way. FINDING_
P135 eliminated the "pole at anchor" hypothesis (P76's informal diagnosis)
by showing every anchor P79 samples sits deep in a smooth, textbook
growing-mode regime, far from the oscillatory transient FINDING_P77 found
(~160 zero-crossings at (g_hat=0.5, k=1)). P135's own live candidate,
[INFERRED] and untested there: the IC lever shifts the early transient's
phase/amplitude, and that shift propagates into the late-time amplitude
the anchors sample -- an ACCUMULATED sensitivity, not a local defect.

THE ESTIMATOR, chosen to avoid this campaign's own seventh-instance
failure (FINDING_P80: "the gate measures something other than what the
claim asserts" -- a point sample of an oscillating quantity measures
PHASE, not AMPLITUDE, and the claim here is about amplitude). Track
RMS(contrast) over an EARLY window (t in [1, 100], well before P79's own
anchors at t~1e4/1e8, and squarely inside the ~160-crossing regime P77
found at k=1) as the lever varies -- an amplitude-type summary, not a
point value.

PRE-REGISTERED OUTCOMES (before any number is computed):
  EARLY-TRANSIENT-CONFIRMED  the early-window RMS(contrast) shows a
      relative spread across the lever sweep (x0.1..x2, same range P79
      used) at k in {1,2,3} that is CLEARLY LARGER than at k=10 (control)
      -- i.e. the IC-sensitivity is already present in the early
      transient, before any late-time anchor is reached, and roughly
      tracks P79's own late-time instability ranking (k=1,2 large
      spread; k=3 the qualitatively different sign-flip case).
  EARLY-TRANSIENT-REFUTED  the early-window RMS spread is comparable
      across k in {1,2,3,10} (no discrimination) -- the early transient
      does not carry the signature, and the late-time instability's real
      cause is still unidentified.
  PARTIAL  spread discriminates at some k but not others.

CONTROLS:
  POSITIVE CONTROL (rtol): early-window RMS at a fixed (k, lever) must be
      stable across rtol in {1e-8, 1e-10, 1e-12} -- if this quantity
      itself is numerically unstable, nothing else in this file can be
      trusted, exactly the discipline P79's own G4 gate applied to the
      separation.
  REUSE, NOT REDERIVE: run/contrast imported directly from P79's module.

WHAT THIS FILE DOES NOT DO: design a replacement observable (a separate,
larger task, only motivated by this file's own verdict). Test G2 (anchor-
A1) or G5 (zero-crossing counts) directly -- P77 already established the
crossing-count pattern; this file asks a DIFFERENT question (does the
crossing PATTERN'S dependence on the lever explain the late instability,
not merely that crossings exist). Vary Lambda, G_N, or any external
constant. Quote any k[h/Mpc]. Touch MULTING itself (Gate 1).
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

run, contrast = p79.run, p79.contrast
sep, PHIDOT, LAM, GH = p79.sep, p79.PHIDOT, p79.LAM, p79.GH

KS = (1.0, 2.0, 3.0, 10.0)
LEVERS = (0.1, 0.5, 1.0, 2.0)
EARLY_WINDOW = np.geomspace(1.0, 100.0, 400)


def early_rms(law, gh, kk, rtol=1e-10, **ic):
    s = run(law, gh, LAM, kk, rtol=rtol, **ic) if ic else run(law, gh, LAM, kk, rtol=rtol)
    vals = np.array([contrast(s, law, gh, LAM, t) for t in EARLY_WINDOW])
    return float(np.sqrt(np.mean(vals**2)))


def main() -> int:
    print("=" * 78)
    print("P136 -- does the early transient carry P79's late-time IC-sensitivity?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------ control
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- rtol stability of early-window RMS(contrast)")
    print("-" * 78)
    print(f"\n    {'rtol':<12}{'RMS @ k=1, lever=1':<24}{'shift'}")
    prev, worst = None, 0.0
    for rt in (1e-8, 1e-10, 1e-12):
        v = early_rms("linear", GH, 1.0, rtol=rt, phidot0=PHIDOT)
        print(f"    {rt:<12.0e}{v:<24.12e}{'' if prev is None else f'{abs(v - prev):.2e}'}")
        if prev is not None:
            worst = max(worst, abs(v - prev) / abs(v))
        prev = v
    control_ok = worst < 0.01
    print(
        f"\n    largest relative shift {worst:.2e}; control {'PASSES' if control_ok else 'FAILS'}"
    )
    if not control_ok:
        print("\n  *** early-window RMS is not numerically trustworthy -- STOP.")
        return 1

    # ------------------------------------------------------------- Part A
    print("\n" + "-" * 78)
    print("PART A -- early-window RMS(contrast), linear-law/g_hat=1 branch,")
    print("across the lever sweep, k in {1,2,3, CONTROL=10}")
    print("-" * 78)
    print(f"\n    {'k':<8}" + "".join(f"{'lever=' + str(f):<16}" for f in LEVERS) + "spread")
    spreads = {}
    for kk in KS:
        vals = [early_rms("linear", GH, kk, phidot0=f * PHIDOT) for f in LEVERS]
        sp_ = max(vals) / min(vals)
        spreads[kk] = sp_
        print(f"    {kk:<8}" + "".join(f"{v:<16.6e}" for v in vals) + f"{sp_:.4f}")

    # ------------------------------------------------------------- Part B
    print("\n" + "-" * 78)
    print("PART B -- cross-check against P79's/P135's own late-time instability")
    print("-" * 78)
    print(f"\n    {'k':<8}{'early-RMS spread':<20}{'P79 G3 late spread (or sign flip)'}")
    late = {}
    s_ref = run("linear", 0.0, LAM, 1.0)
    a1, a2 = s_ref.sol(1e4)[0], s_ref.sol(8e7)[0]
    for kk in KS:
        vals = [sep(kk, a1, a2, phidot0=f * PHIDOT) for f in LEVERS]
        if all(v > 0 for v in vals) or all(v < 0 for v in vals):
            late[kk] = max(vals) / min(vals)
            late_str = f"{late[kk]:.4f}"
        else:
            late[kk] = float("inf")
            late_str = "sign flip"
        print(f"    {kk:<8}{spreads[kk]:<20.4f}{late_str}")

    # ------------------------------------------------------------ Verdict
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)

    control_spread = spreads[10.0]
    unstable_spreads = {kk: spreads[kk] for kk in (1.0, 2.0, 3.0)}
    print(f"\n  Control (k=10) early-RMS spread: {control_spread:.4f}")
    for kk, sp_ in unstable_spreads.items():
        ratio = sp_ / control_spread
        print(f"  k={kk}: early-RMS spread = {sp_:.4f}  ({ratio:.2f}x the control)")

    discriminates = all(spreads[kk] / control_spread > 1.5 for kk in (1.0, 2.0, 3.0))
    partial = any(spreads[kk] / control_spread > 1.5 for kk in (1.0, 2.0, 3.0))

    if discriminates:
        print("\n  -> EARLY-TRANSIENT-CONFIRMED. The early-window RMS(contrast) already")
        print("     shows elevated lever-sensitivity at every unstable k, well before")
        print("     any late-time anchor is reached. This is consistent with P135's own")
        print("     candidate mechanism: the transient, not the anchor, carries the")
        print("     IC-sensitivity that later shows up in P79's separation.")
    elif partial:
        print("\n  -> PARTIAL. Early-window sensitivity is elevated at some but not all")
        print("     of the unstable k values -- see the k-by-k ratios above.")
    else:
        print("\n  -> EARLY-TRANSIENT-REFUTED. The early-window RMS(contrast) does not")
        print("     discriminate unstable k from the k=10 control any more than the")
        print("     control's own baseline variation. The late-time instability's real")
        print("     cause remains unidentified by this file.")

    print("\n  NOT ESTABLISHED regardless of outcome:")
    print("   * a replacement, IC-robust observable -- separate design task.")
    print("   * a mechanistic EXPLANATION even if correlation is confirmed -- this")
    print("     file establishes correlation, not the causal chain.")
    print("   * anything about G2/G5 directly -- not rerun here.")
    print("   * anything observational -- internal units, NO_BRIDGE_FITTING in force")
    print("   * anything about MULTING itself (Gate 1): both completions are OURS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
