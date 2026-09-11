# claim.md — thermal-pair fingerprint: does real cluster-pair thermal
# scatter reach MULTING's own predicted sign-crossing?

**Experiment id:** `20260911-thermal-pair-fingerprint`
**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Origin:** an external, pasted AI-generated research proposal (not
authored by this project or by TJB), independently cross-checked against
this project's own prior work before being taken seriously — see
`pearl_registry/INDEX.md` row `2026-09-11` for the full verification
trail (math re-derived against `code/multing_core.py`, external citations
checked via 18 tool calls). This file freezes what survived that check
into an actual falsifiable claim, per this project's own hard rule: no
code until the claim is written down.

**STATUS OF THIS DOCUMENT: gate check only. Zero-Signal Gate PASSES
(§3) — unlike the adjacent, already-REFUSE'd branch this extends
(`experiments/20260907-icm-expansion-correlation`). That does NOT mean
code may start. `estimand.md` with a DAG and the four causal
identifiability checks is the next mandatory artifact (§2, §8) and does
not yet exist. No script in this folder yet.**

---

## 1. Step -3 — Novelty check (run first, per FL; it decides which
## branch this is)

`[VERIFIED-tool]` grep over `null_results/INDEX.md`, `parked/INDEX.md`,
`pearl_registry/INDEX.md`, and the adjacent experiment folder, per this
project's own Process Rule 1 (`CLAUDE.md`, added 2026-09-07 after
`P215`/`P216`/`P217`: check this project's own directories before
external literature).

### 1.1 An adjacent, structurally similar claim was already run and
### REFUSE'd — read before assuming this is the same thing

`experiments/20260907-icm-expansion-correlation/claim.md`: tested whether
MULTING's own force law predicts a sign-reversal in the pair-acceleration
response to thermal energy, **along the model's own smooth mean
z-trajectory** `k(z), R(z), M(z), d(z)`. Verdict: `REFUSE
(no_falsifiable_predicate_yet)` at first pass; then, after two follow-up
stages (`FINDING_stage3_floor_shares_the_sign.md`,
`FINDING_stage4_dflip_is_not_derivable_in_the_construction.md`), a
stronger closure: **`Q(z) = (β₂/β₁)·k(z)R(z)/(M(z)c²d(z)) > 1` at every
representable `z` from −0.95 to 16.9, minimum `1.7484` at `z=1.443`. No
reversal exists along the model's own trajectory.** That file's own §6
states explicitly what it did **not** test: *"not that a population
version is illegitimate — only that it is OURS, not the model's."*

### 1.2 What changed — one assumption, not a rebundling of the old one

Per the Adaptive Iteration Branch Rule (`falsification-ladder.md`): a
revived branch needs an explicit, stated changed assumption, not a blind
retry. Here:

| | closed branch (09-07) | this branch |
|---|---|---|
| population | the model's own smooth mean `z`-trajectory (one point per `z`) | **real, individual cluster pairs, with their own measured scatter around that mean** |
| dependent variable | `H_local` (local expansion rate, `s⁻¹`) — required a Cosmicflows-class dataset **absent from this repo**, and risked inheriting v82's own self-flagged `H0,anchor` peculiar-velocity circularity | **pairwise relative dynamics via kSZ** (a genuinely different observable — a two-point statistic between two specific tracked objects, not a local rate) |
| was the falsifiable predicate fillable? | **No** — `E21`'s own 12-group enumeration of v82's archive found no numbered result of that form | **Yes** — this project's own re-derivation (§3) supplies one, from the same frozen `(β₁,β₂)` already used for `PREREGISTRATION_v82_prospective_tests.md` |

**Revival condition, stated per the Branch Rule: a genuinely new
population source (real scatter, not the mean trajectory) AND a
genuinely new, previously-infeasible observable (kSZ pairwise dynamics,
not `H_local`) AND a newly-derivable predicate.** All three hold; this is
not a re-run of the closed branch under a new name.

### 1.3 The math is not new to this project either — named here so it
### is not silently rediscovered a third time

`ξ ≡ (K/(Mc²))·(R/s)`, the pasted proposal's own central variable, is
`FINDING_P208/P209`'s own `ψᵢ ≡ Kᵢrᵢ/(Mᵢc²)` divided by separation `s`.
`P208/P209` already used this exact combination to derive a real external
bound from MICROSCOPE (`η·|Δψ| ≤ 2.5×10⁻⁸ m`) and already established
that, for **laboratory materials**, `η=κ/g` cannot be given a number
because the model does not define composition-dependence of `k` sharply
enough. That specific blocker does **not** transfer here: for galaxy
clusters, `K` (thermal energy) is the directly intended, directly
observable quantity (via tSZ), not an undefined per-material postulate.
Recorded so a future session does not re-derive `ψ` a third time.

---

## 2. Step -2 — EstimandOps L0 classification

