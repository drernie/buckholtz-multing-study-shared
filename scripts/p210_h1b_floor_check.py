"""P210 -- Floor check on H1b's pre-registered thresholds (FL Step 4a).

H1b (`experiments/20260701-h1b-whim-thermal-mass-bias/claim.md`) froze, on
2026-07-17 and before any data:

    KILL    :  r < 0.15  AND  p > 0.20
    PROMOTE :  r > 0.30  AND  p < 0.10

where r is a PARTIAL correlation of delta_M with E_WHIM, controlling
M_true and dynamical state (k = 2 controls), on a sample of N > 100.

Those thresholds predate FL Step 4a and have never been checked against a
floor. This script performs the half of that check that is possible with
no data at all.

TWO DIFFERENT FLOORS -- do not conflate them:

  NOISE floor      what a RANDOM predictor yields at this N and k.
                   Depends only on sample size and control count.
                   COMPUTED HERE, exactly.

  STRUCTURAL floor what a WHIM-free but physically correlated predictor
                   yields through the data's own covariance. This is the
                   one that actually bit before: in NR-010 the raw
                   correlation was r = 0.021 while the partial, after
                   controlling M_WL, was -0.701 -- from structure, not
                   mechanism.
                   NOT COMPUTABLE WITHOUT THE DATA. Left explicitly open.

A clean noise floor therefore does NOT clear H1b. It removes one of two
ways the criterion could be invalid.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from scipy import stats

# H1b's own pre-registered numbers.
KILL_R, KILL_P = 0.15, 0.20
PROMOTE_R, PROMOTE_P = 0.30, 0.10
N_CONTROLS = 2  # M_true, dynamical state
SAMPLE_SIZES = (100, 138, 200, 300)  # 138 = the Vladutescu-Zopp TNG sample
RNG_SEED = 20260907


def dof(n: int, k: int) -> int:
    """Degrees of freedom for a partial correlation with k controls."""
    return n - k - 2


def p_two_sided(r: float, n: int, k: int) -> float:
    """Two-sided p for a partial correlation r."""
    d = dof(n, k)
    t = r * np.sqrt(d) / np.sqrt(1.0 - r**2)
    return float(2.0 * stats.t.sf(abs(t), d))


def r_at_p(p: float, n: int, k: int) -> float:
    """The partial r whose two-sided p equals exactly p."""
    d = dof(n, k)
    t = stats.t.isf(p / 2.0, d)
    return float(t / np.sqrt(d + t**2))


def null_sd_analytic(n: int, k: int) -> float:
    """SD of partial r under the null, via the Fisher-z approximation."""
    return 1.0 / np.sqrt(n - k - 3)


def null_sd_monte_carlo(n: int, k: int, trials: int = 20000) -> tuple[float, float]:
    """Monte-Carlo SD and 95th percentile of |partial r| under the null."""
    rng = np.random.default_rng(RNG_SEED)
    out = np.empty(trials)
    for i in range(trials):
        z = rng.standard_normal((n, k + 2))
        y, x, ctrl = z[:, 0], z[:, 1], z[:, 2:]
        # residualise both against the controls, then correlate
        q, _ = np.linalg.qr(np.column_stack([np.ones(n), ctrl]))
        ry = y - q @ (q.T @ y)
        rx = x - q @ (q.T @ x)
        out[i] = float(np.corrcoef(ry, rx)[0, 1])
    return float(out.std(ddof=1)), float(np.percentile(np.abs(out), 95))


def section(t: str) -> None:
    print(f"\n{'=' * 72}\n{t}\n{'=' * 72}")


def main() -> int:  # noqa: PLR0915  (linear report, read top to bottom)
    section("P210 -- H1b floor check (FL Step 4a), NOISE floor only")

    # ---- PC1: Monte Carlo must reproduce the analytic null SD ------------
    n_pc = 100
    mc_sd, mc_p95 = null_sd_monte_carlo(n_pc, N_CONTROLS)
    an_sd = null_sd_analytic(n_pc, N_CONTROLS)
    print(f"\nPC1 [positive control] null SD of partial r at N={n_pc}, k={N_CONTROLS}")
    print(f"     analytic 1/sqrt(N-k-3) = {an_sd:.5f}")
    print(f"     Monte Carlo (20k)      = {mc_sd:.5f}")
    assert abs(mc_sd - an_sd) / an_sd < 0.05, "MC and analytic null SD disagree"
    print("     agree within 5%. PASSES.")

    # ---- PC2: the p-function must invert cleanly ------------------------
    r_check = r_at_p(0.20, n_pc, N_CONTROLS)
    back = p_two_sided(r_check, n_pc, N_CONTROLS)
    print(f"\nPC2 [positive control] r_at_p(0.20) = {r_check:.5f} -> p = {back:.5f}")
    assert abs(back - 0.20) < 1e-9, "p-value function does not invert"
    print("     round-trips exactly. PASSES.")

    # ---- The noise floor -------------------------------------------------
    section("NOISE FLOOR -- what a RANDOM predictor reaches")
    print(
        f"  {'N':>5s} {'null SD':>9s} {'95th pct |r|':>13s} {'PROMOTE 0.30':>14s} {'passable by noise?':>20s}"
    )
    for n in SAMPLE_SIZES:
        sd = null_sd_analytic(n, N_CONTROLS)
        _, p95 = null_sd_monte_carlo(n, N_CONTROLS, trials=8000)
        sigma = PROMOTE_R / sd
        print(f"  {n:5d} {sd:9.4f} {p95:13.4f} {sigma:12.1f}sig {'NO':>20s}")
        assert p95 < PROMOTE_R, f"noise reaches PROMOTE at N={n}"
    print("\n  VERDICT: the PROMOTE threshold r>0.30 is NOT reachable by a random")
    print("  predictor at any planned sample size. The noise floor is clean.")

    # ---- The two clauses of each criterion, checked for agreement -------
    section("INTERNAL CONSISTENCY -- do the r-clause and p-clause agree?")
    print("  A criterion with two clauses is only well posed if they fire together.\n")
    print(
        f"  {'N':>5s} {'r at p=0.20':>12s} {'KILL r':>8s} {'consistent?':>13s} "
        f"{'r at p=0.10':>12s} {'PROMOTE r':>10s} {'redundant?':>11s}"
    )
    kill_broken = []
    for n in SAMPLE_SIZES:
        r_k = r_at_p(KILL_P, n, N_CONTROLS)
        r_p = r_at_p(PROMOTE_P, n, N_CONTROLS)
        # KILL wants r < 0.15 AND p > 0.20, i.e. r < r_k. Consistent only if r_k >= 0.15.
        ok = r_k >= KILL_R
        if not ok:
            kill_broken.append((n, r_k))
        print(
            f"  {n:5d} {r_k:12.4f} {KILL_R:8.2f} {'yes' if ok else 'NO -- GAP':>13s} "
            f"{r_p:12.4f} {PROMOTE_R:10.2f} {'yes' if r_p < PROMOTE_R else 'no':>11s}"
        )

    section("FINDINGS")
    if kill_broken:
        print("  1. THE KILL CRITERION HAS A DEAD BAND, and it widens with N.")
        print("     KILL requires r < 0.15 AND p > 0.20. But p > 0.20 already")
        print("     requires r below the values above, which are SMALLER than 0.15:\n")
        for n, r_k in kill_broken:
            print(f"       N={n:4d}: results with {r_k:.4f} <= r < {KILL_R} satisfy the")
            print("              r-clause but FAIL the p-clause -- KILL does not fire.")
        print("\n     Such a run is neither killed nor promoted. The pre-registration")
        print("     does not say what happens to it.")
    else:
        print("  1. KILL's two clauses agree at every planned N.")

    print("\n  2. PROMOTE's p-clause is REDUNDANT. At every N above, any r > 0.30")
    print("     already has p far below 0.10, so the clause never binds. Harmless,")
    print("     but it is not the extra safeguard it looks like.")

    print("\n  3. THE UNDEFINED MIDDLE. Nothing is specified for 0.15 <= r <= 0.30 --")
    print("     a band roughly 1.5 to 3 sigma wide at these sample sizes, i.e. the")
    print("     single most likely place for a real-but-modest effect to land.")

    section("WHAT THIS DOES NOT CLEAR")
    print("  The STRUCTURAL floor is untouched and is the one that has bitten")
    print("  this project before. NR-010, on real cluster data, went from a raw")
    print("  r = 0.021 to a partial r = -0.701 once M_WL was controlled -- an")
    print("  enormous partial correlation produced by covariance structure, not")
    print("  by any tested mechanism.")
    print()
    print("  Nothing here rules that out for H1b. A WHIM-free predictor that")
    print("  shares structure with delta_M could still clear r > 0.30. Testing")
    print("  that needs the actual data:")
    print("    - shuffle E_WHIM across clusters, preserving its marginal;")
    print("    - or predict delta_M from M_true and dynamical state alone;")
    print("    - report efficiency = (observed - floor) / (ceiling - floor).")
    print()
    print("  So: noise floor CLEAN, structural floor UNKNOWN, criterion has a")
    print("  dead band and an undefined middle. Fix the bands before running.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
