# Task 014 — baseline arm output

## Findings

**Verdict: The conclusion is not supported. The reported x* = 5.0 cm is a boundary artifact of reused, mismatched search bounds — not the genuine cost-minimizing thickness.**

### What the numbers actually show (verified via direct execution)

The cost function `f(x) = 12x + 340/(x+1)` is strictly convex on `x > -1`, so it has a single global minimum, findable analytically: `x* = sqrt(340/12) - 1 ~= 4.323 cm`, with `f(x*) ~= 115.75`.

Reproducing the script exactly as written:
- Bounded search on `[5.0, 45.0]` (the reused bounds): `x* = 5.000`, `f* = 116.667`
- Wide bounded search on `[0.0, 45.0]`: `x* = 4.323`, `f* = 115.750` — matching the analytic result, landing strictly inside the interval, confirming this is the genuine interior optimum.

The true unconstrained cost-minimizing thickness (~4.32 cm) lies below the lower bound (5.0 cm) copied from the previous large-diameter/high-temp run.

### Why the report's reasoning is wrong

1. **"Converged cleanly (no error, no warning) -> valid result"** is a non-sequitur. `minimize_scalar(method="bounded")` reports `success=True` whenever it finds the minimizer within the given bounds — it has no visibility into whether those bounds are appropriate.
2. The result landing exactly at the boundary (5.0000048 ~= 5.0) is itself a classic red flag, not corroborating evidence.
3. The report's own stated expectation contradicts its conclusion: "true optimum should be a few cm, not tens of cm" — consistent with ~4.3 cm — yet the bounds `(5.0, 45.0)` structurally forbid anything below 5 cm.
4. Magnitude: the true optimum is ~13% smaller than the reported result.

### Root cause and fix

Search bounds are problem-instance-specific and were carried over from an unrelated optimization without being re-derived. Bounds should be set wide enough to not clip the true optimum, and any result landing at/near a bound should trigger a wider re-check before being reported as final.

---

**DRAFT CLAIM:** The report's conclusion that x* = 5.0 cm is "the genuine cost-minimizing thickness" for the new pipe design is not supported and is contradicted by direct recomputation. The cost function is strictly convex with a single global minimum at x ~= 4.32 cm (cost ~= 115.75), verified both analytically and by re-running `minimize_scalar` with wider bounds (0, 45) that don't clip the optimum. The reported result of exactly 5.0 cm is a boundary artifact: the search bounds `(5.0, 45.0)` were copied unchanged from a prior, unrelated optimization and were never re-derived for the new coefficients, so the search window excludes the true optimum, which lies just below the lower bound. `success=True` with no warning is expected, mechanical behavior when a solution is clamped to a bound — it is not evidence the bound was appropriate. The fix is to set problem-appropriate bounds for each new problem instance and treat any bounded-optimizer result landing at or very near a boundary as a signal requiring a wider-bound re-check before being reported as final.
