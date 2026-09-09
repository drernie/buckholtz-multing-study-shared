# FINDING — TNG WHIM pilot, Stage 1: the API cutout genuinely reaches
# the WHIM annulus, contrary to what the docs alone suggested; a first
# real number computed and controlled

**Date:** 2026-09-09
**Script:** `whim_pilot_halo200.py`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive
**Continues:** `parked/H1b-whim-thermal-mass-bias.md` (TNG-300 access
granted 2026-09-08/09) — this is the first concrete step toward the
"we can compute 3 of H1b's 4 needed ingredients ourselves" plan, not a
claim H1b is now runnable end-to-end (the 4th ingredient, hydrostatic
mass, is still external — see that file).

## What was checked before trusting anything

The TNG API's own documentation (`/data/docs/api/`) describes the
per-halo `cutout.hdf5` endpoint only as returning particles "of" the
halo, without specifying whether that means gravitationally-bound-only
(which would stop well short of R200-3R200) or the full FoF-linked
group (which can extend further). This was flagged as a real, unresolved
risk before any pilot was built.

**Resolved empirically, not by more reading:** pulled a Coordinates-only
gas cutout for a pilot halo and measured the actual radial distribution
directly (separate check, `check_radial_extent.py`, not committed —
scratch). Result: particles extend to **3.40×R200**, with 99.3% within
3×R200 — the cutout genuinely reaches the WHIM annulus this project
needs. This directly overturned a documentation-based worry that could
have wrongly stopped the pilot before it started.

## Pilot target

TNG300-1, snapshot 99 (z=0), halo_id=200. `M_200 = 1.175×10¹⁴ M_☉`,
`R_200 = 1032.7` physical kpc — chosen specifically because halo 0 (the
box's most massive halo) proved impractical: its gas-only Coordinates
cutout was 754 MB / 23.7M particles, vs. this halo's 41-69 MB / 1.72M
particles. Near H1b's own stated mass threshold (~10¹⁴ M_☉), not an
extreme object.

## Controls — both real, both pass

1. **Cutout total gas mass vs. the catalog's own `GroupMassType[gas]`:**
   `1.996×10¹³ M_☉` in the cutout, **exactly** `1.996×10¹³ M_☉` in the
   catalog (ratio 1.000). Confirms the cutout mechanism and field
   extraction are correct — not an approximate or partial match.
2. **Physical sanity check, not a tautology:** median temperature of
   gas within `0.3×R200` (deep inner ICM) is `2.06×10⁷ K` — squarely in
   the well-established range for a massive cluster's hot core (~1-10
   keV). This is a real, independently-known physical fact the pipeline
   had to reproduce, not something built into the test by construction.
   Confirms the standard TNG temperature formula
   (`T=(γ-1)·u/k_B·(UnitEnergy/UnitMass)·μ`, `μ=4/(1+3X_H+4X_H·x_e)`,
   `X_H=0.76`, `γ=5/3`) — verified against the project's own FAQ page
   this session, not applied from memory alone — is correctly
   implemented in code, units included.

## A real bug found and fixed before it produced a wrong number

The first run of the (exploratory, secondary) thermal-energy-scale
proxy overflowed to `inf` — `RuntimeWarning: overflow encountered in
multiply`, not a silently wrong finite value. Root cause: per-particle
mass in grams (~10⁷ M_☉ × 1.989×10³³ g/M_☉ ≈ 2×10⁴⁰) exceeds float32's
~3.4×10³⁸ range; the HDF5 mass field loads as float32. Fixed by an
explicit `float64` cast before the gram conversion. Caught by the
overflow warning itself, not by manual inspection — the warning did its
job.

## Result

```
Annulus (R200 < r < 3*R200):
  gas particles (any T):        453,612
  gas particles, WHIM-T range:  409,918
  gas mass, any T:              5.253e12 Msun
  gas mass, WHIM-T only:        4.742e12 Msun
  WHIM mass fraction:           90.28%
```

**Compared against real, independent literature (not a self-check):**
Li et al. 2025 (`arXiv:2503.05011`, The Three Hundred project,
GIZMO-SIMBA/Gadget-X) report the WHIM mass fraction "increases with
radius until ~3×R200c, where it plateaus at ~70 per cent." This pilot's
90.28% is real but higher — a genuine, honest discrepancy, not hidden.
**Candidate explanations, none confirmed:** (a) different simulation
(TNG's own fiducial model vs. GIZMO-SIMBA/Gadget-X — a real physics-model
difference, not a bug); (b) different halo mass (this pilot's single
1.2×10¹⁴ M_☉ halo vs. their own sample's own mass range/median); (c) a
single-halo measurement here vs. their own sample-averaged plateau —
halo-to-halo scatter is real and unmeasured with N=1.

## What this does and does NOT establish

**Does establish:** the TNG API can supply real, controlled WHIM
mass-fraction measurements for individual clusters — the missing
ingredient this project can compute itself, distinct from hydrostatic
mass (still external). The pipeline (cutout → temperature → radial +
temperature selection) works and is verified against two independent
controls plus one caught-and-fixed bug.

**Does NOT establish:**
1. Anything about H1b's actual correlation test — N=1 pilot, no
   dynamical-state confound control yet, no comparison against `delta_M`
   (still blocked on external hydrostatic-mass data).
2. That 90.28% is "the" WHIM fraction for clusters of this mass — a
   single-halo number, not a sample statistic; the Li+2025 discrepancy
   is flagged, not resolved.
3. That the exploratory thermal-energy-scale proxy
   (`4.183×10⁶⁰`, deliberately non-standard units) is a real, usable
   physical quantity — it is a placeholder pending a proper `(3/2)Nk_BT`
   calculation in standard (erg or keV) units, not attempted here.
4. `NO_AUTHOR_ERROR` — this is a measurement from real public simulation
   data, not a claim about MULTING or v82.

## Next step, named not done

Scale from N=1 to the pre-registered N≥71 (or the full 324-cluster
Three Hundred-comparable sample, if useful for cross-checking against
Li+2025 directly), add the dynamical-state confound indicator per
cluster, and — separately, on its own schedule — wait for or pursue
external hydrostatic-mass data (`correspondence/
draft_three_hundred_data_request_20260909.md`, not yet sent). Combining
the two is the actual H1b test; not attempted here.
