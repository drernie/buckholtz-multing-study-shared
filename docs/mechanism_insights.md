# Mechanism Insights — What Negative Results Revealed

**Date:** 2026-06-13  
**Status:** LIVING DOCUMENT — add insights as gates complete  
**Scope:** OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION

This document accumulates **mechanistic constraints** derived from failed/partial experiments.  
Each insight is a statement about what the bridge F_oP → H_MULT(z) MUST or CANNOT be doing,  
derived from what we ruled out.

---

## How to Read This

- **Negative result** → what approach we ruled out
- **Mechanistic insight** → what this tells us about the underlying mechanism
- **Implication** → constraint on the author's actual bridge
- **Confidence** → how robust the inference is

Confidence levels:
- `[THEOREM]` — follows from math/physics, not refutable by new data
- `[STRONG]` — consistent across multiple gates, no counter-evidence
- `[SIGNAL]` — one gate only, needs confirmation
- `[HYPOTHESIS]` — plausible inference, easily overturned

---

## Insight Register

---

### INSIGHT-1: ε(z) has multiple characteristic scales — no single-parameter bridge can fit it

**Source:** NR-001/002, Gates M8-A + M8-A-R1 (commit 30473a2, add7cba)  
**Confidence:** `[STRONG]` — arithmetic verified (M8-A-R1 PASS, 4 corrections applied)

**Negative result:** Constant-ε bridge fails (max residual 0.104, factor 4.7× variation). Power-law bridge fails (α sign changes 3×).

**ε(z) structure:**
```
z:    0.06  0.14  0.25  0.40*  0.65  1.00  1.50  2.10  3.20  5.00  8.50
ε:   .063  .125  .215  .228   .213  .186  .214  .171  .106  .048  .101
      ↑     ↑     ↑    PEAK↓   ↓    LOCAL_MIN  RISE   ↓    ↓   GLOBAL_MIN  UPTICK
```

**Mechanistic insight:** The bridge formula must produce output with:
1. A primary peak near z ≈ 0.40 (not at z=0 or z→∞)
2. A secondary rise near z ≈ 1.5 (local structure, not noise — 3 points confirm)
3. An uptick at z=8.5 (single-point, leverage risk — treat with caution)

**Implication:** The bridge involves at least 2 competing physical processes active at different epochs. A single power-law or monotone function is ruled out by theorem (α changes sign 3×).

**What this means for Q1 (bridge method):** The formula must be a ratio, difference, or product of at least 2 epoch-dependent quantities with different scalings — not a single scaling relation.

---

### INSIGHT-2: Cluster density ≠ bridge proxy — cluster formation rate is a better candidate

**Source:** NR-003, Gate M8-C (commit d1638d4)  
**Confidence:** `[SIGNAL]` — single gate, r=0.723 needs confirmation on independent data

**Negative result:** PS comoving density n(>M, z) is monotone decreasing → Pearson r = −0.05 to −0.41.

**Positive signal:** Survey count rate dN/dz peaks at z=0.40–0.65 (M_min=1e14), r=0.723.

**Mechanistic insight:** If the bridge connects to cluster physics, the relevant epoch marker is the **formation activity** (rate of cluster production or merger events), not the static cluster abundance. This is physically plausible: merger-driven energy injection peaks when structure formation is most active (~z≈0.5–1.0), not at z=0.

**Implication:** The author's D_C:AB(z) or cluster schedule likely tracks a quantity that peaks mid-redshift, consistent with the cluster formation peak epoch (z≈0.5–1.5 in standard ΛCDM).

**Caveat:** r=0.723 is PARTIAL. Secondary structure at z=1.0–1.5 is NOT reproduced. This signal is suggestive, not confirmatory.

---

### INSIGHT-3: k_A from virial self-similar scaling is monotone by theorem

**Source:** NR-004, Gate M8-D (commit 9100b0a)  
**Confidence:** `[THEOREM]` — follows from dimensional analysis + overdensity criterion

