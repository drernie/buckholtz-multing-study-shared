# FINDING E15 — a first, partial, honestly-caveated number for a gap
# v82 names about itself and explicitly declines to quantify: the
# force-law-level correction from real, measured scatter is real
# (`+13%`/`+62%`), consistently pushes the total force in one direction
# across the real data range, but does NOT license the re-fit claim the
# first draft made

**Date:** 2026-09-06
**Claim:** `CLAIM_E15_jensen_gap_real_scatter.md` (pre-registered)
**Script:** `E15_jensen_gap_real_scatter.py`
**Continues:** `FINDING_E13` (measured `σ_{M_gas|T}=0.49`) and this
project's own `FINDING_P157`/`P158` (Jensen's-inequality machinery for
this exact linear-vs-quadratic force-law structure, previously run only
with an admittedly illustrative scatter). Option 1 of the six
continuation options, first of the set.

## The question, in v82's own words

`[VERIFIED-BASH]` v82.md:1060-1063: *"Every quantity in Sec. II.D is a
single, representative value at each redshift, not a scattered
population of node properties. Because the force law is markedly
nonlinear in these quantities, evaluating it at a representative value
is not generally the same as averaging it over the distribution; **we
have not attempted to quantify this difference.**"*

## Controls — pass

- `σ→0` returns correction factor exactly `1.0` for both `F1`, `F2`.
- Monte Carlo (`N=5×10⁶`) matches the closed-form log-normal moments
  (`E[X]=exp(σ²/2)`, `E[X²]=exp(2σ²)`) to `<0.5%`.

## Result — corrected in place after a Step 8a skeptic pass, per this
## project's no-silent-correction discipline

**Force-term-level correction factors (from `E13`'s real `σ=0.49`):**

```
F1 (dipole,      linear in k):    +12.8%
F2 (quadrupole, quadratic in k):  +61.6%
differential (F2 vs F1):          +43.4%   <- MCID fires (threshold 10%)
```

**Three real corrections from the skeptic, all incorporated, none
dropped silently:**

1. **`σ=0.49` is one layer, not the total scatter in `k`.** `k` also
   depends on temperature `T` via the "self-similar" mass-temperature
   step, whose own scatter is `[VERIFIED — still UNQUANTIFIED,
   FINDING_E9]`. If independent, scatters add in quadrature — **the
   true correction is plausibly larger than reported here, not
   smaller.** Partial cancellation (if `T` and `M_gas` are
   anti-correlated in the shared calibration sample) is possible but
   not checked. The `+13%`/`+62%` numbers are a **lower-bound-flavored
   partial estimate**, not a total.
2. **The "population-averaging" frame itself is genuinely ambiguous,
   and this file does not resolve it.** v82's own sentence is
   compatible with two readings: **(a)** the node genuinely represents
   a population average, in which case this correction is real and
   v82's point-evaluation is biased; **(b)** the node is a canonical
   fitted value, and the relevant uncertainty is the *small* calibration
   error on the fit itself (`B=2.24±0.03`, not `σ=0.49`'s full
   population scatter). This file computes under reading (a) without
   arguing for it over (b) — **stated explicitly as the calculation's
   central, unresolved assumption.**
3. **The force-term corrections are NOT a computed re-fit of `β₁,β₂`,
   and the first draft's "would imply a `43%` shift in `β₂/β₁`" language
   over-reached.** `H(z)` is a nonlinear function of `F_total`, and
   this project's own `E8`/`E11` already found a real `(β₁,β₂)`
   near-degeneracy — an actual re-fit would move along that degeneracy
   direction, not rescale each force term independently. **What
   survives is the force-law-level statement only.**

## The one genuinely resolved sub-question — computed, not assumed

The skeptic separately flagged a real ambiguity the first draft missed
entirely: `F_total = F0 − F1 + F2 − F_accretion` — `F1` enters with a
**minus** sign, `F2` with a **plus** sign, so their respective `+13%`
and `+62%` corrections pull `F_total` in **opposite** directions. Net
direction depends on `|F2|/|F1|`, with a crossover at `≈0.207`.

**Computed directly with TJB's own real fitted `(β₁,β₂)` (Table II,
`unconstrained_spotlighted`) and his own `forces()` function, at the
real data redshifts** `[VERIFIED-CODE]`:

| `z` | `\|F2\|/\|F1\|` | net push |
|---|---|---|
| `0.07` | `1.003` | UP |
| `0.25` | `0.952` | UP |
| `1.00` | `0.879` | UP |
| `2.00` | `0.878` | UP |
| `2.33` | `0.883` | UP |

**Above the `0.207` crossover at every single real data point — the
net direction is not ambiguous in practice**, whatever the answer to
the two open framing questions above turns out to be.

## What this does and does NOT establish

**Does establish:** the force-law-level Jensen's gap from `E13`'s real
scatter is genuine, materially sized (`~13%`/`~62%`), consistently
one-directional across the real data range, and directly answers the
*narrow* version of TJB's own named question — using a real, sourced
number rather than the illustrative one `P158` had to use.

**Does NOT establish, honestly, per the skeptic's three corrections:**

1. The *total* scatter in `k(z)` — only the `M_gas`-`T` layer's
   contribution.
2. Which reading of "representative value" (population-average vs.
   canonical-fit) v82's own construction actually intends — the
   calculation's central open assumption.
3. Any actual shift in the fitted `β₁,β₂` values — that requires a real
   re-fit through the nonlinear `H(z)` pipeline, respecting the known
   degeneracy, and was not attempted here.
4. Does not draft or send anything to TJB. `NO_AUTHOR_ERROR` —
   answering a question v82 poses about itself, not a claim about v82's
   correctness.

## Next step, named not done

A real re-fit — recompute `β₁,β₂` (or at minimum the small-eigenvalue
direction from `P176`'s own Hessian machinery) using population-
averaged `F1, F2` instead of point-evaluated ones, the way `E8`
propagated the CC covariance — is the only way to answer the skeptic's
`A4` decisively.
