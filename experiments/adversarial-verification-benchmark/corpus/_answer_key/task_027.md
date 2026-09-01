# Answer Key — Task 027

**Tier:** Clean negative control (no seeded defect)

## Ground truth

This is a clean, correctly-executed analysis. Checks a correct-flagging
solving agent should confirm are actually satisfied here (not
necessarily items it needs to name unprompted — absence of complaint
about them is fine):

- Randomized assignment (20/20 stores to layout) with a fixed,
  comparable observation window (8 weeks, same period for both) —
  controls for seasonality and selection.
- Assumption checks performed *before* the test, not after: normality
  via Q-Q plot, equal-variance via Levene's test (reported, p=0.41,
  non-significant — justifies `equal_var=True` in `ttest_ind`).
- The unit of analysis (store-level mean basket size, n=20 per group) is
  consistent with the unit of randomization (stores, not individual
  transactions) — no pseudoreplication.
- Effect size and 95% CI are reported alongside the p-value, not p-value
  alone.
- The conclusion ("statistically significant increase... plausible
  effect size") is appropriately hedged to the actual CI width, not
  overstated as a precise point claim.

## Ground truth for the blind evaluator

- **defect_location:** none
- **defect_type:** none — this is a clean task; a correct response
  should not flag a defect (a hedge such as "external validity to other
  store formats is untested" is a reasonable, non-penalized
  observation, not a false positive, as long as it isn't framed as
  invalidating the reported result)
