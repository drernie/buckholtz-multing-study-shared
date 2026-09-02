# Run 2 extension (16 new tasks) — progress log

Manifest: manifest2.json (seed 20260902). No isolation="worktree" (broken hook
in this environment) -- plain background Agent calls, consistent with the
project's own verified-clean no-isolation baseline.

## RESUMED in new session (2026-09-02) -- solving arm now 31/32 complete.
## Only task030-treatment still outstanding (dispatched, running).

## Solving calls -- status this checkpoint
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
- [x] 025 both saved
- [x] 026 both saved
- [x] 029 both saved
- [x] 030 -- baseline saved, treatment PENDING (dispatched, not yet returned)
- [x] 031 both saved

## Why the prior checkpoint stopped: real, measured budget wall

21 completions received in the first session at ~150-170K tokens EACH in the
completion notification alone (before any of my own writing/saving cost) =
~3.3M+ tokens consumed just receiving Run 2 solving-arm results, for 21 of
the eventual 32 solving calls. This matched (and re-confirmed by direct
measurement) the wall PREREGISTRATION.md's own Addendum 1 had already
estimated and scoped down for.

## What actually exists after this checkpoint (real, usable results)

31 of 32 target solving-arm outputs for the "other half" of the corpus (task
pairs 012-031) are now saved to disk (this directory), with real,
tool-verified defect-catches or well-reasoned REJECT verdicts in every
completed output. Only task030-treatment remains outstanding.

NOT run: skeptic sub-calls, blind Run-3 scoring, K5 recheck. These 31(-32)
raw outputs are NOT yet scored against ground truth and are NOT part of any
statistical claim -- they are solving-arm transcripts only.

## Next step (per standing agreement with user)
Once task030-treatment lands: commit the batch, then STOP and report
completion to the user. Do NOT proceed to skeptic sub-calls / Run-3 blind
evaluation / K5 recheck without a separate, explicit go-ahead -- these are
the most expensive remaining stages and the user asked to gate them
individually given the real cost this run has demonstrated.
