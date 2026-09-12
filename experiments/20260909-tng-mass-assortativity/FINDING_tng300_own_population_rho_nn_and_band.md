# FINDING — TNG300's own population, matched to FLAMINGO's selection
# protocol: INCONCLUSIVE. `rho_NN=-0.42` at `N=35` is noise-consistent,
# not independent of the already-falsified `N_sub=30` alarm; `rho_band`
# unmeasurable (`N_pairs=3`); does not discriminate Hypothesis A from B

**Continues:** `CLAIM_tng300_own_population_rho_nn_and_band.md`
(committed BEFORE the script ran) → `FINDING_flamingo_addendum_
jackknife_band_closure.md`'s own named next step. **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, from the already-cached `top_halos_pos_mass.csv`,
## no new API call, frozen `N_SUB=35`)

```
median true-NN separation: 43.92 Mpc, mean: 42.25 Mpc (both in target window)

rho_NN   = -0.4208 (t=-2.67, nominal p<0.01)
rho_band = -0.3577 (N_pairs=3, 40-45 Mpc)

Permutation null (1000 draws), rho_NN:   mean=-0.0304, SD=0.2040, p=0.028
Permutation null (1000 draws), rho_band: mean=-0.1912, SD=0.4968, p=0.624

Reference:
  TNG300 FULL sample (N=1461, non-mass-matched): r=+0.3827, N_pairs=4694
  FLAMINGO (N=1200, mass-matched, SAME protocol): rho_NN=-0.0231, rho_band=+0.0271
```

## Independent skeptic review (Step 8a, context-blind) — five questions

Full text preserved in the session record. **Every quantitative claim
in the skeptic's own report was independently re-derived before use**
(`audit-verification-gate.md`) — one real correction to the skeptic's
own supporting number found in the process, detailed at item 4.

1. **Is `N=35`'s selection genuinely blind to outcome? (`WEAKENED`.)**
   The 13-candidate exploratory bracket computed ONLY NN-separation
   statistics, never a correlation — legitimate blinding on the
   outcome variable, escaping the SPECIFIC "look-elsewhere across
   nested r-values" failure mode that killed the earlier `N_sub=30`
   point. **But a different, still-live concern survives**: top-`N`-
   by-mass selects the rarest, most strongly-clustered halos
   (assembly bias) — the SAME critique `FINDING_scale_matched_
   nearest_neighbor_rho.md`'s own skeptic pass already raised against
   `N_sub=30`. Renaming the failure mode (blind vs. nested) does not
   remove the underlying selection concern.
