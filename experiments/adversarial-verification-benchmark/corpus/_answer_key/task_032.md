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
