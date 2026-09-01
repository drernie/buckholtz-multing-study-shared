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

## Corpus-integrity note (2026-09-02, two rounds)

**Round 1:** the original version of this task (SD 2.3/2.1) had a real,
unintentional bug: its own reported t=3.12/p=0.003/CI=[0.21,0.99] did
not follow from its own reported mean/SD/n at all (correct values from
those inputs: t=0.86, p=0.39, CI=[-0.81,2.01]) — found independently by
a baseline agent, a treatment-builder agent, and a skeptic sub-call
during a real Run 2 execution, with zero coordination between them (see
`PREREGISTRATION.md` Addendum 2, `result_summary.md`). Fixed by solving
for the SD values (0.64/0.58, replacing 2.3/2.1) that make the pooled
two-sample t-test formula on mean=8.1/8.7, n=20/20 actually produce
t=3.11, p=0.004, CI=[0.21,0.99] — verified via `scipy.stats`.

**Round 2 (re-verification against solving agents):** with the SD
values fixed, a *second*, more subtle bug became visible and was
independently caught by both a fresh baseline and a fresh treatment-
builder agent: the script's own CI formula hardcoded a z-critical value
(`1.96`) instead of the correct t-critical value for df=38 (`2.024`).
Under the new SD values, the reported CI [0.21,0.99] actually matches
the *correct* t-based computation, not what the shown (z-based) script
would produce ([0.22,0.98]) — a residual script/report mismatch the
Round-1 fix didn't catch because it only checked t/p, not the CI
formula's own internal correctness. Fixed by replacing the hardcoded
`1.96` with `stats.t.ppf(0.975, df)` in the script.

**What was found but NOT further "fixed":** both re-verification agents
also raised a legitimate, substantive methodological point — no
pre-treatment covariate-balance check between the 40 stores is shown,
so chance imbalance (store size, format, footfall) can't be ruled out
as an alternative explanation. This is a real, well-reasoned observation
that a sufficiently rigorous reviewer will very likely make about *any*
report this brief describing a between-subjects randomized design — not
a fabricated or invented concern. Rather than keep adding disclaimers
to chase full immunity to scrutiny (risking the "infinite surgery"
anti-pattern), this is recorded here as a genuine, standing limitation:
**a response that raises the missing-balance-check concern as an
open question, without claiming it invalidates the result, should be
treated as a legitimate, non-disqualifying hedge, not a false
positive** — the same allowance the original answer key already made
for "external validity untested"-style observations.
