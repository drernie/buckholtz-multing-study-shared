# FINDING P83 — **V2 IC-CONDITIONED**, and **V1** on matter-dominated starts

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P83_ic_robustness_of_boundary.py`

> This step found **three** errors in its own measuring apparatus and none in the
> physics. One of them pointed toward **confirmation**, which is the direction
> that does not announce itself, and it is written up first.

---

## The question

`FINDING_P79` destroyed `FINDING_P78`'s D-SEP by showing the separation moved by
a factor ~5 under the `φ̄̇(1)` lever — an initial-condition artifact wearing the
costume of a physical result. `FINDING_P81` then reported a connected viable
region **without ever asking the same question of it.** This cashes P81's own
registered prediction.

**Observable: the boundary FUNCTION, not surviving-point counts.**
`R_boundary := |X_crit(lever) − X_crit(1)| / X_crit(1)`.
Lever: `φ̄̇(1) × {0.1, 0.25, 0.5, 1, 2, 4}`. `×10` excluded by construction —
`FINDING_P77` had to retract a conclusion after finding it puts 84.85 % of the
energy budget in the scalar, i.e. a different cosmology.

---

## Error 1 — the bisection failed toward **confirmation**

The first locator named its endpoints `lo`/`hi` — **semantic** labels for
not-viable/viable — then tested convergence **numerically** as `hi − lo ≤ tol`.
On edge E2 the not-viable end sits at *larger* `ĝ`, so it was called as
`(lo=3.0, hi=2.0)`; `hi − lo` was negative at the first comparison and the loop
exited after **one iteration**, returning the midpoint of the original bracket.

Every lever setting then returned the same `2.724745`, and:

```
max R_boundary = 0.0000   ->  V1 IC-ROBUST
```

the single most favourable of the four pre-registered outcomes.

**What caught it:** the `iters` column. A bisection that converges in one step is
not a measurement by construction.

**Two fixes, not one.** (a) The interval test is now on `abs()` and scaled by the
midpoint, so endpoint *order* cannot matter. (b) A **post-condition**: the
returned point must still straddle a flip, and convergence in under 3 iterations
is rejected. A bisection has no built-in failure signal — it always returns a
number inside the bracket — which is exactly why `scipy.optimize.brentq` enforces
opposite signs as a **precondition that raises**, not as docstring advice. My
locator was predicate-based rather than sign-based and I put the check in prose.

## Error 2 — a bracket endpoint my own file had already flagged

E1 was first bisected from `ĝ = 5.0`. `FINDING_P81`'s own table lists `(5, 0)` as
**UNRESOLVED** — the integrator cannot carry it. The locator correctly refused,
and E1 returned nothing for half the lever. The data saying so was in a file I
wrote the day before. Endpoint moved to `ĝ = 1.0`, which P81 measured at
`min(1−ĝφ̄) = −7.9e+04`.

## Error 3 — reading a classification flip as a moving wall

Part B shows `λ=0` at `ĝ=0.75` flipping from **viable** (`×0.1…×0.5`) to **not
viable** (`×1…×4`), with the flip *inside* the matter-dominated range. Read
alone, that is a strong IC-dependence signal — and it is **wrong**. The boundary
function says `ĝ_crit(λ=0)` moves from `0.7767` to `0.7590` over a five-fold
lever change: **2.3 %**. P81's grid point at `ĝ = 0.75` simply sits within a few
percent of `ĝ_crit ≈ 0.76`, so a tiny boundary shift flips that one cell.

**This is precisely the argument for measuring the boundary function rather than
points.** Stopping at Part B would have produced the opposite conclusion.

---

## Controls

| | check | result |
|---|---|---|
| **C0** | the predicate must be P81's, unchanged | `0.871740 / 0.864306 / 0.484961` against P81's `0.8717 / 0.8643 / 0.4850` |
| **C1** | explicit `phidot0` at the default = the default | **bitwise** identical |
| **C3** | the locator must refuse to invent a boundary | at `ĝ=0` returns `None`: *"bracket is not what it claims"* |

`viability()` was **extended** with `phidot0` in P81 rather than reimplemented
here. Two copies of a predicate drift, and P83 would then be measuring the
movement of a boundary P81 never had.

### Regime check — run **before** the verdict, not after

`φ̄(1) = 0`, so the scalar's entire initial energy is kinetic and scales as
`φ̄̇²`:

| lever | `φ̄̇(1)` | kinetic fraction | regime |
|---|---|---|---|
| ×0.1 | `7.92e-03` | 0.0560 % | matter-dominated |
| ×0.25 | `1.98e-02` | 0.3489 % | matter-dominated |
| ×0.5 | `3.96e-02` | 1.3812 % | matter-dominated |
| ×1 | `7.92e-02` | 5.3052 % | matter-dominated |
| ×2 | `1.58e-01` | **18.3070 %** | matter-dominated |
| ×4 | `3.17e-01` | 47.2680 % | **SCALAR-SIGNIFICANT** |

`×2` reads `18.3070 %` against the `18.31 %` `FINDING_P77` reported
independently — an unplanned confirmation that this computes the same quantity
P77 did. `×4` lands at 47 %, matching the ~47 % predicted from P77's numbers
before the code was written.

---

## Result

### E1 — `λ_crit = 0` **exactly**, so E1 is re-posed

Every `λ > 0` down to `1e-12` is viable at `ĝ=0.75`; `min(1−ĝφ̄)` climbs smoothly
`0.4712 → 0.8051` across eight decades, then drops **discontinuously** to
`0.0285` at `λ=0`. The transition sits **at the truncation surface**, not at a
finite critical coupling, so `R_boundary` in `λ` is `0/0` and is not reported.
The observable that does exist is `ĝ_crit(λ=0)`.

| lever | `ĝ_crit(λ=0)` | `R_boundary` | `ĝ_crit(λ=0.1)` | `R_boundary` |
|---|---|---|---|---|
| ×0.1 | 0.776737 | 0.0522 | 2.974716 | 0.0810 |
| ×0.25 | 0.769998 | 0.0431 | 2.934646 | 0.0665 |
| ×0.5 | 0.758986 | 0.0281 | 2.870290 | 0.0431 |
| **×1** | **0.738209** | — | **2.751767** | — |
| ×2 | 0.701444 | 0.0498 | 2.552339 | 0.0725 |
| ×4 | 0.645628 | 0.1254 | 2.273207 | 0.1739 |

Both edges **strictly monotone decreasing** in the lever — more initial scalar
velocity drives `φ̄` higher, `1−ĝφ̄` dips lower, and failure arrives at smaller
coupling. A coherent mechanism, not scatter.

### The verdict quantity, read twice

| | value |
|---|---|
| `max R_boundary`, **full** lever | **0.1739** |
| `max R_boundary`, **matter-dominated only** | **0.0810** |
| for scale — the movement that **killed** `FINDING_P78` | `R ≈ 4.0` |

### Topology — no bifurcation

Component count is **1** at every lever tested (`×0.1`, `×1`, `×4`). The region
shrinks `22 → 21 → 19` of 25 reduced-grid points; class flips versus `×1` are
`{×0.1: 1, ×4: 2}`. **V4 is not seen.**

### Free convergence datum

Two *independent processes* bisected E1 at three lever settings. Relative
differences `6.4e-06`, `5.5e-05`, `2.4e-05` — all inside the `1e-4` tolerance
asked for. The locator is reproducible across runs.

---

## Verdict

**V2 IC-CONDITIONED** on the full lever (`0.10 ≤ 0.1739 < 1.0`): the region
survives, but its boundary moves with the initial condition, so **every quotation
of the viable corner must carry the IC it was measured at**.

**V1 IC-ROBUST on matter-dominated starts** (`0.0810 < 0.10`). The IC dependence
is concentrated in `×4` — a start with 47 % of the energy in the scalar, i.e. a
regime change rather than a perturbation of the initial data.

**P81 is strengthened, not weakened.** Its boundary moves by ~8 % across a
40-fold lever range within matter domination, against the factor ~5 that
destroyed P78's separation — **a difference of roughly 50× in fragility.**

---

## On the `η^0.299` connection — the exponents do **not** discriminate

Fitting `ĝ_crit ∝ η^n` over six points:

| edge | `n` | max log-residual |
|---|---|---|
| E1 (`λ=0`) | **−0.0478** | 0.0387 |
| E2 (`λ=0.1`) | **−0.0701** | 0.0534 |

The residuals are `0.04–0.05`, so this is an **approximate** trend, not an
established power law, and the exponents are indicative only.

It is tempting to set `−0.05…−0.07` (background) against `+0.299` (perturbation
sector, `FINDING_P80`) and conclude there is no shared `IC → envelope → response`
map. **That inference does not hold.** If both quantities depend on a common
envelope `A(η)` — one as `A^a`, the other as `A^b` — different exponents follow
automatically from a *single* map. The exponents alone separate nothing.

What *would* discriminate: measure `A(η)` directly and test whether both
quantities collapse onto functions of it. `FINDING_P82` already attempted the
envelope route for `D` (RMS over the growth window) and got `0.390`, not the
`1` a clean collapse needs — so that route is known not to work cleanly, and
saying more than that here would be inventing a result.

---

## What is NOT established

- **Boundaries other than the two P81 localised.** A boundary elsewhere in
  `(ĝ, λ)` could behave differently; nothing here excludes it.
- **Topology below the reduced grid's resolution** — P81's own limit, inherited
  and not removed.
- **Lever settings above `×4`.** `×10` is excluded by construction.
- **That `V=0` is fatal at `ĝ ≥ 0.75` in general** — it is fatal there only when
  `φ̄̇(1)` is large enough. See the correction filed in `FINDING_P81`. This does
  **not** touch `FINDING_P69`, which worked at different parameters (Gate 1).
- **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in force.
- **Anything about MULTING itself** (Gate 1). The completion is ours.
- **Perelman condition 5** (external reconstruction) — still not met.
