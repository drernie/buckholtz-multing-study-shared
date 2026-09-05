# CLAIM P197 — does the choice of cluster-mass measurement method
# (caustic vs. Planck SZ) move P196's own 1.47× residual?

**Date:** 2026-09-06
**Continues:** `FINDING_P196_ADDENDUM2`, which structurally ruled out
concentration (both scatter and source) as an explanation for `P196`'s
own residual and named `M200c`'s own caustic-technique measurement
systematics as the first of two remaining candidates.
**Authorization:** explicit user go-ahead ("сделай это по очереди
действуй автономно"), 2026-09-06, naming mass-measurement systematics
as candidate 1 of 2.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive.

**Correction (2026-09-06, caught mid-analysis by a Step 8a skeptic
pass, independently confirmed against the primary source before
accepting):** the first version of the script fed `MSZ` directly into
`P196`'s own `Δ=200`-anchored NFW builder, silently treating it as a
`Δ=200` mass. `[VERIFIED-arXiv:1507.08289]`, read directly this
session, Rines et al. (2016) §II.2: "The Planck mass estimates are
extracted from an aperture of `θ₅₀₀`, the angular radius corresponding
to `r₅₀₀`" — `MSZ` is a real `Δ=500` mass, not `Δ=200`. The first
version's raw result (`MSZ/M200c` mean ratio `1.68`, `74%` scatter,
`r=0.56`) was wrong — a genuine `Δ`-definition mismatch, not a real
astrophysical finding — and directly contradicted Rines et al.'s own
headline result ("SZ mass estimates... are not significantly biased"
relative to dynamical mass). Fixed: `MSZ` is now converted onto the
same `Δ=200`-anchored NFW machinery via a generalized root-finder
(`solve_halo_matching_target_delta`), matching at its own real `Δ=500`
instead of being silently mistreated as `Δ=200`.

## What is already available, not requiring a new fetch

`P196`'s own VizieR fetch (`J/ApJ/819/63/table4`) already includes,
for the same 123 clusters, **two independent, real, published mass
estimates**, both already columns in the table this project has
already downloaded twice: `M200c` ("Caustic mass", the dynamical mass
this project has used throughout `P196`/`ADDENDUM`/`ADDENDUM2`) and
`MSZ` ("Planck Sunyaev-Zeldovich mass proxy") — a second, methodologically
independent mass estimate for the identical clusters, from a completely
different physical technique (thermal SZ signal, not galaxy dynamics).
**Reusing this existing column is a real, cheap, already-available test
of "does the mass-measurement method matter" — no full caustic-technique
reimplementation is needed** (the prior chat's own earlier assessment
that a from-scratch caustic reimplementation is a multi-day undertaking
stands unchanged; this file does not attempt it).

## New estimand element specific to this file

**Population**: same 123 HeCS-SZ clusters.

**Endpoint 1**: direct comparison of `M200c` (caustic) vs `MSZ` (Planck
SZ) for the same clusters — ratio, correlation, scatter. This
quantifies the real, independent mass-measurement disagreement itself,
before it is propagated anywhere.

**Endpoint 2**: re-run `P196`'s own full pipeline (Girardi `R_vir`,
step 2a exact `z`-reference correction, step 2b `Δ178→500` NFW shape
correction via Duffy et al. 2008 — concentration source already shown
structurally not to matter, `FINDING_P196_ADDENDUM2`) substituting
`MSZ` for `M200c` as the mass input, and compare the resulting mean
ratio/scatter against `P196`'s own `1.4665`/`11.1%`.

**Falsifiable predicate**: if substituting `MSZ` moves the mean ratio
materially (per `P196`'s own MCID band `[0.95,1.05]`, or the scatter
by `>5` percentage points), mass-measurement-method choice is a real,
material contributor to the residual. If not, this specific candidate
is also structurally ruled out, narrowing the field further.

**MCID**: reused unchanged from `CLAIM_P196`.

## Positive control

At the row level, `MSZ` and `M200c` are already known (from the
literature this project already checked in `FINDING_P196`'s handoff
history) to be positively correlated real physical mass proxies for
the same objects — a Pearson correlation `r>0` between the two columns
on this real sample is the minimum sanity check before trusting either
one as a mass input.

## What this does NOT establish

1. Does not reimplement the caustic technique from scratch — reuses
   the catalog's own already-published `M200c` and `MSZ` values.
2. Does not resolve which of the two mass estimates is "more correct"
   — only whether their real, published disagreement is large enough
   to matter for `P196`'s own residual.
3. Does not draft or send anything to TJB.
4. `NO_AUTHOR_ERROR`.
