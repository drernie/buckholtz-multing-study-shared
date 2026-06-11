# M2-G4 Fisher Rank Identifiability Test

**Date:** 2026-06-11
**Verdict:** PASS (test executed in full) — identifiability result: **β-pair NON-IDENTIFIABLE (practical)**

## Status labels

- NOT_VALIDATION
- NOT_REFUTATION
- AUTHOR_PHYSICAL_BRIDGE_STILL_NEEDED
- AI_MEDIATED_BRIDGE_FOUND
- OUR_RECONSTRUCTION_IDENTIFIABILITY
- MCMC_BLOCKED
- CLAUDE_SPECIFIC_AI_MEDIATED_BRIDGE

## Purpose

This test asks whether hidden parameters (β_d, β_q, H_anchor, D(z) schedule) can be
identified from reported Table A1 / H_MULT outputs under the reconstructed
Claude-specific bridge. It is an identifiability audit of OUR reconstruction of ONE
AI service's implementation.

## Scope boundary

This is **not** an analysis of Dr. Buckholtz's author-confirmed physical model.
ChatGPT used an H ~ Ḋ/D-style approach; Gemini used force→acceleration. Three AI
services = three different bridges. Only the Claude-specific Φ-normalization
reconstruction is analyzed here.

## Input data

- `data/supplementary_extracted/claude_galaxy_cluster_parameters.csv` — 12 rows
  (z, m_A, k_A, r_A, D ranges → geometric/arithmetic midpoints), provenance AI_CHOICE.
- H_MULT reported column (Table A1 rows 1–12), provenance CLAUDE_OUTPUT.
- σ_H from H-data column.
- Code reused: `src/bridge_phi.py` (Φ math), `src/cluster_schedule.py` (loader) —
  both pre-existing from the parallel audit session.

Missing: author-confirmed cluster variables; author-confirmed bridge.

## Model analyzed

```
H²_MULT(z) = H²_anchor × Φ(z) / Φ(z_anchor)
Φ(z) = A_m − A_d + A_q
A_m = m_A/D², A_d = 2 k_A β_d r_A/D³, A_q = k_A² β_q² r_A²/D⁴
```

Implemented exactly as above via `bridge_phi.h_mult_from_params_list` (anchor = row 1, z=0).
Jacobian: central finite differences (rel step 1e-6), σ-weighted (Fisher convention).
Symbolic sympy rank was not required: numeric column norms are 9–13 orders below the
leading singular value, far beyond any symbolic-vs-numeric ambiguity.

## Context check (not a gate)

Reconstruction at Claude's own (β_d=4.5, β_q=18.0, H_anchor=73):
**RMS σ-distance to reported H_MULT = 14.1σ.** Our Φ-reconstruction does NOT
reproduce Claude's reported column — consistent with the prior finding that the
emitted numbers follow ~(1+z)^0.79 rather than any force-law computation.
(Evidence the bridge text and the emitted numbers are decoupled even within Claude.)

## Parameter scenarios

| Scenario | Parameters | Obs | Rank (num) | Rank (practical, 1e-8) | Cond # | Verdict |
|---|---|---:|---:|---:|---:|---|
| A | β_d, β_q | 12 | 2 | 2* | 4.7e3 | **FAIL (practical)** — both columns ~0 |
| B | β_d, β_q, H_anchor | 12 | 3 | **1** | 2.0e12 | **FAIL** — only H_anchor identifiable |
| C | β_d, β_q, α_D, H_anchor | 12 | 4 | **2** | 7.6e11 | **PARTIAL** — α_D & H_anchor identifiable; β-pair dead |
| D | β_d, β_q + 12 free D_i | 12 | — | — | — | **FAIL_BY_COUNTING** (14 params > 12 obs) |

\* Scenario A numeric rank 2 is meaningless in practice: see sensitivities below.

## Jacobian / Fisher results (σ-weighted)

Singular values:
- A: [3.45e-9, 7.37e-13]
- B: [1.48, 2.49e-9, 7.36e-13]
- C: [3.92e+1, 1.16, 1.88e-9, 5.14e-11]

