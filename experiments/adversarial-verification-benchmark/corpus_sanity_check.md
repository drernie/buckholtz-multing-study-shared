# Corpus Sanity Check (2026-09-01)

Verification item 3 of the benchmark plan: "for each of the 26 defect
tasks, confirm the seeded defect actually changes the correct answer
(not a cosmetic change) — organizer spot-check before Run 2 launches."

## Method

Read all 32 tasks + answer keys in full (14 defect tasks — 002-015 —
were re-read fresh, since they predate this session's visible context
window; 001 and 016-032 were already in context from authoring/earlier
verification). For each of the 26 defect tasks, confirmed: (1) the
answer key's claimed defect is actually present in the task's script/
report text; (2) correcting it would flip the correct verdict, not a
cosmetic change; (3) exactly one seeded defect, per Phase B's own
anti-tautology rule.

Went further than a read-through: every task with an explicit formula
+ explicit numeric inputs + a claimed numeric "result" in its prose was
independently recomputed in Python (`scipy`/`numpy`), not just visually
re-checked. This caught real bugs a pure read-through would have
missed — several claimed results simply don't follow from the given
formulas.

## All 26 defects: present, real, single, non-cosmetic

Confirmed for all 26 (001-026): the answer key's named defect is
actually in the text/code, is the sole seeded defect, and correcting it
flips the report's conclusion (not a wording nitpick). No task was
found with zero, or more than one, genuine seeded defect.

## Real corpus bugs found and fixed (9 total)

Independent recomputation found that 9 of the 32 tasks stated a
numeric "result" that did not actually follow from the formula +
inputs given in the same task — an authoring error, unrelated to the
intended seeded defect, but capable of confusing or misdirecting a
solving/evaluating agent. All 9 were fixed by recomputing the correct
value precisely (script: verified twice, before and after each fix)
and editing both `task.md` and, where they cited the same figures,
the answer key.

| Task | What was wrong | Fix |
|---|---|---|
| 001 (defect) | Stated ratio 1.63398 didn't match `c_axis/a_axis` from the given values (actual: 1.63363) | `c_axis` 5.9412→5.9425 |
| 005 (defect) | Stated t=4.71/p<0.001/d=1.02 didn't match the t-test on the actual embedded score arrays (actual: t=9.86, d=2.09) | Corrected means/SDs/t/p/d to the array-derived values |
| 011 (defect) | Stated NPV $18.4M didn't match `npv()` on the given cash flows at 4.15% (actual: $9.2M) — nearly 2x off, and would have broken the "$15M threshold" framing entirely | NPV/threshold corrected to $9.2M/$8M; sensitivity-range % figures (the actual seeded defect) untouched |
| 012 (defect) | Stated K_eq=27.84 didn't match `exp(-dG/RT)` on the given dG/R/T (actual: 28.92) | Corrected to 28.92 |
| 013 (defect) | Stated both distance methods gave ~2,340 pc; actual computation gave 2,535 pc (Method 1) vs 43,035 pc (Method 2) — an order-of-magnitude mismatch that broke the task's entire premise (the methods must agree for the shared-zero-point defect to make sense) | Corrected RR Lyrae absolute-magnitude formula and apparent magnitude so both methods land at ~2,535 pc |
| 014 (defect) | Narrative claimed the optimizer lands at the *upper* bound (45.0); actual bounded optimum is 5.000 — the *lower* bound. The story was physically backwards for the given cost coefficients | Flipped "upper bound/45.0" → "lower bound/5.0" throughout task + answer key |
| 022 (defect) | Stated merged row count 8,214 (= sum of both files); actual `drop_duplicates` behavior on colliding sequential IDs gives 5,003 (a real, deterministic consequence of the ID-collision defect itself, not a rounding slip) | Corrected to 5,003; strengthened the answer key to note the count mismatch as an additional, cheaper available tell |
| 029 (clean) | Stated Q_total=48,230,000 m³; actual integral of the given Gaussian-pulse `q(t)` over [0,120] is ~1,638,600 m³ — off by ~29x | Corrected Q_total, error estimate, and the "historical range" comparison figure so the clean verdict's own reasoning (cross-check against an independent expectation) stays true |
| 031 (clean) | Stated EV=$4.82B and sensitivity range $4.1B-$5.7B; actual `dcf()` on the given cash flows/WACC/growth gives $3.94B and a $3.3B-$4.9B range | Corrected both figures |

