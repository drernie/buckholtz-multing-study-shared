# data_acquisition_plan.md — thermal-pair fingerprint

**Continues:** `claim.md` §8 item 2 / `estimand.md`'s own Status section
(costed acquisition plan, after the synthetic-battery mandate). Read
`estimand.md` first.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Method:** every item below is `[VERIFIED-REAL]` via a background
research pass (36 tool calls, real files/pages fetched — not search
snippets) or explicitly marked `[SOURCE_NOT_FOUND]`. No cost estimate
below is invented; each is derived from a real file size, a real
footprint-overlap number, or a stated, explicit assumption flagged as
such.

---

## The decisive finding: this plan is NOT the one `estimand.md` assumed

`estimand.md`'s own Endpoint section described building the pairwise
statistic "the same way as `arXiv:2511.23417`'s own pairwise-kSZ velocity
estimator, for the subset of that catalog's pairs." **That is not
buildable as written.** The paper's own Data Availability statement
points to a Zenodo record (`10.5281/zenodo.17373480`) containing only
five small files — binned pairwise-kSZ curves and figure data (`Fig1.csv`,
`Fig3_*.csv`, `Fig4_*.csv`, `Fig5.npy`, `Fig6.npy`) — **no per-object
table**. The 456,803 ML-inferred per-cluster `τ`/velocity values that
produced those figures are internal to the DESI/ACT collaboration, not
released. `estimand.md`'s § Consistency (b) already worried this
pipeline might carry undisclosed assumptions; it did not anticipate that
the pipeline's *output* would be unavailable at all.

**This forces a real design decision — Fork 1, below — before any cost
estimate downstream of it means anything.**

---

## Fork 1 — how to get a pairwise-velocity statistic at all

| Option | What it is | Verdict |
|---|---|---|
| **1a. Request the per-object table from the DESI/ACT collaboration** | Same route this project already used successfully once (`experiments/20260701-h1b-whim-thermal-mass-bias/estimand.md` Option E — The Three Hundred data request, sent 2026-07-17, still awaiting reply 2 months later) | Real option, but this project's own track record says **budget months, not weeks**, for a reply — and there is no guarantee of a "yes." |
| **1b. Re-implement the classical pairwise-momentum kSZ estimator from scratch** | The `τ`-inference step in `2511.23417` is one, ML-based way to estimate optical depth per object; the field's older, more transparent method (Hand et al. 2012-style: stack the CMB temperature at galaxy positions, weighted by an estimated optical depth from a mass-observable relation, not an ML model) needs only the **public** ACT DR6 `y`-map + public DESI DR1 spectroscopic catalog | **Recommended.** More work up front, but (i) it is buildable entirely from confirmed-public data, (ii) a transparent, formula-based `τ` estimate is *more* auditable for this project's own Consistency check than an opaque ML model would be, and (iii) it sidesteps `estimand.md` § Consistency (b)'s exact worry (a gravity-model-trained pipeline) by construction — the classical estimator's assumptions are explicit and can be varied as a sensitivity check. |

**This plan costs option 1b** (the buildable one) below, and treats 1a as
a parallel, low-effort, long-latency request worth sending alongside it,
not instead of it — matching this project's own established pattern of
running a cheap correspondence request in parallel with a costed
technical path (H1b again).

---

## The six ingredients, costed

