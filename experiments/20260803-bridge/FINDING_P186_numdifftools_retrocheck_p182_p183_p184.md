# FINDING P186 — numdifftools retrocheck of P182/P183/P184's core LOO
# claims: all survive, with a real recomposition gap found and fixed

**Date:** 2026-09-01
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (numerical-robustness retrocheck of
prior findings — not a new physics claim)
**Continues/answers:** sci-code-audit's Layer 4 finding (boyko-project-
radar, 2026-09-01): `numdifftools` was introduced and validated in
`FINDING_P185`, but only applied there to P185's OWN Set A/Set B
leave-one-out angles — never retroactively to `FINDING_P182`/`P183`/
`P184`'s own claims, which still rested on the fixed-step (h1=1e-5)
convention P185 itself showed can be numerically fragile for
leave-one-out subset constructions. Pearled the same day
(`pearl_registry/INDEX.md`) with an explicit falsifiable prediction.
**Script:** `P186_numdifftools_retrocheck_p182_p183_p184.py` (numpy/
scipy/numdifftools, 6 tests, ruff clean, project test suite still
passes — 881 in `tests/` + 6 in this file + 47 across P177-P185).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** all three retrochecked claims (rank,
> sign, magnitude) confirmed correct under the adaptive Hessian, with
> two genuine numerical caveats identified and documented (see
> Correction and §2).
> **Ontological/mechanistic interpretation status:** UNCHANGED —
> `FINDING_P177`'s central question is untouched by this file.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-09-01, context-asymmetric skeptic-caught, applied
before finalizing — code verified present in the dispatch)

A skeptic review of the first draft found one real, significant gap
(a Recomposition Gate violation, FL Step 8a) and confirmed one genuine
numerical caveat; a second hypothesized caveat was checked directly
and refuted.

**CONFIRMED, FIXED — Recomposition Gate violation.** The first draft's
conclusion claimed "agreement held to well within the ~0.5-1% tolerance
P185 established," but the code only tested RANK (`desi_angle ==
max(...)`) and SIGN (`slope > 0`) — never a quantitative per-point
comparison against the original fixed-step LOO angles. A claim about
*magnitude* was resting on tests that only checked *ordering*. Fixed:
added `test_quantitative_agreement_with_fixed_step`, which imports
`P182`'s own fixed-step function directly (not hardcoded numbers, so
it can't drift from the source) and compares point-by-point at the
clean step=1e-4 configuration. Result: max relative difference
**0.768%** (at z=1.037), all 8 points within 0.38-0.77% — genuinely
inside the informally-stated tolerance band, now actually checked in
code, not merely asserted in prose.

**CONFIRMED, FLAGGED — `step=None` internal contamination.** Checked
whether numdifftools' fully-adaptive step-size search ever evaluates
`chi2_eps_indices` at a point triggering the `H2<=0` safety-penalty
return (1e12), which would silently contaminate that configuration's
Hessian. Directly instrumented and counted: `step=None` triggers this
512 times across the 8 LOO subsets; the two FIXED step configs (1e-4,
1e-3) trigger it **zero** times. The qualitative conclusions held even
at `step=None` despite this, but `step=None`'s results are flagged as
the least trustworthy of the three — the two clean, fixed-step configs
are this file's primary evidence, not `step=None`.

**REFUTED BY DIRECT CHECK — eigenvector-selection ambiguity.** The
skeptic's strongest hypothesis: `eigvecs[:, 0]` (ascending order)
might silently select a saddle-point direction instead of the true
near-null direction, since the near-null eigenvalue occasionally comes
out numerically *negative* (order 1e-7 to 1e-9). Checked directly
across every LOO subset, both weightings, all 3 step configs: the
near-null eigenvalue is always separated from the second-smallest by
6-8 orders of magnitude (ratio always < 1e-6) — the sign flicker is
real floating-point noise around a true near-zero value, but the
eigenvector selection is never ambiguous.

**ACCEPTED, MINOR** — the positive-control assertion used a 2%
tolerance while the docstring cited "~1%." Tightened to 1.5% (observed
value 0.7%, comfortably inside either bound) so assertion and prose
agree.

## 0. Premise — `NO_AUTHOR_ERROR`

This file evaluates the numerical robustness of this project's own
prior reconstructions (`P182`/`P183`/`P184`); it makes no claim about
v82's own theory.

## 1. What was attempted

Recomputed `P182`/`P183`/`P184`'s core leave-one-out claims — all
built on the same Set A (7 real cosmic-chronometer points, z=1.037-
1.965, plus DESI at z=2.33) — using `numdifftools.Hessian` (adaptive
Richardson extrapolation) instead of the fixed-step (h1=1e-5) central-
difference Hessian all three originally used:

- **P182** — is DESI's leave-one-out drop the largest among all 8?
- **P183** — does the z³-regression slope (LOO angle vs z_dropped³)
  stay POSITIVE, opposing the diffuse-Taylor-leverage mechanism's
  predicted negative sign?
- **P184** — does DESI remain the leave-one-out max after its χ²-weight
  is homogenized to the median of the other 7 sigmas, and under full
  8-point weight equalization?

## 2. Results

```
Positive control: Set A adaptive angle = 0.01932 deg (matches P185) -- PASS

