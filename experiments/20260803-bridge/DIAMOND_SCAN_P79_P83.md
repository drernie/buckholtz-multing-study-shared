# Diamond scan — arc P79 → P83

**Trigger:** the standing rule that a research phase is not "done" until the
scan runs (`feedback_diamond_scan`, written after the `F₄ = Aut(J₃(O))` synthesis
was nearly missed on 2026-06-27).
**L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Verification artifact:** `scratchpad/diamond_p79_p83.py` (both diamonds carry a
falsifiable prediction and were **run**, not asserted).

---

## Q1 — what was found that was **not** the goal

| find | whose goal was something else |
|---|---|
| **`γ = 2/3` with `w` measured `→ 1/3`** | P82 asked "does `f` exist and converge"; what came back was an **external textbook validation of the background's equation of state** |
| **`λ_crit = 0` exactly** | P83 measured the boundary's *movement*; what it learned was the boundary's **nature** — a discontinuity at the truncation surface, not a critical point |
| **`18.3070 %` vs P77's `18.31 %`** | P83's regime check independently reproduced a number P77 had published |
| **pearl_registry schema defect** — 37 of 181 rows invisible to the health hook | found while registering; 9 rows were mine, repaired; 26 are not and were reported, not rewritten |

## Q2 — which discarded result gets reinterpreted

**P77's 93/7 split — rehabilitated as a correct measurement of a mislabelled
quantity.** It had been withdrawn as protocol-dependent. P80 shows the number is
not wrong; it measures a **different cut** (Euler-term-only ablation). What was
wrong is the **label**: what P77 called "background" was carrying
perturbation-sector physics its probe could not separate.

**P78's D-SEP — the death is narrowed.** P83 shows the pipeline is IC-**robust**
(`R ≈ 0.08`) while the separation was IC-**fragile** (`R ≈ 4`). So D-SEP's death
was never a symptom of a shaky apparatus. The fragility belongs to the
**separation between completions**, specifically.

## Q3 — the unexpected pairs. **Two, both verified.**

### 💎 D1 — `λ`'s role is **confining**, not energetic

The two results sat badly together. P82 measured `w → 1/3`: the oscillating
quartic field redshifts like radiation, so its **energy** becomes negligible
(`Ω_φ: 3.2e-04 → 7.1e-07`). P81/P83 found that removing `λ` is **fatal**,
discontinuously. If the potential makes the scalar energetically irrelevant, why
is deleting it catastrophic?

**Because `λ` does not act through energy. It acts through amplitude.** With
`V=0`, `φ̄̈ = ĝρ_A − 3Hφ̄̇` has **no restoring force**: `φ̄` is sourced by matter
and never turns over, so `1−ĝφ̄` is driven toward zero. Any `λ > 0` supplies
`λφ̄³` and caps it.

Measured at `ĝ = 0.5`, where both sides are viable so the comparison is not
confounded:

| `λ` | max `φ̄` | monotone? | turning points | min `M` |
|---|---|---|---|---|
| **0** | `6.207e-01` | **True** | **0** | 0.689666 |
| `1e-8` | `3.148e-01` | False | 12 | 0.842593 |
| `1e-4` | `1.987e-01` | False | 46 | 0.900647 |
| `0.01` | `1.465e-01` | False | 89 | 0.926769 |
| `1` | `9.856e-02` | False | 181 | 0.950722 |

**This explains `λ_crit = 0` exactly.** Confinement is a qualitative on/off
switch, not a graded effect: `λ → 0⁺` gives an ever-later first turnover but
*still* a turnover; `λ = 0` gives none at all. The discontinuity P81 and P83 both
hit is a mechanism switching on, not a critical point being crossed.

The arithmetic closes: `min M = 1 − ĝ·max(φ̄)` exactly (`1 − 0.5×0.0986 = 0.9507`
✓), so **the minimum is attained at the global maximum of `φ̄`** — the first
oscillation peak, since the envelope is damped.

