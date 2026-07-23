# docs/135 — Audit 3: Independent End-to-End Reproduction + Fair Model Comparison

**Date:** 2026-07-23 (precision-revised same day after user's two-pass adversarial review)
**Origin:** third of the user's three priority audits (docs/133=Audit 1, docs/134=Audit 2).
Executed via boyko-agent, coordinator-reproduced. **This document was substantially revised
after the user read the full text (not just the summary) and found real problems the summary
had hidden** — see "Revision log" below. Treat this as the authoritative version.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

## Revision log (why this version differs from the first draft)

The first draft blended several non-comparable statistical objects into one table and one
verdict, which — even with `n/a` cells — visually implied a completed model-ranking that was
never actually run. The user's adversarial re-read caught this and seven other precision
problems. Per Surgery Log discipline (rules/perelman-audit.md), each fix is logged with what it
retracts:

| # | Old claim | Problem | New status |
|---|---|---|---|
| 1 | Single unified table mixing χ²/AIC/BIC (27 CC) with Pearson r (443 clusters) | Different data, targets, metrics, sample sizes, likelihoods — a single table implies one ranking | Split into **Table A** (CC likelihood) and **Table B** (cluster pipeline), see below |
| 2 | MULTING full labeled `η-only` free params | β_d=100, β_q=3.24e7 were grid-selected on the same data — not free | Relabeled: `η fitted; β_d, β_q data-selected hyperparameters` |
| 3 | "Full model r=0.6235 worse than monopole r=0.7334" reported as a plain finding | If full is nested in monopole (β=0 recovers it exactly), an optimized full model cannot score worse than monopole — this needed an actual check, not an assumption | **Re-checked this session, P0 section below** — resolves cleanly, no violation, but the "grid optimum" label was imprecise. **Already established more rigorously by `null_results/20260713-nr013-r011-beta-profile-nesting.md` (2026-07-13, closed-form limit + train/holdout) — this session's check is a same-day confirmation, not a new finding; see P0 section's correction note** |
| 4 | "MULTING cannot be evaluated on 27 CC points physically" | Overstates a specification gap as a physical impossibility | "No population-level mapping to a unique H_MULT(z) has been specified yet" |
| 5 | "Independently reproduced" (R011 numbers) | Coordinator re-ran the *same* script/repo/data — this is repeatability, not independent reimplementation | Split: `COORDINATOR-REPRODUCED: YES` / `INDEPENDENT REIMPLEMENTATION: NOT DONE` |
| 6 | "Three independent audits converge" | All three share the same repo, same φ definition, same data, same coordinator workflow | "Methodologically distinct but dependency-correlated audits converge on the same bottleneck" |
| 7 | w=-1.889±0.925 (train split) cited as evidence of "fragility" | One seed (42) is an observation, not a distribution | `w INSTABILITY: SUGGESTED (1 seed)` / `DISTRIBUTION: NOT MEASURED` |
| 8 | χ²=12.81 for ΛCDM presented without comment | χ²/ν≈0.51 (25 dof) is low; depends on diagonal-only error model | Flagged explicitly: `ILLUSTRATIVE DIAGONAL-ERROR LIKELIHOOD, no covariance matrix` |

---

## Correction to this audit's own planning (retained from the first draft, still valid)

When this audit was scoped, the plan cited R011's stored `AIC_LCDM=16.8` and `AIC_MULTING=19.3`
as if directly comparable numbers already sitting in facts.json. **This framing was imprecise**:
MULTING's φ(z) depends per-cluster on M500/R500/E_thermal, not on z alone (Q006 — no continuous
MULTING H(z) exists) — so it never had a genuine 27-CC-point likelihood the way ΛCDM does, and
R011's `AIC_MULTING=19.3` was computed on a different footing (a Fisher-z/AIC proxy over the
443-cluster r-value, not the same χ²-on-27-points basis ΛCDM's 16.8 uses).
```
OLD ΛCDM–MULTING AIC COMPARISON — INVALIDATED
```

---

## Table A — CC likelihood (27 cosmic chronometers, same data, same likelihood)

| Model | n | k | χ² | AIC | BIC |
|---|--:|--:|--:|--:|--:|
| **ΛCDM** (H0, Ωm) | 27 | 2 | 12.81 | **16.81** | **19.40** |
| **wCDM** (H0, Ωm, w) | 27 | 3 | 12.81 | 18.81 | 22.70 |
| **MULTING** | — | — | NOT TESTABLE | — | — |

