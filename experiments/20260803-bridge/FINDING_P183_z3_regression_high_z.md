# FINDING P183 — z³-regression across all 8 high-z leave-one-out
# points, per the user's direct request — same confound, stronger null

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (statistical evaluation of a specific
test design — not a new physics claim)
**Continues/answers:** `FINDING_P182`'s own skeptic's Attack 2, which
proposed this exact test as the properly-framed ("diffuse," not
single-point) version of the Taylor-truncation-leverage discriminator,
and the user's direct request to run it.
**Script:** `P183_z3_regression_high_z.py` (numpy/scipy, 4 tests, ruff
clean, project test suite still passes).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** the regression numbers themselves are
> correct and reproducible. The first draft's INTERPRETATION
> ("leverage-point artifact, therefore no diffuse leverage, question
> stays neutral") is corrected — see Correction.
> **Ontological/mechanistic interpretation status:** UNCHANGED from
> `FINDING_P177`/`P179`/`P182` — genuine correspondence vs.
> Taylor-truncation leverage remains open.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing)

**Process note:** the skeptic dispatch for this file's first draft
again omitted the actual source code (a repeat of `FINDING_P180`'s
mistake). The skeptic explicitly flagged this and produced a
substantively correct statistical critique anyway; its 4 hypothesized
code-level bugs were checked directly against the real source and
**refuted** (LOO index alignment correct; `v_null`'s sign ambiguity
resolved by the established rescale-to-`eps=1` convention, not a
missing `abs()`; eigenvector selection is `eigh`'s standard
ascending-order convention, validated throughout `P177`–`P182`; `V_PRED`
is a fixed constant, never recomputed inside the loop).

**Accepted — presenting the regression p-values as formal statistical
significance was overreaching.** The 8 leave-one-out angles are **not**
independent samples — each shares 6 of 7 underlying points with every
other one — so the iid assumption behind `linregress`/`spearmanr`'s
p-values does not hold. Retained as descriptive comparisons only.

**Accepted — "signal disappears without DESI, therefore it was an
artifact" over-interpreted non-significance as absence-of-effect** at
`n=7`, where power to detect a modest real slope is essentially zero.

**Accepted — a previously-unconsidered confound.** Excluding DESI
doesn't just remove one point — it roughly **halves the x-range**
(`z³`) of the remaining 7 points (`12.65`→max `7.59`), independently
collapsing the regression's power to detect *any* slope. "Signal
disappears without DESI" is consistent with either "DESI was the whole
signal" **or** "the test became underpowered regardless" — not
distinguished here.

**Accepted, independently verified before accepting — a genuine sign
mismatch.** This file's own stated mechanistic prediction (diffuse
Taylor-truncation leverage) is a **negative** slope (dropping a
high-`z³` point should improve the match). The observed slope is
**positive** in both regressions (`+3.095×10⁻⁵` full, `+3.210×10⁻⁶`
excluding DESI) — checked directly against the printed numbers, not
simply taken on the skeptic's word. This is **weak evidence AGAINST**
the mechanism, not neutral (weak because of the non-independence and
low-power issues above, not because the sign doesn't matter).

**Accepted — `z³` is one unverified functional form** among several
equally plausible ones (`(1+z)³`, `ln(1+z)`, comoving distance); not
compared here.

**Accepted, restated explicitly — the same core confound `FINDING_P182`
already established also contaminates this regression.** DESI's `~50×`
`χ²`-weight means removing it removes both the largest-`z³` point *and*
the dominant weight-constraint simultaneously; this test cannot
separate a `z³`-driven mechanism from a weight-driven one any better
than `P182`'s single-point comparison could.

**Net result:** the first draft's "regression leverage-point artifact,
therefore no diffuse leverage, question stays neutral" is corrected to
a **stronger, more precise null**: this test structurally cannot
discriminate genuine diffuse Taylor-truncation leverage from DESI's
simultaneous weight-and-range dominance, and — independently of that —
the observed effect's sign points *away from*, not toward, the very
mechanism it was designed to detect.

## 0. Premise — `NO_AUTHOR_ERROR`

This file evaluates a specific statistical test design against TJB's
own real data and functions (reproduced verbatim); it makes no claim
about v82's own theory.

## 1. What was attempted

Regressed the 8 real high-z leave-one-out angles (`FINDING_P179`/`P182`)
against `(z_dropped)³`, following the skeptic's own proposed
"diffuse-leverage" test design.

## 2. Results

```
FULL (8 points):     slope=+3.095e-05  r^2=0.6873  naive-p=0.0109
EXCLUDING DESI (7):   slope=+3.210e-06  r^2=0.0229  naive-p=0.7462
Spearman (all 8):     rho=0.3810        naive-p=0.3518

Mechanism-predicted slope sign: NEGATIVE
Observed slope sign (both regressions): POSITIVE
```

## 3. Verdict

**RETRACTED (framing)**: "regression leverage-point artifact, no
diffuse leverage, neutral" — replaced with the stronger, correctly
qualified null below.

**Established**: this `z³`-regression test cannot discriminate genuine
diffuse Taylor-truncation leverage from DESI's simultaneous weight-and-
range dominance (structural confound, same root cause as `FINDING_P182`).
Independently, the observed slope's sign is opposite the mechanism's
own prediction — weak evidence against the `z³`-diffuse form
specifically, not a neutral non-result, though weak given non-
independence of the LOO angles and `n=7`–`8`.

`FINDING_P177`'s open question (genuine correspondence vs.
Taylor-truncation leverage) remains **completely unresolved** by this
file, as by every prior file in the `P175`–`P183` thread.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not resolve `FINDING_P177`'s open question.**
3. **No formal statistical significance is claimed** for any p-value
   here — the 8 LOO angles are not independent samples.
4. **Does not test alternative functional forms** (`(1+z)³`,
   `ln(1+z)`, comoving distance) that could show a different pattern.
5. **Does not break the DESI weight/range/redshift confound** — the
   only way to do that (per `FINDING_P182`'s own "does NOT establish")
   is a re-weighted rerun with DESI's uncertainty homogenized to the
   other high-z points' scale; not attempted here.
6. **Does not establish the sign mismatch is decisive** — it is
   reported as weak evidence, explicitly qualified by the sample-size
   and independence limitations above, not as a refutation.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
