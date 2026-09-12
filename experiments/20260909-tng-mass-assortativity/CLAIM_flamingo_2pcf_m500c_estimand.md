# CLAIM — a real, source-faithful 2PCF-style estimand for v82's own
# "characteristic node separation" (docs/162 item 9, first computation)

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b/-1. **User-requested** ("переходи к docs/162 item 9").
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (measuring a real clustering
statistic and comparing to a cited external number — not causal, not
predictive)

## What this replaces

Every `rho_NN`/`rho_band` test in this branch (P158's whole
computational sub-branch, now CLOSED — see `FINDING_P158`'s Twelfth
entry) used a nearest-neighbor-distance or fixed-separation-band
statistic on a hard top-`N` rank cut. `docs/162` item 9 established
this is NOT v82's own actual empirical route: v82 cites Basilakos &
Plionis 2004 (`[91]`) — a POPULATION-LEVEL, richness-dependent galaxy-
cluster two-point correlation function, `xi(r) = (r0/r)^gamma`, fitted
via the standard cluster-clustering estimator, not a nearest-neighbor
rule. This claim builds the first source-faithful version of that
statistic on FLAMINGO's own data.

## Method

**Population:** select clusters by `M500c` (v82's own convention, per
`docs/162` item 3) DIRECTLY from the full FLAMINGO halo catalog — not
by re-ranking an already-`M200c`-filtered pool (that would silently
reintroduce the wrong convention as the outer selection). Three
top-`N` cuts (`N in {200, 1000, 5000}`), spanning fewer-but-more-
massive ("richer" proxy) to more-but-less-massive ("poorer" proxy),
loosely mirroring Basilakos & Plionis's own richer/poorer-subsample
split (this project has no true richness measure in FLAMINGO, mass
rank is the available proxy — stated explicitly, not silently
assumed).

**Estimator:** `xi(r) = DD(r)/RR(r) - 1`, the "natural"/Peebles-Hauser
estimator. FLAMINGO's box is PERIODIC — this removes the usual reason
a random catalog is needed (no survey mask, no edge loss up to
`r=L/2`): `RR(r)` has an EXACT analytic form for a uniform Poisson
population in a periodic box of volume `V`,
`RR(r) = N(N-1) * [4*pi*r^2*dr] / V`. No random catalog is built or
needed. `DD(r)` is computed from real periodic pairwise separations
(reusing this branch's own `periodic_sep_matrix` construction).

**Range and binning:** log-spaced bins from `5` to `150` Mpc (`15`
bins) — inside the regime where the cited literature values (`r0 ~
10-30` Mpc-class) live, well below `L/2=500` Mpc.

**Fit:** `xi(r) = (r0/r)^gamma`, fit via linear regression in
`log(xi)` vs. `log(r)` on bins where `xi(r) > 0` (the power law is
only defined there; negative/noisy bins at large `r` are excluded from
the fit, not zeroed or clipped).

**Cosmology for unit conversion:** FLAMINGO reports physical Mpc
directly (no `h` ambiguity in its own outputs) — the literature values
(`h^-1` Mpc) are converted to physical Mpc using FLAMINGO's own `h`
read directly from the simulation's cosmology metadata (HDF5 file
attributes), not assumed from memory.

**Negative control (mandatory before trusting the pipeline on real
data, per Perelman-audit § No-Collapse Tests / artifact-provenance-
gates.md Gate 3):** the SAME `DD/RR-1` pipeline run on `N` UNIFORM
RANDOM positions in the same periodic box must give `xi(r) ~ 0` within
Poisson sampling noise at every bin. This validates the analytic
`RR(r)` normalization and the pair-counting code BEFORE any claim is
made about real clusters — exactly the "does the same test pass on
the control too" discipline this project's own rules require.

## What this would and would not settle

- **Directly tests** whether FLAMINGO's own cluster population
  reproduces the clustering-amplitude range v82 itself cites as its
  empirical anchor (`r0 ~ 20.7 h^-1 Mpc` richer / `~9.7 h^-1 Mpc`
  poorer, Basilakos & Plionis 2004) — a check nothing in this branch
  has done before now (every prior test computed a mass-correlation
  statistic, never checked FLAMINGO's own clustering amplitude against
  the literature number v82 actually anchors to).
- **Does NOT** compute a mass-assortativity `rho` — that is a
  SEPARATE, follow-on generalization (a mass-marked 2PCF / mark
  correlation function), not attempted in this first pass. Whether the
  `rho > -0.5` question even has a well-posed 2PCF-style analog is
  itself an open design question, not resolved here.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`) — only checks whether FLAMINGO is a plausible
  stand-in population for the empirical route v82 itself cites.
- **Does NOT** resolve richness vs. mass-rank as proxies being
  genuinely equivalent — this is a real, disclosed limitation, not
  assumed away.

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked: (a) is the
analytic `RR(r)` formula correctly derived and applied for a periodic
box (no edge-loss correction needed, unlike a real survey); (b) does
the negative control (random positions) actually validate the pipeline
or could it pass trivially; (c) is the mass-rank-as-richness-proxy
caveat honestly scoped, not silently smuggled into a stronger claim;
(d) is the comparison to Basilakos & Plionis's own numbers apples-to-
apples (same kind of statistic, comparable population type — galaxy
clusters vs. FLAMINGO's simulated halos).

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
