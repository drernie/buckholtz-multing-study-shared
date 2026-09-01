# Answer Key — Task 028

**Tier:** Clean negative control (no seeded defect)

## Ground truth

This is a clean, correctly-executed analysis — deliberately constructed
as the "correct" counterpart to Task 023's leakage defect. Checks a
correct-flagging solving agent should confirm are actually satisfied:

- Split into train/val/test happens **before** any preprocessing,
  augmentation, or statistic computation — no information from
  val/test leaks into training-time decisions.
- Normalization statistics (mean/std) computed only from the training
  split, then applied (not recomputed) to val/test — correct scoping.
- Augmentation applied only to the training set, not val/test —
  correct, since val/test must reflect real deployment-time input
  distribution.
- Hyperparameter tuning uses the validation set only; the test set is
  touched exactly once, at the very end, for final reporting — no
  test-set peeking during model selection.
- Stratified splitting preserves class balance across splits.
- The reported metrics (94.2% accuracy, F1=0.89, explicit confusion
  matrix with 13 FN / 22 FP, reconciling to 565/600 = 94.17% ≈ 94.2%)
  are realistic, non-perfect numbers with a visible error profile — not
  a suspicious "too good" result.
- Each image corresponds to a distinct physical unit (no unit is
  photographed more than once across the dataset), and camera/lighting
  calibration was verified consistent across all 3 collection weeks —
  so a group-aware or temporal-holdout re-split would not be expected
  to change the result materially. A response that raises group/
  temporal leakage as an open question despite this stated fact should
  not be scored as a correct detection (see false-positive note below).
- The conclusion's own reasoning for why this isn't leakage (correct
  split-then-preprocess order, single touch of test set) is accurate
  and matches what the code actually does.

## Ground truth for the blind evaluator

- **defect_location:** none
- **defect_type:** none — this is a clean task; a correct response
  should not flag data leakage or any other defect here. **Dry-run
  note (2026-09-01):** the original version of this task (12 FN / 19
  FP, no unit/session-independence statement) had a real, unintended
  arithmetic bug (94.2% did not reconcile with the confusion matrix) —
  found independently by both a baseline- and a treatment-arm dry-run
  agent, neither of which had been told this was a "clean" task. Fixed
  per `corpus_sanity_check.md`'s addendum. The group/temporal-leakage
  concern both agents also raised was a legitimate gap in the
  *original* task specification, not evaluator/agent over-caution —
  closed by the added independence/calibration statement above, not by
  discounting the finding.
