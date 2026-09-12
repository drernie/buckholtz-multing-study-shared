# FINDING — M500c vs M200c overlap: ratio confirms textbook physics,
# overlap is real but NOT uniform (91-92% for 2 of 3 N, 74% at N=50 —
# a suggestive ~2sigma single-point anomaly, mechanism undiagnosed);
# critically, overlap itself does NOT answer whether prior Pearson r
# results are stable under the mass-definition switch

**Continues:** `CLAIM_flamingo_m500c_m200c_overlap.md` (committed
BEFORE the script ran) → `docs/162_ontology_spec_v82.md` item 3's own
`[OPEN]` flag, replacing a `[MEMORY]`-tier literature estimate with a
real measurement. **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, live `hdfstream` data, FLAMINGO's own SOAP catalog,
## `M200c` and `M500c` for the SAME halos, no cross-catalog matching)

```
Shared pool: N=5000 halos with valid M200c AND M500c
M500c/M200c ratio: mean=0.6759, median=0.6886, SD=0.0715

     N  overlap_count  overlap_frac
    35             32         91.4%
    50             37         74.0%
  1200           1101         91.8%

At N=1200 boundary (ranks 1100-1300): ratio mean=0.6800, SD=0.0665
```

## Independent skeptic review (Step 8a, context-blind) — every
## quantitative claim independently re-derived before use

Poisson swap-count analysis independently reproduced exactly:
`SE` on overlap fraction from `sqrt(swap_count)/N` gives `4.95%` (`N=
35`), `7.21%` (`N=50`), `0.83%` (`N=1200`); the `N=35` vs. `N=50` gap
(`17.4` percentage points) against combined SE (`8.75` pp) gives
`1.99` sigma — confirmed exactly.

1. **Is the ratio distribution plausible (`CONFIRMED-REAL`)?** Median
   `0.689` sits within the standard, widely-cited NFW-profile range
   (`M500c/M200c ~ 0.68-0.72` for typical cluster concentrations,
   `c200~4-6`) — matching to the third decimal. The `10.6%` relative
   scatter (`SD/mean`) is consistent with known concentration-mass
   scatter (`~0.15` dex in `log c`) propagated through the
   `M500c(M200c, c)` relation. `mean < median` (left/low-side tail) —
   physically expected (dynamically disturbed/merging halos give lower
   `M500c/M200c`, `M500c`'s smaller aperture cuts more of the
   unrelaxed outskirts) — a real, not-anomalous signature of genuine
   cluster physics, not measurement noise.
2. **Is the `N=50` dip (`74.0%`, vs. `91.4%`/`91.8%` at the other two
   `N`) a real, mechanism-identified anomaly (`WEAKENED`)?** The gap
   to `N=35` is `~2 sigma` — real enough to be "suggestive," not
   "proven." **The script's own boundary diagnostic was only run for
   `N=1200` (where nothing anomalous was found) — NOT for `N=50`
   (where the anomaly actually is)** — a real, self-caught gap: the
   one place worth diagnosing was not diagnosed. No swap-out halo's
   own rank/ratio-percentile was printed. **Three plausible mechanisms
   remain equally undistinguished by this data**: a real local
   mass-function feature (a cluster of near-tied `M200c` values near
   rank `40-60`), a real local excess of below-average-ratio halos in
   that specific rank range, or `N=50` simply being a `~2 sigma`
   statistical fluctuation among only `3` tested points.
