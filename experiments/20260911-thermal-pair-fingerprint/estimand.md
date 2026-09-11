# estimand.md — thermal-pair fingerprint

**Continues:** `claim.md` §8 item 1 (the mandatory next artifact before any
data acquisition or code). Read `claim.md` first — this file does not
repeat its Step -3/-2/-5 gates.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## EstimandOps L0 Classification

**Question type: Causal.** Not descriptive (this is not "are `K` and
pairwise dynamics associated"), not predictive (a forecasting model that
fits the association would not distinguish MULTING's specific mechanism
from a shared-driver explanation). MULTING's force law asserts thermal
energy **sources** an additional force term; the estimand below is built
to let that assertion fail, not just to measure a correlation.

Per `claim.md` §2, this file supplies the DAG and four identifiability
checks that section deferred. Written **before** any data is touched —
`claim.md` §5 already confirmed the ingredients exist publicly, but
nothing has been downloaded.

---

## Population

Real galaxy-cluster **pairs** — not single clusters — drawn from the
overlap of a kSZ-tracked spectroscopic catalog (DESI-DR1-class), a
weak-lensing mass catalog, and an ACT-DR6-class Compton-`y` map.

**Inclusion criteria:**
- Both members have a weak-lensing mass estimate and a measurable
  Compton-`Y` (tSZ) signal above the survey's own stated detection
  threshold.
- Both members fall inside the kSZ-tracked LRG/cluster sample's own
  redshift range (`arXiv:2511.23417`'s own selection, not redefined
  here).
- Pair separation `s` inside a range where the pairwise-kSZ estimator
  itself is validated (per that paper's own reported scale range — to be
  read off its methods section before any pull, not assumed).

**Exclusion criteria:**
- Either member below the survey's own mass-completeness limit at its
  redshift (avoids Malmquist-type selection differentially entering `K`
  and `M`).
- A cluster appearing in more than one candidate pair is assigned to
  **at most one** pair (chosen by closest match on the matching
  variables below); the rest of its candidate pairs are dropped. Reason:
  SUTVA (§ below) — the same physical object cannot licitly appear as an
  independent unit twice.
- Pairs whose members sit in the same larger multi-cluster system or
  supercluster complex at separation comparable to `s` itself (a
  catalog-level check, not yet specified numerically — this is an open
  design item, not a placeholder to skip).

**Definitional note carried from `pearl_registry`'s 2026-09-09 entry:**
"the pair" in v82's own text is not sharply defined (nearest-neighbor vs.
all-pairs-within-a-radius gave `ρ=0.019` vs `ρ=+0.38` for an unrelated
correlation this project already measured on TNG-300 — a large,
consequential difference). **This estimand adopts the definition the
source kSZ paper itself uses for its own pairwise statistic** — inheriting
its convention rather than inventing a new one, specifically to avoid
re-opening that ambiguity here.

---

## Intervention

N/A — observational. There is no assignment mechanism; `ξ` is a measured
covariate of each real pair, not something manipulated.

## Comparator

**Null hypothesis (standard gravity):** conditional on mass, redshift,
large-scale environment, and dynamical state, pairwise dynamics has **no**
residual dependence on `ξ = (K/(Mc²))(R/s)`.

**MULTING alternative:** conditional on the same set, pairwise dynamics
depends on `ξ` with the specific functional form `claim.md` §4 froze:
`F/(GM²/s²) = −1 + 2β₁ξ − β₂ξ²`, `β₁=1.433479×10¹⁰`,
`β₂=7.806760×10¹⁷` — not merely "some slope," a **shaped** dependence,
including entering net-repulsive behavior above `ξ=3.669×10⁻⁸`.

---

## Endpoint

**Primary:** a pairwise-dynamics statistic constructed the same way as
`arXiv:2511.23417`'s own pairwise-kSZ velocity estimator, for the subset
of that catalog's pairs falling in this estimand's population, regressed
against `ξ` after conditioning on the matching set below.

**Secondary (independent path, per `claim.md` §5's own "Path A/Path B"
idea — not yet built, named as a design requirement):** an X-ray-based
analogue — `K` from eROSITA/CHEX-MATE `T_X`+`M_gas` instead of tSZ, and a
redshift-space or independent velocity-field estimator instead of kSZ —
run on a non-overlapping cluster sample, to check whether any detected
effect survives a fully independent measurement chain (guards against a
shared-instrument or shared-pipeline systematic masquerading as physics).

