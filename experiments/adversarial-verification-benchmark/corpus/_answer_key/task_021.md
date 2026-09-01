# Answer Key — Task 021

**Tier:** C (fresh synthetic, out-of-domain)
**Category:** Artifact Zoo Universal — `empty_input`

## The seeded defect

`daily_summary_score()` computes `total / len(customer_scores)`. If any
customer has an empty list of recent scores (a plausible real-world case
— a brand-new customer with zero transactions yet, or one whose scores
were all filtered out upstream), `len(customer_scores) == 0` and the
function raises `ZeroDivisionError`. The claim that the batch "completed
without errors" and processed "12,406 customers with 0 exceptions" is
only true because, apparently, no customer in *this particular run*
happened to have an empty score list — not because the code correctly
handles that case.

## Why this changes the correct answer

"Zero exceptions on this run" is not the same as "handles all inputs
correctly" — it means the empty-input case never occurred in this
particular dataset. The very next batch run (a day with more new
signups, or a data-quality issue that filters all of one customer's
scores) risks crashing the whole batch job on a single bad customer
record, which is a real production risk the report doesn't surface at
all. This is the Artifact Zoo's canonical `empty_input` case: a
function untested against the empty-collection edge case, validated
only by absence-of-failure on one dataset that didn't happen to contain
that case.

## What a correct detection should name

- `daily_summary_score` divides by `len(customer_scores)` with no guard
  for the empty-list case.
- "0 exceptions on 12,406 real customers" is evidence about *this*
  dataset's composition, not a proof the function is robust to all
  valid inputs.
- A correct claim of robustness requires either an explicit test with
  an empty scores list, or a code-level guard (e.g., return `None`/skip
  customers with no scores) plus a stated policy for what an empty
  history should produce.

## Ground truth for the blind evaluator

- **defect_location:** `daily_summary_score()` — `total / len(customer_scores)`
  with no check for `len == 0`
- **defect_type:** empty_input edge case, unhandled (Artifact Zoo
  Universal — `empty_input`)
