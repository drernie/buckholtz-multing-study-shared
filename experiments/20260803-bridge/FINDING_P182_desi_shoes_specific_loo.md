# FINDING P182 — trying low-z vs high-z again using the leave-one-out
# results, per the user's direct request — a genuinely confounded null

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (evaluation of a specific test design
using data already computed in `FINDING_P179` — not a new physics
claim)
**Continues/answers:** `FINDING_P179`'s own unresolved question
("`FINDING_P177`'s original open question... remains UNRESOLVED — only
the reliability of the ordering itself changed, not its physical
meaning") and the user's direct request to try low-z vs high-z again
using the leave-one-out results specifically.
**Script:** `P182_desi_shoes_specific_loo.py` (numpy/scipy, 4 tests,
ruff clean, project test suite still passes).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** the leave-one-out numbers themselves are
> correct (reproduce `FINDING_P179` exactly) and the new DESI/SHOES
> decomposition is computed correctly. The first draft's
> INTERPRETATION is RETRACTED IN FULL — see Correction.
> **Ontological/mechanistic interpretation status:** UNCHANGED from
> `FINDING_P177`/`P179` — genuine correspondence vs. Taylor-truncation
> leverage remains open; this file neither narrows nor resolves it.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing — retraction is total, not a softening)

A skeptic review of the first draft (given the actual code) raised
several attacks, independently checked before accepting.

**Accepted, confirmed by direct check — a fatal confound.** DESI's
measurement uncertainty (`σ=2.8`) is dramatically smaller than every
other high-z point's (`14`–`50.4`, median `~20`) — DESI carries roughly
**50×** the `χ²`-weight (`1/σ²`) of a typical other high-z point. Since
the near-null eigenvector is shaped by the *weighted* residual
structure, dropping DESI is expected to shift it by an outsized amount
purely from removing a disproportionately heavy data point —
completely independent of DESI's redshift. "Furthest from `z=0`" and
"highest `χ²`-weight" are perfectly confounded for this one point in
this dataset; the test's design cannot separate them.

**Accepted — the original prediction was a strawman.** "DESI-drop
should show the LARGEST improvement if Taylor-leverage is real" does
not follow from a properly *diffuse* leverage model (leverage roughly
`∝z³` per point): DESI's marginal leverage over the next-most-extreme
point (`z=1.965`) is only `~1.7×`, not dominant — such a model predicts
mild point-to-point variation among all 8 drops, not a single stark
outlier.

**Checked, not simply accepted — the specific "within 1σ of noise"
claim was itself methodologically questionable, and this was verified
directly rather than taken at face value.** The skeptic's own number
used `FINDING_P179`'s established high-z jackknife std (`0.00035°`) as
the noise floor — but that statistic is computed from *all 8*
leave-one-out values, **including the very DESI-drop value being
tested for being an outlier**, which inflates the reference. Excluding
DESI from its own reference set (comparing only to the other 7 drops'
own spread, jackknife-corrected for `n=7`) gives a much higher apparent
significance (`~3.6σ`) — but that alternative is itself built from only
7 points, whose own std is poorly estimated. **Both numbers are
computed and reported below; the significance is genuinely ambiguous**
(`1.13σ` vs `3.61σ`, depending on a defensible methodological choice),
not resolved by picking whichever number is more convenient.

**Accepted — the first draft used the LOO mean as a full-sample
proxy.** Fixed: the real, non-leave-one-out full-sample angles are now
computed directly and used throughout.

**Accepted — the SHOES sanity check was weak** (only required falling
within `[min,max]` of the other 7 — true for `~75%` of draws from any
common distribution by chance). Strengthened to require closeness to
the mean (`<1σ`) — verified to hold (`0.15σ`).

**Net result: the first draft's headline conclusion ("dropping DESI
argues against DESI-specific Taylor-truncation leverage") does NOT
survive and is retracted in full.** The honest conclusion is that this
specific test design — leave-one-out applied to identify a single
dominant point — cannot discriminate here, for two independent
reasons: an unresolvable weight confound, and an ambiguous
significance estimate.

## 0. Premise — `NO_AUTHOR_ERROR`

This file evaluates a specific test design against TJB's own real data
and functions (reproduced verbatim); it makes no claim about v82's own
theory.

## 1. What was attempted

Using `FINDING_P179`'s already-validated leave-one-out machinery,
explicitly labeled each of the 8 low-z and 8 high-z leave-one-out
drops by the redshift dropped, to test whether dropping DESI (`z=2.33`,
the single most extreme, furthest-from-the-`z=0`-Taylor-expansion-point
data point) specifically drives the previously-established low-z
(`0.0062°`) vs high-z (`0.0195°`) angle gap.

## 2. Results

```
Real full low-z angle:  0.00624 deg
Real full high-z angle: 0.01946 deg

SHOES drop: 0.00625 deg (0.15 sigma from other-7 mean) -- unremarkable, as expected
DESI drop:  0.01985 deg (the max of all 8 high-z LOO values)

DESI chi2-weight vs median other high-z point: ~51x

Significance of DESI's deviation:
  excluding DESI from its own reference (n=7, jackknife-corrected): 3.61 sigma
  including DESI in the reference (FINDING_P179's own jackknife std): 1.13 sigma
```

## 3. Verdict

**RETRACTED**: dropping DESI does not provide usable evidence against
(or for) the DESI-specific Taylor-truncation-leverage hypothesis. Two
independent, fatal problems:

1. DESI's much smaller measurement uncertainty gives it outsized
   `χ²`-weight, fully confounded with its redshift distance — this test
   cannot tell "DESI matters because it's far from `z=0`" apart from
   "DESI matters because it's precisely measured."
2. The statistical significance of DESI's own leave-one-out deviation
   is itself ambiguous (`1.13σ` to `3.61σ`) depending on a defensible
   methodological choice of reference statistic.

**SUPPORTED (symmetric check)**: SHOES's already-known zero
contribution is correctly reproduced by this stricter test (`0.15σ`
from the mean) — an internal consistency check on the method, not new
physics.

`FINDING_P177`'s original open question (genuine correspondence vs.
Taylor-truncation leverage) remains **exactly as unresolved** as
`FINDING_P179` left it. This file neither narrows nor resolves it.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not resolve `FINDING_P177`'s open question** — the attempted
   resolution failed for the two structural reasons in the Correction.
3. **Does not rule out DESI-specific leverage, nor confirm it** — the
   confound and the significance ambiguity both point the same
   direction: inconclusive, not "argues against."
4. **A properly-controlled version of this test remains undone.** It
   would need, at minimum: a re-weighted rerun with DESI's uncertainty
   homogenized to the other high-z points' scale (to separate the
   weight confound from the redshift-distance effect), and a
   pre-registered, non-circular significance test (e.g. against an
   independently-simulated null, not a same-dataset jackknife std).
5. **Does not test the diffuse (whole-range, not single-point) form of
   the Taylor-truncation-leverage hypothesis** — a `z³`-regression
   across all 8 high-z drops, as the skeptic proposed, was not run
   here.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
