"""P79 -- does P78's discrimination survive the window it lives in?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS RUNS FIRST, AND WHY IT CAN DESTROY THE BEST RESULT OF THE ARC.

FINDING_P78 returned D-SEP: the growth channel separates the linear mass law
M = 1 - g*phi from the exponential M = exp(-g*phi). But look at WHERE:

    k=1   +26.71%      k=3   +0.63%      k=10  +0.10%      k=30  +0.00%

Essentially the whole verdict rests on k=1. And k<=1 is exactly the window
FINDING_P77 flagged as the least trustworthy: the largest a2-spread (1.0059 vs
1.0020 elsewhere), the largest anchor sensitivity, and an outright blow-up at
(g_hat=0.5, k=1) where the coupled contrast oscillates through zero ~160 times.

So the strongest claim of the campaign currently stands on its least validated
ground. This file applies every gate P76/P77 built to the SEPARATION itself --
not to eps, to the DIFFERENCE between completions, which is the quantity D-SEP
actually asserts.

PRE-REGISTERED OUTCOMES (before any number):
  W-OK    the separation survives every gate at k<=3 -> D-SEP stands and the
          low-k window is usable for completion discrimination.
  W-FAIL  any gate fails -> D-SEP is UNSUPPORTED and P78's verdict reverts to
          undecided. The separation would then be a property of the window, not
          of the completions.

GATES, each with its threshold fixed here and not adjustable later:
  G1 a2-convergence     separation changes <2% over the final stretch
  G2 anchor A1          separation changes <5% across A1 spanning 3 decades
  G3 lever phibar_dot   separation changes <10% over x0.1..x2 -- and ONLY that
                        range, because P77 established x10 is a kination-
                        dominated cosmology rather than an initial-data variation
  G4 rtol               separation stable across 1e-8..1e-12
  G5 zero-crossings     counted on BOTH runs, not just the reference -- the
                        specific error P77 made and had to retract
"""

import importlib.util
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location(
    "p78_ref", os.path.join(_HERE, "P78_completion_discrimination.py")
)
p78 = importlib.util.module_from_spec(_sp)
sys.modules["p78_ref"] = p78
_sp.loader.exec_module(p78)

run, contrast, t_of_a = p78.run, p78.contrast, p78.t_of_a
mass_law, bg_of, T_END = p78.mass_law, p78.bg_of, p78.T_END
PHIDOT = p78.PHIDOT_INIT
LAM, GH = 1.0, 1.0


def eps(name, gh, kk, a1, a2, rtol=1e-10, **ic):
    out = []
    for g in (gh, 0.0):
        s = run(name, g, LAM, kk, rtol=rtol, **ic) if ic else run(name, g, LAM, kk, rtol=rtol)
        t1, t2 = t_of_a(s, a1), t_of_a(s, a2)
        if t1 is None or t2 is None:
            return None
        out.append(contrast(s, name, g, LAM, t2) / contrast(s, name, g, LAM, t1))
    return np.log(out[0] / out[1]) / np.log(a2 / a1)


def sep(kk, a1, a2, rtol=1e-10, **ic):
    """THE quantity D-SEP asserts: the separation between completions."""
    a = eps("exponential", GH, kk, a1, a2, rtol=rtol, **ic)
    b = eps("linear", GH, kk, a1, a2, rtol=rtol, **ic)
    return None if (a is None or b is None) else a - b


