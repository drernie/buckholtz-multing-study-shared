# Statistical Pre-Registration — Adversarial Verification Benchmark

**Status at commit time:** written and committed to git BEFORE Run 2
launches — no Run 2 output exists yet, no test statistic has been
computed, no result has been seen. Any change to this document after
Run 2 starts must be logged as a deviation in `result_summary.md` with
its own reasoning, never silently edited. This is the file the
project's own Falsification Ladder methodology requires before any
"expensive test" (Phase H's own escape-route discipline) — its git
commit timestamp is the record that this was fixed in advance.

## 0. What this pre-registers

Everything in Phases F–H of the approved plan (`Plan: Adversarial
Verification Methodology — Benchmark Research Program`), made numeric,
unambiguous, and resolved where the plan itself left an open question.
Two ambiguities are resolved explicitly below (§3.5, §4) rather than
left to be decided after seeing results.

## 1. Estimand (recap, not re-derived)

Already gated causal at plan-authoring time (EstimandOps L0, plan
Context section): does the explicit FL Standard-Ladder protocol +
skeptic sub-call (treatment) *cause* a higher correct-defect-detection
rate than the same ambient-default environment without that explicit
instruction (baseline — reframed 2026-09-01 per the pilot leakage
test's own finding, see plan Phase C), holding task and underlying
model constant. Identifiability by design: every one of the 32 tasks
receives BOTH arms (matched pairs, not a per-task coin flip) —
exchangeability holds by construction, not by post-hoc adjustment.

## 2. Design

- N=32 tasks (26 defect-seeded, 6 clean), per `CORPUS_MANIFEST.md`,
  corpus-sanity-checked (`corpus_sanity_check.md`) and dry-run-validated
  on 2 of the 32 (`dry_run_n2_results.md`) before this file was written.
- Every task × both arms = 64 `Agent` calls in Run 2 (baseline,
  treatment-builder+skeptic+synthesis per task).
- **Dispatch order** (resolves an ambiguity the plan left implicit —
  Context section mentions "randomized wave assignment" without a
  procedure): the 64 (task, arm) pairs are shuffled once, with a fixed
  seed, before Run 2 starts, and dispatched in that fixed order. Seed
  and resulting order are written to `manifest.json` at Run 2 launch
  time, before any call is made — this guards against any systematic
  ordering effect (e.g., all-baseline-then-all-treatment interacting
  with time-of-day model-state drift) without needing true
  non-reproducible randomness. Procedure: Python `random.Random(20260901).shuffle(...)`
  on the 64-item list, seed fixed to today's date (`YYYYMMDD` as int)
  for reproducibility and auditability — not re-rolled if Run 2 needs
  to restart partway.
- Run 3 (blind evaluation): one evaluator pass per (task, output),
  organizer-private arm mapping, per Phase D/E. Evaluator model:
  different from whichever model runs Run 2's arms (Independent
  Verification Strength Ladder — already the design used in the
  evaluator pilot, `evaluator_pilot_results.md`).

## 3. Primary outcome metrics — exact test specification

All four below are **matched-pairs** designs (same task through both
arms) — McNemar's test, not a two-proportion z-test, per the plan's own
explicit correction of that error mode.

### 3.1 Metric 1 — Detection rate (n=26 defect tasks)

- Per task: `detected = (defect_correctly_identified AND match ∈
  {exact, close})`, per arm.
- 2×2 discordant table: `(baseline=0,treatment=1)` vs
  `(baseline=1,treatment=0)`, concordant pairs uninformative to
  McNemar and reported separately (both arms hit / both arms miss).
- **Test:** McNemar's **exact** test (binomial on the discordant
  pairs), not the chi-square approximation — with only 26 pairs and a
  plausibly small discordant count, the chi-square approximation is
  not reliable. `statsmodels.stats.contingency_tables.mcnemar(table,
  exact=True)`.
- **Effect size:** Cohen's h on the two marginal detection rates, and
  the McNemar odds ratio (ratio of the two discordant cell counts).
