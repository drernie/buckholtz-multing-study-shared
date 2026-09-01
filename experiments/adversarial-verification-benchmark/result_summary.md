# Result Summary — Adversarial Verification Benchmark, N=16 Run (2026-09-02)

Per `PREREGISTRATION.md` §6. This run is **exploratory, not confirmatory**
(Addendum 1, scope reduced from N=32 to N=16 for session-budget reasons,
committed before Run 2 launched) — every number below must be read with
that qualifier, not as a standalone finding.

## Headline result: inconclusive, underpowered as pre-registered

**Metric 1 (detection rate), the pre-registered 13-task defect set**
(001-011, 017, 023 — Tier A all 11 `docs/146` categories + 1 Tier B +
1 Tier C):

| Arm | Detected (strict: exact/close) |
|---|---|
| Baseline (ambient-default) | 13/13 = 100% |
| Treatment (explicit FL protocol + skeptic) | 12/13 = 92.3% |

McNemar's exact test on the 2×2 discordant table (baseline-only=1,
treatment-only=0, both-hit=12, both-miss=0): **p = 1.0**. Cohen's h =
0.56 (point estimate only — with a single discordant pair total, this
number is not interpretable as an effect size; it is reported because
§3.1 pre-registered reporting it regardless of outcome).

**This is exactly the underpowered/inconclusive outcome the pre-
registration warned about before any data existed** (§3.1: "at n=26
[here n=13], adequately powered only for a moderate-or-larger effect...
a smaller true effect will read as inconclusive and must be reported as
inconclusive, not as evidence of no effect"). With only one discordant
pair in the entire 13-task set, this run has essentially zero power to
detect a real difference in either direction. **Kill criterion K1**
(detection rates converge, McNemar p≥0.05) is spiritually met (p=1.0),
though its numeric "discordant ratio 0.67–1.5" sub-condition is
undefined with a zero-count discordant cell — noted, not adjudicated
either way, since the p-value alone already settles inconclusiveness.

**Metric 2 (false-positive rate): dropped for this run.** All 3
selected clean-control tasks turned out to have real, substantive
problems discovered live during baseline execution (Addendum 2) — not
agent over-caution. No valid false-positive-rate measurement exists
from this run's clean-task selection. See "Corpus integrity findings"
below.

**Metrics 3 (confidently-wrong rate) and 4 (compute cost):** not
computed for this write-up — out of session-budget scope for this
already-large turn. Flagged as a follow-up, not silently dropped.

## The one discordant task (004) — a metric-design finding, not a protocol failure

Task 004's treatment-arm final claim was legitimately downgraded from a
confident REJECT to NEEDS-REAL-DATA after the skeptic sub-call raised a
real, substantive objection (the "44,600× SSR variation" evidence came
from noiseless synthetic data, not validated against a real noise
floor) — the Response Matrix worked exactly as designed, producing a
more epistemically honest final answer. But the blind evaluator's
binary detection rubric then scored that appropriately-hedged answer as
"not detected," because it declined to confidently assert the seeded
defect (narrow `p` bounds) is wrong. **This is worth flagging as a
property of the detection-rate metric, not a defect in the treatment
protocol**: a workflow that correctly downgrades overconfident claims
in response to legitimate pushback can lose "detection credit" under a
metric that only rewards confident correct answers, not appropriate
uncertainty. Baseline's draft (never skeptic-reviewed) kept its
original confident REJECT and scored as detected. This tension between
"rewards confidence" and "rewards honesty" is a real limitation of
Metric 1 as currently defined, not evidence the treatment arm
under-performed substantively.

## Corpus integrity findings (the actual, substantive result of this run)

Independent of the underpowered headline comparison, this run
surfaced — and fixed, or at minimum documented — real problems in the
benchmark corpus itself, at a rate that is itself notable:

- **9 corpus bugs found and fixed before Run 2** (`corpus_sanity_check.md`).
- **A 2nd corpus bug found during the N=2 dry run**, independently by
  3 agents with zero coordination (`dry_run_n2_results.md`).
- **A 3rd, more severe corpus bug found live during Run 2 baseline
  execution**: task_027's reported significance test (t=3.12, p=0.003)
  does not follow from its own reported summary statistics at all
  (correct value: t=0.86, p=0.39) — found independently by the baseline
  agent, then independently reconfirmed by the treatment-builder agent,
  then independently reconfirmed a third time by the skeptic (who
  additionally showed a paired-design rescue is *also* ruled out by the
  reported p-value). **Three independent verification paths converged
  on the identical finding with zero coordination between them** — per
  this project's own Independent Verification Strength Ladder, this is
  meaningfully closer to "blind replication by another group" than the
  "same model, isolated context" tier that any single one of these
  checks would rate alone.
- **Two more originally-"clean" tasks (028, 032) also turned out to
  have real, uncontrived problems** — one an organizer editing mistake
  (a fix that only ever landed in the answer key, never the actual
  task text), one a genuine structural gap in the pipeline design that
  was never deliberately seeded.

**Taken together: of the 3 clean-control tasks actually run in this
N=16 subset, 0 of 3 were actually clean.** This is the single most
striking empirical result of this run, and it says something about
corpus construction difficulty, not about the workflow-comparison
hypothesis this benchmark was designed to test. Every one of these bugs
was caught by a **general-purpose research agent working under this
project's own ambient FL-derived rules** — which is itself weak,
suggestive evidence for the broader hypothesis (a disciplined, verify-
before-claim environment catches real defects, including defects in
its own test materials) even though it isn't the controlled comparison
the benchmark was built to make.

## Secondary finding: treatment-prompt gap (found and fixed pre-Run-2)

The N=2 dry run found the original treatment-arm prompt under-elicited
tool-based verification relative to what baseline did unprompted on the
same task (`dry_run_n2_results.md`) — fixed by adding an explicit
verification directive (`PREREGISTRATION.md` §7) before Run 2 launched.
Post-fix, **all 16 treatment-arm builder outputs in the real run wrote
and executed genuine verification code** (synthetic ablations, bug-
injection sweeps, independent recomputation) — the fix held.

## What this run does NOT establish

- **Does not confirm or refute the core hypothesis** (explicit FL
  protocol + skeptic sub-call detects more defects than ambient-default
  alone) — the comparison was underpowered by design (pre-registered)
  and further compressed by the N=32→N=16 budget-driven reduction.
  Detection rate came back statistically indistinguishable (p=1.0),
  which must be read as "no information," not "no effect."
- **Does not measure false-positive rate at all** — the clean-task arm
  of this run was compromised and dropped.
- **Does not establish anything about the remaining 16 corpus tasks**
  not included in this N=16 subset, including the 3 clean tasks (029,
  030, 031) never run here — those still need the systematic
  "significance-stat-from-summary-stats" re-check flagged in Addendum 2
  before being trusted in a future run.
- **Baseline's apparent edge (13/13 vs 12/13) is not evidence baseline
  is superior** — it rests on a single discordant pair, explained above
  as a metric-design artifact on task 004, not a substantive gap.

## Recommended next steps (not executed this session — scope decision for the user)

1. Fix the metric-3 gap: distinguish "confidently wrong" from
   "appropriately hedged" so a Response-Matrix downgrade like task
   004's isn't penalized identically to an actual miss.
2. Systematic corpus-wide re-check for the "summary-stats-implies-
   checkable-inferential-stats" pattern before trusting any of the
   remaining 16 tasks (Addendum 2's own standing follow-up).
3. Design 3 genuinely-verified clean controls (with the same rigor now
   applied post-hoc to 027/028/032) before attempting Metric 2 again.
4. If resuming toward the full pre-registered N=32, budget for it as
   its own session — this run alone (16 tasks × 2 arms × builder +
   skeptic + evaluation) consumed the majority of a fresh session's
   token budget even after the N=16 reduction.
