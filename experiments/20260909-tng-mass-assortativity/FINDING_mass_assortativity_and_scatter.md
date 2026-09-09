# FINDING — Direct TNG-300 measurement of the two open unknowns named in
# FINDING_P158_jensen_mass_averaging_v82_force_terms.md

**Date:** 2026-09-09
**Scripts:** `pair_mass_correlation.py` → `top_halos_pos_mass.csv`,
`mass_observable_scatter.py` (reuses `../20260909-tng-whim-pilot/
whim_n71_results.csv`, no new API calls)
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive
**Answers, directly from TNG-300 data:** the two open unknowns
`FINDING_P158_jensen_mass_averaging_v82_force_terms.md` named and left
unchecked — (1) the sign/magnitude of `rho`, the log-mass correlation
between paired nodes ("mass assortativity"), and (2) `sigma_lnm`, cluster
mass-observable scatter at v82's own target mass range. Both were
previously scoped as a literature-grounding step (`docs/153` plan); this
measures them directly instead.

## Part 1 — Mass assortativity (`rho`)

### Design

Fetched `info.json` for the top 1500 halo IDs (== top 1500 halos by
total FOF mass, TNG's own catalog sort key — chosen specifically because
this project already discovered 2026-09-09 that `Group_M_Crit200` is
**not** strictly monotonic in ID; a contiguous top-ID slice sidesteps
that without assuming monotonicity). 1461/1500 usable (39 dropped to
transient network errors or a missing/zero `M_Crit200`). Computed all
pairwise 3D separations (periodic-corrected, box=205 Mpc/h), binned by
separation, and measured Pearson `r(log M1, log M2)` per bin.

### Result

```
N usable halos = 1461, mass range 8.39e12 - 1.54e15 Msun (median 4.66e13)
N pairs total  = 1,066,530

Headline (40-45 Mpc, v82's own node separation):
  N pairs = 4694
  r(log M1, log M2) = 0.3827  (t=28.37, p<0.001)

Negative control (masses shuffled, same target-band pairs):
  r = 0.0277  (~0, as expected -- confirms no spurious pipeline correlation)

Positive control (<5 Mpc separation):
  N pairs = 104, r = 0.3334  (p<0.001)
```

**Full separation-bin table (5 Mpc bins, 0-100 Mpc), all p<0.001:**

| bin (Mpc) | N pairs | r |
|---|---|---|
| 0-5 | 104 | 0.333 |
| 5-10 | 517 | 0.434 |
| 10-15 | 772 | 0.421 |
| 15-20 | 1199 | 0.392 |
| 20-25 | 1679 | 0.382 |
| 25-30 | 2263 | 0.436 |
| 30-35 | 2881 | 0.386 |
| 35-40 | 3649 | 0.403 |
| **40-45** | **4694** | **0.383** |
| 45-50 | 5909 | 0.397 |
| 50-100 (remaining bins) | 121,616 | 0.382-0.401 |

**Headline answer to P158: `rho ≈ 0.38` (positive, real, p<0.001) at
v82's own characteristic node separation.** Per P158's own conditional
result, a population-averaging Jensen's-gap correction to `F^(2)`
(quadrupole) relative to `F^(1)` (dipole) is boosted **more** than
`F^(1)` precisely when `rho > -0.5` — this measured value (`+0.38`) sits
well inside that regime, not near the `-0.5` threshold that would flip
the ordering.

### An honest, load-bearing caveat: the correlation is nearly FLAT across
### 0-100 Mpc, not specific to the 40-45 Mpc band

The table above shows `r` staying in a narrow `0.33-0.44` range across
the ENTIRE separation range tested, with no visible decay. This was not
predicted going in and is worth stating plainly rather than only
reporting the headline number in isolation. Two honest readings:

1. **Real, and physically explicable, not an artifact** (per the negative
   control's own `r≈0.03`, the signal is not spurious): the top-1500
   sample is a highly-biased tracer population (the most massive ~0.01%
   of halos in the box). Halo mass is known to correlate with the
   large-scale density field, and that field is itself correlated over
   tens-to-hundreds of Mpc — so almost any two halos drawn from this
   biased tail can show correlated mass through shared large-scale
   environment, not only through being a genuine "close pair."
2. **A real methodological gap for matching v82's own construction**:
   v82's own bridge treats a **specific pair** (nearest-neighbor-like,
   not "any two halos that happen to be ~40 Mpc apart amid 1500 other
   massive halos"). This measurement does not restrict to nearest-
   neighbor pairs — it uses every pair in the separation band, which
   likely over-counts halos that are *also* close to several other
   massive neighbors. **Now built — see "Nearest-neighbor-restricted
   check" below, and the result changes the picture substantially.**

### Nearest-neighbor-restricted check, same day — the 40-45 Mpc band
### contains ZERO true nearest-neighbor pairs in this sample

`nearest_neighbor_assortativity.py`, reusing `top_halos_pos_mass.csv`
(no new API calls). For each of the 1461 halos, found its single nearest
neighbor (not "any pair in a band") among the same sample.

```
Nearest-neighbor separation distribution (N=1461):
  min=2.36  max=37.92  median=9.19  mean=10.65 Mpc

Mass correlation among ALL nearest-neighbor pairs (any separation):
  r(log M_self, log M_neighbor) = 0.0192  (t=0.73, n.s.)

Nearest-neighbor pairs whose separation falls in 40-45 Mpc:
  N = 0 (of 1461)
```

**This is a genuinely important correction, not a minor scope note.**
The maximum nearest-neighbor separation across the ENTIRE top-1500-
most-massive-halo sample is 37.9 Mpc — no halo in this population has
its true nearest neighbor at 40-45 Mpc at all. Every pair contributing
to the earlier `rho=+0.38` headline at that separation is, by
construction, NOT a nearest-neighbor pair for either halo in it — each
member has a genuinely closer, more massive-correlated neighbor
elsewhere (median 9.2 Mpc away) that the all-pairs measurement ignored.
And restricted to genuine nearest-neighbor pairs at ANY separation, the
mass correlation is **not significant** (`r=0.019`, essentially zero) —
a much weaker result than the flat `~0.38` the all-pairs approach found
everywhere.

**Reading:** the original all-pairs `rho=+0.38` reflects broad
large-scale bias/clustering of a sparse, highly mass-selected tracer
population (reading 1, above) — confirmed, not just suspected. It is
NOT evidence of assortativity between the SPECIFIC pairs a node would
actually be "paired with" under a nearest-neighbor reading of v82's own
construction; that specific question now has its own, much weaker,
non-significant answer (`r=0.019`). **Which reading applies to v82's
own physical intent is not resolved here** — if "the pair" in v82's
sense is not literally "nearest spatial neighbor" but something else
(a characteristic scale from a different physical argument, not halo-
catalog nearest-neighbor statistics), neither number above may be the
right one to use, and that ambiguity is itself worth naming rather than
silently picking one answer.

**What this does NOT establish:** that `rho` is exactly `0.38` for
"the" pair construction v82 itself uses; that the assortativity is
short-range-specific rather than a broad large-scale-bias effect
(now positively confirmed to be the latter, not just suspected — see
the nearest-neighbor check above); or anything about MULTING's own
correctness (`NO_AUTHOR_ERROR`).

**What this DOES establish, robustly — revised after the nearest-
neighbor check:** at least ONE well-defined reading of `rho` at v82's
own characteristic separation is **positive and highly significant**
(`+0.38`, all-pairs, reflecting large-scale bias, not proximity per se).
A DIFFERENT, arguably more construction-faithful reading (mass
correlation between a halo and its literal nearest neighbor) is
**consistent with zero** (`r=0.019, n.s.`), and — more fundamentally —
**no halo in this sample has a true nearest neighbor at 40-45 Mpc at
all**. Both are real, both survive their own negative controls; they
simply answer different questions, and which one v82's own physical
construction actually asks is not settled by this project's
reconstruction. Either way, **nothing found here suggests a route to
`rho < -0.5`** — the ordering-reversal regime `FINDING_P158` names stays
unreached under every reading tried.

## Part 2 — Mass-observable scatter (`sigma_lnm`)

Reused the already-collected N=71 WHIM-pilot sample (no new API calls;
mass range 1.28e14-7.34e14 Msun sits close to v82's own targeted range).
Observable proxy: richness (`GroupNsubs`), a real proxy astronomers use
(e.g. redMaPPer-style richness-mass relations). Fit
`log(M_true) = a + b*log(N_richness)`, matching the literature convention
of reporting scatter of TRUE mass at fixed observable, not the inverse.

```
N = 71
Fit: log10(M_true) = 11.966 + 0.762 * log10(N_richness)
r(log N_richness, log M_true) = 0.596

sigma_logM|richness = 0.127 dex
sigma_lnM|richness  = 0.293  (natural-log units)
```

**Sanity check (rough, not a load-bearing claim):** published richness-
mass scatter for real cluster-finders (e.g. redMaPPer-class estimators)
is commonly quoted in the `sigma_lnM ~ 0.2-0.3` range — this project's
own direct N=71 measurement (`0.293`) sits inside that ballpark, though
this is a `[MEMORY]`-tier comparison (the exact published figures were
not re-verified live this session) and richness-in-a-simulation is not
identical to redshift-space richness from a real survey.

**What this does NOT establish:** that `0.293` is THE scatter value
relevant to v82's own mass variable — richness is one specific proxy
among several a real analysis could use, and this is this project's own
first, direct measurement on a modest N=71 sample, not a definitive
literature-quality value.

## Correction, same day — Part 2's `sigma_lnM|richness` answers the
## WRONG question; the actually-needed quantity is simpler and was sitting
## in the same dataset unused

**Caught by re-reading `P158_jensen_mass_averaging_v82_force_terms.py`
directly** (not by a skeptic pass — a plain second look while drafting
this file's own "what's next" summary), the same category-error class a
prior 2026-09-02 literature-grounding attempt was independently caught
making by a Step 8a skeptic (`FINDING_P158_ADDENDUM_literature_
grounding.md` — REJECTED for using measurement-*technique*-disagreement
scatter, WL vs. HE, when the formula needed population mass scatter).
Part 2 above made a different but same-*class* mistake: it computed
`Var[log M_true | richness]` — the scatter of true mass **conditional
on** an observable proxy, after de-trending a mass-richness relation.

**What `R(p) = ⟨m^p⟩/⟨m⟩^p` in `FINDING_P158`'s own §2 actually needs**
(confirmed directly from the script, `sigma_lnm` is the parameter of a
raw `m = exp(Normal(0, sigma_lnm))` draw — see `monte_carlo_cross_check`,
line 91-92): the **unconditional** population scatter of the node's own
`log(mass)` — no observable proxy involved at all. TNG-300 gives the
TRUE mass directly, so the correct quantity needs no proxy step:

```
sigma_lnM (N=71, 1.28e14-7.34e14 Msun, v82-adjacent range) = 0.368
sigma_lnM (N=1461, 8.39e12-1.54e15 Msun, this file's broader Part 1 sample) = 0.743
sigma_lnM (N=40 sub-slice, 3e14-8e14 Msun, tightest around v82's ~5-6e14 target) = 0.229
```

**Honest population-scope sensitivity, not resolved here:** these three
real numbers span `0.23-0.74` depending purely on which population of
"nodes" is assumed to be entering v82's own force-average — a question
this project's reconstruction does not pin down precisely. This
sensitivity is itself the more informative finding: `sigma_lnm` is not a
single well-defined number until the node population is specified, and
narrower mass windows (closer to v82's own stated target) give smaller
scatter than the full massive-halo tail.

**`0.293` (Part 2 above) is not deleted, just downgraded**: it remains a
real, correctly-computed richness-mass conditional scatter (a legitimate
quantity in its own right, coincidentally close in magnitude to the
correct N=71 unconditional value 0.368) — it is simply not what `FINDING_
P158`'s own formula asks for. Left in place above per the Hindsight
Distortion Gap Heuristic (correct with a dated addendum, don't rewrite).

## Combined bottom line for `docs/153` bottleneck-1 planning

Both of P158's named open unknowns now have a real, direct, TNG-native
answer instead of an unresolved literature-search gap — **and both
answers turned out to need a second, corrective pass the same day**,
which is itself worth noting as a pattern (both mistakes were the same
species: assuming an available, easy-to-compute quantity was the one
actually needed, without re-deriving the target formula's exact
requirement first):

```
rho: two internally-consistent readings, not one number
  all-pairs (any halo pair in the 40-45 Mpc band)     = +0.38 (p<0.001)
  nearest-neighbor-restricted (the halo's true NN)    = N=0 pairs in that band;
                                                          r=0.019 (n.s.) at ANY separation
sigma_lnM (unconditional, population scope-dependent) = 0.23-0.74,
  see Correction above — N=71 v82-adjacent sample: 0.368
```

Per P158's own conditional result, `rho > -0.5` means the population-
averaging correction (if it were applied) would boost the quadrupole
term `F^(2)` MORE than the dipole `F^(1)`. **Both readings of `rho`
above satisfy `rho > -0.5`** — the ordering-reversal regime is unreached
either way — but they disagree sharply on how large and how physically
grounded the effect is (a robust `+0.38` vs. an essentially-null
`0.019`), and only a clearer statement of what "the pair" means in
v82's own construction would resolve which one is the right number to
use. This is a real, honest contribution toward `docs/153`'s own
bottleneck-1 pre-conditions — not a resolution of bottleneck 1 itself,
and less conclusive than this file's own first-pass version claimed.
