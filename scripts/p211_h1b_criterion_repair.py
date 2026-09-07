"""P211 -- repair H1b's decision bands (FL Step 4a follow-through).

P210 found two defects in H1b's 2026-07-17 pre-registration:

    KILL    :  r < 0.15  AND  p > 0.20      <- clauses disagree; dead band
    PROMOTE :  r > 0.30  AND  p < 0.10      <- p-clause never binds
    (nothing specified for 0.15 <= r <= 0.30)

WHY AMENDING IS LEGITIMATE HERE. Changing a decision rule after seeing a
result is p-hacking. Changing one before any data exists is repairing a
broken instrument. H1b has produced NO data -- its folder holds claim.md,
estimand.md and decision.md, with no metrics, no controls, no results.
That is checkable, and the amendment is dated and additive: the original
criteria are NOT rewritten.

THE REPAIR. Replace two 2-clause rules that can both fail with one
interval rule that partitions the outcome space completely. The hypothesis
is directional (claim.md: "correlates POSITIVELY"), so one-sided bounds:

    KILL         : upper 95% one-sided bound on r  <  0.15
    PROMOTE      : lower 95% one-sided bound on r  >  0.30
    INCONCLUSIVE : otherwise

Both original numbers are kept. No gaps, no overlaps, no dead band, and
the behaviour is now monotone in N -- more data makes a verdict MORE
reachable, not less, which is what the old rule got backwards.

This script derives the consequences, including the one the original
design never checked: the sample size its own KILL rule requires.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np

KILL_R = 0.15  # kept from the original pre-registration
PROMOTE_R = 0.30  # kept from the original pre-registration
K_CONTROLS = 2  # M_true, dynamical state
Z_95 = 1.6448536269514722  # one-sided 95%
SAMPLE_SIZES = (100, 138, 200, 300, 500)


def se_z(n: int, k: int = K_CONTROLS) -> float:
    """Standard error of the Fisher z-transformed partial correlation."""
    return 1.0 / np.sqrt(n - k - 3)


def upper_bound(r: float, n: int) -> float:
    """Upper one-sided 95% bound on the true r, given observed r."""
    return float(np.tanh(np.arctanh(r) + Z_95 * se_z(n)))


def lower_bound(r: float, n: int) -> float:
    """Lower one-sided 95% bound on the true r, given observed r."""
    return float(np.tanh(np.arctanh(r) - Z_95 * se_z(n)))


def verdict(r: float, n: int) -> str:
    if upper_bound(r, n) < KILL_R:
        return "KILL"
    if lower_bound(r, n) > PROMOTE_R:
        return "PROMOTE"
    return "INCONCLUSIVE"


def min_n_for_kill() -> int:
    """Smallest N at which KILL can fire even for a perfectly null r = 0."""
    n = K_CONTROLS + 4
    while upper_bound(0.0, n) >= KILL_R:
        n += 1
        if n > 100_000:
            raise RuntimeError("KILL unattainable at any sample size")
    return n


def min_observed_r_for_promote(n: int) -> float:
    """Smallest observed r whose lower bound clears PROMOTE_R."""
    return float(np.tanh(np.arctanh(PROMOTE_R) + Z_95 * se_z(n)))


def section(t: str) -> None:
    print(f"\n{'=' * 72}\n{t}\n{'=' * 72}")


def main() -> int:
    section("P211 -- repaired decision bands for H1b")

    # ---- PC1: the bounds must bracket the point estimate -----------------
    for n in SAMPLE_SIZES:
        for r in (-0.5, 0.0, 0.2, 0.45, 0.8):
            assert lower_bound(r, n) < r < upper_bound(r, n), (r, n)
    print("\nPC1 [positive control] lower < observed < upper for every (r, N) probed. PASSES.")

    # ---- PC2: the partition must be complete and disjoint ----------------
    section("PC2 -- is the new rule a complete, disjoint partition?")
    grid = np.linspace(-0.95, 0.95, 3801)
    for n in SAMPLE_SIZES:
        verdicts = [verdict(float(r), n) for r in grid]
        assert all(v in {"KILL", "PROMOTE", "INCONCLUSIVE"} for v in verdicts)
        # exactly one verdict per r is guaranteed by construction (if/elif);
        # what must be checked is that KILL and PROMOTE never overlap.
        overlap = [
            float(r)
            for r in grid
            if upper_bound(float(r), n) < KILL_R and lower_bound(float(r), n) > PROMOTE_R
        ]
        assert not overlap, f"KILL and PROMOTE overlap at N={n}: {overlap[:3]}"
        counts = {v: verdicts.count(v) for v in ("KILL", "INCONCLUSIVE", "PROMOTE")}
        print(f"  N={n:4d}  {counts}  no overlap, no gap")
    print("\n  Every possible r maps to exactly one verdict. The dead band is gone.")

    # ---- The consequence the original design never derived ---------------
    section("SAMPLE SIZE -- what the repaired KILL actually requires")
    n_min = min_n_for_kill()
    print(f"\n  KILL is unattainable below N = {n_min}, even for a perfectly null r = 0.")
    print(f"  At N = 100 the best possible upper bound is {upper_bound(0.0, 100):.4f} > {KILL_R}.")
    print("  claim.md specifies only 'N > 100'. That is NOT enough for its own KILL rule.")
    assert upper_bound(0.0, 100) > KILL_R
    assert upper_bound(0.0, n_min) < KILL_R

    section("WHAT EACH VERDICT NOW COSTS")
    print(f"  {'N':>5s} {'KILL possible?':>15s} {'max r for KILL':>16s} {'min r for PROMOTE':>19s}")
    for n in SAMPLE_SIZES:
        ok = upper_bound(0.0, n) < KILL_R
        if ok:
            hi = grid[[upper_bound(float(r), n) < KILL_R for r in grid]].max()
            kill_cell = f"{hi:.4f}"
        else:
            kill_cell = "unattainable"
        print(
            f"  {n:5d} {'yes' if ok else 'NO':>15s} {kill_cell:>16s} "
            f"{min_observed_r_for_promote(n):19.4f}"
        )

    # ---- Sensitivity: the KILL bar is a SCIENTIFIC choice, not a stats one
    section("SENSITIVITY -- N required if the KILL threshold were relaxed")
    print("  KILL at 0.15 means 'we can rule out an effect as large as r=0.15'.")
    print("  How large that bar should be is a judgement about what counts as")
    print("  'no effect' -- NOT a statistical question, and not decided here.")
    print("  What the statistics can say is what each choice costs:\n")
    print(f"  {'KILL bar':>9s} {'min N for KILL':>15s} {'max r for KILL at N=138':>25s}")
    for bar in (0.10, 0.15, 0.20, 0.25, 0.30):
        n = K_CONTROLS + 4
        while float(np.tanh(Z_95 * se_z(n))) >= bar:
            n += 1
        best = float(np.tanh(np.arctanh(bar) - Z_95 * se_z(138)))
        cell = f"{best:.4f}" if best > -1 and 138 >= n else "unattainable"
        print(f"  {bar:9.2f} {n:15d} {cell:>25s}")
    print("\n  Reading: relaxing the bar to 0.20 makes KILL reachable at N>=70 and")
    print("  much easier at any N -- at the cost of a weaker claim when it fires.")

    section("VERDICT ON THE REPAIR")
    print("  Fixed: the dead band (KILL's two clauses could both fail) and the")
    print("  undefined middle (0.15-0.30 now returns INCONCLUSIVE explicitly).")
    print("  Behaviour is now monotone in N -- more data narrows the interval and")
    print("  makes a decisive verdict MORE reachable. The old rule did the reverse.")
    print()
    print("  NEWLY EXPOSED, and it is a real constraint rather than a repair:")
    print(f"  the design's own 'N > 100' cannot deliver a KILL. N >= {n_min} is")
    print("  required for KILL to be reachable at all. If the eventual sample")
    print("  cannot reach that, say so BEFORE running -- a test that can only")
    print("  return PROMOTE or INCONCLUSIVE is not a test of the claim.")
    print()
    print("  STILL OPEN: the structural floor (P210). A WHIM-free but correlated")
    print("  predictor could clear PROMOTE through covariance alone -- NR-010 went")
    print("  from raw r=0.021 to partial r=-0.701 that way. Needs the data.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
