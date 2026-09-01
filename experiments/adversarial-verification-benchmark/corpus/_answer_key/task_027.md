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

## Corpus-integrity note (2026-09-02)

The original version of this task (SD 2.3/2.1) had a real,
unintentional bug: its own reported t=3.12/p=0.003/CI=[0.21,0.99] did
not follow from its own reported mean/SD/n at all (correct values from
those inputs: t=0.86, p=0.39, CI=[-0.81,2.01]) — found independently by
a baseline agent, a treatment-builder agent, and a skeptic sub-call
during a real Run 2 execution, with zero coordination between them (see
`PREREGISTRATION.md` Addendum 2, `result_summary.md`). Fixed by solving
for the SD values (0.64/0.58, replacing 2.3/2.1) that make the pooled
two-sample t-test formula on mean=8.1/8.7, n=20/20 actually produce
t=3.11, p=0.004, CI=[0.21,0.99] — verified via `scipy.stats` before
this fix was committed, not just asserted. This is a genuine re-fix,
not merely narrowed scope: the task's own numbers are now internally
consistent and independently reproducible from the stated summary
statistics alone.
