"""Why did two bisections with DIFFERENT brackets agree to 1 ulp?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

P91 returned B-SUSPICIOUS-TIGHT, which is the outcome it pre-registered for
exactly this: agreement of 2.220e-16 and 0.000e+00 between two bisections that
were deliberately given different brackets ((1.0, 0.1) vs (0.9, 0.2), and
(3.0, 2.0) vs (3.5, 1.5)). Bisection from different brackets walks different
midpoints and lands on different dyadic grids -- 0.9/2^14 = 5.493e-05 spacing
versus 0.7/2^14 = 4.272e-05 -- so coinciding to one unit in the last place is
not something two independent searches do.

P91's Part C sharpens the puzzle rather than resolving it: varying n_probe by
10x, and swapping the probe grid from log-uniform-in-t to uniform-in-N, both
moved the reconstruction's boundary by EXACTLY 0.000e+00. A quantity that does
not move when the thing it is supposedly computed from is replaced wholesale is
not being computed from it.

FOUR MEASUREMENTS, no theorising. Each could come out either way.

  M1  EXACT VALUES. repr() of both returned floats and of both final brackets.
      "Agrees to 1 ulp" and "is the same float" are different facts and the
      printed 9 decimals cannot tell them apart.

  M2  THE MIDPOINT SEQUENCES. Both bisections instrumented to record every
      midpoint they tested. If the two paths are genuinely different and still
      end at the same float, that is one situation; if the paths CONVERGE onto
      shared values partway, that is a completely different one.

  M3  DO THE TWO PREDICATES AGREE POINTWISE? A fine scan in g_hat comparing
      p81.viability(...)['ok'] against viable_recon(...)['ok'] at every point.
      Two bisections hunting the SAME boolean flip will of course land close;
      the question is whether the flip itself sits at the same place.

  M4  WHERE IS EACH FLIP, REALLY? Both boundaries re-located at tol 1e-13
      instead of 1e-4. If the two true flips differ by, say, 1e-9 while both
      1e-4 bisections return the same float, the agreement in P91 was an
      artifact of the tolerance and NOT evidence about either implementation.
      If the two true flips agree to 1e-13 as well, the agreement is real and
      the question becomes why -- which M1-M3 should then answer.

WHAT THIS FILE WILL NOT DO: conclude that the boundary is reproduced. P91's
verdict stands withdrawn until the cause is named, and naming it is this file's
only job.
"""

import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p91 = _load("P91_boundary_through_the_reconstruction.py", "p91_probe")
p81 = _load("P81_background_viability.py", "p81_probe")

EDGES = (
    ("lambda=0", 0.0, (0.9, 0.2), (1.0, 0.1)),
    ("lambda=0.1", 0.1, (3.5, 1.5), (3.0, 2.0)),
)


