# NR-003 — Press-Schechter Comoving Density (Model A) FAIL

**Date:** 2026-06-12  
**Gate:** M8-C  
**Verdict:** REJECT (Model A only — Model B is PARTIAL, see experiments/m8c)  
**Commit:** d1638d4  
**Safety:** OUR_RECONSTRUCTION · EXTERNAL_STANDARD_PHYSICS · <HYPOTHESIS> · NOT_VALIDATION

---

## What Was Tested

**Model A — PS comoving cluster density:**  
n(>M_min, z) from Press-Schechter → use as proxy for bridge activity  
Tested at M_min = 1e14, 5e14, 2e15 M_sun

---

## Why It Failed

- n(>M_min, z) is **monotonically decreasing** with z for any M_min below PS knee
- Peaks at z → 0, not at z ≈ 0.40
- Pearson r vs ε: −0.048 to −0.413 (all negative, all sizes of M_min)
- Failed because comoving density is dominated by the exponential suppression erfc(ν/√2) at high z

---

## Mechanistic Insight

**[INSIGHT-2] Cluster DENSITY cannot explain ε(z) peak — cluster formation RATE can (partial signal).**

The distinction matters:
- `n(>M, z)` = how many clusters exist at epoch z (cumulative, monotone decreasing with z)
- `dN/dz` = how many clusters are forming per unit redshift at epoch z (rate, can peak mid-way)

Model B (dN/dz) gave Pearson r = 0.723 for M_min=1e14 — the best signal found so far.

**Implication:** If the bridge connects to cluster physics at all, the relevant quantity is likely the **formation rate** or some derivative of n(z), not the total abundance. This is consistent with the idea that the bridge might track energy injection from mergers or growth, not the static cluster count.

**What NOT to retry:** Any bridge based purely on comoving cluster abundance n(>M, z) applied directly as a proportionality to H_MULT. The physics selects for a derivative quantity.

---

## Cross-reference

- PARTIAL result (Model B dN/dz, r=0.723): `reports/m8c_closure_schedule.json`
- See [INSIGHT-3] in `docs/mechanism_insights.md` for synthesis with M8-D

---

## Scope

`OUR_RECONSTRUCTION · CONDITIONAL_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED`  
Press-Schechter is standard physics. Whether the author uses it is unknown.