**Two clean-control tasks (029, 031) had bugs, not just defect tasks** —
worth flagging explicitly: an unnoticed arithmetic error in a *clean*
task is arguably worse than one in a defect task, since it would have
silently corrupted the false-positive-rate measurement (Phase F metric
2) by making a supposedly-sound analysis's own claim untrue.

## Noted, not fixed (narrative results that don't literally reproduce, but don't threaten the verdict)

Tasks 009 and 018 (both "numerical artifact mistaken for physics,"
`quad` at extreme range) narrate specific negative results. Running the
actual given code: task 009 gives `Q(1e12) = 0.0` exactly (not the
narrated -4.7e-3); task 018 raises `IntegrationWarning: Result too
large` (not the narrated -3.2e188). Both are *different* symptoms of
the same underlying fact — `quad` is unreliable across the stated
extreme dynamic range — so if a solving agent actually executes the
code, whatever it observes will still point toward the same correct
verdict ("this is a numerical artifact, not physics"), not away from
it. Left as narrated fiction rather than force-matched to literal
`quad` output, since forcing an exact match isn't necessary for
correctness here and risks introducing new arithmetic bugs for no
benefit — unlike 001/005/011/012/013/014/022/029/031, where the
mismatch was between the story's own key numbers, not between the
story and a live tool run.

## Verification of the fixes themselves

Every fix above was independently re-computed after editing to confirm
`file_value == python_computed_value`, not just asserted. See
`/tmp/verify2.py`, `/tmp/verify4.py` outputs (session transcript) —
all 9 fixes confirmed to match on re-check.

## Addendum (2026-09-02): the gap this check itself had

This check's own §"Method" reasoned that tasks stating only summary
statistics (mean/SD/n) without raw data arrays were "not independently
checkable," and skipped them. That reasoning was wrong: a two-sample
t-test's statistic, p-value, and CI are deterministic functions of
(mean, SD, n) per group — no raw array is needed to verify them. This
exact gap let task_027 through with a severe, undetected bug (its
reported t=3.12/p=0.003 didn't follow from its own reported mean/SD/n
at all) — found live during a real Run 2, independently by three
agents with zero coordination (see `result_summary.md`). A systematic
corpus-wide re-scan for this specific pattern, done immediately after,
found no other instance in the remaining 31 tasks — task_027 was
uniquely vulnerable. Fixed (SD values solved for and verified via
`scipy.stats` so the reported statistics now actually follow from the
reported inputs); see the task's own answer key for the exact numbers.
The lesson generalizes past this one bug: "not literally executable
without external data" is not the same claim as "not independently
checkable" — always ask whether a *derived* quantity is checkable from
what *is* given, separately from whether the *raw* data is available.

## What this sanity check does NOT establish

- Does not re-run the corpus through Run 2's actual solving agents —
  this confirms the corpus's own internal consistency and that each
  defect is real and singular, not that the corpus is well-calibrated
  in difficulty (that's what the full N=32 run itself measures).
- Does not re-verify every non-formula-bearing narrative claim (e.g.,
  F1 scores, AUC values, accuracy percentages tied to unprovided
  external data files) — those are, by construction, not independently
  checkable and are treated the same way a real peer reviewer treats a
  cited-but-unreproduced result: taken as given, per the task's own
  framing as a report to be evaluated on its reasoning, not
  re-executed from scratch.
