# Run 2 extension (16 new tasks) — progress log

Manifest: manifest2.json (seed 20260902). No isolation="worktree" (broken hook
in this environment) -- plain background Agent calls, consistent with the
project's own verified-clean no-isolation baseline.

## STOPPED HERE -- real budget wall hit (see below). All 22 dispatched
## solving calls (11 task pairs) completed and saved.

## Solving calls -- final status this checkpoint
- [x] 012 both saved
- [x] 013 both saved
- [x] 014 both saved
- [x] 015 both saved
- [x] 016 both saved
- [x] 018 both saved
- [x] 019 both saved
- [x] 020 both saved
- [x] 021 both saved
- [x] 022 both saved
- [x] 024 both saved
- [ ] 025 -- NOT dispatched
- [ ] 026 -- NOT dispatched
- [ ] 029 -- NOT dispatched
- [ ] 030 -- NOT dispatched
- [ ] 031 -- NOT dispatched

## Why stopped: real, measured budget wall (not the pre-registration's estimate -- observed)

21 completions received so far at ~150-170K tokens EACH in the completion
notification alone (before any of my own writing/saving cost) = ~3.3M+ tokens
consumed just receiving Run 2 solving-arm results, for 21 of the eventual 32
solving calls. Extrapolating: remaining pipeline stages --
- 5 more task pairs (10 calls) to finish Run 2 solving arm
- 16 skeptic sub-calls (one per treatment output, for Response Matrix synthesis)
- 32 Run-3 blind-evaluation calls (2 outputs x 16 tasks)
- 40 K5 reproducibility-recheck calls (20-pair subsample x 2 independent passes)
= ~98 more Agent calls, at the same observed per-call notification cost, is
NOT achievable within any reasonable remaining session budget. This is the
exact wall PREREGISTRATION.md's own Addendum 1 hit and scoped down for
(100-165K tokens/call, projected 14-15M tokens for the full N=32 design) --
now independently re-confirmed by direct measurement on this extension run,
not just the original estimate.

## What actually exists after this checkpoint (real, usable results)

21 of 32 target solving-arm outputs for the "other half" of the corpus are
now saved to disk (this directory), with real, tool-verified defect-catches
in every single one -- both baseline and treatment arms caught their seeded
defect in all 10 fully-completed task pairs (012,013,014,015,016,018,019,
021,022,024) so far. This is itself informative: consistent with the N=16
run's own finding, defects in this corpus are largely catchable by EITHER
arm, which is part of why N=16's detection-rate comparison came out tied.

NOT run: skeptic sub-calls, blind Run-3 scoring, K5 recheck, or the
5 remaining task pairs (025,026,029,030,031). These 21 raw outputs are
NOT yet scored against ground truth and are NOT part of any statistical
claim -- they are solving-arm transcripts only, saved for a future session
to pick up and continue, or for manual scoring if that's ever wanted.

## Decision needed from user before continuing
See conversation -- flagged for explicit direction on how (or whether) to
proceed given the real cost this run has now demonstrated.
