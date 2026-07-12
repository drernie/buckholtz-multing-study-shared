# Decision — 20260713-r011-beta-profile-nesting

**Date:** 2026-07-13
**Status:** REJECTED WITHIN IMPLEMENTATION
**Evidence grade:** A (real MCXC/PSZ2 + real Moresco et al. 2022 H(z) data
[VERIFIED-REAL]; plus one closed-form analytic derivation)

## Computation passport

```
dataset:
  source: MCXC/PSZ2 cluster catalog (data/clusters_clean.csv) + Moresco et al. 2022
          cosmic-chronometer H(z) (data/hz_cc.csv)
  hash (clusters_clean.csv): 5fdda91fbc30482c   (sha256 of pandas hash, first 16 hex)
  hash (hz_cc.csv):          9a3af5f845c2f4a4
  n_raw = 1740
  n_used = 443            (after Ethermal_c2_Msun not-null AND z within hz_cc range)
  unique_cluster_id = 443 (0 duplicates in raw 1740-row catalog, verified)

code:
  implementation_commit: 483b5fe6d1d4288a0035634e8124a1d221656128 (src/pearson_fit.py
                          unchanged since 0453bb8, this experiment only reads it)
  experiment_commit: <filled at merge time by the commit that adds this folder>
  entrypoint: experiments/20260713-r011-beta-profile-nesting/artifacts/verify_r011_beta_profile.py
  exact command: python experiments/20260713-r011-beta-profile-nesting/artifacts/verify_r011_beta_profile.py
                 (run from repo root)

parameters:
  eta_d bounds swept: {0, 1e3, 1e4, 2.46e4, 1e5, 1.23e5, 2.46e5, 4.92e5, 1e6, 2.46e6, 1e7}
                       plus a finer 300x300 grid, eta_d in [0, 1e-2..1e5] log-spaced,
                       concentrated near eta_d=0
  eta_q bounds swept: log-spaced 2000 points in [1e-6, 1e7] per eta_d (main profile);
                       300 points in [0, 1e-6..1e3] for the fine near-zero grid
  spacing: log-uniform (np.logspace), except explicit 0 always included
  profiling method: for each eta_d, r_prof(eta_d) = max over the full eta_q grid of
                     r(eta_d, eta_q), subject only to the validity policy below (NOT
                     a minimal-feasibility boundary sweep -- that was v4's error, see
                     docs/122 v4 correction)

model:
  objective: scipy.stats.pearsonr(H_MULT(z), H_CC(z)) -> r, maximized
  baseline: Q(eta_d=0, eta_q=0) = 0.733359017698...
  validity policy: phi_i finite AND phi_i>0 AND 0<H_MULT_i<1e6 AND z_i within the
                    hz_cc linear-interpolation range
  reference convention: phi_ref = phi of the first cluster (lowest z) among those
                          with phi>0, after sorting by z ascending
  H_anchor = 73.0 (production default, src/pearson_fit.py)
  definition: eta_d = beta_d/D0, eta_q = beta_q/D0 (D0 cancels exactly from every
               ratio phi_i/phi_ref -- see PASS-A, docs/122 v3)

analytic result:
  lim_{eta_q -> infinity} phi_i/phi_ref = [(k_i r_i)^2(1+z_i)^4] / [(k_ref r_ref)^2(1+z_ref)^4]
    (independent of eta_d, eta_q, D0 -- zero free parameters, function of catalog data only)
  r_infinity = 0.623517498888019...  (computed directly from the template, no fit)

limitations:
  - no interval-arithmetic / certified global optimization; numeric grid + one exact
    analytic limit, not a proof over the full continuous (eta_d, eta_q) domain
  - independence of the 443 target observations from shared H(z) anchors and
    catalog-level systematics not separately established (cluster-identity leakage
    IS excluded: 443/443 unique cluster_id)
  - tests only this implementation's specific F->H(z) mapping (D=D0/(1+z)), not any
    other possible MULTING formulation or a relativistically-derived bridge
```

## Numerical results [OUR-RECONSTRUCTION]

### Nested baseline

| | r | n |
|--|---|---|
| Q(eta_d=0, eta_q=0) — monopole, zero free parameters | 0.733359 | 443/443 |

### R011's original "grid-search optimum" — reframed

