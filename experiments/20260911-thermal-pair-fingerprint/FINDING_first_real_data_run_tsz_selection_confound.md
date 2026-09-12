# FINDING — first real-data run: strong first-pass signal was a
# redshift-dependent tSZ-selection artifact, confirmed and removed

**Continues:** `FINDING_pairwise_ksz_estimator_phase1.md` (Phase 1,
estimator math) → this file is Phase 2's first real-data result.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Data:** real ACT DR6.02 f150 GHz coadd temperature map (5.35 GB,
`lambda.gsfc.nasa.gov`) + real ACT-DR5 MCMF cluster catalog, z∈[0.2,0.8],
4390 clusters, all landing inside the map footprint (0 off-map).

---

## What happened, in order

1. **`run_real_data_phase2.py`** (the explicitly-labeled "engineering
   shakeout, not the pre-registered test") ran the full pipeline
   end-to-end on real data for the first time. Raw extracted
   temperatures: mean **-49.25 µK**, std **90.07 µK** — roughly an
   order of magnitude larger than Hand et al. 2012's own simulated kSZ
   expectation (1.6 µK / 0.3 µK for 10¹⁴/10¹³ M_☉ clusters at 200 km/s).
   The pairwise estimator on these raw temperatures gave a
   **statistically strong, monotonically-growing-with-separation**
   signal: z = -4.27, -4.11, -4.35, -3.86, -3.38, -3.03, -1.51 across 7
   quantile bins from 593 to 4787 Mpc.
2. **This was NOT reported as a positive result.** A real velocity-
   correlation signal should *decay* at large separations (pairs
   thousands of Mpc apart share no causal/gravitational connection in
   ΛCDM); growth to ~4800 Mpc is not physically sensible for kSZ. Per
   `skeptic-triggers.md` Trigger 2 (unexpected success), this was
   treated as `REQUIRES-CHECK`, not evidence.
3. **Hypothesis formed:** the ACT-DR5 MCMF cluster catalog is itself
   tSZ-selected (Multi-Component Matched Filter confirmation of ACT's
   own SZ-detected candidates) — a partial circularity Hand et al. 2012
   avoided by using optically-selected BOSS galaxies instead. If survey
   depth/mass-completeness evolves with redshift (standard for a
   roughly flux-limited SZ survey), raw T_i correlates with z_i, and
   pairs with the largest 3D separation are overwhelmingly pairs with
   very different z (not physically associated) that get large weight
   in Eq. 3's `c_ij` — reproducing the observed pattern without any kSZ.
4. **Cheap diagnostic** (`diagnose_tsz_selection_confound.py`):
   Pearson r(T,z) = +0.068 (p=6×10⁻⁶) — statistically significant but
   linearly weak. Redshift-quartile means showed a real, directionally
   consistent trend hidden under the correlation coefficient: z∈[0.20,
   0.376) mean=-59.98 µK → z∈[0.635,0.80) mean=-42.29 µK, an ~18 µK
   swing. Verdict at this stage: real trend exists, but a small linear
   r does not by itself prove it drives the *pairwise-weighted*
   statistic's full effect size — needed a direct test of the actual
   mechanism, not a proxy.
5. **Decisive test** (`detrend_and_rerun.py`): fit T(z) with a quadratic
   (`T(z) = -119.964·z² + 159.057·z - 95.816`), subtract it, re-run the
   *identical* estimator on the residuals.

## The result

| | ORIGINAL (raw T) | DETRENDED (T(z) removed) |
|---|---|---|
| r=593 Mpc | z=-4.27 | z=+0.42 |
| r=1442 Mpc | z=-4.11 | z=+0.39 |
| r=1946 Mpc | z=-4.35 | z=-0.03 |
| r=2458 Mpc | z=-3.86 | z=+0.13 |
| r=2993 Mpc | z=-3.38 | z=+0.28 |
| r=3562 Mpc | z=-3.03 | z=-0.05 |
| r=4787 Mpc | z=-1.51 | z=-0.56 |

**Every bin collapses to |z|<0.6.** The residual per-cluster std barely
moved (89.81 vs 90.07 µK — the quadratic trend removes almost none of
the total *variance*, since individual-cluster scatter dwarfs the
smooth z-trend) — yet the *pairwise-correlated* signal vanished
entirely. This is the signature of exactly the mechanism hypothesized:
a smooth trend in T(z), not per-cluster noise, was driving the
pairwise statistic, because the estimator's own weighting amplifies
exactly the pairs (large-z-separation) where that trend matters most.

## What this DOES establish

- **The pipeline works end-to-end on real data** — real map, real
  catalog, real extraction, real jackknife, real diagnosis of a real
  confound, real direct test. This is genuine Phase 2 engineering
  progress.
- **A concrete, previously-unflagged methodological hazard for this
  branch's specific choice of tracer population** (SZ-selected clusters
  vs Hand et al.'s optically-selected galaxies) is now documented,
  diagnosed, and shown to be removable by a simple z-detrend.
- **The Cheapest Differentiating Test Protocol worked as designed**:
  cheap correlation check first (informative but inconclusive) → one
  decisive direct test (definitive) — not a guess, not a shortcut.

## What this does NOT establish

1. **Not evidence against kSZ or MULTING.** The original signal was
   never a kSZ candidate to begin with — its physical implausibility
   (growing with separation) was the reason it was investigated, not
   trusted. Its removal by detrending is confirmation of the artifact
   hypothesis, not a null result about MULTING.
2. **Not a demonstration that the detrended pipeline is now ready for a
   real test.** Beam matching and τ-weighting remain entirely unbuilt
   (per `FINDING_pairwise_ksz_estimator_phase1.md`'s own list) — this
   finding closes exactly one gap (the population-selection artifact),
   not all of them. **[UPDATED 2026-09-12]** Point-source handling is
   separately resolved: no dedicated DR6 point-source catalog is
   publicly released yet (Vargas et al., cited by the DR6 Maps paper,
   arXiv:2503.14451, itself listed as "2025, in preparation" — checked
   directly in that paper's own reference list) — ACT's own
   `map_srcfree` product (all ≥5σ sources subtracted by the survey
   team) is used instead of DIY masking, see `run_real_data_phase2.py`.
3. **Not proof the quadratic detrend is the *correct* or *final*
   handling of this artifact** — it is the simplest model that could
   capture the observed non-monotonic quartile pattern, chosen and
   applied honestly, not tuned to produce a particular outcome. A more
   principled fix (e.g. matching clusters by mass proxy instead of
   detrending temperature directly) is a legitimate future refinement.

## Cross-check on `map_srcfree` (2026-09-12) — same result, confirms
## point sources were never the driver

Re-ran the identical original+detrend test on ACT's own point-source-
subtracted map (`map_srcfree`, all ≥5σ sources removed by the survey
team) instead of the raw map. Fresh extraction, independent cache:

| | raw map (original finding) | `map_srcfree` |
|---|---|---|
| z at r=593 Mpc | -4.27 | -4.23 |
| z at r=1442 Mpc | -4.11 | -4.02 |
| z at r=1946 Mpc | -4.35 | -4.25 |
| z at r=2458 Mpc | -3.86 | -3.72 |
| z at r=2993 Mpc | -3.38 | -3.25 |
| z at r=3562 Mpc | -3.03 | -2.92 |
| z at r=4787 Mpc | -1.51 | -1.43 |
| detrended, all bins | &#124;z&#124;<0.6 | &#124;z&#124;<0.6 |

**Nearly identical, few-percent-level differences only.** This is the
expected, confirming result: the artifact was already correctly
diagnosed as a redshift-dependent tSZ-*selection* effect (which map
version is used doesn't touch that), not point-source contamination —
removing point sources was never expected to change the outcome, and
it didn't. Point-source handling is a real, separately-necessary fix
(a single bright unmasked source at one cluster's position would still
be a legitimate individual-cluster risk `map_srcfree` now closes), but
this cross-check confirms it was not silently masking the earlier
result's own actual cause.

## Status

**Confound identified, tested, and confirmed removable.** Point-source
handling resolved 2026-09-12 (`map_srcfree`, see above). Next, before
any result here can be treated as informative about kSZ/MULTING: real
beam matching and an explicit freeze-then-look protocol remain (per
`FINDING_pairwise_ksz_estimator_phase1.md`'s own remaining-work list).
This file's own detrended, near-zero result should NOT be re-reported
later as "no kSZ found" — it is a null-by-construction check of the
estimator's honesty, not a completed test of the physics.
