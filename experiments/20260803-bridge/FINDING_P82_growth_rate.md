# FINDING P82 — **F-OK.** The standard growth rate exists in our units

**Status:** built, run, verdict **F-OK** against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P82_growth_rate.py`

> Two cross-checks fell out of this file that were **not designed in**. Both are
> recorded below with their own verification, because an unplanned agreement is
> worth more than a planned one — and is also the easier kind to over-read.

---

## Why `f` and not more `ε`

`FINDING_P76`'s `ε` is a **shift** — a ratio of one run's growth to another's.
It is internal by construction: it needs a reference run, and no observation
gives you one. The quantity the literature measures is the growth rate

```
f(a,k) = d ln δ_m / d ln a
```

whose product with `σ8` is what redshift-space distortions constrain. `f` needs
no reference run. It is the first quantity in this arc with the **shape** of an
observable — though nothing here is compared to data.

---

## The lock mass is **external**, which is the whole point

In matter domination the growing mode is `δ ∝ a`, so `f = 1`. Textbook, owing
nothing to this project — unlike `FINDING_P74`'s lock mass, whose target was
internal and through which a deliberately fabricated term sailed unnoticed. P76
already used `δ ∝ a`; P82 uses its **logarithmic derivative**, which is strictly
sharper: a growth off by a constant factor still passes `δ ∝ a` by eye and fails
`f = 1` immediately.

### The trap this file was built to avoid

Our background is **not** pure matter domination — the scalar carries kinetic and
(at `λ ≠ 0`) potential energy, both of which feed `H`. If `f` came out below 1
because of that, it would be **correct physics** and would look identical to a
broken pipeline. So `Ω_φ` is printed beside `f` at every point, and the lock mass
is asserted only where `Ω_φ` is demonstrably small. `FINDING_P78`'s A3 failed
falsely for exactly this species of reason.

| `t` | `a` | `Ω_φ` | `f` | `f−1` |
|---|---|---|---|---|
| `1.0e+04` | `1235.62` | `3.173e-04` | `0.999794138` | `−2.059e-04` |
| `1.0e+05` | `5734.03` | `6.384e-05` | `0.999957839` | `−4.216e-05` |
| `1.0e+06` | `26613.7` | `1.341e-05` | `0.999991095` | `−8.905e-06` |
| `1.0e+07` | `123529` | `2.877e-06` | `0.999998087` | `−1.913e-06` |
| `8.0e+07` | `494114` | `7.093e-07` | `0.999999527` | `−4.732e-07` |

All five points have `Ω_φ < 1e-3`; worst `|f−1| = 2.06e-04`. **Lock mass passes.**

## Negative control — the lock mass must be able to fail

A gate that passes on everything is not a gate (the lesson of P76's hardcoded
column and P77's non-discriminating pole test). The same pipeline is run on the
**raw** `Δ_m` instead of the contrast. Since `Δ_m = δ·ρ_phys ∝ δ·a⁻³`, it must
land near `f − 3`:

| `t` | `f` (contrast) | `f` (raw `Δ_m`) | difference |
|---|---|---|---|
| `1.0e+04` | `0.999794138` | `−2.000205862` | `+3.000000` |
| `1.0e+05` | `0.999957839` | `−2.000042161` | `+3.000000` |
| `1.0e+06` | `0.999991095` | `−2.000008905` | `+3.000000` |
| `1.0e+07` | `0.999998087` | `−2.000001913` | `+3.000000` |
| `8.0e+07` | `0.999999527` | `−2.000000473` | `+3.000000` |

Exactly `3.000000` at every point. **The gate distinguishes the two quantities**,
so its PASS above carries information.

## Convergence in both knobs that could fake a value

**C1 — the differencing step.** Changes fall `1.36e-08 → 1.30e-09 → 1.49e-10 →
1.62e-11` as `dlnt` goes `1e-2 → 1e-4`. **Converged.**

**C2 — the solver tolerance.** Across `rtol = 1e-8 … 1e-12`, worst shift
`4.99e-13`. `f` does **not** track the solver.

---

## The deliverable — `f(a,k)` with the coupling on

Internal units. Compared to nothing; comparison is bridge 10 and is blocked.
`Δf := f(ĝ=1) − f(ĝ=0)` at late times:

| `k` | `f(ĝ=1)` | `f(ĝ=0)` | `Δf` |
|---|---|---|---|
| 3 | `1.040021849` | `0.999999527` | `+0.04002232` |
| 10 | `1.045794366` | `0.999999527` | `+0.04579484` |
| 30 | `1.046739050` | `0.999999527` | `+0.04673952` |

---

## Cross-check 1 — the growth index, and it was not designed in

Part A's deviation is not merely *small*; it **tracks** `Ω_φ`. Reading
`(1−f)/Ω_φ` down the table: `0.649, 0.661, 0.664, 0.665, 0.667` — converging on
**2/3**.

The textbook growth index for a constant-`w` component is `γ = 3(1−w)/(5−6w)`,
which gives exactly `2/3` at `w = 1/3`; and an oscillating quartic potential is
known to redshift like radiation.

**That chain came out of memory, which is not evidence.** So rather than trusting
the formula, the scalar's effective `w` was measured **directly** from the run —
`w = ∫p_φ / ∫ρ_φ` over the oscillations, averaging the densities rather than the
pointwise ratio (which would over-weight the turning points where `ρ_φ` is tiny).

| window in `t` | measured `⟨w_φ⟩` | oscillations in window |
|---|---|---|
| `1e4 … 1e5` | `0.417079` | 8 |
| `1e5 … 1e6` | `0.369645` | 18 |
| `1e6 … 1e7` | `0.345980` | 38 |
| `1e7 … 8e7` | `0.343502` | 71 |

`w` descends toward `1/3` as the oscillation count grows — 8 cycles is too few
for the average to have settled, 71 gets within 3 %.

Feeding the **measured** `w = 0.345928` into `γ = 3(1−w)/(5−6w)` gives
`γ = 0.670973`. Measured **directly** as `(1−f)/Ω_φ`, the last point gives
`γ = 0.667059`. The two routes differ by `0.0039` (**0.58 %**), and the direct
measurement sits `0.06 %` from `2/3`.

**How independent is this?** Genuinely — the target (`γ = 3(1−w)/(5−6w)`, and
`w = 1/3` for an oscillating quartic) is **external textbook**, and `w` was
measured rather than assumed. This is a real lock mass on the background's
physics, not an internal consistency loop.

**What it is not:** exact. `w` is still drifting toward `1/3` at the end of the
span, so the agreement is **asymptotic**, and the residual `0.58 %` is consistent
with that drift rather than with anything having been demonstrated to converge.
Extending the run would sharpen it; this file does not.

## Cross-check 2 — `Δf` versus `ε`, and what it says about anchoring

Algebraically

```
Δf = f_coupled − f_uncoupled = d ln(δ_c/δ_u)/d ln a = d ln G/d ln a = ε
```

so P82 recomputes `FINDING_P76`'s `ε` by a route with **no anchor and no
reference ratio**. `FINDING_P77` separately measured that the *anchored* `ε` is
biased **low by ~0.2 %** against an anchor-free local slope, quoting
`0.045789597` at `k=10` against the anchored `0.045688`.

| `k` | `Δf` (P82, late) | P77 **anchored** `ε` | ratio |
|---|---|---|---|
| 3 | `0.040022322` | `0.039965` | `1.00143` |
| 10 | `0.045794840` | `0.045688` | `1.00234` |
| 30 | `0.046739523` | `0.046633` | `1.00228` |

`Δf` exceeds the anchored `ε` by `0.14–0.23 %` — matching the anchoring bias P77
measured by a different method. Against P77's own **anchor-free** value at
`k=10`:

| | |
|---|---|
| P77 anchor-free local slope | `0.045789597` |
| P82 `Δf` | `0.045794840` |
| relative difference | **`1.15e-04`** (0.011 %) |

**How independent is this?** *Less than it looks, and the distinction matters.*
P82 calls `p76.run` and `p76.contrast` — the **same** integrator and the **same**
observable definition P77 used. So this is **not** an independent confirmation of
the physics. What it independently confirms is the **extraction algebra**
(`Δf ≡ d ln G/d ln a ≡ ε`) and the **existence and size of P77's anchoring
bias**, from a third file that computes it a different way. On the Independent
Verification Strength Ladder that is roughly "same model, isolated context" —
**weak-to-medium**, and it is recorded at that strength, not higher.

---

## What is NOT established

- **Anything observational.** `f` is in internal units and compared to no
  dataset. `NO_BRIDGE_FITTING` in force; bridge 10 is blocked.
- **That `f` is the *right* observable for this completion** — only that it is
  computable and well-behaved in it.
- **Anything about MULTING itself** (Gate 1). The completion is ours.
- **Perelman condition 5** (external reconstruction) — still not met.
