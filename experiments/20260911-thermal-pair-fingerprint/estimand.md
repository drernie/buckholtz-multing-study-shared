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

Headline, corrected: broad kSZ-literature window (585 pairs) still gives
~100% power at 3x noise; the corrected narrow window, centered on the
verified 45 Mpc but with its *width* still undetermined, gives **18-48
pairs and 8-30% power** — real but weak, neither dead nor adequately
powered. The window-width choice remains the single most consequential
open decision in this branch. **All numbers are best-case, confounder-
free upper bounds** — the synthetic four-world battery has not run; real
power will be lower. Next: the Exact Pair Census (`FINDING_power_
analysis.md` §4a) — real catalog positions, not a Poisson-volume model —
to resolve the width question directly instead of guessing among window
choices.

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

**[UPDATED 2026-09-11]** Estimand written, DAG now includes the `G`
(shared-electron-gas) backdoor path and a fifth, non-classical Temporal
Structure item, alongside the original four identifiability checks —
none dismissed as satisfied. `claim.md` now separates a cheaper,
non-causal C1 kill-test (does the frozen `S_M` shape appear at all) from
the full causal C2 mechanism claim this file's DAG serves. **A synthetic
four-world identifiability battery is now a hard pre-data gate** — the
pipeline must be shown not to false-PROMOTE on optical-depth-confounded
or merger-confounded mock data before it may touch anything real.

No data pulled. No code exists in this folder. Per `claim.md` §8 as
amended: next is (1) the synthetic battery's own design and pass/fail
criteria (not yet written — this file only mandates that it happen), (2)
a costed data-acquisition plan, (3) the mock-catalog power analysis this
file's own MCID section requires. Code remains gated behind all three.
