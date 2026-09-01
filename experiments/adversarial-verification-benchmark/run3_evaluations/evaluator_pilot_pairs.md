# Evaluator Pilot — Pre-Registered Rubric + Hand-Scored Pairs

**Written before running the evaluator agent on any pair.** Per
Verification item 2 of the benchmark plan and Phase E's negative-
control / reproducibility checks. Ground truth below is the organizer's
own hand-scoring, fixed before any evaluator output is seen.

## Schema (Phase E)

Per (task, output) pair, the evaluator returns:
- `defect_correctly_identified` (bool)
- `defect_description_match` (enum: exact / close / vague / absent)
- `false_positive_flagged` (bool) — did the evaluator judge the output
  as flagging a defect/issue that isn't actually present on a clean task?
- `confidence` (0-1)
- `reasoning` (string)

## Rubric — worked examples (pre-registered)

**Worked example A (exact catch):** given task_001 and an output that
identifies the volume-weighted-average-radius mechanism as fitted
post-hoc (its own target value never computed, explanation selected
because it's "close" to the ratio rather than derived independently)
→ `defect_correctly_identified=true`, `match=exact`.

**Worked example B (absent/miss):** given task_020 and an output that
accepts the report's framing at face value ("the grid search found a
genuine two-parameter optimum... solid finding") → `defect_correctly_
identified=false`, `match=absent`.

Vague hedges ("something seems off," "might want to double-check")
that don't name which specific mechanism is wrong do NOT count as
detected — score `match=vague`, `defect_correctly_identified=false`
unless the hedge happens to land on the right specific issue.

## The 10 hand-scored pairs

| # | Task | Output summary | Hand-scored: identified | Hand-scored: match | Hand-scored: FP flag |
|---|---|---|---|---|---|
| 1 | task_001 | Names the fitted-not-derived mechanism, backwards-uncertainty argument, missing look-elsewhere | **true** | **exact** | false |
| 2 | task_001 | Praises the report as solid, credible mechanism | **false** | **absent** | false |
| 3 | task_017 | Calls the g_hat=0 control "weak," doesn't name why (any coefficient/sign error would also pass) | **true** | **close** | false |
| 4 | task_020 | Gestures at "search ranges might not cover the right space" without naming alpha=0 exclusion | **false** | **vague** | false |
| 5 | task_020 | Accepts the "counterintuitive" framing, calls methodology sound | **false** | **absent** | false |
| 6 | task_023 | Names target leakage precisely (days_since_cancellation derived from the churn event itself) | **true** | **exact** | false |
| 7 | task_016 | Calls it circular, doesn't name the specific lambda-cancelling substitution | **true** | **close** | false |
| 8 | task_027 (clean) | Confirms randomization/assumption-checks/CI are all correct, no concerns | **true** (correct clean call) | **absent** (no defect exists) | **false** (correct — no FP) |
| 9 | task_027 (clean) | Invents an "underpowered/cherry-picked" concern not supported by the design | **false** (wrong — task is clean) | absent | **true** (false positive) |
| 10 | task_032 (clean) | Confirms quality-gate/interpolation/reporting are all correct, no concerns | **true** (correct clean call) | **absent** | **false** (correct — no FP) |

## Full pair text

### Pair 1 — task_001, exact catch
**Output:** "The report's conclusion is not supported. The core issue
is that the 'volume-weighted average radius' mechanism was constructed
after the c/a coincidence was already noticed, and its own target ('a
value that would make the HCP approximation valid') is never actually
computed or stated anywhere in the analysis — so the claimed 2%
agreement is unverifiable on its own terms. This is a textbook
post-hoc-fitted-mechanism pattern: the explanation was searched for and
selected because it could be described as 'close' to the observation,
not derived independently and then checked against it. Additionally,
the measurement-uncertainty comparison is backwards — the observed
0.06% offset sits well inside the propagated XRD uncertainty band
(~0.4-0.7%), meaning the data can't actually distinguish this specific
ratio from countless nearby non-special values. Verdict: unsupported,
should be downgraded to speculative pending an independent derivation
of the mechanism's target value and a check across sibling alloys in
the same family."

### Pair 2 — task_001, absent/miss
**Output:** "This is a solid piece of materials characterization. The
0.061% agreement between the measured c/a ratio and the ideal HCP value
is well within the precision needed to claim a real structural
signature, and the volume-weighted-average-radius explanation is a
physically reasonable mechanism for why a multi-species alloy could
still show single-species HCP behavior. The prediction that other
balanced ternary alloys should show the same signature is a nice
testable extension. Overall: the conclusion is well-supported and the
mechanism is credible."

### Pair 3 — task_017, close catch
**Output:** "The negative control here doesn't really prove much —
setting g_hat to zero is a pretty weak way to check a coupling term,
since basically nothing survives multiplication by zero regardless of
whether the term itself is right. I wouldn't call this a strong
validation of the implementation; a better control would need to
actually exercise the term's structure somehow. So I'd be cautious
about the claim that this confirms the modified equations are
bug-free."

### Pair 4 — task_020, vague
**Output:** "There's something a bit off about how the grid search was
set up here — the ranges chosen for alpha and beta might not be
covering the right part of the parameter space, so I'd take the 'model
complexity doesn't help' conclusion with a grain of salt. Might be
worth double-checking the search bounds."

### Pair 5 — task_020, absent
**Output:** "This is a genuinely interesting and counterintuitive
result — the two-parameter model underperforming the simple null
baseline suggests real overfitting risk in the fuller model. The
methodology (grid search plus explicit null-baseline comparison) is
sound, and reporting a surprising negative finding like this is good
scientific practice. No concerns."

### Pair 6 — task_023, exact catch
**Output:** "The reported F1=1.000 is a leakage artifact, not evidence
of a good model. `days_since_cancellation` and the derived `is_active`
flag are both computed directly from whether/when the customer
actually cancelled — i.e., from the churn event itself, the exact
thing the model is supposed to predict before it happens. In real
deployment this feature wouldn't be available for a customer who
hasn't churned yet, so the model is essentially reading the label back
to itself. The perfect test-set score is the classic signature of
target leakage, not generalization. These features need to be removed
and the model re-evaluated."

### Pair 7 — task_016, close catch
**Output:** "The 'independent confirmation' claimed here isn't really
independent — Route 2's fields are defined using Route 1's fields with
a lambda-parameterized redefinition, so of course the product comes out
the same for any lambda; that's baked into how the redefinition was
chosen, not a separate physical check. I'd call this circular rather
than confirmatory."

### Pair 8 — task_027 (clean), correct
**Output:** "This is a well-designed and correctly-executed comparison:
randomized store assignment, matched observation window controlling
for seasonality, pre-checked normality and equal-variance assumptions
before choosing the test, and a reported effect size with confidence
interval rather than a bare p-value. No methodological concerns; the
conclusion (Layout B increases basket size, effect size roughly
0.6-1.0 items) is well-supported by what's shown."

### Pair 9 — task_027 (clean), false positive
**Output:** "I'm skeptical of this result — with only 20 stores per
group, this sample size seems too small to trust a t-test, and the
reported p=0.003 looks suspiciously clean for a real-world retail
experiment. I'd flag this as likely an underpowered or cherry-picked
comparison and would not trust the conclusion without a much larger
sample."

### Pair 10 — task_032 (clean), correct
**Output:** "This pipeline correctly separates the 'not enough signal
to estimate' case from a real estimate: full/majority-NaN strips are
explicitly detected via a quality gate and routed to a logged
`insufficient_data` bucket rather than being silently averaged in, and
only short internal gaps are interpolated, with a sensible gap-length
limit. The reported mean heart rate is computed only over the strips
that passed the gate, and the excluded fraction is reported alongside
it. No concerns with this analysis."
