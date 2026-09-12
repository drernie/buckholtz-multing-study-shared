# FINDING — the "true global NN" ground-truth attempt is itself
# invalidated by a scale/density mismatch, self-caught before write-up
# and independently confirmed by Step 8a skeptic; a concrete fix is
# identified but not implemented

**Continues:** `CLAIM_flamingo_subvolume_true_global_nn.md` (committed
BEFORE the script ran) → `FINDING_flamingo_subvolume_replication.md`
and `FINDING_flamingo_subvolume_periodic_wrap_bias.md`'s own shared
recommendation for a true, pre-cut global-NN reference. **User-
requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, live `hdfstream` data) — and the design flaw found
## in it, self-caught before any conclusion was written

```
rho_NN true:     mean=-0.1574, SD=0.2006  (1/10 reach |rho|>=0.42)
rho_NN periodic: mean=0.0145,  SD=0.2069  (0/10)
rho_NN open:     mean=-0.0394, SD=0.2321  (1/10)
mean fraction of halos whose true-NN partner is NOT in the sub-cube's
  own local top-N: 75.7% (range 65-87%)
```

**Before treating any of this as informative, a follow-up check was
run** (not part of the original script) on the ACTUAL separation scale
of the "true" pairs:

```
true-NN separation (n=400 halo-instances across all 10 cubes):
  median=21.62 Mpc, mean=23.97 Mpc
  fraction in the original [40,45] Mpc target window: 5.0%
  fraction < 40 Mpc: 86.8%
```

**This is disqualifying.** The "true" search pool (top-`5000`-by-
GLOBAL-mass across FLAMINGO's whole box) has number density `~4x`
higher than each sub-cube's own local selection (density ratio
independently verified: `5000/1000^3` vs. `35/302.6267^3` `= 3.96`) —
because the local selections went deep enough in LOCAL mass rank to
hit `40-45` Mpc specifically for each region's own local density, while
the global pool includes many additional, LESS MASSIVE halos never
eligible for any sub-cube's own "top local `N`" selection. **`rho_true`
as computed answers a DIFFERENT question — mass assortativity at
`~22` Mpc median separation, among a denser, lower-average-mass partner
population — not the `40-45` Mpc question this entire branch is about.**

## Independent skeptic review (Step 8a, context-blind) — the scale
## mismatch was disclosed IN the prompt for independent scrutiny, not
## hidden; skeptic confirmed it and found a second, separate problem

Full text preserved in the session record. **Every quantitative claim
independently re-derived before use** — density ratio `3.96` confirmed
exactly; Poisson-scaling prediction (`density_ratio^(-1/3) * 42.5 =
26.9` Mpc, vs. observed `21.62` — same direction, somewhat more shrunk
than naive scaling, consistent with real halo clustering) confirmed;
the counting-identity check on `frac_outside` (average sub-cube
population `~139` vs. average `local_N=40` gives `(139-40)/139=71%`,
close to the observed `75.7%`) independently re-derived and confirmed.

1. **Does the scale mismatch invalidate `rho_true` (`FALSIFIED` — as a
   ground truth for the original question)?** Confirmed: the predictor
   set stays mass-rank-consistent (each sub-cube's own local top-`N`),
   but the PARTNER set is drawn from a systematically denser, lower-
   mass population — asymmetric contamination of one arm of the
   correlation still contaminates `rho` as a whole. `rho_true`'s own
   headline (`mean=-0.157`, `1/10` anomalous) is **not informative for
   the `40-45` Mpc question** and should not be quoted as resolving the
   periodic-vs-open ambiguity.
2. **Is `-0.157` internally consistent with "assortativity at `~22`
   Mpc" (`NEEDS-REAL-DATA`)?** No independent prediction exists in this
   branch for what `rho` should look like at that (wrong but real)
   scale — cannot sanity-check the number either way. The directional
   agreement with TNG300's own `-0.42` (both negative) is noted as
   weak, not confirmatory — different scale, different partner pool,
   sign-agreement alone is closer to coincidence than replication.
3. **Is `frac_outside=75.7%` informative (`FALSIFIED`, plus a real
   labeling bug)?** The skeptic found the code computes "partner NOT in
   the cube's own local top-`N`" while the summary line describes it as
   "partner lies OUTSIDE the sub-cube" — **these are different
   measurements**, conflated in the write-up. A pure counting identity
   (population size `~139` vs. selected `~40`) already predicts
   `~71%` "not in local top-N" with NO physics involved — matching the
   observed `75.7%` closely. **This diagnostic is dominated by
   arithmetic, not a clean measurement of periodic-boundary failure.**
   A real fix requires disambiguating and recomputing the RIGHT
   quantity.
4. **Correct fix (`CONFIRMED-REAL` direction, concrete recipe
   supplied)**: anchor the true-NN partner pool to the SAME number
   density as each sub-cube's own local selection (not the full
   top-`5000`) — compute a global mass cutoff `M` such that `M`
   halos across the WHOLE `1000` Mpc box gives the SAME density as the
   local selections (`M~1080-1990` depending on per-cube vs. median
   anchoring), validate that this density-matched global pool's own
   median NN separation actually lands in `40-45` Mpc (an empirical
   check, not assumed), THEN redo the true-NN lookup against that
   density-matched pool. **Not implemented here** — named as the
   concrete next step, per the same "not yet run" discipline the
   whole branch has followed all session.

**Response (Step 8a matrix): all four points accepted. This is a
real, disclosed design error in my own test — caught by a follow-up
sanity check BEFORE writing any conclusion, and independently
confirmed (with an additional, separate labeling bug found) by the
mandatory skeptic pass, not defended or minimized.**

## What this DOES establish

- **The "true global NN" as implemented here is NOT a valid ground
  truth for the periodic-vs-open comparison** — a real, load-bearing
  design flaw (partner-pool density mismatch), caught and disclosed
  honestly rather than reported as a resolving result.
- **A concrete, implementable fix is identified** (density-matched
  partner pool, with an empirical validation step) — a real next step,
  not yet run.
- **A separate, independent labeling bug in the `frac_outside`
  diagnostic** was found by the skeptic and confirmed by direct
  counting-identity arithmetic — the `75.7%` number, as reported,
  substantially overstates what it appears to measure.
- **The underlying periodic-vs-open question from the prior test
  remains exactly where it was left**: genuinely open, neither
  confirmed nor ruled out — this attempt to settle it with a "true"
  reference did not succeed, and the branch now knows precisely why,
  and what a working fix would require.

## What this does NOT establish

1. Does NOT provide a valid ground truth for the periodic-vs-open
   comparison — the attempt failed for a specific, understood reason.
2. Does NOT say anything reliable about mass assortativity at `40-45`
   Mpc from this specific test's own `rho_true` numbers.
3. Does NOT change TNG300's own `rho_NN=-0.42` verdict (still
   INCONCLUSIVE per `FINDING_tng300_own_population_rho_nn_and_band.md`)
   or the periodic-wrap bias verdict (still open per `FINDING_
   flamingo_subvolume_periodic_wrap_bias.md`).
4. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**A real, honestly-reported null result about this SPECIFIC test's own
validity — not a physics finding, a methods finding.** The concrete,
correctly-scoped fix (density-matched partner pool) is named and
implementable, but represents meaningfully more design work than this
specific attempt, and is not run here pending further direction.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
