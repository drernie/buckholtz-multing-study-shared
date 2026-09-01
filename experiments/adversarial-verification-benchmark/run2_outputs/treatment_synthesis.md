# Run 2 — Treatment Arm: Skeptic Response Matrix Synthesis (2026-09-02)

Per Step 8a: for each of the 16 treatment drafts, the skeptic's verdict
determines whether the draft is promoted unchanged (CONFIRMED-REAL) or
revised (WEAKENED) before becoming the final treatment output fed to
Run 3. All 16 skeptic verdicts and reasoning are in the session
transcript; this file records the Response Matrix outcome for each.

## Promoted unchanged (CONFIRMED-REAL, 9 of 16)

001, 002, 003, 005, 006, 007, 008, 009, 010 — all survived 3
independent falsification attempts each. Several skeptics noted minor
style/scoping tightenings (e.g. 001's look-elsewhere paragraph could
cite an independent supporting fact the skeptic found; 007 could add a
V_ctrl-selection caveat) — none change the verdict or the substance of
the DRAFT CLAIM already recorded in the transcript, so the original
draft claim stands as the final treatment output for these 9 tasks.

## Revised per skeptic findings (WEAKENED, 7 of 16)

### task_004 — significant revision
Skeptic's strongest point: the "44,600x" and "8x SSR rise" findings
come from noiseless synthetic data and were never checked against a
realistic noise floor; separately, the SSR~2.3 magnitude objection
(point D) more likely indicates a *normalized/weighted* residual metric
consistent with the original report's own methodology than it does a
fabricated number. **Final claim:** "The report's own methodology
cannot support its 'dEa is unidentifiable' conclusion, but neither can
a confident rejection of it: `p` is bounded to a ±2% window around its
literature default, which is either a genuine methodological error (too
narrow to let a real compensation effect show) or an appropriate window
under an unstated re-parameterization — this can't be resolved without
the real `rate_data.npy`, the actual noise floor, and an explicit
statement of what SSR metric (raw vs. weighted) was used. The one clean,
verifiable defect is procedural: no artifact provenance is given for
`rate_data.npy` (Gate 1 failure), and the sweep never reports the
fitted `p*` alongside SSR, which would make boundary-clamping visible
either way. Verdict: NEEDS-REAL-DATA, not REJECT — the claim as
submitted is unverifiable, not falsified."

