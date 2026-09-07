"""P212 -- H1b AMENDMENT 2: KILL bar 0.15 -> 0.20, sign-reversed subtype,
and a feasibility check on the frozen structural-floor null models.

Three changes, all made BEFORE any data exists.

1. KILL bar relaxed 0.15 -> 0.20 (user decision, 2026-09-07). This is a
   scientific judgement about the smallest effect worth calling "not
   nothing", not a statistical one. P211 tabulated its cost; this applies
   it. Consequence: minimum N for a reachable KILL drops 124 -> 71.

2. NEW SUBTYPE: `KILL - opposite-sign signal`. The hypothesis is
   directional (positive), so one-sided bounds put a strongly NEGATIVE
   result into KILL. Formally right -- the positive claim is refuted --
   but it conflates "no effect" with "strong effect the other way", and
   six months later a bare `H1b KILLED` would have lost that distinction.

   The proposed trigger was `L_95 < 0`. REJECTED as too weak: at N=138
   even r = -0.01 gives L_95 = -0.151 < 0, so the subtype would fire on
   noise. Used instead the MIRROR of PROMOTE:

        opposite-sign  <=>  U_95(r) < -PROMOTE_R

   exactly as demanding negatively as PROMOTE is positively, and a strict
   SUBSET of KILL rather than a fourth verdict.

3. Feasibility of the frozen structural-floor null models. Freezing the
   ALGORITHM before data removes a real degree of freedom (choosing the
   permutation scheme after seeing the structure). But a stratified
   permutation is only meaningful if strata are not so fine that nothing
   can permute within them. That is checkable now, from N alone.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np

KILL_R_OLD = 0.15
KILL_R = 0.20  # AMENDMENT 2
PROMOTE_R = 0.30
K_CONTROLS = 2
Z_95 = 1.6448536269514722
SAMPLE_SIZES = (71, 100, 124, 138, 200, 300)


def se_z(n: int, k: int = K_CONTROLS) -> float:
    return 1.0 / np.sqrt(n - k - 3)


def upper_bound(r: float, n: int) -> float:
    return float(np.tanh(np.arctanh(r) + Z_95 * se_z(n)))


def lower_bound(r: float, n: int) -> float:
    return float(np.tanh(np.arctanh(r) - Z_95 * se_z(n)))


def verdict(r: float, n: int) -> str:
    """The full amended rule. Order matters: the subtype refines KILL."""
    if upper_bound(r, n) < KILL_R:
        if upper_bound(r, n) < -PROMOTE_R:
            return "KILL-opposite-sign"
        return "KILL"
    if lower_bound(r, n) > PROMOTE_R:
        return "PROMOTE"
    return "INCONCLUSIVE"


def min_n_for_kill(bar: float) -> int:
    n = K_CONTROLS + 4
    while upper_bound(0.0, n) >= bar:
        n += 1
    return n


def section(t: str) -> None:
    print(f"\n{'=' * 72}\n{t}\n{'=' * 72}")


def main() -> int:  # noqa: PLR0915  (linear report)
    section("P212 -- H1b AMENDMENT 2")

    # ---- 1. The relaxation, and what it buys ----------------------------
    section("1. KILL bar 0.15 -> 0.20")
    n_old, n_new = min_n_for_kill(KILL_R_OLD), min_n_for_kill(KILL_R)
    print(f"\n  minimum N for a reachable KILL:  {n_old} (bar 0.15)  ->  {n_new} (bar 0.20)")
    assert n_old == 124, f"P211's number changed: {n_old}"
    assert n_new < n_old
    print(f"  The design's own 'N > 100' is now SUFFICIENT (was not: 100 < {n_old}).")
    print(f"\n  {'N':>5s} {'max r giving KILL':>19s} {'min r giving PROMOTE':>21s}")
    grid = np.linspace(-0.95, 0.95, 3801)
    for n in SAMPLE_SIZES:
        killable = [float(r) for r in grid if upper_bound(float(r), n) < KILL_R]
        hi = f"{max(killable):.4f}" if killable else "unattainable"
        lo = float(np.tanh(np.arctanh(PROMOTE_R) + Z_95 * se_z(n)))
        print(f"  {n:5d} {hi:>19s} {lo:21.4f}")

    # ---- 2. The subtype --------------------------------------------------
    section("2. Sign-reversed subtype")
    print("\n  Rejected trigger L_95 < 0 -- it fires on noise. At N=138:")
    for r in (-0.01, -0.05, -0.10):
        print(f"    r={r:+.2f}  L_95={lower_bound(r, 138):+.4f}  (< 0, would have fired)")
    assert lower_bound(-0.01, 138) < 0
    print("\n  Adopted trigger: U_95(r) < -PROMOTE_R, the mirror of PROMOTE.")
    print(f"\n  {'N':>5s} {'max r for opposite-sign':>25s}")
    for n in SAMPLE_SIZES:
        opp = [float(r) for r in grid if upper_bound(float(r), n) < -PROMOTE_R]
        cell = f"{max(opp):.4f}" if opp else "unattainable"
        print(f"  {n:5d} {cell:>25s}")

    # ---- Partition still complete and disjoint, WITH the subtype --------
    section("PC -- partition still complete and disjoint")
    for n in SAMPLE_SIZES:
        vs = [verdict(float(r), n) for r in grid]
        assert all(v in {"KILL", "KILL-opposite-sign", "PROMOTE", "INCONCLUSIVE"} for v in vs)
        # the subtype must be a strict SUBSET of KILL's condition
        for r in grid:
            if upper_bound(float(r), n) < -PROMOTE_R:
                assert upper_bound(float(r), n) < KILL_R, "subtype escapes KILL"
        # KILL and PROMOTE must never co-fire
        both = [
            float(r)
            for r in grid
            if upper_bound(float(r), n) < KILL_R and lower_bound(float(r), n) > PROMOTE_R
        ]
        assert not both, f"overlap at N={n}"
        counts = {v: vs.count(v) for v in ("KILL-opposite-sign", "KILL", "INCONCLUSIVE", "PROMOTE")}
        print(f"  N={n:4d}  {counts}")
    print("\n  Subtype is a strict subset of KILL; no overlap; no gap. PASSES.")

    # ---- 3. Structural-floor null models: feasibility --------------------
    section("3. Frozen structural-floor null models -- are they executable?")
    print("\n  M0-1 permutes E_WHIM WITHIN strata of (M_true, z, dynamical state).")
    print("  A stratified permutation is vacuous if strata hold < 2 units, and")
    print("  weak below ~5. Units per stratum for a 3-way stratification:\n")
    print(f"  {'N':>5s} {'2x2x2=8':>9s} {'3x3x2=18':>10s} {'3x3x3=27':>10s} {'4x4x3=48':>10s}")
    schemes = {"2x2x2": 8, "3x3x2": 18, "3x3x3": 27, "4x4x3": 48}
    viable: dict[str, int] = {}
    for n in SAMPLE_SIZES:
        cells = [f"{n / s:9.1f}" for s in schemes.values()]
        print(f"  {n:5d} " + " ".join(cells))
    for name, s in schemes.items():
        smallest = min(n for n in SAMPLE_SIZES if n / s >= 5.0)
        viable[name] = smallest
    print("\n  Smallest N in the planned range giving >= 5 units per stratum:")
    for name, n in viable.items():
        print(f"    {name:>6s}  ->  N >= {n}")
    # The frozen rule must be DETERMINISTIC given N, or the freedom returns.
    # Rule: take the FINEST scheme that still keeps >= 5 units per stratum.
    # This uses the sample's SIZE, which is known before unblinding, and
    # never its STRUCTURE, which is not.
    print("\n  FROZEN RULE (deterministic in N, uses sample SIZE only, never")
    print("  its structure): take the FINEST scheme keeping >= 5 units/stratum.")
    order = ["4x4x3", "3x3x3", "3x3x2", "2x2x2"]
    print(f"\n  {'N':>5s} {'scheme selected':>17s} {'units/stratum':>14s}")
    for n in SAMPLE_SIZES:
        chosen = next((s for s in order if n / schemes[s] >= 5.0), None)
        assert chosen is not None, f"no viable stratification at N={n}"
        print(f"  {n:5d} {chosen:>17s} {n / schemes[chosen]:14.1f}")
    print("\n  Choosing the stratification AFTER seeing the data is exactly the")
    print("  freedom this freeze removes. Note this corrects a hand-written")
    print("  line in the first draft that said 3x3x2 needs N>=200; the computed")
    print("  table says N>=100. The numbers govern, not the prose.")

    section("SUMMARY")
    print("  KILL bar          0.15 -> 0.20   (min N for KILL: 124 -> 71)")
    print("  New subtype       KILL - opposite-sign, U_95 < -0.30")
    print("  Null model M0-1   permute E_WHIM within strata; scheme = finest")
    print("                    keeping >=5 units/stratum (2x2x2 at N<100,")
    print("                    3x3x2 at N>=100, 3x3x3 at N>=138, 4x4x3 at N>=300)")
    print("  Null model M0-2   predict delta_M from controls only, no WHIM term")
    print("  Order of ops      compute p(r | M0) FIRST, unblind the real pairing after")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