2. **Is `rho_NN=-0.4208, p=0.028` real signal? (`FALSIFIED` as robust
   signal; `WEAKENED` as a flagged anomaly.)** Analytic SD at `N=35`
   (`1/sqrt(N-2)=0.174`) and the empirical permutation SD (`0.204`)
   agree closely — independently re-verified. **Corrected distance
   calculation**: `|-0.4208-(-0.0304)|/0.204 = 1.91` (not the skeptic's
   own `~2.06` — re-derived directly, a small arithmetic slip in the
   skeptic's own report, caught before use). The DIRECT empirical
   permutation p-value (`0.028`) is the honest number to cite, not a
   derived sigma-count — consistent with this branch's own recent
   `"don't overclaim a sigma-count"` lesson (`pearl_registry`,
   2026-09-12). **Critical fact, independently verified by direct
   halo-ID intersection (user-requested check, 2026-09-12), not
   inferred**: `top-30` is an EXACT subset of `top-35` — `30` of `35`
   halo IDs identical (`85.7%`), the `5` "new" halos being exactly
   ranks `31-35` by mass (`3.573e14`-`3.696e14` Msun, the lowest-mass
   halos in the `N=35` sample). This is NOT an independent re-test of
   the earlier `N_sub=30` alarm — it is the SAME `30` halos plus `5`
   more, in the SAME single simulation box. A `~2σ` result computed on
   data that is `85.7%` identical to an already-falsified `~2.6σ`
   result is not new evidence, by construction, not merely by
   plausible inference.
3. **Is `rho_band=-0.3577` (`N_pairs=3`) usable? (`FALSIFIED`.)** Three
   raw pairs (six after symmetrization) cannot support a correlation
   estimate — permutation SD (`0.497`) confirms the statistic itself
   carries essentially no information (`p=0.624`). **Reported here for
   completeness only; not used in any conclusion below.**
4. **Does the `TNG300` vs. `FLAMINGO` gap discriminate Hypothesis A
   from B? (`WEAKENED`.)** Two-sample Fisher-`z` test, independently
   re-derived: `Z=-2.38, p~=0.017` (normal approximation) — a marginal
   difference, not a clean rejection of "same underlying `rho`."
   **Correction to the skeptic's own supporting reasoning**: the
   skeptic's report attributed part of this gap to FLAMINGO's `N=1200`
   selection being systematically "more massive... fewer per unit
   volume" than TNG300's `N=35`, based on a stated volume ratio of
   `~114x`. **That ratio is itself a pre-existing arithmetic error in
   this branch, caught independently during this same check**:
   `(1000/302.6)^3 = ~36x`, not `114x` (see the dated correction in
   `CLAIM_flamingo_independent_rho_check.md`; no effect on any
   previously-reported `rho`/SD/CI number, only this descriptive
   ratio). Recomputing the number-density match with the corrected
   ratio: `FLAMINGO`'s own density (`1200/1e9 Mpc^-3`) times `TNG300`'s
   volume gives an EXPECTED `~33.3` halos — almost exactly `TNG300`'s
   own actual `N=35` selection (density ratio `1.05`). **The two
   selections are actually closely matched in number density** — the
   "different mass regime" explanation for the gap is weaker than the
   skeptic's report suggested; the marginal `2.4 sigma` gap stands on
   its own, without that additional (incorrect) supporting argument.
5. **Overall honest verdict? (`INCONCLUSIVE`, matching the claim's own
   pre-committed fallback.)** Cannot discriminate Hypothesis A
   (observable difference), Hypothesis B (population/simulation
   difference), or a third explanation (small-`N` sampling noise
   dominates any single-box estimate at this regime) — all three
   remain consistent with the data.

**Response (Step 8a matrix): all five points accepted; two
corrections made to the skeptic's own supporting numbers (item 2's
sigma-count, item 4's volume-ratio-dependent reasoning) before use,
neither changing the final verdict.**

## What this DOES establish

- **`rho_NN=-0.42` at TNG300's own `N=35`, matched to FLAMINGO's
  selection protocol, is a genuinely blind (not nested-swept) single
  test — but is noise-consistent at this small `N`, and is NOT
  independent evidence separate from the already-falsified `N_sub=30`
  point (verified `85.7%` halo-ID overlap — `30/35` identical, not
  inferred).** Flagged as an anomaly worth
  independent replication in a larger, genuinely different volume —
  not a standalone result.
- **`rho_band` cannot be measured at TNG300's own matched `N=35`**
  (`N_pairs=3`) — the box is simply too small at this mass/scale
  combination to populate the band observable at all.
- **A genuine, unrelated arithmetic error (`~114x` should be `~36x`
  for FLAMINGO's own volume advantage over TNG300) was caught and
  corrected across 6 files during this check** — descriptive only, no
  computational impact on any prior result.
- **The one pattern that continues to hold up across every scale-
  matched attempt in this entire branch (TNG300's own mass-rank sweep,
  Magneticum, FLAMINGO, and now this test) is that NONE of them
  reproduces TNG300's own well-powered, non-mass-matched `+0.38`
  reading** — every attempt at the target `40-45` Mpc scale, in every
  simulation tried, gives something small, negative, or statistically
  indistinguishable from zero. This is suggestive but not, by itself,
  a decisive discrimination between "the `+0.38` reflects a broader
  population/selection effect" and "small-`N` scale-matched samples
  are simply too noisy to see a real, smaller positive signal."

## What this does NOT establish

1. Does NOT confirm Hypothesis A or B — genuinely inconclusive.
2. Does NOT independently corroborate the earlier `N_sub=30` alarm —
   same halos, not new evidence.
3. Does NOT establish `rho_band` at TNG300's own matched scale in any
   form — unmeasurable at this `N`.
4. Does NOT resolve whether "top-N-most-massive-halos" is the right
   operational definition of v82's own "node" — unchanged.
5. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**A real, honestly-inconclusive result, exactly as pre-committed.**
The discriminating test named in the FLAMINGO addendum has now been
run — it does not settle Hypothesis A vs. B, but it does rule out
treating `TNG300`'s own `N=35` matched subsample as either a clean
replication of FLAMINGO's near-zero result or a clean revival of the
earlier `N_sub=30` concern. The honest state of the magnitude/mechanism
question remains UNDETERMINED, now on a firmer, better-understood
footing (the noise floor at small `N` is now explicitly quantified,
not just asserted).

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
