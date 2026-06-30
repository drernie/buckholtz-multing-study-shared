# Estimand — H1c: Morphological State Mediator

## EstimandOps L0 Classification
**Question type:** Predictive (causal path analysis via partial correlation)

*Note: This edges toward causal mediation but is classified predictive because we
have no intervention — we test whether morphological state is a sufficient confounder.
DAG is supplied for transparency but does not upgrade to causal.*

## Population
CCCP (Canadian Cluster Comparison Project) galaxy clusters:
N=50, 0.15 < z < 0.55, X-ray luminous (Mahdavi et al. 2013) [VERIFIED-REAL]

**Inclusion criteria:**
- Same N=50 clusters used in H1a analysis
- Centroid shift w500 available from published morphology catalog

**Exclusion criteria:**
- Clusters with no published centroid shift measurement: excluded from main analysis,
  sensitivity check will use X-ray concentration parameter c_SB as substitute

## Intervention
N/A — observational mediation analysis.

## Comparator
Null hypothesis (alternative to H1c):
r(delta_M, E_ICM | M_WL, w500) remains > 0.40 in absolute value — morphological
state does NOT account for the partial correlation.

## Endpoint
**Primary:** Partial correlation r(delta_M, E_ICM | M_WL, w500)
  - delta_M = M_WL − M_HE [OUR-RECONSTRUCTION from CCCP Table 1]
  - E_ICM = M_gas × T_x proxy [OUR-RECONSTRUCTION from CCCP data]
  - M_WL = WL mass from Mahdavi et al. 2013
  - w500 = X-ray centroid shift (morphological disturbance indicator)

**Secondary:** r(delta_M, w500 | M_WL) — does disturbance directly predict bias?

**Tertiary:** Scatterplot of residuals delta_M vs w500 colored by E_ICM quartile.

## Summary Measure
Partial Pearson correlation (3-variable and 4-variable cases).
Confidence interval via bootstrapping (B=10,000).

## MCID (Minimum Clinically Important Difference)
Change in |partial r| from -0.701 [OUR-RECONSTRUCTION] to < 0.20 when w500 added.
**Significance threshold:** |r(delta_M, E_ICM | M_WL, w500)| < 0.20, p > 0.20

Secondary confirmation: r(delta_M, w500 | M_WL) > 0.30 in positive direction
(more disturbed → more bias), p < 0.10.

## ICE (Intercurrent Events)
**ICE strategy: treatment-policy**

Potential ICEs:
- Cluster has no published w500 (not measured): substitute c_SB concentration
  parameter where available; otherwise exclude (document exclusion fraction)
- Cluster centroid shift varies with energy band used: use standard 0.5–2.0 keV
  measurement; if band not specified in source, note as uncertainty

Rationale: treatment-policy preserves the full CCCP sample heterogeneity.
Exclusions only for missing data (not substantive events).

**Significance threshold:** p < 0.10 for secondary r(delta_M, w500 | M_WL) claim.

## Natural Language Statement
"We estimate whether the partial correlation between lensing-to-hydrostatic mass gap
and ICM thermal energy proxy (after controlling for WL mass) in N=50 CCCP clusters
is mediated by cluster morphological disturbance (X-ray centroid shift w500), by
computing the residual partial correlation after additionally conditioning on w500."

## What this does NOT mean
1. Does NOT establish that morphological disturbance CAUSES mass bias (observational)
2. Does NOT test TJB's mechanism directly — only tests whether it is NEEDED to explain
   the partial correlation finding
3. Does NOT apply to the WHIM proxy (H1b) — H1c and H1b can both be true simultaneously
4. A H1c PROMOTE does NOT rule out TJB's mechanism at cosmic web filament scales
5. Sample size N=50 with 4-variable partial correlation has df=44 → power is limited
   for detecting small-to-medium effects

## Causal DAG (for transparency)
```
            Cluster dynamical state
            (merger history, w500)
           /                        \
          ↓                          ↓
  E_ICM / T_x         delta_M = M_WL - M_HE
  (thermal energy)      (mass bias)
          \                          ↑
           ----[→ confounds? or →]---
                   M_WL
                   (controls for size)
```
H1c predicts: the path E_ICM → delta_M is spurious; both are driven by w500.
H1 predicts: E_ICM has direct effect on delta_M beyond w500.

## Data requirements

**Source 1 (preferred): Mahdavi et al. 2013 Table or appendix**
- Check if w500 is reported for CCCP clusters
- URL: https://arxiv.org/abs/1210.3689

**Source 2: Mann & Ebeling 2012 (Chandra cluster morphologies)**
- MNRAS 420, 2120 (2012), arXiv:1111.0610
- Provides centroid shift and concentration for ~300 Chandra clusters
- CCCP overlap: likely ~30-40 clusters
- URL: https://arxiv.org/abs/1111.0610

**Source 3: ACCEPT survey (Cavagnolo et al. 2009)**
- Contains morphological parameters for many X-ray clusters
- Potential CCCP overlap

**Source 4: Zhang et al. 2023 or other CCCP morphology paper**
- Search: "CCCP centroid shift morphology"

**Cost estimate:** 1-2h (data search + partial correlation computation on existing CCCP dataset)

## Status
[NEEDS-DATA] Centroid shift w500 not yet confirmed available for CCCP N=50.
Priority: HIGH — this is cheaper test than H1b and has direct bearing on H1 viability.
