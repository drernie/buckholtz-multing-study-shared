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

## 6. Exact Pair Census — real catalog result [ADDED 2026-09-11]

**Continues §4a's own named next step.** `exact_pair_census.py` replaces
§2's Poisson-volume model with an exact pairwise-separation count on
**real** `(RA, Dec, z)` positions — the ACT-DR5 MCMF catalog (Klein, Mohr
& Davies 2024, `arXiv:2406.14754`), downloaded directly from CDS
(`cdsarc.cds.unistra.fr/ftp/J/A+A/690/A322/`, public, no login). **6237
rows — `[VERIFIED]` matches the paper's own abstract count exactly.**
`4390` clusters survive the same `z∈[0.2,0.8]` cut used throughout this
branch. The catalog's own `fcont1C` contamination column is already
capped at `<0.2` in the public table (`max=0.19988`, checked directly,
not assumed) — no separate purity cut needed on top of the catalog's own
default selection.

**Method:** real `(RA,Dec,z)`→Cartesian comoving-Mpc conversion via
`astropy.cosmology.Planck18` (same cosmology as §2-§3c), a `scipy`
`cKDTree` sparse-distance-matrix pairwise search (no `N²` loop, no
`healpy` needed — this sidesteps the Fork-2 footprint-intersection
blocker entirely, since exact positions make an assumed-area Poisson
model unnecessary for the pair COUNT itself), and a direct histogram of
the `14200` real pairs found within `200` Mpc comoving.

**Exact counts, full ACT-DR5 MCMF footprint (`13211 deg²`,
`[VERIFIED-arXiv:2406.14754]`, corrects §1's own `13750` deg² ACT-DR6
proxy), `z∈[0.2,0.8]`:**

| Window | Real exact count (full footprint) | Real, area-scaled to Fork-2 mid (775 deg²) | Step 3c's Poisson-model number (same footprint) |
|---|---|---|---|
| broad `[20,160]` Mpc | 7651 | **449** | 585 |
| narrow-25 `[20,70]` Mpc | 910 | **53** | 48 |
| narrow-10 `[35,55]` Mpc | 374 | **22** | 18 |

