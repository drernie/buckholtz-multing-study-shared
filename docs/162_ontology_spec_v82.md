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

`[OPEN]`: the practical size of the resulting mismatch for already-
reported rank-based correlations — plausibly modest but NOT
quantified (Step 8a: `M500c/M200c` is monotonic ON AVERAGE with real
concentration-driven scatter, `~5-10%`; expected top-`N` selection
overlap `~90-95%`, not "nearly all" — cheap, not-yet-run kill-test:
cross-match halo IDs ranked both ways in one already-available
snapshot).

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

## Retrospective classification of prior work (per the user's own
## request: audit against this spec, do not recompute)

| Prior result | Classification against this spec |
|---|---|
| `P223` finite-r force-law algebra (sympy derivation) | **NOT AFFECTED** — pure symbolic manipulation of v82's own Eqs. 1-9, no population/statistic choice involved. |
| TNG300/Magneticum/FLAMINGO `rho_NN` (all variants, all 4 subcube-saga tests) | **NUMERICALLY VALID, ONTOLOGICALLY MISMATCHED** — real, correctly-computed nearest-neighbor mass correlations; not a source-faithful test of v82's own cluster-cluster-correlation-function-based separation concept. |
| `rho_band` (all-pairs-in-a-40-45-Mpc-band) | **CLOSER in spirit to a 2PCF-style statistic** than `rho_NN` (pairs within a separation band, not just nearest-neighbor) — but still computed on an `M200c`-selected, hard-top-`N`-thresholded population, not a full 2PCF fit — **PARTIALLY MATCHED**, closest existing result to what item 9 recommends, still not the same statistic. |
| `FINDING_P158`'s own `rho<=-0.5` directional-safety conclusion | **STATUS REOPENED** — the underlying numeric result stands, but its claim to test v82's own pair-population specifically is weakened pending a source-faithful estimand. |

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
