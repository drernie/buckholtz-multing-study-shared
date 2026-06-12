# M7-A Eq31 Mass-Ratio Toy-Test

**Date:** 2026-06-11 · **Verdict:** **PARTIAL**

## Status labels
NOT_VALIDATION · NOT_REFUTATION · M7_NUMEROLOGY_AUDIT · EQ31_TOY_TEST · EXTERNAL_STANDARD_PHYSICS

## Claim
Paper Eq. (31), canonical source line 881:
`(m_W)² : (m_Z)² : (m_Higgs)² :: 7 : 9 : 17`
Author's accuracy claim (Sec 2.7): Higgs predicted within 1σ "for some time";
"recently" W within 1σ.

## Data (EXTERNAL_STANDARD_PHYSICS, hard-coded with citation)
| Set | m_W (GeV) | m_Z (GeV) | m_H (GeV) |
|---|---|---|---|
| PDG 2022 | 80.377±0.012 | 91.1876±0.0021 | 125.25±0.17 |
| PDG 2024 avg | 80.3692±0.0133 | 91.1880±0.0020 | 125.20±0.11 |
| CDF-II 2022 (W only) | 80.4335±0.0094 | — | — |

No local particle-mass source exists in repo; values are standard PDG-style.
W mass itself is experimentally contested (CDF-II vs ATLAS/CMS/LEP) — hence
the sensitivity rows.

## Method
Squared masses compared to 7:9:17 via (a) W-normalized ratios, (b) sum-normalized,
(c) least-squares scale s minimizing Σ(m_i²−s·t_i)², (d) Z-anchored prediction
(author: Z best-measured) with pulls in experimental σ.

## Results (PDG 2022 primary)
| Quantity | Actual | Target | Deviation | Notes |
|---|---:|---:|---:|---|
| Z ratio (W=7) | 9.0096 | 9 | +0.11% | per-mille level |
| H ratio (W=7) | 16.9977 | 17 | −0.013% | per-mille level |
| lsq mass dev W | −0.0056% | 0 | — | scale s=923.0 GeV² |
| lsq mass dev Z | +0.048% | 0 | — | but σ_Z/m_Z = 0.0023% → ≫σ |
| lsq mass dev H | −0.012% | 0 | — | within σ_H |
| Z-anchored pred m_W | 80.4199 | 80.377 | **−3.58σ** | PDG2022 |
| Z-anchored pred m_W | 80.4203 | 80.3692 | **−3.84σ** | PDG2024 |
| Z-anchored pred m_W | 80.4199 | 80.4335 | **+1.45σ** | CDF-II 2022 |
| Z-anchored pred m_H | 125.325 | 125.25 | −0.44σ | ✓ author's claim holds |

## Best-fit scale test
s = 923.03 GeV² (PDG2022). Residuals (GeV²): W +0.7, Z −8.0, H +3.9.
Mass-level agreement 0.005–0.05% — numerically impressive, but Z is measured to
0.0023%, so the Z residual alone is ~20σ_Z under the joint fit.

## Uncertainty check
Deviations EXCEED experimental uncertainties for W (3.6–3.8σ vs PDG average) and
Z (under joint scale). Higgs is consistent (<1.2σ in all sets). The author's
"recently W within 1σ" is reproducible ONLY against the contested CDF-II 2022
value (+1.45σ); against the PDG world average it fails at ~3.8σ.

## Interpretation
**Approximate numerical relation** (per-mille in mass), NOT exact, with NO
physical derivation provided in the paper. Classification: approximate
relation / candidate numerical coincidence. The 7:9:17 pattern's W-prediction
lands between the contested experimental camps — an interesting provenance fact,
not evidence of mechanism.

## Overclaim guard
This test does not validate or refute IDM/MULTING. It tests one mass-ratio claim
against standard experimental values. "No derivation" ≠ "theory false".

## Verdict
**PARTIAL** — numerically close but not exact; deviations exceed current
experimental uncertainty for W (vs PDG average) and Z; no derivation provided.

## Next recommended gate
M7-B 5:1 dark-isomer ratio audit
