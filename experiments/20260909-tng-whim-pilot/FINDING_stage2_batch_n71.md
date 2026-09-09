# FINDING — TNG WHIM batch, Stage 2: N=71 real clusters, all controls
# pass, a real (p<0.001) mass-anticorrelation found — not yet H1b itself

**Date:** 2026-09-09
**Script:** `whim_batch_n71.py` → `whim_n71_results.csv`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive
**Continues:** `FINDING_stage1_pilot_halo200.md` (single-cluster pilot,
controls verified) — this scales to H1b's own pre-registered minimum
sample size (`N≥71`, AMENDMENT 2).

## Run

71 clusters collected from 72 candidate halo IDs checked (IDs 5-76,
one skipped for falling below the 1×10¹⁴ M☉ threshold or a fetch
failure — not investigated further, immaterial at this N). Wall time:
**65.3 minutes**. Each cluster's own gas cutout was deleted immediately
after processing (not retained — 71× ~30-150MB would be several GB).

## Controls — 71/71 pass, not just the pilot's one case

Every cluster individually passed both Stage-1 controls (cutout gas
mass vs. catalog `GroupMassType[gas]`; inner-ICM temperature in the
physically expected 10⁶-10⁹ K band). Zero exceptions, zero silent
failures — the script logs and skips (does not silently include) any
cluster whose info-fetch or cutout-fetch fails.

## Result

```
N = 71
WHIM mass fraction (%):  min=2.5   max=72.9   mean=33.4   median=30.2   stdev=16.0
M200 range: 1.28e14 - 7.34e14 Msun (mean 3.37e14)

Pearson r (M200 vs WHIM%):          -0.429
Pearson r (log10(M200) vs WHIM%):   -0.406
```

**This is a real, statistically significant anticorrelation, not noise.**
For N=71, `r=-0.429` gives `t≈-3.94` on 69 degrees of freedom —
`p<0.001`, two-tailed. More massive clusters in this sample have
systematically lower WHIM mass fraction in their R200-3R200 annulus.

**Physically plausible, not asserted as confirmed:** a candidate
mechanism is that more massive clusters have deeper potential wells and
correspondingly more extended, already-shock-heated (>10⁷ K, "hot ICM"
rather than "WHIM") gas reaching further past R200 — so the same
temperature-defined WHIM window captures a smaller *fraction* of a more
massive cluster's annulus gas. **Not tested here** — would need the
temperature *profile* shape vs. mass, not just the binary WHIM/non-WHIM
split this batch computed.

## Comparison against real, independent literature

Li et al. 2025 (`arXiv:2503.05011`, The Three Hundred project,
GIZMO-SIMBA/Gadget-X) report the WHIM mass fraction "increases with
radius until ~3×R200c, where it plateaus at ~**70 per cent**." This
batch's own mean (33.4%) and even its maximum (72.9%, a single cluster)
sit mostly well below that reported plateau — **a real, now
quantified-at-N=71 discrepancy, not a one-cluster fluke** (Stage 1's own
single-cluster 90.28% was, in hindsight, closer to an upper outlier than
representative — this is exactly why N=1 pilots are pilots, not
results).

**Candidate explanations, named, none confirmed:**
1. Different simulation physics (TNG's own fiducial model vs.
   GIZMO-SIMBA/Gadget-X) — a real, substantial modeling difference, not
   a bug in either analysis.
2. Different halo mass range/sample (this batch: 1.3-7.3×10¹⁴ M☉,
   TNG300-1's own box; Li+2025: The Three Hundred's zoom-in sample,
   selected `M500≥10¹⁴`) — the two mass ranges likely overlap but are
   not identical samples.
3. Different radial binning/reporting convention — Li+2025 report a
   plateau reached "until ~3×R200c," which could mean their own
   fraction *at* 3×R200c specifically, not averaged over the full
   R200-3R200 shell as this batch computes.

None of these is checked here — named as real candidates for a future,
smaller follow-up, not resolved.

## What this does and does NOT establish

**Does establish:**
1. A working, controlled, N=71-scale WHIM-fraction measurement pipeline
   for real TNG-300 clusters — 3 of H1b's 4 needed ingredients
   (`M_true`, WHIM fraction, and — via `group_nsubs`/`GroupFirstSub`,
   not yet analyzed — a rough substructure-count proxy for dynamical
   state) are now computable end-to-end for any qualifying cluster.
2. A real, statistically significant (p<0.001) anticorrelation between
   cluster mass and WHIM mass fraction in this project's own
   reconstruction of the R200-3R200 annulus — a genuine, if modest
   (r≈-0.43, ~18% of variance), empirical pattern.
3. A real, quantified discrepancy against Li+2025's own reported
   plateau, worth further checking, not hidden.

**Does NOT establish:**
1. **H1b's own actual correlation test** (`E_WHIM → delta_M`) — the
   4th ingredient, hydrostatic mass bias, remains external and missing;
   letter drafted (`correspondence/draft_three_hundred_data_request_
   20260909.md`), not sent (user's own explicit choice, "tomorrow or
   the day after").
2. The mechanism behind the mass-anticorrelation — a plausible
   candidate is named, not tested.
3. Whether the mass-anticorrelation or the Li+2025 discrepancy bears on
   MULTING in any way — `NO_AUTHOR_ERROR`, this is a real measurement
   from public simulation data, unrelated to v82 or TJB's own claims
   except insofar as it prepares H1b's own infrastructure.
4. A dynamical-state confound control — `group_nsubs` and
   `group_first_sub_id` were collected but not yet used; H1b's own
   pre-registered design requires controlling for dynamical state
   before any `E_WHIM → delta_M` correlation counts.

## Next step, named not done

1. **Analyze `group_nsubs` as a dynamical-state proxy** against both
   mass and WHIM% — does substructure count add information beyond
   mass alone, or is it fully collinear with mass (in which case a
   different proxy is needed for real confound control)?
2. **Wait for or pursue the external hydrostatic-mass data** — the
   actual bottleneck for H1b itself.
3. If the Three Hundred data arrives for a comparable cluster sample,
   this batch's own 71 WHIM measurements are immediately reusable — no
   rework needed on this half.