`Fits:` ΛCDM H0=68.77±2.27, Ωm=0.317±0.042. wCDM H0=68.38±5.00, Ωm=0.314±0.054, w=−0.959±0.464.
`Error model:` diagonal quoted CC errors only, **no covariance matrix** — χ²/ν≈12.81/25≈0.51 is on
the low side for 25 dof; flagged here rather than left silent. If Moresco+2022's points carry
non-trivial covariance, AIC/BIC here should be read as **illustrative-diagonal-error**, not final.
`Why MULTING is "NOT TESTABLE" here, not "n/a":` φ is not a function of z alone (depends
per-cluster on M500, R500, E_thermal — Q006), so it has no likelihood on these 27 points at all.
This is a specification gap, not a claim that no such likelihood could ever exist (see P0 section).

## Table B — cluster pipeline (443 real MCXC/PSZ2 clusters, common metric = Pearson r)

| Model | Objects | Metric | Train | Holdout (70/30, seed=42) |
|---|--:|---|--:|--:|
| ΛCDM (shape only, H0-invariant) | 443 | Pearson r | 0.8796 | — |
| wCDM (shape only) | 443 | Pearson r | 0.8811 | — |
| MULTING monopole (β=0) | 443 | Pearson r | 0.7334 | 0.7087 |
| MULTING full (β_d=100, β_q=3.24×10⁷ — R011's *restricted-grid* optimum) | 443 | Pearson r | 0.6235 | 0.6162 |
| MULTING full at TJB's own Table A1 values (β_d=4.5, β_q=18.0) | 443 | Pearson r | **0.6234** | not re-split |

Table A and Table B are **not the same likelihood** and must not be read as one ranking. Table B's
r is a correlation metric — it does not capture absolute calibration, bias, heteroscedastic
errors, or parameter count. It answers "is the shape reproducible," not "which model the data
prefer" in a likelihood sense.

**Effective complexity, stated honestly:** MULTING full is not free — β_d, β_q were selected via
grid search on this same 443-cluster set. Correct accounting: `η fitted (via curve normalization);
β_d, β_q data-selected hyperparameters` — three effective tuned quantities, not one.

---

## P0 — Nesting invariant test (run this session, per user's flagged concern)

**Correction (added after cross-checking docs/122, post-hoc — this should have been checked
first):** this test duplicates, and does not supersede, prior work. `null_results/20260713-nr013-r011-beta-profile-nesting.md`
(verdict: REJECTED WITHIN IMPLEMENTATION, 2026-07-13) already established this exact result ten
days earlier, more rigorously — including a closed-form analytic `η_q→∞` limit (not just a
numeric scan) and a train/holdout split, formalized at `experiments/20260713-r011-beta-profile-nesting/decision.md`
and narrated in `docs/122_bottleneck_synthesis_cosmological_branch_verdict.md` (v5/v6). Per the
Adaptive Iteration Branch Rule (falsification-ladder.md), `null_results/INDEX.md` should have been
grepped for "nesting" before writing a new script — it was not. The numbers below are a **same-day,
same-repository re-derivation** (Independent Verification Strength Ladder: "same model, isolated
context" — Weak-Medium, not independent reimplementation), useful as a sanity cross-check and for
one incremental data point (the TJB-literal-pair number), not as a new finding. NR-013 is the
citable source; treat the section below as confirmation, not discovery.

**The concern, stated precisely:** φ(β_d, β_q) = M500/D² − 2β_d·k_A·R500/D³ + (β_q·k_A·R500)²/D⁴
reduces to the pure monopole term M500/D² exactly when β_d=β_q=0 — the full model is nested in
the monopole model by construction. If so, an optimized full model cannot score worse than
monopole on the same objective (max over a superset of parameters is ≥ max over the subset). But
R011 reports r_full=0.6235 < r_mono=0.7334 for its "full-grid optimum." That needed an actual
check, not an assumption in either direction.

**Test run** (`scratchpad/nesting_invariant_check.py`, reusing `src/pearson_fit.py`'s own
`single_pearson`/`grid_search_pearson` on the real 443-cluster set — not a new formula):

1. **Exact identity check:** `single_pearson(β_d=0, β_q=0)` → **r=0.733359**, matching R011's
   0.7334 to 4 digits. Confirms φ(0,0) is numerically the monopole term, as the algebra predicts.
2. **1D scan, β_d alone (β_q=0), 1e-3→1e8 log-spaced:** r stays flat at 0.7334 up to β_d≈10³,
   then decays slowly, crashing only past β_d≈10⁶–10⁷.
3. **1D scan, β_q alone (β_d=0), 1e-3→1e8 log-spaced:** r falls fast — 0.7334 at β_q≲0.08, down
   to 0.6237 by β_q≈6.7, **and then plateaus at exactly r=0.6235 from β_q≈20 all the way to
   β_q=1e8.** (Mechanism: once the quadrupole term dominates φ, it rescales φ by a factor that
   cancels in a Pearson correlation — further increases in β_q change nothing.)
4. **r at TJB's own Table A1 values (β_d=4.5, β_q=18.0):** **r=0.623443** — essentially identical
   to R011's restricted-grid "optimum" of 0.6235 at (100, 3.24×10⁷). TJB's own literal published
   coupling already sits in the saturated-bad regime.
5. **Extended 2D grid, β_d,β_q ∈ [1e-3, 1e8] (40×40 log-spaced, includes near-zero):** global max
   is **r=0.7334 at (β_d,β_q)≈(10⁻³,10⁻³)** — i.e., at the boundary approaching zero coupling.
6. **R011's original restricted grid reproduced exactly:** [1e2,1e8]² → r=0.6235 at
   (100, 3.24×10⁷), matching the stored value.

**Verdict on the nesting concern: NO VIOLATION, but the "full-grid optimum" label was imprecise.**
R011's grid search never included β near zero (its own range started at β=10²), so it reported
the best point *within a restricted region*, not the true unconstrained optimum. The true global
optimum over all β≥0 sits at β≈0 — i.e., **the model's own correlation objective is maximized at
zero coupling, not away from it.** This does not weaken the original qualitative finding — it
sharpens it: adding any dipole/quadrupole coupling strength actually explored in this project
(TJB's own 4.5/18.0, or R011's restricted-grid 100/3.24×10⁷) reduces the correlation relative to
pure monopole, and the objective's genuine maximizer is the no-coupling limit itself.

**Corrected statement to use going forward, replacing "full-grid optimum":**
> Within the tested coupling range (from TJB's own Table A1 values up through the grid search's
> upper bound), every explored (β_d, β_q) reduces the 443-cluster Pearson r relative to the pure
> monopole limit. An extended search confirms the correlation objective's true unconstrained
> maximum over β_d,β_q≥0 is the monopole limit itself (β→0), not a restricted-grid artifact.

---

## Prediction vs. fit — split precisely

- **Train/holdout predictive evaluation — PRESENT.** The 70/30 splits (seed=42) on both the CC
  points and the cluster set are genuine out-of-sample checks; they only confirm the in-sample
  ranking (no model improves out-of-sample), which is itself informative.
- **Independent theory-first prediction — ABSENT.** No model here predicts H(z) from parameters
  fixed independently of the data being scored. ΛCDM/wCDM: H0/Ωm(/w) fit to all 27 CC points.
  MULTING monopole: H0=73, D0=100 Mpc set to the data scale. MULTING full: β_d, β_q are
  grid-selected on the same 443 clusters being scored.
- These are two different senses of "prediction" and should not be collapsed into one negative
  statement ("nothing here is a genuine prediction") — the holdout numbers are real evidence of a
  specific, narrower kind.

## wCDM constraint quality — anti-cherry-pick finding (retained, still valid)

wCDM's extra parameter is unpaid-for: Δχ²=0.0034 (best-fit w=−0.959≈−1 collapses onto ΛCDM), so
ΔAIC=+2.00 is essentially the bare 2Δk penalty. w's own uncertainty (±0.464, 1σ band
[−1.42, −0.49]) spans most of the plausible dark-energy range — this is **evidence for
simplicity-preference, not evidence against wCDM being viable**; 27 chronometer points simply
cannot constrain w meaningfully.

**Single-seed caveat (added this revision):** the train-split value w=−1.889±0.925 (seed=42) is
**one observation, not a distribution**. Correct status:
```
w INSTABILITY — SUGGESTED (single 70/30 split, seed=42)
w INSTABILITY DISTRIBUTION — NOT MEASURED (would require repeated splits / bootstrap / LOO)
```
A repeated-split or bootstrap estimate of Var(ŵ) under resampling is P2 future work (below), not
done here.

## Reproducibility — split precisely

```
COORDINATOR-REPRODUCED (same repo, same script, same data)  — YES
SAME-IMPLEMENTATION REPEATABILITY                            — PASS (4-digit match)
INDEPENDENT REIMPLEMENTATION (separate code from formulas)   — NOT DONE
```
r-values (ΛCDM 0.8796, MULTING-mono 0.7334, MULTING-full 0.6235) match R011's stored
0.8795/0.7334/0.6235 to 4 significant digits when the same script is re-run. This establishes
**computational repeatability of this implementation**, not an independent empirical validation.

---

## Corrected Audit 3 status line

```
ΛCDM vs wCDM on same CC likelihood       — VALID COMPARISON
Evidence for w != -1                     — ABSENT
ΛCDM weakly preferred by AIC/BIC         — SUPPORTED (simplicity preference, not exclusion of wCDM)
R011 same-code reproducibility           — PASS
Independent reimplementation             — NOT DONE
MULTING vs ΛCDM on CC likelihood         — NOT TESTED (reason: missing C1 closure, Audit 1)
Cluster-pipeline r ranking               — REPRODUCED
Nesting invariant (P0)                   — CHECKED, NO VIOLATION — true global optimum is beta=0
                                            (confirms NR-013, 2026-07-13 — not a new finding)
Full-model "degradation"                 — CONFIRMED as a genuine feature of the objective,
                                            not a restricted-grid artifact (see P0 section)
Fair model comparison including MULTING  — INCOMPLETE (blocked on C1, not on statistics)
```

## Overall verdict

**For the whole project (unchanged, per Audits 1+2+3 jointly):** `PIVOT + NEEDS_DATA`

**For this document (Audit 3) specifically:** `PARTIAL PASS / BLOCKED` — it successfully (a)
compared ΛCDM against wCDM on one shared likelihood, (b) reproduced the R011 cluster pipeline to
4 digits, (c) resolved the nesting question with a real numerical test rather than leaving it as
an assumption, and (d) established that TJB's own literal Table A1 β-values land in the same
degraded-r regime as R011's restricted-grid optimum. It did **not** — and could not — compare
MULTING against ΛCDM on a common statistical footing, because MULTING still lacks a unique
population-level H_MULT(z) (Audit 1's finding, confirmed independently here).

**Corrected replacement for the original "Not PASS" sentence:**
> On the 443-cluster correlation metric used in R011, every tested MULTING coupling —
> including TJB's own Table A1 values — scores lower than the pure-monopole (β=0) baseline, and
> an extended search confirms β=0 is the metric's actual global optimum, not merely the best of a
> restricted grid. A direct CC-likelihood comparison between MULTING and ΛCDM remains impossible
> because the current implementation does not define a unique population-level H_MULT(z).

**Corrected replacement for the original "Not FAIL" sentence:**
> The R011 implementation is computationally reproducible to four digits, and its central
> qualitative claim (nonzero dipole/quadrupole coupling reduces the correlation metric) survives
> a proper nesting check. This establishes repeatability and internal consistency of the
> implementation, not an empirical validation of MULTING.

---

## Cross-check against Audits 1 and 2

All three audits are **methodologically distinct but dependency-correlated** — they use different
angles (theory closure / provenance / statistics) but share the same repository, the same φ
definition, the same real data, and the same coordinator workflow, so their agreement is not
fully independent evidence:
- **Audit 1 (C1 closure, docs/133):** H_MULT(z) has no derived equation — NEEDS_DATA.
- **Audit 2 (provenance, docs/134):** H_MULT(z) row flagged 🔴 "not a derived formula" for the
  same reason.
- **Audit 3 (this document):** independently confirms *why* no chi2/AIC/BIC exists for MULTING —
  φ isn't a function of z alone — and, as new work this revision, confirms via direct numerical
  test that the "full model underperforms monopole" finding is a genuine feature of the
  correlation objective (global optimum at β=0), not a restricted-grid artifact.

## Next tasks surfaced by this revision (not executed here — out of this audit's scope)

- **P1** — keep Tables A and B permanently separate in any future write-up; never re-merge them.
- **P2** — repeated-split / bootstrap estimate of w's resampling distribution (replaces the
  single-seed "fragile" language with an actual distribution).
- **P3** — explicit likelihood specification for Table A (diagonal vs covariance, nuisance
  parameters, effective k) if Moresco+2022 covariance data becomes available.
- **P4** — only after TJB supplies a unique H_MULT(z): re-attempt Table A with MULTING included on
  a genuine shared likelihood.

---

*Artifacts: `scripts/audit3_fair_model_comparison.py` (ruff-clean, coordinator-reproduced),
`scratchpad/nesting_invariant_check.py` (P0 test, this revision, not committed — verification
script, reuses `src/pearson_fit.py` functions on real data, no new formulas introduced),
`scratchpad/boyko_AUDIT3_model_comparison.md` (full agent report, first-draft numbers, all
reproduced identically in this revision). No new data collected — reuses `data/hz_cc.csv` and
`data/clusters_clean.csv` already in the repo.*
