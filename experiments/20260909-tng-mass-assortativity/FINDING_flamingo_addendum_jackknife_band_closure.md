# FINDING — FLAMINGO addendum: withdraws the "13 sigma" overclaim,
# replaces it with a properly-scoped jackknife CI; the all-pairs-in-band
# observable on the SAME subsample is underpowered to discriminate
# observable-difference from population-difference

**Continues:** `CLAIM_flamingo_addendum_jackknife_band_closure.md`
(committed BEFORE the script ran) → corrects `FINDING_flamingo_
independent_rho_check.md`'s own `"~13 sigma"` / `"rho<=-0.5 excluded"`
language, per an external methodological correction (the user, not
self-caught).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Why this exists

`FINDING_flamingo_independent_rho_check.md` stated: *"`-0.5` sits `~13
sigma` from this measurement's own null distribution."* This divides
the distance from the point estimate to `-0.5` by the **permutation-
null SD** (`0.0359`, the spread of `rho_hat` under `H0: rho=0`). That
SD characterizes the null distribution at `rho=0` — it is not
automatically the correct standard error for testing the *composite*
hypothesis `H0: rho<=-0.5`, since `Var(rho_hat)` is not constant in
`rho` (classical motivation for the Fisher `z`-transform:
`Var(rho_hat) ~ (1-rho^2)^2/(n-1)` under bivariate-normal, shrinking as
`|rho|` grows away from `0`). Reusing a null-centered SD for a distant
composite hypothesis is the same class of error `artifact-provenance-
gates.md` Gate 4 names generally — a quantity computed for one purpose,
reused for a different one without re-deriving it.

## Result (real, from a live `hdfstream` connection, on the SAME frozen
## `N=1200` subsample as the prior FLAMINGO test)

```
rho_NN   (true nearest-neighbor, identical to prior test): -0.0231
rho_band (all pairs, 40-45 Mpc, on the SAME N=1200, N_pairs=127): 0.0271

Spatial delete-one-block jackknife (5x5x5=125-block grid, 124 used):
  rho_NN jackknife SE:   0.0476
  rho_band jackknife SE: 0.1231
  rho_band N_pairs range across jackknife replicates: (119, 127)

CI-based test of H0: rho<=-0.5
  rho_NN   95% CI: [-0.1165, 0.0703]  -- excludes -0.5? YES
  rho_NN   99% CI: [-0.1458, 0.0996]  -- excludes -0.5? YES
  rho_band 95% CI: [-0.2142, 0.2685]  -- excludes -0.5? YES
  rho_band 99% CI: [-0.2901, 0.3443]  -- excludes -0.5? YES
