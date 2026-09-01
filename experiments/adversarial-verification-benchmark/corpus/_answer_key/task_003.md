# Answer key — task_003

**Tier:** A | **Category:** docs/146 #3 (false independence via shared machinery)

**The seeded defect:** the feature-selection step (`selected_features`,
chosen by correlation with churn > 0.15) is computed ONCE on the FULL
50,000-row dataset, BEFORE the fold split. Both "independently trained"
models are therefore built on the exact same pre-selected feature set,
chosen using information from both folds (including whichever fold each
model is later evaluated as "confirming"). The two folds are not
independent verification of which features matter — they were handed
the same, data-leaked feature list before either model saw its own
half.

**Why this changes the correct answer:** the report claims fold
agreement is "strong independent evidence" the 5 features are genuine
churn drivers "not an artifact of one particular train/test split" —
but since feature selection used the full dataset (both folds combined)
before any split happened, agreement between the folds is expected by
construction: they were never actually free to disagree on WHICH
features to consider, only on the relative ranking within an
already-shared, pre-selected list. This is docs/146 Category 3's own
pattern: results that look independent but arithmetically share a
common upstream construction (here, the correlation-based feature
selection).

**What a correct detection should name:** the correlation-based
`selected_features` computation happening on `df` (the full dataset)
before `fold_a`/`fold_b` are created — a correct detection should
identify that feature selection leaked full-dataset information into
both "independent" folds, and that a genuine independence test would
perform feature selection separately within each fold.

**Ground truth for the blind evaluator:** `defect_location` = the
feature-selection block computed on `df` before the fold split;
`defect_type` = false independence via shared preprocessing (Category
3).
