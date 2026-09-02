# Task 020 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 020

### 1. Falsifiable claim
"Two-parameter model, grid-searched over alpha,beta in [10^2,10^8] (50x50 log grid), achieves best r=0.6235 -- lower than the trivial null (alpha=0,beta=0, r=0.7334). Added complexity does not help." Implicit: the grid search actually located the model's true optimum.

### 2. Controls
Negative control invalid: the (0,0) "null baseline" was never a candidate the grid search was allowed to select (alpha_log_range bottoms out at alpha=100). Positive control absent entirely — nothing shows the search machinery can recover a known true optimum.

### 3. Red flags
- Silently-fixed `alpha_log_range=(2.0,8.0)` — the script's own comment says this deliberately excludes alpha near 0, needed to connect to the null baseline. The prose interpretation never mentions this.
- In-sample-only optimization: both the grid search and null check use the SAME n=443 sample used to pick (alpha,beta) — reporting the max of 2500 in-sample trials as "best achievable" with no held-out evaluation is a standard overfitting pattern.
- Unverified black boxes: compute_correlation/load_cluster_data never shown — can't confirm (0,0) is a continuous member of the same family being searched.

### 4. Executed check
- alpha=100 is IDENTICAL to the search range's lower edge exactly (10**2.0 == 100.0) — not an interior stationary point.
- Synthetic reconstruction: restricted grid reproduces the exact reported pattern (best sits at range floor, below null); extended grid (alpha to 0) makes the "puzzle" disappear entirely.
- Pearson-r standard error at n=443 ~= 0.048 for a single test — the reported r-values come from the MAX of 2500 correlated in-sample trials, no comparable error bar, upward-biased.

### 5. Verdict
**REJECT the stated interpretation.** Killed: "r=0.6235 is the model's best achievable correlation" and "the model underperforms the null." Not killed: whether a correctly-searched, out-of-sample-tested model actually beats/ties/loses to the null — genuinely unknown, not established either way.

---

### DRAFT CLAIM
A grid search over a two-parameter model (alpha, beta restricted to [10^2,10^8]) reported its best in-range correlation (r=0.6235, at alpha=100) as lower than a null baseline (alpha=0,beta=0, r=0.7334) evaluated OUTSIDE that search range, concluding "added complexity does not help." The reported "optimum" alpha is mathematically identical to the search range's lower boundary, and the code's own comment states the range was deliberately chosen to exclude alpha near zero. A synthetic reconstruction confirms this exact pattern (best-in-range = range floor, below an out-of-range null) is fully produced by range restriction alone, no real "complexity hurts" effect needed. Both checks are also in-sample only, no held-out or permutation-based negative control. Verdict: not supported — an artifact of a misconfigured search range, not a finding about the model.
