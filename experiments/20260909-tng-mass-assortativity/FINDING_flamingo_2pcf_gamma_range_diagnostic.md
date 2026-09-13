# FINDING — gamma mismatch is PARTIALLY (not substantially) a
# fit-range artifact: real curvature confirmed, but a ~0.5-unit
# residual gap remains against the physically-correct literature
# comparison

**Date:** 2026-09-13
**Claim tested:** `CLAIM_flamingo_2pcf_gamma_range_diagnostic.md`
**Script:** `flamingo_2pcf_gamma_range_diagnostic.py`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (deterministic re-fit of already-recorded xi(r) values, no
## new FLAMINGO download)

```
=== Local log-log slope gamma_local, N=5000 ===
r=5.6-7.0:0.094  r=7.0-8.8:0.236  r=8.8-11.1:2.099  r=11.1-13.9:1.322
r=13.9-17.4:2.061  r=17.4-21.8:2.744  r=21.8-27.4:1.485  r=27.4-34.4:2.900
r=34.4-43.1:1.289  r=43.1-54.1:3.559  r=54.1-67.8:1.679  r=67.8-85.1:3.122
r=85.1-106.8:5.972  r=106.8-133.9:-3.000

=== Refits over alternative r-ranges ===
N=200:  full=2.616  [5,30]=2.190  [10,50]=2.188  [30,150]=2.945
N=1000: full=2.227  [5,30]=1.339  [10,50]=1.634  [30,150]=3.122
N=5000: full=2.118  [5,30]=1.553  [10,50]=2.072  [30,150]=2.553

Literature: richer r0=20.7 h^-1 Mpc gamma=1.6; poorer r0=9.7 h^-1 Mpc gamma=2.0
```

## Independent re-verification (before dispatching the skeptic)

Checked whether the local-slope values show a real trend or pure
noise: Pearson correlation of all 14 values against `log(r)` is weak
(`r=0.18`), but this is dominated by the last bin (`r=106.8-133.9`,
`gamma_local=-3.000`), which comes from two tiny, noise-level `xi`
values (`0.0102 -> 0.0201`). Excluding that one bin, the correlation
strengthens to `r=0.74` (n=13), and split-half means show a clear
increasing trend (`1.43 -> 2.86`, first 7 vs. last 6 pairs).

## Independent skeptic review (Step 8a, context-blind — claim + code +
## raw output ONLY, no reasoning chain)

**Verdict: WEAKENED.**

(a) **Range choice — defensible, but the COMPARATOR is soft.** The
`[10,50]` range's a priori motivation (near the literature's own `r0`
scale) is sound and stated before seeing results — not post-hoc range
cherry-picking. But: FLAMINGO's `M500c`-selected, high-mass sample is
the physical analog of Basilakos & Plionis's RICHER subsample
(`gamma=1.6`), not the poorer one (`gamma=2.0`). The best-powered
result (`N=5000`, `[10,50]`, `gamma=2.072`) matches the WRONG
subsample — against the physically-correct target (`1.6`), a `~0.5`
gap remains.

(b) **Local-slope trend is real (confirmed independently, `r=0.74`
excluding one noise-dominated bin) but may be the wrong physics.** The
trend shows `xi(r)` steepening at LARGE `r` (expected behavior near
any correlation function's transition past `r0` — not FLAMINGO-
specific). It does NOT show a genuine shallow POWER LAW at small `r`
matching `gamma=1.6`: the smallest bins (`r=5.6-8.8`) are nearly FLAT
(`xi=6.69, 6.55, 6.20` — barely changing), a plateau, not a `gamma=1.6`
power law. Averaging a flat plateau into a fit pulls `gamma` down
mechanically, which is a different phenomenon from matching the
literature's own power-law shape.

(c) **`N=200`'s `[5,30]` range is DEGENERATE with `[10,50]`, not an
independent small-r test.** `xi(200)` is undefined (`dd<3`) at bins
1-3 and 5, so `[5,30]` for `N=200` actually samples `r~11-27` Mpc —
the same effective bins as `[10,50]`. This is why the two values are
nearly identical (`2.190` vs. `2.188`) — not confirmation of a trend,
a data-sparsity artifact. The "3 of 3 N confirm the trend" framing is
really "2 of 3, plus one case that could not test it."

