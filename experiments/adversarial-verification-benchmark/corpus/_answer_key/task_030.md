# Answer Key — Task 030

**Tier:** Clean negative control (no seeded defect)

## Ground truth

This is a clean, correctly-executed analysis — deliberately constructed
as the "correct" counterpart to Task 020's box-excluded-optimum defect.
Checks a correct-flagging solving agent should confirm are actually
satisfied:

- The grid search's own optimum lands strictly inside the searched
  range for both hyperparameters (`learning_rate=0.03` is neither the
  smallest [0.001] nor largest [0.1] value swept; `max_depth=7` is
  neither the smallest [3] nor largest [11]) — the report explicitly
  checks and states this, unlike Task 020 where the box excluded the
  true optimum's region entirely.
- Cross-validation is performed only on the training set; the test set
  is held out untouched throughout the entire 25-combination sweep and
  used exactly once, for final reporting.
- The close agreement between CV RMSE (4.21) and final test RMSE (4.35)
  is used correctly as evidence against overfitting to the validation
  folds — a legitimate, appropriately-scoped inference from that
  comparison.
- No baseline or competing configuration outside the searched grid is
  silently excluded from a comparison the way Task 020's `alpha=0`
  baseline was.

## Ground truth for the blind evaluator

- **defect_location:** none
- **defect_type:** none — this is a clean task; a correct response
  should not flag a box-excluded-optimum or overfitting concern here