def bisect_traced(f_ok, x_bad, x_good, tol_rel=1e-4, max_iter=200):
    """P91's bisection with every midpoint recorded. Same arithmetic, plus a log."""
    path = []
    for _ in range(max_iter):
        mid = 0.5 * (x_bad + x_good)
        r = f_ok(mid)
        if r["state"] == "unresolved":
            return None, path, (x_bad, x_good), "unresolved"
        path.append((mid, bool(r["ok"])))
        if r["ok"]:
            x_good = mid
        else:
            x_bad = mid
        if abs(x_good - x_bad) <= tol_rel * max(abs(mid), 1e-300):
            break
    return 0.5 * (x_bad + x_good), path, (x_bad, x_good), "ok"


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("p91 tightness probe -- naming the cause of a 1-ulp agreement")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    for label, lam, (rb, rg), (pb, pg) in EDGES:
        print("\n" + "=" * 78)
        print(f"EDGE {label}")
        print("=" * 78)

        xr, pr, br, _ = bisect_traced(lambda g, lm=lam: p91.viable_recon(g, lm), rb, rg)
        xp, pp, bp, _ = bisect_traced(lambda g, lm=lam: p81.viability(g, lm), pb, pg)

        # ---------------------------------------------------------- M1
        print("\n  M1 -- EXACT VALUES (repr, not 9 decimals)")
        print(f"    recon  bracket {(rb, rg)}  ->  {xr!r}")
        print(f"    P81    bracket {(pb, pg)}  ->  {xp!r}")
        print(f"    identical float: {xr == xp}")
        print(f"    recon final bracket: {br[0]!r} .. {br[1]!r}")
        print(f"    P81   final bracket: {bp[0]!r} .. {bp[1]!r}")

        # ---------------------------------------------------------- M2
        print("\n  M2 -- MIDPOINT SEQUENCES (last 6 of each)")
        print(f"    recon walked {len(pr)} midpoints, P81 walked {len(pp)}")
        shared = {round(m, 15) for m, _ in pr} & {round(m, 15) for m, _ in pp}
        print(f"    midpoints common to both paths: {len(shared)}")
        print(f"    {'recon midpoint':<26}{'ok':<8}{'P81 midpoint':<26}{'ok'}")
        for i in range(-6, 0):
            a = f"{pr[i][0]:.15f}" if len(pr) >= -i else ""
            ao = str(pr[i][1]) if len(pr) >= -i else ""
            b = f"{pp[i][0]:.15f}" if len(pp) >= -i else ""
            bo = str(pp[i][1]) if len(pp) >= -i else ""
            print(f"    {a:<26}{ao:<8}{b:<26}{bo}")

        # ---------------------------------------------------------- M3
        print("\n  M3 -- DO THE TWO PREDICATES AGREE POINTWISE?")
        lo, hi = min(xr, xp) * 0.995, max(xr, xp) * 1.005
        gs = np.linspace(lo, hi, 41)
        dis = []
        for g in gs:
            a_ok = p91.viable_recon(g, lam)
            b_ok = p81.viability(g, lam)
            if a_ok["state"] != "measured" or b_ok["state"] != "measured":
                continue
            if a_ok["ok"] != b_ok["ok"]:
                dis.append((g, a_ok["ok"], b_ok["ok"]))
        print(f"    scanned 41 points over [{lo:.6f}, {hi:.6f}]")
        print(f"    points where the two predicates DISAGREE: {len(dis)}")
        for g, a_, b_ in dis[:6]:
            print(f"      g={g:.9f}  recon={a_}  P81={b_}")

        # ---------------------------------------------------------- M4
        print("\n  M4 -- WHERE IS EACH FLIP REALLY (tol 1e-13, not 1e-4)?")
        fr, _p, _b, _s = bisect_traced(
            lambda g, lm=lam: p91.viable_recon(g, lm), rb, rg, tol_rel=1e-13
        )
        fp, _p2, _b2, _s2 = bisect_traced(
            lambda g, lm=lam: p81.viability(g, lm), pb, pg, tol_rel=1e-13
        )
        if fr is None or fp is None:
            print("    one side unresolved at tight tolerance -- not measured.")
            continue
        print(f"    recon true flip : {fr!r}")
        print(f"    P81   true flip : {fp!r}")
        rel = abs(fr / fp - 1.0)
        print(f"    relative difference of the TRUE flips: {rel:.6e}")
        print(f"    (P91 compared the tol=1e-4 answers and got {abs(xr / xp - 1.0):.3e})")
        if rel > 1e-6 >= abs(xr / xp - 1.0):
            print("    => THE 1-ULP AGREEMENT WAS AN ARTIFACT OF THE TOLERANCE.")
            print("       The two predicates flip in different places; the coarse")
            print("       bisections merely rounded to the same float.")
        elif rel <= 1e-9:
            print("    => the flips genuinely coincide to 1e-9 or better. The")
            print("       agreement is real and M1-M3 above say why.")
        else:
            print("    => flips differ at an intermediate level; report as measured.")

    print("\n" + "=" * 78)
    print("This file names a cause. It does NOT restore P91's verdict, which")
    print("stays withdrawn until the finding says what the cause was.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
