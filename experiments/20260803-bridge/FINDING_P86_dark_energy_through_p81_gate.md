# FINDING P86 — **DE-DECOUPLED**, and the gate turns out to be blind to `Λ` by construction

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifacts:** `P86_dark_energy_through_p81_gate.py`, `P86C_part_c_standalone.py`

> The verdict is **half a result**. One half is measured; the other half is a
> property of the *predicate*, not of the cosmology, and quoting the number
> without it would overstate what was shown.

---

## What was added, and why it is one parameter

`FINDING_P85` returned Z-CONDITIONAL: the `t → z` mapping is free, but the
background contains no dark energy, so no epoch is "today". P85 registered the
prediction that such a term could not be added cosmetically — it would have to
re-enter at P81's viability gate. This cashes it.

Adding a constant to the potential, `V = λφ̄⁴/4 + V₀`, and adding a cosmological
constant to Friedmann are **the same operation** here: a constant has zero
derivative, so `V′ = λφ̄³` is untouched and Klein–Gordon never sees it, while the
energy density does. One parameter, Friedmann only.

**How much?** Not free-floating. `Λ` is constant while `ρ_m ∝ a⁻³`, so `Ω_Λ`
rises monotonically and *some* epoch always has `Ω_Λ = 0.7`. Choosing `Λ` **is**
choosing which `a` is "today" — the same single external number P84 and P85
already counted. `Ω_Λ = 0.7` is used here as a **definition** of the reference
epoch, never as a value imported from data.

`P81.viability()` was **extended** with `lam_cc`, not reimplemented — two copies
of a predicate drift, and P86 would then be measuring a gate P81 never had.

---

## The control that was broken by the rule it cited

**C2, first version.** It called `viability()` with an absurd `Λ`, got
`state=UNRESOLVED` ("integrator gave up"), and scored `not ok` as *"the gate can
reject a Λ"*. Under the Substrate Gate rule — **the one P81 itself had to be
corrected for** — unresolved means *not measured*, which is neither viable nor
non-viable. An infrastructure failure was recorded as evidence about the
predicate, inside a control written to prevent exactly that.

**C2, rewritten**, asks the honest question instead: is there *any* `Λ` the gate
rejects on **physical** grounds?

| `Ω_Λ=0.7` at | `Λ` | state | `min_M` | ok | why |
|---|---|---|---|---|---|
| `a=1e+06` | `2.333e-18` | measured | `0.871740335` | True | viable |
| `a=5e+05` | `1.867e-17` | measured | `0.871740335` | True | viable |
| `a=1e+05` | `2.333e-15` | measured | `0.871740335` | True | viable |
| `a=3e+04` | `8.642e-14` | measured | `0.871740335` | True | viable |
| `a=1e+04` | `2.333e-12` | measured | `0.871740335` | **False** | `rho_phys<=0` |
| `a=5e+03` | `1.867e-11` | unresolved | — | False | integrator gave up |

**`any rejection on a PHYSICAL clause: False`.**

The single rejection fires on `rho_phys<=0` — and that happens because `Λ` drives
`a` to `≈ 4.9e195`, so `C/a³` **underflows to exactly `0.0`** in double
precision. `min_rho_phys` is `0.0`, not negative. `min_M` stays at `0.8717`
throughout, so `1−ĝφ̄` never approaches zero — which is the pathology that clause
exists to catch. The rejection is **arithmetic, not physics**:
BLOCKED-INFRASTRUCTURE.

### The real finding hiding in that control

**P81's predicate has no clause a cosmological constant can violate.** Its four
conditions are `a>0`, `ρ_phys>0`, `min(1−ĝφ̄)>0.1`, `H` monotone. More `Λ` means
more Hubble friction, which **damps** `φ̄` and pushes `1−ĝφ̄` back toward 1 —
*toward more viable*. `H` still decreases (to `√Λ`). There is no "must
decelerate" condition anywhere in it.

---

## Making the gate affordable, and validating that first

P86's Part C stalled: every non-viable evaluation is a runaway the solver fights
to `t=1e8` at `rtol=1e-10`, and a bisection spends half its iterations there. The
old run sat **1333 s** on a single grid row.

`P81.viability()` now carries a **terminal event** at `M = 1−ĝφ̄ = −1`, by which
point the predicate has already failed irrecoverably (`FLOOR` is `0.1`, and
`ρ_phys = ρ_A·M` is negative there).

**That change alters how the predicate is computed, so it was validated before
being used** — `P86C` Part A is a *blocking* gate that refuses to run Part C if
anything moves:

| | check | result |
|---|---|---|
| **A1** | P81's three published **viable** points | `0.871740 / 0.864306 / 0.484961` — exact |
| **A2** | P83's **located boundary** `ĝ_crit(λ=0.1)` | `2.751767` vs published `2.751767`, rel `1.764e-07`, 12 iterations |
| **A3** | the one allowed change | `(2,0)` was **UNRESOLVED**; now **measured**, `M` reaches `−1` at `t=153.9` |

A1 alone would have proved nothing — viable points never reach `M = −1`, so they
cannot be affected *by construction*. **A2 is the one carrying information**: it
probes exactly the region where the event fires, and it is the quantity Part C
measures.

### One consequence to record

For **non-viable** points the reported `min_M` is now the value **at the stop**
(`−1`), not the global minimum over the full span. The `ok` flag is unchanged
everywhere, but figures like `FINDING_P81`'s `−1.86e+13` are no longer
reproducible by the current code. A note has been filed there.

---

## Results

### Part B — the grid, with and without `Λ`

| `ĝ \ λ` | 0 | 0.01 | 0.1 | 0.5 | 1 | 2 | 10 |
|---|---|---|---|---|---|---|---|
| 0 | OK | OK | OK | OK | OK | OK | OK |
| 0.25 | OK | OK | OK | OK | OK | OK | OK |
| 0.5 | OK | OK | OK | OK | OK | OK | OK |
| 0.75 | . | OK | OK | OK | OK | OK | OK |
| 1 | . | OK | OK | OK | OK | OK | OK |
| 1.5 | . | OK | OK | OK | OK | OK | OK |
| 2 | . | OK | OK | OK | OK | OK | OK |
| 3 | . | . | . | OK | OK | OK | OK |

**49 of 56 viable with `Λ`; 49 of 56 without. Zero classification flips.**

### Part C — the verdict quantity

| edge | P83 (no DE) | with DE | `R_boundary` | iters |
|---|---|---|---|---|
| `ĝ_crit` at `λ = 0` | `0.738209` | `0.748289` | **`0.0137`** | 15 |
| `ĝ_crit` at `λ = 0.1` | `2.751767` | `2.751767` | **`0.0000`** | 12 |

### An asymmetry that is not noise

The `λ=0` edge moves `1.4 %`; the `λ=0.1` edge does not move at all. That
follows from **diamond D1**: at `λ=0` there is no confinement — `φ̄` grows
monotonically with zero turning points — so `Λ`'s extra Hubble friction genuinely
damps it and pushes the boundary *up*, toward more viable. At `λ=0.1` the
potential's confinement already dominates and `Λ` adds nothing measurable.

**`Λ`'s friction only matters where the potential is not already confining.** Not
designed in; it falls out of D1.

---

## Verdict — **DE-DECOUPLED**, read with both halves

Worst `R_boundary = 0.0137 < 0.08`, the yardstick being the largest `R_boundary`
P83 measured inside matter domination.

**Measured half.** `min_M = 0.871740335` is unchanged to `3e-11` across **five
orders** of `Λ`. The constraint epoch sits at `a ≈ 12` (diamond D2), where `Λ` is
below the matter density by many orders, so a term that only matters at `a ≈ 1e5`
cannot reach it. **This confirms D2's prediction directly.**

**Structural half.** Part of the decoupling is not a fact about epochs at all:
the predicate has *no clause* `Λ` can violate. Quoting `0.0137` alone would
present a structural insensitivity as an empirical result.

### Consequence for `FINDING_P85`

`P85`'s **Z-CONDITIONAL is liftable**. The completion can carry a dark-energy
term without disturbing anything P81 or P83 established, so an epoch worth
calling "today" now exists — at the cost of the **same one** external number P84
already counted, and no more.

---

## What is NOT established

- **That the extended completion is right.** Viability is **necessary, never
  sufficient** — P81's own caveat, inherited unchanged, and now weakened further
  by the gate's `Λ`-blindness.
- **That `Ω_Λ = 0.7` is correct for anything.** A definition of the reference
  epoch, not a measurement.
- **That `Λ` is the right *form*.** A constant is the cheapest option; a
  dynamical dark energy would enter Klein–Gordon and would have to re-enter here.
- **That a `Λ`-sensitive viability criterion could not be written.** One could —
  it would need a clause about acceleration or an age constraint. P81 has none,
  and this file does not add one.
- **Anything observational.** No dataset, no Table A1 quantity;
  `NO_BRIDGE_FITTING` untouched.
- **Anything about MULTING itself** (Gate 1). Adding a term to *our*
  reconstruction says nothing about the source model.
- **Perelman condition 5** — still not met.
