# estimand.md — thermal-pair fingerprint

**Continues:** `claim.md` §8 item 1 (the mandatory next artifact before any
data acquisition or code). Read `claim.md` first — this file does not
repeat its Step -3/-2/-5 gates.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**[AMENDED 2026-09-11 — external critique, independently verified before
applying: one load-bearing citation (astro-ph/0502226) checked directly
against its own abstract and found to be about tSZ-mass scaling only —
no mention of kSZ or optical-depth/velocity degeneracy; the underlying
physics claim it was attached to is nonetheless real and independently
corroborated by this file's own § Measurement-Validity finding below,
already present before this amendment. Applied: a new DAG node (`G`),
a new § Temporal Structure item, a mandatory pre-data synthetic
identifiability battery (§ below), and a sharper negative-control design.
Not applied: "Causal DAG: MISSING" — the DAG below already existed at
the time of that critique; what was accurate in it is that the DAG was
**incomplete**, not absent.**

**[AMENDED 2026-09-11, 4th pass — the fixed-window Endpoint is
SUPERSEDED, per `null_results/INDEX.md` NR-025.]** The Exact Pair
Census + window-width scan (`FINDING_window_width_resolution.md`)
showed that a fixed-separation-window pair count has no defensible
width: power is monotonic in width (no interior optimum for `N≳15`, so
"wider" is trivially always better), and the real two-point correlation
`1+ξ(s)` computed from real cluster positions has **no local feature at
`s=45` Mpc** — that number is `v82`'s own model-internal initial
condition, not a scale singled out by real large-scale-structure
clustering. **§ Endpoint and § Summary Measure below are rewritten** to
use each real pair's own separation `s` continuously, rather than
sorting pairs into a window — this removes the width choice from the
design entirely instead of trying to justify one. The old, window-based
text is kept, struck through in spirit but not deleted (project
convention: mark superseded, do not erase), immediately below the new
text in each section.

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

**[AMENDED 2026-09-11, 4th pass] Primary, s-dependent design (replaces
the window-based Primary Endpoint below).**

**The core move:** instead of assigning every pair the SAME `ξ` (drawn
i.i.d. from one population distribution, `claim.md` §3a's own flagged
marginal `HYPOTHESIS`), give each real pair its OWN model-predicted `ξ`,
computed from its OWN measured `z` and `s` — reusing, not re-deriving,
two pieces of already-verified prior work:

```
ξ_pred(z, s) = (β₁/β₂) · Q(z) · (d₀ / s)
```

- `Q(z) = (β₂/β₁)·K(z)R(z)/(M(z)c²·d(z))` — `v82`'s own smooth mean
  `z`-trajectory, already tabulated at every `z` from `-0.95` to `16.9`
  by the CLOSED branch `experiments/20260907-icm-expansion-correlation/
  FINDING_stage4_dflip_is_not_derivable_in_the_construction.md`
  (`[VERIFIED]`, re-used here unchanged, not recomputed). Solving that
  file's own definition for `ξ` gives `ξ_trajectory(z) = (β₁/β₂)·Q(z)` —
  checked directly against the one published cross-reference point:
  `Q(z=1.443)=1.7484` gives `(β₁/β₂)·1.7484 = 1.8358×10⁻⁸×1.7484 =
  3.210×10⁻⁸`, exactly `claim.md` §4's own `ξ(z=1.443)` value. This is
  arithmetic identity, not a new assumption.
- `d₀ = 45` Mpc comoving, `[VERIFIED]` v82.md:58-59,318, constant at
  every `z` (already established, `FINDING_power_analysis.md` §2) — the
  separation at which the trajectory's own `Q(z)`/`ξ(z)` was computed.
- `s` — the real pair's own measured comoving separation, from a real
  catalog (`exact_pair_census.py`'s own real positions, or the eventual
  real kSZ-tracked catalog once pulled) — **not** a window boundary.

`ξ∝1/s` is not a new physical claim: it falls directly out of `ξ =
(K/(Mc²))(R/s)`'s own already-verified definition (`claim.md` §4).
Applying it per-pair, using each pair's own `s` instead of the
trajectory's own `d(z)`, is the ONLY change — `K(z), R(z), M(z)` are
still taken from `v82`'s own trajectory at the pair's `z` (the same C1
"fingerprint" assumption already in force: real per-cluster physical
`K, R, M` are NOT substituted in, that remains the separate, unresolved
C2 causal question `claim.md` §7a already named).

**A real, checkable consequence, not yet checked (name it, don't
assume it): a real pair with `s < 45` Mpc gets a BOOSTED `ξ_pred`
relative to the trajectory's own value at that `z`, purely
geometrically** — independent of `FINDING_E13`'s `σ=0.49` mass
scatter, which `claim.md` §4 already leaned on to close the trajectory's
own `14%` gap to crossing. Close real pairs may approach or cross
`ξ_crossing=3.669×10⁻⁸` through separation alone. Whether this actually
happens for real pairs in the real `z` range used here is a five-minute
check once `Q(z)` is loaded alongside the real Exact-Pair-Census `(z,s)`
values — flagged as the FIRST cheap validity check for whoever builds
this next (§ MCID below), not computed in this prose amendment.

Per member of a pair, real intrinsic scatter is still applied exactly
as before (`claim.md` §3a's own flagged substitution, unchanged in
status): `ξ_A, ξ_B ~ Lognormal(mean=ξ_pred(z,s), σ_ln=0.49)`,
independently drawn — `ξ_pred(z,s)` is the pair-level deterministic
center, not a claim that both members share one exact value.

**Same outcome variable as before** — a pairwise-dynamics statistic
constructed the same way as `arXiv:2511.23417`'s own pairwise-kSZ
velocity estimator — now regressed against each pair's own `ξ_pred(z,s)`
(§ Summary Measure below), not against a window-averaged constant.

**Population consequence:** the window-based inclusion criterion on `s`
(narrow band around `45` Mpc) is DROPPED. The relevant `s`-range
restriction is now purely the ALREADY-EXISTING § Population criterion —
"pair separation `s` inside a range where the pairwise-kSZ estimator
itself is validated" — which was always there and now does the only
`s`-restriction work needed. **A new lower-`s` caveat, not previously
needed:** `exact_pair_census.py`'s own histogram (`FINDING_window_width_
resolution.md` §3) showed a large, suspicious excess at `s<10` Mpc,
almost certainly catalog near-duplicate/deblending contamination, not a
real close-pair population — real, validated small-`s` pairs will need
their own explicit vetting before inclusion, separate from and in
addition to the kSZ estimator's own validated range.

---

**Superseded (window-based) Primary, kept per this project's own
mark-don't-erase convention — do not build against this version:**

A pairwise-dynamics statistic constructed the same way as
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

**[AMENDED 2026-09-11, 4th pass] s-dependent redesign — same nested-
model logic, same `FINDING_P166`/`FINDING_P167` AIC/BIC convention,
different regressor.** Three models, fit per pair `i` using its own
`(z_i, s_i)`, not a window-constant:

- **Model 0 (null):** `y_i = c` — matching covariates only, no `ξ`-
  dependence of any kind.
- **Model 1 (MULTING, fixed shape):** `y_i = c + λ·S_M(z_i,s_i)`, where
  `S_M(z_i,s_i) = β₁·(ξ_{A,i}+ξ_{B,i}) − β₂·ξ_{A,i}·ξ_{B,i}` using the
  per-pair `ξ_pred(z_i,s_i)` (§ Endpoint) as each member's scatter
  center. `β₁:β₂` ratio is fixed (not fitted — same discipline as
  before); `λ` is the one free amplitude, absorbing the unknown overall
  proportionality between a two-node force-law quantity and an observed
  pairwise-velocity residual. **This is the load-bearing change**: `S_M`
  now varies smoothly across the FULL real sample via each pair's own
  `z,s` — not a single value repeated across `N` i.i.d. draws.
- **Model 2 (free, generic alternative):** `y_i = c + μ·ξ_pred(z_i,s_i)`
  — a free-slope **linear** term in the SAME regressor `ξ_pred(z_i,s_i)`
  Model 1 uses, still required, not optional, and still doing the same
  job as before: separating "some monotonic trend in the model's own
  predicted `ξ` profile exists" (which ordinary mass-proxy leakage into
  `K` could produce, without MULTING) from "the specific quadratic,
  sign-crossing shape exists" (Model 1), which ordinary leakage should
  not produce.

**PROMOTE / REJECT / INCONCLUSIVE regions unchanged in spirit** (below)
— Model 1 must beat both Model 0 and Model 2 by the pre-registered
`ΔAIC` margin, AND the closest-to-crossing real pairs (now identifiable
directly by their own small `s` and/or high-`z` combination, not by
falling in an arbitrary window) must show sign consistent with the
predicted crossing.

**Optional, named but not adopted as primary (robustness only,
§ Sensitivity Analyses):** a free-form spline/polynomial directly in
`s` (bypassing `ξ_pred`/`Q(z)` entirely) would be a more agnostic
negative-control-style alternative, catching any `s`-dependence not
captured by the `ξ` formula at all — costs more free parameters, hence
power, so kept as a secondary check, not the primary Model 2.

---

**Superseded (window-based) Summary Measure, kept per this project's
own mark-don't-erase convention — do not build against this version:**

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

**[UPDATED 2026-09-11, corrected same day after external critique —
verified before applying, see `FINDING_power_analysis.md` §2] Computed,
not placeholder — conditional on an unresolved window-*width* choice, no
longer on a wrong window *center*.** The first version of this section
used a window sourced from `pearl_registry`'s `s0~30 Mpc` note; that
number is v82's own *rejected* `H0,anchor` grounding attempt, not its
frozen pair-separation IC. Checked directly against v82's own text
(`s(0)=d0=45` Mpc, physical) and against this project's own already-
verified `FINDING_stage4` table (`d(z)=d0/(1+z)`) — both confirm `d0=45`,
giving a **constant 45 Mpc comoving** characteristic separation at every
`z` (not a redshift-dependent range).

**[UPDATED 2026-09-11, 2nd pass — Exact Pair Census run, see
`FINDING_power_analysis.md` §6]** The Poisson-volume model above is now
superseded by a real count on real `(RA,Dec,z)` positions from the
ACT-DR5 MCMF catalog (`arXiv:2406.14754`, 6237 clusters, `[VERIFIED]`
matches the paper exactly). Real clustering pushes narrow-window pair
counts **up** relative to the idealized model, as predicted
(`FINDING_power_analysis.md` §4a's own clustering-bias note) — but a
separate, previously-unflagged density-provenance gap in the old model
(applying the full-catalog density to a redshift-restricted shell)
pushed the broad-window count in the opposite direction. Net, real,
area-scaled-to-775deg² counts: broad=449 (100% power), narrow-25
(`[20,70]` Mpc)=53 (34.0% power), narrow-10 (`[35,55]` Mpc)=22 (10.7%
power) — a real but modest (`+2` to `+4` percentage points) improvement
over the withdrawn 8-30% range, not a qualitative change. **Still real
but weak; still neither dead nor adequately powered.** The window-width
choice remains the single most consequential open decision in this
branch — the Exact Pair Census answered the *shape* question, not the
width choice itself. **All numbers are best-case, confounder-free upper
bounds** — the synthetic four-world battery has not run; real power
will be lower. The area-scaling from ACT-DR5's full footprint to the
`700-850 deg²` Fork-2 target is a first-order linear approximation
(`exact_pair_census.py`'s own explicit caveat), not a real DES-Y3/
DESI-DR1/eRASS1 cross-match — that four-way exact overlap is the one
remaining open item before this MCID can move past "conditional."

**[UPDATED 2026-09-11, 3rd pass] The window-WIDTH question above is now
RESOLVED — negatively — see `FINDING_window_width_resolution.md` and
`null_results/INDEX.md` NR-025.** Power is monotonic in width under the
current model (no interior optimum for `N≳15`); the real two-point
correlation `1+ξ(s)`, computed directly from this catalog's own real
positions, shows no local feature at `s=45` Mpc — a smoothly declining
function in which `[40,50)` is not even a local maximum among its
neighbors. `d0=45` Mpc has no independent support from real clustering
statistics; it remains solely `v82`'s own model-internal initial
condition. **The fixed-window pair-count test design is REJECTED** — the
underlying MULTING mechanism is not, it survives untested by this
specific design. The Population/Endpoint framing above ("pairs near
v82's characteristic separation") therefore has no defensible
operationalization as a window count. A genuinely different Endpoint —
fitting `S_M`'s predicted `ξ∝1/s` dependence against each real pair's
own separation, rather than counting pairs in a window — remains a
live, un-adopted option, and would require amending this section
(Population/Endpoint/Summary Measure) before any code, not a numeric
rerun of the current design.

**[UPDATED 2026-09-11, 4th pass — the option named above is now
adopted; § Endpoint and § Summary Measure above are amended.] The
window-based MCID numbers above (8.4%-34.0%) do NOT carry over to the
s-dependent design and must not be quoted for it.** The new design uses
the FULL real sample (no window), so its power will generically be
higher — likely closer to the broad-window number (`N≈449`, `100%`
power) than the narrow one — but this is a plausibility expectation,
not a computed value: the new Model 1/Model 2 regressors are different
quantities than the old i.i.d.-window `ξ`, so `power_analysis_mock_
catalog.py`'s own `one_trial()` cannot simply be re-pointed at a new
`N`; it needs a new mock-data generator that draws `(z,s)` from the
real census (or an equivalent real-catalog resampling) and computes
`ξ_pred(z,s)` per mock pair, THEN applies the same scatter/noise/AIC
machinery. **This is the concrete next artifact — a new mock-catalog
power analysis for THIS design — required before any code touches real
kSZ/tSZ data, per this branch's own standing discipline. Not built in
this amendment.**

**[UPDATED 2026-09-11, 5th pass — built, see
`FINDING_power_analysis_s_dependent.md`.]** `power_analysis_s_
dependent.py` ran the real mock power analysis this section named: real
`(z,s)` bootstrap-resampled from the full 7693-pair census pool, the
same two-part PROMOTE bar as § Summary Measure. **At `N≈449` (Fork-2
mid footprint), power = `98.6%` @3x noise, `0.2%` false-promote** —
comparable to the old design's own `N=449` number, with a strictly
harder pass bar (beat both Model 0 and Model 2, not just Model 0). A
full power curve now exists from `N=10` to `N=2000` — the real payoff
is not a higher per-pair efficiency, it is that this design has **no
window-width ceiling**: it can use the full real population directly,
unlike the old design NR-025 showed had no principled way past
`18-53` pairs. Also ran § Positivity's own named cheap check for the
first time: `3.978%` of real pairs (`306/7693`) already have
deterministic `ξ_pred>ξ_crossing`, **with no scatter assumption at
all** — a materially stronger Positivity basis than the old mass-
scatter-only plausibility argument, though flagged against a real,
not-yet-checked risk (the closest such pairs sit at `s≈10.5-11.6` Mpc,
right against the `S_MIN_VALID=10` Mpc cut meant to exclude small-`s`
instrumental artifacts — Consistency (d) needs to resolve this before
the Positivity result is trusted outright).

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
energy) · `G` (electron/gas density distribution — **[ADDED 2026-09-11]**,
see below) · `R` (characteristic radius) · `s` (pair separation) ·
`ξ = f(K,M,R,s)` (the deterministic exposure) · `V_true` (real pairwise
peculiar velocity, latent — never directly observed) · `τ` (true electron
optical depth, a physical property of `G`) · `τ_ML` (the kSZ pipeline's
ML-**inferred** estimate of `τ`, not `τ` itself) · `V_kSZ` (the
**measured** outcome, a function of `V_true` **and** `τ_ML`) · `Y_tSZ`
(the measured tSZ signal, from which `K` is inferred) · `Sel` (catalog
selection/construction) · `MULTING-force` (the hypothesized causal
mechanism under test, dashed = not assumed to exist).

**Edges:**

```
M ──────────────→ K, G             (mass-temperature scaling; mass sets gas reservoir)
M ──────────────→ V_true           (standard gravity: mass sets local dynamics)
z ──────────────→ K                (thermal-history evolution)
z ──────────────→ V_true           (Hubble-flow / growth-factor evolution)
Env ────────────→ K, G             (external pressure / accretion heating -- v82's own text)
Env ────────────→ V_true           (large-scale tidal/flow field)
Dyn ────────────→ K, G             (mergers shock-heat AND redistribute gas at fixed M)
Dyn ────────────→ V_true           (disturbed systems: anomalous peculiar velocities)
G ──────────────→ K                (thermal content is a property of the gas distribution)
G ──────────────→ τ                (optical depth IS an integral over the same electron gas)
G ──────────────→ Y_tSZ            (tSZ is also an integral over the same electron gas, weighted by T_e)
K ──────────────→ Y_tSZ            (K is inferred FROM Y_tSZ -- near-definitional, not independent)
K, M, R, s ─────→ ξ                (deterministic, by definition)
ξ ┄┄┄┄[MULTING-force]┄┄┄→ V_true   (THE HYPOTHESIZED PATH -- dashed, not assumed)
V_true ─────────→ V_kSZ            (real signal enters the measurement)
τ ──────────────→ V_kSZ            (true optical depth enters the real kSZ signal physically)
τ_ML ───────────→ V_kSZ            (the PIPELINE'S ESTIMATE of tau -- what the analysis actually uses)
[sim-trained gravity model] → τ_ML (tau_ML's own training assumes standard gravity)
Sel ────────────→ {which (M,z,Env,Dyn,K) combinations enter the catalog at all}
```

**The confounding structure, stated plainly:** `M`, `z`, `Env`, `Dyn` each
have arrows into **both** `K` (hence `ξ`) and `V_true` — classic
confounders, all four must be conditioned on for any `ξ`–`V_kSZ`
association to be interpretable.

**[AMENDED 2026-09-11] Two distinct threats live in the measurement
tract, not one — conflated in this file's first version:**

1. **`τ_ML` vs. `τ`** — a **model-specification** threat: the ML
   estimate of optical depth is trained on simulations that assume
   standard gravity, so any discrepancy between `τ_ML` and true `τ` could
   itself correlate with the very effect being tested.
2. **`G → τ, Y_tSZ` (the newly added backdoor path
   `K ← G → τ → V_kSZ`)** — a **shared-physics** threat, independent of
   any modeling choice: tSZ and kSZ are both integrals over the *same*
   electron column (`Y_tSZ ∝ ∫n_e T_e dl`, `τ ∝ ∫n_e dl`), so stratifying
   pairs by thermal signal mechanically stratifies by electron column
   too — capable of producing a `K`–`V_kSZ` association through shared
   `n_e`, with **zero** gravitational content. This path exists even with
   a *perfect*, bias-free `τ_ML`.

Neither is a classical confounder (nothing common-causes both `ξ` and an
independent draw of `V_kSZ`'s noise) — both are threats to **Consistency**
(§ below), restated to keep them from being treated as a single,
already-handled item.

---

## Four Identifiability Checks

### 1. Consistency

**Threat, not yet resolved — now two named sub-threats, per the DAG
amendment above.** `Y^ξ` (the pairwise-dynamics outcome under exposure
level `ξ`) is well-defined only if (a) `ξ` itself is computed identically
for every pair — requires fixing the pair-definition ambiguity
(§ Population, above) once, not per-analysis; (b) the model-specification
threat: `V_kSZ` risks meaning something systematically different from
`V_true` because `τ_ML` is trained assuming standard gravity; and
**(c) [ADDED 2026-09-11] the shared-physics threat: `K` and `τ` are both
integrals over the same electron gas `G`, so a `K`–`V_kSZ` association
can appear even with a perfect `τ_ML` and zero MULTING effect** — this
was previously folded into (b) and is now kept separate because its
mitigation is different (it needs an *independent* thermal-content proxy,
not a better velocity pipeline).

**Partial mitigations, neither a fix:**
- For (b): using the SAME kSZ pipeline/ML model throughout at least makes
  that distortion **systematic and shared** across the `ξ`-range rather
  than differential — the free-linear intermediate model (§ Summary
  Measure) would absorb a shared, `ξ`-independent bias into the
  intercept, not manufacture the specific sign-crossing shape.
- For (c): the § Endpoint "Path B" (X-ray `T`+`M_gas` instead of tSZ) is
  the direct answer — `T` and `M_gas` do not share `G`'s optical-depth
  integral the way `Y_tSZ` and `τ` do, so an effect surviving in Path B
  alone is not explained by this specific backdoor path (though it may
  still have its own).

**(d) [ADDED 2026-09-11, 4th pass] New, design-specific threat: small-`s`
blending/deblending.** The s-dependent redesign (§ Endpoint) uses the
FULL validated `s`-range instead of a window that happened to sit well
inside it — meaning genuinely small-`s` real pairs, previously excluded
by construction, now enter the sample. Two real clusters close enough on
the sky risk (i) CMB-map-level signal blending given ACT's own beam size
(`~1.4-2.2` arcmin FWHM), and (ii) contaminating each other's
independently-fit per-object `τ_ML`/velocity estimate. This is DIFFERENT
from threats (b)/(c) above — it is instrumental/geometric, not a shared-
physics or model-specification issue — and is NOT resolved by the
already-existing Population criterion "pair separation `s` inside a
range where the pairwise-kSZ estimator itself is validated," since that
criterion bounds validity for a SINGLE typical pair, not specifically
for the smallest, most MULTING-informative separations this redesign
now deliberately wants to reach. Mitigation, not yet built: an explicit
minimum-`s` cut informed by the real angular separation at each pair's
`z` (not a fixed comoving number), checked against the source pipeline's
own stated resolution limit before any pair below it is trusted.

**[UPDATED 2026-09-11, 7th pass — checked directly for all 306 real
Positivity pairs, see `FINDING_beam_blending_check.md` §3a.]** All 306
real pairs behind the `3.978%` Positivity fraction now have their real
angular separation computed directly (not estimated from a base rate):
`5/306` (`1.6%`) sit at or near real blending risk (`<2×` beam FWHM),
`3/306` (`1.0%`) genuinely below the beam FWHM itself. Excluding all
`5` at-risk pairs moves the Positivity fraction only from `3.978%` to
`3.913%` — a `1.6%` relative reduction, not a collapse. **Consistency
(d) is now a quantified, small correction, not an open unknown** — no
further action on this specific threat is required before the
sign-near-crossing PROMOTE sub-check and the synthetic four-world
battery.

### 2. Positivity

**Not yet verified — an assumption, flagged as such.** Requires that,
within each `(M,z,Env,Dyn)` stratum used for matching, the real sample
spans a genuine range of `ξ`, including some pairs meaningfully closer to
the `3.669×10⁻⁸` crossing than the model's own mean trajectory (`claim.md`
§4's `~14%` gap). `FINDING_E13`'s real `σ=0.49` scatter in `M_gas–T`
makes this *plausible*, not *confirmed* — this must be checked empirically
on the real pulled catalog (a simple histogram of `ξ` per stratum) before
any regression is trusted, and reported even if it fails.

**[ADDED 2026-09-11, 4th pass] Now directly checkable, not just
plausible, thanks to the s-dependent redesign.** Because `ξ_pred(z,s)`
is a deterministic function of each REAL pair's own `(z,s)` (§ Endpoint),
Positivity no longer rests only on the mass-scatter argument above —
`ξ_pred` for the closest real pairs (already known to exist:
`exact_pair_census.py`'s own histogram shows real pairs down to
`s<10` Mpc, before the small-`s` vetting `§ Consistency (d)` requires)
can be computed directly from the already-tabulated `Q(z)` and compared
to `ξ_crossing` with no scatter assumption at all. **Not computed in
this amendment** — named as the cheapest possible check for whoever
builds the new mock-catalog power analysis (§ MCID): load `Q(z)`
alongside the real `(z,s)` census values, compute `ξ_pred` for the
closest 1% of real pairs, and report directly whether any exceed
`ξ_crossing` before relying on scatter to get there.

**[UPDATED 2026-09-11, 5th pass — now CONFIRMED, not just checkable,
see `FINDING_power_analysis_s_dependent.md` §2.]** `3.978%` of real
pairs (`306/7693`) have deterministic `ξ_pred(z,s) > ξ_crossing`, zero
scatter needed — the closest five span a real `z` range (`0.277` to
`0.574`), not one coincidence. **Positivity is materially stronger than
before.** **[UPDATED 2026-09-11, 7th pass — resolved for all 306, see
`FINDING_beam_blending_check.md` §3a.]** Direct check of the full
`306`-pair Positivity set (internal consistency confirmed:
`306/7693=3.978%`, exact match to the number above) finds `301/306`
(`98.4%`) at `≥2×` beam FWHM, `286/306` (`93.5%`) comfortably resolved
at `≥5×`. Only `5` pairs (`1.6%`) are genuinely at risk. Excluding them
gives a blending-risk-excluded Positivity fraction of `301/7693=
3.913%` — **the Positivity result survives this check essentially
intact**, not merely for the 5 originally-illustrated pairs.

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

### 5. [ADDED 2026-09-11] Temporal Structure — not one of the classical
### four, but required here and previously missing

**MULTING's force law is instantaneous; kSZ gives an integrated
quantity.** `a = a(K(t),M(t),R(t),s(t))`, but
`v(t) = v(t₀) + ∫_{t₀}^{t} a\,dt'`. A regression of today's `V_kSZ` on
today's `ξ` implicitly assumes today's `ξ` is a reasonable proxy for the
pair's `ξ`-history — which fails specifically when merger history moves
`K` and `V_true` together over the same interval (the `Dyn` path already
in the DAG), **and** more generally whenever a pair's `ξ` has not been
roughly constant over the dynamical time relevant to building up `v`.
**This is not resolved by conditioning on `Dyn`** (a present-epoch
proxy) — it requires either (a) restricting to pairs with independent
evidence of a stable recent history (e.g. `Dyn`-relaxed for a
resolvable look-back window), accepting the resulting selection is a
genuine restriction of the estimand's own population, not a nuisance to
average over; or (b) the `λ_M`-in-a-forward-model reformulation named
below, which requires machinery this project has not built (§ Open
Design Item).

**Open design item, not resolved here:** a proper causal answer needs a
forward/temporal dynamics model — `a = a_baseline + λ_M · a_MULTING(...)`,
testing `H_M: λ_M=1` against `H_0: λ_M=0` inside that model — rather
than a direct regression of `v` on instantaneous `ξ`. Building that
model is the same undertaking `claim.md`'s own external-proposal review
flagged as unverified (§5, many-body/N-body/BBGKY derivation) — this
estimand does not assume that work exists or will be done; C1 (§ below)
is deliberately scoped to avoid needing it, and is weaker precisely
because of that.

**[ADDED 2026-09-11, 4th pass] One real, untested consequence of the
s-dependent redesign for this threat, named not resolved:** smaller
real `s` plausibly means a shorter relevant dynamical timescale for the
pair, which COULD make "today's `ξ`" a better proxy for the pair's own
recent `ξ`-history at small `s` than at large `s` — i.e. this threat
may not be uniform across the sample the redesign now spans. This is a
plausible direction, not a checked one; it cuts the same way as
§ Consistency (d)'s new small-`s` instrumental threat pulls the OTHER
way (small `s` = better temporal proxy, but also more
blending/deblending risk) — the two do not net out to anything
knowable without real data, and are kept separate, not combined into
one adjustment.

---

## Pre-Data Requirement: Synthetic Identifiability Battery
## [ADDED 2026-09-11 — adopted from external critique, matches this
## project's own Oracle Adequacy Gate applied to this specific estimator]

**Before any real catalog is touched, this project's own
`falsification-ladder.md` Step 2b (Oracle Adequacy Gate) requires
checking that the evaluator — here, the estimator/regression pipeline
itself — can actually distinguish the states it claims to distinguish.**
Concretely: construct four synthetic mock worlds, matched in sample size
and marginal `(M,z,Env,Dyn)` distributions to the real target catalog:

1. **World `MULTING`** — mock pairs generated with the frozen `(β₁,β₂)`
   force law actually sourcing the dynamics.
2. **World `optical-depth-confounded`** — no MULTING effect; `K`–`V_kSZ`
   association injected purely through the `G→τ→V_kSZ` backdoor path
   (§ DAG amendment above), zero true gravitational dependence on `K`.
3. **World `merger-confounded`** — no MULTING effect; `Dyn` drives both
   `K` and `V_true` independently, no `K→V_true` causal path at all.
4. **World `null`** — no MULTING effect, no confounding-induced
   association either.

**Pass condition:** the full analysis pipeline (matching, the C1 `S_M`
kill-test, and — if attempted — the C2 causal estimator) must correctly
classify all four worlds, including **not** producing a false PROMOTE in
worlds 2 or 3. **A pipeline that cannot pass this battery on synthetic
data is `ORACLE_INADEQUATE` per this project's own gate and is
prohibited from running on real data until fixed** — this is a hard
gate, not a recommended step.

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

1. **Permutation / shuffle negative control — [SHARPENED 2026-09-11].**
   Within each matched stratum, randomly reassign `K` among pairs
   **while holding `M`, `z`, `s`, and each pair's own `τ_ML`/`Y_tSZ`
   fixed** (not a plain shuffle of all columns together) — this is the
   design that actually isolates the question: does the association
   survive breaking the *correct* `K`-to-pair linkage while leaving the
   measurement chain (and its `G→τ` backdoor) untouched? A plain
   full-shuffle, by contrast, could accidentally also break the
   `G→τ→V_kSZ` path and falsely appear to pass. Direct precedent for the
   general method in this project: `experiments/20260909-tng-mass-
   assortativity` (mass-shuffle gave `r=0.028≈0`); the refinement above
   is new here, not inherited from that precedent as-is.
2. **Path A vs. Path B independence** (§ Endpoint) — an effect appearing
   only in the tSZ+kSZ chain and not in the independent X-ray+alternative-
   velocity-estimator chain is presumptively a shared-pipeline systematic,
   per `claim.md`'s own citation-check finding about `τ_ML`.
3. **(Optional, if power allows) Dynamical-state proxy substitution** —
   `w500` vs. `c_SB`, matching `H1c`'s own documented substitution
   pattern, to check the exchangeability threat is not silently carried
   by the choice of proxy alone.
4. **[ADDED 2026-09-11, 4th pass] Free-form `s`-spline alternative** —
   the more agnostic Model 2 named but not adopted in § Summary Measure:
   refit with `ξ_pred`/`Q(z)` replaced by a free spline/polynomial
   directly in `s`, to check that Model 1's win (if any) is not merely
   "some smooth function of `s` fits better than a constant" but
   specifically tracks the `ξ∝1/s`-shaped, sign-crossing prediction.

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
| `Q(z)=(β₂/β₁)k(z)R(z)/(M(z)c²d(z))>1` at every `z∈[-0.95,16.9]`, `Q_min=1.7484` at `z=1.443` — reused here as `ξ_trajectory(z)=(β₁/β₂)Q(z)` for the s-dependent Endpoint | `[VERIFIED]`, this project's own closed prior work | `experiments/20260907-icm-expansion-correlation/FINDING_stage4_dflip_is_not_derivable_in_the_construction.md` |
| Fixed-window pair-count design has no principled width — power monotonic in width, real `1+ξ(s)` has no local feature at `s=45` Mpc | `[VERIFIED-run]` | `FINDING_window_width_resolution.md`, `null_results/INDEX.md` NR-025 |

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
4. **[UPDATED 2026-09-11]** Has a computed, `[VERIFIED-run]` MCID
   candidate range (8.4%-34.0% power depending on window width and
   footprint — see the MCID section above and `FINDING_power_analysis.md`
   §6) **for the now-superseded window-based design only** (item 6
   below) — do not quote it for the s-dependent design, which does not
   yet have its own MCID number at all.
5. Is **not** a data-acquisition plan. `claim.md` §8 item 2 (costed
   acquisition) still comes after this file, and code still comes after
   that.
6. **[ADDED 2026-09-11, 4th pass]** The s-dependent redesign does
   **not** yet have its own power analysis, its own real-data Positivity
   check, or its own small-`s` instrumental vetting — all three are
   named as concrete next steps (§ MCID, § Consistency (d), §
   Positivity), none built here. Does **not** claim the redesign is more
   powerful than the old window-based design — only that it removes an
   undecidable free parameter (window width) the old design had no way
   to fix; whether it is MORE statistically powerful remains to be
   computed, not assumed from the qualitative argument in § Endpoint.

## Status

**[UPDATED 2026-09-11]** Estimand written, DAG now includes the `G`
(shared-electron-gas) backdoor path and a fifth, non-classical Temporal
Structure item, alongside the original four identifiability checks —
none dismissed as satisfied. `claim.md` now separates a cheaper,
non-causal C1 kill-test (does the frozen `S_M` shape appear at all) from
the full causal C2 mechanism claim this file's DAG serves. **A synthetic
four-world identifiability battery is now a hard pre-data gate** — the
pipeline must be shown not to false-PROMOTE on optical-depth-confounded
or merger-confounded mock data before it may touch anything real.

**[UPDATED 2026-09-11]** `claim.md` §8's own ordered list is now partly
done: (2) the costed data-acquisition plan (`data_acquisition_plan.md`)
and (3) the mock-catalog power analysis (`power_analysis_mock_catalog.py`,
`FINDING_power_analysis.md`, now including a real Exact Pair Census on
real ACT-DR5 MCMF positions, §6 of that file) both exist and are
`[VERIFIED-run]`. **(1), the synthetic four-world battery's own design
and pass/fail criteria, is still not written — this remains the hard
gate before any real kSZ/tSZ pipeline code (Fork 1b) may touch real
data.** The Exact Pair Census pulled real cluster catalog positions
(public, no login, `[VERIFIED]` row count) for pair-counting only — it
did not pull any kSZ/tSZ map or build any estimator, and is not itself
gated by the synthetic battery for that reason (no MULTING-relevant
statistic was computed from real measurement data, only geometry).

**[UPDATED 2026-09-11, 4th pass — s-dependent redesign.]** The window-
width question named as open above is now closed: `FINDING_window_
width_resolution.md`/NR-025 showed the fixed-window design has no
principled width, and this amendment replaces it. `§ Endpoint` and `§
Summary Measure` now use each real pair's own `(z,s)` continuously via
`ξ_pred(z,s)=(β₁/β₂)Q(z)(d₀/s)` — reusing the CLOSED branch's own
`Q(z)` trajectory table and the already-verified `d₀=45` Mpc, not new
physics. One new DAG-adjacent identifiability threat named (§
Consistency (d), small-`s` blending/deblending) and one existing check
(§ Positivity) is now directly checkable rather than merely plausible.
**[UPDATED 2026-09-11, 5th pass] Items (1) and (2) below are now DONE,
see `FINDING_power_analysis_s_dependent.md`:** the Positivity check
came back CONFIRMED (`3.978%` of real pairs already deterministically
above crossing) and the power analysis gives `98.6%` power at `N≈449`
(3x noise, two-part bar), with a full, uncapped power curve from
`N=10` to `2000`. **One real, un-closed risk surfaced by doing this
work, not before it:** the Positivity result's own driving pairs sit
right against the small-`s` instrumental cut named in § Consistency
(d) — that check must resolve before the Positivity result is trusted,
not treated as a formality.

**[UPDATED 2026-09-11, 7th pass] Item (1) below is now fully done, see
`FINDING_beam_blending_check.md` §3a:** all 306 real pairs behind the
Positivity fraction directly checked (not just the 5 illustrated ones)
— `301/306` (`98.4%`) clear `≥2×` beam FWHM; the blending-risk-excluded
Positivity fraction is `3.913%` vs. the original `3.978%`. Consistency
(d) is now a quantified, small correction, not an open threat.

**Next, in order:** (1) the sign-near-crossing PROMOTE sub-check (not
implemented in the power analysis's own `promote()`); (2) only then,
the synthetic four-world battery's own concrete design for THIS
Endpoint; (3) only then, code touching real kSZ/tSZ data. No such code
exists in this folder.
