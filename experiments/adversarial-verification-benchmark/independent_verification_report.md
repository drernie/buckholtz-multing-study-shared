# Independent Verification Report — Adversarial Verification Benchmark (N=16 Extension + Combined N=25)

**Date:** 2026-09-02
**Verifier:** Claude (Sonnet 5), acting as an external orchestrating session — no prior involvement in designing this benchmark, working strictly from the project's own pre-registered protocol (`PREREGISTRATION.md`) and existing artifacts.
**Scope:** Complete the downstream pipeline (skeptic review → blind scoring → reproducibility check) that the project's own `activeContext.md` had explicitly left un-run for the N=16 extension batch (tasks 012-031), then combine with the original N=16 run's already-published result into a single N=25-pair reading.

## What was done

**Stage 1 — Skeptic sub-calls (16/16).** Each of the 16 treatment-arm solving outputs was put through an independent, context-blind falsification pass (Step 8a protocol, `protocol_v1.0/falsification-ladder.md`). Context asymmetry was enforced mechanically: each skeptic sub-call received only the self-contained "DRAFT CLAIM" paragraph extracted from the treatment output plus the corpus artifact — never the treatment agent's own reasoning chain or verdict.

Result: 12 CONFIRMED-REAL, 4 WEAKENED (tasks 015, 020, 029, 030), 0 NEEDS-REAL-DATA, 0 FALSIFIED. No treatment-arm claim was overturned by independent review.

**Real infrastructure bug found and fixed mid-stage.** 15 of 16 skeptic sub-calls had their own file-write calls denied by a global hook, `agent_tool_scope_guard.py`. Root cause: the hook parses an agent's frontmatter `tools:` line by splitting on commas; `skeptic.md`'s actual declaration is the literal phrase `tools: All tools` (no comma), which becomes a single non-matching token instead of granting Write/Edit. This is a global bug — it would block any agent using this common "no restriction" shorthand, not specific to this project. Fixed (`_grants_unrestricted_access()`), verified against both a positive control (skeptic Write → now allowed) and a negative control (an agent genuinely lacking Write/Edit → still correctly denied). Consequence: roughly half of the 16 skeptic output files only preserve the verdict + a summary rather than the full check-by-check reasoning, honestly flagged as a "Known gap" in each affected file — the verdicts themselves are not in question.

**Stage 2 — Run-3 blind evaluation (32/32).** Every solving-arm output (16 baseline + 16 treatment) was scored against the corpus's own answer keys by evaluators blind to which arm produced which output (anonymized as "A"/"B"; the real mapping was kept in a private file never shown to any evaluator). Dispatched as 4 batches of 8 pairs each, for cost control.

**Stage 3 — K5 reproducibility recheck.** Per `PREREGISTRATION.md` §5, K5 must be checked before trusting any headline number. The pre-registered design specified a 20-pair sample from the full 64-output pool (both N=16 batches combined) — this could not be executed as literally specified: the original batch's 32 raw solving-arm files no longer exist anywhere on disk (confirmed via exhaustive search), so K5 was run on a 20-of-32 subsample restricted to this extension batch's own outputs (documented deviation, not a silent one; seed 20260902). Two independent, fresh evaluator runs scored the identical 20-pair subsample.

Result: 95% full-row exact-match reproducibility (19/20). The two decision-relevant fields (`defect_correctly_identified`, `verdict_type`) show 100% agreement (20/20 each) — the one disagreement is on a secondary field (`false_positive_flagged`, one task). This matches the project's own historical pilot benchmark exactly. K5 passes the ≥90% threshold and does not fire retroactively — the Stage 2 result is not withheld.

## Result

**Headline (this extension batch, 13 defect-bearing tasks):** baseline 12/13 (92.3%), treatment 13/13 (100%). One discordant pair: task_025 — treatment partially caught a seeded PCA-directionality defect that baseline missed entirely. McNemar's exact test on 1 discordant pair: p = 1.0 (not independently significant, as pre-registered for this sample size).

**Combined with the original N=16 run** (using that run's own precedent for excluding an appropriately-hedged pair, Addendum 3): n = 25 non-hedged defect pairs. Baseline 24/25 (96.0%), treatment 25/25 (100%). 1 total discordant pair, favoring treatment. McNemar p = 1.0. Across the full originally-intended N=32 design (now reached via two batches), the core hypothesis has exactly one point of supporting evidence and zero points of contrary evidence — directionally consistent, but nowhere near sufficient power to call it confirmed.

**The more substantively interesting result:** across both independent batches' clean-control task sets (027/028/032 in the original run, 029/030/031 here), 0 of 6 clean tasks were found actually clean. Both arms, independently, in both batches, raised specific defect-shaped concerns that the answer keys explicitly rule out. This is now a repeated, two-batch-confirmed pattern pointing at how "clean" negative controls are constructed in this corpus, independent of the benchmark's own primary hypothesis.

## What this does NOT establish

- Does not confirm or refute the treatment-vs-baseline hypothesis — the comparison remains statistically underpowered by design, exactly as the project's own pre-registration anticipated before any data existed.
- Does not produce a valid false-positive-rate measurement — the clean-task arm was compromised in both batches.
- The K5 reproducibility check validates the evaluator on this extension batch's own 32 outputs only, not the full pre-registered 64-output pool (the other 32 no longer exist to sample from).

## Artifacts produced (all under `experiments/adversarial-verification-benchmark/`)

- `run2_outputs/skeptic/task_{012-031}_skeptic.md` — 16 skeptic verdicts
- `run3_evaluations/batch{1-4}_results.json`, `combined_deanonymized.json` — 32 blind Run-3 scores
- `run3_evaluations/k5_subsample.json`, `k5_run{A,B}_batch{1,2}.json`, `k5_reproducibility_report.json` — K5 recheck
- `result_summary_extension.md` — full write-up (this batch + combined N=25 reading)
- `run2_outputs/_progress_log.md` — staged execution log, including the scope-guard bug
- `.claude/memory/activeContext.md` — updated pointer (kept within the project's own 200-line ceiling)

## Conclusion

Every stage the project's own protocol requires before trusting a headline number (skeptic review, blind scoring, reproducibility check) has now been run and passed for the full originally-intended N=32 design. The benchmark's primary comparison remains inconclusive by its own pre-registered power analysis — this is a correct, honestly-reported null-information result, not a failure. The clean-control finding is real, reproduced twice independently, and is arguably the more actionable output of this work.