| | r | n | note |
|--|---|---|---|
| beta_d=100, beta_q=3.24e7 (eta_d=1, eta_q=3.24e5) | 0.623517 | 443/443 | below Q(0,0), as required by nesting; was a box-constrained local optimum (`beta_d_log_range=(2.0,8.0)` excludes beta_d<100), not global — see claim.md A2 |

### True profile r_prof(eta_d) = max over eta_q

| eta_d | r_prof | n | eta_q @ max |
|---|---|---|---|
| 0 | 0.733359 | 443 | ~0 |
| 1.0e3 | 0.732700 | 443 | ~0 |
| 1.0e4 | 0.725794 | 443 | 1.51e-3 |
| 2.46e4 | 0.712500 | 443 | 2.84e-3 |
| 1.0e5 | 0.633332 | 443 | 9.41e-3 |
| 1.23e5 | 0.623517 | 443 | 2.23e5 |
| 2.46e5 | 0.623517 | 443 | 3.01e5 |
| 4.92e5 | 0.623517 | 443 | 4.31e5 |
| 1.0e6 | 0.623517 | 443 | 5.31e5 |
| 2.46e6 | 0.623517 | 443 | 7.17e5 |
| 1.0e7 | 0.623517 | 443 | 1.59e6 |

**No point exceeds `Q(0,0)=0.733359` anywhere on this grid.**

### Finer 300x300 near-zero grid (checking for a missed overshoot)

Maximum found across the entire fine grid: exactly `Q(0,0)=0.733359`, achieved only
at `eta_d=eta_q=0`. No violation found.

### Analytic limit

`r_infinity = 0.623517498888019` (zero free parameters), matching the numeric
plateau to 7 significant figures. Confirmed `eta_d`-independent at `eta_d in {0, 1e4,
1e6, 1e8}` (all four give `r=0.623517` at `eta_q=1e8`).

### Fine-tuning check

Perturbing `eta_q` by ±0.1%/1%/10% around the profile-optimal point at
`eta_d=2.46e5`: `r` unchanged to 6 decimal places at every level. The plateau is a
stable degeneracy, not fine-tuned cancellation — but `F_q/F_m ~ 1e14` there, so the
dipole is numerically/analytically inert (a quadrupole-only fit in disguise).

### Train/holdout (grouped by unique cluster_id, seed=42)

| Split | n | dipole+quadrupole (eta_d=2.46e5, near F_d/F_m~1) r | monopole r |
|---|---|---|---|
| train (70%, n=310) | 310/310 valid | 0.5699 | 0.7292 |
| holdout (30%, n=133) | 132/133 valid | 0.7024 | 0.7667 |

Degraded but not collapsed in both splits; leakage excluded (443/443 unique
`cluster_id`, 0 duplicates in the raw 1740-row catalog).

## Verdict

**REJECTED WITHIN IMPLEMENTATION.**

The claim under test — tuning `(beta_d, beta_q)` inside the currently implemented
`F->H(z)` mapping improves the fit to real H(z) data relative to the nested
monopole baseline — fails against every configuration examined: the dense scanned
2D region, the finer near-zero grid, and the closed-form `eta_q -> infinity` limit.

## Kill Analysis