### task_011 — moderate revision
Skeptic corrections: WACC-range NPV low end is $3.8M not $5M (widens
the case, doesn't weaken it); "does not test 3.65%-4.65% at all" is
overstated (83% of the band overlaps, and every rate in both the
narrated and actual band still gives NPV>$8M — the code/text mismatch
is a reproducibility bug, not an outcome-changing one); "confirms the
$9.2M headline" glosses over not knowing whether the print statement
ran before or after the rate reassignment. **Final claim:** "The report
does not justify discounting a risky private project's cash flows at
the risk-free rate; the breakeven rate is 6.13%, and any realistic
project cost of capital (8-15% WACC) drops NPV to $3.8M-$7.0M, well
below the $8M threshold — this is the load-bearing defect, sufficient
on its own to reject the approval conclusion. Separately (a lower-
severity, procedural finding): `RISK_FREE_RATE` is reassigned from
4.15% to 3.98% before the sensitivity loop runs, so the code does not
literally test the narrated 3.65%-4.65% band (it tests 3.48%-4.48%) —
though every rate in both bands still clears $8M, so this specific
mismatch does not itself change the pass/fail outcome, only the
report's internal reproducibility. Verdict: REJECT the approval
conclusion on the discount-rate-methodology ground; the sensitivity-band
mismatch is a real but secondary defect."

### task_017 — minor revision
Skeptic corrections: "no positive control anywhere in the report" is an
unverifiable universal negative from the task summary alone; closing
sentence overclaims scope. **Final claim:** unchanged core (tautology
demonstrated via 9 injected bugs, all passing), with the closing
sentence narrowed to: "the g_hat=0 test cannot distinguish a correct
implementation of the new coupling term from a broken one of the same
g_hat-multiplicative form — no positive control at nonzero g_hat is
disclosed alongside this test, so the claim 'we can now trust the
modified equations' behavior at g_hat != 0' is not supported by the
evidence given."

### task_023 — minor revision
Skeptic correction: the specific "target leakage" mechanism label is
somewhat circular (the synthetic replication assumed `churned` is
defined by `cancellation_date` presence, matching what it then "found")
— but the top-line reject conclusion survives via multiple independent
paths (leakage, tautological label, or degenerate task all kill
"deployable predictor" equally). **Final claim:** "F1=1.000 is
inconsistent with a genuine predictive task on account-behavior
features. `is_active` and `days_since_cancellation` are both provably
functions of the cancellation event itself; under the standard
assumption that `churned` is defined by that same event, this is direct
target leakage — verified by synthetic replication (F1 collapses to
0.168 when the two features are removed, to 0.118 under label-
shuffling). Under an alternative label definition the mechanism label
would change, but 'deployable predictor' fails either way: exact
F1=1.000 on a real-world task is only explained by leakage, a
tautological label, or a degenerate test set — none of which supports
deployment. Verdict: REJECT."

### task_027 — moderate revision, relabeled
Skeptic correction: the draft's own recomputed CI used z=1.96 instead
of the correct t-quantile (should be [-0.81, 2.01], not [-0.77, 1.97]);
"cannot be run" overstated (undefined loader ≠ proven broken); most
importantly, skeptic did the rescue-path analysis and found the
paired-20-store reading is itself ruled OUT by the reported p-value
(would give p≈0.006 at df=19, not the reported 0.003) — strengthening,
not weakening, the case that the report's numbers don't cohere.
**Final claim (relabeled per skeptic's own suggested vocabulary):**
"Recomputing the pooled two-sample t-test directly from the report's
own stated means/SDs/n (8.1/2.3/20 vs 8.7/2.1/20) gives t=0.86, p=0.39,
95% CI=[-0.81, 2.01] (correct t-quantile) — not the reported t=3.12,
p=0.003, CI=[0.21, 0.99]. The gap is too large for rounding (SE off by
~3.6x). A paired-by-store reading doesn't rescue it either: at df=19,
t=3.12 implies p≈0.006, not the reported 0.003 — so no simple
re-interpretation of the design reconciles the numbers. The most likely
explanations are (a) the significance test was actually run at the
transaction level, not the 20-store randomization unit (pseudo-
replication), or (b) the printed 'SD' values are per-transaction
dispersion mislabeled as per-store SD. The supporting script cannot be
independently run (undefined `load_store_baskets`). Verdict: NEEDS-
REAL-DATA — the report's own summary statistics and its own inferential
statistics cannot both be correct; resolving which is wrong requires
the raw per-store data."

### task_028 — moderate revision
Skeptic corrections: the "97.2% sibling overlap" figure is conditional
on an unverified k=4-photos-per-unit assumption, presented too much
like a measurement; label-shuffle is actually the WRONG negative
control for group leakage specifically (it would pass even under severe
group leakage, since shuffling breaks the label-group correlation the
same way it breaks any other signal) — group-aware re-split is the
correct test, already named in the second half of the draft but wrongly
paired with label-shuffle in the verdict. **Final claim:** "The report's
'no evidence of data leakage' conclusion only rules out the leakage
mechanisms it actually checked (train-only preprocessing/tuning) — it
does not address group/unit leakage (multiple photos per physical unit
landing on both sides of a plain label-stratified split) or temporal
distribution shift (3 weeks of data shuffled together, no held-out-week
test), both real risks for this exact data-collection pattern that the
report never rules out. IF the dataset has k>=2 photos per physical
unit, a synthetic simulation of the exact split code shows the sibling-
overlap rate is high (~97% at k=4) — but this is conditional on an
unverified assumption, not a measurement of the real dataset. The
correct checks are a GroupShuffleSplit re-split keyed on unit ID (for
group leakage) and a held-out-week evaluation (for temporal shift) —
not a label-shuffle test, which would not detect group leakage at all.
Confusion-matrix arithmetic is internally consistent (565/600=94.17%
≈94.2%). Verdict: the 'no data leakage' claim is unsupported as
broadly stated; narrow it to 'no evidence of preprocessing leakage,
group/temporal leakage untested' pending the two re-splits above."

### task_032 — moderate revision
Skeptic correction: the specific "silently ~22% lower" downstream-impact
number was measured on a proxy "standard peak detector" (scipy
find_peaks), not the actual (unseen) production `estimate_heart_rate` —
this substitution is exactly the kind of unverified provenance transfer
the project's own Gate 1 discipline flags. The architectural finding
(residual NaN reaches the estimator) stands on its own regardless of
what the estimator does with it. **Final claim:** "The quality gate
(total-NaN fraction <=20%) and the interpolation step (single-run
length <0.5s) enforce two independent thresholds, so there exists a
class of inputs — a single contiguous dropout longer than 0.5s but
still under the 20% total-NaN cap — for which neither threshold
excludes or repairs the strip, and unhandled NaN samples reach the
heart-rate estimator. This was confirmed by direct execution against
the two threshold functions as described (a 6-second contiguous dropout
in a 30-second strip passes the quality gate with 1500 NaN samples
still unresolved after interpolation). What happens next depends on the
actual (unseen) `estimate_heart_rate` implementation — a proxy peak
detector run against the residual-NaN signal produced a silently biased
result with no error or warning, illustrating a plausible failure mode,
but this was not measured against the pipeline's own actual estimator
and should not be quoted as its behavior. Verdict: the claim that the
pipeline 'explicitly detects and handles both cases' is not supported —
there is a structurally unhandled third case — but the downstream
numeric impact on the reported 71.4 bpm figure is unverified, not
established, pending a test against the actual `estimate_heart_rate`
function."

## Baseline-arm outputs

Unchanged — the 16 baseline outputs from Run 2's first phase are used
as-is for Run 3 (baseline is single-pass by design, no skeptic
sub-call, per Phase C).
