# FINDING E17 ADDENDUM 3 — sigma-sensitivity IS material (MCID confirmed
# on a defensible bracket, not just the extreme endpoint); the exclusion-
# fraction confound is NOT material (confirmed against seed noise), but
# getting there required a genuine numerical self-correction along the way

**Date:** 2026-09-06
**Continues:** `FINDING_E17_ADDENDUM2`'s own two explicitly-open caveats
— (a) no `σ`-sensitivity sweep on the scatter WIDTH kept from Duffy+2008
after the MEDIAN was swapped to Correa Paper III; (b) the exclusion-
fraction change (`5.65%→1.02%`) not decomposed from the pure median-
swap effect. Explicit go-ahead given ("E17's σ-sweep и exclusion-fraction
decomposition").

## L0 (EstimandOps)

**Descriptive.** Two independent sub-questions: (a) is `Addendum 2`'s
own `~1.82×` divergence headline robust to the `σ(log10 c)` scatter-
width choice? (b) does the differential exclusion rate between the two
concentration sources (not the median choice itself) drive part of the
reported `~5×→~1.8×` shrinkage?

## Real, disclosed self-correction during execution (not silent)

The original Part (b) design compared "exclude" (drop unphysical
`z_{-2}<0` draws) against "clip" (floor `z_{-2}` at the physical boundary,
keep the draw). Running it found a genuine mathematical singularity:
Correa's own `alpha` formula has `np.log(1.0+z_{-2})` in a denominator
that vanishes exactly at `z_{-2}=0`; even clipping to a tiny positive
epsilon (`1e-6`) left `alpha` finite-but-enormous, which overflowed in
`mass_history_ratio`'s own `(1+z)**alpha` — confirmed by actually running
both variants and observing `NaN` either way. This is not a coding bug;
it is a real feature of the source MAH-model parametrization at its own
boundary. **Replaced** with a numerically sound alternative: since
`formation_redshift(c)` is monotonic in `c` (verified, PC2), "exclude
`z_{-2}<0`" is mechanically equivalent to "exclude the lowest-c
percentile" at a source's own natural rate — letting each source be
re-evaluated at a *different* percentile-truncation aggressiveness.

## Step 8a skeptic — context-blind, claim + full code + printed output —
## verdict: WEAKENED, 4 real points, all fixed in place

1. **Sweep's own `σ=0.05` bottom endpoint is not a physically defensible
   population scatter** (a factor of `3` below Duffy's own `0.15`); the
   original "`63.0%` max shift" headline leaned on it. **Fixed:** the
   MCID already fires on a defensible, symmetric `±0.05` dex bracket
   around Duffy's value (`σ∈{0.10,0.20}`) — `29.8%`/`21.4%` at `z=2.33`
   — so the MATERIAL verdict does not depend on the extreme endpoint.
   The `63%` figure is kept only as an explicitly-labelled secondary
   number.
2. **Part (b)'s "forced to the other source's rate" framing overclaimed
   what percentile truncation at a different rate actually equalises.**
   Traced by hand: forcing Correa-III to Duffy's `5.60%` percentile
   removes its own `1.02%` physical tail *plus* `~4.58` percentage
   points of otherwise-valid draws; forcing Duffy to Correa-III's
   `1.02%` percentile leaves `~4.63` percentage points still caught by
   the physical cut afterward. **Neither forced row actually equalises
   both sides' effective truncation** — in each row, one side stays
   close to its own natural rate. **Fixed:** relabelled throughout to
   describe what is actually varied (lower-c-tail percentile-cut
   aggressiveness), not "matched exclusion rate." The underlying
   conclusion (divergence is insensitive to this) still holds — it
   answers the original caveat via a different, still-valid route.
3. **No seed-variance check existed** for Part (b)'s tiny reported
   shifts (`0.0%`/`0.1%`) — indistinguishable from Monte Carlo noise
   without one. **Fixed:** reran across 5 independent seeds; noise
   ceiling `0.08%`, an order of magnitude below the MCID threshold —
   confirms the near-zero shift is real, not noise.
4. **Only `z=2.33` was checked**, not `z=2.00` (`Addendum 2`'s own MCID
   checked both). **Fixed:** `z=2.00` added to the sweep — MCID
   confirmed MATERIAL there too (`22.9%` on the defensible bracket).

**No point dismissed.** All 4 addressed in the code, the printed output,
and `CLAIM_E17`'s own Addendum 3 section — per this project's no-silent-
correction discipline.

## Result

**Part (a): MATERIAL.** `σ(log10 c)` choice is a real, non-negligible
driver of the divergence headline — `29.8%`/`22.9%` shift at `z=2.33`/
`z=2.00` on a defensible `±0.05` dex bracket alone (full-range: up to
`63.0%`/`45.8%`). `SOURCE_NOT_FOUND` for a superior real replacement
value for `σ` itself (Dutton & Macciò 2014's own abstract quotes only a
`0.2` dex Einasto *shape*-parameter scatter, a different quantity) — the
result stays a sensitivity bound, not a corrected point estimate.

**Part (b): not material.** The `Duffy→Correa-III` divergence shrinkage
(`1.401×`) is stable to `<0.1%` — well inside the `0.08%` seed-noise
ceiling — whether or not the lower-c tail is percentile-cut more or less
aggressively. The reported `~5×→~1.8×` headline shrinkage from
`Addendum 2` is confirmed **not** a truncation-rate artefact.

## What this does and does NOT establish

**Does establish:** `Addendum 2`'s own divergence headline is real but
`σ`-sensitive — a stated range, not a single trustworthy point estimate,
is the honest summary; the exclusion-fraction confound named in
`Addendum 2`'s own caveat (b) is genuinely closed.

**Does NOT establish:**
1. A single "corrected" divergence number — Part (a)'s own result is
   that no single number is robust; reporting a range (`~1.0×` to `~3×`
   depending on `σ` choice, at `z=2.33`) is the honest output.
2. That `σ=0.15` (Duffy's own value, kept by default) is the *correct*
   choice for a cluster-calibrated concentration source — only that no
   better real value was found in a bounded search.
3. `NO_AUTHOR_ERROR` — a sensitivity/robustness check on this project's
   own reconstruction, not a claim about v82's or Correa's correctness.

## Pearl Registry

The `σ`-choice sensitivity (Part a) is itself a real, disclosed limit on
how far the `E17`/`Addendum 2` line's numbers can be trusted as point
estimates — worth a Pearl Registry row naming the open need (a real,
cluster-scale-specific `σ(log10 c)` value, not found in this session's
bounded search) as a concrete, checkable follow-up if this thread is
ever revisited.