*The same `λ` that makes the scalar's energy irrelevant is what keeps its
amplitude bounded — and only the amplitude enters viability, through
`M(φ̄) = 1 − ĝφ̄`.*

### 💎 D2 — the viability constraint is set in an epoch the late universe has forgotten

`min(1−ĝφ̄)` is a minimum over eight decades. Where is it attained?

| `(ĝ, λ)` | `t` at min | fraction of log span | `a` there | `Ω_φ` **there** |
|---|---|---|---|---|
| (0.5, 1) | `1.07e+01` | 12.9 % | 12.9 | `5.0e-02` |
| (1, 1) | `1.00e+01` | 12.5 % | 12.2 | `1.2e-01` |
| (2, 0.1) | `1.66e+01` | 15.3 % | 16.2 | **`4.9e-01`** |
| (0.75, 1e-4) | `2.90e+02` | 30.8 % | 112 | `1.7e-01` |
| (1.5, 0.01) | `3.88e+01` | 19.9 % | 28.4 | `3.9e-01` |

The minimum lands in the first decade or two, while the scalar still carries
**5 % to 49 %** of the energy budget. By the epoch where `f(a,k)` is measured
(`t ≥ 1e4`), `Ω_φ` has fallen to `7.1e-07` — **four to six orders of magnitude**
lower.

**So the viable corner P81 mapped and P83 showed robust is fixed entirely by an
early transient of a component that is provably negligible during the epoch the
observable lives in. The boundary and the observable probe different epochs of
the same completion.**

**Pairing with P83, which is stronger than either alone:** a quantity determined
by an early transient turned out to be **robust to the initial scalar velocity**
(`R ≈ 0.08` across a 40-fold lever within matter domination). *Early does not
imply fragile* — which is not what one would guess, and is why P83 had to be run
rather than reasoned about.

**A refinement of P81's own predicate falls out:** the "≥ 8 decades" requirement
is not doing the work it appears to. The verdict is decided in the first ~1.5
decades; the remaining seven change nothing.

## Q4 — did we falsify a wrong *expectation* rather than the physics?

| falsified item | verdict |
|---|---|
| **P80's control A2** | **Yes, exactly this case.** The control asserted false physics (`∂ε/∂ĝ_pert` must vanish at `ĝ_bg=0`), so correct behaviour was recorded as failure — twice. Already reformulated. |
| **P78's D-SEP** | **Partly.** The expectation was "completions are distinguishable in `ε`". P79 killed it as IC-dependent, but P79's *own* registered prediction says a separation must be quoted **with an IC-spread bar**. D-SEP is therefore *not established* rather than dead, and a correct reformulation exists. |
| **My `1.958` ↔ cubic-term claim** | **No.** That was simply wrong in sign (`D = +0.163` predicts `2.140`, above 2, against a measured `1.958` below). Struck, not reformulated. |
| **Both `η^0.299` explanations** | **No.** One was an invalid test (point sample of an oscillating field), one a matched estimator that returned `0.390`. The gap stays open. |

---

## What this changes for the next step

The normalisation bridge inherits a structural fact it did not have before: **the
`(ĝ, λ)` corner is an early-universe constraint, and `f(a,k)` is a late-universe
observable.** Any mapping from internal units to `h/Mpc` has to carry both, and
they are not constrained by the same physics or the same epoch.

## What is NOT established

- **That D1's mechanism is the *only* route to the `λ=0` pathology.** It is
  sufficient and measured; nothing here excludes an additional one.
- **That the early-transient structure survives outside the five `(ĝ,λ)` points
  probed for D2**, or outside the default IC (P83 tested the boundary's IC
  robustness, not the *timing* of the minimum).
- **Anything about `FINDING_P69`** (Gate 1 — different parameters).
- **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in force.
- **Perelman condition 5** — still not met.
