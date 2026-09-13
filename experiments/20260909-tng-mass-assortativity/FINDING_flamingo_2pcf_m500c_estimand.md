# FINDING — a first real 2PCF-style estimand on M500c-selected FLAMINGO
# clusters: order-of-magnitude and richness-direction match v82's own
# cited literature anchor; correlation SHAPE does not; several
# structural confounds remain unaddressed

**Date:** 2026-09-12
**Claim tested:** `CLAIM_flamingo_2pcf_m500c_estimand.md`
**Script:** `flamingo_2pcf_m500c_estimand.py`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (raw output, real FLAMINGO data, live `hdfstream` download)

```
FLAMINGO cosmology h = 0.681 [VERIFIED from file Cosmology attrs]

=== Negative control: N=1000 uniform-random positions ===
3/15 bins have RR<1 (too sparse for a Gaussian Poisson-noise check)
Of the remaining 12 bins with RR>=1: 11/12 have |xi| <= 2*sigma_Poisson
xi range (all bins): [-1.0000, 1.0134], mean=-0.1449

=== M500c-selected FLAMINGO clusters: xi(r) and power-law fit ===
     N     r0_mpc    gamma n_bins_fit  r0_hinv_mpc   M500c_min_1e14Msun
   200      35.09    2.615         10        23.89                4.858
  1000      24.04    2.228         14        16.37                2.502
  5000      19.61    2.119         15        13.35                1.037
```

`M500c` selected DIRECTLY from the full catalog (not re-ranked from an
`M200c`-filtered pool). `h=0.681` read from the file's own `Cosmology`
attrs, not assumed.

## Independent re-verification (before dispatching the skeptic)

Confirmed the RR(r) analytic formula and pair-counting code on a
synthetic uniform-random catalog (N=3000, independent of the script's
own N=1000 negative control): 15/15 bins gave `xi≈0` within 2-sigma
Poisson noise, DD and RR agreed to the expected sampling precision at
every bin — the estimator machinery is correct before touching real
cluster data.

## Independent skeptic review (Step 8a, context-blind — claim + code +
## raw output ONLY, no reasoning chain)

**Verdict: WEAKENED.**

(a) **Analytic `RR(r)` for a periodic box — CONFIRMED, clean.** The
minimum-image convention plus `r_max=150 Mpc < L/2=500 Mpc` puts this
entirely inside the regime where the closed-form `RR(r)=4πr²/V` is
exact — no survey-mask or edge correction needed, a genuine advantage
of using a periodic simulation box over a real observational footprint.

(b) **Negative control — WEAKENED, structurally underpowered.** Three
real problems: (i) the reported `mean=-0.1449` is an artifact — three
`dd=0` bins are pinned at exactly `xi=-1` by construction and drag the
naive mean down; the informative number is the 11/12-testable-bins
figure, not the mean. (ii) `sigma=1/sqrt(DD)` treats pairs as
independent samples when they are not (the same halo appears in many
pairs, inflating true variance above the naive Poisson estimate) — the
check is stricter than a fair one, so passing it is not as strong
evidence as it looks. (iii) only `N=1000` was tested; `N=200`'s much
sparser counts (`dd∈{0,1,2,3}` in five bins) were never independently
validated by a matched-`N` control. (iv) no POSITIVE control (a
planted, known `r0`/`gamma` signal, checked for recovery) exists —
"absence-only battery, no canary," a real gap.

(c) **`N=200` fit — FALSIFIED as a trustworthy quantitative result.**
The unweighted `log(xi)` vs. `log(r)` regression gives the `dd=2`
outlier bin (`r=11.1` Mpc, `xi=24.60`) the SAME regression weight as
the `dd=147` bin at `r=133.9` Mpc — a ~74x-better-measured point. The
reported `r0=35.09`/`gamma=2.615` for `N=200` should not be quoted
against literature without reweighting or an outlier-robust refit.

