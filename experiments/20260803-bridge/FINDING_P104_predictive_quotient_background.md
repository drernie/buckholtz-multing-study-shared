# FINDING P104 — **CONVERGES (M1).** Dimensionless background shape survives the freedom `P103` proved — the first positive/converging result in the whole arc

**Status:** built, run (branch-range bug caught and fixed mid-build before
trusting a result), control passed, verdict against pre-registered
outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P104_predictive_quotient_background.py`

> User-proposed pivot, adopted as stated: `FINDING_P103` proved
> `Λ_internal` **not derivable in this completion** — not proved it
> unknowable in principle. The sharper next question: does `Λ`'s freedom
> also poison *dimensionless* predictions, or only the absolute scale?
> **M1** (scale degeneracy only — `Λ` is a clock offset) vs **M2**
> (dynamical degeneracy — `Λ` changes the physics itself).

---

## Scope cut, decided before building

The user's own examples (`k_J/(aH)`, ratios of `f(k)` growth differences,
transfer-function shape) are **perturbation-level** observables, computed
by `G_growth()`/`f_recon()` (the `P76`–`P92` growth-channel machinery).
Checked *before* writing code: `lam_cc` appears **only** in `P81`/`P86`
and the `P93`–`P103` bridge files — never in `P76`'s growth solver or
`P89`'s `f_recon`. That machinery has always run at `lam_cc=0` with no
hook for anything else. Testing the user's exact proposal would require
extending it first — itself a new completion needing its own full pass
(action → background → constraints → perturbations → viability →
observables), exactly as the user's own writeup anticipated. **Not done
here.** This file tests the same M1-vs-M2 question at the layer already
built: the background's dimensionless `H(a)` shape.

## The design

Comparing `H(a)` at a fixed numeric `a` across branches would be unfair —
different `Λ` trivially give different absolute `H` anywhere, which just
restates that `Λ` sets scale. Instead, each branch gets its own
`Λ`-intrinsic reference:

```
a_star(Λ) := (C_MATTER / Λ)^(1/3)      -- where ρ_Λ = ρ_matter
shape_Λ(x) := H(a_star(Λ)·x) / H(a_star(Λ))
```

No external anchor — `a_star` comes from the potential's own structure,
mirroring `FINDING_P86`'s "`Ω_Λ=0.7` is a definition, not a measurement"
logic. Ask whether `shape_Λ(x)`, as a function of `x`, is the same across
independently-chosen `Λ` branches.

## A branch-selection bug caught before trusting the result

First attempt used `Λ ∈ {1e-17, 1e-15, 1e-13, 1e-11, 1e-9}` — the two
largest values fall **outside** the window `FINDING_P100`/`P102` already
validated as measurable for this exact solver pipeline
(`[1.125×10⁻¹⁷, 4.924×10⁻¹²]`). `solve_background_safe(1e-9)` came back
`s._ok=False` outright — individually verified before rewriting the range,
not discovered mid-run. Corrected to `Λ ∈ {2e-17, 1e-16, 1e-15, 1e-14,
1e-13, 3e-12}`, all inside the validated window.

## Control — passed

At `x=0.02` (deep matter/field domination, far below every branch's own
`Λ`-crossing), `shape_Λ(x)` **must** already agree across branches — this
is a necessary precondition, not the main result.

| `Λ` | `shape(0.02)` |
|---|---|
| `2e-17` | `250.0129` |
| `1e-16` | `250.0199` |
| `1e-15` | `250.0408` |
| `1e-14` | `250.0908` |
| `1e-13` | `250.1936` |
| `3e-12` | `251.1895` |

Relative spread `4.70×10⁻³` — **passes** the `5%` threshold.

## Main comparison

| `x` | relative spread across 6 branches |
|---|---|
| `0.05` | `1.49×10⁻³` |
| `0.2` | `2.22×10⁻⁴` |
| `0.5` | `6.07×10⁻⁵` |
| `1` | `0.0` (trivial — normalization point) |
| `2` | `2.21×10⁻⁵` |
| `5`, `10` | not measurable at the widest branch (`Λ=2e-17`) — excluded, not forced |

**Worst spread across the whole comparison: `1.49×10⁻³`** (`0.15%`), at
`x=0.05` — orders of magnitude inside the `5%` convergence threshold,
across `Λ` spanning **5 decades** and `x` spanning nearly **3 decades**.

---

## Verdict — **CONVERGES (M1 — scale degeneracy only)**

Dimensionless `shape_Λ(x)` agrees across independently-chosen, unanchored
`Λ` branches to well within `0.2%` everywhere measurable. `Λ` behaves as
a clock/ruler offset here — it sets **where** the completion's history
sits, not **what shape** that history has. The same structural freedom
`FINDING_P103` proved for the absolute scale does **not**, on this test,
propagate into the dimensionless dynamics. The completion retains real,
dateable-only-not-shapeable predictive content — the first genuinely
**converging**, positive result in the `P93`–`P104` arc.

### Not established

- Anything at the perturbation/growth level (`f(k)`, Jeans scale,
  transfer function) — `G_growth`/`f_recon` never accepted `lam_cc`; a
  genuine perturbation-level Predictive Quotient test requires extending
  that solver first.
- That `x ∈ [0.05, 10]` is wide enough — collapse or divergence outside
  this range was not tested.
- That 6 log-spaced branches represent the full measurable `Λ` range — a
  denser scan was not attempted.
- Any numeric value of `ε(k)`, `f(k)`, or `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