**Matching / conditioning set (both paths):** lensing mass `M` (both
members), redshift `z`, a large-scale density-field proxy (nearest
counted neighbor density or an equivalent environment estimator — source
to be fixed at data-pull time), and a dynamical-state proxy. For the
dynamical-state proxy, this project already has a working precedent —
`experiments/20260701-h1c-morphology-mass-bias/estimand.md` used X-ray
centroid shift `w500`, with X-ray concentration `c_SB` as a documented
substitute when `w500` is unavailable. Reused here, not reinvented.

## Summary Measure

Nested model comparison, the same convention this project already used
for `FINDING_P166`/`FINDING_P167` (AIC/BIC on real fitted models, not a
bare correlation coefficient): fit (a) a null model with the matching
covariates only, (b) MULTING's frozen functional form as one additional
term (no free parameters — `β₁,β₂` are fixed, not fitted here), and
compare `Δχ²`, `ΔAIC`. A free-slope linear-in-`ξ` alternative is fit as
a **third**, intermediate model — this is required, not optional: it is
what discriminates "any thermal-mass correlation exists" (which standard
astrophysics could produce via unmodeled mass-proxy leakage) from "the
specific MULTING-shaped, sign-crossing dependence exists" (which it
should not).

## MCID

**Not yet numeric.** Per `estimand-ops.md`'s own Data Requirements
discipline and this project's own repeated practice (`FINDING_P191`-
`P194`), the threshold is set by a **power analysis on mock catalogs
matching the real sample's expected size and `ξ`-scatter**, run before
the real data is touched — not asserted here from intuition. Placeholder
structure only:

- **PROMOTE** candidate region: MULTING's fixed-form model beats both the
  null and the free-linear alternative by a pre-registered `ΔAIC`
  margin, **and** the highest-`ξ` stratum shows sign consistent with the
  predicted crossing (not merely a steeper slope).
- **REJECT** candidate region: the null model is not beaten by either
  alternative at the pre-registered margin.
- **INCONCLUSIVE**: the free-linear model beats the null, but does not
  distinguish itself from MULTING's fixed form at the available power
  (the two are only really distinguishable near the crossing, where data
  may be sparse) — an expected, informative outcome, not a design
  failure.

## ICE (Intercurrent Events)

**ICE strategy: treatment-policy**, matching this project's own H1b/H1c
convention.

- A pair where one member undergoes a detected major merger between the
  lensing and tSZ observation epochs → include as-is; disturbed systems
  are part of the real population, not a data-quality problem.
- A pair where the kSZ pipeline's own quality flags mark the velocity
  estimate as unreliable → exclude, and report the exclusion fraction
  (this is a real hazard given §"Consistency" below — exclusions must be
  audited for whether they correlate with `ξ`, which would itself bias
  the result).
- Compton-`Y` below the detection threshold for one member → exclude the
  pair; do not impute `K=0`, which would be a substantive physical claim
  (no thermal energy), not a missing-data placeholder.

---

## Causal DAG

Text form (this repository has no prior `dag.md` file or diagram
convention to match — written as explicit edges, consistent with how
`experiments/20260907-icm-expansion-correlation/claim.md` §4 already
wrote its own 5-path confound list in prose).

**Nodes:**
`M` (gravitating/lensing mass) · `z` (redshift) · `Env` (large-scale
density field) · `Dyn` (dynamical/merger state) · `K` (true thermal
energy) · `R` (characteristic radius) · `s` (pair separation) ·
`ξ = f(K,M,R,s)` (the deterministic exposure) · `V_true` (real pairwise
peculiar velocity, latent — never directly observed) · `τ_ML` (the
kSZ pipeline's ML-inferred optical depth per object) · `V_kSZ` (the
**measured** outcome, a function of `V_true` **and** `τ_ML`) · `Sel`
(catalog selection/construction) · `MULTING-force` (the hypothesized
causal mechanism under test, dashed = not assumed to exist).

**Edges:**