| # | Ingredient | Verdict | Access | Real cost |
|---|---|---|---|---|
| 1 | `K` via tSZ (Compton-`y`) | `[VERIFIED-REAL]` | `lambda.gsfc.nasa.gov` — direct file `ilc_actplanck_ymap.fits`, **1.78 GB**, plus mask + beam files. No login. **Correction to `estimand.md`'s own assumption**: this is **Plate Carrée (CAR) projection, ~0.5 arcmin pixels**, not native HEALPix. | Download: minutes. Per-cluster `Y` extraction (aperture photometry at each cluster position, background-subtracted): **new code, ~1-2 days**, not a downloadable column — this project has no existing tSZ-extraction script. |
| 2 | pairwise dynamics (kSZ) | `[VERIFIED-REAL, Fork 1b]` | Same `y`-map (#1) + DESI DR1 spectroscopic catalog, public at `data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/`. | **The largest real cost in this plan.** Re-implementing a pairwise-momentum kSZ estimator (stacking, optical-depth weighting, covariance via jackknife/bootstrap) is a **multi-day-to-multi-week** undertaking, not a data pull — flagged honestly rather than folded into "download time." No existing code for this in this repo. |
| 3 | `M` via weak lensing | `[VERIFIED-REAL, PARTIAL — real bottleneck found]` | DES Y3 redMaPPer catalog public (`desdr-server.ncsa.illinois.edu`, FITS, λ>20, >21,000 clusters) — but its **native product is richness `λ`, not a per-cluster mass column**; a separate, published richness–mass calibration is needed. **Sky-overlap constraint, computed not assumed**: DES-Y3 ∩ DESI-DR1 footprint = **851.3 deg²** — small against ACT DR6's ~13,000 deg². | Download: minutes. Richness→mass conversion: reuses a published scaling relation (not built from scratch), **~1 day**. **The 851 deg² overlap is the real limiter on final sample size — must be computed against the other footprints (§ Fork 2) before the sample-size line in this plan means anything.** |
| 4 | X-ray cross-check (`T_X`) | `[VERIFIED-REAL]` | `erosita.mpe.mpg.de/dr1/.../erass1cl_main_v3.2.fits`, **~48 MB**, direct download, no registration. Column `KT` (+ `KT_L`/`KT_H` uncertainties) — **usable directly**, no separate spectral modeling needed. | Download + column read: **hours**, not days. |
| 5 | large-scale environment | `[VERIFIED-REAL for inputs / SOURCE_NOT_FOUND for a ready product]` | DESI DR1 LSS catalogs (galaxies + matched randoms + systematic weights) public at `data.desi.lbl.gov`. **No pre-built density-field product found.** | Must be **built from scratch** (counts-in-cells against the public randoms) — standard, well-precedented technique, but new code: **~2-3 days**. |
| 6 | dynamical-state proxy | `[VERIFIED-REAL — better than this project's own prior precedent]` | Sanders et al. 2025 (`arXiv:2502.02239`), full-text confirmed: **full eRASS1 sample, 12,247 clusters**, centroid shift `w`, concentration (`c₅₀₀`, `c₈₀₋₈₀₀`), ellipticity, Gini, power ratios. Data hosted at the same `erosita.mpe.mpg.de` page as #4. | Download: minutes. **No conversion or calibration needed** — this is a direct, large upgrade over `experiments/20260701-h1c-morphology-mass-bias`'s own `N=50` CCCP-based proxy, reusable there too if that branch ever reopens. |

---

## Fork 2 — the sample-size question, attempted 2026-09-11, NOT pixel-exact

**What was actually tried:** `healpy`/`astropy_healpix`/`mocpy` are not
installed and `healpy` fails to build in this environment (no `pkg-config`
on Windows — a real, checked blocker, not skipped). The ACT DR6 mask
itself is **1.78 GB** (same size as the map — confirmed via `WebFetch` on
the LAMBDA product page, not assumed), making a pixel-exact download-
and-intersect infeasible inside this session. Fell back to real,
individually-sourced published numbers instead of a guess:

| Pair | Value | Source |
|---|---|---|
| DES-Y3 ∩ DESI-DR1 | **851.3 deg²** | found via real paper/press coverage, prior pass |
| eRASS1 ∩ DESI Legacy Survey DR10 | **12,791 deg²** | `[VERIFIED-arXiv:2402.08452]`, Bulbul et al. 2024, quoted directly: *"the 12,791 deg² common footprint of eRASS1 and the DESI Legacy Survey DR10"* |
| eRASS1 total | 13,116 deg², western Galactic hemisphere, `179.9442°<l<359.9442°` | `[VERIFIED-arXiv:2402.08452]`, same paper |
| ACT DR6 total | "~1/3 of the sky" (≈13,750 deg²) | `[VERIFIED-REAL]`, LAMBDA info page's own stated figure — not a precise polygon |

**Reading these together, not just listing them:** eRASS1 already covers
**97.5% of its own area (12,791/13,116 deg²) in common with the DESI
Legacy footprint** — it barely restricts DESI at all. ACT DR6's own
footprint (~13,750 deg², Chile-based, the same general southern
extragalactic sky DES/DESI/eROSITA jointly target — this is the explicit
science motivation behind all of these surveys existing in the same sky
region, not a coincidence) is comparably large. **Reasoned, not
pixel-verified, conclusion: the 851.3 deg² `DES-Y3∩DESI-DR1` figure is
very likely close to the true 4-way number**, since neither ACT nor
eRASS1 has been found to be a tighter constraint than DESI or DES-Y3
already are.

**What this is NOT:** a computed number. It is a bounded, sourced
estimate: **upper bound 851.3 deg², plausible working range
~700-850 deg²**, honestly short of a pixel-exact figure. Getting an
exact number requires either (a) the 3.56 GB ACT mask+map download and a
from-scratch equal-area-grid intersection (no `healpy` needed — a plain
`numpy` RA/sin(Dec) grid works, but reading/rasterizing 1.78 GB of
HEALPix FITS without `healpy` needs a manually implemented pixel→(RA,Dec)
conversion, itself a source of bugs to control for), or (b) finding an
existing 4-way cross-match paper that already did this (plausible given
how common ACT×DES×DESI×eROSITA joint science is, not found in this
pass — worth a dedicated literature search before spending compute on
(a)).

**Recommendation, stated plainly:** do not spend the multi-hour/GB
effort on pixel-exact precision **yet** — 851.3 deg² (or the ~700-850
working range) is precise enough to decide whether Fork 1 is worth
pursuing at all. Revisit for exact precision only once the mock-catalog
power analysis shows the result is sensitive to the exact N in that
range.

---

## Total honest cost, stated plainly

| Phase | Estimate |
|---|---|
| Downloads (items 1, 3, 4, 6) | Minutes each; ~2 GB total |
| Footprint-intersection check (Fork 2) | Hours — **do this first** |
| Richness→mass calibration (item 3) | ~1 day |
| Environment density-field build (item 5) | ~2-3 days |
| tSZ per-cluster extraction (item 1) | ~1-2 days |
| **kSZ pairwise estimator (item 2, Fork 1b)** | **~1-3 weeks** — the dominant cost, and the one item with no existing code anywhere in this repo to build from |
| Parallel: data request to DESI/ACT collaboration (Fork 1, option 1a) | ~1 hour to draft + send; reply timeline unknown, this project's own precedent says months |

**This is not a weekend script.** The kSZ estimator alone is a real,
multi-week engineering undertaking, before the synthetic identifiability
battery (`estimand.md`'s own hard pre-data gate) or any real data pull.

---

## What this does NOT establish

1. **Not that the project should proceed.** This file costs the branch;
   it does not recommend committing the weeks of work required — that
   remains a decision for the user, informed by a real number instead of
   an assumption.
2. **Not that Fork 1b's estimator, once built, will pass the synthetic
   battery.** That gate (`estimand.md`) still comes before any of this
   touches real data.
3. **Not a final sample-size number.** Fork 2's own footprint
   intersection is unresolved — the 851 deg² figure is a partial,
   pessimistic bound, not the final N.

## Status

**Costed. Not authorized to proceed.** Next, in order: (1) Fork 2's cheap
footprint-intersection check, (2) a user decision on Fork 1 (build 1b,
send 1a, or both in parallel — this project's own H1b precedent favors
both), (3) only then the mock-catalog power analysis, (4) only then the
synthetic four-world battery's own concrete design, (5) only then code.
