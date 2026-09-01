# Evaluator Pilot — Results (2026-09-01)

Verification item 2 of the benchmark plan. Evaluator model: `opus`
(different from this session's default model, per Independent
Verification Strength Ladder — "different model" rates Medium vs.
"same model, isolated context" Weak-Medium). Rubric and hand-scored
ground truth were written and committed **before** any evaluator call
(`evaluator_pilot_pairs.md`), per Phase E's "Real vs theater?"
mitigation.

## Raw results

| # | Task | Hand (organizer) | Pass A | Pass B | A=hand? | B=hand? | A=B? |
|---|---|---|---|---|---|---|---|
| 1 | 001 | true/exact/false | true/exact/false | true/exact/false | ✅ | ✅ | ✅ |
| 2 | 001 | false/absent/false | false/absent/false | false/absent/false | ✅ | ✅ | ✅ |
| 3 | 017 | true/**close**/false | true/**exact**/false | true/**close**/false | ❌ (match) | ✅ | ❌ (match) |
| 4 | 020 | false/vague/false | false/vague/false | false/vague/false | ✅ | ✅ | ✅ |
| 5 | 020 | false/absent/false | false/absent/false | false/absent/false | ✅ | ✅ | ✅ |
| 6 | 023 | true/exact/false | true/exact/false | true/exact/false | ✅ | ✅ | ✅ |
| 7 | 016 | true/**close**/false | true/**exact**/false | true/**exact**/false | ❌ (match) | ❌ (match) | ✅ |
| 8 | 027 (clean) | true/absent/false | true/absent/false | true/absent/false | ✅ | ✅ | ✅ |
| 9 | 027 (clean) | false/absent/true | false/absent/true | false/absent/true | ✅ | ✅ | ✅ |
| 10 | 032 (clean) | true/absent/false | true/absent/false | true/absent/false | ✅ | ✅ | ✅ |

## Scores against the pre-registered thresholds

- **Full-tuple agreement with hand-scoring:** Pass A = 8/10 = **80%**
  (below the 85% bar); Pass B = 9/10 = **90%** (above it). The two
  passes disagree with *each other* on the pairs where they disagree
  with the hand score — not a case of picking whichever pass looks
  better.
- **Field-level agreement** (both passes, both against hand-scoring):
  `defect_correctly_identified` — **10/10 (100%)**, both passes.
  `false_positive_flagged` — **10/10 (100%)**, both passes.
  `defect_description_match` — 8/10 (Pass A), 9/10 (Pass B); both
  disagreements are exact-vs-close calls, never identified-vs-absent.
- **Reproducibility (Pass A vs Pass B, same pairs, fresh calls):**
  9/10 = **90%** — meets the pre-registered ≥90% bar, but only by
  landing exactly on it; the one divergence (pair 3) is the same
  boundary that also diverged from hand-scoring.
- **Primary-metric impact:** Phase F's actual detection-rate metric
  only requires `match ∈ {exact, close}` — both passes and the hand
  score placed every pair in the same {exact,close}-or-not band. The
  disagreement never crosses that boundary, so it would not have
  changed a single task's classification for Phase F's metric 1, 2, or
  3 as currently defined.

## Diagnosis

The instability is confined to the exact/close boundary on two
pairs — both involving a "the mechanism is tautological/circular by
construction" defect (task_017's trivial-zero control, task_016's
lambda-redefinition identity) — where the judged output names the
right general phenomenon in fairly specific language without using the
literal algebraic notation from the ground truth. My own pre-registered
worked examples (A: exact catch: B: absent/miss) both anchor the
identified/absent boundary, not the exact/close boundary — that gap in
the rubric is the root cause, not evaluator unreliability on the
decision-relevant fields.

Re-reading pair 7's judged output against my own hand-scoring
rationale: the output does state that Route 2's fields were "defined...
with a lambda-parameterized redefinition... baked into how the
redefinition was chosen" — which is close to naming the actual
mechanism, just without the literal substitution. Both evaluator passes
independently called this "exact." On reflection, my own "close" hand
score for pair 7 was arguably too strict — this looks like a genuine
rubric-boundary ambiguity, not a one-sided evaluator error.

## Verdict (oracle-adequacy-gate framing)

- **Gameable?** No sign of it — the evaluator did not upgrade any
  output's score for confident tone alone (pair 2 and pair 5, both
  confident and wrong, were correctly scored false/absent).
- **Real vs theater?** Reasoning fields are substantive and cite the
  actual mechanism in every pair, not generic praise/criticism.
- **Negative control?** This pilot's own pairs 2, 5, 9 (obvious misses /
  a false-positive plant) were all caught correctly in both passes.
- **Reproducible?** 90% — meets the bar, marginally, with the failure
  mode isolated and understood (see Diagnosis).
- **Measures the intent?** Per this pilot's own hand-check (<85% on
  Pass A's strict full-tuple read), the plan's own pre-written rule
  says: mark every downstream metric using the failing field `[WEAK]`
  until fixed.

**Net verdict: WEAK, not INADEQUATE.** The two fields that actually
drive Phase F's primary outcome metrics (`defect_correctly_identified`,
`false_positive_flagged`) are 100% reliable across both passes and
against hand-scoring. The `defect_description_match` field's exact/close
distinction — used only for Phase B's `[EXPLORATORY]` stratification
breakdown, never a primary metric — needs a rubric fix before being
trusted on its own.

## Fix applied before Run 2

Added a third worked example to the pre-registered rubric, anchoring
the exact/close boundary specifically (using pair 7's actual text as
the worked case, since it's the one that reproduced across both
passes): naming the mechanism in accurate non-notational language
counts as **exact** if it correctly states *why* the invariance holds
(the redefinition was chosen to force it) even without literal algebra;
**close** is reserved for outputs that correctly identify the
phenomenon category ("this looks circular / tautological") without
stating why. This resolves pair 3 and pair 7 under the clarified rule
(both would now score exact) without touching the two fields that were
already 100% reliable.

## What this pilot does NOT establish

- Does not re-run the corrected rubric through a third pass — the fix
  is applied going into Run 3, not independently re-validated here.
  Phase E's own reproducibility check on Run 3's real 20-pair
  subsample is still required and will exercise the corrected rubric
  for the first time under real conditions.
- n=10 synthetic pairs, hand-authored by the organizer to cover a
  spread of match categories — not a random sample of what Run 2 will
  actually produce. This pilot validates the rubric's logic and the
  evaluator's basic reliability, not the full Run 3 evaluation.
