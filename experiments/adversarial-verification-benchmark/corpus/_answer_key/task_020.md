# Answer Key — Task 020

**Tier:** B (verbatim-lifted historical incident)
**Category:** docs/146 Category 4 — Narrow-to-broad overclaim (box-excluded optimum)

## The seeded defect

The grid search's own search range, `alpha_log_range=(2.0, 8.0)`, means
`alpha = 10**log_alpha` never goes below `100`. The comparison "null
baseline" uses `alpha=0`, which lies **outside** the searched box
entirely. So the "grid-search optimum" (`r=0.6235`) was never actually
compared, within the same search space, against the region near
`alpha=0` where the reported-higher baseline (`r=0.7334`) lives. The
grid search didn't find that the two-parameter model underperforms the
null baseline *at its true optimum* — it excluded the null baseline's
neighborhood from the search box from the start, then compared its
in-box result to an out-of-box point as if they were comparable.

## Why this changes the correct answer

The report's interpretation — "our fuller two-parameter model actually
underperforms the simplest baseline... a genuine, if counterintuitive,
finding" — is not supported. The correct reading is the opposite of
what's claimed: the grid search's own box excludes the actual optimum
(which is at or near `alpha=0`, `beta=0`, since that's what scores
higher), so `r=0.6235` is not "our model's best achievable correlation"
at all — it's the best achievable correlation *given an
under-specified, badly bounded search range*. This is docs/146 Category
4 (narrow-to-broad overclaim, box-excluded-optimum family, a named
recurring pattern in this project): a bounded search's own artificial
boundary is silently reported as if it captured the full parameter
space, and the resulting "surprising" finding is actually a search-
design artifact, not a property of the model.

## What a correct detection should name

- `alpha_log_range=(2.0, 8.0)` never lets `alpha` go below 100 —
  the comment even flags this explicitly, but the report's own
  interpretation ignores it.
- The correct fix is to extend the search range to include `alpha` near
  0 (e.g. `alpha_log_range` starting well below 2.0, or explicitly
  including `alpha=0` as a candidate point) before claiming anything
  about where the true optimum lies relative to the null baseline.
- "Added model complexity does not help" is an overclaim: the box search
  never actually explored the region where complexity could help (or
  could confirm it doesn't) — the two facts (in-box optimum, out-of-box
  baseline) are not commensurable as reported.

## Ground truth for the blind evaluator

- **defect_location:** `alpha_log_range=(2.0, 8.0)` in
  `grid_search_pearson` — excludes `alpha` near 0 from the search box
- **defect_type:** narrow-to-broad overclaim / box-excluded-optimum
  (docs/146 Category 4) — a bounded search's artificial limit is
  reported as if it were the full picture