**Two separate real effects are visible here, not one — kept distinct
per this project's own `feedback_verdict_attribution.md` discipline
(don't merge two independent causes into one number):**

1. **Real clustering pulls the narrow-window ratio UP**, exactly the
   direction `§4a`'s own clustering-bias note predicted: real
   `narrow-10/broad = 0.0489` vs. the idealized Poisson model's
   `0.0303` (narrow-25 similarly: `0.1189` vs `0.0819`). Real clusters
   really are positively-clustered tracers, not a Poisson field.
2. **A separate, newly-found provenance gap in §1's own density
   input**: `density_per_deg2` there was computed from the FULL catalog
   (`6237` clusters, all `z∈[0.04,2]`) divided by area, then applied as
   if that were the density *within* the `z∈[0.2,0.8]` shell — but only
   `4390/6237` (`70.4%`) of real clusters actually fall in that shell.
   This inflated §2's `N_clusters_mid` input by a factor of `~1.42×`,
   which — since pair count scales roughly as `N²` at fixed volume —
   substantially inflated the broad-window Poisson estimate specifically
   (`585` vs. the real, clustering-corrected `449`). This is the same
   class of error `docs/146` Category 11 already names (a stale/
   mismatched-scope input silently reused), caught here by direct
   comparison against real data, not by a pasted critique.

**Power, re-run with `one_trial()` (identical Monte Carlo methodology,
`N_MC=4000`, `ΔAIC>6` + `|z|>1.96`, `power_analysis_mock_catalog.py`
Step 3d) at the real, area-scaled counts:**

| Window | low (700deg²) | mid (775deg²) | high (850deg²) |
|---|---|---|---|
| narrow-10, N=20/22/24 | 9.4% | 10.7% | 11.5% |
| narrow-25, N=48/53/59 | 29.7% | 34.0% | 37.9% |
| broad, N=405/449/492 | 100.0% | 100.0% | 100.0% |

**Reading:** real clustering gives a real but modest power improvement
over Step 3c's idealized numbers (narrow-10: `8.4%→10.7%` at mid
footprint; narrow-25: `29.8%→34.0%`) — roughly `+2 to +4` percentage
points, not a qualitative change. **The branch's own verdict is
unchanged: "weak, not dead."** The window-*width* choice remains the
free, undetermined parameter (`10.7%` vs `34.0%` is still a `~3×`
swing). The area-scaling from the full ACT-DR5 footprint to the
`700-850 deg²` Fork-2 target is still a first-order **linear**
approximation, explicitly flagged in `exact_pair_census.py` itself — it
assumes uniform cluster density and clustering statistics across the
sky, which the real DES-Y3/DESI-DR1/eRASS1 cross-match (still not done)
could push in either direction. This step answers the *shape* question
(§4a's own framing) honestly; it does not close Fork 2.

## Status

**[UPDATED 2026-09-11, 2nd pass] Exact Pair Census run — narrow-window
pairs upgraded from MODEL-DERIVED to VERIFIED (real positions); the
window-WIDTH question remains open, correctly so.**

```
Data availability (per-object kSZ table): CONFIRMED NOT PUBLIC
ACT source density (6237, arXiv:2406.14754):           VERIFIED
DES-Y3 x DESI-DR1 overlap (851.3 deg^2):                VERIFIED
ACT/eRASS1 four-way EXACT overlap:                      OPEN --
                                                          still not
                                                          resolved by
                                                          the Exact Pair
                                                          Census (that
                                                          used ACT-DR5
                                                          MCMF alone,
                                                          linearly
                                                          area-scaled)
Broad-window pairs (20-160 Mpc comoving):               VERIFIED (real
                                                          census: 449 @
                                                          mid footprint,
                                                          not 585 --
                                                          see SS6)
v82's own separation, d0=45 Mpc physical, s(0):         VERIFIED
Narrow-window pairs (comoving, width TBD):              VERIFIED (real
                                                          census, SS6):
                                                          22 (+-10 Mpc),
                                                          53 (+-25 Mpc)
                                                          @ mid footprint.
                                                          WIDTH still open.
Noise model (A_noise, relative-noise bracketing):       NOT VERIFIED
Area-scaling to Fork-2 target (linear, ACT-wide->775deg^2): NOT VERIFIED,
                                                          flagged
                                                          explicitly as
                                                          first-order
"Narrow branch is dead":                                WITHDRAWN
"Narrow branch is viable":                              NOT YET ISSUED --
                                                          10.7%-34.0%
                                                          power (real
                                                          census) is
                                                          real but weak,
                                                          modestly better
                                                          than the
                                                          idealized model
```

Next, in order: (1) resolve the ACT/eRASS1/DES/DESI four-way exact
footprint (replaces the linear area-scaling caveat with a real
cross-match — the one remaining open item from `data_acquisition_
plan.md`'s Fork 2); (2) only then does a window-WIDTH decision have a
real, non-approximated sample size behind it; (3) the synthetic
four-world identifiability battery (`estimand.md`'s own hard gate)
remains unbuilt and is not affected by this update — it is orthogonal
to sample size.

**[UPDATED 2026-09-11, 3rd pass] Item (2) above is now moot — the
window-width question is RESOLVED (negative), see
`FINDING_window_width_resolution.md`.** Power is monotonic in width
(no interior optimum, `N≳15`), and the real two-point correlation
`1+ξ(s)` computed directly from this catalog shows no local feature at
`s=45` Mpc — it is a smoothly declining function, and `[40,50)` is not
even a local maximum among its own neighboring bins. `s=45` Mpc has no
independent support from real cluster clustering; it remains solely
`v82`'s own model-internal initial condition. **The fixed-window count
test design itself is REJECTED** (`null_results/INDEX.md` NR-025) — not
the underlying MULTING mechanism, which survives untested by this
specific design. A genuinely different test (fit `S_M`'s predicted
`s`-dependence against each real pair's own separation, not a window
count) remains a live, un-adopted option requiring an `estimand.md`
amendment before any code.
