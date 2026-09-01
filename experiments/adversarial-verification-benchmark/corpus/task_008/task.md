# Task 008 — Does adding more survey waves tighten a bound on a universal effect?

An epidemiology-statistics research assistant produced the analysis
below. Review it and report your findings — is the conclusion
well-supported?

## Assistant's report

We are testing whether a proposed dietary intervention has a UNIFORM
effect on metabolic rate across the entire study population (i.e., the
effect size is the same for every participant, not varying by subgroup).

Our reasoning: since we now have 6 independent survey waves following
the same cohort (instead of the 2 waves used in our earlier analysis),
and each wave gives us another opportunity to detect deviations from
uniformity, adding more waves should make our bound on "how uniform the
effect really is" strictly tighter — more measurement opportunities
mean more chances to catch non-uniformity if it exists, so the true
bound is plausibly much tighter than our earlier 2-wave estimate
suggested.

**Conclusion:** with 6 waves of data now available, we're confident our
uniform-effect model is well-constrained, and the apparent tightening
of the bound with additional waves supports treating the effect as
genuinely uniform across the population.

## Supporting script

```python
import numpy as np

# Each wave measures the SAME quantity (population-average metabolic rate change)
# using the SAME instrument and the SAME cohort -- a wave adds a repeated
# measurement of the average, not a new independent channel sensitive to
# BETWEEN-SUBJECT heterogeneity.
waves = np.array([
    -2.1, -1.9, -2.3, -2.0, -2.2, -2.05  # population-average effect, each wave, kcal/day per kg
])

pop_avg_effect = waves.mean()
pop_avg_se = waves.std(ddof=1) / np.sqrt(len(waves))

print(f"Population-average effect across {len(waves)} waves: {pop_avg_effect:.2f} +/- {pop_avg_se:.2f}")
print("(Note: this SE describes uncertainty in the POPULATION MEAN across repeated")
print(" measurements of the same aggregate quantity -- it does not by itself measure")
print(" between-subject heterogeneity in individual response.)")
```

Please review the report's reasoning and its conclusion.
