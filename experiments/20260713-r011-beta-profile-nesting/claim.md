# Claim — R011 beta_d/beta_q Profile: Nested-Model Test Against the Monopole Baseline

## Hierarchy

R011 (MULTING dipole/quadrupole cosmic-acceleration mechanism, cluster-scale
`phi = m_A/D^2 - 2*beta_d*k_A*r_A/D^3 + (beta_q*k_A*r_A)^2/D^4`, `D=D0/(1+z)`)
  └── R011-original: grid_search_pearson found "optimum" r=0.6235 at beta_d=100,
      beta_q=3.24e7 — cited as evidence the full model underperforms the monopole
  └── **This experiment (docs/122 v3-v6 chain): is that "optimum" actually the best
      the full model can do, once the nested monopole point (eta_d=eta_q=0) and a
      genuine profile over the nuisance parameter eta_q are both checked properly?**

## Motivation

External review of an earlier synthesis (docs/122) caught, in sequence:
1. (v3->v4) the first "does any eta_d work" sweep held eta_q fixed at 0 — not a
   profile, a dipole-only slice. The resulting "collapse" was real for that slice,
   over-generalized in prose to the full model.
2. (v4->v5) even after fixing that, the claim "grid-search optimum r=0.6235 is what
   other branches converge toward" was never checked against the nested baseline
   `Q(eta_d=0, eta_q=0)` — a mathematical requirement, since the monopole is a
   special case of the full model.
3. (v5->v6) the numeric plateau at r=0.6235 for large eta_q was observed but not
   derived — could it be a resolution artifact, or a real, provable limit?

This experiment is the canonical, standalone registration of the resolved chain,
independent of the docs/122 narrative history.

## FL Zero-Signal Gate (Step -5)

- Entity: real MCXC/PSZ2 cluster catalog (443 clusters after H(z)-range filtering)
  cross-matched against real Moresco et al. 2022 cosmic-chronometer H(z) data
  [VERIFIED-REAL]
- Falsifiable predicate: some (eta_d, eta_q) configuration of the implemented
  dipole+quadrupole model improves Pearson r against real H(z) data relative to the
  nested monopole-only baseline (eta_d=eta_q=0)
- Measurable outcome: `r(eta_d, eta_q)` vs `Q(0,0)=0.7334`, computed directly via
  `src/pearson_fit.single_pearson` — PASS if any tested/derived point exceeds
  `Q(0,0)`, FAIL if none does

Gate passes: all three fields specified. Proceed to claim.

## Falsifiable Claim (FL Step 0)

**Main claim (the one being tested):** tuning `(beta_d, beta_q)` within the
implemented `F->H(z)` mapping demonstrates improved Pearson correlation with real
H(z) data relative to the nested monopole-only model, in at least one of: the dense
scanned 2D `(eta_d, eta_q)` region, the near-zero fine grid, or the closed-form
`eta_q -> infinity` limit.

**Reparameterization sub-claim (PASS-A, not falsified by this experiment — see
Assumptions):** raw `beta_d`/`beta_q` are not independently identifiable; only
`eta_d=beta_d/D0`, `eta_q=beta_q/D0` are observable, since
`phi = (1/D0^2)*Phi(eta_d, eta_q; data)` exactly (proven analytically, confirmed to
14 significant digits).

## Pre-registered criteria

| Outcome | Verdict | Implication |
|---|---|---|
| Any tested/derived `r(eta_d,eta_q) > Q(0,0)=0.7334` | PASS — main claim survives | beta-tuning strategy viable, resume fitting |
| No tested/derived point exceeds `Q(0,0)`, and the `eta_q->infinity` limit is derived in closed form as data-only (no free parameters) | REJECT WITHIN IMPLEMENTATION | beta-tuning strategy disfavored; need new `F->H(z)` physics, not more fitting |

## Minimum Testable Hypothesis (FL Step 1)

1. Compute `Q(0,0)` directly (monopole-only, zero free parameters beyond `D0`,
   which cancels).
2. Compute `r_prof(eta_d) = max_{eta_q: phi_i>0 for all i} r(eta_d,eta_q)` via a
   dense log-grid (2000 points) across a wide `eta_d` range, plus a finer 300x300
   grid concentrated near `eta_d=0` where an overshoot above `Q(0,0)` would be most
   plausible if a coarser grid missed one.
3. Derive `lim_{eta_q->infinity} r(eta_d,eta_q)` analytically and confirm the
   closed-form result matches the observed numeric plateau, at high precision, and
   is provably independent of `eta_d`.
4. Check whether the plateau is fine-tuned (sensitive to small `eta_q`
   perturbations) or a stable degeneracy.
5. Check train(70%)/holdout(30%, seed=42) grouped by unique `cluster_id` for
   leakage and reproducibility of the corrected (non-collapsing) profile.

## Assumptions (Claim Entropy)

| # | Assumption | Testable? | Evidence |
|---|-----------|-----------|---------|
| A1 | `beta_d`, `beta_q` individually unidentifiable; only `eta_d=beta_d/D0`, `eta_q=beta_q/D0` observable | [VERIFIED] | Analytic derivation + 14-digit numeric confirmation, docs/122 v3 |
| A2 | `grid_search_pearson`'s default `beta_d_log_range=(2.0,8.0)` structurally excludes `beta_d<100`, hence excludes the nested baseline point | [VERIFIED-CODE] | `src/pearson_fit.py:57` (default param) and `:87` (`bd_vals = np.logspace(beta_d_log_range[0], beta_d_log_range[1], n_pts)`) |
| A3 | 443/443 unique `cluster_id` in the filtered dataset, 0 duplicates in the raw 1740-row catalog | [VERIFIED] | direct pandas check, this experiment's artifact |
| A4 | The `eta_q -> infinity` limit is independent of `eta_d` | [VERIFIED-ANALYTIC] | ratio `phi_i/phi_ref` cancels `eta_d`, `eta_q`, `D0` entirely in that limit; confirmed at 4 `eta_d` values |
| A5 | No certified/interval-arithmetic proof exists that `sup_{eta_d,eta_q} r <= Q(0,0)` over the FULL continuous domain | [ACKNOWLEDGED LIMITATION] | not attempted in this experiment; would require a different toolchain |

**Claim entropy:** 1 (only A5 remains a genuine open gap; A1-A4 are closed)

## Counterfactual Frame

"In what world is the main claim (beta-tuning beats monopole) true?"
→ A world where the implemented `F->H(z)` bridge, despite being only a
  phenomenological hypothesis (not derived from TJB's action/field equations — see
  the G1 blocker noted in `src/pearson_fit.py`'s own docstring), happens to admit a
  dipole/quadrupole configuration that fits real cluster data better than a bare
  inverse-square monopole term.

Independent changes needed for the main claim to be true:
1. A configuration exists in the dense scanned region beating `Q(0,0)` — not found.
2. The `eta_q->infinity` asymptote exceeds `Q(0,0)` — proven false in closed form
   (converges to 0.6235, strictly below 0.7334).
3. A narrow, un-scanned interior maximum exists between the grid and the asymptote
   — not excluded by proof, only by every scan and limit computed (see A5).

All three would need to hold for the main claim to survive; (1) and (2) are already
closed against it.

## Status

**REJECTED WITHIN IMPLEMENTATION (2026-07-13).** See `decision.md` for the full
computation passport, numerical results, Kill Analysis, and Relaxation Map.
