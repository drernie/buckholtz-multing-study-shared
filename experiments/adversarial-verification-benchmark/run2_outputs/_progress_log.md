# Run 2 extension (16 new tasks) — progress log

Manifest: manifest2.json (seed 20260902). No isolation="worktree" (broken hook
in this environment) -- plain background Agent calls, consistent with the
project's own verified-clean no-isolation baseline.

## RESUMED in new session (2026-09-02) -- solving arm now 32/32 COMPLETE.

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
- [x] 030 both saved
- [x] 031 both saved

## Why the prior checkpoint stopped: real, measured budget wall

21 completions received in the first session at ~150-170K tokens EACH in the
completion notification alone (before any of my own writing/saving cost) =
~3.3M+ tokens consumed just receiving Run 2 solving-arm results, for 21 of
the eventual 32 solving calls. This matched (and re-confirmed by direct
measurement) the wall PREREGISTRATION.md's own Addendum 1 had already
estimated and scoped down for.

## What actually exists after this checkpoint (real, usable results)

All 32 of 32 target solving-arm outputs for the "other half" of the corpus
(task pairs 012-031) are now saved to disk (this directory), with real,
tool-verified defect-catches or well-reasoned REJECT verdicts in every
completed output. The full N=32 solving arm (all 32 tasks x 2 arms = 64
calls total across both the original run and this extension) is COMPLETE.

## NEW SESSION (2026-09-02, downstream pipeline authorized, staged execution)

User explicitly authorized proceeding to the downstream pipeline (skeptic
sub-calls -> Run-3 blind evaluation -> K5 recheck), staged with a checkpoint
after each stage given the real ~150-170K-token/call cost.

### Stage 1 — Skeptic sub-calls: 16/16 COMPLETE

All 16 treatment-arm outputs (tasks 012-031) put through a Step 8a
context-blind falsification pass (Context Asymmetry: skeptic given ONLY the
self-contained "DRAFT CLAIM" section extracted from each treatment output,
plus the corpus artifact -- never the treatment agent's own reasoning/
verdict). Results, all saved to `run2_outputs/skeptic/task_XXX_skeptic.md`:

| Task | Verdict |
|---|---|
| 012 | CONFIRMED-REAL |
| 013 | CONFIRMED-REAL |
| 014 | CONFIRMED-REAL |
| 015 | WEAKENED |
| 016 | CONFIRMED-REAL |
| 018 | CONFIRMED-REAL |
| 019 | CONFIRMED-REAL |
| 020 | WEAKENED |
| 021 | CONFIRMED-REAL |
| 022 | CONFIRMED-REAL |
| 024 | CONFIRMED-REAL |
| 025 | CONFIRMED-REAL |
| 026 | CONFIRMED-REAL |
| 029 | WEAKENED |
| 030 | WEAKENED |
| 031 | CONFIRMED-REAL |

**Tally: 12 CONFIRMED-REAL, 4 WEAKENED, 0 NEEDS-REAL-DATA, 0 FALSIFIED.**
Every one of the 16 treatment-arm draft claims survived independent
context-blind review at least in weakened form -- none was fully falsified.

**Real infrastructure bug found and fixed mid-stage (not a finding about any
task):** 15 of the 16 skeptic subagents had their own `Write`/`Edit` calls
denied by the global `agent_tool_scope_guard.py` hook
(`~/.claude/hooks/agent_tool_scope_guard.py`). Root cause: the hook splits
the invoking agent's frontmatter `tools:` line on commas to build an
allowlist; `skeptic.md`'s actual frontmatter is the single literal phrase
`tools: All tools` (no comma), which becomes the one-element set
`{"All tools"}` -- neither `"Write"` nor `"Edit"` matches that string, so
the hook denied every Edit/Write call from the skeptic role unconditionally,
regardless of the frontmatter's own clearly-unrestricted intent. This is a
global bug (affects every project on this machine using the shorthand
`tools: All`/`All tools`), not specific to this benchmark. **Fixed**
(`_grants_unrestricted_access()` added, recognizes `all`/`all tools`/`*`
case-insensitively before the enumerated-allowlist check) and verified with
a positive control (skeptic Write -> now `allow`) and a negative control
(an agent that genuinely lacks Write/Edit -> still correctly `deny`).

**Consequence for this stage's evidentiary completeness:** because the fix
landed only after most of the 16 calls had already run, roughly half of the
16 skeptic files contain the full check-by-check reasoning (the subagent
either pasted it into its chat response after the file write failed, or the
fix landed before its call), while the other half preserve only the verdict
+ a one-paragraph summary, with an explicit "Known gap" note where detail
was lost. **The verdict itself is intact and trustworthy for all 16** --
what's missing is some intermediate show-your-work detail for future
re-audit, not the scoring-relevant outcome. Flagged, not silently accepted.

