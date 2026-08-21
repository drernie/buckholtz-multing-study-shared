# FINDING P78 — the growth channel appeared to discriminate completions. It does not.

**Status:** built, run, **verdict retracted the same day by `P79`.**
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P78_completion_discrimination.py`

---

> ## ⚠️ RETRACTED BY `FINDING_P79`
>
> This file returned **D-SEP** — the growth channel separates the two mass laws
> by **26.7 % at `k=1`**, `5×10⁸×` the numerical floor. `P79` then applied the
> five gates `P76/P77` had built, **to the separation itself**, and three failed:
>
> | gate | result |
> |---|---|
> | G1 `a₂`-convergence | **FAIL** — 3.13 % at `k=2` (threshold 2 %) |
> | G2 anchor `A₁` | **FAIL** — 25 % spread at `k=2` |
> | G3 `φ̄̇(1)` lever | **FAIL** — **5.2× spread at `k=1`, and the separation CHANGES SIGN at `k=3`** |
> | G4 rtol | PASS (2.6×10⁻⁸) |
> | G5 zero-crossings | PASS (1 crossing on all four runs) |
>
> **G4 and G5 passing is what makes this decisive.** The window is numerically
> clean, so the failure is not an integrator artifact — the separation genuinely
> depends on the initial conditions.
>
> **D-SEP is unsupported.** Bridge 4 (completion uniqueness) reverts to **open**,
> with the obstruction now named: *the discriminating power sits at low `k`, and
> at low `k` the separation is an initial-condition artifact.*
>
> **This is NOT evidence that the completions are degenerate.** It is evidence
> that this measurement window cannot tell. `D-DEG` was not returned either.

---

## The question

`FINDING_P75` proved the **structural** layer is completion-blind: the constraint
algebra closes with `V(φ)` and `M(φ)` unspecified, so P68's exponential mass law
and P69's quartic-potential linear law are structurally indistinguishable **by
proof**. `FINDING_P76/P77` then built a **dynamical** channel, `ε(k)`, of which
`P77`'s ablation showed ≥83.6 % is *background*-mediated — precisely the layer
where completions differ most. Hence:

```
does ε(k) differ between   M(φ) = 1 − ĝφ   and   M(φ) = e^{−ĝφ} ?
```

**Both are completions of the same local law**, and that premise is *checked*:

| law | `M(0)` | `M′(0)` | `M″(0)` |
|---|---|---|---|
| linear | 1.000000000 | −1.000000000 | 0.000000000 |
| exponential | 1.000000000 | −1.000000000 | **1.000000000** |

Identical to first order — the order the local force law fixes — and free to
differ beyond it, which is what "a completion" means.

**Revival condition** (Adaptive Iteration Branch Rule): P68 was `parked`. Reviving
it needs a condition absent at parking time, and there is one — `P75` proved
structural discrimination impossible and `P76/P77` built a channel that did not
then exist. The branch is revived **to be measured, not promoted**.

---

## Controls — all three exact

| control | result |
|---|---|
| **A2** at `ĝ=0` the two systems are identical (`M ≡ 1`), so `ε` must agree to machine precision | **`0.000e+00`** — bit-identical at `k=1` and `k=10` |
| **A3** the linear branch must reproduce `P76`'s own code | **`0.00e+00`** at every `k`, to 12 digits |

**Both floors are exactly zero**, so the effective floor is `P77`'s rtol
stability, `1.3×10⁻¹¹`.

### A3 caught an error in the test, not in the code

A first version hard-coded `FINDING_P77`'s **published** values, which are
rounded to six decimals, and the assert fired at a `1.35×10⁻⁵` "discrepancy" —
entirely the rounding of my own reference table (`0.045688` vs the true
`0.045687543`). Tightening rtol from `10⁻⁸` to `10⁻¹²` left the gap at **exactly
zero**, proving it was not integrator noise. Fixed by importing `P76` and running
it. **Comparing a rounded literal against a full-precision computation is not a
reproduction test.**

---

## The measurement

| k | ε linear | ε exponential | difference | relative |
|---|---|---|---|---|
| **1** | 0.024793 | 0.031415 | **6.621×10⁻³** | **+26.71 %** |
| 3 | 0.039965 | 0.040218 | 2.531×10⁻⁴ | +0.63 % |
| 10 | 0.045688 | 0.045735 | 4.717×10⁻⁵ | +0.10 % |
| 30 | 0.046633 | 0.046635 | 1.951×10⁻⁶ | +0.00 % |

Largest separation **`5×10⁸×` the floor** → the pre-registered **D-SEP**.

**And the shape is the whole story.** The completions **agree deep subhorizon**
(identical to 5 digits at `k=30`) and differ only near the transition — which is
physically sensible, since `M(φ)` differ at *second* order and second order
weighs most where `φ` does the most work. But it also means the entire verdict
rested on `k≲1`, the one window `P77` had flagged as least trustworthy.

`P79` was written to test exactly that, and it destroyed the verdict.

---

## What survives

1. **The controls.** Two independent floors measured at exactly zero, and a
   reproduction of `P76` bit-for-bit. The machinery is sound; what failed is the
   window.
2. **The generalised system.** `make_system` now takes arbitrary `M(φ)`, with
   signs derived from `P75`'s general form and verified against `P76`'s at
   `M′=−ĝ`. Any future completion can be measured through it.
3. **The premise check** — both mass laws demonstrably complete the *same* local
   law.
4. **The negative result itself:** the discrimination, if it exists, does **not**
   live deep subhorizon. At `k=30` the two completions agree to 5 digits. Any
   future attempt must look at the transition scale — and must first solve the
   initial-condition dependence `P79` found there.

## What this does NOT establish

1. **That the completions are distinguishable** — retracted by `P79`.
2. **That they are degenerate** — `D-DEG` was not returned either. The window
   cannot tell.
3. **That two mass laws span the completion space.** They are two points in it.
4. **Anything observational.** Internal units, `NO_BRIDGE_FITTING` in force.
5. **Anything about MULTING itself** (Gate 1): both completions are *ours*.

---

## Skeptic Verdict (Step 8a)

**Not run as a separate review.** `P79` *is* the adversarial pass on this file,
pre-registered before the numbers and executed with thresholds fixed in advance —
and it returned W-FAIL against this file's own headline. Recorded as an open item
rather than claimed complete.
