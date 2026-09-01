# Task 020 — Grid-search "optimum" for a two-parameter model fit

A data-science research assistant produced the analysis below. Review
it and report your findings — is the conclusion well-supported?

## Assistant's report

We grid-searched our two-parameter model (`alpha`, `beta`) against our
correlation dataset (n=443, real measurements) and found the
best-fitting point at `alpha=100, beta=3.24e7`, giving `r=0.6235`.

We also checked the "null" baseline (`alpha=0, beta=0`, i.e., the
simplest possible model with both parameters off) and found it gives
`r=0.7334` — HIGHER than our grid-search "optimum."

**Interpretation:** this is a puzzling but real result — apparently our
fuller two-parameter model actually underperforms the simplest baseline
at its own reported optimum. We report `r=0.6235` as our model's best
achievable correlation, and note this as a genuine, if counterintuitive,
finding: added model complexity does not help here.

## Supporting script

```python
import numpy as np

def grid_search_pearson(data, alpha_log_range=(2.0, 8.0), beta_log_range=(2.0, 8.0), n_grid=50):
    # NOTE: alpha_log_range starts at 2.0 (i.e., alpha=100 minimum) --
    # this range does NOT include alpha near 0, which would be needed
    # to smoothly connect to the (alpha=0, beta=0) null baseline
    best_r = -1.0
    best_params = None
    for log_alpha in np.linspace(*alpha_log_range, n_grid):
        for log_beta in np.linspace(*beta_log_range, n_grid):
            alpha = 10 ** log_alpha
            beta = 10 ** log_beta
            r = compute_correlation(data, alpha, beta)
            if r > best_r:
                best_r = r
                best_params = (alpha, beta)
    return best_r, best_params

data = load_cluster_data()  # n=443, real measurements

best_r, best_params = grid_search_pearson(data)
r_null_baseline = compute_correlation(data, alpha=0.0, beta=0.0)

print(f"Grid-search optimum: alpha={best_params[0]:.1f}, beta={best_params[1]:.2e}, r={best_r:.4f}")
print(f"Null baseline (0,0): r={r_null_baseline:.4f}")
print(f"Baseline exceeds grid-search 'optimum': {r_null_baseline > best_r}")
```

Please review the report's reasoning and its conclusion.