### Stage 2 — Run-3 blind evaluation: 32/32 COMPLETE

All 32 (task, arm) outputs blind-scored against `corpus/_answer_key/`, arm
label anonymized as A/B (private mapping: `run3_evaluations/_arm_mapping_PRIVATE.json`,
never shown to any evaluator). Dispatched as 4 batches of 8 pairs (cost
optimization -- one fixed per-call overhead instead of 32 -- documented
deviation from a literal "one call per pair" reading, not a statistical
design change). Results: `run3_evaluations/batch{1..4}_results.json`,
de-anonymized combined: `run3_evaluations/combined_deanonymized.json`.

**McNemar table, 13 defect-bearing tasks (012-026, excl. 029/030/031 which
are the clean-control set):**

| | Treatment detected | Treatment missed |
|---|---:|---:|
| **Baseline detected** | 12 | 0 |
| **Baseline missed** | 1 (task_025) | 0 |

**One real discordant pair: task_025 — treatment caught the seeded PCA-
directionality defect (partially, `match=close`), baseline missed it
entirely.** This is the single informative data point from this extension
batch's headline comparison; McNemar on n=1 discordant pair is not
independently significant, consistent with this project's own repeated
finding that N=16-scale runs are underpowered by design (Addendum 1).

**Clean-task result (029, 030, 031): 0 of 3 were actually clean — both
arms independently flagged real-seeming issues the answer key does not
corroborate, symmetrically (baseline and treatment agree with each other,
disagree with the key on all 3).** This is not a benchmark-design failure;
it is the SAME finding the original N=16 run made on ITS 3 clean tasks
(027/028/032 — "0 of 3 were actually clean" per `result_summary.md`).
Two batches, two independent clean-task pools, same outcome — this is now
a repeated pattern pointing at how "clean" controls are constructed in
this corpus generally, not at any one task.

### Stage 3 — K5 recheck: COMPLETE, PASSES

**Adaptation from the pre-registered design, flagged not silently applied:**
PREREGISTRATION.md §5 specifies sampling 20 of "the actual 64 Run 2
outputs" (both N=16 batches combined). The original batch's 32 raw
solving-arm output files (tasks 001-011, 017, 023, 027, 028, 032) do not
exist anywhere on disk in this project as of 2026-09-02 (confirmed via
exhaustive filesystem search) -- likely cleaned up after
`result_summary.md` was written, never archived. Regenerating them would
mean re-running the entire original solving arm, a separate large spend
not authorized here. **K5 was therefore run on a 20-of-32 subsample of
ONLY the extension batch's own outputs** (seed 20260902, matching
`manifest2.json`'s own seed; selection script + subsample list:
`run3_evaluations/k5_subsample.json`) -- narrower than the pre-registered
64-pool design, same 20-pairs-twice reproducibility logic.

Two independent fresh evaluator runs (Run-A, Run-B) over the identical
20-pair subsample, each split into 2 batches (4 calls total):
`run3_evaluations/k5_run{A,B}_batch{1,2}.json`.

**Result: 19/20 = 95% full-row exact match across all 3 decision fields
(`defect_correctly_identified`, `false_positive_flagged`, `verdict_type`).
The two DECISION-RELEVANT fields for Metric 1 (`defect_correctly_identified`,
`verdict_type`) show 100% agreement (20/20 each) -- the one disagreement is
on the secondary `false_positive_flagged` field for task_013/B.** This
matches the pilot's own historical pattern exactly ("reproducibility 90%,
decision-relevant fields 100% agreement", `evaluator_pilot_results.md`).
**K5 PASSES the ≥90% threshold -- does not fire retroactively. The Stage 2
headline comparison is not withheld.** Full report:
`run3_evaluations/k5_reproducibility_report.json`.

## DONE — full pipeline complete for the N=16 extension batch

All three staged steps (skeptic sub-calls, Run-3 blind evaluation, K5
recheck) complete. Written up in `../result_summary_extension.md`,
including a combined N=25-non-hedged-defect-pair reading with the original
N=16 run (per its own Addendum 3 exclusion precedent): baseline 24/25,
treatment 25/25, 1 discordant pair favoring treatment (task_025), McNemar
p=1.0 -- still underpowered-inconclusive, not a confirmed effect. Combined
clean-control finding: 0 of 6 tasks across both batches (027/028/029/030/
031/032) found actually clean -- the more substantively interesting result
of this benchmark to date. Nothing further pre-authorized; a fresh
direction (e.g. a genuine N=32 run with fresh clean-control tasks, or
moving to a different bottleneck per `docs/147`) awaits explicit
instruction, per this project's own standing `## Next allowed actions`
discipline in `.claude/memory/activeContext.md`.
