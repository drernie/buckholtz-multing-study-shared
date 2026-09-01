# Task 027 — Comparing two store layouts' average basket size

A retail-analytics research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We ran a controlled test comparing two store layouts (A: current, B:
redesigned aisle order) across 40 comparable stores, randomly assigned
20 to each layout, over the same 8-week period to control for
seasonality. We compared average basket size (items per transaction)
between groups using an independent two-sample t-test, after confirming
both groups' basket-size distributions were reasonably close to normal
(checked via Q-Q plots) and had comparable variance (Levene's test,
p=0.41, no significant difference).

**Result:** Layout B: mean basket size 8.7 items (SD 0.58, n=20 stores).
Layout A: mean basket size 8.1 items (SD 0.64, n=20 stores). Two-sample
t-test: t=3.11, p=0.004. 95% CI for the difference: [0.21, 0.99].

**Conclusion:** Layout B produces a statistically significant increase
in average basket size compared to Layout A, with a plausible effect
size (roughly 0.6-1.0 more items per basket).

## Supporting script

```python
import numpy as np
from scipy import stats

layout_a = load_store_baskets("layout_a")  # 20 stores, mean basket size per store
layout_b = load_store_baskets("layout_b")  # 20 stores, mean basket size per store

# Assumption checks before running the t-test
levene_stat, levene_p = stats.levene(layout_a, layout_b)
print(f"Levene's test for equal variance: p={levene_p:.3f}")

t_stat, p_value = stats.ttest_ind(layout_b, layout_a, equal_var=True)
mean_diff = np.mean(layout_b) - np.mean(layout_a)
se_diff = np.sqrt(np.var(layout_b, ddof=1)/len(layout_b) + np.var(layout_a, ddof=1)/len(layout_a))
df = len(layout_a) + len(layout_b) - 2
t_crit = stats.t.ppf(0.975, df)  # correct t-critical value for a two-sample t-test, not a z-approximation
ci_low, ci_high = mean_diff - t_crit*se_diff, mean_diff + t_crit*se_diff

print(f"Layout A: mean={np.mean(layout_a):.1f}, sd={np.std(layout_a, ddof=1):.1f}, n={len(layout_a)}")
print(f"Layout B: mean={np.mean(layout_b):.1f}, sd={np.std(layout_b, ddof=1):.1f}, n={len(layout_b)}")
print(f"t={t_stat:.2f}, p={p_value:.3f}")
print(f"95% CI for difference: [{ci_low:.2f}, {ci_high:.2f}]")
```

Please review the report's reasoning and its conclusion.
