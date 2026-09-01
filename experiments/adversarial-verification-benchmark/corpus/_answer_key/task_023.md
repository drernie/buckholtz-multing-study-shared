# Answer Key — Task 023

**Tier:** C (fresh synthetic, out-of-domain)
**Category:** Artifact Zoo ML — `perfectly_separable` / data leakage

## The seeded defect

`days_since_cancellation` is `NaN` exactly when a customer has never
cancelled, and `is_active` is defined as `1` exactly when
`days_since_cancellation` is `NaN`. But `churned` (the prediction
target) is presumably `1` exactly for customers who *did* cancel — i.e.
`is_active` (and, redundantly, the `NaN`-ness of
`days_since_cancellation` itself, before the `.fillna(-1)` step) is a
near-perfect proxy for the label the model is supposed to be
*predicting*. `days_since_cancellation` is a feature computed **from
the cancellation event itself** — it can only be known for customers
who already churned, and its very presence/absence directly encodes the
target. This is classic target leakage: a feature that is causally
downstream of (or definitionally equivalent to) the label, included as
an input.

## Why this changes the correct answer

F1 = 1.000 on a held-out test split does not mean "the model generalizes
perfectly to unseen customers" in the deployable sense the report
claims. It means the model learned to read `is_active`/
`days_since_cancellation`'s `NaN`-pattern, which is a restatement of the
label, not a predictive signal available *before* a customer churns.
In real deployment, a customer's future churn is unknown, so
`days_since_cancellation` would not be available as an input feature —
the model would collapse without the leaked feature. A suspiciously
perfect F1=1.000 on a real (non-trivial) classification task is exactly
the red flag this project's own methodology treats as a mandatory
trigger for a leakage check, not a cause for celebration.

## What a correct detection should name

- `days_since_cancellation` and `is_active` are both derived from
  whether/when the customer cancelled — the exact event the model is
  supposed to predict in advance.
- F1=1.000 / precision=1.000 / recall=1.000 on a real-world churn task
  is a red flag for leakage, not evidence of a good model.
- The correct fix is to remove any feature that is causally downstream
  of the churn event itself (or only becomes known once churn has
  already happened) and re-evaluate.

## Ground truth for the blind evaluator

- **defect_location:** the `features` list including
  `days_since_cancellation` and `is_active`, both derived from the
  churn event itself
- **defect_type:** target leakage producing a perfectly-separable /
  suspiciously-perfect result (Artifact Zoo ML — `perfectly_separable`)
