# Claim — H1d: Mass-Threshold Effect on ICM-Mass-Bias Partial Correlation

## Hierarchy
H1 (MULTING thermal energy = second gravitational source)
  └── H1a: ICM thermal energy correlates with mass gap → KILLED (r=0.021, p=0.883)
  └── H1b: WHIM in cluster outskirts correlates with mass gap → NEEDS-DATA
  └── H1c: Morphological state mediates partial r → NEEDS-DATA
  └── **H1d: The partial correlation depends on cluster mass (threshold effect)**

## Motivation

TJB's preprint frames the MULTING thermal energy effect as relevant to cosmic-web
nodes — which correspond to cluster-scale halos, not groups. The mechanism would be
stronger where:
(a) thermal energy is largest (massive clusters, T_x > 5 keV)
(b) mass bias is most diagnostically important (M_200 > 3×10^14 M_sun)

If H1d holds: the partial r(delta_M, E_ICM | M_WL) should be LARGER in magnitude
in high-mass clusters than in low-mass clusters (groups and poor clusters).

This is testable on existing CCCP data by mass subsample analysis.

## FL Zero-Signal Gate (Step -5)

- Entity: CCCP clusters N=50, split by M_WL median (Mahdavi et al. 2013) [VERIFIED-REAL]
- Falsifiable predicate: partial r(delta_M, E_ICM | M_WL) differs significantly
  between high-mass and low-mass subsamples
- Measurable outcome: Fisher z-transform test comparing two partial correlations

Gate passes: proceed to claim.

## Falsifiable Claim (FL Step 0)

**H1d-main:** The partial correlation r(delta_M, E_ICM | M_WL) [OUR-RECONSTRUCTION]
is significantly larger in absolute magnitude in the high-mass subsample
(M_WL > median_M, n~25) than in the low-mass subsample (M_WL < median_M, n~25).

Specifically:
- |r_high| > 0.50 AND |r_low| < 0.30 → PROMOTE (threshold effect confirmed)
- r_high substantially more negative than r_low → directional consistency
  with TJB mechanism acting preferentially at high mass

**H1d-secondary:** The correlation r(delta_frac, T_x) [fractional mass bias vs
temperature] shows breakpoint behavior near T_x = 5 keV, consistent with the
ICM thermal energy crossing a threshold for gravitational significance.

## Pre-registered Criteria (set BEFORE running mass-split analysis)

| Outcome | Verdict | Implication for H1 |
|---------|---------|-------------------|
| |r_high| > 0.50 AND |r_low| < 0.30 AND Fisher z-test p < 0.10 | PROMOTE H1d | Mass-dependent mechanism; supports H1 at cluster scale |
| |r_high - r_low| < 0.20 (no significant difference) | KILL H1d | Uniform mechanism; no mass threshold; H1 must explain all masses equally |
| Intermediate: 0.20 ≤ |r_high - r_low| ≤ 0.35 | INCONCLUSIVE | Suggestive but underpowered (n~25 per bin) |

**Kill threshold note:** Fisher z-test with n=25 per bin has power ≈ 0.50 to detect
r difference of 0.40. This is a low-power test. INCONCLUSIVE is the most likely
outcome. PROMOTE requires the difference to be clear (>0.50 in high vs <0.30 in low).

## Minimum Testable Hypothesis (FL Step 1)

1. Split CCCP N=50 by median M_WL (Mahdavi et al. 2013 Table 1)
2. Compute partial r(delta_M, E_ICM | M_WL) separately for high-mass and low-mass
3. Apply Fisher z-transformation to test equality of correlations
4. Check T_x distribution in each subsample (confirm mass-temperature ordering)
5. Sensitivity: split by T_x > 5 keV vs T_x < 5 keV instead of mass

## Assumptions (Claim Entropy)

| # | Assumption | Testable? | Evidence |
|---|-----------|-----------|---------|
| A1 | CCCP sample (N=50) provides enough power for mass-split test (n~25 per bin) | [VERIFIED] | Fisher z-test: power≈50% for r-diff=0.40; explicitly noted as low-power |
| A2 | High-mass clusters (M_WL > 5×10^14 M_sun) are the relevant range for TJB mechanism | [INFERRED] | TJB cites cosmic web nodes; cluster virial radii qualify |
| A3 | The partial r(delta_M, E_ICM | M_WL) = -0.701 [OUR-RECONSTRUCTION] is replicable on the full CCCP sample | [HYPOTHESIS] | Computed in H1a analysis; dependent on proxy choice |
| A4 | Mass bias interpretation is consistent across high/low mass clusters | [WEAK] | HE bias may be different in low-T clusters (hydrostatic assumption less valid) |

**Claim entropy:** 3 (A3 HYPOTHESIS, A4 WEAK, low statistical power acknowledged)

## Claim Entropy (Perelman)

claim_entropy = 1 (A3 status) + 1 (A4 low evidence) + 1 (missing negative control on morphology covariate) + 0 + 1 (low statistical power noted but unresolved)
             = **4**

## Counterfactual Frame

"In what world is H1d true?"
→ World where TJB's mechanism has a mass-scale threshold (cluster ≫ group)
→ Thermal energy is only dynamically significant above M_200 ~ 3×10^14 M_sun
→ The partial correlation we found is driven by the high-mass end of the CCCP sample

Independent changes needed to falsify H1d while keeping H1 alive:
1. The mechanism acts uniformly across all masses (no threshold)
2. OR the mechanism is absent at all cluster masses and only manifests in filaments (H1b)
3. OR the sample is insufficient to detect a threshold (inconclusive, not falsified)

## Status
[EXECUTABLE] Analysis can run on existing CCCP data without new observations.
Cost: ~1-2h Python (mass split + partial correlation + Fisher z-test).

## Data source
Mahdavi et al. 2013, ApJ 767, 116 (arXiv:1210.3689) — [VERIFIED-REAL, cite:mahdavi2013]
Same CCCP Table 1 used in H1a analysis.
