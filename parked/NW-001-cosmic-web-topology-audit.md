# NW-001 — Cosmic Web Topology as MULTING Audit Upgrade

**Date:** 2026-06-23
**Verdict:** ARCHIVE (parked) — valid core, blocked by two prerequisites.
**L0 (EstimandOps):** Descriptive → Predictive (correlational). **NOT causal** — cannot infer
"topology participates in cluster interaction" without confounder control.
**Score:** 4/10 as "start now", 7/10 as "parked roadmap item".

---

## Proposal (one line)

Apply cosmic-web topology methods (DisPerSE / NEXUS / T-web / graph centrality) to test whether
MULTING residuals correlate with large-scale-structure topology rather than pair separation.

## Component scoring

| Component | Score | Rationale |
|---|--:|---|
| Epistemic hygiene (dropped "universe-brain" metaphysics) | 9 | 85–90% metaphysics correctly discarded |
| Network/cosmic-web methods as mature field | 8 | DisPerSE, NEXUS, T-web, graph centrality are real science |
| Falsifiable core ("topology vs pair-distance") | 7 | Concrete, testable in principle |
| fσ8 → cosmic web chain (reviewer ⭐⭐⭐⭐⭐) | 4 | Overrated. r≈0.85 (n=10, z≤5); fσ8 IS structure growth → partly tautological |
| Applicability to audit right now | 3 | Blocked: no per-cluster MULTING observable + BETA-1 HOLD |
| As parked roadmap item | 6 | Worth recording, not running |

## Three holes the reviewer missed (verified)

1. **Unit-of-analysis mismatch (fatal for current form).** ε(z) is a GLOBAL function of redshift
   (from H(z)); cosmic-web topology is LOCAL (per cluster). Correlating them requires a
   **per-cluster MULTING residual φ_i** which **does not exist** in the repo `[VERIFIED-ABSENT]`
   (grep over code/ src/ scripts/ returns only fit coefficients and astro merger rates, not a
   MULTING residual). Defining φ_i is itself blocked by the β-blocker.
2. **Mass ↔ topology ↔ z confounding.** Web density correlates strongly with cluster mass, T_X, z.
   "Topology explains variance better than z" requires **partial correlation controlling M500** —
   else "topology beats z" is an artifact of topology ≈ mass proxy.
3. **MULTING has no topological term `[VERIFIED]`.** F_oP = F_m − F_d + F_q is PAIRWISE (depends on
   r between two bodies); no Lagrangian (blocker G3). So MULTING cannot *predict* which topological
   dependence it should produce → 5 network metrics × correlation hunting = multiple-comparisons / p-hacking risk.

---

## Parked Pearl fields (FL Parked Pearl Rule)

| Field | Content |
|---|---|
| **Original branch** | Cosmic-web topology correlates with MULTING residuals → topology as physical driver |
| **What was killed** | The "start now" formulation: correlating GLOBAL ε(z) with LOCAL topology — unit mismatch; no φ_i exists |
| **What survives** | (1) Epistemic hygiene method (drop metaphysics, keep falsifiable core); (2) cosmic-web toolchain is mature & reusable; (3) the partial-correlation-by-mass discipline is a transferable audit technique |
| **Revival Condition** | (a) β resolved by TJB (unblocks φ_i definition) **OR** (b) a per-cluster MULTING residual φ_i is independently defined and computed |
| **Related future gates** | BETA-1 HOLD (docs/115); G3 Lagrangian; any per-cluster observable work |
| **Forbidden use** | Do NOT cite NW-001 as evidence that topology participates in MULTING interaction. Do NOT claim "cosmic web confirms MULTING." It is correlational, descriptive, and confounded by mass until φ_i + partial correlation exist. |

## Mandatory protocol if revived

1. **Define φ_i first** (per-cluster MULTING residual) — without it there is nothing to correlate.
2. **Partial correlation controlling M500** is the FIRST step, not an option — else result = mass proxy.
3. Pre-register the single network metric + hypothesis (avoid 5-metric hunting).

---

*ARCHIVE — not a null result. Revisit only when Revival Condition is met.*
*Cross-ref: this is the same confounder lesson as the dipole hypothesis-lab (D(z)/mass proxy).*
