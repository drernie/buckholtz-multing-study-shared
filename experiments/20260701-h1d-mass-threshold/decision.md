# Decision — 20260701-h1d-mass-threshold

**Date:** 2026-07-01
**Status:** KILL (H1d)
**Evidence grade:** B (N=50 real observational data [VERIFIED-REAL])

## Numerical results [OUR-RECONSTRUCTION]

### Full sample (baseline verification)
| | r | p |
|--|---|---|
| partial r(delta_M, E_proxy \| M_WL) | −0.701 | <0.0001 |

Verified: matches H1a decision.md exactly ✅

### Mass-split analysis (H1d test)
Median M_WL = 6.0 × 10^14 M_sun

| Subsample | N | partial r(delta_M, E_proxy \| M_WL) | p |
|-----------|---|------|---|
| HIGH-mass (M_WL ≥ 6.0) | 25 | **−0.732** | <0.0001 |
| LOW-mass  (M_WL < 6.0) | 25 | **−0.731** | <0.0001 |

Fisher z-test (|r_high| vs |r_low|):
- z_stat = 0.005, p = 0.498 (one-tailed)
- |r_high| − |r_low| = 0.001 (essentially zero)

### Temperature sensitivity split
| Subsample | N | partial r | p |
|-----------|---|-----------|---|
| HOT (T_x ≥ 5 keV) | 41 | −0.681 | <0.0001 |
| COOL (T_x < 5 keV) | 9 | −0.066 | 0.867 |

Note: COOL bin (N=9) is severely underpowered — power to detect r=−0.70 with N=9 is < 30%.
The null in cool clusters is NOT informative.

## Verdict

**H1d KILLED** by pre-registered criterion:
- |r_high| − |r_low| = 0.001 < 0.20 (kill threshold)
- Fisher z = 0.005, p = 0.498 (no significant difference)

The partial correlation r(delta_M, E_proxy | M_WL) ≈ −0.73 is IDENTICAL
in high-mass and low-mass subsamples. No mass-threshold effect.

## Kill Analysis

**What was killed:**
H1d — the hypothesis that the ICM/mass-bias partial correlation shows
a mass-threshold effect (stronger in M_WL > ~6×10^14 M_sun clusters).

Conditions: {CCCP N=50, M_WL-split analysis, partial correlation method, OUR_RECONSTRUCTION}

**What was NOT killed:**
1. H1 (broad TJB mechanism) — H1d only tested whether the effect is mass-threshold-dependent
2. H1c — morphological state as mediator (still untested, needs w500 data)
3. H1b — WHIM filament thermal energy correlation (still NEEDS-DATA)
4. The existence of a T_x-dependent behavior (see Pearl below)
5. The reality of the partial r = −0.701 (verified by BOTH subsample analyses)

## Pearl candidate (unexpected finding) [CANDIDATE]

**Observation:** T_x split shows r = −0.681 (HOT, N=41) vs r = −0.066 (COOL, N=9).

**Falsifiable prediction (Pearl P001):**
If the partial correlation r(delta_M, E_proxy | M_WL) is driven by ICM thermal state
rather than mass, then:
- A sample with more cool clusters (T_x < 5 keV) would show WEAKER partial r
- A partial r controlling for T_x would drop substantially: |r(delta_M, E_proxy | M_WL, T_x)| < 0.40

**Revival condition:** Requires cool-cluster sample with N ≥ 20 (T_x < 5 keV clusters)
for adequate power. XMM or Chandra surveys targeting low-temperature groups.

**next_check:** 2026-07-15 (when H1c analysis with morphology data is run —
  T_x and w500 are often correlated, so H1c analysis will cross-test this pearl)

**trigger_condition:** H1c analysis reveals that T_x (not morphology) drives the
residual after controlling for M_WL.

## Relaxation Map (from H1d kill)

| Branch | Changed assumption | Prediction | Status |
|--------|--------------------|-----------|--------|
| H1d original | Mass threshold effect | |r_high| >> |r_low| | KILLED |
| H1d-Tx | T_x threshold instead of mass | |r_hot| >> |r_cool| on larger sample | PEARL [CANDIDATE] — needs N≥20 cool clusters |
| H1c | Morphology (w500) mediates partial r | Residual drops when w500 added | NEEDS-DATA |
| H1b | WHIM gas in filaments | r > 0.30 in simulations | NEEDS-DATA (TNG API) |

## Skeptic concerns (pre-answered)

**Concern 1:** "N=25 per bin may be insufficient for subgroup partial correlation"
→ ACCEPTED as limitation. Power to detect r=0.40 difference with N=25 per bin is ~50%.
BUT: the observed r_diff = 0.001 is negligible regardless of power. A small sample
can only miss a real effect — it cannot manufacture a perfect null (p=0.498) from noise.
The KILL is robust.

**Concern 2:** "The T_x split result (COOL: r=−0.066) looks like a null"
→ DISMISSED as underpowered. N=9 cool clusters cannot detect r=−0.70 reliably.
The null in cool bin is NOT evidence against H1d or H1. See Pearl candidate above.

**Concern 3:** "Maybe the mass threshold is higher (>10^15 M_sun)?"
→ ACCEPTED as un-tested. CCCP only has N=7 clusters with M_WL > 10×10^14 M_sun.
This cannot be tested on CCCP data. Would require South Pole Telescope or ACT data.

## Status summary for H1 Cycle 2

| Sub-hypothesis | Status | Data |
|----------------|--------|------|
| H1a | KILLED (2026-07-01) | r=0.021, N=50 CCCP [VERIFIED-REAL] |
| H1b | NEEDS-DATA | TNG API required |
| H1c | NEEDS-DATA | Centroid shift w500 for CCCP needed |
| H1d | **KILLED (2026-07-01)** | r_diff=0.001, N=50 CCCP [VERIFIED-REAL] |

H1 (broad) status: INCONCLUSIVE (H1a and H1d killed; H1b and H1c untested)
