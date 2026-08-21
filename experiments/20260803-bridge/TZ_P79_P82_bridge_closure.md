# ТЗ — closing what can be closed, and naming what cannot

**Date:** 2026-08-21 · **Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Status:** specification. Steps P79–P82 execute against it.

---

## L0 gate (EstimandOps, mandatory before the tier)

| | |
|---|---|
| **Question type** | **Descriptive.** Every step below characterises a property of a model *we* constructed — its parameter space, its internal attributions, its observables. No causal claim about nature is made, and no comparison to data is performed. |
| **Entity** | our scalar completion of the local MULTING force law, in the `(V, M)` family |
| **Falsifiable predicate** | named per step, with a pre-registered threshold |
| **Measurable outcome** | named per step, against a *measured* floor, never an assumed one |

**What none of this will mean:** it will not mean MULTING is confirmed; it will
not mean our completion *is* MULTING; it will not license any comparison to
`H(z)`, `fσ8` or lensing, because `NO_BRIDGE_FITTING` remains in force and the
normalization gap is unclosed.

---

## The final goal, stated so it can fail

> **Bring the reconstruction to the point where exactly one thing stands between
> it and a frozen, falsifiable prediction — and name that thing precisely enough
> that it becomes a yes/no question rather than a research programme.**

Not "prove MULTING". Not "find another agreement". The deliverable is a
**closed-form list of what remains open, with each item either closed, or shown
to be closed-by-someone-else-only, with the reason.**

---

## The ten bridges, triaged by what *we* can actually do

| # | bridge | can we close it? | why |
|---|---|---|---|
| 1 | local `F_ij` → global `a(t)` | **No** | needs an N-body/coarse-graining derivation, not a completion. Out of scope for this arc; naming it is the contribution. |
| 2 | `β₁,β₂` from a mechanism | **No** | the coefficients belong to the *original* theory, and the only route we have — fitting to data — is forbidden by `NO_BRIDGE_FITTING`. |
| 3 | MULTING → *unique* action | **No, but boundable** | `P75` already proved the structural layer cannot discriminate; uniqueness cannot be proven from inside. |
| 4 | completion uniqueness | **DONE — `P78`** | **D-SEP:** the growth channel separates linear from exponential `M(φ)` by **26.7 % at k=1**, `5×10⁸×` the floor. The question is now empirical, not metaphysical. |
| 5 | normalization → physical units | **No** | genuinely blocked on input we do not have. This is the single hard external dependency and it must be said plainly. |
| 6 | background → *physically viable* cosmology | **Yes — P81** | scan `(ĝ,λ)` for trajectories with `a>0`, `ρ_phys>0`, `1−ĝφ̄` bounded away from 0, stable over decades. |
| 7 | background → correct perturbations and growth | **Yes — P82** | `f(a,k) = d ln δ/d ln a` is directly computable from what we already integrate. |
| 8 | internal `k` → `h/Mpc` | **No** | downstream of bridge 5. |
| 9 | growth → *causal* attribution | **Yes — P80** | `P77`'s ablation probe violates the constraints by the size of the signal. A **derivative at the on-shell point** does not. |
| 10 | model → frozen prediction → data | **No** | downstream of 5 and 8. |

**Four closable, six not — and of the six, five reduce to bridges 1, 2 and 5.**
That is the honest shape of the endgame.

---

## P79 — validate the window the P78 result actually lives in

**Why first.** `P78`'s D-SEP verdict rests almost entirely on `k=1`
(26.7 %; by `k=30` the separation is 0.00 %). And `k≲1` is exactly the window
`P77` flagged: largest `a₂`-spread, largest anchor sensitivity, and a blow-up at
`(ĝ=0.5, k=1)`. **The strongest result of the arc currently stands on its least
validated ground.** That has to be settled before anything is built on it.

