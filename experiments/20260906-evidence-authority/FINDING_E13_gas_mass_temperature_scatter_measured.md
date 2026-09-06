# FINDING E13 — one of `E9`'s six `UNQUANTIFIED` dependencies measured:
# the gas-mass/thermal-energy input carries a real `~49-63%` scatter
# from v82's own cited source, and it feeds directly into the
# dipole/quadrupole force terms — not a peripheral quantity

**Date:** 2026-09-06
**Continues:** `FINDING_E9`, which found 6 of v82's 10 inputs carry a
declared-but-unmeasured dependency. Executes option B ("measure one of
the six"), per the user's own stated order ("D → B").

## Which dependency, and why this one

`E9` flagged the same dependency (`X-ray mass-temperature scaling-
relation calibration`) on three steps: gas mass, ICM thermal energy, and
temperature. Chosen because — unlike the other `UNQUANTIFIED` entries —
this one has a name, a specific citation, and a specific equation in
v82's own text, making it directly measurable from a source v82 already
uses rather than requiring a new literature search.

## v82's own construction (Eq. 13, `[VERIFIED-BASH]` v82.md:427-442)

```
M_gas,X(z) = M_gas,piv · (T_X(z)/T_piv)^B · (E(z)/E(z_piv))^C
```

with `T_piv=2.27 keV`, `M_gas,piv=2.28×10¹³ M_☉`, `z_piv=0.25`,
**`B=2.24±0.03`, `C=-1.00⁺⁰·²⁹₋₀.₃₀`**, cited to reference `[23]` — "a
fitted `M_gas`-`T` relation from the largest cluster X-ray sample to
date (3061 clusters, `0.05<z<1.07`)."

## The source, checked directly, not from v82's paraphrase

`[VERIFIED-arXiv:2511.14356]` Ramos-Ceja, Fiorino, Bulbul, Ghirardini,
Clerc et al. (2025), *"The SRG/eROSITA all-sky survey: X-ray scaling
relations of galaxy groups and clusters."* Downloaded and read directly
this session (not from abstract alone). §4.4, verbatim:

> *"The resulting best-fit parameters for the `M_gas`-`T` relation are
> `B=2.24⁺⁰·⁰³₋₀.₀₃`... `C=-1.00⁺⁰·²⁹₋₀.₃₀`... and
> `σ_{M_gas|T}=0.49⁺⁰·⁰²₋₀.₀₂` for the intrinsic scatter."*

**v82's `B` and `C` match this source to 3 significant figures — copied
correctly.** `v82` never quotes `σ_{M_gas|T}`. `[VERIFIED-BASH]`: zero
occurrences of "scatter" in this sense anywhere in v82's text.

## Size of the measured dependency

The paper's own fitting form is a log-normal scatter around a power
law (§3.1, `Y/Y_piv = A(X/X_piv)^B(E(z)/E(z_piv))^C`, `ln`-normal
residual with std `σ_{Y|X}`). `σ_{M_gas|T}=0.49` in natural-log terms
corresponds to a **`1σ` multiplicative range of `[e⁻⁰·⁴⁹, e⁺⁰·⁴⁹] =
[0.61, 1.63]`** — i.e., gas mass at fixed temperature varies by
`-39%/+63%` at `1σ`. This is consistent in scale with the same paper's
own framing elsewhere (§5.8: for the similarly-sized `σ_{Lx|T}=0.57`,
"the scatter can be as large as `50-70%` at fixed `T`").

**This is a real, larger-than-`E5`'s finding.** `E5`'s cosmic-
chronometer SPS systematic was `~9%` mean. This gas-mass scatter is
`4-7×` larger in fractional terms.

## A second, real finding inside the source itself: unresolved
## disagreement about the SIZE of this scatter

Same section, immediately following: *"`Zhang et al. (2008)`,
`Croston et al. (2008)` and `Arnaud et al. (2007)` report LOWER values
for the intrinsic scatter of the `σ_{M_gas|T}` relation, but these
measurements are presented without error bars and therefore a
statistical comparison with our findings cannot be made."* **v82's own
cited source explicitly cannot compare its own scatter estimate against
three earlier papers, because they omitted uncertainties on their own
scatter estimates.** This is a second-order provenance gap — not just
"is the scatter propagated," but "is even the SIZE of the scatter
itself settled in the literature v82 draws from."

## Why this is not peripheral — structural check, not just an
## unpropagated error bar

`[VERIFIED-BASH]` v82.md:332: *"force and its multipole corrections,
thermal energy sets the dipole and quadrupole terms"* — `k_X(z)`
(Eq. 14, built directly from `M_gas,X(z)`) is not a downstream or
cross-check quantity. **It directly sets the `β₁`/`β₂` terms** — the
same two parameters `E8`/`E11` already found carry a `4-7.6×`
understated degeneracy from a *different* unpropagated systematic (the
cosmic-chronometer covariance). This gas-mass scatter is a second,
independent, larger, and currently completely unexamined contributor
to the same `(β₁,β₂)` uncertainty budget.

## What this does NOT establish

1. **Does not propagate this scatter through the fit.** Sizing it
   (turning `UNQUANTIFIED` into a number) was this step's scope, per
   `E9`'s own framing; propagating it through `β₁`/`β₂` the way `E8`
   propagated the CC covariance is the natural next step, not done
   here.
2. Does not resolve the Zhang/Croston/Arnaud-vs-Ramos-Ceja tension on
   the scatter's own size — flagged, not adjudicated.
3. Does not show any v82 conclusion is wrong — the central values
   (`B`, `C`) are copied correctly; only the scatter around them is
   unused.
4. `NO_AUTHOR_ERROR` — the scatter value is the cited source's own
   published number, read directly from its full text this session.