3. **Does `74-92%` overlap answer the actual practical question — does
   the `M200c`-vs-`M500c` mismatch matter for this project's own prior
   Pearson-`r` correlation results (`WEAKENED` — the question is NOT
   directly answered by this test)?** **This is the single most
   important correction from this review.** Overlap measures set
   membership, not statistic stability. The `13` swapped-out halos at
   `N=50` are NOT a random `13` — they are SYSTEMATICALLY the
   lowest-ratio halos in that rank range (that is mechanically why they
   fell below the `M500c` cutoff), and `M500c/M200c` ratio correlates
   with dynamical state/concentration/merger history — exactly the
   kind of physical property that can also correlate with whatever is
   being tested in a mass-assortativity analysis. **A `26%`
   membership swap, systematically biased by a real physical property,
   is NOT the same claim as "Pearson `r` changes by `<26%`" or "Pearson
   `r` is stable."** The honestly-scoped conclusion: `2` of `3` tested
   `N` corroborate the prior `[MEMORY]`-tier `~90-95%` estimate; `N=50`
   does not; and **none of this measures whether any already-reported
   `rho_NN`/`rho_band` number would shift under an actual `M500c`-based
   re-selection** — that requires recomputing the correlation on both
   selections directly, not inferring it from overlap.
4. **Do `3` pre-specified `N` values characterize the overlap-vs-`N`
   relationship (`WEAKENED`/`NEEDS-REAL-DATA`)?** `35`, `50`, `1200`
   are not log-uniformly spaced and, critically, are non-monotonic in
   the observed result — meaning the TRUE shape of overlap-vs-`N`
   between `50` and `1200` (or beyond) is **not characterized** by
   this test. At least `4` genuinely distinct hypotheses (a sharp dip
   isolated to `~N=50`; a broad dip spanning `40-200`; an oscillating
   function; pure `2 sigma` noise with true overlap monotonically
   rising) remain equally consistent with only `3` points. A cheap
   fix (data already downloaded, in memory) is a real log-spaced sweep
   — not run here.

**Response (Step 8a matrix): all four points accepted. Item 3 is the
load-bearing correction — it changes what this test can honestly claim
to have settled, from "the mass-definition mismatch is probably minor"
to "the mismatch is real and its size at the SET-MEMBERSHIP level is
now measured, but its effect on any actual downstream STATISTIC
remains untested."**

## What this DOES establish

- **The `M500c/M200c` ratio itself is real, measured, and matches
  standard astrophysical expectations exactly** — a genuine, useful,
  reusable number for this branch (`mean=0.676`, `~10.6%` scatter).
- **Top-`N` overlap between `M200c`- and `M500c`-based selections is
  real but genuinely variable across `N`** (`74-92%` across the `3`
  tested values) — replacing a `[MEMORY]`-tier guess with real,
  measured numbers, even though those numbers turned out less uniform
  than the guess assumed.
- **A real, previously-unstated methodological point, now on record**:
  overlap fraction is the WRONG proxy for "does this mass-definition
  choice matter for a correlation result" — the swap is systematically
  biased, not random, so a high overlap number could still hide a real
  shift in `rho`, and a lower overlap number does not by itself prove
  one. Correctly answering the practical P158 question requires
  recomputing the actual statistic on both selections, not just
  measuring set overlap.

## What this does NOT establish

1. Does NOT establish whether any already-reported `rho_NN`/`rho_band`
   number would change under an `M500c`-based re-selection — the
   overlap proxy cannot answer this; a direct recompute is needed
   (named, not run here).
2. Does NOT establish a mechanism for the `N=50` anomaly — three
   concrete, cheap follow-up diagnostics are named (boundary check at
   `N=45-55`; print swap-out halos' own rank/ratio-percentile; a full
   `N`-sweep) but not run.
3. Does NOT characterize the overlap-vs-`N` relationship at any `N`
   not directly tested.
4. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**A real, honestly-scoped measurement that both confirms and
complicates the prior `[MEMORY]`-tier estimate — replacing a guess
with real data, at the cost of a real, more nuanced picture than "it's
probably fine."** The single biggest actionable takeaway: this
specific cross-check (set overlap) was the wrong question to fully
settle P158's own practical concern; a direct before/after
recomputation of an actual correlation statistic on both mass
selections is the real next step if this specific sub-question is
pursued further.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