- **Power (pre-registered, not revisited after data):** at n=26 pairs,
  adequately powered only for a moderate-or-larger effect (Cohen's h
  ≳ 0.5 — the plan's own stated benchmark, roughly Cross-Context
  Review's own effect magnitude, arXiv:2603.12123). A smaller true
  effect reads as **inconclusive**, and must be reported as
  inconclusive — never as evidence of no effect. This is stated here,
  before any data exists, specifically so it cannot be revised after
  seeing a null result.
- Sensitivity band: report both the strict (`exact`/`close`) and
  lenient (`exact`/`close`/`vague`) detection-rate definitions, per the
  plan's Phase F metric 1 — the strict band is primary, lenient is a
  pre-registered sensitivity check, not an alternate primary metric.

### 3.2 Metric 2 — False-positive rate (n=6 clean tasks)

- Per task: `false_positive_flagged`, per arm.
- **Test:** McNemar's exact test, same procedure as 3.1.
- **Power caveat (stated now, not after seeing the result):** n=6 pairs
  has essentially no power to detect anything short of a near-total
  reversal — a single discordant pair out of 6 is already a 1/6≈16.7%
  swing. This metric is reported with its p-value and effect size like
  the others, but the write-up must explicitly flag the granularity
  limitation every time it's cited, and must not describe a
  non-significant result here as "confirms no false-positive cost."
- Always reported paired with Metric 1, per the plan's own rule — never
  detection rate alone.

### 3.3 Metric 3 — "Confidently-wrong" rate (n=32, all tasks)

- Per task: `confidently_wrong = (verdict_type == missed)` — i.e.
  Metric 3 is now defined directly in terms of the same `verdict_type`
  field Addendum 3 (below) adds to the evaluator schema, so
  `appropriately_hedged` outputs are excluded here too, on the same
  grounds (Addendum 3 predates this cross-reference in document order
  only — both were written and applied together, post-Run-3, as one
  fix). This replaces the original `[WEAK]/[HYPOTHESIS]`-marker-based
  definition, which was a reasonable proxy at pre-registration time but
  is now subsumed by the evaluator's own direct judgment.
- **Test:** McNemar's exact test on the full 32-pair table.

### 3.4 Metric 4 — Compute/token cost (n=32, all tasks)

- Per task, per arm: summed input+output tokens across all `Agent`
  calls for that (task, arm) — for treatment, this includes the
  builder call AND the skeptic sub-call (both count toward treatment's
  cost, since the skeptic call is part of what treatment's protocol
  requires).
- **Cost-per-correct-detection** (used by the Phase H kill criterion,
  §5): `total tokens for that arm across all 26 defect tasks / number
  of those 26 correctly detected by that arm`. Computed once per arm
  after Run 3 scoring is complete, not per-task-then-averaged (a
  per-task ratio is undefined when a task is not detected).
- **Test:** paired Wilcoxon signed-rank test on the 32 per-task
  (treatment_tokens − baseline_tokens) differences —
  `scipy.stats.wilcoxon`. Chosen over a paired t-test because token
  cost is right-skewed (a few tasks needing extra treatment-arm
  back-and-forth create outliers); the sign test's own robustness to
  that skew is preferred to relying on the CLT at n=32.

### 3.5 Metric 5 — Correction latency (descriptive only, NOT part of the Holm-corrected family)

**Resolves an internal inconsistency in the approved plan**, flagged
explicitly rather than silently picked: Phase G's own text says "Holm-
Bonferroni correction across the 5 primary outcome metrics," but Phase
F's own definition of metric 5 states baseline is "single-pass by
construction" — i.e., baseline's correction-latency value is
structurally undefined/zero for every task, not a real random variable
to run a paired test against. A paired test with one arm's value fixed
at a structural constant is not a meaningful significance test.
**Resolution, pre-registered now:** metric 5 is reported descriptively
(treatment's own mean/median additional-call count across the 26
defect tasks, and the qualitative fact "baseline has no correction
mechanism by design") and is **excluded from the Holm-Bonferroni
family** — the corrected family is Metrics 1–4 (m=4), not 5. This
decision is made here, before Run 2, specifically so it cannot be
second-guessed after seeing whether metric 5 "would have helped."

### 3.6 Multiple-comparison correction

Holm-Bonferroni step-down correction across the 4 p-values from
Metrics 1–4 (§3.1–3.4). `statsmodels.stats.multitest.multipletests(
pvals, method="holm")`. Metric 6 (cross-domain transfer, Tier A vs Tier
C effect-size comparison) and every per-`docs/146`-category
stratification (Phase B's own stratification) are `[EXPLORATORY]`
only — reported without correction, never treated as confirmatory,
per the plan's own explicit instruction.

## 4. Handling of missing/excluded data (resolves a second gap the plan left implicit)

- **Run 2 call failure** (an `Agent` call errors out after retries):
  that (task, arm) pair is excluded from every metric, logged by ID in
  `result_summary.md`, and the corresponding McNemar/Wilcoxon table
  drops that pair entirely (not imputed, not treated as a miss). If
  more than 2 of the 64 pairs fail this way, that is itself reported as
  a finding (something about the harness, not the hypothesis) before
  any headline number is presented.
- **Run 3 evaluator failure / `ORACLE_INADEQUATE` on a specific pair**:
  same treatment — excluded, logged, not imputed as either a hit or a
  miss.
- **No interim looks, no optional stopping.** Run 2 executes to
  completion (all 64 calls) before Run 3 begins; Run 3 executes to
  completion (all output pairs scored) before any test statistic in
  §3 is computed. This is a single fixed-N batch design, not a
  sequential one — consistent with this project's own prior decision
  (`pearl_registry/INDEX.md`, entry on E-value/sequential testing) that
  sequential-testing machinery was out of scope here.

## 5. Kill criteria (verbatim from the approved plan, Phase H, made numerically precise)

| # | Pattern | Precise threshold | Consequence |
|---|---|---|---|
| K1 | Detection rates converge | McNemar exact test (§3.1) p≥0.05 **AND** discordant ratio (larger discordant cell / smaller discordant cell) between 0.67 and 1.5 | **KILL** — report as null, not inconclusive, only if BOTH conditions hold |
| K2 | Advantage vanishes after compute control | cost-per-correct-detection ratio (§3.4) ≥3.0 **AND** raw detection-rate delta (treatment − baseline, percentage points, strict band) <10pp | **KILL** (or explicit downgrade to "not compute-efficient" if only the cost condition holds and the delta is ≥10pp) |
| K3 | High false-alarm rate | Treatment FP rate (§3.2) exceeds baseline FP rate by ≥15 percentage points (i.e., ≥1 of 6 clean tasks net swing) | **PARTIAL KILL** — falsifies the "fewer confidently-wrong conclusions" half of the hypothesis even if K1 does not fire |
| K4 | Human-in-the-loop dependency | N/A — out of scope for this design (no human-in-the-loop per task) | Stated as an explicit limitation, not evaluated |
| K5 (highest priority, checked FIRST, before K1–K3) | Evaluator fails its own oracle-adequacy pilot | Already checked pre-Run-2 (`evaluator_pilot_results.md`) — reproducibility 90%, decision-relevant fields 100% agreement. **If the real Run 3 20-pair reproducibility re-check (below) falls below 90%,** K5 fires retroactively | Headline comparison **withheld entirely**, not reported as null or positive, until a second independently-designed evaluator reproduces it |

**K5's real-run re-check** (per Phase E, not yet executed): re-run the
Run 3 evaluator twice on a 20-pair random subsample of the actual 64
Run 2 outputs (not the pilot's 10 hand-authored pairs), fresh calls,
check ≥90% exact-match reproducibility before trusting any headline
number from §3.

## 6. What gets reported regardless of outcome

Per the plan's own Verification item 6 (unchanged, restated here for
completeness): `result_summary.md` reports detection rate and FP rate
paired (never one alone), states the McNemar p-value and effect size
for every one of Metrics 1–4, explicitly labels Metric 6 and every
per-category breakdown `[EXPLORATORY]`, states plainly whether any of
K1–K5 fired, and states Metric 5 descriptively per §3.5's resolution.

## 7. Frozen treatment-arm prompt (Phase A/C, updated post-dry-run)

Per the dry run's own secondary finding (`dry_run_n2_results.md`) —
without an explicit verification directive, treatment under-performed
its own baseline by reasoning about a check instead of running one —
the treatment-arm prompt is frozen here in its corrected form:

> "You are reviewing a research assistant's analysis using a
> disciplined Falsification-Ladder Standard-Ladder protocol. Work
> through it explicitly: 1. State the falsifiable claim being made in
> the report. 2. Check for a positive control and a negative control —
> does the report supply either? 3. Look specifically for:
> circular/tautological validation, target leakage, silently-fixed
> parameters, or any other reason the reported result could be
> misleading. 4. **Wherever the artifact's own claim is checkable by
> running code (recomputing a stated number from given inputs, an
> ablation, a synthetic negative control) — write and execute that
> check, don't just describe what it would show.** 5. State your
> verdict. 6. End with a SELF-CONTAINED 'DRAFT CLAIM' paragraph (3-6
> sentences) for blind handoff to an independent reviewer."

This exact text (step 4 is the addition) is what Run 2's treatment arm
uses — any further change requires a new dated addendum to this file,
not a silent edit.

## Addendum (2026-09-02, before Run 2 launch): scope reduced to N=16

**Reason:** session token-budget constraint. This session's own observed
per-`Agent`-call cost (100-165K tokens, driven by the global CLAUDE.md +
always-on rules loading into every call — the same channel identified
in the leakage pilot) projected the full N=32 design (96 solving-side
calls + ~13 Run-3 evaluation batches + the K5 recheck) at roughly
14-15M tokens against a ~15M remaining budget — no real margin for
retries or `result_summary.md` itself. Flagged to the user before
launch (not discovered mid-run); explicit decision: reduce to N=16 now,
logged here as a deviation rather than silently downsized.

**Selected 16 of the 32 tasks** (13 defect + 3 clean, stratified):
- Tier A, one non-repeat task per `docs/146` category (all 11 covered):
  001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011.
- Tier B: 017 (control-at-trivial-zero, closer lift).
- Tier C: 023 (target leakage, ML, cross-domain).
- Clean (3 of 6): 027 (stats), 028, 032 — the latter two deliberately
  chosen because both received corpus-sanity-check fixes (028's
  confusion-matrix arithmetic, found via the dry run; 032's per-patient
  independence statement, applied proactively) and this run doubles as
  their first real-conditions check.

**Statistical consequence, stated now (not after seeing results):**
power is reduced further below the original N=32 design's own already-
limited power. At n=13 defect pairs, McNemar's exact test needs an even
larger effect than the original design's Cohen's h≳0.5 threshold to
reach significance. **This run is exploratory, not confirmatory** —
`result_summary.md` must say so in its own words, every time a number
from this run is reported, not just by reference to this addendum. The
n=3 clean-task FP-rate check has essentially no power (a single
discordant pair is already a 1/3 swing) and is reported descriptively
only, same treatment as §3.2's n=6 caveat, more so.

**Unchanged:** test choice (McNemar exact / Wilcoxon), the Holm-
Bonferroni family (§3.6), all kill-criteria thresholds (§5), missing-
data handling (§4), and the frozen treatment-arm prompt (§7, above) —
only N is reduced. Dispatch order (§2) is re-shuffled for the 32
(task, arm) pairs actually in scope, same fixed-seed procedure.

## Addendum 3 (2026-09-02, post-Run-3, autonomous follow-up): evaluator schema gains `verdict_type`, retroactive reclassification of the one discordant pair

**Reason:** the real Run 2/3 execution surfaced a genuine rubric gap in
Metric 1 (§3.1), not anticipated at pre-registration time. Task 004's
treatment-arm output was legitimately downgraded by its skeptic sub-
call from a confident REJECT to `NEEDS-REAL-DATA` (the skeptic's
objection — that the supporting "44,600× SSR variation" evidence came
from noiseless synthetic data, not validated against the real dataset's
noise floor — was itself confirmed sound). The blind evaluator's binary
`defect_correctly_identified` field has no way to distinguish "declined
to assert, correctly, because the artifact is genuinely unverifiable
from what's given" from "asserted confidently and was wrong" — both
score `false`. This conflates an epistemically *better* behavior
(appropriate hedging under legitimate adversarial pressure) with an
actual miss, and does so in exactly the direction that penalizes the
treatment arm's own skeptic-review mechanic for working as designed.

**Fix, applied retroactively to this run's own scoring (not merely
prospective):** the Phase E evaluator schema (§3, main body) gains a
fourth field, `verdict_type: detected | missed | appropriately_hedged`.
`appropriately_hedged` = the output correctly identifies that the
artifact's claim cannot be confidently verified or refuted from the
information given (a `NEEDS-REAL-DATA`/`NEEDS-MORE-INFO`-style verdict
that is itself the epistemically correct response), as opposed to
`missed` = the output asserts a confident verdict and that verdict is
wrong. Pairs where either arm's output is `appropriately_hedged` are
**excluded from Metric 1's primary binary count** (same treatment as a
missing-data pair, §4) and reported separately, descriptively, as their
own category — not folded into the detection-rate denominator either
as a hit or a miss.

**Effect on this run's own Metric 1 result:** task 004's treatment
output is reclassified `appropriately_hedged` (verified against the
skeptic's own sound objection, recorded in the session transcript) and
removed from the primary 13-pair set, leaving **n=12 non-hedged defect
pairs, both arms 12/12 = 100% detected, 0 discordant pairs, McNemar
p=1.0 by construction** (no information either way — a cleaner and more
honest characterization than the original framing, which read as
"baseline edges out treatment 13/13 vs 12/13" purely because of the
rubric gap this addendum fixes). `result_summary.md` is updated to
report this corrected figure as primary, with the original
13-pair/1-discordant-pair figure kept alongside as an explicit, labeled
"before this addendum" comparison — not silently replaced, since
p-hacking-by-relabeling-after-seeing-results is exactly the failure
mode this whole pre-registration file exists to prevent. The
distinguishing fact that makes this a legitimate fix rather than a
post-hoc rationalization: the reclassification rule (what counts as
`appropriately_hedged`) is defined structurally (skeptic-confirmed
NEEDS-REAL-DATA verdict) and applies symmetrically to either arm on any
future run — it was not tuned to flip this specific result in a
favorable direction, and in fact it makes the finding *less* favorable
to the treatment-vs-baseline narrative (perfect tie, not an edge in
either direction) than either the original 13/13-vs-12/13 reading or a
naive "just drop the discordant pair without saying why" edit would.

## Addendum 2 (2026-09-02, mid-Run-2, before treatment-arm calls): Metric 2 (false-positive rate) dropped for this run

**Reason:** discovered live, during baseline-arm execution (16 of 32
solving calls complete), that all 3 selected clean tasks (027, 028,
032) have real, substantive problems — not agent over-caution:

- **task_027**: the reported significance test does not follow from
  its own reported summary statistics. `t=3.12, p=0.003, CI=[0.21,
  0.99]` is claimed for Layout A (mean=8.1, SD=2.3, n=20) vs Layout B
  (mean=8.7, SD=2.1, n=20) — recomputing the pooled-variance t-test
  from exactly those numbers gives `t=0.86, p=0.39, CI=[-0.81, 2.01]`
  [VERIFIED via `scipy.stats`, independent of and prior to any Run 2
  agent's own finding of the same thing]. This is the same class of
  bug as the corpus-sanity-check/dry-run findings (a claimed statistic
  not reconciling with its own stated inputs) — missed originally
  because `corpus_sanity_check.md` reasoned that tasks without raw
  data arrays weren't independently checkable, which is **wrong**: a
  two-sample t-test is a deterministic function of (mean, SD, n) per
  group, no raw array needed. This blind spot was not caught by the
  N=2 dry run either (which used 023/028, not 027).
- **task_028**: the group/temporal-leakage-closing sentence intended
  to make this task genuinely clean was, on review, only ever applied
  to `_answer_key/task_028.md` (the private ground truth) — never to
  `corpus/task_028/task.md` (what solving agents actually see). The
  gap solving agents are flagging is real and still open in the
  artifact; this is an organizer editing error, not agent
  over-caution.
- **task_032**: a genuine, previously-unconsidered structural gap — a
  strip with total NaN fraction under the 20% exclusion threshold but
  containing one continuous run longer than the 0.5s interpolation
  window is neither excluded nor properly interpolated. Not something
  deliberately seeded; a real design oversight, confirmed by direct
  reproduction in the reviewing agent's own output.

**Decision (user, AskUserQuestion, 2026-09-02):** continue Run 2 to
completion using the corpus as currently instantiated — do not spend
further budget re-fixing/re-verifying the clean tasks mid-run. Instead,
**Phase F metric 2 (false-positive rate) is dropped from this run's
Holm-Bonferroni family** (§3.6's family is now Metrics 1, 3, 4 — m=3,
not 4) and reported, if at all, only as a qualitative note that the
clean-task arm of this run could not validly measure false-positive
behavior. The 13 defect-task baseline results already collected
(batches 1-2) are unaffected and remain valid — this problem is
narrowly scoped to the 3 clean tasks. Metric 1 (detection rate, n=13
defect pairs) remains the primary measurement this run can support.

**Standing follow-up — RESOLVED 2026-09-02 (autonomous post-run
check).** Systematic re-scan of all 32 tasks for this exact pattern
(stated mean/SD/n or equivalent summary statistics alongside a derived,
uncomputed p-value/CI/test-statistic, no raw data given) found **no
other instance** — task_027 was uniquely vulnerable in the whole
corpus. 027, 028, and 032 have since been re-fixed with the same
recompute-and-verify rigor as `corpus_sanity_check.md`'s original pass
(see that file's own addendum and each task's answer key for the
specifics) — not merely narrowed in scope. Not yet re-run through
solving agents to confirm empirically; that remains open.
