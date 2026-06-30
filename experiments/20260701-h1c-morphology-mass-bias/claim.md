# Claim — H1c: Morphological State Mediates the ICM/Mass-Bias Partial Correlation

## Hierarchy
H1 (MULTING thermal energy = second gravitational source)
  └── H1a: ICM thermal energy correlates with mass gap → KILLED (r=0.021, p=0.883)
  └── H1b: WHIM in cluster outskirts correlates with mass gap → NEEDS-DATA
  └── **H1c: Morphological state explains the partial r(delta_M, E_ICM | M_WL) = -0.701**
  └── H1d: Effect is mass-threshold-dependent (M > threshold)

## Motivation (Pearl from H1a analysis)

The H1a analysis found a null direct correlation (r=+0.021) but a striking
partial correlation r(delta_M, E_ICM | M_WL) = -0.701 [OUR-RECONSTRUCTION]:
at fixed M_WL, clusters with MORE ICM thermal energy show LESS mass bias.

Two competing interpretations:
1. (TJB-consistent) More thermal energy → some compensating effect on hydrostatic mass
2. (Standard physics) More thermal energy correlates with relaxation → better HE estimate

H1c tests interpretation (2): cluster dynamical state (morphological relaxation)
is a CONFOUNDER that creates the apparent partial correlation.
If H1c holds, TJB's mechanism is NOT needed to explain our partial r finding.

## FL Zero-Signal Gate (Step -5)

- Entity: CCCP clusters (N=50, Mahdavi et al. 2013) [VERIFIED-REAL]
- Falsifiable predicate: morphological disturbance predicts residual mass bias
  after controlling for M_WL AND E_ICM
- Measurable outcome: partial r(delta_M, w500 | M_WL, E_ICM) compared to pre-registered threshold

Gate passes: all three fields specified. Proceed to claim.

## Falsifiable Claim (FL Step 0)

**H1c-main:** The partial correlation r(delta_M, E_ICM | M_WL) = -0.701
[OUR-RECONSTRUCTION] is primarily explained by cluster morphological state (centroid
shift w500). Specifically: after also conditioning on w500, the residual partial
correlation r(delta_M, E_ICM | M_WL, w500) drops below 0.20 in absolute value.

**H1c-mechanism:** Morphologically relaxed clusters (w500 < 0.01) have:
(a) higher apparent E_ICM (concentrated, in equilibrium)
(b) smaller mass bias (thermal pressure dominates → HE mass accurate)
Morphologically disturbed clusters (w500 > 0.01) have:
(a) lower apparent E_ICM (gas stripped, infalling)
(b) larger mass bias (non-thermal pressure → HE mass underestimate)
This creates a spurious negative partial correlation between E_ICM and delta_M.

## Pre-registered Criteria (set BEFORE seeing centroid shift data)

| Outcome | Verdict | Implication |
|---------|---------|-------------|
| |r(delta_M, E_ICM \| M_WL, w500)| < 0.20 AND r(delta_M, w500 \| M_WL) > 0.40 | PROMOTE H1c; partial r explained by morphology | TJB mechanism NOT needed for partial r finding |
| 0.20 ≤ |residual r| ≤ 0.40 | INCONCLUSIVE (REPEAT) | Morphology partial explanation; TJB mechanism remains possible |
| |residual r| > 0.40 AND still significant p < 0.10 | KILL H1c; partial r survives morphology control | Supports H1 — non-morphological explanation needed |

**Key asymmetry:** H1c KILL → supports H1 (TJB mechanism); H1c PROMOTE → undermines H1 need.

## Minimum Testable Hypothesis (FL Step 1)

1. Obtain w500 centroid shift for CCCP clusters (from published morphology data)
2. Compute partial r(delta_M, E_ICM | M_WL, w500) using scipy.stats.partial_corr
   on N=50 CCCP clusters
3. Compare to r(delta_M, E_ICM | M_WL) = -0.701 [OUR-RECONSTRUCTION]
4. Check: r(delta_M, w500 | M_WL) direction (should be positive if H1c holds)

## Assumptions (Claim Entropy)

| # | Assumption | Testable? | Evidence |
|---|-----------|-----------|---------|
| A1 | w500 centroid shift is available for CCCP clusters from published papers | [INFERRED] | Mann & Ebeling 2012 provides CCCP morphology; CCCP papers may include |
| A2 | w500 captures the relevant dynamical state for HE bias | [VERIFIED-REAL] | Meneghetti et al. 2010, Nurgaliev et al. 2013: w500 correlates with mass bias |
| A3 | CCCP sample sufficient (N=50) for three-variable partial correlation | [VERIFIED] | df=46 → r > 0.29 is significant at p<0.05 |
| A4 | The partial r(delta_M, E_ICM | M_WL) = -0.701 [OUR-RECONSTRUCTION] is stable | [HYPOTHESIS] | Needs re-verification with centroid shift covariate added |

**Claim entropy:** 4 (4 partially confirmed assumptions)

## Claim Entropy (Perelman)

claim_entropy = N_unsupported_HIGH + N_hidden_assumptions + N_missing_negative_controls
              + N_ambiguous_definitions + N_unresolved_blockers
             = 1 (A1 status) + 1 (E_ICM definition ambiguity) + 1 (missing negative control) + 0 + 1 (data not yet in hand)
             = **4**

Target at PROMOTE: 0

## Counterfactual Frame

"In what world is H1c true?"
→ World where standard cluster physics (merger dynamics, non-thermal pressure)
  is sufficient to explain ALL of the mass bias variation.
→ TJB's mechanism is NOT active or NOT detectable at cluster scales.
→ The apparent partial correlation in H1a analysis is a statistical artifact
  of ignoring morphological state.

Independent changes needed for H1c to be false (and H1 to be supported):
1. Morphology does NOT drive the partial r (residual > 0.40 after w500 control)
2. WHIM thermal energy predicts mass bias independently (H1b PROMOTE)
3. Some other cluster property not captured by w500 drives the residual

All three would need to fail simultaneously for H1c to be definitively killed.

## Status
**KILLED (2026-07-01).** See decision.md.

Data source corrected: w500/wX came from Mahdavi et al. 2013 Table 2 (the same paper as
H1a/H1d), NOT Mann & Ebeling 2012 as originally planned (that paper uses a different
metric — BCG-to-X-ray-peak separation, not centroid shift). Coverage: 47/50 CCCP
clusters.

**Result:** partial r(delta_M, E_proxy | M_WL, wX) = −0.726, p=7.7e-9 — essentially
unchanged from baseline (−0.714), and well above the |r|>0.40 KILL threshold.
Secondary checks confirm wX is uncorrelated with both delta_M and E_proxy at fixed M_WL
(both r≈−0.08, p>0.5). Morphology is NOT a confounder for this partial correlation.

## Relationship to H1

H1c is an **alternative explanation** (standard physics) for the H1a partial
correlation finding. It is part of H1's falsification cycle:

- H1c PROMOTE → partial r explained; H1 not supported by CCCP data
- H1c KILL → partial r unexplained by morphology; H1 remains viable; proceed to H1b, H1d

**OUTCOME: H1c KILLED.** Standard cluster morphology does not explain the partial
correlation. This removes the leading standard-physics alternative explanation,
narrowing (but not closing) the space of competing accounts. H1b (WHIM/filament test)
is now the highest-priority remaining test.