def main() -> int:
    print("=" * 78)
    print("P79 -- does P78's D-SEP survive the low-k window it lives in?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    s_ref = run("linear", 0.0, LAM, 1.0)
    A1, A2 = s_ref.sol(1e4)[0], s_ref.sol(8e7)[0]
    KS = (1.0, 2.0, 3.0)

    print("\n  The quantity under test is NOT eps -- it is the SEPARATION")
    print("  eps_exp(k) - eps_lin(k), which is what D-SEP actually asserts.")
    print(f"\n    {'k':<8}{'separation':<20}{'relative to eps_lin'}")
    base = {}
    for kk in KS:
        d = sep(kk, A1, A2)
        base[kk] = d
        print(f"    {kk:<8}{d:<20.6e}{d / eps('linear', GH, kk, A1, A2):+.2%}")

    # ---------------------------------------------------------------- G1
    print("\n" + "-" * 78)
    print("G1 -- a2-convergence of the SEPARATION (threshold: <2% final stretch)")
    print("-" * 78)
    print(f"\n    {'k':<8}{'@1e6':<18}{'@1e7':<18}{'@8e7':<18}{'final change'}")
    g1 = {}
    for kk in KS:
        vals = [sep(kk, A1, s_ref.sol(te)[0]) for te in (1e6, 1e7, 8e7)]
        chg = abs(vals[-1] / vals[-2] - 1.0)
        g1[kk] = chg
        print(f"    {kk:<8}" + "".join(f"{v:<18.6e}" for v in vals) + f"{chg:.2%}")
    G1 = all(v < 0.02 for v in g1.values())
    print(f"\n    => G1 {'PASS' if G1 else 'FAIL'}")

    # ---------------------------------------------------------------- G2
    print("\n" + "-" * 78)
    print("G2 -- anchor A1 across three decades (threshold: <5%)")
    print("-" * 78)
    print(f"\n    {'A1 from t=':<14}" + "".join(f"{'k=' + str(k):<20}" for k in KS))
    rows = {}
    for ta in (1e3, 1e4, 1e5, 1e6):
        vals = [sep(kk, s_ref.sol(ta)[0], A2) for kk in KS]
        rows[ta] = vals
        print(f"    {ta:<14.0e}" + "".join(f"{v:<20.6e}" for v in vals))
    print(f"\n    {'k':<8}{'min':<18}{'max':<18}{'spread'}")
    g2 = {}
    for i, kk in enumerate(KS):
        vs = [rows[ta][i] for ta in rows]
        sp_ = max(vs) / min(vs)
        g2[kk] = sp_
        print(f"    {kk:<8}{min(vs):<18.6e}{max(vs):<18.6e}{sp_:.4f}")
    G2 = all(v < 1.05 for v in g2.values())
    print(f"\n    => G2 {'PASS' if G2 else 'FAIL'}")

    # ---------------------------------------------------------------- G3
    print("\n" + "-" * 78)
    print("G3 -- phibar_dot lever, x0.1..x2 ONLY (threshold: <10%)")
    print("-" * 78)
    print("  x10 is deliberately EXCLUDED: FINDING_P77 established it puts 84.85%")
    print("  of the t=1 energy budget in the scalar, i.e. a kination-dominated")
    print("  cosmology rather than a perturbation of the initial data. Including")
    print("  it would be testing a different model, not this one's robustness.")
    print(f"\n    {'lever':<12}" + "".join(f"{'k=' + str(k):<20}" for k in KS))
    lrows = {}
    for f in (0.1, 0.5, 1.0, 2.0):
        vals = [sep(kk, A1, A2, phidot0=f * PHIDOT) for kk in KS]
        lrows[f] = vals
        print(f"    x{f:<11.1f}" + "".join(f"{v:<20.6e}" for v in vals))
    print(f"\n    {'k':<8}{'min':<18}{'max':<18}{'spread'}")
    g3 = {}
    for i, kk in enumerate(KS):
        vs = [lrows[f][i] for f in lrows]
        sp_ = max(vs) / min(vs)
        g3[kk] = sp_
        print(f"    {kk:<8}{min(vs):<18.6e}{max(vs):<18.6e}{sp_:.4f}")
    G3 = all(v < 1.10 for v in g3.values())
    print(f"\n    => G3 {'PASS' if G3 else 'FAIL'}")

    # ---------------------------------------------------------------- G4
    print("\n" + "-" * 78)
    print("G4 -- rtol stability of the separation")
    print("-" * 78)
    print(f"\n    {'rtol':<12}{'separation k=1':<24}{'shift'}")
    prev, g4 = None, 0.0
    for rt in (1e-8, 1e-10, 1e-12):
        v = sep(1.0, A1, A2, rtol=rt)
        print(f"    {rt:<12.0e}{v:<24.12e}{'' if prev is None else f'{abs(v - prev):.2e}'}")
        if prev is not None:
            g4 = max(g4, abs(v - prev) / abs(v))
        prev = v
    G4 = g4 < 0.01
    print(f"\n    => largest relative shift {g4:.2e}; G4 {'PASS' if G4 else 'FAIL'}")

    # ---------------------------------------------------------------- G5
    print("\n" + "-" * 78)
    print("G5 -- zero-crossings on BOTH runs (the error P77 made and retracted)")
    print("-" * 78)
    print("  P77 counted crossings only on the g_hat=0 reference, saw 1 everywhere,")
    print("  and wrongly concluded its test was merely non-discriminating. The")
    print("  blow-up came from the COUPLED run. Count every run used here.")
    tt = np.logspace(0, 8, 20000)
    print(f"\n    {'k':<8}{'lin g=1':<14}{'exp g=1':<14}{'lin g=0':<14}{'exp g=0':<14}{'status'}")
    g5 = {}
    for kk in KS:
        counts = []
        for nm, g in (("linear", GH), ("exponential", GH), ("linear", 0.0), ("exponential", 0.0)):
            s = run(nm, g, LAM, kk)
            cs = np.array([contrast(s, nm, g, LAM, tv) for tv in tt])
            counts.append(sum(1 for i in range(1, len(cs)) if cs[i] * cs[i - 1] < 0))
        worst = max(counts)
        g5[kk] = worst
        print(
            f"    {kk:<8}"
            + "".join(f"{c:<14}" for c in counts)
            + ("OSCILLATORY" if worst > 3 else "clean")
        )
    G5 = all(v <= 3 for v in g5.values())
    print(f"\n    => G5 {'PASS' if G5 else 'FAIL'}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    gates = {
        "G1 a2-convergence": G1,
        "G2 anchor": G2,
        "G3 lever": G3,
        "G4 rtol": G4,
        "G5 zero-crossings": G5,
    }
    for nm, ok in gates.items():
        print(f"  {nm:<24}{'PASS' if ok else 'FAIL'}")
    allpass = all(gates.values())
    print()
    if allpass:
        print("  -> W-OK. The separation survives every gate at k <= 3. FINDING_P78's")
        print("     D-SEP stands, and the low-k window IS usable for completion")
        print("     discrimination -- which also partially reopens the k<=1 region")
        print("     that FINDING_P77 excluded at g_hat=0.5.")
    else:
        failed = [n for n, ok in gates.items() if not ok]
        print(f"  -> W-FAIL on {failed}.")
        print("     *** FINDING_P78's D-SEP is UNSUPPORTED. *** The separation would")
        print("     then be a property of the measurement window, not of the")
        print("     completions, and the uniqueness question reverts to undecided.")
        print("     This is NOT evidence that the completions are degenerate -- it")
        print("     is evidence that this window cannot tell.")

    print("\n  NOT ESTABLISHED regardless of outcome:")
    print("   * anything observational -- internal units, NO_BRIDGE_FITTING in force")
    print("   * that two mass laws span the completion space")
    print("   * anything about MULTING itself (Gate 1): both completions are OURS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
