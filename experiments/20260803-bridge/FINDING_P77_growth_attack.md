# FINDING P77 — the spectrum survives; three of its own retractions were themselves wrong

**Status:** built, run, reviewed context-blind, **then corrected on four
axes — two against this file and two in its favour.**
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
ε_∞ = 0.046758
```

**Confirmed after review.** A reviewer suspected a slow logarithmic rise rather
than an asymptote. Extending the grid: `ε(300) = 0.046757` (increment
`1.01×10⁻⁵`), `ε(1000) = 0.046758` (increment `1.15×10⁻⁶`) — a 10× drop per step,
**faster than logarithmic**. Saturation confirmed; the concern is refuted.

This is **S3** of the pre-registered outcomes — not merely "a regime exists"
(S1) but a *systematic, saturating spectrum*. **S2 (grid accident) is refuted.**

> ### ⚠️ RETRACTED — the `k_J` cross-check
>
> An earlier version of this section claimed the transition sits near
> `FINDING_P70`'s independently derived `k_J = √3·λ^{1/6}(ĝC)^{1/3} ≈ 1.73`, and
> called it "two independent routes, one scale" `[INFERRED — read by eye]`.
> **Fitted, it fails.** A 7-point fit of `ε(k) = ε_∞·k²/(k²+k_J²)` gives
>
> ```
> fitted k_J = 0.9536        P70's derived k_J = √3 = 1.7321        ratio 0.551
> ```
>
> Forcing `k_J = √3` leaves a **−52.9 %** residual at `k=1`. Observed
> `ε(1)/ε(100) = 0.530` against the Yukawa prediction `1/(1+3) = 0.250` — a factor
> of two, not a near-miss. Even the *fitted* Yukawa form carries 4.4 % residuals,
> so the functional form is not a good description either. **The claim was
> coincidence, not consistency, and is struck.**

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
inside the average. `ε_local(k=10) = 0.04579` is the honest number.

**Confirmed after review**, and the local slope is **exactly** anchor-free, not
approximately: `G(a_j) = C_on(a_j)/C_on(A₁) ÷ [C_off(a_j)/C_off(A₁)]`, so in
`G(a_{j+1})/G(a_j)` both `A₁` factors cancel algebraically. Numerically, anchors
three decades apart give **`0.045789597` and `0.045789597`** — identical to nine
digits. Extending `A₁` to `t=10⁷` gives shifts `+2.0×10⁻⁴ → +7.4×10⁻⁵ →
+2.2×10⁻⁵ → +6.0×10⁻⁶`, converging on `0.04579`.

---

## C. The lever over a range P76 did **not** choose — and the range itself was wrong

P76 used `φ̄̇(1) ×0.5` and `×2` — **its own choice**, which may have been
conveniently narrow. Pushed two decades:

| `φ̄̇(1)` | ×0.1 | ×0.5 | ×1 | ×2 | **×10** | spread |
|---|---|---|---|---|---|---|
| ε(k=10) | 0.045764 | 0.045753 | 0.045688 | 0.045344 | **0.041343** | **1.1069 ✗** |
| ε(k=30) | 0.046621 | 0.046627 | 0.046633 | 0.046621 | 0.045869 | 1.0167 ✓ |

**At `k=10` the spread is 10.7 % — the gate FAILS as written.** At `k=30` it is
1.7 % and passes. But read on: the `×10` point does not belong in the test.

**⚠️ RETRACTION 1 — and it was itself over-strict.** P76's narrow `×0.5/×2`
range *was* mine and did flatter the result. But `×10` on `φ̄̇` is `×100` on the
scalar's **kinetic energy**, and that flips the early universe:

| lever | scalar kinetic fraction at `t=1` | regime |
|---|---|---|
| ×1 | 5.31 % | matter-dominated |
| ×2 | 18.31 % | matter-dominated |
| **×10** | **84.85 %** | **kination-dominated** |

So `×10` is **a different cosmology, not a perturbation of the initial data.**
The honest statement: `ε(k=10)` is stable to **~0.9 %** across every
matter-dominated start (`×0.1…×2`), and moves 10 % only if a scalar-dominated
start is admitted. **The `k=10` corner is reinstated with that scope; the
"corner is `k ≳ 30`" claim is withdrawn.**

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

**⚠️ RETRACTION 2 stands, but the NUMBER does not.** The effect is a
**modified expansion history**, not a new force on matter — P76's framing is
withdrawn, and that survives every test. The **93/7 split does not**: probe `B`
has no unique initial condition, and varying its *start time* moves the direct
share by a factor 2.5:

| `B` starts at | ε_bg | direct | direct share |
|---|---|---|---|
| `t=1` | 0.042668 | 0.003019 | **6.61 %** |
| `t=10³` | 0.038199 | 0.007488 | **16.39 %** |

At fixed protocol the split is clean — partial ablation with a factor `f` on the
fifth force gives a **linear** response (slope 0.003019, max residual `2.8×10⁻⁵`,
0.94 %), and the constraint violation scales as `(1−f)` and reaches `8.7×10⁻¹⁵`
at `f=1`, so it is bookkeeping, not an independent error. **But across protocols
the number moves 2.5×.** What is robust: the background dominates in every
protocol tried (**≥83.6 %**). What is not: the value `93/7`.

### The caveat — corrected twice, in both directions

**B is deliberately off-shell:** deleting a term breaks the first-class algebra
`FINDING_P73` proved, so B violates the `0i` constraint at **6.8×10⁻²**.

> **First correction — my original caveat was wrong in kind.** It compared that
> `6.8×10⁻²` (a *normalised constraint residual*) with the `6.6×10⁻²` *direct
> share of ε* and concluded the split was unresolvable. A reviewer pointed out
> these are **different quantities**; the matching digits are a coincidence of
> magnitude, not a systematic-versus-signal comparison. Correct.
>
> **Second correction — but the pessimism was still partly right, for another
> reason.** The proper measurement is the *linear response*: partial ablation
> gives slope `0.003019` with `0.94 %` residual, and the constraint violation
> scales as `(1−f)` to `8.7×10⁻¹⁵` at `f=1`. **At fixed protocol the split is
> clean.** What is *not* clean is the protocol: varying B's start time moves the
> direct share `6.61 % → 16.39 %`.
>
> **Net:** the direct term is resolved *within* a protocol and unresolved
> *across* protocols, and the protocol dependence dominates. The dominance of the
> background survives both (≥83.6 %); the number `93/7` does not.

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
> test — this project's own Cheapest-Differentiating-Test rule.
>
> ### ⚠️ And the diagnosis was worse than "non-discriminating" — it measured the wrong run
>
> The sign-count above was taken on the **`ĝ=0` reference**. The ratio blows up
> because of the **numerator**, which was never examined. Counted properly:
>
> | k | crossings, `ĝ=0` (ref) | crossings, `ĝ=0.5` (numerator) |
> |---|---|---|
> | 1.0 | 1 | **~160**, between `t=5.9×10⁶` and `10⁸` |
> | 10 | 1 | few |
>
> And moving the anchor does **not** help: `|G−1|` at `k=1` runs
> `3.27×10¹⁰ → 3.25 → 3.23 → 3.21 → 2.68×10¹⁰` across `A₁` from `t=10³` to `10⁷`.
>
> **P76's "near-zero contrast at an anchor, probably fixable by moving it" is
> WRONG and is retracted.** The `k=1` *coupled* run oscillates violently through
> zero at late times. The exclusion of `k ≲ 1` stands — **for a completely
> different reason than either file recorded.**
>
> A separate mechanism was also checked and **excluded**: `contrast()` divides by
> `ρ_phys = ρ_A(1−ĝφ̄)`, but `min(1−ĝφ̄) = 0.87` over eight decades. That
> incidentally closes an older open item — **`FINDING_P65`'s `x=1` surface is not
> approached in any run here.**

---

## Verdict

| axis | pre-registered outcome | result | after review |
|---|---|---|---|
| regime | S1 / S2 / S3 | **S3** — saturating spectrum, 7 stable k | **strengthened** — `ε(1000)` increment `1.2×10⁻⁶` |
| anchor | ANCHOR FAIL? | **passed** (0.65 %), 0.2 % low bias | **strengthened** — local slope exactly anchor-free (9 digits) |
| lever ×0.1…×10 | — | FAILED at k=10 | **over-strict** — `×10` is kination-dominated, a different cosmology; `k=10` reinstated for matter-dominated starts |
| attribution | withdraw if bg dominates | withdrawn — 93 % background | **withdrawal stands, the number does not** — direct share `6.6 %→16.4 %` with protocol |
| `k_J` cross-check | — | claimed consistent, `[INFERRED by eye]` | **FALSIFIED** — fitted `k_J = 0.954` vs `√3`; struck |
| pole at `k ≲ 1` | — | "test did not discriminate" | **worse — it measured the wrong run.** Exclusion stands, reason replaced |

**Survives:** the spectrum `ε(k)` and its saturation at `ε_∞ = 0.046758`;
rtol-independence to `1.3×10⁻¹¹`; even parity in `ĝ`; `μ_tot ≡ 1`, so Einstein
gravity is untouched; and — after correction — the `k=10` corner, scoped to
matter-dominated initial data.

**Withdrawn from P76:** "fifth force" (the *framing*, not the split's size),
"quadratic scaling" (leading order only, `D = 0.148`).

**Withdrawn from THIS file:** the `k_J` cross-check (falsified), the "corner is
`k ≳ 30`" reframing (over-strict), the `93/7` number (protocol-dependent), and
the pole diagnosis (measured the wrong run).

```
ε_local(k=10) = 0.04579,   ε_∞ = 0.046758
  a saturating, rtol-stable, anchor-free, even-in-ĝ growth-index shift,
  ≥83.6 % BACKGROUND-MEDIATED, stable across matter-dominated starts,
  ill-posed for k ≲ 1 because the COUPLED run oscillates through zero
```

---

## What this does NOT establish

1. **Anything observational.** No calibration of `k` to `h/Mpc`, no data
   comparison; **`NO_BRIDGE_FITTING` remains in force**.
2. **The size of the direct force** — resolved within a protocol (0.94 %),
   unresolved across protocols (2.5×). The bound `≥83.6 % background` is what
   holds.
3. ~~That the transition scale is `k_J`~~ — **falsified**, not merely untested.
4. **Why the `k ≲ 1` coupled run oscillates.** The *fact* is measured (~160 zero
   crossings); the *mechanism* is not identified.
5. **Anything at other `λ`** — only `ĝ` was scanned.
6. **Anything about MULTING itself** (Gate 1): the completion is *ours*.

---

## Skeptic Verdict (Step 8a)

**Not yet run on P77 itself.** P77 *is* the adversarial pass on P76, built from a
context-blind review plus an outside reading; running a further review on the
attack file is the natural next step and has not been done. Recorded as an open
item rather than claimed as complete.
