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

## Addendum, same day — `group_nsubs` checked, NOT a usable dynamical-
## state proxy (a real, honest negative result)

**Question:** does substructure count (`GroupNsubs`) carry real,
mass-independent dynamical-state information usable for H1b's own
confound control, or is it just a diluted echo of mass?

**Method:** (1) correlate `log(Nsubs)` against `log(M200)` directly;
(2) fit and remove the mass trend (OLS in log-log space), leaving a
residual — clusters with *more* substructure than their mass alone
predicts are candidate unrelaxed/merging systems, *fewer* candidate
relaxed ones; (3) correlate that mass-independent residual against
WHIM%, separately from raw `Nsubs` against WHIM%.

**Result:**
```
r(log M200, log Nsubs)        =  0.596  (p<0.001) -- substantially collinear with mass
r(log Nsubs, WHIM%)           = -0.187  (n.s.)     -- weaker echo of the mass-WHIM link
r(nsubs residual, WHIM%)      =  0.074  (n.s.)     -- ~zero once mass is removed
```

**Verdict: `GroupNsubs` is NOT a usable dynamical-state confound
control here.** It is moderately collinear with mass (bigger halos
trivially host more subhalos, independent of dynamical state), and once
the mass trend is removed, the residual carries no detectable relation
to WHIM% (`r≈0.07`, not significant at `N=71`). Using raw `Nsubs` as a
"dynamical state" variable would have silently re-tested the mass
correlation under a different name — caught here before that mistake
was made, not after.

**What this does NOT establish:** that dynamical state has no real
effect on WHIM% — only that this specific, cheap, catalog-native proxy
does not capture it. Ansarifard et al. 2019's own dynamical-state
indicators (VR/R/IR/VI morphological class, azimuthal scatter `σ_A`)
require synthetic X-ray imaging this project does not have a pipeline
for — a real, substantial undertaking, not attempted here.

## Second addendum, same day — CM/potential-minimum offset checked,
## ALSO not a usable dynamical-state proxy for WHIM% (second real
## negative result)

**Question:** is the offset between `GroupCM` (mass-weighted center)
and `GroupPos` (potential minimum / most bound particle) — a real,
standard cluster-relaxation indicator (Mohr et al. 1993; the same
physical idea behind Ansarifard+2019's own 2D "centroid shift," here in
a simpler, directly-available 3D catalog form) — related to WHIM%, once
mass is controlled for?

**Method:** `check_cm_offset_confound.py` re-fetched each cluster's
`info.json` (light, no gas cutout needed — the Stage-2 batch's own
cutouts were already deleted), computed the periodic-corrected 3D
offset normalized by `R200`, then ran the same collinearity + de-trend
+ residual-correlation procedure as the `GroupNsubs` check above.

**Result:**
```
Offset/R200: min=0.027  max=2.807  mean=0.405  median=0.213  stdev=0.502
r(log M200, offset/R200)             = -0.543  (p<0.001) -- more massive
                                        clusters in this sample have
                                        systematically SMALLER offset
r(offset/R200, WHIM%), raw           =  0.154  (n.s.)
r(mass-detrended offset resid, WHIM%)= -0.083  (n.s.)
```

**Robustness check on the single most extreme point** (halo 38,
offset=2.81×R200 — flagged as a real outlier before trusting the full
sample, not silently included): excluding it, `r(logM,offset)=-0.480`
(still `p<0.001`) and the mass-detrended residual correlation becomes
`-0.057` (still not significant) — **the null result is not an
artifact of one extreme point.**

**Verdict: a second, independent, standard dynamical-state proxy also
fails to show a mass-independent relation to WHIM%** in this N=71
sample. Combined with the `GroupNsubs` result above, two real,
different, physically-motivated confound-control candidates both come
back null — worth taking as a real (if still limited-N) signal that
either (a) dynamical state genuinely does not drive WHIM% much beyond
what mass explains, at least via these two proxies, or (b) both proxies
are individually too coarse/noisy to detect a real but modest effect at
`N=71`. Not distinguished here.

## Third addendum, same day — DM velocity dispersion within R200 checked,
## THIRD dynamical-state proxy also null (positive control confirms the
## pipeline itself is sound)

