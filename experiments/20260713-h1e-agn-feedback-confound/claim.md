# Claim — H1e: AGN Feedback Mediates the ICM/Mass-Bias Partial Correlation

## Hierarchy

H1 (MULTING thermal energy = second gravitational source)
  └── H1a: ICM thermal energy correlates with mass gap → KILLED (r=0.021, p=0.883)
  └── H1b: WHIM in cluster outskirts correlates with mass gap → NEEDS-DATA
  └── H1c: Morphological state (centroid shift wX) explains the partial correlation → KILLED (r_residual=-0.726, unchanged from baseline)
  └── H1d: Effect is mass-threshold-dependent → KILLED (r_diff=0.001)
  └── **H1e: AGN feedback (radio/kinetic mode, cool-core regulation) explains the partial correlation**

## Motivation (registered gap from NR-012)

NR-012 (H1c decision.md, `experiments/20260701-h1c-morphology-mass-bias/decision.md:81`
and Relaxation Map row in `null_results/20260701-nr012-h1c-morphology-mediator.md:51`)
explicitly listed AGN feedback as an untested alternative explanation for the partial
correlation `r(delta_M, E_ICM | M_WL) ≈ -0.70 to -0.73`, and named the missing
ingredient as "AGN-activity indicators per cluster" — flagged but never pursued,
because no covariate was in hand at the time.

Physical motivation (standard astrophysics, not TJB-specific): AGN feedback in its
Radio/Kinetic Mode (dominant in massive relaxed ellipticals/cool-core cluster BCGs —
the same regime as most of the CCCP sample) injects non-thermal turbulent energy into
the ICM via jets and X-ray cavities. Two distinct channels could produce the observed
partial correlation without invoking TJB's mechanism:
1. AGN-driven turbulence inflates the thermal-energy proxy E_ICM without tracking the
   true gravitational potential depth.
2. The same non-thermal pressure violates the hydrostatic-equilibrium assumption used
   to derive M_HE, directly biasing delta_M = M_WL - M_HE.

This is mechanistically distinct from H1c (morphological/dynamical disturbance, tested
via centroid shift wX): a cluster can be dynamically relaxed (low wX, would pass H1c)
while still hosting strong AGN feedback (cool-core clusters are, almost by definition,
BOTH relaxed AND AGN-regulated — that is precisely why cooling flows don't run away).
H1e is therefore NOT a retry of H1c under a different name; it targets a mechanism
H1c's covariate (wX) does not capture. Flagged explicitly per the Adaptive Iteration
Branch Rule so this isn't mistaken for reopening a killed branch.

## FL Zero-Signal Gate (Step -5)

- Entity: CCCP clusters (N=50, Mahdavi et al. 2013) [VERIFIED-REAL], the same sample
  as H1a/c/d
- Falsifiable predicate: an AGN-feedback indicator (cool-core status, and/or a
  quantitative radio/X-ray-cavity power proxy) predicts residual mass bias after
  controlling for M_WL AND E_ICM
- Measurable outcome: partial r(delta_M, AGN_indicator | M_WL, E_ICM) compared to a
  pre-registered threshold, mirroring H1c's design exactly

Gate passes. Proceed to claim.

## Falsifiable Claim (FL Step 0)

**H1e-main:** The partial correlation `r(delta_M, E_ICM | M_WL) ≈ -0.70` is primarily
explained by AGN feedback activity. Specifically: after also conditioning on an
AGN-feedback indicator, the residual partial correlation
`r(delta_M, E_ICM | M_WL, AGN_indicator)` drops below 0.20 in absolute value.

**H1e-mechanism:** Clusters with strong AGN feedback (cool-core, radio-loud BCG,
and/or detected X-ray cavities) have systematically different E_ICM (inflated by
non-thermal turbulent energy) and/or delta_M (biased by non-thermal pressure in the
HE mass estimate) than clusters without strong central AGN activity, in a way that
reproduces the observed negative partial correlation without requiring TJB's
mechanism.

## Pre-registered Criteria (set BEFORE fetching any AGN indicator's relationship to
delta_M/E_ICM -- the cluster list + cool-core flags below were already fetched as
part of identifying the sample, but no correlation with the outcome variables has
been computed yet at the time this file is written)

| Outcome | Verdict | Implication |
|---------|---------|-------------|
| \|r(delta_M, E_ICM \| M_WL, AGN_indicator)\| < 0.20 AND cool-core/AGN status itself correlates with delta_M or E_ICM at \|r\|>0.30 (p<0.10) | PROMOTE H1e; partial r explained by AGN feedback | TJB mechanism NOT needed for partial r finding |
| 0.20 ≤ \|residual r\| ≤ 0.40 | INCONCLUSIVE (REPEAT) | AGN feedback partial explanation; TJB mechanism remains possible |
| \|residual r\| > 0.40 AND still significant p < 0.10 | KILL H1e; partial r survives AGN control | Third standard-physics alternative eliminated; strengthens H1's remaining space (H1b only) |