```

For reference, three independently-derived SE estimates for `rho_NN`,
all of the same order: naive i.i.d. `1/sqrt(N-1) = 0.0289`, permutation-
null SD `= 0.0359`, block-jackknife SE `= 0.0476`. The jackknife SE
(which captures real spatial/large-scale-structure correlation that
mass-only permutation cannot) is the widest of the three, as expected.

## Independent skeptic review (Step 8a, context-blind — claim + code +
## raw output only, no reasoning chain)

Three questions posed: (1) is the jackknife itself sound, (2) is the
corrected `-0.5` exclusion now properly scoped, (3) does `rho_band`
actually discriminate "different observable" from "different
population/simulation." Full verdict text preserved in the session
record; response matrix below. **Every quantitative claim in the
skeptic's own report was independently re-derived before being
accepted** (`audit-verification-gate.md` — an agent's `[VERIFIED]` is
this project's `[INFERRED]` until re-checked) — one real error was
caught in that re-check, noted at item 2.

1. **Jackknife design (`WEAKENED`, no implementation bug found).**
   Block-jackknife variance formula coded correctly (`(k-1)/k *
   sum(theta_i - theta_bar)^2`); `200` Mpc blocks against a `~42` Mpc
   typical NN separation is a defensible choice (most NN pairs survive
   a single block removal); recomputing `rho_NN`/`rho_band` from
   scratch on the reduced set (not just reassigning "affected" pairs)
   is the correct approach since nearest-neighbor is a non-local
   operation; `124` replicates is enough for a stable variance estimate.
   **The real finding**: jackknife SE is a **local** estimate of how
   sensitive the statistic is to removing `1/125` of the data near the
   OBSERVED point (`rho~0`) — extrapolating it to bound behavior at a
   distant point (`rho=-0.5`) is not something delete-one-block
   jackknife promises by construction. This is not a bug; it is a
   mismatch between what the tool measures and what the original claim
   asked it to support. Accepted, addressed in item 2.

2. **Corrected `-0.5` scoping (`WEAKENED`, with a real correction to my
   own re-verification of the skeptic's own numbers).** The Fisher-type
   variance-shrinkage argument (`Var(rho_hat) ~ (1-rho^2)^2/(n-1)`)
   correctly predicts the TRUE SE at `rho=-0.5` is smaller than the
   local SE at `rho~0` — but this holds under i.i.d. bivariate-normal
   data, which real, spatially-clustered, truncated top-`N`-by-mass
   halo positions are not. The skeptic's own report additionally cited
   a Fisher-`z` "`SE(r) ~ 0.0566`" as an independent cross-check — **re-
   derived independently and found to be the 95% CI HALF-WIDTH
   (`1.96 * SE_z`), not the SE itself** (`SE_z = 1/sqrt(n-3) = 0.0289`,
   confirmed by direct calculation, matching the file's own previously-
   cited naive i.i.d. value). Corrected before use below. With that fix,
   Fisher-`z` SE (`0.0289`) actually agrees closely with the naive
   i.i.d. estimate and is narrower than the jackknife SE (`0.0476`) —
   consistent with jackknife capturing real extra structure the i.i.d.
   formula misses, not evidence against the jackknife.
   **Net: `-0.5` is excluded by all three independently-derived SEs at
   once** (`0.4769/0.0289=16.5`, `0.4769/0.0359=13.3`,
   `0.4769/0.0476=10.0` — verified directly), a margin wide enough that
   no single precise sigma-count is defensible (the normal-tail
   approximation this far out is not itself verified for this non-i.i.d.,
   truncated-selection dataset), but the qualitative conclusion is
   corroborated three independent ways, not resting on one borrowed
   number. **Corrected framing adopted below**: state the exclusion
   without a specific sigma value.
3. **`rho_band` vs. `TNG300`'s own `+0.38` (`FALSIFIED` for the strong
   reading; `CONFIRMED` for the weak reading).** **Strong reading
   rejected**: comparing `TNG300`'s own point value (`+0.38`) against
   this addendum's `rho_band` CI is a one-sample test against a fixed
   number, ignoring `TNG300`'s own sampling uncertainty at its
   `N_pairs=4694` (smaller than this test's `SE=0.1231`, but nonzero —
   independently checked: the gap between `+0.38` and this test's own
   99% upper bound (`0.3443`) is only `~0.3` of this test's own band
   SE, i.e. easily within noise, not a real exclusion). **More basic
   problem, independently confirmed**: `FLAMINGO`'s `N=1200` mass-
   matched subsample and whatever population `TNG300`'s own `+0.38`
   was measured on differ in density, mass range, and simulation —
   still confounded. A near-zero `rho_band` here is consistent with
   BOTH candidate explanations (different observable at fixed
   population vs. different population/simulation) and cannot
   discriminate them. **Weak reading holds**: this specific test, with
   `N_pairs=127`, has a `95%` CI half-width of `~0.24` — wide enough
   that a point estimate of `0.0271` is fully compatible with anything
   from roughly `-0.2` to `+0.3`. It is underpowered to say anything
   beyond "not obviously large," exactly as pre-registered in the claim.
   **The real discriminating test, not yet run**: measure BOTH `rho_NN`
   and `rho_band` on `TNG300`'s OWN population (not just cite its
   published `+0.38`) — if both match the FLAMINGO pattern (`band !=
   NN`, `band ~ large positive`, `NN ~ 0`), that supports observable-
   difference; if both instead depend on which population is used, that
   supports population/simulation-difference. Not attempted here.

**Response (Step 8a matrix): all three points accepted, none dismissed;
one arithmetic slip in the skeptic's own supporting number caught and
corrected before use, not passed through.**

## What this DOES establish

- **The `"~13 sigma"` / `"rho<=-0.5 excluded"` claim in `FINDING_
  flamingo_independent_rho_check.md` is WITHDRAWN as originally
  phrased.** It conflated a null-hypothesis-centered SD with the
  standard error needed for a distant composite-hypothesis test — a
  real, user-caught methodological error, not a computational bug (the
  arithmetic `0.4769/0.0359=13.3` is itself correct; the SD being
  divided by was the wrong quantity for that specific question).
- **The underlying qualitative conclusion survives, now on firmer
  ground than before**: `rho_NN` is small and consistent with zero;
  `rho<=-0.5` is excluded by a wide margin under THREE independently-
  derived SE estimates (naive i.i.d., permutation-null, block-
  jackknife) at once, rather than resting on one borrowed number — a
  real strengthening of the evidentiary base, even though the specific
  sigma-count is retracted.
- **`rho_band` on the SAME matched `N=1200` subsample is also small
  and statistically indistinguishable from zero** — it does NOT
  reproduce `TNG300`'s own `+0.38` on this population, but the test is
  too underpowered (`N_pairs=127`) to say whether that is because the
  observable differs, the population/simulation differs, or both —
  genuinely UNDETERMINED, not evidence favoring either explanation.

## What this does NOT establish

1. Does NOT provide a defensible precise sigma-count for the `-0.5`
   exclusion — only a qualitative "excluded by a wide margin,
   corroborated three ways" statement, honestly bounded by the fact
   that the normal-tail approximation this far out is unverified for
   this dataset's actual (non-i.i.d., truncated, spatially-clustered)
   structure.
2. Does NOT discriminate "different observable" from "different
   population/simulation" as the explanation for the `TNG300` `+0.38`
   vs. this branch's near-zero readings — the one test that would (both
   observables measured on `TNG300`'s own population) has not been run.
3. Does NOT resolve whether "top-N-most-massive-halos" is the right
   operational definition of v82's own "node" — unchanged from every
   prior finding in this thread.
4. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**A real, user-initiated correction of a genuine overclaim, applied
honestly rather than defended.** The practical answer to `FINDING_
P158`'s own safety question (`rho > -0.5`) is, if anything, on firmer
ground than the withdrawn "13 sigma" framing suggested (corroborated by
three independent SE estimates instead of one), while the specific
numeric precision claimed for that exclusion is retracted as
unsupported. The separate magnitude/mechanism question (`TNG300`'s
`+0.38` vs. near-zero true-NN readings) remains genuinely UNDETERMINED,
narrowed further by ruling out a clean discriminating read of this
specific `rho_band` sub-test, with the real next step named but not run.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
