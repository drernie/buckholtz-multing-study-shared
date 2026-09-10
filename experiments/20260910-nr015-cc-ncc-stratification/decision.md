# Decision — 20260910-nr015-cc-ncc-stratification

**Date:** 2026-09-10
**Status:** SURVIVES reading (1); does not eliminate reading (2)
**Evidence grade:** B (N=45/50, real observational CCCP data, same
dataset as NR-010/011/012/014/015)

## Numerical results

Positive control (`load_columns_pc()`, `N=50`, exact `NR-015` filter):
`r(delta_M, E_ICM | M_WL) = -0.7008` and `r(delta_M, T_X | M_WL) = -0.8108`
— both match `NR-015`'s own reported numbers to `<0.001`. **PASS.**

Stratification sample (`N=45`, requires `K0`/`wX`/`P3P0` also present —
5 of the 50 lack full morphology data):

| Split | Relaxed/CC | Disturbed/NCC | Fisher z-test |
|---|---|---|---|
| `K0<30` vs `K0>=30` | `N=6`, too small — skipped | `r=-0.816` (`N=39`) | not computable |
| `wX` median split | `r=-0.866` (`N=22`) | `r=-0.843` (`N=23`) | `z=-0.265, p=0.791` |
| `P3P0` median split | `r=-0.763` (`N=22`) | `r=-0.861` (`N=23`) | `z=+0.912, p=0.362` |

**A real, unplanned finding on its own:** this X-ray-luminous CCCP sample
is heavily skewed toward non-cool-core clusters (`39/45` at `K0>=30`) —
the exact split `NR-015` itself pre-registered (`K0` cut) is underpowered
on this specific sample, through no fault of the design; the two
independent proxies already present in the same dataset (`wX`, `P3P0`)
are what actually deliver a usable, well-powered test here.

## Verdict

**Reading (1) — definitional-artifact — is favored over reading (2) —
common-physical-driver — by both usable splits.** Neither wX nor P3P0
shows the pattern reading (2) requires (concentration in the disturbed
subsample); both Fisher z-tests are consistent with no difference at all
(`p=0.79`, `p=0.36`). The `T_X`-`delta_M` partial correlation is present
at comparable strength in dynamically relaxed and disturbed clusters
alike — consistent with `T_X` entering `M_hydro`'s own HSE formula
mechanically, not with dynamical state driving the pattern through a
separate physical channel.

## What this does NOT establish

1. **Does not eliminate reading (2).** A null result on a difference test
   is not proof of no difference — with `N=22/23` per bin, this design
   has real but limited power to detect a moderate true difference in
   correlation strength. `wX`/`P3P0` are established, standard
   dynamical-state proxies, but neither is a perfect measure of "true"
   merger/relaxation stage — a genuine, real driver could still be
   partially masked by proxy imprecision.
2. **Does not quantify the actual size of the artifact.** The
   complementary, still-unrun literature check named in `NR-015`'s own
   Relaxation Map (row 1: read Mahdavi et al. 2013's own HSE derivation,
   extract `∂ln M_hydro/∂ln T_X` for their specific pipeline) would
   directly test whether reading (1)'s mechanism has enough leverage to
   produce `r≈-0.81` on its own — this finding is consistent with that
   mechanism, not a direct measurement of its strength.
3. Does not touch `H1b`/WHIM — that branch remains structurally immune
   to this entire question either way (different gas phase, different
   radius range from the interior `T_X` used here).
4. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   of a CCCP-derived statistical pattern; no claim about MULTING/TJB's
   own theory.

## Kill Analysis

**What this test killed:** the specific prediction that the `T_X`-
`delta_M` correlation concentrates in dynamically disturbed clusters
(reading 2's own signature) — not observed in either of the two usable,
independent dynamical-state splits.

**What survives:** reading (1) as the better-supported explanation for
`NR-015`'s own collapse of the `M_gas`-only partial correlation, though
not proven to the exclusion of reading (2) given the power limits above.

## Update to NR-015

`NR-015`'s own status ("mechanism unresolved," both readings held
equally live) should be updated: reading (1) now has real, cross-
validated support; reading (2) has none from this specific test, though
it is not excluded. See `null_results/20260718-nr015-tx-shared-variable-
artifact.md`'s addendum.

## Files

- `claim.md` — pre-registration.
- `cc_ncc_stratification.py` — full analysis, positive control, 3 splits,
  Fisher z-tests. `ruff check` clean.