**Key asymmetry (same as H1c):** H1e KILL -> supports H1 (TJB mechanism, by further
elimination); H1e PROMOTE -> undermines H1's need.

## Two-phase data plan (honest scope note)

Unlike H1c (which reused already-cached delta_M/E_ICM values from the H1a
computation), this session found that **no CSV of the underlying H1a/c/d per-cluster
values (delta_M, E_ICM, M_WL, wX) was ever persisted** -- they were computed inline in
a prior session and are not reproducible from files currently in this repo. This is a
real gap, not specific to H1e.

- **Phase 1 (shared infrastructure fix) -- COMPLETE 2026-07-13:** re-extracted M_WL,
  M_hydro, M_Gas, T_X, wX, K0 per cluster (50/50, zero name mismatches) directly from
  the downloaded Mahdavi et al. 2013 PDF via `pdfplumber` (not an AI-summarized
  WebFetch -- that path was tried first and rejected as unreliable for large numeric
  tables). Saved as `artifacts/cccp_mahdavi2013_merged.csv`, `[VERIFIED-DIRECT-READ]`,
  with raw extraction text and parser committed for full reproducibility. Internal
  sanity check against the paper's own stated "~10% average mass bias" passed (median
  and sum-ratio statistics bracket it; the naive mean is outlier-pulled, explained not
  hidden). This gap no longer blocks any future H1x branch.
- **Phase 2 (H1e-specific) -- data now in hand, test not yet run:** K0 (central
  entropy, keV cm^2) turned out to already be a standard quantitative AGN-feedback
  proxy in the same table -- no separate radio/X-ray-cavity catalog fetch needed. The
  "cheapest first test" and the "quantitative catalog" stretch goal from the original
  plan have effectively merged into one: K0 IS the quantitative indicator.

## Assumptions (Claim Entropy)

| # | Assumption | Testable? | Evidence |
|---|-----------|-----------|---------|
| A1 | K0 (central entropy) is a valid, quantitative proxy for AGN feedback activity | [VERIFIED-REAL, literature-established] | Standard result: low K0 = cool-core = radio-loud BCG regulating cooling flow (McNamara & Nulsen review; Rafferty et al. 2006; Bîrzan et al. 2004); the source paper itself uses a K0 threshold to define cool-core in its own Fig. 3 |
| A2 | K0 is not simply a relabeling of wX (already tested, killed in H1c) | [OPEN] | Source paper's own Fig. 4 reports Spearman r=0.52+-0.10 between K0 and wX -- correlated but far from identical (r^2~0.27, most variance unshared); still needs an explicit partial-correlation-controlling-for-wX check to confirm H1e is not just H1c restated |
| A3 | Base CCCP data (M_WL, M_hydro, M_Gas, T_X, K0, wX) is re-extractable from the same Mahdavi 2013 source used for H1a/c/d | [VERIFIED-DIRECT-READ] | Done -- `artifacts/cccp_mahdavi2013_merged.csv`, 50/50 clusters, pdfplumber extraction, sanity-checked |
| A4 | A quantitative AGN-feedback proxy exists in publicly accessible, already-used data (no new external catalog needed) | [VERIFIED-REAL] | K0 (central entropy), already in Table 2 of the same source paper as M_WL/M_Gas/M_hydro/wX |

**Claim entropy:** 1 (A2 open; A1, A3, A4 resolved -- down from 2)

## Counterfactual Frame

"In what world is H1e true?"
-> A world where standard AGN-feedback astrophysics (already well-established,
independent of MULTING) is sufficient to explain the partial correlation, without
needing to invoke a second gravitational source.
-> TJB's mechanism is not detectable at cluster scale once AGN feedback is properly
accounted for, just as it was not detectable once morphology (H1c) was accounted for.

Independent changes needed for H1e to be false (and H1 to survive further, pending
H1b): AGN-feedback indicator does NOT explain the residual (per the KILL criterion
above) -- would be the third of three natural standard-physics alternatives
eliminated (H1a raw correlation, H1c morphology, H1e AGN feedback), leaving H1b
(WHIM/filament, TJB's actual proposed cosmic-web-scale mechanism) as the only
remaining untested channel.

## Status
**CLOSED — KILL (2026-07-17).** Test executed via `artifacts/h1e_partial_correlation_test.py`:
r(delta_M, E_ICM | M_WL, K0) = -0.7181, p=1.33e-08 -- exceeds the pre-registered KILL
threshold (|r|>0.40, p<0.10). AGN feedback does not mediate the partial correlation.
Full writeup: `decision.md`. Registered as `null_results/20260713-nr014-h1e-agn-feedback-confound.md`.