**Causal.** Identical reasoning to the closed branch's own §2: the
proposition is not "are thermal content and pairwise dynamics
associated" (descriptive) — MULTING's force law asserts that thermal
energy **sources** an additional, direction-specific force term that
**changes** pairwise dynamics relative to standard gravity. A merely
associational result does not support or refute this; ordinary structure
formation supplies competing causal paths for the same association
(shared dependence on cluster mass, environment, dynamical state,
selection effects — see the closed branch's own §4, which lists five).

**Consequence, per `estimand-ops.md`: a DAG and the four identifiability
checks (consistency, positivity, exchangeability, SUTVA) are required
before any result from this branch counts as evidence, in either
direction.** Not written here. This is the single largest piece of work
this claim.md defers — see §8.

---

## 3. Step -5 — Zero-Signal Gate

| field | content | pass? |
|---|---|---|
| **Entity** | Real, individually observed pairs of galaxy clusters (or cluster–cluster-pair systems within a larger kSZ-tracked catalog), matched on lensing mass, redshift, and large-scale environment | ✅ |
| **Falsifiable predicate** | MULTING's frozen spotlighted fit (`β₁=1.433479×10¹⁰`, `β₂=7.806760×10¹⁷`, same row `PREREGISTRATION_v82_prospective_tests.md` already froze) predicts, for identical-node pairs, `F/(GM²/s²) = −1 + 2β₁ξ − β₂ξ²`, `ξ=(K/(Mc²))(R/s)` — **independently re-derived against `code/multing_core.py`'s own `F0−F1+F2`, not just the pasted text `[VERIFIED-sympy][VERIFIED-file]`.** This has a computed, non-monotonic sign structure: net-attractive for `ξ` below `3.669×10⁻⁸`, net-repulsive above it (second root; the first root, `3.491×10⁻¹¹`, is unphysically small for real clusters). | ✅ **CAN BE FILLED** — unlike the closed branch, whose predicate could not be filled from v82's own archive at all |
| **Measurable outcome** | For real cluster pairs stratified by `ξ` (computed from tSZ-derived `K`, weak-lensing `M`, and catalog `R`, `s`), does pairwise dynamics (kSZ-inferred relative velocity, or an equivalent statistic) show the predicted `ξ`-dependence, INCLUDING entering net-repulsive behavior for the highest-`ξ` real pairs — after controlling for mass, redshift, separation, and environment? | ⚠️ conditional on §5, §8 |

**Verdict: PASSES.** Proceed to estimand-level design (§8), not to code.

---

## 4. The frozen numerical claim itself

Using v82's own **spotlighted** Table II row (`H0,anchor=73.2160`,
`χ²₃₃=15.7515`, already independently re-optimized to `<0.1%` by
`FINDING_E18`, the same row `PREREGISTRATION` froze):

```
xi_crossing = 3.668913e-08     [VERIFIED-sympy, cross-checked against
                                 code/multing_core.py's own force
                                 convention, not just the pasted text]
```

**Any change to `(β₁,β₂)` voids this number** and requires a new
pre-registration — same discipline `PREREGISTRATION_v82_prospective_
tests.md` already states for its own three predictions.

**Sharper than the closed branch's own framing.** Translating that
branch's own floor (`Q_min=1.7484` at `z=1.443`) into `ξ` gives
`ξ(z=1.443) ≈ 3.210×10⁻⁸` — only **~14% below** the crossing, not "75%
short" as the closed branch's own `β₂/β₁`-ratio framing reads (same
underlying fact; the function is steep near the root —
`d(F/F_N)/d(ln ξ) ≈ −1050` — so a modest distance in `ξ` corresponds to a
large distance in `β`-ratio space).

**Why real scatter plausibly closes a 14% gap, not asserted, computed:**
`FINDING_E13` measured `σ=0.49` (natural-log, i.e. ≈63% per 1σ) intrinsic
scatter in the real `M_gas–T` relation this project's own force-law
reconstruction depends on (`[VERIFIED-arXiv:2511.14356]`, Ramos-Ceja et
al. 2026). A 63%-per-1σ scatter comfortably covers a 14% gap for a
non-trivial tail of real pairs — this is the empirical basis for
expecting the crossing to be reachable by real, individual pairs even
though the model's own smooth mean trajectory never reaches it.

---

## 5. Feasibility — checked, not assumed

`[VERIFIED-REAL]`, via a background citation-verification pass (18 tool
calls, real abstracts fetched, not search snippets):

