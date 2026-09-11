# FINDING — mock-catalog power analysis: population definition decides
# whether the C1 kill-test is even runnable

**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Artifact:** `power_analysis_mock_catalog.py` — real code, real output,
`[VERIFIED-run]`. All inputs either directly cited (arXiv IDs given
inline) or explicitly flagged as an assumption; none invented silently.
**Continues:** `estimand.md`'s own MCID section ("not yet numeric... a
mock-catalog power analysis... before any real number is frozen") and
`data_acquisition_plan.md`'s Fork 2 (the 700-850 deg² footprint bound).

---

## 1. What this is, and what it is NOT

This answers the narrow, C1-scoped statistical question: **given a real
sample size and a real predicted signal shape, and assuming ONLY
measurement noise (no confounding, no measurement-validity threats), how
much data is needed to detect it?** It does **not** answer the C2 causal
question, and it does **not** run `estimand.md`'s own mandatory synthetic
four-world identifiability battery (MULTING / optical-depth-confounded /
merger-confounded / null) — that remains a separate, not-yet-built
artifact. This power analysis is a **best-case upper bound**: real power,
once confounding and measurement-validity threats are folded in, will be
lower than every number below.

---

## 2. The decisive finding: "the pair" definition changes N_pairs, and
## the narrow-window number was WRONG until corrected

