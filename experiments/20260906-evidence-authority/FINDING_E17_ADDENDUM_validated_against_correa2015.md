# FINDING E17 ADDENDUM — validating against Correa+2015's own values
# closes one gap cleanly and opens a more serious one

**Date:** 2026-09-06
**Continues:** `FINDING_E17_mass_scatter_for_F0_Faccretion.md`. Closes the
one open verification gap the 2nd Step 8a skeptic pass named: no control
had cross-checked `E17`'s constants/formulas against Correa+2015's own
published values (`arXiv:1501.04382`), fetched directly from the LaTeX
source this session (not from memory).

## L0 (EstimandOps)

**Descriptive** — does `E17`'s transcription of Correa+2015's own
constants and formulas, and its choice of input mass, match what the
source paper itself states? Not a re-derivation, a direct check.

## Result 1 — `A_COSMO_PLANCK=798.0`: `[VERIFIED-arXiv]`, exact match

Correa+2015's own Section 3.6.1 (LaTeX source, not a table extraction):
*"We find `A_WMAP1=787±52.25`, `A_WMAP3=850±39.60`, `A_WMAP5=903±48.63`,
`A_WMAP9=820±51.03` and `A_Planck=798±43.73`."* `E17`'s
`A_COSMO_PLANCK=798.0` matches exactly.

## Result 2 — cosmology (`Ωm`, `ΩΛ`): a small, confirmed-negligible mismatch

`E17` used this project's own `P176` cosmology (`Ωm=0.315, ΩΛ=0.685` —
TJB's own v82 assumption), not Correa's own simulated Planck cosmology
(their Table 2: `DMONLY-Planck1: Ωm=0.317, ΩΛ=0.683`). Checked directly:
recomputing `z_{-2}` at `E17`'s own `c_median` with Correa's exact values
instead shifts `z_{-2}` by `0.37%` — negligible, does not change any
reported conclusion.

## Result 3 — a real, material, previously-unflagged gap: `M0` is outside
## the model's own stated validity range

`[VERIFIED-arXiv]`, Correa+2015's own text, twice: *"the concentration-mass
relation adopted... Duffy et al. (2008) relation, which is calibrated in
the mass range `10^10-10^14 M_☉`"*; and, in their own step-by-step guide
(the same equations `E17` uses): *"valid over the halo mass range for
which the concentration-mass and the `z_{-2}-M_0` relations, obtained
from simulations, are valid (e.g. `10^10-10^14 M_☉` for Duffy et al.
2008)."*

**`E17`'s own `M0 = 6.0×10^14 M_☉` (this project's own v82 pivot mass) is
`6×` above the upper edge of this stated range.** Neither the original
claim, nor either of the two prior skeptic passes, checked this. Correa's
own paper names the consequence directly, comparing their semi-analytic
model against an independent analytic one (their Fig. 10 discussion):
*"the analytic model predicts larger masses at high redshift for halos
with final masses `>10^14 M_☉`... a factor of 9 difference at `z=5`
between the models for a `10^15 M_☉` halo."* The divergence is
**concentrated at high `z`** for exactly this mass range — the same
regime where `E17`'s own Jensen correction was found `MATERIAL`
(`z=1.00, 2.00, 2.33`).

## What this means for `E17`'s own numbers

**Does not overturn** `E17`'s central results — the algebra, the
`offset`/`jensen` decomposition, and the direction of both effects stand.
**Does add a real, disclosed caveat that was missing:** the Jensen
correction and the offset finding, both reported "MATERIAL at `z≥1`," are
now known to sit in a mass/redshift regime where Correa+2015's own model
comparison shows growing disagreement with an independent construction —
so the specific *magnitudes* at `z=2.00` and `z=2.33` carry more
uncertainty than the Monte Carlo convergence check alone suggested. The
`z=0.07`/`0.25` points are less affected (closer to `z=0`, where models
agree well regardless of mass).

## What this does and does NOT establish

**Does establish:** `A_cosmo` is exactly right; the cosmology choice is
immaterial; the mass-range extrapolation is real and was not previously
checked.

**Does NOT establish:** the *size* of the resulting extra uncertainty —
Correa's own comparison is against their own EPS-based analytic model,
not against real cluster data, and the factor-of-9 example is at `z=5`,
outside `E17`'s own `z≤2.33` range. Quantifying the actual impact at
`E17`'s specific `(M0,z)` points is a further, not-attempted step.

## Pearl Registry update

The existing `E17` offset-finding Pearl entry
(`pearl_registry/INDEX.md`) is updated in place: `A_cosmo` validation
`CONFIRMED`; the open item is now specifically the mass-range
extrapolation, not a generic "not yet validated" note.

## Next step, named not done

Check whether a concentration-mass relation calibrated to cluster-scale
halos (`M0≳10^14 M_☉` — e.g. a cluster-specific extension of Duffy+2008,
or a more recent cluster-mass MAH study) gives a materially different
`z_{-2}`/`α`/`β` at `E17`'s own `M0`, before treating the high-`z` Jensen
correction magnitude as more than order-of-magnitude-plausible.