Quantitative agreement (step=1e-4, vs P182's own fixed-step angles):
  max relative difference = 0.768% (at z=1.037), all 8 points 0.38-0.77%

Eigenvalue-selection check: never ambiguous
  max ratio of near-null to second-smallest eigenvalue = 4.99e-07

1e12-penalty contamination by step config:
  step=None: 512 hits (flagged, not primary evidence)
  step=1e-4: 0 hits (clean, primary evidence)
  step=1e-3: 0 hits (clean, primary evidence)

P182 retrocheck -- DESI is max at every config: {None: True, 1e-4: True, 1e-3: True}
P183 retrocheck -- slope stays positive at every config:
  {None: 4.799e-05, 1e-4: 4.809e-05, 1e-3: 4.947e-05}
P184 retrocheck -- DESI is max under homogenization at every config: {None: True, 1e-4: True, 1e-3: True}
P184 retrocheck -- DESI is max under full equalization at every common sigma:
  {20.0: True, 27.57: True, 30.0: True}
```

## 3. Verdict

**SURVIVES, with the recomposition gap fixed**: all three of `P182`/
`P183`/`P184`'s core leave-one-out claims — rank, sign, and now also
magnitude — hold under the adaptive Hessian. The two fixed-step
configurations are the clean, primary evidence; `step=None`'s
agreement is corroborating but flagged as less trustworthy due to
internal penalty contamination. Eigenvector selection was checked and
found never ambiguous.

This closes the verification debt sci-code-audit's Layer 4 flagged and
resolves `pearl_registry`'s own falsifiable prediction (row added
2026-09-01, marked RESOLVED same session) — but only because the first
draft's overclaim was caught and an actual quantitative test was added,
not because the original rank/sign-only tests were sufficient to
support the "tolerance held" wording on their own.

`FINDING_P177`'s central question (genuine correspondence vs.
Taylor-truncation leverage) is **untouched** by this file — this
strengthens confidence in the NUMERICS underlying `P182`/`P183`/`P184`,
it does not narrow or resolve the underlying physics question.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not resolve `FINDING_P177`'s central question.**
3. **Does not validate `step=None` as a trustworthy configuration on
   its own** — it is corroborating only; the two fixed-step configs
   are the primary evidence throughout this project's use of
   `numdifftools` going forward.
4. **Does not check every LOO subset's quantitative agreement** — the
   per-point comparison is against `P182`'s angles specifically (Set
   A, original weights); `P184`'s homogenized/equalized variants were
   checked only by rank (max), not by quantitative magnitude against
   their own fixed-step counterparts.
5. **No formal statistical significance is claimed** for any reported
   distance/ratio — inherits the same non-independent-LOO-samples
   caveat established in `P182`-`P185`.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
