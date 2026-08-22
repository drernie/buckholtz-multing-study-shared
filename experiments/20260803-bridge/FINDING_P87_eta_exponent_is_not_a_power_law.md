# FINDING P87 — **E-NOTALAW.** There was no exponent to explain, and the reason is Hubble friction

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifacts:** `P87_eta_exponent_is_it_a_power_law.py`, `scratchpad/p87_damping.py`

> Two earlier attempts hunted for the **meaning** of `η^0.299`. Both failed. This
> one asked the cheaper and more destructive question first — *is it a power law
> at all?* — and the answer dissolves the gap **with a mechanism**, not merely
> with a shrug.

---

## The question P80 never asked

`FINDING_P80` measured `D := ∂ε/∂ĝ_pert` at `ĝ_bg=0`, `k=10`, against
`η = φ̄̇(1)/φ̄̇_ref`. It reported the exponent (`0.299`) and the spread (`4.32×`)
but **not the fit residual**.

`FINDING_P83` had already hit this: its `ĝ_crit ~ η^{−0.048}` carried log-residuals
of `0.039`, and that finding had to say *"approximate trend, not an established
power law."* **The same check was never run on `0.299`.**

---

## Controls, and the one that turned out to be prophetic

| | check | result |
|---|---|---|
| **C1** | the fitter must recover a known exponent | `x^0.5` → **`0.500000`**, resid `1.1e-16` |
| **C2** | it must **not** report a clean power law for a non-power curve | `1 + 0.3·ln x` → **`0.316366`**, resid `5.2e-02` |
| **C3** | the peak-finder must fail where D1 says no peak exists | `λ=0` → **`None`** |

**C2 was built to prove the fitter can detect a non-power-law. It returned
`0.316` — nearly indistinguishable from the mystery `0.299`.** That does not
prove `D(η)` is logarithmic. It shows vividly *what kind of number* a non-power
curve produces when forced through a power-law fit over a 16× range.

C1 alone would have been worthless here: a fitter that always reports "power law"
passes it. **C2 carries the information.**

---

## Part B — `D(η)` is not a power law

| `k` | exponent | max log-resid | R² | power law? |
|---|---|---|---|---|
| 3 | `0.469862` | `0.0494` | `0.988428` | **NO** |
| 10 | `0.298656` | `0.0202` | `0.996460` | **NO** |
| 30 | `0.289882` | `0.0185` | `0.996949` | *marginally yes* |

Threshold: `max log-resid < 0.02` — the level at which P83 refused to call its own
fit a power law.

**Exponent spread across `k`: `0.1800`**, against a stability criterion of `0.05`.

`k=30` scrapes under the residual threshold, which is exactly why one criterion
is not enough. **Stability decides it: `0.47 → 0.30 → 0.29` is not one number.**

Consistency check: `k=10` gives `0.298656` against P80's published `0.299` — the
same quantity is being measured, not a different one.

### Verdict — **E-NOTALAW**

`η^0.299` is not a property of the model. It is the **local slope at `k=10`** of a
curve that is not a power law. **The two earlier explanations failed not because
they were poor, but because there was nothing to explain.**

---

## Part C — the free-field prediction failed too, and that made the result general

At `ĝ_bg=0` the background scalar has **no source**: it is a free field in
`V = λφ̄⁴/4` from `φ̄(1)=0`. Energy conservation to the first turning point gives
`φ̄_peak ∝ η^{1/2}`. Diamond D1 had already established the first peak is the
epoch that matters, so this quantity has independent standing.

| `η` | `φ̄_peak` | `t` of peak | `peak/η^0.5` |
|---|---|---|---|
| 0.25 | `1.801714e-02` | 21.58 | `3.603e-02` |
| 0.50 | `3.474293e-02` | 14.21 | `4.913e-02` |
| 1.00 | `6.563008e-02` | 9.568 | `6.563e-02` |
| 2.00 | `1.192692e-01` | 6.675 | `8.434e-02` |
| 4.00 | `2.003340e-01` | 4.914 | `1.002e-01` |

`φ̄_peak ~ η^0.873`, residual `0.0511`. **Prediction `η^0.5` fails — and so does
power-law-ness itself.**

---

## The mechanism, **confirmed** rather than guessed

The deviation runs in the direction Hubble friction would give: peak time falls
`21.6 → 4.9` as `η` grows, so small `η` sits under friction longer, its peak is
suppressed more, and the apparent exponent steepens. **But that was noticed after
seeing the direction**, which makes it a consistency observation, not a test.

**Decisive test: delete the `−3Hφ̄̇` term and re-measure.** With friction gone,
energy is exactly conserved to the turning point, so `η^0.5` becomes *exact* —
and the test was written so that failure would **withdraw** the story.

| | exponent | max log-resid |
|---|---|---|
| with friction | `0.872936` | `0.0511` |
| **without friction** | **`0.500000`** | **`0.0000`** |
| prediction | `0.500000` | — |

**Exact.** Zero residual.

> ### Why exponents are ill-defined in this system
>
> **Hubble friction introduces a time-dependent scale that breaks the scale
> invariance of the `η → amplitude` map.** Without friction: an exact power law.
> With friction: none. `η^0.299` was never a mystery — it is the same effect,
> observed in the perturbation sector instead of the background.

### The boundary of that claim, stated plainly

The frictionless run is a **diagnostic**, not a solution of the coupled system:
removing `−3Hφ̄̇` from Klein–Gordon while keeping Friedmann **violates the Bianchi
identity**. It is valid for the isolated question *what sets `φ̄_peak`* and
**cannot** be applied to `D`, which needs consistent perturbation equations.

So: friction spoiling `φ̄_peak`'s power law is **`[VERIFIED]`**. Carrying that
mechanism across to `D` is **`[INFERRED]`** — supported by both quantities failing
power-law-ness in the same system, not demonstrated.

---

## What survives from `FINDING_P80`

**Stands** — measured with controls: `D` is **odd** in `η` to `1.1 %`; `D(0) = 0`
**exactly** with both linear channels closed; `D` converges in both the
differencing step and `rtol`.

**Withdrawn**: the exponent `0.299`. The honest statement of the rest is
**"`D` grows sublinearly with `η`"**, with no exponent quoted.

### Consequence for the IC-dependence question

The campaign had asked whether `η^0.299` and P83's IC-dependence share a common
`IC → envelope → response` map. **There is nothing to connect**: one of the two
objects does not exist. What *is* now known is smaller and firmer — the map from
`η` to the background amplitude is the free-field energy balance **modified by
friction**, exactly and verifiably so in the frictionless limit.

---

## What is NOT established

- **That friction is why `D` is not a power law.** `[INFERRED]`, see above.
- **Anything outside `η ∈ [0.25, 4]` and `k ∈ [3, 30]`.** A wider range could
  behave differently; nothing here excludes it.
- **That some *other* function fits `D(η)` well.** This step shows a power law
  does not; it did not search for a replacement, and none is proposed.
- **Anything observational.** `NO_BRIDGE_FITTING` untouched.
- **Anything about MULTING itself** (Gate 1).
- **Perelman condition 5** — still not met.
