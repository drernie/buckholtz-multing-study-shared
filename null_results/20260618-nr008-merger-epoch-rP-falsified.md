# NR-008 — Merger-Epoch r_P(z) Hypothesis Falsified (H-k_A-1)

**Date:** 2026-06-18
**Slug:** merger-epoch-rP-falsified
**Verdict:** REJECT
**Script:** `scripts/test_rP_merger_hypothesis.py`
**Safety:** OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION

---

## Claim Tested (H-k_A-1)

> ε(z) from Table A1 is reproduced by **virial k_A** ∝ H(z)^(4/3) combined with a
> **non-standard r_P(z)** that has a minimum near z≈0.25–0.40, reflecting the epoch of
> maximum cluster proximity during the cosmic cluster-merger peak.
> Specifically: r_P(z) = r_P_standard(z) / (1 + A × ξ_merger(z))^(1/2)
> where ξ_merger(z) ∝ (1+z)^2.5 / H(z).

---

## Result

| Candidate | Pearson r | Peak z | Verdict |
|-----------|-----------|--------|---------|
| k_A virial + r_P standard (NR-004 baseline) | 0.524 | 0.40 | FAIL |
| k_A × n^(2/3) × (1+z)^2 (full MULTING structure) | 0.524 | 0.40 | FAIL |
| D^4 × H^(4/3) × n^(2/3) × (1+z)^2 (M* scaling) | 0.479 | 0.40 | FAIL |
| **k_A virial + r_P merger-epoch [H-k_A-1]** | **0.682** | **0.65** | **REJECT (< 0.75)** |
| D×H^(1/3) family (D^n×H^(n/3)) | 0.618–0.628 | 0.40 | PARTIAL |
| f×sigma8(z) — best single physical signal | 0.775 | 0.65 | NEAR-THRESHOLD |
| D×H^(1/3) + r_P merger combined | 0.702 | 0.65 | PARTIAL |
| Unconstrained D^5.5×H^2.75 (ceiling) | 0.820 | 1.00 | NEAR-THRESHOLD |

**Kill-test threshold: r > 0.75 (falsification), r > 0.85 (confirmation).**

H-k_A-1 best r = **0.682 < 0.75** → **FALSIFIED**.

Additional diagnostic: best A parameter in H-k_A-1 scan hits the upper bound of search
(A=100, saturated), indicating the model cannot improve within the merger-rate framework.

---

## Critical Finding (Pearl Gate output)

**ε(z) has a secondary bump at z=3.2–8.5 that no single-component formula can explain.**

```
eps(z=3.20) = 0.106  ← above
eps(z=5.00) = 0.048  ← dip
eps(z=8.50) = 0.101  ← secondary peak (2.1× higher than z=5.00)
```

This secondary structure is **invisible to f×sigma8, merger rates, or any low-z-peaking formula.**

**Key diagnostic:** f×sigma8(z) WITHOUT z=8.50 gives **r=0.851** — crossing the 0.85 threshold
on 10 of 11 points. The secondary bump at z=8.50 is the structural obstacle.

**Implication (INFERRED):** ε(z) may require TWO components:
- PRIMARY (z=0–2): consistent with f×sigma8(z) [r=0.851 on 10 pts]
- SECONDARY (z=3–8.5): secondary bump unexplained by low-z cluster physics

This two-component structure is consistent with MULTING's F_oP = F_m − F_d + F_q:
the quadrupole term F_q may dominate at z>3 (early universe, proto-cluster scales).

---

## Why the Claim Fails

1. **Merger rate ξ ∝ (1+z)^2.5 increases with z** → r_P correction makes r_P smaller at HIGH z,
   not at intermediate z~0.40. The resulting eps_predicted peaks at z=0.65, not z=0.40.
2. **The A parameter saturates** at maximum of scan range, indicating the model topology
   cannot fit the shape regardless of parameter value.
3. **Unconstrained ceiling r=0.820** — with any D^a×H^b formula, the max achievable is 0.82,
   still below the 0.85 threshold. The secondary bump (z=8.50) is the structural blocker.

---

## Mechanistic Insight

**[INSIGHT-6] ε(z) from Table A1 has TWO structural features that likely require TWO MULTING terms:**
- Feature 1: Primary hump at z=0.25–0.65 → DIPOLE term (F_d ∝ β_d k_A/r_P²)
- Feature 2: Secondary hump at z=3.2–8.5 → QUADRUPOLE term (F_q ∝ β_q)

**[INSIGHT-7] f×sigma8(z) is the best physical proxy for the DIPOLE component** (r=0.851 on 10 pts).
This observable is directly measurable by RSD galaxy surveys and does NOT require knowing β_d.

**[INSIGHT-8] The D^n×H^(n/3) family (n=1,2,3,4,6) all peak at z=0.40** with r≈0.62.
Base function: D(z)×H(z)^(1/3). Physical meaning: linear growth amplitude × (ρ_crit)^(1/6).

---

## What NOT to Retry

- Any single-component merger rate model for r_P
- Any monotone function (virial, PS density, NFW concentration alone)
- Any formula that cannot produce the z=3–8.5 secondary bump

## What to Try Next (if TJB provides Q2 answer)

- Two-component fit: eps = α × f×sigma8(z) + β × F_q_model(z, β_q)
- Test: if β_q=0 → secondary bump disappears → eps should be monotone for z>2
- Compare single-β_q value against TJB's β_q=18.0 (Claude output)
- MCMC on {β_d, β_q} with k_A = f×sigma8-based schedule (not virial)

---

## Scope

`OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · BETA-1-HOLD-CONTINUES`
BETA-1 HOLD remains: full bridge requires both β_d and β_q from TJB.