| | |
|---|---|
| **Predicate** | the `ε_exp − ε_lin` separation at `k ≲ 3` survives every gate `P76/P77` built |
| **Gates** | `a₂`-convergence <2 %; anchor `A₁` sweep <5 %; `φ̄̇(1)` lever `×0.1…×2` (matter-dominated only) <10 %; rtol `10⁻⁸…10⁻¹²`; zero-crossing count on **both** runs |
| **Pre-registered** | **W-OK** all gates pass → D-SEP stands and the low-`k` window is usable · **W-FAIL** any gate fails → D-SEP is *unsupported*, and P78's verdict reverts to undecided |

**This step can destroy P78.** That is why it is first.

---

## P80 — constraint-preserving attribution (bridge 9)

**Why the current one fails.** `P77`'s probe deletes `+ĝρ_Aδφ` from the Euler
equation. That takes the system **off-shell** — `P73`'s first-class algebra
breaks, the `0i` residual reaches `6.8×10⁻²`, and the direct share moves
`6.6 % → 16.4 %` with the probe's start time.

**The fix, and it is not a patch.** Promote the coupling to two independent
parameters — `ĝ_bg` in the background equations, `ĝ_pert` in the perturbation
sector — and measure

```
direct  :=  ĝ · ∂ε/∂ĝ_pert   evaluated AT  ĝ_pert = ĝ_bg = ĝ
```

A **derivative at the on-shell point** never leaves the constraint surface,
unlike a finite deletion. This is thermodynamic integration's trick: integrate
`∂H/∂λ` along the coupling instead of subtracting two states.

| | |
|---|---|
| **Predicate** | the on-shell derivative reproduces the off-shell split's *sign and order*, with a systematic **smaller** than the direct term |
| **Control** | at `ĝ=0` the derivative must vanish identically |
| **Pre-registered** | **A-OK** systematic ≪ direct → the split becomes a measurement · **A-DEG** the two channels are not separable even on-shell → attribution is impossible in principle here, which is itself a result |

---

## P81 — is there a physically viable background at all? (bridge 6)

Consistency and existence are established (`P63`, `P64`). *Viability* is not.

| | |
|---|---|
| **Predicate** | ∃ a region of `(ĝ, λ)` where, over ≥8 decades: `a>0`, `ρ_phys>0`, `min(1−ĝφ̄) > 0.1`, and `H` monotone |
| **Known point** | `(1,1)` gives `min(1−ĝφ̄) = 0.87` (`P77` I4) — one point, not a region |
| **Pre-registered** | **V-REGION** a connected region exists → the completion has a viable corner and its boundary is the new constraint · **V-POINT** only isolated points → the completion is fine-tuned, and that must be said · **V-NONE** none survive → the completion is not viable and the arc ends |

---

## P82 — the growth rate itself (bridge 7)

`ε` is a *shift*. The observable the literature actually uses is the growth rate
`f(a,k) = d ln δ_m / d ln a`, whose product with `σ8` is what redshift-space
distortions measure.

| | |
|---|---|
| **Predicate** | `f(a,k)` is computable, converged, and reduces to the matter-domination value `f → 1` at `ĝ=0` |
| **Lock mass** | `f = 1` in matter domination — **textbook**, external to this project |
| **Pre-registered** | **F-OK** lock mass passes and `f` converges → we have the standard observable, in *our* units, ready for the day bridge 5 closes · **F-FAIL** → say so, and `ε` remains the only channel |

**What P82 will NOT do:** compare to any `fσ8` dataset. Producing `f` in internal
units is the deliverable; comparing it is bridge 10 and is blocked.

---

## Stop rule, named in advance

The `docs/145` audit (2026-08-17) recorded a plateau: no new falsifiable number
between `P22` and `P76`. `P76/P77/P78` broke it.

> **If P79 returns W-FAIL and P80 returns A-DEG, stop.** That combination means
> the one measurable discrimination we have is unsupported *and* its attribution
> is impossible in principle — and the correct action is to write the null
> result, not to start P83.

---

## Deliverable

A single document stating, for each of the ten bridges: **closed / closable-but-not-by-us / blocked-on-named-external-input**, with the evidence attached — so that the remaining question is answerable yes/no rather than open-ended.
