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
  should not flag data leakage or any other defect here.

## Corpus-integrity note (dated, two rounds)

**Round 1 (2026-09-01, N=2 dry run):** the original version of this
task (12 FN / 19 FP, no unit/session-independence statement) had a
real, unintended arithmetic bug (94.2% did not reconcile with the
confusion matrix) — found independently by both a baseline- and a
treatment-arm dry-run agent, neither told this was a "clean" task.
Confusion matrix fixed to 13 FN / 22 FP. An independence/calibration
sentence was *intended* to close the group/temporal-leakage gap both
agents also raised, but — an organizer error caught only in Round 2
below — that sentence was added to this answer key file only, never
to the actual `corpus/task_028/task.md` that solving agents see.

**Round 2 (2026-09-02, real Run 2):** both the baseline and treatment
agent independently re-found the identical, still-open group/temporal-
leakage gap, correctly, since the task text they actually received
still didn't rule it out. This is what surfaced the Round-1 editing
mistake. Fixed for real this time: the independence/calibration
sentence now lives in `task.md`'s own report text (verified by reading
the file back), not just here.

**Round 3 (2026-09-02, re-verification after the Round-2 fix):** a
fresh baseline and treatment agent, given the Round-2-fixed text, STILL
raised group/temporal leakage — but this time the point is more
sophisticated and was NOT closed by the independence/calibration
sentence: "distinct physical units, consistent camera/lighting" rules
out duplicate-image leakage and gross calibration drift, but not
production-batch, supplier-lot, or operator/shift confounds correlated
with collection week, which a plain label-stratified split still
doesn't control for. One treatment agent built a synthetic analog
demonstrating a real ~7-point accuracy gap between a random split and a
week-grouped split under a plausible confound structure — this is not
a hypothetical concern, it has a demonstrated non-zero effect size in
at least a toy setting structurally identical to this task's own split
code. **Revised guidance, correcting Round 2's own premature scoring
rule:** this concern should be treated as a legitimate, non-
disqualifying hedge (per the general allowance already stated above for
"external validity untested"-style observations), not a false positive
— Round 2's "should be scored as a false positive" instruction is
itself withdrawn. Closing this gap completely would require the task to
state that a week-grouped/held-out-week validation was ALSO run and
gave consistent results — a stronger, more specific claim than the
current text makes, and not added here in order to avoid an unbounded
"fix, re-verify, find something new" cycle (see `result_summary.md`'s
note on this exact tradeoff). This task is retained as a "best-effort
clean" control, not a "provably unimpeachable" one — the two are not
the same bar, and this project's own experience across three rounds is
itself evidence they may not be reachable together for a report this
short.
