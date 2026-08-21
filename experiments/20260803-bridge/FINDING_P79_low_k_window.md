# FINDING P79 — **W-FAIL.** The separation is an initial-condition artifact.

**Status:** built, run, verdict issued against pre-registered thresholds.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P79_low_k_window.py`

> **This file was written to destroy the best result of the arc, and it did.**
> `FINDING_P78`'s **D-SEP** is retracted.

---

## Why this ran before anything was built on P78

`P78` returned D-SEP on the strength of one point:

```
k=1  +26.71%      k=3  +0.63%      k=10  +0.10%      k=30  +0.00%
```

Essentially the whole verdict lived at `k=1` — and `k≲1` is exactly the window
`P77` had already flagged: the largest `a₂`-spread (`1.0059` against `1.0020`
elsewhere), the largest anchor sensitivity, and an outright blow-up at
`(ĝ=0.5, k=1)` where the coupled contrast crosses zero ~160 times.

**The strongest claim of the campaign stood on its least validated ground.**

### The quantity under test is the separation, not `ε`

`P76/P77`'s gates were built for `ε`. D-SEP asserts something else — that
`ε_exp − ε_lin` is nonzero and meaningful. **A stable `ε` with an unstable
difference is a perfectly possible combination**, so the gates are applied here
to the *difference*.

**Thresholds fixed before the run and not adjusted after:** G1 `<2 %`, G2 `<5 %`,
G3 `<10 %`, G4 rtol-stable, G5 crossings on **all four** runs.

---

## Results

**Baseline separation:** `6.621×10⁻³` at `k=1` (+26.71 %), `4.166×10⁻³` at `k=2`
(+16.24 %), `2.531×10⁻⁴` at `k=3` (+0.63 %).

### G1 — `a₂`-convergence `[FAIL]`

| k | @10⁶ | @10⁷ | @8×10⁷ | final change |
|---|---|---|---|---|
| 1 | 6.560×10⁻³ | 6.598×10⁻³ | 6.621×10⁻³ | 0.35 % ✓ |
| **2** | 3.779×10⁻³ | 4.040×10⁻³ | 4.166×10⁻³ | **3.13 %** ✗ |
| 3 | 2.563×10⁻⁴ | 2.535×10⁻⁴ | 2.531×10⁻⁴ | 0.17 % ✓ |

### G2 — anchor `A₁` across three decades `[FAIL]`

| k | min | max | spread |
|---|---|---|---|
| 1 | 6.355×10⁻³ | 6.686×10⁻³ | 1.0520 (5.2 %) |
| **2** | 3.658×10⁻³ | 4.572×10⁻³ | **1.2498 (25 %)** |
| 3 | 2.398×10⁻⁴ | 2.531×10⁻⁴ | 1.0555 (5.6 %) |

### G3 — the `φ̄̇(1)` lever `[FAIL — and this is the decisive one]`

| `φ̄̇(1)` | k=1 | k=2 | k=3 |
|---|---|---|---|
| ×0.1 | 8.894×10⁻³ | 9.467×10⁻⁴ | **−6.365×10⁻⁵** |
| ×0.5 | 9.393×10⁻³ | 2.128×10⁻³ | 4.539×10⁻⁵ |
| ×1 | 6.621×10⁻³ | 4.166×10⁻³ | 2.531×10⁻⁴ |
| ×2 | 1.800×10⁻³ | 1.297×10⁻³ | 1.664×10⁻⁴ |
| **spread** | **5.2×** | **4.4×** | **sign change** |

`×10` was **deliberately excluded**: `P77` established it puts 84.85 % of the
`t=1` energy budget in the scalar — a kination-dominated cosmology, not a
variation of initial data. Every point above is matter-dominated.

**At `k=1` the separation varies by a factor 5. At `k=3` it changes sign.** Both
values there are four orders above the floor, so this is not noise around zero;
these are two confidently measured numbers of opposite sign.

### G4 — rtol `[PASS]` · G5 — zero-crossings `[PASS]`

| rtol | separation at `k=1` |
|---|---|
| 10⁻⁸ | 6.621256415265×10⁻³ |
| 10⁻¹⁰ | 6.621256589116×10⁻³ |
| 10⁻¹² | 6.621256556646×10⁻³ |

Largest relative shift **2.63×10⁻⁸**. And crossings, counted on **all four** runs
(the exact error `P77` made and retracted — it counted only the reference):
**1 crossing everywhere, at every `k`.**

---

## Verdict — **W-FAIL**

**Three of five gates fail. `FINDING_P78`'s D-SEP is unsupported.**

### Why G4 and G5 passing is what makes this decisive

If the window were numerically bad, G4 or G5 would fail too and the diagnosis
would be "fix the integrator". They pass — cleanly. **So the window is
numerically sound and the separation genuinely depends on the initial
conditions.** That is a statement about the observable, not about the arithmetic.

### A reframing I floated, and which the data killed

Between the partial and full runs I suggested the gates might be measuring
*precision* while D-SEP asserts only *existence* — the same category error found
in `P76`'s convergence gate. **G3 destroys that.** A quantity that changes sign
under a legitimate initial-data variation does not establish the existence of a
separation with a definite sign either. There is nothing to reframe, and the
`AOG-1` question is moot rather than argued away.

### What this does and does not mean

| | |
|---|---|
| **Established** | the separation observed in `P78` is a property of the **measurement window**, not of the completions |
| **NOT established** | that the completions are degenerate. `D-DEG` was not returned. **The window cannot tell** — a third outcome, distinct from both |
| **Consequence** | bridge 4 (completion uniqueness) reverts to **open**, with the obstruction named: *the discriminating power sits at low `k`; at low `k` the separation is initial-condition dependent* |

---

## What this does NOT establish

1. **That completions are indistinguishable in principle** — only that *this*
   observable in *this* window cannot distinguish them.
2. **That a better-conditioned low-`k` observable does not exist.** Finding one is
   now the named prerequisite for reopening bridge 4.
3. **That the `k≳10` agreement is exact** — it is agreement to 5 digits at `k=30`,
   which bounds any high-`k` discrimination but does not exclude it below that.
4. **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in force.
5. **Anything about MULTING itself** (Gate 1): both completions are *ours*.

---

## Consequence for the plan

The `TZ` stop rule requires **both** `W-FAIL` *and* `A-DEG` before stopping. Only
the first has occurred, so `P80` proceeds — and it matters **more** now, not
less: if the on-shell attribution can separate the background channel from the
direct one, it will say **which** channel carries the initial-condition
dependence found here. That is currently indistinguishable, and it is the
difference between "the background history is IC-sensitive" and "the coupling
itself is".

---

## Skeptic Verdict (Step 8a)

**This file is itself the adversarial pass**, written and pre-registered before
its numbers, with thresholds fixed in the docstring and unchanged afterwards. A
separate context-blind review has **not** been run on it — recorded as an open
item rather than claimed complete.
