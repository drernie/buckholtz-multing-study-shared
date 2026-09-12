# FROZEN PROTOCOL v2 — thermal-pair kSZ fingerprint, independent-
# population holdout test

**Written and committed BEFORE running the test this file governs.**
Continues `FROZEN_PROTOCOL_v1.md` (INCONCLUSIVE, skeptic-confirmed,
`FINDING_frozen_test_v1_result.md`) and the pearl_registry entry
(2026-09-12) recording the skeptic's proposed joint REJECT clause.

**Why this is a genuine v2, not a post-hoc re-diagnosis of v1's own
data:** per the user's own explicit requirement this session — applying
a tightened criterion to v1's own already-seen numbers would be a
post-hoc diagnostic, not an independent test. v2 therefore changes the
**population**, not just the criteria: ACT-DR5 MCMF (v1's cluster
catalog) is itself SZ-selected from ACT's own temperature maps — a
structural precondition for the exact confound v1 found. v2 uses the
**DESI DR1 LRG catalog** instead (`LRG_NGC_clustering.dat.fits` +
`LRG_SGC_clustering.dat.fits`, 2,138,627 real objects, downloaded
2026-09-12, byte-verified complete) — spectroscopically/optically
selected, structurally independent of ACT's own map. This is Hand et
al. 2012's own original tracer choice, not an ad hoc substitution.

**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## 1. What changed from v1, and why

| | v1 | v2 |
|---|---|---|
| Population | ACT-DR5 MCMF clusters (SZ-selected) | DESI DR1 LRG galaxies (spectroscopically selected) |
| N | 4390 (full z∈[0.2,0.8] shell) | 4390 (random subsample, same N for a fair comparison, seed=20260911) |
| z range | [0.2, 0.8] | [0.4, 0.8] — the DESI∩MCMF overlap (DESI LRGs span 0.4-1.1; this range is fixed BEFORE looking at any v2 result, chosen for comparability with v1, not tuned) |
| Map, beam correction, outlier flag | `map_srcfree`, FWHM=1.4′, 8σ MAD | **unchanged** — this part of the pipeline is not in question |
| PROMOTE conditions 1-2 | separate | **unchanged** |
| PROMOTE conditions 3-4 (shape, detrend) | separate, independently evaluated | **replaced by a single joint clause** (see §2) |

## 2. The joint artifact-shape clause (skeptic's proposal, pearl_registry
## 2026-09-12, applied here for the first time — not to v1's own data)

Old v1 logic treated "peak not at max-r bin" and "survives detrending"
as two separate PROMOTE conditions, which could both fail for the SAME
underlying reason without forcing REJECT. v2 replaces this with an
explicit systematic-detector:

```
IF peak |p_pair| bin == largest-separation bin
   AND detrended |z| < 2 in the 2 smallest-r bins:
   VERDICT = REJECT-MEASUREMENT-SUBSTRATE
   (a genuine detection is not established, AND the shape matches a
   known systematic signature -- distinct from a plain non-detection)
```

**PROMOTE** requires ALL of (conditions 1-2 as in v1, conditions
3'-4' merged):
1. Raw |z| ≥ 3 in the 2 smallest-r bins.
2. Correct sign (negative) in those bins.
3'. NOT (peak at largest-r bin AND detrended |z| < 2 in smallest bins)
    — the joint systematic-detector above does not fire.
4'. Detrended |z| ≥ 2 in the 2 smallest-r bins (kept as an independent
    floor in addition to 3', so a signal that merely avoids the exact
    v1 artifact shape still has to show real post-detrend significance,
    not just fail to match one specific known bad pattern).

**REJECT-MEASUREMENT-SUBSTRATE** if condition 1 or 2 fails outright, OR
the joint systematic-detector fires (§2 above) regardless of 1-2.

**INCONCLUSIVE**: 1-2 pass, the systematic-detector does NOT fire, but
4' still fails (a middle case: not the known artifact shape, but not
yet significant post-detrend either).

## 3. What this test can and cannot establish

- **If DESI-LRG raw data does NOT reproduce the monotonic-growth-peak-
  at-max-r pattern:** real, structural (not just criteria-level)
  evidence that the pattern is tied to the SZ-selected population
  specifically — strengthens (does not prove) the SUPPORTED-AS-
  EXPLANATION reading from v1's own precision-corrected finding.
- **If DESI-LRG raw data DOES reproduce the same pattern:** evidence the
  artifact is NOT specific to SZ-selection (could be a broader z-
  dependent systematic in this map/pipeline, e.g. a real calibration or
  atmospheric-residual trend) — a genuinely new, important finding, not
  a failure of this test.
- **Either way, this is still not a MULTING test.** DESI LRGs are
  individual galaxies, not mass-characterized clusters — the
  `ξ_pred(z,s)`/`S_M(z,s)` physics this branch cares about needs cluster
  mass, which LRGs alone don't carry. v2 answers a methodological
  question (does the v1 artifact travel with the SZ-selected population,
  or is it pipeline-wide?), not a physics question.

## 4. Frozen pipeline

- **Map:** `act_dr4dr6_coadd_AA_night_f150_map_srcfree.fits` (unchanged
  from v1).
- **Beam correction:** `beam_correction.apply_beam_correction`, FWHM=
  1.4′ (unchanged).
- **Extraction:** `real_map_extraction.extract_cluster_temperatures`,
  1′ aperture (unchanged).
- **Outlier flag:** 8σ MAD (unchanged).
- **Population:** DESI DR1 LRG (NGC+SGC combined), z∈[0.4,0.8],
  random subsample N=4390, `np.random.default_rng(20260911)`.
- **Estimator, bins:** `pairwise_ksz_estimator.core_pairwise_estimator`,
  7 quantile bins (unchanged method).
- **Detrending:** quadratic T(z) fit and subtract, same as v1.

## 5. Skeptic pass

Same as v1 §4 — required before this verdict is reported as final,
given only this file's criteria + the raw numeric output.