**Question:** does DM particle velocity dispersion within R200 (relative
to the group's own bulk velocity, `GroupVel`) — a real, standard
dynamical-state indicator closely tracking the M-sigma relation — carry
mass-independent information about WHIM%?

**Design note:** a subhalo/galaxy-based sigma_v would match real
observational practice more closely, but a live probe first (not assumed
from memory) showed individual clusters carry hundreds of subhalos (halo
200: `GroupNsubs=859`) with no bulk velocity field-selection available on
the subhalo search endpoint — that route would need one API call PER
SUBHALO, tens of thousands total across the sample. Switched to a DM
particle cutout per cluster (`Coordinates,Velocities`, same pattern as
the gas cutouts) instead — one request per cluster, tractable.
`experiments/20260909-tng-whim-pilot/velocity_dispersion_confound.py` →
`whim_n71_with_vdisp.csv`.

**Built-in positive control, and it passed cleanly:** sigma_v is expected
to be strongly, positively collinear with M200 (the M-sigma relation is
one of the tightest scaling relations in cluster physics) — confirmed:
`r(log M200, log sigma_v) = 0.938` (`p<0.001`, N=71). A single-cluster
sanity check (halo 200, M200~1.2e14 Msun) gave `sigma_v=440` km/s,
consistent in order of magnitude with the Evrard et al. 2008-type M-sigma
relation (`[MEMORY]`-tier coefficients, not re-verified live — a rough
consistency check, not a precise one).

**Result:**
```
r(log M200, log sigma_v), raw           =  0.938  (p<0.001) -- positive control, as expected
r(log sigma_v, WHIM%), raw              = -0.380  (p<0.01)  -- echoes the mass-WHIM link
r(mass-detrended sigma_v residual, WHIM%)=  0.020  (n.s.)    -- ~zero once mass is removed
```

Two clusters were dropped from the 71 during checkpointed collection due
to a transient server-side degradation (11 consecutive halo IDs failing
`info.json` in a row, mid-run — `BLOCKED-INFRASTRUCTURE` per the
Substrate Gate, not evidence about those clusters) and successfully
recovered on retry; final N=71, no clusters permanently missing.

**Verdict: a third, independent, standard dynamical-state proxy also
fails to show a mass-independent relation to WHIM%.** Combined with
`GroupNsubs` and CM/potential-minimum offset, **three different,
physically-motivated confound-control candidates now all come back
null** at N=71. Unlike the first two (which were only moderately
collinear with mass, `r≈0.5-0.6`), velocity dispersion is *very* strongly
collinear with mass (`r=0.938`) — its own positive control is one of the
cleanest results in this whole experiment, which makes the null residual
result correspondingly more trustworthy: the measurement pipeline
demonstrably CAN detect a strong real signal (mass itself, via sigma_v)
and still finds nothing left over for WHIM% once that signal is removed.

**What this does NOT establish:** with three different proxy types now
null, it becomes more plausible (not proven) that dynamical state, at
least as captured by these catalog-native and particle-level proxies,
is not a major independent driver of this sample's WHIM% — but a
synthetic-X-ray-based morphological indicator (Ansarifard+2019's own
VR/R/IR/VI classes, azimuthal scatter) remains untested and is a
methodologically different class of proxy, not covered by any of the
three tried here.

## Fourth addendum, same day — temperature-profile mechanism test: a
## real POSITIVE finding, not another null

**Question:** does the candidate mechanism named above ("more massive
clusters have deeper potential wells producing more extended already-
shock-heated (>10⁷K) gas past R200, shrinking the WHIM-temperature-
window's captured fraction") actually hold, checked directly against
the temperature profile shape instead of just the binary WHIM split?

**Method:** `temperature_profile_vs_mass.py` re-fetched gas cutouts for
the same 71 known-good clusters (deleted after the original batch;
same fields, same formula) and split annulus gas into three bins —
cold (`T<1e5K`), WHIM (`1e5-1e7K`), hot (`T>1e7K`) — instead of the
original binary split, plus a radial sub-split (inner `1.0-2.0×R200`
vs. outer `2.0-3.0×R200`).

**Positive control passed exactly:** recomputed WHIM% matches the
original CSV's own value to `0.0000` percentage points for all 71
clusters — same formula, same fields, confirms this is a real
re-measurement, not a different pipeline giving a different answer by
accident.

**Result — the candidate mechanism is supported, and its own radial
signature confirms WHERE:**
```
r(log M200, hot_fraction_pct)                      =  0.386  (N=71, p<0.001)
r(log M200, hot_fraction_inner [1.0-2.0 R200])      =  0.503  (N=71, p<0.001)
r(log M200, hot_fraction_outer [2.0-3.0 R200])      = -0.177  (N=70, n.s.)
```

More massive clusters DO have a significantly larger fraction of
`T>1e7K` ("hot," non-WHIM) gas in their annulus — and this effect is
concentrated in the INNER half of the annulus (`1.0-2.0×R200`, where
shock-heated gas driven by a deeper potential well would physically be
expected to sit), not spread out to the outer edge near `3×R200`, where
the correlation with mass vanishes. This is internally consistent with
the named mechanism, not just a restatement of the original WHIM-mass
anticorrelation under a different name — the radial split is new
information the original binary WHIM/non-WHIM measurement could not
show.

**What this does NOT establish:** that this is the ONLY mechanism
behind the Li+2025 discrepancy — the other two named candidates
(different sim physics, different radial-binning convention) remain
untested; that the effect is causal in the sense of confirming the
"deeper potential well" physical story specifically, as opposed to some
other mass-dependent heating process with the same radial signature;
anything about MULTING (`NO_AUTHOR_ERROR` — this is standard ICM/WHIM
astrophysics in a public simulation, unrelated to v82's own claims).

## Fifth addendum, same day — the Fourth Addendum's own suggested
## follow-up (hot vs. WHIM fraction, mass-controlled) turns out to be
## a near-tautology, not new information

**Question, named as a cheap follow-up in the pearl_registry row for
the Fourth Addendum:** does `hot_fraction` predict `WHIM_fraction`
beyond what mass alone already explains?

**Caught before over-interpreting it:** `cold_fraction + WHIM_fraction
+ hot_fraction = 100%` EXACTLY for every cluster — they are a 3-way
split of the same fixed annulus mass, not three independent
measurements. `hot_vs_whim_partial_correlation.py` computed the raw
correlation (`r=-0.984, p<0.001`) and then, explicitly, the correlation
implied by the arithmetic alone if `cold_fraction` were exactly zero
(`r=-0.986`) — the two are nearly identical. **The near-perfect
anti-correlation is a structural consequence of the closed 3-part
composition (`cold_fraction` is small, ~1.9% ± 1.1%, so
`WHIM≈100−hot`), not new physical evidence that hot and WHIM gas trade
off for a reason beyond arithmetic.** Mass-detrending both sides first
does not escape this (`r=-0.984` again) — the compositional constraint
holds regardless of mass.

**Verdict:** this specific follow-up, as originally scoped, does not
add information beyond the Fourth Addendum's own hot-fraction-vs-mass
result. A genuinely independent test of "does hot gas trade off against
WHIM gas for a real physical reason" would need a measure that is NOT
mechanically complementary — e.g. absolute WHIM mass (not fraction) vs.
absolute hot mass, or a comparison across radius rather than across
temperature bins at fixed radius. Not attempted here — named as the
corrected version of this follow-up, not built.

## Next step, named not done

1. ~~Analyze `group_nsubs` as a dynamical-state proxy~~ — **done, real
   negative result** (see Addendum above).
2. ~~Analyze CM/potential-minimum offset~~ — **done, second real
   negative result, robust to the one outlier** (see Second Addendum
   above).
3. ~~Analyze DM velocity dispersion within R200~~ — **done, third real
   negative result, positive control confirms the pipeline itself is
   sound** (see Third Addendum above). No further catalog/particle-level
   dynamical-state proxy is currently named as untested; a
   synthetic-X-ray morphological indicator would need a pipeline this
   project does not have.
3a. ~~Check the full temperature profile shape vs mass~~ — **done, real
    POSITIVE result: hot-gas fraction increases with mass, concentrated
    in the inner annulus** (see Fourth Addendum above). One of the three
    named candidate explanations for the Li+2025 discrepancy is now
    supported; the other two (sim physics, radial-binning convention)
    remain untested.
4. **Wait for or pursue the external hydrostatic-mass data** — the
   actual bottleneck for H1b itself.
5. If the Three Hundred data arrives for a comparable cluster sample,
   this batch's own 71 WHIM measurements are immediately reusable — no
   rework needed on this half.
