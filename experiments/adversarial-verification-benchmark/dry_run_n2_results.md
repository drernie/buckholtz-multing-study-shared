# N=2 End-to-End Dry Run (2026-09-01)

Verification item 4: one defect task (task_023, target leakage) + one
clean task (task_028, at the time of this run) through the full
Run 1→2→3 pipeline, before committing to the real N=32 run.

## Pipeline stages exercised

1. **Baseline arm** — minimal prompt ("analyze this and report
   findings"), single pass. Run on both tasks.
2. **Treatment arm, builder step** — explicit FL-structured prompt
   (state claim → check controls → look for leakage/circularity/fixed
   params → verdict → self-contained draft claim for blind handoff).
   Run on both tasks.
3. **Treatment arm, skeptic sub-call** — genuinely separate `Agent`
   call, `skeptic` type, given ONLY the draft claim + original task
   (Context Asymmetry Rule), asked to falsify. Run on both draft claims.
4. **Treatment arm, synthesis** — Step 8a Response Matrix applied to
   each skeptic verdict, producing the final treatment output.
5. **Organizer relabeling** — private mapping of {baseline, treatment}
   → {Output X, Output Y}, kept out of the evaluator's prompt.
6. **Blind evaluator** — one batched call, refined rubric (post
   evaluator-pilot fix), scored all 4 (task, output) pairs without arm
   labels.

**All 6 stages ran correctly, no orchestration bugs found in the
mechanics themselves** — task content flowed through cleanly, the
skeptic sub-call was genuinely blind to the builder's reasoning, the
evaluator scored real (not hand-authored) outputs sensibly and matched
ground truth on all 4 pairs (all `defect_correctly_identified=true`,
`match=exact`, `false_positive_flagged=false`).

## Major unplanned finding: a second corpus bug, caught in real time

task_028 (at dry-run time: 12 FN / 19 FP / 94.2% accuracy) had the same
class of arithmetic bug found in `corpus_sanity_check.md` — except this
one was **missed by that sanity check itself**, because 028 has no
literal Python formula, only a stated confusion matrix + accuracy
figure, and the sanity check only re-derived tasks with an explicit
formula. **Three independent agents in this dry run — baseline,
treatment-builder, and (fully blind) the skeptic — each independently
recomputed 569/600=94.83% and flagged the mismatch with the stated
94.2%, with zero coordination between them.** That's about as strong a
confirmation as a single-session process can produce that the bug was
real, not an artifact of one agent's idiosyncrasy.

Fixed immediately (see task_028's `task.md`/answer key): confusion
matrix corrected to 13 FN / 22 FP (→ 565/600 = 94.17% ≈ 94.2%).
Additionally, both baseline and treatment (and the skeptic, on
task_028's draft) raised a second, legitimate concern the original task
text didn't close: group/unit and temporal leakage were never ruled
out for a dataset "collected over 3 separate weeks" with no stated
per-unit independence. Since this concern was raised independently and
correctly by every agent that saw the task, it's a genuine gap in the
task's own specification, not agent over-caution — closed by adding an
explicit independence/calibration statement to task_028's report text.
Proactively applied the same fix to task_030 and task_032 (both
similarly describe multi-record data collection without stating
record-level independence), rather than waiting to rediscover the same
pattern a third and fourth time.

## Secondary finding: treatment-arm prompt may under-elicit empirical verification

Task_023's **baseline** output (minimal prompt) went further than
**treatment**'s (explicit FL-structured prompt): baseline actually wrote
and ran a synthetic ablation script (`Bash` tool), producing a real
before/after F1 comparison (1.000 → 0.485 at chance) as direct evidence.
Treatment's draft *reasoned about* the same ablation as "the cheapest
differentiating test" but never executed it — likely because the
current treatment prompt's 5-step structure (state claim → check
controls → look for patterns → verdict → draft claim) reads as a
reasoning checklist rather than an explicit instruction to verify with
a tool where possible, so it steered the agent toward a well-organized
narrative rather than toward `integrity.md`'s own "Verify-Before-Claim"
instinct — which the baseline agent applied anyway, unprompted, using
its ambient always-on context.

**This is exactly the kind of gap a dry run exists to catch.**
Recommendation for Run 2's real treatment-arm prompt: add an explicit
line instructing the agent to write and execute a verification script
where the artifact's own claim is checkable (not just reason about
what such a script would show) — otherwise the treatment arm risks
under-performing relative to its own baseline on exactly the dimension
("does it verify, not just assert") the whole benchmark is designed to
measure.

## Response Matrix mechanic validated

Task_023's skeptic verdict was `WEAKENED` (correctly caught that
"is_active is essentially the logical inverse of churned" assumes an
undefined churn-label convention). The synthesis step applied the
Response Matrix correctly — softened the overclaim into a conditional
("under the standard assumption that churned = past cancellation..."),
kept the core finding intact — and the resulting final treatment output
still scored `exact` from the blind evaluator. Task_028's skeptic
verdict was `CONFIRMED-REAL` — no revision needed, draft promoted as-is.
Both outcomes are the mechanic working as designed, not a rubber stamp.

## What this dry run does NOT establish

- With n=2 and both tasks landing on a fairly blatant defect category
  (target leakage, arithmetic mismatch), both arms succeeded — this run
  does not discriminate between arms and isn't supposed to; the real
  N=26 spread of difficulty (including several genuinely subtle
  categories per `docs/146`) is what Phase G's actual statistical
  comparison depends on.
- Does not validate the `isolation:"worktree"` mechanism specifically
  (Agent tool, not Workflow, was used throughout this session — the
  Workflow-tool opt-in bar hasn't been met this session). If Run 2
  ultimately uses Workflow, this specific mechanic should get its own
  smake test.
- Only exercised 2 of 26 defect categories and 2 of the corpus's 3
  tiers (no Tier B task was dry-run). A clean pass on 2 tasks is not a
  guarantee the remaining 30 are bug-free — though the corpus sanity
  check (Verification item 3) already independently verified all 32.

## Action items before Run 2

1. Refine the treatment-arm prompt to explicitly request tool-based
   verification, not just structured reasoning (see Secondary finding
   above).
2. Corpus fixes (028, 030, 032) — done, see task files + this doc.