(d) **Apples-to-apples with Basilakos & Plionis 2004 — WEAKENED, real
confounds unflagged.** Five structural confounds named: selection
function (real survey vs. clean mass cut), redshift (survey-averaged
vs. `z=0` only), what "cluster" means (observational classification vs.
`SOAP-HBT` halo), estimator differences (Landy-Szalay-on-a-mask vs.
Peebles-Hauser-on-a-periodic-box — should agree in principle but not
independently checked here), and fit range (unspecified in the cited
paper vs. this run's `5-150` Mpc). A SIXTH, this project's own: the
claim's `"= 30.40 Mpc physical (FLAMINGO h=0.681)"` conversion line
mixes coordinate systems — it applies FLAMINGO's own `h` to convert
the LITERATURE's `h^-1` Mpc quote into a physical distance, which is
not a meaningful operation (the literature's own physical distance used
THEIR `h`, not FLAMINGO's). **Correction applied below**: the
comparison is retained ONLY in `h^-1` Mpc units (both sides using their
own `h` internally, the standard h-independent convention), the
"physical Mpc via our own h" line is retracted.

(e) **Overclaim check on the qualitative finding — WEAKENED.** Two real
overclaim risks: (i) the `gamma` mismatch (FLAMINGO `2.1-2.6` vs.
literature `1.6-2.0`, systematically steeper) is a real shape
disagreement, not a detail to omit — a power law with matching `r0` but
different `gamma` is a genuinely different correlation function. (ii)
The `N=200` number that comes CLOSEST to the literature's richer-
subsample value (`23.89` vs. `20.7` h^-1 Mpc) is exactly the one shown
in (c) to be outlier-sensitive — the strongest headline datum is the
least trustworthy one, as computed.

## My own independent quantification of (c)'s outlier sensitivity
## (re-derived, not accepted on the skeptic's estimate alone)

```
N=200, unweighted, all 10 valid bins:        r0=35.09 Mpc, gamma=2.615 (r0_hinv=23.90)
N=200, unweighted, dd=2 outlier excluded:    r0=34.58 Mpc, gamma=2.542 (r0_hinv=23.55)
N=200, weighted by sqrt(dd) (Poisson proxy): r0=32.41 Mpc, gamma=2.212 (r0_hinv=22.07)
```

**Tighter than the skeptic's own qualitative flag, stated explicitly:**
`r0` moves modestly under both corrections (`35.09 -> 32.41`, a `~8%`
shift, staying within the same broad range as the literature's richer
subsample, `20.7` h^-1 Mpc). `gamma` moves more (`2.615 -> 2.212`), but
even the corrected value stays clearly steeper than the literature's
`1.6`. **Net: the order-of-magnitude `r0` match survives outlier
correction; the `gamma` mismatch does not go away under any of the
three fits tried.**

## Response to skeptic (per Step 8a Response Matrix)

- **(a) CONFIRMED-REAL** — promoted unchanged.
- **(b) Accepted, mitigated in this write-up** — negative-control
  interpretation corrected (11/12 testable-bins figure is the real
  diagnostic, not the mean); the single-`N`/no-positive-control gaps are
  disclosed as real limitations of this FIRST pass, not fixed here.
- **(c) Accepted, quantified independently** — see the table above; the
  `N=200` unweighted number is retracted as a standalone quote, the
  weighted/outlier-excluded alternatives are reported alongside it.
- **(d) Accepted, corrected** — the physical-Mpc unit-mixing line is
  retracted; comparison retained in `h^-1` Mpc only. The five other
  confounds are disclosed, not resolved (out of scope for a first pass).
- **(e) Accepted, language downgraded** — see "What this DOES
  establish" below; "reproduces the amplitude range" is replaced with a
  narrower, correctly-scoped statement.

## What this DOES establish

- FLAMINGO's own `M500c`-selected cluster population, ranked by mass as
  a richness proxy, shows a two-point correlation amplitude
  (`r0 ~ 13-24` h^-1 Mpc across `N=200` to `N=5000`, robust to outlier/
  weighting corrections at the `~8%` level) that lands in the SAME ORDER
  OF MAGNITUDE as v82's own cited empirical anchor (Basilakos & Plionis
  2004: `9.7-20.7` h^-1 Mpc) — a check nothing in this branch has done
  before, and a genuine (if modest) positive finding: FLAMINGO is a
  plausible stand-in population for the empirical route v82 itself
  cites, at least at the order-of-magnitude level.
- The DIRECTION of richness-dependence matches: fewer/more-massive
  (`N=200`) gives a larger `r0` than more/less-massive (`N=5000`), the
  same qualitative pattern the cited literature reports between its own
  richer and poorer subsamples.
- The analytic periodic-box `RR(r)` estimator is verified correct
  (synthetic test + skeptic confirmation) — a reusable, validated piece
  of machinery for any future 2PCF-style work on FLAMINGO.

## What this does NOT establish

- **Does NOT establish shape agreement** — `gamma` is systematically
  steeper in FLAMINGO (`2.1-2.6`) than in the cited literature
  (`1.6-2.0`), a real, unresolved disagreement, not a detail to smooth
  over.
- **Does NOT** validate mass-rank as equivalent to observational
  richness — a disclosed, unaddressed proxy assumption.
- **Does NOT** control for the five further confounds named in (d)
  (selection function, redshift, cluster-definition mismatch, estimator
  differences, unmatched fit range) — real, structural, sim-vs-
  observation gaps, not attempted to be closed here.
- **Does NOT** compute a mass-assortativity `rho` (the original P158-
  style question) — this first pass measures spatial clustering
  amplitude only; a mass-marked generalization is a separate, not-yet-
  attempted follow-on.
- **Does NOT** provide a rigorous statistical test of agreement with
  the literature values (no error bars are computed for `r0`/`gamma`
  themselves — a bootstrap or jackknife over the cluster sample would be
  needed for that, not attempted here).
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Status

First real computation for `docs/162` item 9. A genuine, if narrow,
positive step (order-of-magnitude + richness-direction corroboration)
alongside a real, disclosed shape mismatch (`gamma`) and several
unaddressed confounds. Item 9 is NOT closed by this — it establishes
that the estimand-construction direction is viable and worth
continuing, not that it is finished. The natural next differentiating
step (not run here, not authorized by this FINDING alone) would be a
mass-marked generalization (does mass assortativity show up in a
properly-weighted, full-population 2PCF-style statistic, replacing the
now-closed `rho_NN` design) — named, not attempted.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
