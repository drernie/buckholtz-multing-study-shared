# FINDING P184 — DESI-uncertainty-homogenized rerun, per the user's
# direct request — the weight confound is broken, a new one surfaces

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (evaluation of a specific confound-
breaking test — not a new physics claim)
**Continues/answers:** `FINDING_P182`'s and `FINDING_P183`'s own "what
this does NOT establish" — both explicitly named a
DESI-uncertainty-homogenized rerun as the only way to break the DESI
weight/redshift confound — and the user's direct request to run it.
**Script:** `P184_desi_sigma_homogenized.py` (numpy/scipy, 6 tests
incl. 2 skeptic-requested robustness checks, ruff clean, project test
suite still passes).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** the homogenization and its results are
> correct and robustly reproduced across a sigma sweep and a full
> weight-equalization variant. Wording overreach in the first draft's
> conclusion is corrected — see Correction.
> **Ontological/mechanistic interpretation status:** UNCHANGED from
> `FINDING_P177`/`P182`/`P183` — genuine correspondence vs.
> Taylor-truncation leverage remains open; a NEW, still-unresolved
> confound (measurement type) is identified.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing — this dispatch included the actual source code,
confirmed by the skeptic itself, closing the gap that recurred in
`FINDING_P180`/`P183`)

A skeptic review raised 7 attacks. Two were addressed by running the
exact additional checks it proposed — both **strengthened** the
finding rather than weakening it. The rest are wording/reporting
corrections.

**Addressed, strengthens the finding — a single homogenized-sigma
choice is not a robustness test.** Swept `σ_DESI` across the entire
realistic range spanned by the other 7 high-z points' own real sigmas
(`14.0`–`50.4`) plus their mean. **DESI remains the max of 8
leave-one-out drops at every one of these values.** Only at an
unrealistic `σ=100` (2× the largest real measurement uncertainty in
the whole dataset) does it stop being strictly the max, and even then
by a negligible margin.

**Addressed, strengthens the finding — homogenizing only DESI still
leaves a `3.6×` sigma spread among the other 7, not true equalization.**
Reran with **all 8** high-z sigmas set to an identical common value
(`20.0`, `27.6`, `30.0` tested). **DESI still gives the largest
leave-one-out angle** (`0.01988°` vs next-highest `0.01963°`) at every
value tested — materially stronger evidence than the single-point test
that DESI's outsized influence is not a weight artifact in any form.

**Accepted — the full-8-point angle barely moves** (`0.01946°` →
`0.01950°`, `~0.2%`) under a `~50×` weight cut. Worth stating plainly:
DESI's raw `χ²`-weight was likely never the dominant driver of the
*full-sample* fit geometry — a point's *presence* and its *weight* are
different levers. Does not contradict the leave-one-out results (which
are about presence), but the first draft's "RULES OUT the pure
weight-artifact explanation" was too strong; softened.

**Accepted — the descriptive distance (`5.36`, in units of the other
7's own std) was printed without a live caveat**, despite the
docstring's warning that it isn't a formal significance number (same
issue `FINDING_P183` already flagged for non-independent LOO samples,
here compounded by a small-`n=7`-std estimate). Now caveated inline
wherever printed.

**Accepted — `naive-p` values printed without an inline caveat.**
Fixed: caveat now printed alongside every `naive-p`, not just noted in
prose once.

**Accepted — the sign-persistence test reported only sign, hiding
whether homogenization moved the slope toward zero.** Fixed: both
homogenized and original slope values are now printed together
(`3.095×10⁻⁵` original vs `3.446×10⁻⁵` homogenized — essentially
unchanged, not partially resolved).

**Accepted — "measurement-type confound" was named without a concrete
causal mechanism** for why it would specifically matter to this
geometric quantity. Reworded to state this honestly (an entangled,
unspecified alternative) without dressing it up as a fully specified
hypothesis.

**Net result: the core finding is upgraded, not weakened.** DESI's
outsized leave-one-out influence survives both a realistic sigma sweep
and a full weight-equalization variant — considerably stronger
evidence against "purely a weight artifact" than the single-value test
alone provided. Overreaching language and unflagged significance
numbers are corrected; the `z³`-regression sign-mismatch with the
Taylor-truncation-leverage mechanism persists unchanged under every
weighting scheme tested.

## 0. Premise — `NO_AUTHOR_ERROR`

This file evaluates a specific confound-breaking test against TJB's
own real data and functions (reproduced verbatim); it makes no claim
about v82's own theory.

## 1. What was attempted

Set DESI's measurement uncertainty to match the other high-z points'
scale (single value, a realistic sweep, and full 8-point equalization)
and reran the leave-one-out analysis (`FINDING_P179`/`P182`) and
`z³`-regression (`FINDING_P183`) under each.

## 2. Results

```
Full-8 angle: 0.01946 deg (original weights) -> 0.01950 deg (homogenized)

Leave-one-out with homogenized DESI sigma: DESI STILL the max (0.01985 deg)

Sigma sweep (14.0-50.4, realistic range): DESI remains max at EVERY value
Full weight equalization (all 8 sigmas equal): DESI STILL max (0.01988 deg)

z^3-regression slope: ORIGINAL +3.095e-05 -> HOMOGENIZED +3.446e-05
  (both positive -- mechanism predicts negative -- unchanged by homogenization)
```

## 3. Verdict

**SUPPORTED, upgraded from the single-value test**: DESI's outsized
leave-one-out influence is **not** a weight artifact — robust across a
realistic sigma sweep and full weight equalization.

**UNCHANGED**: the `z³`-regression's sign-mismatch with the diffuse
Taylor-truncation-leverage mechanism (`FINDING_P183`) persists exactly
under homogenized weighting — homogenization did not fix the wrong
sign.

**NEW, UNRESOLVED**: DESI is the only BAO/Lyman-alpha measurement in
an otherwise all-cosmic-chronometer high-z subsample — "furthest in
redshift" and "only point of this measurement type" remain entangled
for this one point, with no concrete mechanism proposed for why
measurement type specifically would matter. This is a genuinely new
confound this file surfaces but cannot resolve.

`FINDING_P177`'s open question (genuine correspondence vs.
Taylor-truncation leverage) remains **unresolved**.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not resolve `FINDING_P177`'s open question.**
3. **Does not identify WHY DESI's influence persists** — only that it
   is not purely weight-driven. Redshift-distance and measurement-type
   remain confounded.
4. **Does not propose a concrete mechanism for the measurement-type
   alternative** — named honestly as unspecified, not a tested
   hypothesis.
5. **Does not attempt to separate redshift from measurement-type** —
   the only way to do that within this dataset would require a second
   BAO/Lyman-alpha-type point at a different redshift, or a second
   cosmic-chronometer point near `z=2.33`, neither of which exists in
   the real 33-point dataset.
6. **No formal statistical significance is claimed** for any reported
   distance/ratio — the LOO angles remain non-independent samples.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
