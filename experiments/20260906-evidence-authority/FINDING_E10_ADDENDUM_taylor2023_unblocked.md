# FINDING E10 ADDENDUM — unblocked via Taylor et al. 2023, and the modern
# number is much smaller than the citation `E10`/`E6` originally used

**Date:** 2026-09-06
**Continues:** `FINDING_E10_sne_fitter_shift_blocked.md` (named this exact
paper, `[VERIFIED-arXiv:2301.10644]`, as the unblocking candidate but did
not fetch it). `docs/157_next_steps_plan_20260906.md` item 4, explicit
go-ahead given.

## L0 (EstimandOps)

**Question type: descriptive.** Does a modern, real, published
per-object comparison of two SNe Ia light-curve fitters exist that
reproduces `E6`'s pattern (same supernovae, two fitters, a measured
distance-modulus/`w` shift) — without repeating `E10`'s own near-miss
(reconstructing a per-object quantity from a merged catalog whose column
identity turned out to be wrong)?

## What was found — no reconstruction needed this time

Taylor, Jones, Popovic, Vincenzi, Kessler, Scolnic, Dai, Kenworthy &
Pierel (2023), *"SALT2 Versus SALT3: Updated Model Surfaces and Their
Impacts on Type Ia Supernova Cosmology"*, `[VERIFIED-arXiv:2301.10644]`
— fetched and read directly this session (abstract + Methodology §4 +
Data Availability, not from memory). Unlike `E10`'s VizieR attempt, this
paper **already publishes the per-object-level comparison itself** — no
reconstruction from a merged table was needed, avoiding exactly the
column-misidentification risk `E10` caught.

**Same structure as `E6`'s pattern:** 1083 SNe Ia trained identically on
both SALT2 and SALT3 model frameworks ("SALT2.FRAG"/"SALT3.FRAG"); a
common sample of **308 SNe Ia** from the public DES-SN3YR data, fit with
both surfaces, compared object-by-object.

## The real, quoted numbers

- **Headline systematic:** `Δw = +0.001 ± 0.005` — "the first estimate of
  the SN+CMB systematic uncertainty arising from the choice of SALT
  model framework," stated by the authors as **"a negligible effect at
  the current level of dark energy analyses."**
- **Per-object light-curve parameters** (`m_B`, `α·x₁`, `β·c`): binned
  averages agree to within `≲0.025` mag.
- **Per-object bias-corrected distance modulus (`μ`):** agree to within
  `≈0.1` mag, with the **average difference per redshift bin at least an
  order of magnitude smaller** (`≲0.01` mag).
- **Redshift trend:** the slope of `Δμ` vs. `z` is consistent with zero
  to `<1σ` — "the choice of SALT model framework does not bias the
  DES-SN3YR cosmology."
- **Hubble scatter:** `σ=0.152` mag (SALT2.FRAG) vs. `σ=0.151` mag
  (SALT3.FRAG) — essentially identical.
- **Sample-selection sensitivity:** 1 SN cut by SALT3 but kept by SALT2
  has an absolute Hubble residual of `2.6σ`; the 14 SNe cut by SALT2 but
  kept by SALT3 have a mean absolute residual of `0.66σ` — a small,
  quantified edge effect, not a systematic driver.
- **Public data:** surfaces at `10.5281/zenodo.4001177` and
  `10.5281/zenodo.7400436`; underlying DES-SN3YR data at
  `des.ncsa.illinois.edu/releases/sn` — a real, checkable, public trail.

## What this means for `E6`'s own pattern

`E10` originally targeted Kessler et al. (2009)'s `w=−0.76` (MLCS2k2) vs.
`w=−0.96` (SALT-II) — a `Δw≈0.20` shift, ~3σ(stat), from switching
**between two structurally different fitting frameworks**. Taylor+2023's
modern comparison is **between two versions of the same framework**
(SALT2 vs. SALT3, both SALT-family) and finds `Δw` smaller by roughly
**two orders of magnitude** (`0.001` vs. `0.20`).

**This is a real, useful update to `E6`'s own two-field classification,
not a null result:** the "fitter choice" systematic risk `E6` used as an
example is **methodology-dependent and has shrunk over time** as the
field converged on a shared model family (SALT2→SALT3 iterate the same
framework; MLCS2k2 was a genuinely different approach). The general
lesson `E6` wanted to illustrate (methodological choices can carry
hidden systematic risk) still stands — `E5`'s SPS-model shift (`+6.80%`,
today, real) and `E13`'s `M_gas`-`T` scatter (`σ=0.49`, today, real) are
both still-live instances of exactly this risk, in the same session. What
changes is that the *specific* SNe Ia fitter-choice instance `E6` first
reached for is now a resolved case, not an open one.

## What this does and does NOT establish

**Does establish:** `E6`'s SNe Ia example now carries a real, modern,
per-object-validated measurement (`Δw=0.001±0.005`), not only a 2009
citation — `E10`'s own named blocker is closed.

**Does NOT establish:**
1. Nothing about MULTING/v82 directly — this is a general
   cosmology-methodology finding, unconnected to this project's own
   force-law reconstruction.
2. Does not re-derive Taylor+2023's own numbers independently — they are
   quoted, not reproduced from raw data (the public Zenodo/DES links
   would allow that as a further, not-attempted, step).
3. `NO_AUTHOR_ERROR` — a literature-grounding update to this project's
   own `E6`/`E10` line, not a claim about Taylor et al.'s own work.

## Pearl Registry entry

The "fitter-choice systematic shrinks as methodology converges within a
model family, but not necessarily across different families" pattern is
a real, portable, falsifiable observation — logged in
`pearl_registry/INDEX.md`.
