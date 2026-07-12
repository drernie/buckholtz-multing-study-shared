# NR-013 — R011: beta_d/beta_q fitting does not beat the nested monopole baseline — REJECTED WITHIN IMPLEMENTATION

**Date:** 2026-07-13
**Verdict:** REJECTED WITHIN IMPLEMENTATION (tool-verified numeric scan + one
closed-form analytic limit)
**Branch:** R011 — the MULTING dipole/quadrupole cosmic-acceleration mechanism,
tested via `src/pearson_fit.py` against real MCXC/PSZ2 clusters and real Moresco
et al. 2022 H(z) data

---

## Claim (falsified)

Tuning `(beta_d, beta_q)` inside the implemented `F->H(z)` mapping
(`D=D0/(1+z)`) improves the Pearson correlation with real H(z) data relative to the
nested monopole-only model (`beta_d=beta_q=0`).

## Why falsified

| Test | Result | Evidence |
|------|--------|----------|
| Nested baseline `Q(eta_d=0,eta_q=0)` | 0.733359 (n=443) | `[VERIFIED-REAL]` zero free parameters beyond `D0`, which cancels |
| R011's original "grid-search optimum" (`beta_d=100, beta_q=3.24e7`) | 0.623517 (n=443) — below baseline | Reframed: `grid_search_pearson`'s own default `beta_d_log_range=(2.0,8.0)` (`src/pearson_fit.py:57,87`) structurally excludes `beta_d<100`, so this was a box-constrained local optimum, not global |
| True profile `r_prof(eta_d) = max` over eta_q, dense grid, `eta_d` up to 1e7 | never exceeds 0.733359 | max reached is 0.623517, the same plateau, for `eta_d >= 1.23e5` |
| Finer 300x300 grid near `eta_d=0` (checking for a missed overshoot) | max found = 0.733359 exactly, at `(0,0)` | no violation |
| Analytic `eta_q -> infinity` limit | `r_infinity = 0.623517498888...`, zero free parameters, proven `eta_d`-independent | matches the numeric plateau to 7 sig figs; the dipole term is analytically absent from this limit, not just practically negligible |
| Fine-tuning check (`eta_q` perturbed ±0.1%/1%/10% at the plateau) | `r` unchanged to 6 decimals | plateau is a stable degeneracy, not fine-tuned cancellation — but `F_q/F_m ~ 1e14` there, dipole numerically inert |
| Train(70%)/holdout(30%,seed=42), grouped by unique `cluster_id` | degraded but not collapsed in both splits (train 0.57 vs 0.73 monopole; holdout 0.70 vs 0.77 monopole) | 443/443 unique `cluster_id`, 0 duplicates — cluster-identity leakage excluded |

**Full computation passport (dataset hashes, code commit, exact command, parameter
bounds, validity policy, reference convention):**
`experiments/20260713-r011-beta-profile-nesting/decision.md`.

## Kill Analysis

**What this KILLED:**
- The strategy of rescuing the MULTING cosmological branch by fitting
  `(beta_d, beta_q)` — any value, however chosen — inside the currently implemented
  `F->H(z)` mapping. No configuration examined, scanned or analytically derived,
  beats the monopole.

**What this did NOT kill (survives):**
- All possible formulations of MULTING as a theory (only this implementation's
  bridge and fitting strategy are disfavored).
- A new, physically derived `F->H(z)` mapping (bottleneck #1) — untested, the
  actual open question.
- Eq.32 and IDM branches — no overlap, unaffected.
- The formal possibility of a narrow interior maximum between the scanned grid and
  the asymptote — excluded by every scan and limit computed, not by certified proof.

**Relaxation Map:**

| Variant | Changed assumption | Prediction | Status |
|---------|--------------------|-----------|--------|
| New physically-derived `F->H(z)` bridge | Replace the phenomenological `D=D0/(1+z)` hypothesis | Would change the objective itself, not just the search over it | Not tested (bottleneck #1) |
| Independent `(eta_d,eta_q)` constraint | From theory or a different observable, not this Pearson-r fit | Removes the free-fitting degeneracy | Not tested |
| Held-out dataset, genuine out-of-sample prediction | Different cluster sample, not re-fit on the same 443 | Tests generalization | Not tested |
| Certified global optimum | Interval arithmetic / certified optimization finds `Q>0.7334` | Would directly overturn this result | Not attempted |
| Different observable | non-monopole terms show a unique predictive advantage elsewhere | Sidesteps this specific H(z)/Pearson-r test | Not tested |

## Addendum — corrected chain (methodology lesson)

This result went through two self-caught errors before reaching this registered
form, both recorded as pearls in `pearl_registry/INDEX.md` (2026-07-13 entries):
1. An earlier sweep (docs/122 v3) silently fixed the quadrupole nuisance parameter
   `eta_q=0` instead of profiling it — producing a convincing but false "collapse"
   result, corrected in docs/122 v4.
2. The corrected version (v4/v5) cited a "grid-search optimum" (0.6235) without
   checking it against the nested monopole point, which is a mathematical
   requirement once the monopole is recognized as a special case of the full model
   — closed in docs/122 v5, with the origin of the plateau derived in closed form
   in v6.

## Forbidden use

Do NOT cite this result as a proof that `sup_{eta_d,eta_q} r(eta_d,eta_q) = Q(0,0)`
over the full continuous parameter space — that requires certified global
optimization, not attempted here. Do NOT cite this as a refutation of MULTING as a
theory — only this implementation's beta-fitting rescue strategy is disfavored.

## Correct next direction

Per the Relaxation Map: further beta_d/beta_q coefficient-fitting in this pipeline
has low expected value. The productive next step is a physically derived `F->H(z)`
bridge (bottleneck #1), not another fitting round — see
`docs/122_bottleneck_synthesis_cosmological_branch_verdict.md` for the full
synthesis this experiment formalizes.

---

*REJECTED WITHIN IMPLEMENTATION — tool-verified on [VERIFIED-REAL] MCXC/PSZ2 + Moresco+2022 data (n=443).*
*Full analysis: `experiments/20260713-r011-beta-profile-nesting/decision.md`.*
*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
