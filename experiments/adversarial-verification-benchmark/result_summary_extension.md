# Result Summary — Adversarial Verification Benchmark, N=16 Extension Run (2026-09-02)

Per `PREREGISTRATION.md` §6 and its own item 4 ("resuming toward the full
pre-registered N=32 still needs its own session's budget; not attempted
here" — `result_summary.md`, original N=16 run). This document covers the
SECOND 16-task batch (`manifest2.json`, tasks 012-031) that completes the
originally pre-registered 32-task corpus. It does not edit or supersede
`result_summary.md` (the original N=16 run) — both stand, and a combined
reading is given at the end of this file.

**This run is exploratory, not confirmatory**, same qualifier as the
original run and for the same reason (Addendum 1's N=32→N=16-per-batch
budget-driven split) — every number below must be read with that qualifier.

## Headline result: 13 defect pairs, 1 discordant, favoring treatment

Full pipeline run this session, staged with checkpoints per standing
agreement: solving arm (32/32, prior session) → skeptic sub-calls (16/16,
Step 8a context-blind) → Run-3 blind evaluation (32/32, arm-anonymized) →
K5 reproducibility recheck (20-pair subsample, 95% agreement, PASSES).
Full detail, including the real infrastructure bug found and fixed
(`agent_tool_scope_guard.py`'s "tools: All tools" parsing) and the
K5 sampling-pool adaptation (original N=16 batch's raw files no longer
exist on disk): `run2_outputs/_progress_log.md`.

**Metric 1 (detection rate), n=13 defect pairs:**

| Arm | Detected |
|---|---|
| Baseline (ambient-default) | 12/13 = 92.3% |
| Treatment (explicit FL protocol + skeptic) | 13/13 = 100% |

McNemar's exact test: 1 discordant pair (task_025, treatment detected —
partially, `match=close` — what baseline missed entirely), 0 pairs in the
other direction. With only 1 total discordant pair, McNemar's exact test
gives **p = 1.0** — not independently significant, exactly the
underpowered-by-design outcome `PREREGISTRATION.md` warned about before
any data existed. **This is a real, single informative data point in
treatment's favor, not a confirmed effect.**

**Metric 2 (false-positive rate): still not cleanly measurable.** All 3
selected clean-control tasks (029, 030, 031) again turned out to have
real, substantive-seeming problems that both arms independently raised
and the answer key does not corroborate — see "Corpus integrity findings"
below. Same outcome as the original run's 027/028/032.

## Corpus integrity findings (repeated pattern, now across 2 independent batches)

- **029, 030, 031: 0 of 3 clean-control tasks were actually clean**,
  scored strictly against the answer key. Both arms (baseline and
  treatment) independently and consistently raised specific, code-checked
  objections the answer key explicitly rules out as non-defects (task_029:
  parameter-provenance/circularity concern the key says is resolved;
  task_030: leakage/grouping concern the key explicitly says "should not"
  be flagged; task_031: citation/growth-rate-discontinuity concern the key
  treats as standard, non-disqualifying practice).
- **This is now a repeated finding, not a one-batch anomaly**: the original
  N=16 run found the identical pattern on ITS 3 clean tasks (027/028/032 —
  "0 of 3 were actually clean," `result_summary.md`). **Across the full
  originally-intended N=32 corpus's clean-control set (6 tasks total: 027,
  028, 029, 030, 031, 032), 0 of 6 have been found actually clean by any
  solving agent that has run against them.** This is a substantive finding
  about this corpus's clean-control construction, independent of the
  benchmark's own headline hypothesis, and is now backed by two
  independent batches rather than one.
- Per this project's own `perelman-audit.md` "infinite surgery" anti-pattern
  (invoked explicitly in the original run's own write-up for the same
  reason): this is not re-litigated further here by re-fixing 029/030/031 —
  logged as a structural corpus-construction finding, not chased into a
  fourth patch-and-reverify cycle.

## What this run does NOT establish

- **Does not confirm or refute the core hypothesis on its own** — n=13 is
  underpowered by design (pre-registered), and the single discordant pair
  (task_025) is a real, tool-verified data point, not a statistically
  significant effect.
- **Does not measure false-positive rate at all** — same as the original
  run, the clean-task arm of this batch was compromised.
- **The K5 recheck validates Run-3 evaluator reproducibility on THIS
  batch's own 32 outputs, not the full pre-registered 64-output pool**
  (the original batch's raw files no longer exist on disk — see
  `_progress_log.md` for the exact adaptation).

## Combined reading: both N=16 batches together (n=25 non-hedged defect pairs)

Per the original run's own Addendum 3 precedent (task 004 excluded as
`appropriately_hedged`, not counted as a miss), the combined defect-pair
pool across both batches is:

- Original batch: 12 non-hedged defect pairs (`task_004` excluded per
  Addendum 3), both arms 12/12 = 100%, 0 discordant.
- Extension batch (this file): 13 defect pairs (no hedged exclusions —
  none of this batch's Run-3 evaluations returned `appropriately_hedged`
  on a defect task), baseline 12/13, treatment 13/13, 1 discordant
  (task_025, favoring treatment).

**Combined: n=25 non-hedged defect pairs. Baseline 24/25 = 96.0%, treatment
25/25 = 100%. 1 total discordant pair (favoring treatment), 0 in the other
direction.** McNemar's exact test on b=0, c=1: **p = 1.0** — with only one
discordant pair across the full combined pool, the comparison remains
statistically inconclusive by construction; there is no configuration of a
single discordant observation that reaches significance. **Kill criterion
K1's first condition (p≥0.05) is met; K1's second condition (discordant
ratio 0.67-1.5) does not apply cleanly with a 0/1 split, so this is
reported as underpowered-inconclusive rather than a clean K1 "kill."**

**Honest characterization:** across the full originally-intended N=32
design (now reached, in two batches, via 25 non-hedged defect pairs + a
combined 0/6 clean-control finding), the core hypothesis (explicit FL
protocol + skeptic sub-call detects more defects than ambient-default
alone) has exactly ONE piece of evidence in its favor (task_025) and zero
pieces of evidence against it, out of 25 defect-task comparisons. This is
directionally consistent with the hypothesis but nowhere near sufficient
power to claim it confirmed — an honest reading is "no discordant evidence
against the hypothesis, one weak point of support for it, comparison
remains underpowered." The corpus-integrity finding (0/6 clean controls
actually clean) is, as it was in the original run, the more substantively
interesting and better-supported result of this benchmark to date.
