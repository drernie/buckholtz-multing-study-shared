# docs/162 — ONTOLOGY_SPEC_v82: what v82's own text says each symbol
# in its force law and kinematic bridge physically IS, before any
# further computation

**Date:** 2026-09-12
**Status:** FROZEN specification, not a new claim about the physical
universe. Every field below is either `[SETTLED]` (direct, cross-
checked primary-source text, no ambiguity found) or `[OPEN]` (the
text does not settle it, per Step 8a skeptic review).
**Source:** `experiments/20260803-bridge/CLAIM_P230_what_physically_
is_a_node.md` + `FINDING_P230_what_physically_is_a_node.md` (full
citations, line numbers, and skeptic Response Matrix there — not
repeated here). **User-requested and user-designed** (the 9-field
structure below is the user's own).
**L0:** descriptive (what does v82's text say) — `NO_AUTHOR_ERROR`,
this is not a claim about v82's own theory being right or wrong.

---

## 1. What is a "node"?

`[SETTLED, narrowly]`: a node's OPERATIONALLY-MEASURABLE properties
(mass, radius, thermal energy) are explicitly tied to real galaxy-
cluster ICM (intracluster medium) physics. A node is located where
`>=2` cosmic-web filaments overlap, and "includes" one galaxy cluster
or a few.

`[OPEN]`: whether the force-law mass `m_X` is numerically coextensive
with `M_cluster` specifically, or a total node-region mass of which
the cluster is the dominant but not necessarily exhaustive component
(the text says a node "includes" a cluster, not "is" a cluster — a
real distinction, not pedantry, per Step 8a).

## 2. What does `M` mean?

`[SETTLED]`: `m_X(z) = m_0 * (1+z)^-1.1` (Eq. 10) — an empirical power
law relative to a low-redshift baseline `m_0`. This `m_0` is the SAME
symbol used in the R500 formula (item 3) — v82 states this identity
directly, not left to inference.

`[OPEN]`: which real-world mass (`M500c` of the visible cluster? a
broader node-region total?) `m_0` numerically corresponds to — see
item 1.

## 3. What does `R` mean, including R500?

`[SETTLED]`: `r_X(z)` is DERIVED from `m_X(z)`, not independently
fit — via the standard `R500`-type relation, `r_0 = [3*m_0/(4*pi*500*
rho_crit,0)]^(1/3)`. Stated TWICE in v82's own text (once introducing
the relation, once flagging it as the framework's "most serious
residual circularity" — v82's own words). **Confirmed by direct grep
of the whole document: no `R200`/`M200` convention appears anywhere.**
This is a genuine, load-bearing mismatch with this project's entire
prior simulation work (TNG300/FLAMINGO/Magneticum all used `M200c`).

`[SETTLED, 2026-09-12 update — real measurement replaces the earlier
[MEMORY]-tier estimate]`: on FLAMINGO's real SOAP catalog (`M200c` and
`M500c` for the same halos), `M500c/M200c` ratio `mean=0.676,
median=0.689, SD=0.0715` — matches the standard NFW-profile range
(`~0.68-0.72`) to the third decimal. Top-`N` overlap measured directly:
`N=35 -> 91.4%`, `N=50 -> 74.0%` (a `~2 sigma` single-point anomaly,
mechanism undiagnosed), `N=1200 -> 91.8%`. **`[OPEN, sharpened, not
closed]`**: overlap fraction does NOT by itself answer whether any
already-reported correlation (`rho_NN`, `rho_band`) would shift under
an `M500c`-based re-selection — the swap is systematically biased by a
real physical property (dynamical state/concentration), not random,
so overlap and statistic-stability are DIFFERENT questions. A direct
before/after recompute of an actual correlation on both selections is
the real next step, not yet run. Full account: `experiments/20260909-
tng-mass-assortativity/FINDING_flamingo_m500c_m200c_overlap.md`.

`[UPDATE, 2026-09-12, same day — the direct recompute was run]`: at
`N=1200` (this branch's own "definitive global estimand"), `rho_NN`
under `M200c`- vs. `M500c`-selection differ by only `-0.0032` — `~15x`
smaller than the real jackknife `SE` (`0.0476`) — **the definitive
estimand is confirmed robust to this mass-convention choice.** At
`N=50` (matching the TNG300/subcube saga's own scale), the same
comparison shows a larger raw shift (`0.32 -> 0.08`) but its honest
significance is ambiguous (`z~0.7-1.6`, not a clean detection) and its
MECHANISM (selection-effect vs. correlated-value-effect — a `2x2`
factorial design gap, Step 8a-caught) is unresolved. **Net: the
branch's strongest number is safe; the smaller-`N` concern remains a
real but unconfirmed open question**, not "settled either way." Full
account: `experiments/20260909-tng-mass-assortativity/FINDING_
flamingo_rho_nn_m200c_vs_m500c_selection.md`.

`[UPDATE, 2026-09-12, same day — the 2x2 factorial gap was closed]`:
the mechanism question above is answered, but not as "X is the
driver." All four cells of the selection x correlated-value factorial
were measured at `N in {35, 50, 1200}`. At `N=50`, the interaction term
between selection-criterion and mass-convention (`+0.22`) is
comparable to or larger than either individual main effect (range
`0.10`-`0.34`); the value-convention effect literally flips sign
depending on which selection is held fixed. Step 8a skeptic verdict:
WEAKENED — the claim's own pre-registered decision rule ("if X small
and Y large -> driver=value; reverse -> driver=selection") fires in
neither direction. **Honest conclusion: selection-criterion and
mass-convention are entangled at `N=50`, not separable into a single
driver.** At `N=1200` all four cells and their differences remain tiny
(`<=0.03`), unaffected. No added statistical power over the prior
`z~0.7-1.6` framing (the four cells share ~74%-overlapping objects, not
independent samples). Full account: `experiments/20260909-tng-mass-
assortativity/FINDING_flamingo_rho_nn_2x2_factorial.md`.

## 4. What does `K` (thermal energy) mean?

`[SETTLED]`: the total kinetic energy of nucleons and electrons
comprising the ICM of a node; `70-90%` of a node's ICM kinetic energy
is thermal energy (real citations: Battaglia et al. 2012, Lau et al.
2009, Voit 2005 — all independently verified as real). This thermal
energy is the physical basis v82 proposes for the dipole force term
(analogy with electromagnetism: bulk/ordered motion does not couple,
thermal/isotropic pressure-like energy does — v82's own Sec. IVF
argument, not re-derived here).

## 5. What is the separation `s`?

`[SETTLED]`: the length of the vector from node-A to node-P — a
literal pairwise separation between two SPECIFIC nodes, used directly
in the force law (Eqs. 1-4).

## 6. Where does `d0` (`s0`) come from?

`[SETTLED]`: `s0` is v82's own kinematic-bridge free parameter (Eq.
22, `H0,anchor = s0-dot/s0`) — "the relative separation between two
TYPICAL nodes, today." v82 explicitly tried to ground it directly in
data ("could `s0` and `s0-dot` be grounded directly in data... We
attempted this") via the cluster-cluster correlation length,
`s0~30 Mpc` (ref `[91]`, Basilakos & Plionis 2004) — but ABANDONED
this specific attempt because combining it with pairwise-velocity data
(ref `[92]`, Cen/Bahcall/Gramann 1994) gave an implausible
`H0,anchor~11 km/s/Mpc`. **v82 never disavows the correlation-length
NUMBER itself or the type of statistic it comes from — only the
velocity-side combination.**

## 7. Is `d0` an individual pair-separation rule, or a population
## correlation length?

`[SETTLED, independently re-verified against the cited paper's own
real abstract/results, not assumed]`: `r0` in Basilakos & Plionis 2004
is a POPULATION-LEVEL clustering-amplitude parameter from a fitted
power-law two-point correlation function, `xi(r) = (r0/r)^gamma` —
mathematically the scale where `xi(r0)=1` for a given cluster
subsample. **It is explicitly RICHNESS-DEPENDENT**: the paper reports
`r0=20.7 (+4.0/-3.8) h^-1 Mpc, gamma=1.6` for a richer cluster
subsample and `r0=9.7 (+1.2/-1.2) h^-1 Mpc, gamma=2.0` for a poorer
one — two different numbers from the SAME paper, depending on which
mass/richness cut is used. **`d0` is NOT, and was never claimed by v82
to be, a "distance to your nearest similarly-massive neighbor" rule.**

## 8. Which exact statistic from `[91]` corresponds to v82's own
## number?

`[SETTLED]`: the RICHER of the two subsamples. `20.7 h^-1 Mpc`,
converted to physical Mpc via `h~0.7`, gives `~29.6` Mpc — matching
v82's own `"s0~30 Mpc"` almost exactly (the poorer subsample's
`9.7 h^-1 Mpc ~ 13.9` Mpc physical does not match). This is a positive
finding about v82's own citation fidelity, checked directly, not
assumed.

## 9. What observable estimand does P158 actually need?

**Not yet settled — this is the next real step, not a computation to
run today, per the user's own explicit instruction.** What items 1-8
above jointly constrain:

- The estimand should be built around a REAL cluster-cluster (or
  cluster-mass-proxy) TWO-POINT CORRELATION FUNCTION on a mass-defined
  population, `xi(r)` or a mass-marked generalization of it — NOT a
  nearest-neighbor-order-statistic on a hard top-`N` rank cut. This is
  the single biggest actionable correction from this whole spec.
- The population should be selected/reported using `M500c`-convention
  masses where available (not `M200c`), or with an explicit, checked
  bridge between the two if only `M200c` is available in a given
  catalog.
- Whatever separation scale is used to match v82's own construction
  should be understood as a POPULATION clustering-amplitude parameter
  (richness/mass-cut-dependent, per item 7-8), not a fixed universal
  "40-45 Mpc" target to hit via sample-thinning — the entire `top-N`/
  `subcube`/`density-matching` design chain in this branch's prior work
  was, in retrospect, built to answer a question (median NN distance
  in a scale-matched subsample) that is NOT the question v82's own
  cited empirical route actually poses.
- **Does NOT** mean prior `rho_NN` results were computed incorrectly —
  they remain valid measurements of what they measured. Their
  relationship to v82's own pair/node ontology is what changes status,
  from "the intended test" to "a related but not source-faithful
  proxy."

**[UPDATE, 2026-09-13 — first real computation run, not a final
answer].** `experiments/20260909-tng-mass-assortativity/FINDING_
flamingo_2pcf_m500c_estimand.md`: a real `xi(r)=DD(r)/RR(r)-1` two-
point correlation function (exact analytic `RR(r)` for FLAMINGO's
periodic box, no random catalog needed), on `M500c`-selected clusters
(directly from the full catalog, not re-ranked from an `M200c` pool).
Step 8a skeptic: WEAKENED. **Survives**: FLAMINGO's own clustering
amplitude (`r0 ~ 13-24` h^-1 Mpc across `N=200`-`5000`, robust to
outlier/weighting corrections at the `~8%` level) lands in the SAME
ORDER OF MAGNITUDE as v82's own cited anchor (Basilakos & Plionis 2004,
`9.7-20.7` h^-1 Mpc), and the DIRECTION of richness-dependence matches
(richer proxy -> larger `r0`) — a genuine, previously-unchecked
corroboration that FLAMINGO is a plausible stand-in population.
**Does NOT survive unqualified**: the correlation-function SHAPE
(`gamma`) is systematically steeper in FLAMINGO (`2.1-2.6`) than in the
cited literature (`1.6-2.0`) under every fit tried (unweighted,
outlier-excluded, Poisson-weighted) — a real, unresolved disagreement.
Five further structural confounds (selection function, redshift,
cluster-definition mismatch, estimator differences, unmatched fit
range) remain unaddressed, and no mass-assortativity `rho` has been
computed yet (this first pass measures spatial clustering amplitude
only). **Item 9 is not closed by this** — it establishes the estimand-
construction direction is viable, not that it is finished. Next named
(not attempted) step: a mass-marked generalization of this same
periodic-box estimator, to give `rho` a source-faithful 2PCF-style
analog replacing the now-closed `rho_NN` design.

**[UPDATE, 2026-09-13 — the mass-marked generalization was built, run,
and skeptic-reviewed].** `experiments/20260909-tng-mass-assortativity/
FINDING_flamingo_mark_correlation_rho_of_r.md`: `rho(r)`, the Pearson
correlation of paired `log10(M500c)` among ALL pairs in each of 15
separation bins (`5-150` Mpc), with a mark-shuffle permutation null and
a cell-block positive control (closing the prior 2PCF pipeline's own
"no canary" gap). Step 8a skeptic: WEAKENED. **Result: at `N=5000`
(best-powered, all 15 bins testable), NO mass-assortativity signal
detected anywhere in the range** — the one nominally-significant bin
(`p=0.015`) is fully consistent with the multiple-comparisons noise
floor (`1` of `33` tests, below the `1.65` expected) and sits inside
the pipeline's own demonstrated `|z|~3` per-bin RNG noise floor (from
the positive control's own off-target excursion). **This is a genuinely
new, independent-methodology confirmation of the branch's already-
established null** (`N=1200` `rho_NN~=0`), now on the source-faithful
`M500c` convention, across the full `5-150` Mpc range, with a
literature-standard mark-correlation design. At `N=200`/`N=1000`, many
small-`r` bins were UNTESTABLE (too few pairs), not null — an explicit,
disclosed distinction, not smoothed over. **This closes the direct
P158-motivating mass-assortativity question on the strongest design
this branch has built**, while item 9's separate spatial-clustering
shape-mismatch caveat (`gamma` steeper than the cited literature) stays
open.

**[FINAL CLOSURE, 2026-09-13 — item 9's own experimental/computational
investigation is now complete, user-requested definitive closure]**.
`experiments/20260909-tng-mass-assortativity/FINDING_flamingo_2pcf_
gamma_range_diagnostic.md`: the residual `gamma`-mismatch caveat was
investigated one more turn — re-fitting the ALREADY-RECORDED `xi(r)`
values over alternative `r`-ranges (no new download). Step 8a skeptic:
WEAKENED (a real but PARTIAL explanation, not "resolved" as first
drafted). Applying `docs/151`'s three-field status separation to close
item 9 as a whole:

> **Empirical/Model status — `r0` (spatial clustering amplitude):
> CONFIRMED, robust.** Order-of-magnitude and richness-dependence
> direction match v82's own cited anchor (Basilakos & Plionis 2004),
> independent of fit-range choice — the branch's most solid new result
> under item 9.
>
> **Empirical/Model status — `gamma` (clustering shape): PARTIALLY
> EXPLAINED, genuinely OPEN, out of scope for this branch's own
> toolkit going forward.** Fit-range curvature (independently confirmed
> real, local-slope trend `r=0.74`) explains roughly a third to half of
> the originally-flagged gap. A `~0.5`-unit residual remains even under
> the best-powered, range-corrected, subsample-matched comparison
> (FLAMINGO's mass-selected sample corresponds to Basilakos & Plionis's
> RICHER subsample, `gamma=1.6` — not the numerically-closer but
> physically-wrong "poorer" value this branch initially compared
> against). Closing this residual would require real observational
> cluster data (matched selection function, redshift, cluster
> definition) — outside what a simulation-only toolkit can resolve.
> **Explicitly left open, not chased further** — this is the honest
> stopping point, not an oversight.
>
> **Empirical/Model status — `rho(r)` (mass assortativity): CLOSED.**
> No signal detected anywhere in `5-150` Mpc at the best-powered test
> (`N=5000`), an independent-methodology confirmation of the branch's
> already-established null. This directly answers the question that
> originally motivated `P158`.
>
> **Ontological/mechanistic interpretation status: CLOSER, not
> IDENTICAL, to v82's own cited empirical route.** The 2PCF-style
> design (population-level clustering statistic, `M500c` convention) is
> a genuinely better match to what v82's own text cites (Basilakos &
> Plionis's 2PCF amplitude) than the earlier nearest-neighbor designs
> — but FLAMINGO's `z=0` simulated halos are still not identical to a
> real, redshift-averaged, selection-function-matched observational
> cluster catalog. An approximation, not a reproduction.
>
> **Causal/cosmological claim status: NON-IDENTIFIED**, as with every
> other result in this branch (`NO_AUTHOR_ERROR`) — none of this
> establishes anything about v82's own theory being right or wrong.

**Item 9 is now CLOSED as an active investigation thread.** No further
FLAMINGO-based tests are planned for it. Full account (3 linked
FINDINGs): `FINDING_flamingo_2pcf_m500c_estimand.md`, `FINDING_
flamingo_mark_correlation_rho_of_r.md`, `FINDING_flamingo_2pcf_gamma_
range_diagnostic.md`.

## Retrospective classification of prior work (per the user's own
## request: audit against this spec, do not recompute)

| Prior result | Classification against this spec |
|---|---|
| `P223` finite-r force-law algebra (sympy derivation) | **NOT AFFECTED** — pure symbolic manipulation of v82's own Eqs. 1-9, no population/statistic choice involved. |
| TNG300/Magneticum/FLAMINGO `rho_NN` (all variants, all 4 subcube-saga tests) | **NUMERICALLY VALID, ONTOLOGICALLY MISMATCHED** — real, correctly-computed nearest-neighbor mass correlations; not a source-faithful test of v82's own cluster-cluster-correlation-function-based separation concept. |
| `rho_band` (all-pairs-in-a-40-45-Mpc-band) | **CLOSER in spirit to a 2PCF-style statistic** than `rho_NN` (pairs within a separation band, not just nearest-neighbor) — but still computed on an `M200c`-selected, hard-top-`N`-thresholded population, not a full 2PCF fit — **PARTIALLY MATCHED**, closest existing result to what item 9 recommends, still not the same statistic. |
| `FINDING_P158`'s own `rho<=-0.5` directional-safety conclusion | **STATUS REOPENED** — the underlying numeric result stands, but its claim to test v82's own pair-population specifically is weakened pending a source-faithful estimand. |

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
