# FINDING E17 ADDENDUM 2 — replacing the Duffy extrapolation shrinks
# the offset finding from ~2.5× to ~1.8×, and the skeptic caught a real
# arithmetic error in the first draft's own headline number

**Date:** 2026-09-06
**Continues:** `FINDING_E17_ADDENDUM_validated_against_correa2015.md`
(named this exact fix — a cluster-scale-calibrated concentration-mass
relation — as the next step). Explicit go-ahead given.

## L0 (EstimandOps)

**Descriptive.** Does replacing Duffy et al. (2008)'s own out-of-range
extrapolation with a concentration-mass relation the source paper itself
states is valid at this mass ("wide ranges in mass, redshift and
cosmology") change `E17`'s reported Jensen correction / offset at the
two flagged high-`z` points?

## What was found and used

Correa, Wyithe, Schaye & Duffy (2015), *"The accretion history of dark
matter halos III: A physical model for the concentration-mass
relation,"* `[VERIFIED-arXiv:1502.00391]` — Paper III of the same series
as Paper II (`1501.04382`), already reused unchanged in `E17`'s own
`z_{-2}`/`α`/`β`/`M(z)` chain. Their own Planck-cosmology fitting
function (fetched directly from LaTeX source, `z≤4`, "at all halo
masses" — no narrow fitted-range ceiling) replaces ONLY
`duffy2008_concentration_median`; every other piece of `E17`'s own
machinery is reused unchanged.

## Step 8a skeptic — real, substantive findings, addressed in place

The first draft's headline claim ("divergence shrinks from ~5× to ~2.8×
at `z=2.33`") was reviewed with the full formula, code, and output
pasted inline. Verdict: **CONFIRMED-REAL** on the code diff, sign
structure, and shift arithmetic; **WEAKENED** on four specific points,
three addressed here, one left explicitly open:

1. **No external reproduction control.** PC1-PC3 were tautological
   (implementation identities or a weak plausibility band). **Fixed:**
   found a real, directly-quoted number in the source paper's own
   Discussion (§4.4): *"a `10^10 h^-1 M_☉` halo at `z=2`... `c~5.25`"*
   (WMAP5 instantiation of the same model). This project's Planck
   fitting function gives `c=5.79` at the same `(M,z)` — `10%` agreement,
   a real external check the formula could have failed and didn't. Added
   as `PC4`.
2. **Arithmetic error in the headline number.** The first draft's
   "`~2.8×`" scaled the divergence by the offset alone, silently dropping
   the Jensen factor. **Fixed:** the correct scaling is
   `divergence ~ 1/(offset·jensen)`, giving `old 2.55× → new 1.82×` at
   `z=2.33` — a real correction to a number that would otherwise have
   been reported wrong.
3. **Was evaluating the new relation at `z=0` (not `z_obs`) a defensible
   choice, or a silent default?** A real, substantive question — the
   skeptic hand-computed that Paper III's own formula evaluated directly
   at `z=2.33` gives a *different* concentration than the `z=0`-anchored,
   Paper-II-projected value this file uses. **Resolved by reasoning, not
   a re-run:** v82's own `M(z)=M0·(1+z)^{-1.1}` treats `M0` as the `z=0`
   anchor mass of a single tracked object — exactly Correa Paper II's own
   trajectory semantics. Evaluating Paper III's `c(M0,z_obs)` directly at
   each `z_obs` would ask about a *different* halo (one observed at that
   redshift, not one whose `z=0` mass is `M0`) — internally inconsistent
   with the comparison being made. Stated explicitly in the script's own
   output, not left implicit.
4. **Two caveats named, deliberately left open** (not resolved this
   pass): (a) Duffy+2008's own `σ(log10 c)=0.15` scatter *width* is kept
   even though its *median* was just rejected as out-of-range — no
   `σ`-sensitivity sweep run; (b) the exclusion-fraction change
   (`5.65%→1.02%`) is not decomposed from the median-swap effect — some
   of the reported shift may be truncation-driven, not purely the choice
   of `c-M` relation.

## Result

| `z` | offset (Duffy) | offset (Correa III) | shift | jensen F0 (Duffy) | jensen F0 (Correa III) | shift |
|---|---|---|---|---|---|---|
| 0.07 | 0.9523 | 0.9934 | 4.3% | 1.0152 | 1.0045 | 1.1% |
| 0.25 | 0.8646 | 0.9690 | 12.1% | 1.0584 | 1.0223 | 3.4% |
| 1.00 | 0.5489 | 0.7487 | 36.4% | 1.2822 | 1.1464 | 10.6% |
| 2.00 | 0.2646 | 0.4378 | 65.5% | 1.7221 | 1.4167 | 17.7% |
| 2.33 | 0.2050 | 0.3589 | 75.1% | 1.9146 | 1.5348 | 19.8% |

`c_median`: `3.656` (Duffy, extrapolated) vs `4.711` (Correa III,
cluster-valid). Exclusion fraction: `5.65%` (Duffy) vs `1.02%`
(Correa III).

**MCID (pre-registered, `>20%` shift at `z=2.00` or `z=2.33`): MATERIAL**
— the offset shift alone (`65.5%`/`75.1%`) clears the bar comfortably;
the Jensen-only shift (`17.7%`/`19.8%`) sits just under/at it.

**The corrected headline number:** `FINDING_E17`'s own "`v82`'s mass law
diverges `~5×` from a real MAH model at `z=2.33`" shrinks to **`~1.8×`**
once the concentration-mass relation is not extrapolated beyond its own
stated range — smaller, but the divergence remains real, not resolved to
zero.

## What this does and does NOT establish

**Does establish:** `E17`'s reported magnitudes at `z≥1` are not robust
to the choice of concentration-mass relation between two real, published
alternatives — a genuine sensitivity, now quantified and corrected for
an arithmetic slip the first draft would have shipped uncaught.

**Does NOT establish:**
1. The FINAL, fully-resolved offset/Jensen magnitude — the two named-open
   caveats (scatter-width mismatch, truncation-fraction confound) are
   real, unresolved contributors to the remaining uncertainty.
2. Anything about whether `M0` should be read as "z=0 anchor mass" or
   "observed mass at `z_obs`" in v82's OWN intended physical construction
   — only that THIS comparison requires the former for internal
   consistency with the machinery already in use.
3. `NO_AUTHOR_ERROR` — a sensitivity check on this project's own
   reconstruction, not a claim about v82's or Correa's correctness.

## Pearl Registry update

`E17`'s existing offset-finding Pearl entry is updated in place: the
`~5×` figure is now known to be sensitive to the extrapolation choice,
corrected to `~1.8×` under the cluster-valid relation, with the two
caveats above named as the remaining open items.

## Next step, named not done

A `σ`-sensitivity sweep (Duffy's `0.15` vs plausible cluster-scale
alternatives) and a decomposition of the exclusion-fraction contribution
from the pure median-swap effect, before treating `~1.8×` as more than
order-of-magnitude-plausible.
