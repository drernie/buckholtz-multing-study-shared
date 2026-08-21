# FINDING P77 — the spectrum survives; "fifth force" and "k=10" do not

**Status:** built, run. **Retracts three claims of `FINDING_P76`.**
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive — this characterises a
property of a model *we* constructed. No causal claim about nature is made.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P77_growth_attack.py`

> **Why this file exists.** `FINDING_P76` produced the first quantity in the
> `P50A→P76` arc to survive the `φ̄̇(1)` lever. Precisely *because* it is the best
> candidate so far, it gets attacked hardest. Four axes, three named by an outside
> reading and one by this file. **Two of the four overturn P76's headline.**

---

## A. Is `k=10` a regime, or a lucky grid point? — **REGIME** `[VERIFIED-BASH]`

P76 tested `k = 0.1, 1, 10` and called `k=10` "deep subhorizon". Three points
cannot establish a regime. Filled in:

| k | 1 | 3 | 5 | 10 | 20 | 30 | 100 |
|---|---|---|---|---|---|---|---|
| `k/aH` @8e7 | 243 | 729 | 1214 | 2429 | 4857 | 7286 | 2.4×10⁴ |
| **ε** | 0.024793 | 0.039965 | 0.043132 | 0.045688 | 0.046479 | 0.046633 | **0.046747** |
| spread over `a₂` | 1.0059 | 1.0023 | 1.0020 | 1.0020 | 1.0020 | 1.0020 | 1.0020 |

**All seven stable to ≤0.6 %.** `ε(k)` rises smoothly and **saturates**:
increments `0.0152 → 0.0031 → 0.0026 → 0.0008 → 0.00015 → 0.0001`.

```
ε_∞ ≈ 0.0467
```

This is **S3** of the pre-registered outcomes — not merely "a regime exists"
(S1) but a *systematic, saturating spectrum*. **S2 (grid accident) is refuted.**

**Independent cross-check, not fitted:** the transition sits near `k ≈ 2–3`, and
`FINDING_P70` *separately* derived a comoving screening scale
`k_J = √3·λ^{1/6}(ĝC)^{1/3}` — which at `λ=ĝ=C=1` is `√3 ≈ 1.73`, and predicted
suppression for `k ≪ k_J`, no suppression for `k ≫ k_J`. Two independent routes,
one scale. `[INFERRED — the transition was read by eye; no threshold fit was
performed, so this is a consistency observation, not a measurement]`

---

## B. Does `ε` depend on the anchor? — passes, with a real bias

P76 computed `ε = ln G(a₂;A₁)/ln(a₂/A₁)` with `A₁` **pinned** at `t=10⁴`. That is
a mean slope from a fixed anchor, not `d lnG/d lna`; stability under moving `a₂`
does not establish independence of `A₁`. Never tested in P76.

| `A₁` from `t=` | ε(k=3) | ε(k=10) | ε(k=30) |
|---|---|---|---|
| 10³ | 0.039779 | 0.045486 | 0.046427 |
| 10⁴ | 0.039965 | 0.045688 | 0.046633 |
| 10⁵ | 0.040042 | 0.045762 | 0.046710 |
| 10⁶ | 0.040060 | 0.045784 | 0.046732 |
| **spread** | 1.0071 | **1.0065** | 1.0066 |

Passes at **0.65 %** — but the drift is **monotone**, so it is a bias, not noise.
The anchor-free **local slope** (finite difference between adjacent `a₂`, no
anchor at all) gives:

| k | `ε_local` (10⁶–10⁷) | (10⁷–8×10⁷) | anchored ε |
|---|---|---|---|
| 3 | 0.040055 | 0.040066 | 0.039965 |
| 10 | 0.045778 | **0.045790** | 0.045688 |
| 30 | 0.046727 | 0.046739 | 0.046633 |

**The anchored form is biased LOW by ~0.2 %**, by an early transient sitting
inside the average. `ε_local(k=10) = 0.04579` is the honest number. Small, but it
is a bias and it is now measured rather than assumed absent.

---

## C. ⚠️ The lever over a range P76 did **not** choose — **k=10 FAILS**

P76 used `φ̄̇(1) ×0.5` and `×2` — **its own choice**, which may have been
conveniently narrow. Pushed two decades:

| `φ̄̇(1)` | ×0.1 | ×0.5 | ×1 | ×2 | **×10** | spread |
|---|---|---|---|---|---|---|
| ε(k=10) | 0.045764 | 0.045753 | 0.045688 | 0.045344 | **0.041343** | **1.1069 ✗** |
| ε(k=30) | 0.046621 | 0.046627 | 0.046633 | 0.046621 | 0.045869 | 1.0167 ✓ |

**At `k=10` the spread is 10.7 % — the gate FAILS.** At `k=30` it is 1.7 % and
passes.

**⚠️ RETRACTION 1:** P76's "clean corner at `k=10`" is **wrong**. The corner is
`k ≳ 30`. The narrow lever range was mine, and it flattered the result.

---

## D. ⚠️ Attribution — **"fifth force" is withdrawn**

`(ĝ=1,λ=1)` vs `(ĝ=0,λ=1)` changes **two** things: the background history *and*
the direct scalar force in the perturbed Euler equation. So "this is a fifth
force" was stronger than the data. Ablated:

- **A** full coupled
- **B** same coupled background, `+ĝρ_Aδφ` **removed from Euler**
- **C** `ĝ=0` control

| k | ε_full (A−C) | ε_bg (B−C) | direct (A−B) | \|C₀ᵢ\| of B |
|---|---|---|---|---|
| 3 | 0.039965 | **0.037616** | 0.002348 | 6.06×10⁻² |
| 10 | 0.045688 | **0.042668** | 0.003019 | 6.78×10⁻² |
| 30 | 0.046633 | **0.043486** | 0.003147 | 6.90×10⁻² |

**~93 % of the effect is background-mediated.** The direct force contributes
~6.6 %.

**⚠️ RETRACTION 2:** the effect is a **modified expansion history**, not a new
force on matter. P76's framing is withdrawn.

### The caveat that matters more than the split

**B is deliberately off-shell.** Deleting a term breaks the first-class algebra
`FINDING_P73` proved, so B violates the `0i` constraint — measured at
**6.8×10⁻²**. The direct contribution is **6.6×10⁻²** of the total.

**These are the same order.** So the decomposition **cannot resolve the direct
term from the probe's own systematic.** What *is* robust is the dominance of the
background: 93 % against a 7 % systematic. A probe broken by exactly the size of
the signal answers "which is bigger", never "by how much".

---

## E–H. The remaining four axes

**Parity** — `ε(+ĝ)` vs `ε(−ĝ)`: odd/even = `0.0054 / 0.0011 / 0.0001` at
`k = 3/10/30`. **The leading effect is even in `ĝ`.** Consistent with `ĝ²` — and
**non-discriminating**, exactly as anticipated: `ρ_phys = ρ_A(1−ĝφ̄)` with `φ̄`
itself sourced by `ĝ` produces `ĝ²` from the background alone.

**rtol** — `ε(k=10) = 0.045687543` to **nine digits** across `rtol ∈ [10⁻⁸,10⁻¹²]`,
largest shift `1.3×10⁻¹¹`. **The number belongs to the model, not the solver.**
A reviewer hypothesis that it might track rtol is **refuted**.

**⚠️ Cubic correction** — fitting `|G−1| = C·ĝ²(1+D·ĝ)` gives
**`C = 0.2713`, `D = 0.1483`**: the cubic term is **14.8 %** of the quadratic at
`ĝ=1`, and the local slopes drift `2.0125 → 2.1791`.

**⚠️ RETRACTION 3:** "quadratic scaling" is a **leading-order** description only.
P76's flat statement is withdrawn.

**The pole — my own test did not discriminate.** Sign-change count of the
reference contrast is **1 at every `k` tested (0.5, 0.7, 1, 1.5, 2, 3)**,
including all the clean ones — yet only `k=1` blows up (`|G−1| = 3.25×10¹⁰`).

> A test that returns the same answer regardless of which branch is true is not a
> test — this project's own Cheapest-Differentiating-Test rule. **P76's pole
> diagnosis ("near-zero contrast at an anchor") is probably right — the crossing
> at `k=1` likely lands near an anchor — but this file did not show it.** The
> discriminating test is to move `A₁` at `k=1` and see whether the blow-up moves
> with it. **Not done.**

---

## Verdict

| axis | pre-registered outcome | result |
|---|---|---|
| regime | S1 / S2 / S3 | **S3** — saturating spectrum, 7 stable k |
| anchor | ANCHOR FAIL? | **passed** (0.65 %), with a measured 0.2 % low bias |
| lever ×0.1…×10 | — | **FAILED at k=10**, passed at k≥30 |
| attribution | withdraw if bg dominates | **withdrawn** — 93 % background |

**Survives from P76:** the spectrum `ε(k)`, its saturation at `ε_∞ ≈ 0.0467`, the
rtol-independence, the even parity, and the fact that `μ_tot ≡ 1` means Einstein
gravity is untouched.

**Withdrawn from P76:** "fifth force", "clean at k=10", "quadratic scaling".

```
ε_local(k≥30) ≈ 0.0466 → ε_∞ ≈ 0.0467
  a saturating, rtol-stable, even-in-ĝ, ~93 % BACKGROUND-MEDIATED
  growth-index shift, lever-stable only for k ≳ 30
```

---

## What this does NOT establish

1. **Anything observational.** No calibration of `k` to `h/Mpc`, no data
   comparison; **`NO_BRIDGE_FITTING` remains in force**.
2. **The size of the direct force** — the probe's systematic equals it.
3. **That the transition scale *is* `k_J`** — read by eye, not fitted.
4. **The pole diagnosis at `k=1`** — the test used did not discriminate.
5. **Anything at other `λ`** — only `ĝ` was scanned.
6. **Anything about MULTING itself** (Gate 1): the completion is *ours*.

---

## Skeptic Verdict (Step 8a)

**Not yet run on P77 itself.** P77 *is* the adversarial pass on P76, built from a
context-blind review plus an outside reading; running a further review on the
attack file is the natural next step and has not been done. Recorded as an open
item rather than claimed as complete.
