# FINDING P138 — horizon-crossing anchoring is not testable as designed
# for k>=2; a real design limitation, reported before proceeding further

**Date:** 2026-08-24
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `DESIGN-LIMITED, STOP AND REPORT` (sanity check only ran;
main G3-style test did not proceed for k≥2)
**Script:** `P138_horizon_relative_observable.py`

---

## 1. Why this file

Round-2 arbiter's H2 (design an IC-robust observable), entered after
`FINDING_P135` (pole-at-anchor, refuted) and `FINDING_P136`
(early-transient amplitude, refuted). A third candidate mechanism,
untested in either prior file: `P79`'s own anchors `(a1, a2)` are FIXED
scale-factor values, the same for every `k`. Different `k` modes cross
the horizon (`k = a·H`) at different times — a mode that crossed
recently has had fewer e-folds to relax toward the universal subhorizon
growing-mode attractor by a common fixed anchor than one that crossed
long ago. This file designed a horizon-crossing-relative anchoring
scheme (`a1(k) := a_hc(k)·e^{N1}`, `a2(k) := a_hc(k)·e^{N2}`) to test
whether `P79`'s own G3 lever-robustness gate would pass under this
re-anchoring, at the same `k` values where the fixed-anchor version
failed.

## 2. What the sanity check found, before the main test ran

`t_hc(k)` — the root of `k = a(t)·H(t)` — was sought in `t ∈ [1, T_END]`
for every tested `k`. Result:

| k | horizon crossing found in [1, T_END]? | t_hc | k / (aH at t=1) |
|---|---|---|---|
| 1 | **Yes** | `t≈5.14` | `0.54` (superhorizon at t=1) |
| 2 | **No** | — | `1.09` (already subhorizon at t=1) |
| 3 | **No** | — | `1.63` (already subhorizon at t=1) |
| 10 | **No** | — | `5.43` (deep subhorizon at t=1) |

`a·H` decreases monotonically from `1.84` at `t=1` down to `3.8×10⁻³` at
`t=10⁸` — a clean, single-crossing trajectory. But since `a·H(1) ≈ 1.84`
is already below `k=2,3,10`, those three modes are **already subhorizon
at the very start of the numerical domain** — their true crossing
happened at some `t<1`, outside where this system is integrated.

## 3. Consequence — the design does not test what it set out to test

Only `k=1` has a horizon-crossing event *inside* the domain this
campaign's own trajectories are actually solved over. For `k∈{2,3,10}`,
"e-folds since crossing, measured from t=1" is not a well-posed quantity
the way this file defined it — extrapolating `a·H(t)` backward past
`t=1` to estimate an out-of-domain crossing time was not attempted here
(a materially different, riskier computation: extrapolation outside a
solved ODE domain, not a re-anchoring of an already-solved trajectory).
The main G3-style robustness test was **not run to completion** — only
the sanity check that would have gated it.

## 4. Verdict

**`DESIGN-LIMITED, STOP AND REPORT`, not a mechanism verdict either way.**
This is not `HORIZON-RELATIVE-CONFIRMED` or `-REFUTED` — the pre-registered
test simply could not run as designed for 3 of the 4 tested `k` values.
Recorded honestly rather than silently substituting a different,
untested design (e.g., backward extrapolation) and reporting a result
under the original framing.

**A real, usable finding despite the stop:** the `k/aH(1)` ratio itself
gives an ALREADY-AVAILABLE ranking that roughly tracks `P79`'s own
instability ordering — `k=1` (never crossed within the initial state,
worst instability, `G3` `5.2×` spread) → `k=2` (just barely crossed,
`4.4×` spread) → `k=3` (crossed a bit before start, qualitatively
different sign-flip) → `k=10` (deep subhorizon at start, previously
"clean," though `FINDING_P135`'s own Part B found it *also* sign-flips
in this exact separation test, which `P79` itself never ran there).
Suggestive, not tested as a mechanism — named for a future attempt, not
claimed here.

## 5. What this does NOT establish

1. **That horizon-crossing timing is or is not the mechanism** — the
   decisive test did not run.
2. **A replacement observable.** Not attempted — this file stopped at
   its own gating sanity check.
3. **That backward extrapolation of `a·H(t)` before `t=1` would work or
   would be trustworthy if attempted** — a genuinely different, riskier
   computation, not tried here.
4. **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in
   force.
5. **Anything about MULTING itself** (Gate 1). Both completions are
   ours.

## 6. Reproduction

```bash
python experiments/20260803-bridge/P138_horizon_relative_observable.py
```
(Runs the sanity check, reports "NO CROSSING" for `k≥2`, then attempts
the G3-style test with those `k` values marked incomplete rather than
silently omitted — see the script's own output.)