**Derivation:**
```
r_vir ∝ ρ_crit(z)^(-1/3) ∝ H(z)^(-2/3)
k_A = G·M/r_vir² ∝ ρ_crit(z)^(2/3) ∝ H(z)^(4/3)
H(z) is monotone increasing with z → k_A is monotone increasing with z
```

**Implication (hard constraint):** The author's k_A(z) schedule either:
- (a) Uses a non-standard definition of k_A that does not reduce to G·M/r_vir², OR
- (b) Involves k_A in a ratio/difference that cancels the H(z)^(4/3) trend, OR
- (c) The bridge does not use k_A as a simple multiplier — it may appear in a combination like k_A / k_A_ref(z) where k_A_ref itself also scales as H(z)^(4/3)

This insight is not refutable by choosing a different M_min or a different cosmology. It is a consequence of the virial theorem + spherical overdensity criterion.

---

### INSIGHT-4: The non-monotone ε(z) peak constrains the bridge to a specific topological class

**Source:** NR-001/002/003/004 synthesis  
**Confidence:** `[STRONG]`

Any valid bridge F_oP(z) → H_MULT(z) that reproduces ε must satisfy:
```
d/dz [F_oP(z) / Φ_0(z)] = 0  at some z* ≈ 0.40
```
(or equivalently, the relevant ratio peaks at z*)

For any monotone F_oP and monotone Φ_0 with the same sign of slope, this is impossible.  
Therefore: **at least one component of the bridge must be non-monotone**, OR the ratio of two monotone components must peak at z≈0.40.

**The only positive signal we have** (dN/dz, r=0.723) peaks near z=0.40–0.65 and is non-monotone. This is consistent with being the non-monotone component.

---

## Synthesis: What We Know About the Bridge (Eliminative)

```
MUST be true (by theorem or strong evidence):
  ✓ Bridge output ε(z) is non-monotone with peak near z=0.40
  ✓ Bridge involves at least 2 competing processes (from sign changes in α)
  ✓ Standard virial k_A ∝ H(z)^(4/3) — monotone — cannot be the sole non-monotone ingredient

PROBABLY true (from signal evidence):
  ~ The non-monotone ingredient is related to cluster formation rate (dN/dz signal r=0.723)
  ~ The mechanism is active predominantly in 0 < z < 2 (ε is small at z=5, uptick at z=8.5 uncertain)

CANNOT be:
  ✗ Any single-parameter monotone bridge (ruled out by 3 α sign changes)
  ✗ PS comoving density alone (monotone decreasing)
  ✗ Virial k_A alone (monotone increasing by theorem)
  ✗ Constant ε (4.7× variation rules out)

UNKNOWN (requires TJB Q1+Q2):
  ? The actual formula for k_A(z) the author uses
  ? The actual D_C:AB(z) schedule
  ? Whether Φ-normalization (M8-B forensic) carries the non-monotone structure
  ? Physical interpretation of the secondary rise at z≈1.5
```

---

## Next Insights to Pursue (if TJB answers Q1+Q2)

1. **Does author's k_A(z) scale as H(z)^(4/3)?**  
   If yes → it cannot be the non-monotone ingredient (INSIGHT-3 confirmed).  
   If no → the author uses a non-standard virial scaling (high value finding).

2. **Does Φ(z) normalization peak near z≈0.40?** (M8-B forensic)  
   If yes → the non-monotone structure is in the normalization, not the force.  
   If no → the non-monotone structure must be in F_oP itself.

3. **Does dN/dz (best signal, r=0.723) improve with a lag/smoothing?**  
   ε peaks at z=0.40; dN/dz peaks at z=0.65 for M_min=1e14. A lag of Δz≈0.25 suggests the bridge response is not instantaneous — plausible for a formation-rate proxy.

---

*INTERNAL_DIAGNOSTIC_ONLY · NOT_VALIDATION · NOT_REFUTATION*  
*Compiled 2026-06-13 from gates M8-A, M8-A-R1, M8-C, M8-D*
