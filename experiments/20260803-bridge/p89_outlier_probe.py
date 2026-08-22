"""Why does (k=3, a=1e5) sit 100x worse than every other point in P89?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

P89 returned F-CONFIRMED with a worst relative difference on df of 6.690e-05
against a pre-registered threshold of 1e-4. That is a SCRAPE, not a margin, and
the point is an outlier rather than a typical value:

    k = 3    a = 1e4 -> 1.705e-06   a = 1e5 -> 6.690e-05   a = 4e5 -> 4.639e-06
    k = 10                          a = 1e5 -> 3.254e-06
    k = 30                          a = 1e5 -> 8.541e-07

Two structures are visible and neither is noise: a = 1e5 is the worst point at
EVERY k, and the discrepancy grows sharply as k falls. A verdict that depends on
a value 100x worse than its neighbours has to explain that value or say plainly
that it cannot.

WHAT IS ALREADY RULED OUT BY P89'S OWN OUTPUT. The matched-t versus matched-a
convention differs by 5.5e-07 / 4.5e-08 / 1.1e-08 at k = 3 / 10 / 30 -- two
orders of magnitude BELOW the outlier. The evaluation convention is not the
cause, and this file does not re-test it.

WHAT IS TESTED HERE. Two things differ between P89 and P82 at once: the solver
and the DIFFERENCE SCHEME. P89 steps h in N = ln a directly; P82 steps dlnt in
ln t and divides by the measured d ln a. If the outlier is a difference-scheme
artifact it must shrink when both steps are refined; if it is an implementation
difference it will not move.

PRE-REGISTERED, before any number:
  STEP-LIMITED   refining both steps 10x drops rel(df) by >= 10x
                 -> the outlier is a differencing artifact, the true agreement
                    at this point is much better than 6.69e-05, and F-CONFIRMED
                    stops depending on a scrape.
  PERSISTENT     rel(df) changes by < 2x
                 -> a real implementation difference that the finding must NAME,
                    and F-CONFIRMED must be reported as resting on a value that
                    was not explained.
  PARTIAL        anything between -> named, not smoothed.

A third, cheap diagnostic runs regardless: df is a difference of two nearly equal
numbers, so it is the classic site for cancellation loss. The CONDITION NUMBER
|f(g=1)| / |df| is printed at each point -- if the outlier sits where that number
peaks, cancellation is the mechanism rather than either code being wrong. This is
a diagnostic and is labelled as one; it is not scored.
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T_END = 1e8
LAM = 1.0
K_BAD, A_BAD = 3.0, 1e5


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p89 = _load("P89_f_through_the_reconstruction.py", "p89_probe")
p76 = _load("P76_growth_observable.py", "p76_probe")
p82 = _load("P82_growth_rate.py", "p82_probe")


def df_recon(k, a, h, rtol=1e-11):
    s1 = p89.solve_recon(1.0, LAM, k, a, rtol=rtol)
    s0 = p89.solve_recon(0.0, LAM, k, a, rtol=rtol)
    return p89.f_recon(s1, a, 1.0, LAM, h=h) - p89.f_recon(s0, a, 0.0, LAM, h=h)


def df_p82(k, a, dlnt):
    out = []
    for g in (1.0, 0.0):
        s = p76.run(g, LAM, k, T_END)
        t = p76.t_of_a(s, a, 1.0, T_END)
        if t is None:
            return None
        out.append(p82.growth_rate(s, g, LAM, t, dlnt=dlnt))
    return out[0] - out[1]


def main() -> int:
    print("=" * 78)
    print("p89 outlier probe -- is (k=3, a=1e5) a scheme artifact or a difference?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n" + "-" * 78)
    print("PART 1 -- refine BOTH difference steps together")
    print("-" * 78)
    print(f"  k = {K_BAD:g}, a = {A_BAD:g}. P89 used h = 1e-4 and P82's dlnt = 1e-3.")
    print(f"\n    {'h (recon)':<14}{'dlnt (P82)':<14}{'df recon':<20}{'df P82':<20}{'rel'}")
    rels = []
    for h, dl in ((1e-3, 1e-2), (1e-4, 1e-3), (1e-5, 1e-4), (1e-6, 1e-5)):
        dr = df_recon(K_BAD, A_BAD, h)
        dp = df_p82(K_BAD, A_BAD, dl)
        if dp is None:
            print(f"    {h:<14.0e}{dl:<14.0e}{'a not reachable -- not measured':<40}")
            continue
        rel = abs(dr / dp - 1.0)
        rels.append(rel)
        print(f"    {h:<14.0e}{dl:<14.0e}{dr:<20.12f}{dp:<20.12f}{rel:.3e}")

    if len(rels) < 2:
        print("\n    not enough points -- BLOCKED-INFRASTRUCTURE, not a result.")
        return 1
    drop = rels[0] / rels[-1] if rels[-1] > 0 else float("inf")
    print(f"\n    coarsest / finest = {drop:.3g}x")
    if drop >= 10:
        verdict = "STEP-LIMITED"
    elif drop < 2:
        verdict = "PERSISTENT"
    else:
        verdict = "PARTIAL"
    print(f"    PART 1 -> {verdict}")

    print("\n" + "-" * 78)
    print("PART 2 -- DIAGNOSTIC (not scored): cancellation condition number")
    print("-" * 78)
    print("  df = f(g=1) - f(g=0) subtracts two numbers near 1 to get one near")
    print("  0.04, so |f| / |df| measures how much any absolute error in f is")
    print("  amplified in df. If the outlier sits where this peaks, cancellation")
    print("  is the mechanism -- and that is an observation, not a test.")
    print(f"\n    {'k':<7}{'a':<10}{'f(g=1)':<18}{'df':<18}{'|f|/|df|'}")
    for k in (3.0, 10.0, 30.0):
        for a in (1e4, 1e5, 4e5):
            s1 = p89.solve_recon(1.0, LAM, k, a)
            s0 = p89.solve_recon(0.0, LAM, k, a)
            f1 = p89.f_recon(s1, a, 1.0, LAM)
            d = f1 - p89.f_recon(s0, a, 0.0, LAM)
            mark = "   <- the outlier" if (k == K_BAD and a == A_BAD) else ""
            print(f"    {k:<7g}{a:<10.4g}{f1:<18.12f}{d:<18.12f}{abs(f1 / d):<10.2f}{mark}")

    print("\n" + "=" * 78)
    print("COMBINED")
    print("=" * 78)
    if verdict == "STEP-LIMITED":
        print("  The outlier is a DIFFERENCE-SCHEME artifact. P89's F-CONFIRMED no")
        print("  longer rests on a scrape: at matched refinement the two codes")
        print("  agree far better than the threshold at this point too.")
    elif verdict == "PERSISTENT":
        print("  The outlier is NOT a scheme artifact. F-CONFIRMED stands only")
        print("  because 6.69e-05 happens to fall under 1e-4, and the finding must")
        print("  say so and name the difference as unexplained.")
    else:
        print("  Partly a scheme artifact. The residual must be named in the")
        print("  finding rather than absorbed into the verdict.")
    print("\n  Says nothing about whether the shared EQUATIONS are right.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