```
M ──────────────→ K                (mass-temperature/thermal scaling)
M ──────────────→ V_true           (standard gravity: mass sets local dynamics)
z ──────────────→ K                (thermal-history evolution)
z ──────────────→ V_true           (Hubble-flow / growth-factor evolution)
Env ────────────→ K                (external pressure / accretion heating -- v82's own text)
Env ────────────→ V_true           (large-scale tidal/flow field)
Dyn ────────────→ K                (mergers shock-heat gas at fixed M)
Dyn ────────────→ V_true           (disturbed systems: anomalous peculiar velocities)
K, M, R, s ─────→ ξ                (deterministic, by definition)
ξ ┄┄┄┄[MULTING-force]┄┄┄→ V_true   (THE HYPOTHESIZED PATH -- dashed, not assumed)
V_true ─────────→ V_kSZ            (real signal enters the measurement)
τ_ML ───────────→ V_kSZ            (measurement CONSTRUCTION, not a physical cause of V_true)
[sim-trained gravity model] → τ_ML (τ_ML's own training assumes standard gravity)
Sel ────────────→ {which (M,z,Env,Dyn,K) combinations enter the catalog at all}
```

**The confounding structure, stated plainly:** `M`, `z`, `Env`, `Dyn` each
have arrows into **both** `K` (hence `ξ`) and `V_true` — classic
confounders, all four must be conditioned on for any `ξ`–`V_kSZ`
association to be interpretable. `τ_ML` is **not** a confounder in the
classical sense (nothing causes both it and `ξ`) — it is a threat to
**measurement validity**: `V_kSZ` is not `V_true` observed with
independent noise, it is `V_true` observed through a filter trained under
an assumption (standard gravity in the training simulations) that could
be false in exactly the regime being tested. This is the single largest
open risk this estimand carries forward from `claim.md` §5.

---

## Four Identifiability Checks

### 1. Consistency

**Threat, not yet resolved.** `Y^ξ` (the pairwise-dynamics outcome under
exposure level `ξ`) is well-defined only if (a) `ξ` itself is computed
identically for every pair — requires fixing the pair-definition
ambiguity (§ Population, above) once, not per-analysis — and (b) `V_kSZ`
means the same thing across the sample, which is doubtful given `τ_ML`'s
own dependence on a gravity-model-trained pipeline (DAG, above).
**Partial mitigation, not a fix:** using the SAME kSZ pipeline/ML model
throughout at least makes any distortion **systematic and shared**
across the `ξ`-range, rather than differential — which is why the
free-linear intermediate model (§ Summary Measure) matters: a shared,
`ξ`-independent distortion would bias the intercept/normalization, not
manufacture the specific sign-crossing shape.

### 2. Positivity

**Not yet verified — an assumption, flagged as such.** Requires that,
within each `(M,z,Env,Dyn)` stratum used for matching, the real sample
spans a genuine range of `ξ`, including some pairs meaningfully closer to
the `3.669×10⁻⁸` crossing than the model's own mean trajectory (`claim.md`
§4's `~14%` gap). `FINDING_E13`'s real `σ=0.49` scatter in `M_gas–T`
makes this *plausible*, not *confirmed* — this must be checked empirically
on the real pulled catalog (a simple histogram of `ξ` per stratum) before
any regression is trusted, and reported even if it fails.

### 3. Exchangeability

**The weakest link, named honestly.** Conditional on `{M,z,Env,Dyn}`,
does `ξ`'s variation among otherwise-matched pairs reflect nothing but
"noise" with respect to `V_true`'s potential outcomes? The concrete
threat: `Dyn` (dynamical state) drives **both** `K` and `V_true` through
the *same* underlying process (merger history) — a proxy like `w500`
captures current-epoch disturbance, not full assembly history, so
residual confounding through `Dyn` is expected even after matching.
`experiments/20260701-h1c-morphology-mass-bias` already hit exactly this
limit for a related question. **No claim of exact exchangeability is
made here** — only conditional exchangeability given the stated matching
set, with the residual threat named explicitly rather than assumed away.

### 4. SUTVA

**Plausible at the relevant scales, with one stated exclusion rule.**
Two provisions already built into § Population: (a) no cluster appears
in more than one analyzed pair, and (b) pairs whose members sit inside
the same larger multi-cluster complex are excluded — both aimed at
preventing one pair's realized dynamics from mechanically depending on
another pair's assignment. **Not yet checked:** whether the real catalog,
after these exclusions, still has pairs that share a common large-scale
filament or supercluster membership at a level that could induce
correlated `V_true` residuals across "independent" pairs — this needs a
real check against the environment proxy already required for matching,
not a separate new dataset.

---

## Identification Strategy

