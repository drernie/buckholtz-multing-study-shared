"""Does P81's H-MONOTONICITY clause become grid-activated at large n_probe?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

P92's lambda=0.1 ladder produced a result its convergence control was built to
be able to reject, and it rejected: P81's boundary does NOT converge to the
event-located one. It passes THROUGH it near n_probe=3000 and settles 4.136e-07
away.

    n_probe   g_crit P81         vs exact limit
    300       2.752360021571     2.163e-04
    1000      2.751773338901     3.090e-06
    3000      2.751764836559     9.746e-12   <- crossing, not convergence
    10000     2.751763820128     3.694e-07
    30000     2.751763715539     4.074e-07
    100000    2.751763698415     4.136e-07

THE DIRECTION RULES OUT THE OBVIOUS EXPLANATION. A sampled minimum is always
>= the continuous one, so P81 should call MORE points viable than the exact
predicate and its boundary should sit at LARGER g_hat. It sits at SMALLER
g_hat -- P81 rejects EARLIER. "The grid steps over a dip" cannot produce that.

THE HYPOTHESIS UNDER TEST. P81's predicate has a SECOND grid-dependent clause
that has never been examined: H monotonicity, tested as

    mono = max(np.diff(H)) <= 1e-9 * max(H)

on the same probe grid. At lambda != 0 the scalar oscillates -- 216 turning
points at the lambda=0.1 boundary, 332 at lambda=1, 562 at lambda=10 (P92 Part
B) -- and H is not exactly monotone through an oscillation. A coarse grid
cannot resolve those tiny rises; a fine one can. If so, raising n_probe ACTIVATES
a clause that was dormant, and the boundary moves left. That would also mean
P91's Part 0, which verified that min(1-g*phibar) is the binding clause, checked
it only AT THE DEFAULT GRID -- so its licence to compare is narrower than stated.

THREE MEASUREMENTS. No bisection is needed: viability() already returns
min_M, H_monotone and worst_H_rise_rel on every measured point.

  M1  THE DECISIVE WINDOW. One g_hat chosen strictly BETWEEN the n=100000
      boundary and the n=3000 boundary. At that point n=3000 must say viable and
      n=100000 must say not-viable -- and the `why` string says which clause did
      it. This single column decides the hypothesis.

  M2  THE MECHANISM, QUANTITATIVELY. worst_H_rise_rel against n_probe at a point
      just BELOW each exact flip (viable, so every clause is still passing).
      If the hypothesis holds this quantity GROWS with n_probe and approaches
      or crosses the 1e-9 threshold.

  M3  THE NEGATIVE CONTROL, and it is what makes M2 mean anything. lambda=0 has
      EXACTLY ZERO turning points (P92 Part B), so H is smooth there and
      worst_H_rise_rel must NOT grow with n_probe. If it grows at lambda=0 too,
      the effect is not oscillation-driven and the hypothesis is wrong even if
      M1 and M2 look favourable.

PRE-REGISTERED OUTCOMES:
  H-GRID-ACTIVATED  M1 shows "H not monotone" among the failures at large
                    n_probe but not at n=3000, AND M2 grows with n_probe at
                    lambda != 0, AND M3 does not grow at lambda = 0.
  MIN-M-ONLY        M1 shows min(1-g*phibar) at every n_probe -> the hypothesis
                    is REFUTED and the direction of the discrepancy stays
                    unexplained. Say so; do not substitute another story.
  MIXED             anything else -> report exactly what was seen, name it
                    unexplained, and do not round it toward either outcome.

WHAT THIS CANNOT DO: it diagnoses P81's predicate. It says nothing about whether
the shared EQUATIONS are right, nothing observational, nothing about MULTING.
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


p81 = _load("P81_background_viability.py", "p81_clause")

LADDER = (300, 1000, 3000, 10000, 30000, 100000)

# Exact event-located flips, from P92 Part B. Quoted, not recomputed -- this
# file diagnoses P81 and does not need to re-derive the reconstruction.
EXACT = {0.0: 0.738212214739, 0.1: 2.751764836585, 1.0: 3.518052822000, 10.0: 4.733977969}
TURNS = {0.0: 0, 0.1: 216, 1.0: 332, 10.0: 562}

# strictly between P81's n=100000 boundary (2.751763698415) and its n=3000
# boundary (2.751764836559), so the two must disagree about it
WINDOW_LAM, WINDOW_G = 0.1, 2.7517642


def main() -> int:
    print("=" * 78)
    print("p92 clause probe -- is P81's H-monotonicity clause grid-activated?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("M1 -- THE DECISIVE WINDOW")
    print("-" * 78)
    print(f"  lambda = {WINDOW_LAM:g}, g_hat = {WINDOW_G:.10f}, chosen strictly between")
    print("  P81's n=100000 boundary (2.751763698415) and its n=3000 boundary")
    print("  (2.751764836559). n=3000 must call it viable and n=100000 must not;")
    print("  the `why` string says WHICH CLAUSE did it.")
    print(f"\n    {'n_probe':<10}{'ok':<8}{'min_M':<14}{'H_mono':<9}{'worst_H_rise':<15}{'why'}")
    saw_h_fail, saw_h_pass_at_3000 = False, False
    for npb in LADDER:
        r = p81.viability(WINDOW_G, WINDOW_LAM, n_probe=npb)
        if r["state"] != "measured":
            print(f"    {npb:<10}{'-':<8}{'unresolved -- ' + r['why']}")
            continue
        why = r["why"]
        if "H not monotone" in why:
            saw_h_fail = True
        if npb == 3000 and "H not monotone" not in why:
            saw_h_pass_at_3000 = True
        print(
            f"    {npb:<10}{str(r['ok']):<8}{r['min_M']:<14.9f}"
            f"{str(r['H_monotone']):<9}{r['worst_H_rise_rel']:<15.3e}{why[:34]}"
        )
    print(f"\n    'H not monotone' appears at some n_probe : {saw_h_fail}")
    print(f"    and does NOT appear at n=3000            : {saw_h_pass_at_3000}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("M2 -- THE MECHANISM, QUANTITATIVELY")
    print("-" * 78)
    print("  worst_H_rise_rel just BELOW each exact flip, where the point is")
    print("  still viable so every clause is passing. P81's threshold is 1e-9.")
    print(f"\n    {'lambda':<9}{'turns':<8}" + "".join(f"n={n:<12}" for n in LADDER))
    grows = {}
    for lam, gx in EXACT.items():
        g = gx * (1.0 - 1e-7)
        row, vals = [], []
        for npb in LADDER:
            r = p81.viability(g, lam, n_probe=npb)
            if r["state"] != "measured":
                row.append(f"{'unres':<14}")
                continue
            vals.append(r["worst_H_rise_rel"])
            row.append(f"{r['worst_H_rise_rel']:<14.3e}")
        grows[lam] = (vals[-1] / vals[0]) if len(vals) == len(LADDER) and vals[0] > 0 else None
        print(f"    {lam:<9g}{TURNS.get(lam, '?'):<8}" + "".join(row))
    print(f"\n    {'lambda':<9}{'growth over the ladder (last/first)'}")
    for lam, gr in grows.items():
        print(f"    {lam:<9g}{gr if gr is None else f'{gr:.3g}x'}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("M3 -- THE NEGATIVE CONTROL, which is what makes M2 mean anything")
    print("-" * 78)
    print("  lambda=0 has EXACTLY ZERO turning points (P92 Part B), so H is")
    print("  smooth and worst_H_rise_rel must NOT grow with n_probe. If it grows")
    print("  there too, the effect is not oscillation-driven and the hypothesis")
    print("  is wrong even where M1 and M2 look favourable.")
    g0 = grows.get(0.0)
    osc = [grows[lam] for lam in (0.1, 1.0, 10.0) if grows.get(lam) is not None]
    print(f"\n    lambda=0    growth: {g0 if g0 is None else f'{g0:.3g}x'}   (0 turning points)")
    for lam in (0.1, 1.0, 10.0):
        gr = grows.get(lam)
        print(
            f"    lambda={lam:<5g}growth: {gr if gr is None else f'{gr:.3g}x'}"
            f"   ({TURNS.get(lam)} turning points)"
        )
    control_ok = g0 is not None and g0 < 10.0
    osc_grow = bool(osc) and all(v > 10.0 for v in osc)
    print(f"\n    lambda=0 stays flat (< 10x)            : {control_ok}")
    print(f"    every oscillating lambda grows (> 10x) : {osc_grow}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if saw_h_fail and saw_h_pass_at_3000 and osc_grow and control_ok:
        print("  -> H-GRID-ACTIVATED. Raising n_probe switches on a clause that was")
        print("     dormant at the default grid. Two consequences:")
        print("     * the lambda!=0 discrepancy P92 found is explained, and its")
        print("       direction -- P81 rejecting EARLIER -- follows, since a")
        print("       clause that only ever ADDS failures moves the boundary left;")
        print("     * FINDING_P91's Part 0 verified the binding clause AT THE")
        print("       DEFAULT GRID ONLY, so its licence to compare is narrower")
        print("       than stated and must be re-scoped.")
    elif not saw_h_fail:
        print("  -> MIN-M-ONLY. 'H not monotone' never appears, so the hypothesis")
        print("     is REFUTED. The direction of P92's discrepancy -- P81")
        print("     rejecting EARLIER than the exact predicate -- remains")
        print("     UNEXPLAINED, and no substitute story is offered here.")
    else:
        print("  -> MIXED. The pieces do not line up:")
        print(f"       H-clause seen at some n_probe : {saw_h_fail}")
        print(f"       absent at n=3000              : {saw_h_pass_at_3000}")
        print(f"       oscillating lambdas all grow  : {osc_grow}")
        print(f"       lambda=0 control stays flat   : {control_ok}")
        print("     Reported as seen. Not rounded toward either outcome.")

    print("\n  NOT ESTABLISHED:")
    print("   * anything about whether the shared EQUATIONS are right.")
    print("   * anything observational. Gate 1 holds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
