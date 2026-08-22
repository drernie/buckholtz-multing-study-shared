"""P102 -- build the interior-scanning bracket search FINDING_P101 named but didn't build.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P101 widened the a_today search bracket and found the measurable
Lambda range did NOT extend -- it SHRANK on the low end. Three grid points
that resolved under P100's narrower [300, 3e6] bracket
(Lambda = 1.194e-16, 2.154e-16, 3.888e-16) came back "not measured" under
the wider [10.46, 1e8] bracket. P101 diagnosed WHY, without resolving it:
every root-finder in this arc since P94 checks ONLY the two bracket
ENDPOINTS for a sign change before running brentq -- the interior is never
scanned. A wider bracket makes it MORE likely a real root hides between
same-signed endpoints, not less. P101 named this as a limitation, left it
genuinely open, and did not build the fix. This file builds it.

THE FIX, STATED BEFORE ANY CODE RUNS. Replace the two-point endpoint check
with a genuine interior scan: evaluate resid(a_today) at N log-spaced points
across the bracket (not just the two ends), find every adjacent-point sign
change among the FINITE evaluations, and hand each detected sub-interval to
brentq separately. This can find MULTIPLE roots where the old check could
find at most one (and often found none it should have). Multiple roots for
the SAME Lambda would themselves be new information -- a degenerate,
non-unique a_today solution -- and are reported as such, not silently
collapsed to "the first one found".

TWO STAGES, IN ORDER.
  STAGE A -- deep dive on exactly the 3 "lost" Lambda values from P101, at
    VERY fine resolution (3000 log-spaced points spanning the full ~7
    decades of the bracket, ~430/decade). Cheap (only 3 Lambda values) and
    decisive: either a hidden root is found, or the absence is now backed
    by a resolution P101's 2-point check never had.
  STAGE B -- re-scan the SAME 40-point Lambda grid used throughout
    P99-P101, this time with interior scanning at a coarser-but-still-far-
    finer-than-2-points resolution (300 log-spaced points/Lambda, ~43/decade)
    to see whether the fix changes the overall measurable-count picture
    against BOTH P100 (old narrow bracket, endpoint-only, 19/40) and P101
    (new wide bracket, endpoint-only, 16/40) -- and to check, honestly,
    whether any Lambda shows more than one root (flagged, not resolved).

CONTROLS, BEFORE TRUSTING A DIFFERENT ANSWER THAN P101's.
  (1) REGRESSION: the interior scanner, restricted to its own 2 endpoints
      only (n=2, degenerate case), must reproduce P101's own published
      "not measured" result for one of the 3 lost Lambda values -- proving
      this file's scanner behaves identically to the old code in the
      degenerate limit, so any DIFFERENT answer at higher n is from finer
      resolution, not a different algorithm.
  (2) REGRESSION: at fine resolution, the scanner must still reproduce
      FINDING_P100/P101's own published g values at the two long-standing
      regression Lambda points (2.084e-16, 3.000e-12) -- unchanged answers
      where the old check already worked correctly.

PRE-REGISTERED OUTCOMES for Stage A (the 3 lost Lambda values):
  HIDDEN-ROOT-CONFIRMED   >=1 of the 3 shows a genuine interior sign change
                          -> P101's masking hypothesis was correct. Locate
                          the root(s), check for multiplicity, report the
                          corrected g(Lambda) value(s).
  GENUINELY-EMPTY         all 3 show zero sign changes even at 3000-point
                          resolution -> not a search artifact. P101's open
                          question CLOSES as "no root, to this resolution"
                          (not a P95-style proof, but a completed check).
  MIXED                   some hidden, some empty -> reported per-Lambda,
                          not rounded to either extreme.

PRE-REGISTERED OUTCOMES for Stage B (the full 40-point grid):
  RECOVERS-P100           measurable count returns to >= P100's 19/40 ->
                          the coarse endpoint check was the whole story;
                          bracket WIDTH plus interior scanning together
                          recover what P100's narrow-but-endpoint-only
                          check happened to catch by luck of bracket
                          placement.
  STILL-BELOW-P100        measurable count stays < 19/40 even with interior
                          scanning -> something beyond bracket-check
                          coarseness also caps the range; named, not
                          assumed away.
  DEGENERATE              any Lambda shows > 1 sign change -> flagged as a
                          new structural fact (non-unique a_today), separate
                          from the count comparison above.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome. A cleanly resolved root with a passing out-of-sample check would
license a follow-up step to do that; it is not done here.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p81 = _load("P81_background_viability.py", "p81_for_a102")
p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_a102")
p99 = _load("P99_shape_of_H_across_epochs.py", "p99_for_a102")
p100 = _load("P100_shape_hardened_wide_scan.py", "p100_for_a102")
p101 = _load("P101_widened_a_today_search.py", "p101_for_a102")

shape_lcdm = p99.shape_lcdm
Z_FIT1, Z_FIT2, Z_CHECK = p99.Z_FIT1, p99.Z_FIT2, p99.Z_CHECK
solve_background_safe = p100.solve_background_safe
shape_at = p100.shape_at

A_TODAY_LO, A_TODAY_HI = p101.A_TODAY_LO_NEW, p101.A_TODAY_HI_NEW

LOST_LAMBDAS = (1.1938e-16, 2.1544e-16, 3.8882e-16)  # P101's own "not measured" trio
STAGE_A_N = 3000
STAGE_B_N = 300

# P100's own regression targets, re-quoted once more.
REGRESSION = {
    2.084e-16: 2.905e-06,
    3.000e-12: 1.616e-05,
}
REGRESSION_TOL = 5e-3

LAMBDA_LO_WIDE, LAMBDA_HI_WIDE = p100.LAMBDA_LO_WIDE, p100.LAMBDA_HI_WIDE
P100_MEASURABLE_COUNT = 19
P101_MEASURABLE_COUNT = 16


def resid_z1(s, a_today):
    sh = shape_at(s, a_today, Z_FIT1)
    return (sh - shape_lcdm(Z_FIT1)) if sh is not None else np.nan


def interior_scan_roots(lam_cc, a_lo, a_hi, n):
    """Scan n log-spaced points for sign changes of resid_z1, not just the 2 endpoints.

    Returns (roots, n_valid, n_total) where roots is a list of a_today values,
    one per detected sign change, each independently confirmed by its own
    brentq call on the bracketing sub-interval.
    """
    s = solve_background_safe(lam_cc)
    if s is None:
        return [], 0, n

    grid = np.geomspace(a_lo, a_hi, max(n, 2))
    with np.errstate(all="ignore"):
        vals = [resid_z1(s, a) for a in grid]
    valid = [(a, v) for a, v in zip(grid, vals, strict=True) if np.isfinite(v)]

    roots = []
    for (a_lo_i, v_lo_i), (a_hi_i, v_hi_i) in zip(valid, valid[1:], strict=False):
        if v_lo_i == 0.0:
            roots.append(a_lo_i)
            continue
        if v_lo_i * v_hi_i < 0:
            try:
                root = brentq(lambda a, s=s: resid_z1(s, a), a_lo_i, a_hi_i, xtol=1e-3, rtol=1e-12)
            except (ValueError, RuntimeError):
                continue
            roots.append(root)
    return roots, len(valid), n


def g_at_root(lam_cc, a_today):
    s = solve_background_safe(lam_cc)
    if s is None:
        return None
    sh2 = shape_at(s, a_today, Z_FIT2)
    if sh2 is None:
        return None
    return sh2 - shape_lcdm(Z_FIT2)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P102 -- interior-scanning bracket search (the fix P101 named but didn't build)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print(f"\n  bracket: [{A_TODAY_LO:.4e}, {A_TODAY_HI:.4e}] (P101's widened, corrected bracket)")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- n=2 (degenerate: endpoints only) must reproduce P101's own")
    print("'not measured' result for a lost Lambda -- same algorithm, same answer")
    print("-" * 78)
    lam_probe = LOST_LAMBDAS[0]
    roots_n2, valid_n2, _ = interior_scan_roots(lam_probe, A_TODAY_LO, A_TODAY_HI, 2)
    print(
        f"  Lambda={lam_probe:.4e}, n=2: valid endpoints={valid_n2}/2, roots found={len(roots_n2)}"
    )
    control1_ok = len(roots_n2) == 0
    print(f"  CONTROL 1 {'PASSES' if control1_ok else 'FAILS'} (expected 0 roots, matching P101)")
    if not control1_ok:
        print("  *** the n=2 degenerate case disagrees with P101's own published result.")
        print("  *** STOP -- this scanner is not a faithful generalization of the old check.")
        return 1

    print("\n" + "-" * 78)
    print("CONTROL 2 -- fine resolution must still reproduce FINDING_P100/P101's own")
    print("published g at the two long-standing regression Lambda values")
    print("-" * 78)
    reg_ok = True
    for lam, published in REGRESSION.items():
        roots, valid, _ = interior_scan_roots(lam, A_TODAY_LO, A_TODAY_HI, STAGE_B_N)
        if len(roots) != 1:
            print(f"    Lambda={lam:.4e}: found {len(roots)} roots (expected 1) -- MISMATCH")
            reg_ok = False
            continue
        g = g_at_root(lam, roots[0])
        if g is None:
            print(f"    Lambda={lam:.4e}: root found but g not measurable -- MISMATCH")
            reg_ok = False
            continue
        rel = abs(g / published - 1.0)
        ok = rel < REGRESSION_TOL
        reg_ok = reg_ok and ok
        print(
            f"    Lambda={lam:.4e}: published g={published:.4e}, this file g={g:.6e}, "
            f"rel={rel:.3e}  {'OK' if ok else 'MISMATCH'}"
        )
    print(f"\n    CONTROL 2 {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** STOP -- fine-resolution scanning disagrees with the long-standing")
        print("  *** regression targets. Find the bug before trusting Stage A/B below.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(
        f"STAGE A -- deep dive on P101's 3 'lost' Lambda values, n={STAGE_A_N} "
        f"(~{STAGE_A_N / 7:.0f} points/decade)"
    )
    print("-" * 78)
    stage_a_hits = []
    for lam in LOST_LAMBDAS:
        roots, valid, total = interior_scan_roots(lam, A_TODAY_LO, A_TODAY_HI, STAGE_A_N)
        print(f"\n  Lambda={lam:.4e}: {valid}/{total} points valid, {len(roots)} root(s) found")
        for r in roots:
            g = g_at_root(lam, r)
            print(f"    root a_today={r:.6f}  ->  g(Lambda)={g!r}")
            stage_a_hits.append((lam, r, g))
        if not roots:
            print("    -> zero sign changes even at this resolution")

    if stage_a_hits:
        print(
            f"\n  -> STAGE A VERDICT: HIDDEN-ROOT-CONFIRMED for "
            f"{len({h[0] for h in stage_a_hits})}/3 lost Lambda values."
        )
    else:
        print("\n  -> STAGE A VERDICT: GENUINELY-EMPTY. All 3 lost Lambda values show zero")
        print(f"     sign changes across {STAGE_A_N} log-spaced points -- not a search artifact.")

    # ==================================================================
    print("\n" + "-" * 78)
    print(
        f"STAGE B -- re-scan the same 40-point Lambda grid, n={STAGE_B_N} interior "
        f"points/Lambda (~{STAGE_B_N / 7:.0f}/decade)"
    )
    print("-" * 78)
    grid = np.geomspace(LAMBDA_LO_WIDE, LAMBDA_HI_WIDE, 40)
    print(f"\n    {'Lambda':<14}{'#roots':<8}{'a_today (first)':<18}{'g (first)'}")
    measurable = 0
    degenerate = []
    all_g_signs = []
    for lam in grid:
        roots, _valid, _total = interior_scan_roots(lam, A_TODAY_LO, A_TODAY_HI, STAGE_B_N)
        if not roots:
            print(f"    {lam:<14.4e}{'0':<8}{'not measured':<18}")
            continue
        measurable += 1
        if len(roots) > 1:
            degenerate.append((lam, len(roots)))
        g0 = g_at_root(lam, roots[0])
        all_g_signs.append((lam, g0))
        g_str = f"{g0:+.6e}" if g0 is not None else "not measurable"
        print(f"    {lam:<14.4e}{len(roots):<8}{roots[0]:<18.4f}{g_str}")

    print(f"\n    measurable: {measurable}/40")
    print(f"    (P100, old bracket, endpoint-only:  {P100_MEASURABLE_COUNT}/40)")
    print(f"    (P101, new bracket, endpoint-only:  {P101_MEASURABLE_COUNT}/40)")
    if degenerate:
        print(f"    DEGENERATE Lambda values (>1 root): {len(degenerate)}")
        for lam, n in degenerate:
            print(f"      Lambda={lam:.4e}: {n} roots")
    else:
        print("    no degenerate (multi-root) Lambda values found")

    sign_changes = sum(
        1
        for (_l1, g1), (_l2, g2) in zip(all_g_signs, all_g_signs[1:], strict=False)
        if g1 is not None and g2 is not None and (g1 > 0) != (g2 > 0)
    )

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if measurable >= P100_MEASURABLE_COUNT:
        print(f"  -> RECOVERS-P100. Interior scanning ({measurable}/40) matches or exceeds")
        print(f"     P100's own endpoint-only count ({P100_MEASURABLE_COUNT}/40) even though")
        print(
            f"     P101's endpoint-only check on this SAME wide bracket only found "
            f"{P101_MEASURABLE_COUNT}/40."
        )
        print("     The coarse endpoint check was masking real roots, exactly as diagnosed.")
    else:
        print(f"  -> STILL-BELOW-P100. Interior scanning ({measurable}/40) does not reach")
        print(f"     P100's own endpoint-only count ({P100_MEASURABLE_COUNT}/40).")
        print("     Something beyond bracket-check coarseness also caps the measurable range.")
    print(f"  sign changes of g(Lambda) across measurable points: {sign_changes}")
    if degenerate:
        print(f"  DEGENERATE: {len(degenerate)} Lambda value(s) have more than one a_today")
        print("     root for the SAME z_fit1 condition -- a new structural fact, reported")
        print("     separately, not silently collapsed to a single answer above.")
    print("  NO k[h/Mpc] number is quoted.")

    print("\n  NOT ESTABLISHED:")
    print(f"   * that {STAGE_A_N}/{STAGE_B_N}-point resolution is fine enough to catch every")
    print("     possible hidden root -- a genuinely pathological resid(a_today) could still")
    print("     hide a narrower feature between scan points.")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
