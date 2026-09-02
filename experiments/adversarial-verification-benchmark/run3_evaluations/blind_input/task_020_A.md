# Task 020 — baseline arm output

## Findings

**Verdict: the conclusion is not well-supported. The "puzzling" result is very likely a search-domain artifact, not a genuine finding.**

1. **The code's own comment already flags the flaw:** `alpha_log_range=(2.0,8.0)` never explores near alpha=0, which the comment itself says would be needed to smoothly connect to the null baseline. The report compares a within-domain optimum against an excluded point and calls the discrepancy a "genuine, if counterintuitive" finding.
2. **`alpha_best=100` is exactly `10^2.0`, the lower EDGE of the search range** — a textbook sign the true optimum lies outside the explored region, not that an interior optimum was found. `beta_best` (log10~7.51) is comfortably interior — asymmetric behavior between the two parameters is itself informative.
3. **Unverified assumption:** whether `compute_correlation(data,0,0)` is the continuous limit of the same parametric family or a separately special-cased branch is not established from the given code.

Maps to the Floor-Ceiling Interval pattern: a floor construction was computed but the search was never extended to actually connect to it.

---

**DRAFT CLAIM:** The report's claim that the two-parameter model's grid-search optimum (r=0.6235) genuinely underperforms the null baseline (r=0.7334) is not supported. The grid search restricts alpha to [10^2,10^8], a range the code's own comment says deliberately excludes values near zero needed to connect to the null baseline, and the reported optimal alpha=100 sits exactly on that range's lower boundary — a standard signature of a boundary-truncated search, not a true interior optimum. The comparison to the null baseline is therefore between a constrained-domain optimum and an out-of-domain point. It's also unverified whether compute_correlation(data,0,0) is the continuous limit of the same family the grid searches. Before any complexity claim can be made, the search range should be extended toward zero and the null-baseline computation's provenance confirmed.