**Conditioning / matching (g-formula-style).** No randomization, no
instrument, no natural experiment is available — this is an ordinary
observational design, and should be described as one, not oversold.
Strength: **Medium** on this project's own Independent Verification
Strength Ladder (`falsification-ladder.md`) for the primary result;
**Strong**-tending only if Path A and Path B (§ Endpoint) agree, since
independently-implemented, independently-sourced measurement chains
converging is the strongest tier available here short of a blind
external reproduction.

## Sensitivity Analyses (≥2 required, Full-Ladder)

1. **Permutation / shuffle negative control.** Within each matched
   stratum, randomly reassign `K` among pairs and re-run the regression.
   Direct precedent already in this project:
   `experiments/20260909-tng-mass-assortativity` used exactly this
   design (mass-shuffle gave `r=0.028≈0`) as its own negative control.
   Expected here: near-zero, `ξ`-independent result under shuffling: a
   real signal must vanish under this permutation; a pipeline artifact
   (e.g., from `τ_ML`) might not.
2. **Path A vs. Path B independence** (§ Endpoint) — an effect appearing
   only in the tSZ+kSZ chain and not in the independent X-ray+alternative-
   velocity-estimator chain is presumptively a shared-pipeline systematic,
   per `claim.md`'s own citation-check finding about `τ_ML`.
3. **(Optional, if power allows) Dynamical-state proxy substitution** —
   `w500` vs. `c_SB`, matching `H1c`'s own documented substitution
   pattern, to check the exchangeability threat is not silently carried
   by the choice of proxy alone.

---

## Prior literature summary (FL Step -4: Source Trace)

| Claim | Status | Source |
|---|---|---|
| ACT DR6 Compton-`y` maps are public | `[VERIFIED-REAL]` | NASA LAMBDA, per `claim.md` §5 citation check |
| 9.3σ pairwise-kSZ detection, DESI DR1+ACT DR6+Planck | `[VERIFIED-REAL]` | `arXiv:2511.23417` |
| Per-object kSZ velocities are ML-inferred, not measured | `[VERIFIED-REAL]` | same paper, per `claim.md` §5's own caveat |
| eRASS1: 12,247 clusters, per-cluster `T_X` in the catalog itself | `[VERIFIED-arXiv:2402.08452]` | per `claim.md` §5 |
| `M_gas–T` intrinsic scatter `σ=0.49` (ln) | `[VERIFIED-arXiv:2511.14356]` | `FINDING_E13`, reused here for Positivity plausibility only |
| X-ray centroid shift `w500` as a dynamical-state proxy, with `c_SB` as a documented substitute | `[VERIFIED-REAL]`, this project's own prior design | `experiments/20260701-h1c-morphology-mass-bias/estimand.md` |
| "The pair" is ambiguous in v82's own construction (nearest-neighbor vs. all-pairs give `ρ=0.019` vs. `+0.38`) | `[VERIFIED-run]` | `pearl_registry/INDEX.md`, 2026-09-09 entry |

## What this does NOT mean

1. Does **not** establish that any effect found would be caused by
   MULTING's mechanism specifically — Exchangeability (above) is only
   conditional, and `Dyn`-mediated residual confounding is a live,
   unresolved threat, not a formality.
2. Does **not** claim the kSZ pairwise-velocity measurement is unbiased
   with respect to `ξ` — Consistency (above) is the weakest of the four
   checks, and the mitigation offered is partial, not a resolution.
3. A PROMOTE-region result does **not** mean MULTING "beats" ΛCDM at the
   population level — this estimand is about one specific, narrow
   mechanism signature, not a global model comparison (that question is
   `FINDING_P166`'s, already answered separately).
4. Does **not** yet have a numeric MCID — `estimand-ops.md`'s own
   discipline requires a mock-catalog power analysis before that number
   is set, not an intuition-based threshold.
5. Is **not** a data-acquisition plan. `claim.md` §8 item 2 (costed
   acquisition) still comes after this file, and code still comes after
   that.

## Status

**Estimand written, all four identifiability checks named with their
concrete residual threats stated (none dismissed as satisfied). No data
pulled. No code exists in this folder.** Per `claim.md` §8: the next
artifact is a costed data-acquisition plan naming exact catalog columns,
access mechanism, and sample-size estimate — followed by the mock-catalog
power analysis this file's own MCID section requires before any real
number is frozen.
