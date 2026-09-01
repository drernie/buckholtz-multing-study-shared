# Answer Key — Task 032

**Tier:** Clean negative control (no seeded defect)

## Ground truth

This is a clean, correctly-executed analysis — deliberately constructed
as the "correct" counterpart to Task 024's all-NaN-silently-zero defect.
Checks a correct-flagging solving agent should confirm are actually
satisfied:

- Full/majority-`NaN` strips are explicitly detected (`quality_gate`,
  20% `NaN` threshold) and routed to a separate `insufficient_data`
  bucket, logged and excluded — not silently folded into the analyzed
  results the way Task 024's all-NaN windows were silently treated as
  "not drifting."
- Short `NaN` gaps within an otherwise-good strip are handled by
  bounded linear interpolation (gap < 0.5s) rather than either being
  ignored (`nanmean`-style) or left to propagate `NaN` into downstream
  calculations unexamined.
- The gate itself checks BOTH the total NaN fraction AND the longest
  single contiguous NaN run — a strip with one long dropout (>=0.5s)
  is excluded even if its total NaN fraction is small, so no strip
  reaching `interpolate_short_gaps` can have any unresolved NaN left
  afterward (interpolation there is total, not partial, by
  construction).
- The counts are reconciled explicitly: 4,731 analyzed + 269 excluded =
  5,000 total — nothing is unaccounted for.
- The reported mean heart rate (71.4 bpm) is explicitly stated to be
  computed only over the analyzed subset, with the excluded fraction
  (5.4%) reported alongside it rather than silently absorbed into the
  average or omitted from the report.

## Ground truth for the blind evaluator

- **defect_location:** none
- **defect_type:** none — this is a clean task; a correct response
  should not flag a silent-NaN-handling concern here (unlike Task 024,
  full-dropout strips are explicitly detected and excluded, not
  averaged as if they were valid low-noise readings)

## Corpus-integrity note (2026-09-02)

The original version of this task had a real, undesigned gap: the
20%-total-NaN gate and the <0.5s interpolation window were independent
thresholds, so a strip with one continuous dropout longer than 0.5s but
under 20% total could pass the gate with unresolved NaN reaching the
heart-rate estimator — found by direct execution during a real Run 2
(both the baseline and treatment agent reproduced it independently; see
`result_summary.md`). Fixed by adding a second gate condition
(`longest_nan_run(strip) >= max_single_gap_samples` also excludes),
which closes the gap structurally: any strip that reaches
`interpolate_short_gaps` is now guaranteed to have every remaining NaN
run shorter than the interpolation window, so interpolation there is
total, not partial. This is a genuine fix to the pipeline logic, not
a narrowed claim.