| ingredient | status |
|---|---|
| `K` via tSZ (Compton-`Y`) | ✅ ACT DR6 Compton-`y` maps are real and public (NASA LAMBDA), ILC-constructed, ~13,000 deg² |
| `M` via weak lensing | not independently checked this pass — standard, widely available (DES, KiDS, HSC); assumed feasible, not verified here |
| pairwise dynamics via kSZ | ✅ real: DESI DR1 + ACT DR6 + Planck give a `9.3σ` pairwise-kSZ detection, `arXiv:2511.23417` [VERIFIED-REAL], 913,286 LRGs |
| **per-cluster ("individual") peculiar velocities** | ⚠️ **real risk, found by the citation check, not by the original proposal**: the `456,803`-object per-object velocities are **not measured** — they come from an ML model trained on simulations to estimate each object's optical depth `τ`, combined with the measured kSZ signal. A pair-by-pair (not population-statistic) design inherits whatever assumptions about standard gravity/structure formation are baked into that training. **This must be addressed explicitly in `estimand.md`'s identifiability section (§8) before any result counts** — it is exactly the kind of confound `estimand-ops.md`'s exchangeability check exists to catch. |
| X-ray cross-check (`T`, independent of tSZ) | ✅ eROSITA eRASS1 real, `12,247` clusters, `[VERIFIED-arXiv:2402.08452]`; per-cluster temperatures exist in eRASS1 itself (not only via eFEDS, which is a separate, deeper, largely non-overlapping companion survey — corrects a citation error in the original pasted text) |

**No dataset has been downloaded or touched in this repo for this
branch.** This section establishes that the ingredients exist publicly,
not that acquisition is done.

---

## 6. Counterfactual frame (FL Step -0.5, research claim)

**In what world is this claim true?** A world where thermal energy
gravitates with the sign and magnitude MULTING's fitted `(β₁,β₂)`
assign it — i.e., where the repulsive quadrupole term is real and not an
artifact of the fit to `H(z)` alone. In that world, real cluster pairs
with unusually high thermal content relative to their mass and
separation should show measurably different pairwise dynamics from
otherwise-matched, thermally-ordinary pairs, with the specific,
non-linear `ξ`-dependence derived in §4 — not just "some effect," a
**shaped** one, including the sign-crossing.

**In what world is it false, cleanly?** A world where pairwise dynamics
depend only on gravitating mass, redshift, and environment, with no
detectable residual dependence on thermal content once those are
controlled — the standard-gravity null this branch is built to
distinguish from.

**How many independent changes would it take to save MULTING if this
comes back null?** At least one: the `k`-postulate itself (`MODEL_SPEC_
AUDIT.md`'s own OPEN row) would need revision to decouple the fitted
`(β₁,β₂)` from a literal thermal-energy interpretation of `K` — the same
open question `experiments/20260907-icm-expansion-correlation/claim.md`
§6 already names as the shared upstream bottleneck for this entire
family of tests.

---

## 7. What this claim does NOT establish

1. **Not that MULTING is right or wrong** (`NO_AUTHOR_ERROR`). This is a
   pre-registration gate check on this project's own reconstruction.
2. **Not that the data acquisition is trivial.** §5's ML-inferred-velocity
   caveat is a real, unresolved identifiability concern, not a footnote —
   it may turn out to block a genuine pair-by-pair design entirely,
   forcing a population-statistic redesign instead.
3. **Not that this supersedes or reopens
   `experiments/20260907-icm-expansion-correlation`.** That branch's own
   `REFUSE` stands for its own predicate (`H_local`, model's own mean
   trajectory). This is a structurally distinct branch, per §1.2.
4. **Not a claim that the external pasted proposal was reliable as a
   whole.** Two of its citations were caught mischaracterizing their
   sources (DESI DR2 Lyα direction; scope of the cited symbolic-
   regression paper) — see `pearl_registry/INDEX.md`. Only the parts that
   survived independent verification are carried into this file.
5. **Not yet a DAG, not yet an identifiability check, not yet code.**

---

## 8. Decision — gate result, not a go-ahead to build

**Zero-Signal Gate: PASS. Causal claim: requires estimand.md + DAG before
anything counts. Neither written yet.**

Next artifact, in order, per `estimand-ops.md`'s own Full-Ladder stack
(estimand precedes claim for causal research claims — this file inverted
that order deliberately, to freeze the falsifiable numbers first, since
those were the part inherited from an external, unverified source and
needed checking before any further investment):

1. **`estimand.md`** — population (real inclusion/exclusion criteria for
   cluster pairs), comparator (standard-gravity null, stated precisely),
   endpoint (the exact pairwise-dynamics statistic), MCID, ICE strategy
   for mergers/selection effects, and — because this is causal — a DAG
   naming every plausible confounder from the closed branch's own §4 list
   (mass, environment, dynamical state, selection/estimator effects) plus
   the new one this file surfaces (the kSZ velocity estimator's own
   training-simulation dependence), with the four identifiability checks
   run against it.
2. Only after `estimand.md` passes its own gates: a data-acquisition plan
   (ACT DR6 / DESI kSZ products, a lensing mass catalog, eROSITA/CHEX-MATE
   for an independent X-ray cross-check per the pasted proposal's own
   "Path A / Path B" independence idea) — costed, not assumed free.
3. Only after that: code.

**No script exists in this folder. None should, until step 1 above is
written and passes its own gates.**