(d) **Precision overclaim.** `gamma=2.072` from `7` bins with no
reported fit uncertainty, quoted to 3 decimals, implies more precision
than a 7-point log-log fit with `1-2`-unit bin-to-bin scatter (per the
local-slope values) can support. A realistic uncertainty is `~±0.3`.
`N=200`'s `[5,30]` fit (`4` bins, the fit minimum) is qualitative only.

(e) **Overall conclusion overclaims.** "Substantially resolved" is
stronger than what the numbers license. The skeptic's own precisely-
scoped rewrite (adopted below): fit range is A real contributor
(reduces the gap `~30-50%` at `N=1000`/`N=5000`), curvature is real
and independently confirmed, but a `~0.5`-unit residual gap remains
against the physically-correct comparison, and the four other
disclosed confounds (selection function, redshift, cluster-definition,
estimator differences) — each individually capable of `±0.2-0.5` shift
— remain unaddressed and could plausibly account for the residual.

## Response to skeptic (per Step 8a Response Matrix)

- **(a) Accepted, corrected** — the comparison is now made against the
  physically-appropriate RICHER subsample (`gamma=1.6`), not whichever
  literature value happened to be numerically closest.
- **(b) Accepted, precision added** — the trend is real (independently
  re-confirmed, `r=0.74`) but its physical interpretation is narrowed:
  curvature past `r0`, not a shallow small-`r` power law matching
  `1.6`.
- **(c) Accepted, retracted** — `N=200`'s `[5,30]` is no longer counted
  as an independent confirmation; the pattern is `2` of `3` testable
  `N`, with `N=200` unable to test it at all.
- **(d) Accepted** — all range-restricted `gamma` values are now
  reported with an explicit `~±0.3` qualitative-precision caveat.
- **(e) Accepted, conclusion downgraded** — see "What this DOES
  establish" below, using the skeptic's own suggested wording as the
  base.

## What this DOES establish

- The fit range IS a real, replicated contributor to the previously-
  flagged `gamma` mismatch: restricting to `[10,50]` Mpc reduces
  `gamma` by `~0.5-0.9` units at the two best-powered samples (`N=1000`,
  `N=5000`), and the underlying `xi(r)` shows genuine curvature
  (steepening past `r0`), independently confirmed via the local-slope
  trend.
- This PARTIALLY, not fully, accounts for the mismatch: even at the
  best-powered, range-restricted fit, a `~0.5`-unit gap remains against
  the physically-correct literature comparison (FLAMINGO's mass-
  selected sample corresponds to the RICHER Basilakos & Plionis
  subsample, `gamma=1.6`, not the poorer one).
- The residual `~0.5` gap is consistent in size with what the four
  still-disclosed, still-unaddressed confounds (selection function,
  redshift, cluster-definition mismatch, estimator differences) could
  plausibly account for — this diagnostic narrows, but does not close,
  the shape-mismatch question.

## What this does NOT establish

- **Does NOT** show the gamma mismatch is "resolved" — a genuine,
  quantified residual gap remains even under the most favorable
  (range-corrected, correct-subsample) comparison.
- **Does NOT** resolve the four other confounds named in the prior
  FINDING — closing those would require real observational data
  (redshift-dependent catalogs, matched selection functions), outside
  this branch's own FLAMINGO-based toolkit.
- **Does NOT** change the `r0` order-of-magnitude conclusion (already
  established, unaffected by this diagnostic).
- **Does NOT** affect the separate mass-assortativity `rho(r)` null
  result (`FINDING_flamingo_mark_correlation_rho_of_r.md`) — that
  conclusion stands independently of this spatial-clustering-shape
  question.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Status

Closing diagnostic for `docs/162` item 9's residual `gamma`-mismatch
caveat. Real, partial progress: fit range explains roughly a third to
half of the originally-flagged gap, with genuine curvature independently
confirmed — but a real `~0.5`-unit residual remains against the
correct literature comparison, and further narrowing it is outside
this branch's own available tools (would require real observational
cluster data, not simulation-only methods). This is the honest
stopping point for this sub-question within this branch's own toolkit.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