**[AMENDED 2026-09-11 — external critique, independently verified before
applying, not accepted on its word.]** The original version of this
section used `20-45 Mpc PHYSICAL`, sourced from `pearl_registry`'s
2026-09-09 note calling `s0~30 Mpc` "v82's own characteristic node
separation." **That was a real provenance error, the same class this
project's own `docs/146` Category 11 already names**: `s0~30 Mpc` is a
*different* number with a *different status* — it is the cluster-
cluster-correlation-length value v82 *tried and explicitly rejected* as
an external grounding for `H0,anchor` (v82's own §IV.M). It is not v82's
own frozen initial condition for the pair separation itself.

**Checked directly against v82's own text before correcting anything:**
`data/source_material/buckholtz_202608.0943v1.v82.md:58-59`: *"the
physical distance vector `s(t)` between distinct nodes evolves
proportionally with the cosmic scale factor `a(t)` via `s(t)=a(t)x`."*
Line `:318`: *"`s(0) = d0 = 45`"* [Mpc]. **This project's own
`experiments/20260907-icm-expansion-correlation/FINDING_stage4_...md`
(read in full earlier this session, before this correction) already used
exactly `d(z)=d0/(1+z)`, `d0=45`** — its own table gives `d(z=0)=45.00`,
`d(z=0.5)=30.00` (`=45/1.5`, exactly) — independently re-confirming the
critique's correction from a file this project had already verified,
not merely from the critique's own say-so.

**The consequence for the separation window, worked through precisely,
not just corrected in direction:** since `x = d(z)·(1+z) = d0` is FIXED
by this formula, v82's own "spotlighted" background trajectory has a
**constant 45 Mpc COMOVING separation at every redshift** — not `20-45
Mpc physical` (the original error) and not the critique's own proposed
`32-71 Mpc comoving` either (that conversion applied `physical×(1+z)` to
an already-mismatched `20-45 Mpc` physical premise; the project's own
`d(z)=d0/(1+z)` formula gives a cleaner, different answer: a *constant*
45 Mpc comoving, not a redshift-dependent range).

| Window | N_pairs (Fork-2 mid footprint, 775 deg², LOWER BOUND) | Power @ 3x noise |
|---|---|---|
| 20-160 Mpc comoving (kSZ literature convention) | **~585** | 100% |
| ~~20-45 Mpc physical (WRONG — see above)~~ | ~~12~~ | ~~5.9%~~ |
| **[35,55] Mpc comoving (±10 Mpc around the verified 45 Mpc)** | **~17.7** | **8.4%** |
| **[20,70] Mpc comoving (±25 Mpc around the verified 45 Mpc)** | **~47.9** | **29.8%** |

**Verdict on the branch, corrected: neither "dead" nor "clearly viable."**
The corrected narrow-window numbers (18-48 pairs, 8-30% power depending
on the still-undetermined window *width*) are better than the erroneous
12-pair/5.9% result, but still well short of adequate power at any
reasonable significance target. **The window's center is now fixed
(45 Mpc comoving, verified); its width is not, and that remaining
free choice still swings power by a factor of ~3.5x (8.4% to 29.8%).**

---

## 3. Power results

**At the broad (585-pair) window** — Monte Carlo, `N_MC=4000` per cell,
`ΔAIC>6` + `|z|>1.96` as the PROMOTE criterion (matches this project's
own `FINDING_P166` AIC convention):

| N_pairs | noise = 1x signal RMS | 3x | 10x |
|---|---|---|---|
| 50 | 100.0% | 31.2% | 2.1% |
| 100 | 100.0% | 68.1% | 4.0% |
| **585 (Fork-2 estimate)** | **100.0%** | **100.0%** | **33.9%** |
| 5000 | 100.0% | 100.0% | 100.0% |

False-promote rate under the null stayed near the nominal `~0.5%`
throughout (below the `α=0.05` design level, since the `ΔAIC>6` bar is
stricter than the bare `z`-test alone) — the test is not spuriously
trigger-happy in this idealized setting.

**At the narrow (12-pair) window** — the same test collapses:

| noise | power | false-promote |
|---|---|---|
| 1x | 65.5% | 1.2% |
| **3x** | **5.9%** | 1.1% |
| 10x | 1.4% | 1.1% |

**At `n=12`, the test has essentially no power at any realistic noise
level** — 5.9% at 3x noise is barely above the false-promote rate itself,
meaning a PROMOTE verdict at that sample size would be nearly
uninformative regardless of whether MULTING is true.

---

## 4. What this means for the branch

**If "the pair" means the broad kSZ-statistic window:** the C1 kill-test
is well-powered at the Fork-2-estimated sample size, even under
pessimistic (3x) noise — a real, favorable result, *conditional on* the
marginal-to-joint `ξ`-scatter substitution (`claim.md` §3a's own flagged
`HYPOTHESIS`) holding up, and *conditional on* the confounding structure
being controlled well enough that the synthetic battery passes.

**If "the pair" means v82's own characteristic scale:** the branch is
**not viable as currently scoped** — 12 pairs cannot support this test
at any noise level this analysis considers realistic. The only way
forward in that case is enlarging the usable sky area (revisit Fork 1's
"request the collaboration data" option specifically for its potential
to cover much more sky than the from-scratch ACT+DESI construction can
reach), or accepting that this branch answers a question about the
kSZ-literature's own pairwise scale, not literally the scale in v82's own
text — a real, honest scope narrowing, not a technicality to paper over.

**This is now the single most consequential open decision in this
branch — more consequential than the data-acquisition cost itself.**

---

## 4a. [ADDED 2026-09-11] Two more critique items, checked and adopted

**Clustering bias direction, named precisely.** §3's own comoving-volume
pair count is a Poisson/unclustered lower bound, already flagged as such
before this amendment — real clusters are positively biased tracers
(`ξ_cc(r,z) > 0` at these scales), so the true close-pair count is
higher. This pulls in the *opposite* direction from downstream X-ray/
lensing/morphology selection cuts (which only remove objects). The two
effects were not combined into one number here — reported separately,
per the critique's own point that they should not be netted against each
other without a real calculation of both.

**Noise-model calibration — logged as an explicit, unverified
assumption, not implicitly inherited.** This script's Monte Carlo uses a
*relative* noise framing (1x/3x/10x the signal's own population RMS)
specifically because `data_acquisition_plan.md`'s Fork 1 already found
the source paper's own per-object noise budget is not public — the
9.3σ headline result comes from `913,286` DESI LRGs, not a few hundred
ACT clusters, and nothing in this script assumes that large-sample
optimism transfers to a cluster-scale sample. Named as a formal open
item regardless, per the critique's own suggested ledger convention:

```
A_noise: sigma_mock is adequate for a REAL cluster-scale kSZ estimator
         (not the large-N LRG sample the 9.3-sigma headline used)
STATUS: NOT VERIFIED. Bracketed (1x/3x/10x), not calibrated.
```

**Recommended next step, adopted from the critique, not yet built:**
before spending the multi-GB/multi-week effort `data_acquisition_plan.md`
costs for the full kSZ pipeline, run a much cheaper **Exact Pair Census**
— real `(RA, Dec, z)` triples from the actual ACT-DR5 MCMF catalog (or an
equivalent real, downloadable object list), real angular-to-comoving
conversion per pair, real `s_physical = r_comoving/(1+z_pair)` using
v82's own now-verified convention, and a real histogram `N_pair(s, z)` —
**no tSZ map, no kSZ map, no mass reconstruction needed for this step.**
This replaces the Poisson-volume model in §2/§4 with an exact count on
real positions, and would resolve the window-*width* ambiguity this
section's own table still carries. Not attempted in this pass — named as
the concrete next artifact.

## 5. What this does NOT establish

1. Not a real power number — a best-case, confounder-free upper bound.
   The synthetic four-world battery (`estimand.md`'s own hard gate) has
   not run; real power is lower.
2. Not a resolution of the marginal-vs-joint `ξ`-scatter substitution
   (`claim.md` §3a) — still `HYPOTHESIS`, carried forward as an assumption
   into this analysis, not validated by it.
3. Not a resolution of which separation window is correct — both numbers
   stand, the decision is named, not made.
4. Not a claim about MULTING (`NO_AUTHOR_ERROR`) — this is entirely about
   whether *this project's own reconstruction* of a test is statistically
   viable.

## Status

**[UPDATED 2026-09-11] Computed, corrected once, still not decided —
and correctly so.** Per the critique's own suggested status ledger,
adopted here:

```
Data availability (per-object kSZ table): CONFIRMED NOT PUBLIC
ACT source density (6237, arXiv:2406.14754):           VERIFIED
DES-Y3 x DESI-DR1 overlap (851.3 deg^2):                VERIFIED
ACT/eRASS1 four-way EXACT overlap:                      OPEN
Broad-window pairs (~585, 20-160 Mpc comoving):         MODEL-DERIVED
v82's own separation, d0=45 Mpc physical, s(0):         VERIFIED (corrected
                                                          from an earlier,
                                                          wrong s0~30 Mpc)
Narrow-window pairs (18-48, comoving, width TBD):       MODEL-DERIVED,
                                                          CENTER fixed,
                                                          WIDTH open
Noise model (A_noise, relative-noise bracketing):       NOT VERIFIED
"Narrow branch is dead":                                WITHDRAWN --
                                                          was based on the
                                                          wrong separation
"Narrow branch is viable":                              NOT YET ISSUED --
                                                          8-30% power is
                                                          real but weak
```

Next: the Exact Pair Census (§4a) — cheap, real-catalog-based, resolves
both the window-width ambiguity and replaces the Poisson-volume model
with an exact count. No code beyond this power-analysis script exists in
this folder; the synthetic four-world battery is still unbuilt.