Column norms (C): α_D = 3.9e+1, H_anchor = 1.6, **β_q = 4.1e-9, β_d = 5.3e-11**.

Max relative sensitivity (ΔH/H per 100% parameter change):
- **β_d: 5e-10 … 7e-10** (all scenarios)
- **β_q: 3e-7 … 7e-7**
- α_D: 4.5
- H_anchor: 1.0

Collinearity (C): β_q|α_D cosine = 0.861 — the residual β_q signal is largely
absorbed by the D-schedule exponent.

## β_d / β_q identifiability

- **Is β_d identifiable?** No. Practical sensitivity ~7e-10; no realistic data
  precision reaches it.
- **Is β_q identifiable?** No. ~7e-7 — also far below any plausible σ_H/H (~1e-2).
- **Separately identifiable?** Moot; neither is identifiable at all. (Their columns
  are not mutually collinear — cos 0.02–0.05 — so the failure is sensitivity, not degeneracy
  between them.)
- **Ratio/product only?** No: even joint directions have ~1e-9 singular values.
- **Practically unidentifiable due to near-zero sensitivity?** **Yes — this is the
  central finding.** With Claude's own cluster midpoints, the dipole and quadrupole
  terms are O(1e-3) and O(1e-6) of the monopole (consistent with the prior
  dominance-ratio test), so β variations cannot move H_MULT at any measurable level.

**Implication (provenance, not physics):** the values β_d=4.5, β_q=18.0 reported by
Claude as "chosen to minimize standard deviations" **could not in fact have been
constrained by such a fit** under this bridge — the objective is flat in β to one
part in ~1e7. This also explains the 3-service β divergence (0.78/4.5/4.25 etc.):
β is effectively a free label, not a fitted quantity, under all reconstructed bridges
of this family.

## D(z) / k_A(z) schedule identifiability

- Free per-row D_i (Scenario D): 14 params vs 12 observations (13 vs 11 after anchor
  normalization) → **non-predictive, structurally non-identifiable.** Any H(z) curve
  is exactly reproducible.
- Parametric D(z)=D0(1+z)^(−α_D) (Scenario C, OUR_RECONSTRUCTION): α_D **is**
  identifiable (sensitivity 4.5) and, with H_anchor, carries essentially **all** of
  the model's explanatory power. The "MULTING physics" (β-terms) carries none.
- **What would unlock β identifiability:** independent author-fixed cluster
  variables (m_A, k_A, r_A, D as functions of z with uncertainties), or regimes where
  dipole/quadrupole are not 1e-3 suppressed, or non-H(z) observables sensitive to the
  force law directly.

## w_eff independence check

w_eff is back-calculated from fitted/reported H_MULT (DERIVED_FROM_H_MULT). It adds
**zero** independent rows to the Jacobian; quoting it as support would double-count
the same information.

## Damage / overclaim guard

This result does **not** validate or refute MULTING. It constrains only what can be
inferred from Table A1 under one reconstructed AI-mediated bridge: namely, that the
table cannot pin down β_d/β_q (at ~1e-7 relative sensitivity), that the anchor and
the assumed D(z) schedule dominate, and that an author-confirmed physical bridge plus
author-confirmed cluster schedules remain the binding requirement for any real test.
I may be missing the intended bridge; author clarification is needed.

## Final verdict

**PASS** — test executed in full; honest identifiability result:
- β-pair: **practically non-identifiable** (FAIL) under Scenarios A–C;
- schedule layer (α_D, H_anchor): identifiable (PARTIAL capacity of the model);
- flexible schedule: structurally non-identifiable (FAIL by counting).

## Next recommended gate

**M7-A Eq31 mass-ratio toy-test** (no severe data/formula blocker found requiring M2 cleanup).

## Not-applicable inputs from the task brief

`reports/current_country_prediction_rows.jsonl`, `src/rules_baseline.py`,
`c12_strategic_autonomy_balancer_logic.md`, C13 gate — belong to a different project;
not present in this repo; ignored.
