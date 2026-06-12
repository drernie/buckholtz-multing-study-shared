# NR-004 — MAVS Virial+PS Insufficient (M8-D)

**Date:** 2026-06-13  
**Gate:** M8-D  
**Verdict:** REJECT  
**Commit:** 9100b0a  
**Safety:** M8_D_MAVS · OUR_RECONSTRUCTION · CONDITIONAL_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION · AUTHOR_SCHEDULE_NEEDED · <HYPOTHESIS>

---

## What Was Tested

Minimal Assumption Virial Schedule (MAVS) — 4 components derived from first principles:

- **k_A(z)** = G·M / r_vir(z)² — virial theorem (σ_v² = G·M/r_vir)
- **r_vir(z)** — overdensity criterion M = (4π/3)·200·ρ_crit(z)·r_vir³
- **r_A(z)** = n(>M_min, z)^(−1/3) — mean comoving separation (Press-Schechter)
- **r_P(z)** = r_A(z) / (1+z) — mean physical separation
- **D_C:AB(z)** = r_A(z) — minimal assumption (cluster-cluster distance = mean separation)

Tested at 3 M_min variants: 1e14, 5e14, 2e15 M_sun. No FLRW H(z) fitting. No power-law fit to Table A1.

---

## Why It Failed

| Component | Behavior | Pearson r vs ε | Peak z |
|-----------|----------|----------------|--------|
| k_A | Monotone increasing (∝ H(z)^(4/3)) | −0.462 | z=8.5 (all M_min) |
| r_A | Monotone increasing | −0.257 to −0.555 | z=8.5 |
| r_P | Dominated by PS divergence | −0.257 to −0.600 | z=8.5 |
| D_C:AB | = r_A, same | −0.257 to −0.555 | z=8.5 |

Best positive Pearson r across all: **−0.2573** (all anti-correlated with ε).

**Root cause:** k_A = G·M/r_vir² = G·M · [(4π/3)·200·ρ_crit(z)]^(2/3) / M^(2/3)  
= const · M^(1/3) · ρ_crit(z)^(2/3) ∝ H(z)^(4/3).  
Since H(z) is monotone increasing with z, k_A is **monotone by theorem**. It cannot peak at z=0.40.

---

## Mechanistic Insight

**[INSIGHT-3] Standard virial self-similar scaling predicts k_A ∝ H(z)^(4/3) — monotone by construction.**

This is not a numerical result — it is a **theorem** derivable from dimensional analysis + overdensity criterion alone. It holds for any cluster mass threshold.

**Therefore:**
- The author's k_A(z) schedule is **not** derived from standard virial self-similar scaling, OR
- The bridge involves k_A in a way that is not simply proportional to the virial value (e.g., a ratio or difference that cancels the monotone trend), OR
- The relevant quantity is not k_A at all, but something else that peaks at z≈0.40

**[INSIGHT-4] The non-monotone ε(z) structure constrains the author's bridge to a specific class.**

For any bridge F_oP(z) → H_MULT(z) to reproduce ε with primary peak at z≈0.40:
- F_oP must either peak at z≈0.40, OR
- The normalization Φ(z) must peak at z≈0.40 (canceling a monotone F_oP), OR
- The ratio F_oP / Φ_0 must peak at z≈0.40

None of these are achievable with standard virial + Press-Schechter applied directly.

**[INSIGHT-5] Best empirical signal so far: dN/dz (M8-C Model B, r=0.723).**

The cluster formation rate dN/dz peaks at z=0.40–0.65 for M_min=1e14–5e14. This is the only component in any tested gate that produces a positive correlation with ε and a peak location near the ε primary peak. If the bridge is connected to cluster physics, it is more likely connected to the formation rate (or a closely related quantity) than to the energy scale of individual clusters.

**What NOT to retry:**
- Any bridge where the key function is derived from k_A = G·M/r_vir² alone
- Any single-parameter monotone schedule
- Any approach that treats comoving cluster density n(>M, z) as the primary variable

**What to try IF TJB provides Q2 answer:**
- Verify whether author's k_A(z) is consistent with virial self-similar OR uses a different mass-dependence
- Check if D_eff(z) schedule matches dN/dz shape
- Test whether Φ-normalization itself is the non-monotone component (M8-B forensic)

---

## Scope

`CONDITIONAL_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED`  
MAVS is our construction from standard physics. We do not claim this is what the author uses.  
The mechanistic insights are constraints on ANY viable bridge, not refutation of MULTING.
