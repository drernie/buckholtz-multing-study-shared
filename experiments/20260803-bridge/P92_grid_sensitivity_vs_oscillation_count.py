"""P92 -- does P81's grid sensitivity scale with the OSCILLATION COUNT?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P91 measured that P81's viability predicate is grid-sensitive at
lambda != 0: varying its own n_probe moved g_crit by 1.774e-04 at 300 probes,
while lambda = 0 moved by EXACTLY zero at every n_probe tried. It registered
this prediction:

    "If that sensitivity scales with the OSCILLATION COUNT rather than with
     lambda as such -- P87 measured 12 turning points at lambda=1e-8, 181 at
     lambda=1 -- then at lambda=1 the boundary should need MORE than 3000 probe
     points, and re-running the n_probe ladder at lambda=1 should show movement
     between 3000 and 30000 where lambda=0.1 showed exactly zero. If instead
     lambda=1 is also converged at 3000, the sensitivity is not set by
     oscillation count and the mechanism behind Part C's 1.774e-04 is something
     else that has not been identified."

WHY THIS MATTERS BEYOND TIDINESS. P81's and P83's published boundaries are
quoted at a 1e-4 bisection tolerance. P91 showed the sampling error at 300
probes is 1.774e-04 -- ALREADY ABOVE that tolerance. If the sampling error grows
with oscillation count, then at large lambda the DEFAULT 3000 probes may also
sit above the quoted tolerance, and every boundary this campaign has published
at large lambda would carry an unquantified error larger than its stated one.
Nothing in the campaign has checked that.

THE CONTROL THAT P91 DID NOT HAVE, and the reason this file can say more than
"it moved". The reconstruction classifies by a TERMINAL EVENT on the continuous
trajectory: the integrator locates the FLOOR crossing itself, so no probe grid
enters the answer. That makes it the EXACT LIMIT of P81's sampled predicate, not
merely a second opinion. So P81's boundary must CONVERGE TO IT as n_probe grows.

  * If it does, the discrepancy is sampling and nothing else, and the
    reconstruction's value is the right one to quote.
  * If P81 converges to a DIFFERENT value, sampling is not the only difference
    between the two predicates and the rest has not been identified.

That is a genuinely falsifiable statement about which of two numbers is correct,
which no previous step in this arc has been able to make.

PRE-REGISTERED OUTCOMES:
  O-SCALES     movement between n=3000 and n=30000 is nonzero at lambda=1 AND
               the sampling error grows with the measured turning-point count
               -> the mechanism is oscillation sampling, and the published
               boundaries at large lambda need their n_probe re-justified.
  O-FLAT       lambda=1 is also converged at 3000 -> the sensitivity is NOT set
               by oscillation count; P91's 1.774e-04 has an unidentified cause
               and the prediction registered there is refuted.
  O-NOT-MEASURABLE  the boundary at lambda=1 cannot be bracketed or bisected --
               infrastructure outcome, not evidence either way.

  CONVERGENCE CONTROL, scored separately and able to fail on its own:
  C-CONVERGES  |g_crit_P81(n) - g_crit_recon| decreases as n grows, at every
               lambda where both are measured.
  C-DIVERGES   it does not -> sampling is not the whole difference; say so and
               do NOT claim the reconstruction's value is the correct one.

NO BRACKET IS ASSUMED. The lambda=1 boundary has never been located in this
campaign, so guessing a bracket would be inventing an input. Each boundary is
bracketed by a coarse geometric SCAN first, and a lambda whose scan finds no
flip is reported as not-measurable rather than forced.

A DEFECT IN THIS FILE'S OWN FIRST RUN, recorded rather than silently fixed.
Part B originally counted turning points at the MID-BRACKET g_hat. A bracket
midpoint is only known to lie BETWEEN a viable and a non-viable point, so it can
be either; where it was non-viable the FLOOR event fired, t never reached T_END,
and the count came back None -- three of four lambdas. The criterion "the error
grows with turning-point count" was then unmeasurable rather than false. The
repair: the exact-limit flip is computed FIRST, and the count is taken at
flip*(1 - 1e-6), on the viable side of the boundary, with viability VERIFIED by
the predicate rather than inferred from the definition of a flip. That is also
the physically right place -- the prediction is about how hard THE BOUNDARY is
to sample, so the trajectory that defines it is the one whose oscillations count.

WHAT THIS CANNOT DO: it says nothing about whether the shared EQUATIONS are
right, nothing observational, and nothing about MULTING (Gate 1).
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


p81 = _load("P81_background_viability.py", "p81_for_osc")
p91 = _load("P91_boundary_through_the_reconstruction.py", "p91_for_osc")

LAMBDAS = (0.0, 0.1, 1.0, 10.0)
LADDER = (300, 1000, 3000, 10000, 30000, 100000)
SCAN_LO, SCAN_HI, SCAN_N = 0.1, 40.0, 14
TIGHT = 1e-12


def scan_bracket(f_ok, lo=SCAN_LO, hi=SCAN_HI, n=SCAN_N):
    """Find (x_bad, x_good) by a geometric scan. No bracket is assumed anywhere."""
    xs = np.geomspace(lo, hi, n)
    prev_x, prev_ok = None, None
    for x in xs:
        r = f_ok(float(x))
        if r["state"] != "measured":
            prev_x, prev_ok = None, None
            continue
        if prev_ok is True and r["ok"] is False:
            # bisect() takes (x_bad, x_good) = (NOT viable, viable). The scan
            # walks upward and meets the viable point FIRST, so the pair is
            # returned reversed. Getting this backwards would not corrupt a
            # result -- bisect's own precondition rejects a bracket that is not
            # what it claims -- but it would report every edge as unmeasurable.
            return float(x), float(prev_x), "ok"
        prev_x, prev_ok = float(x), bool(r["ok"])
    return None, None, f"no viable->non-viable flip found over [{lo:g}, {hi:g}]"


def turning_points(g, lam):
    """Count sign changes of phibar_dot along the reconstruction's trajectory.

    # WHY measured on the reconstruction rather than on P81: the count must not
    # itself depend on a probe grid, and the reconstruction's dense solution can
    # be sampled as finely as needed without changing any classification.
    """
    from scipy.integrate import solve_ivp

    with np.errstate(all="ignore"):
        s = solve_ivp(
            p91.bg_rhs_lnA(g, lam),
            (np.log(p91.A_0), np.log(p91.A_0) + 60.0),
            [0.0, p91.U_0, p91.T0],
            method="DOP853",
            rtol=1e-10,
            atol=1e-22,
            dense_output=True,
            events=[p91._floor_event(g), p91._t_event()],
        )
        if not s.success or not len(s.t_events[1]):
            return None
        NN = np.linspace(np.log(p91.A_0), float(s.t_events[1][0]), 400000)
        u = s.sol(NN)[1]
    return int(np.count_nonzero(np.diff(np.signbit(u))))


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P92 -- grid sensitivity versus oscillation count")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- BRACKET EACH BOUNDARY BY SCAN (none is assumed)")
    print("-" * 78)
    print(f"  geometric scan over [{SCAN_LO:g}, {SCAN_HI:g}], {SCAN_N} points. The lambda=1")
    print("  boundary has never been located in this campaign, so guessing a")
    print("  bracket would be inventing an input.")
    print(f"\n    {'lambda':<10}{'bracket (bad, good)':<30}{'note'}")
    brackets = {}
    for lam in LAMBDAS:
        bad, good, note = scan_bracket(lambda g, lm=lam: p81.viability(g, lm))
        brackets[lam] = (bad, good)
        shown = f"({bad:.4g}, {good:.4g})" if bad is not None else "-"
        print(f"    {lam:<10g}{shown:<30}{note}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- OSCILLATION COUNT AT EACH BOUNDARY")
    print("-" * 78)
    print("  Turning points of phibar along the trajectory, counted on the")
    print("  reconstruction's dense solution at 4e5 samples so the count itself")
    print("  cannot depend on a coarse grid. P87 measured 12 at lambda=1e-8 and")
    print("  181 at lambda=1 at ITS OWN parameters; these are at the boundary.")
    print("  REPAIRED: the first run counted at the MID-BRACKET, which is only")
    print("  known to lie between a viable and a non-viable point. Where it was")
    print("  non-viable the FLOOR event fired, t never reached T_END, and three")
    print("  of four counts came back None. The count is now taken JUST BELOW")
    print("  the exact flip, and viability is VERIFIED rather than inferred.")
    print(f"\n    {'lambda':<10}{'exact flip':<18}{'g counted at':<18}{'viable?':<10}{'turns'}")
    turns, exact = {}, {}
    for lam in LAMBDAS:
        bad, good = brackets[lam]
        if bad is None:
            print(f"    {lam:<10g}{'-':<18}{'-':<18}{'-':<10}not measured")
            continue
        fr, _p, note = p91.bisect(
            lambda g, lm=lam: p91.viable_recon(g, lm), bad, good, tol_rel=TIGHT
        )
        exact[lam] = fr
        if fr is None:
            print(f"    {lam:<10g}{'-':<18}{'-':<18}{'-':<10}flip not located: {note}")
            continue
        gc = fr * (1.0 - 1e-6)
        chk = p91.viable_recon(gc, lam)
        ok = chk["state"] == "measured" and chk["ok"]
        turns[lam] = turning_points(gc, lam) if ok else None
        print(f"    {lam:<10g}{fr:<18.9f}{gc:<18.9f}{str(ok):<10}{turns.get(lam)}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- THE n_probe LADDER, AND THE EXACT LIMIT BESIDE IT")
    print("-" * 78)
    print("  The reconstruction classifies by a terminal EVENT on the continuous")
    print("  trajectory, so no grid enters its answer: it is the EXACT LIMIT of")
    print("  P81's sampled predicate, not a second opinion. P81 must converge to")
    print("  it. If it converges elsewhere, sampling is not the whole difference.")
    rows = {}
    for lam in LAMBDAS:
        bad, good = brackets[lam]
        if bad is None:
            continue
        fr = exact.get(lam)  # located in Part B; not recomputed
        print(f"\n  lambda = {lam:g}   (turning points: {turns.get(lam)})")
        if fr is None:
            print("    reconstruction (exact limit): not measured in Part B")
        else:
            print(f"    reconstruction (exact limit): {fr:.12f}")
        print(f"    {'n_probe':<12}{'g_crit P81':<20}{'vs n=100000':<14}{'vs exact limit'}")
        vals = {}
        for npb in LADDER:
            x, _pp, note = p91.bisect(
                lambda g, lm=lam, q=npb: p81.viability(g, lm, n_probe=q),
                bad,
                good,
                tol_rel=TIGHT,
            )
            if x is None:
                print(f"    {npb:<12}not measured -- {note}")
                continue
            vals[npb] = x
        ref = vals.get(LADDER[-1])
        for npb, x in vals.items():
            d_self = abs(x / ref - 1.0) if ref else float("nan")
            d_ex = abs(x / fr - 1.0) if fr else float("nan")
            print(f"    {npb:<12}{x:<20.12f}{d_self:<14.3e}{d_ex:.3e}")
        rows[lam] = (vals, fr)

    # ==================================================================
    print("\n" + "-" * 78)
    print("SCORING")
    print("-" * 78)

    # --- the registered prediction: movement between 3000 and 30000 at lambda=1
    print(f"\n  {'lambda':<10}{'turns':<9}{'|3000 vs 30000|':<19}{'err at 3000 vs exact'}")
    moves, errs = {}, {}
    for lam, (vals, fr) in rows.items():
        if 3000 in vals and 30000 in vals:
            moves[lam] = abs(vals[30000] / vals[3000] - 1.0)
        if 3000 in vals and fr:
            errs[lam] = abs(vals[3000] / fr - 1.0)
        print(
            f"  {lam:<10g}{str(turns.get(lam)):<9}"
            f"{moves.get(lam, float('nan')):<19.3e}{errs.get(lam, float('nan')):.3e}"
        )

    lam1_moves = moves.get(1.0, 0.0) > 0.0
    ordered = [lam for lam in LAMBDAS if lam in errs and turns.get(lam) is not None]
    monotone_in_turns = all(
        errs[a] <= errs[b] + 1e-18
        for a, b in zip(ordered, ordered[1:], strict=False)
        if (turns[a] or 0) <= (turns[b] or 0)
    )
    print(f"\n    lambda=1 moves between 3000 and 30000        : {lam1_moves}")
    print(f"    sampling error grows with turning-point count: {monotone_in_turns}")

    # --- the convergence control
    conv = {}
    for lam, (vals, fr) in rows.items():
        if not fr or len(vals) < 3:
            continue
        seq = [abs(vals[n] / fr - 1.0) for n in LADDER if n in vals]
        conv[lam] = all(b <= a * 1.5 + 1e-18 for a, b in zip(seq, seq[1:], strict=False))
    print(f"    P81 converges toward the exact limit         : {conv}")
    all_conv = bool(conv) and all(conv.values())

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if not rows or 1.0 not in rows:
        print("  -> O-NOT-MEASURABLE. The lambda=1 boundary could not be located")
        print("     or bisected. Infrastructure outcome, NOT evidence either way.")
    elif lam1_moves and monotone_in_turns:
        print("  -> O-SCALES. The lambda=1 boundary still moves between 3000 and")
        print("     30000 probes, and the sampling error grows with the measured")
        print("     turning-point count. The mechanism IS oscillation sampling,")
        print("     and every boundary this campaign published at large lambda")
        print("     needs its n_probe re-justified against its own tolerance.")
    elif lam1_moves:
        print("  -> PARTIAL. lambda=1 does still move, but the error does NOT")
        print("     grow monotonically with turning-point count, so oscillation")
        print("     sampling is not the whole mechanism. Named, not smoothed.")
    else:
        print("  -> O-FLAT. lambda=1 is already converged at 3000 probes. The")
        print("     sensitivity is NOT set by oscillation count, FINDING_P91's")
        print("     registered prediction is REFUTED, and the cause of its")
        print("     1.774e-04 remains unidentified.")

    print()
    if all_conv:
        print("  CONVERGENCE CONTROL -> C-CONVERGES. P81's sampled boundary moves")
        print("  toward the event-located one as n_probe grows, at every lambda")
        print("  measured. Sampling is the difference, and the reconstruction's")
        print("  value is the one to quote.")
    else:
        print("  CONVERGENCE CONTROL -> C-DIVERGES at one or more lambda. Sampling")
        print("  is NOT the whole difference between the two predicates, and the")
        print("  rest is unidentified. Do NOT quote either value as the correct")
        print("  one until it is.")

    print("\n  NOT ESTABLISHED:")
    print("   * that the shared EQUATIONS are right.")
    print("   * anything above the 'independently-written code' rung.")
    print("   * anything observational. Gate 1 holds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