**What was killed (this experiment's scope):**
The specific strategy of rescuing the MULTING cosmological branch by fitting
`(beta_d, beta_q)` — however large or small, however chosen — inside the currently
implemented `F->H(z)` mapping (`D=D0/(1+z)`, this project's phenomenological
hypothesis, not TJB-derived). Conditions: real 443-cluster MCXC/PSZ2 sample, real
Moresco+2022 H(z), Pearson r as objective, the validity/reference conventions stated
in the computation passport above.

**What was NOT killed:**
1. All possible formulations of MULTING as a theory — only this implementation's
   `F->H(z)` bridge and beta-fitting strategy.
2. A new, physically derived `F->H(z)` mapping (bottleneck #1) — untested here.
3. A relativistic or N-body treatment of the same mechanism — out of scope.
4. Eq.32 and IDM as separate branches — unaffected, no overlap with this claim.
5. The formal possibility of a narrow interior maximum between the scanned grid and
   the `eta_q->infinity` asymptote, not excluded by certified proof — only by every
   scan and closed-form limit computed so far (see claim.md A5).
6. `beta_d = beta_q = 0` (pure monopole) as a *description* of the cluster data — it
   remains the best-performing configuration found, r=0.7334.

**Important interpretive note:** REJECTED WITHIN IMPLEMENTATION is a narrower verdict
than "MULTING is falsified." It says: for this specific reproducible pipeline, no
amount of coefficient-tuning recovers or exceeds the monopole baseline. It does not
bound what a differently-derived `F->H(z)` bridge could do.

## Relaxation Map

Reopening this branch requires at least ONE of the following NEW elements (not a
retry of coefficient-fitting with the same mapping):

| # | New element | Why it would matter |
|---|---|---|
| 1 | A physically derived `F->H(z)` mapping, replacing the phenomenological `D=D0/(1+z)` hypothesis | Changes the objective function itself, not just the parameters searched over it |
| 2 | An independent constraint on `(eta_d, eta_q)` from a source other than this Pearson-r fit (e.g. a theoretical bound, or a different observable) | Removes the free-fitting degeneracy this experiment exploited |
| 3 | A new dataset with genuinely held-out prediction (not re-fit on the same 443 clusters) | Tests generalization, not just in-sample correlation |
| 4 | A certified point with `Q > 0.7334`, found via interval arithmetic or certified global optimization | Would directly overturn this experiment's central finding |
| 5 | A different observable where the non-monopole (dipole/quadrupole) components demonstrate a *unique* predictive advantage the monopole cannot replicate | Sidesteps the specific H(z)/Pearson-r test this experiment used |

Without at least one of these, do not re-attempt beta_d/beta_q fitting in this
pipeline — it revisits ground already covered by this experiment plus the docs/122
v3-v6 chain it formalizes.

## Skeptic concerns (pre-answered, carried over from docs/122 v3-v6 external review)

**Concern 1:** "Was `eta_q` actually profiled at every `eta_d`, or fixed?"
→ ADDRESSED. The original v3 sweep fixed `eta_q=0` — a real bug, corrected in v4/v5.
This experiment's profile (`r_prof` table above) genuinely maximizes over a dense
`eta_q` grid at each `eta_d`, not a fixed or minimal-feasibility slice.

**Concern 2:** "If `(0,0)` is nested in the full model, doesn't `max(r) >= r(0,0)`
have to hold — and doesn't the reported `r=0.6235` 'optimum' violate that?"
→ ADDRESSED. `r=0.6235 < r(0,0)=0.7334` — no violation. The apparent tension was
caused by `grid_search_pearson`'s own default box (`beta_d in [1e2,1e8]`) excluding
the nested point, not by a computational error. Stated explicitly now (claim.md A2).

**Concern 3:** "Is the large-`eta_q` plateau fine-tuned cancellation, or a stable
regime?"
→ ADDRESSED. Perturbation test (±0.1%/1%/10%) shows `r` unchanged to 6 decimals —
stable, not fine-tuned. But physically empty for the dipole question (`F_q/F_m ~
1e14`, dipole numerically inert).

**Concern 4:** "Does the holdout split actually establish independence?"
→ PARTIALLY ADDRESSED. Cluster-identity leakage is excluded (443/443 unique
`cluster_id`). Independence from shared H(z) anchors and catalog-level systematics is
NOT separately established — flagged as an open limitation (see computation
passport), not claimed resolved.

**Concern 5:** "Is `sup_{eta_d,eta_q} r(eta_d,eta_q) = r(0,0)` proven for the full
continuous domain?"
→ NOT ADDRESSED, explicitly. This requires certified/interval-arithmetic global
optimization or a monotonicity proof, neither attempted here. The defensible claim is
scoped to what was scanned and to the one closed-form limit derived (see Verdict).

## Cross-references

- Full narrative history of how this result was reached (v2 through v6, including
  the two corrected errors along the way): `docs/122_bottleneck_synthesis_cosmological_branch_verdict.md`
- Canonical R011 status block: `facts.json` (R011.numbers.r011_v5_v6_canonical_status_2026_07_13)
- Methodology pearls from this chain: `pearl_registry/INDEX.md`, entries dated
  2026-07-13 (nuisance-parameter profiling; nesting-inequality gate; analytic-limit
  technique)
