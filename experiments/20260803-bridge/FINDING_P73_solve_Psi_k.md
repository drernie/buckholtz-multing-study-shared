# FINDING P73 — `Ψ_k` solved; and the `μ`-based verdict on it **retracted**

**Status:** built, self-debugged (two real errors), reviewed context-blind,
**one headline retracted after review**, rebuilt around what survives.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P73_solve_Psi_k.py`

> **Read this first.** A draft of this finding was titled *"…and `FINDING_P60`'s
> D2-vs-D3 decided: **D3**"*. **That verdict was wrong and is withdrawn.** The
> reason, the test that killed it, and what remains are all below. The
> constraint-algebra and `Ψ_k` results are unaffected — they were established
> before `μ` was ever computed and do not depend on it.

---

## The chain that made this possible

| | |
|---|---|
| `P61` | built the closed system for `Ψ_k`, found it **not** Bianchi-consistent on a free background. `Ψ_k` left unresolved. |
| `P71` | localised the obstruction **exactly**: `dC/dt|_{C=0} = −Ψ·[Ḣ + 4πG(ρ+p)]`. |
| `P72` | showed P69's background satisfies `Ḣ` **structurally** — it cannot fail there. |
| **P73** | so what does that unlock? |

---

## A. Both constraints are first class — **survives**

**The criterion, corrected.** A first draft demanded `dC₀₀/dt = 0` identically.
**That is the wrong test** — constraints are first class when the derivative of
each is a **linear combination of the constraints**, not when it vanishes.

With the right criterion, and the `Ḣ` equation imposed:

```
dC₀₀/dt  =  −3H·C₀₀  +  (k²/a²)·C₀ᵢ          residual EXACTLY 0
```

Textbook constraint algebra. The other sign choice yields an unrecognisable
mess with nonzero residual, so the selection **discriminates** rather than fits.
`[VERIFIED-SYMPY]`

**Consequence:** impose both constraints once on initial data; the evolution
preserves them. P61's system is **well-posed**, not over-determined — it only
*looked* over-determined on a background where the constraints did not propagate.

---

## Self-caught errors, both real

**1. Wrong first-class criterion** (above). Neither sign passed the wrong test —
which is what forced looking harder rather than concluding "not first class".

**2. Wrong sign in the matter continuity equation** — written from memory. Fixed
by *deriving*: requiring the **scalar** sector's own continuity to be an identity
at `ĝ=0` fixes the sign of the `(k²/a²)Q` term, and mine was wrong. The leftover
at `ĝ≠0` then came out as

```
S_φ = ĝ(δρ_A·φ̄̇ + ρ̄_A·δφ̇)
```

— exactly the first-order form of the exchange term `P71` identified, which is
what confirms the corrected convention rather than merely asserting it.

**Regression check on P71**, run because the corrected sign is one P71 used:
P71's identity `dC/dt = −Ψ·R_Ḣ` holds **for both signs**. The `(k²/a²)Q` term
does not enter the `0i` propagation at all. **`FINDING_P71` needs no
retraction** — but I had to check, not assume.

---

## D. `Ψ_k(t)` — solved. **Survives.**

| k | `\|C₀₀\|` @ t=1 | @ t=10³ | `\|C₀ᵢ\|` @ t=10³ | `Ψ(10³)/Ψ(1)` |
|---|---|---|---|---|
| 0.1 | 0 | 4.9×10⁻¹¹ | 2.1×10⁻¹³ | −2.966 |
| 1.0 | 2.1×10⁻¹⁶ | 6.0×10⁻¹² | 4.8×10⁻¹³ | −2.986 |
| 10 | 6.5×10⁻¹⁷ | 3.0×10⁻¹⁴ | 3.8×10⁻¹⁴ | −7.496 |

Both constraints hold to `<10⁻⁶` relative over three decades of `t`, at every
`k`. **`Ψ_k(t)` is the object `FINDING_P61` left unresolved, and it is now
integrated.**

**Negative control — this is the one that matters.** Same integration on a
background whose KG drag is `3H→2H`, breaking the `Ḣ` equation:

| k | `\|C₀₀\|` @ t=10³ | `\|C₀ᵢ\|` @ t=10³ |
|---|---|---|
| 0.1 | **0.533** | **0.176** |
| 1.0 | **0.085** | **0.100** |
| 10 | **0.170** | **0.159** |

The constraints **drift**, exactly as P71 predicts. **P71's obstruction is not a
formal remark — it is visible in the numerics, and removing it is what makes
`Ψ_k` solvable at all.**

---

## E. `μ(a,k)` — and the retraction

```
μ(a,k) := −(k²/a²)·Ψ / (4πG·δρ_phys)          (P60's Route B reference density)
```

At `t=10³`: **μ = 0.095 (k=0.1) → 0.912 (k=1) → 0.999 (k=10)**.

**I read this as D3** — `μ` is `k`-dependent, therefore a genuine modification —
and wrote that as the finding's headline. **The context-blind reviewer named two
tests that destroy the reading. I ran both. Both come back against me.**

### Test 1 — turn the coupling entirely OFF (`ĝ=0, λ=0`)

| k | μ (`ĝ=1, λ=1`) | μ (`ĝ=0, λ=0`) | coupling signal |
|---|---|---|---|
| 0.1 | 0.095191 | 0.095751 | **0.58 %** |
| 1.0 | 0.912164 | 0.913713 | **0.17 %** |
| 10 | 0.999041 | 0.999056 | **0.00 %** |

**The entire `k`-shape is reproduced with no coupling at all.** It is a
Newtonian-gauge / superhorizon **kinematic** effect present in GR with a free
scalar. What the coupling actually contributes is **≤ 0.58 %** — and that is not
shown here to exceed this setup's own numerical systematics.

The reviewer predicted this quantitatively before I ran it: `k/(aH)` at `t=10³`
is `0.57 / 5.7 / 57` for `k = 0.1 / 1 / 10`, so **`k=0.1` is superhorizon**, and
`|μ−1| ≈ 10⁻³` at `k=10` matches `(aH/k)² ≈ 3.1×10⁻⁴` — the expected GR
gauge correction, not a modification.

### Test 2 — is `μ` converged in `t`?

| t | μ (k=0.1) | μ ratio/decade | `a` ratio/decade |
|---|---|---|---|
| 10 | 0.004749 | | |
| 10² | 0.022255 | 4.687 | 4.755 |
| 10³ | 0.095191 | 4.277 | 4.607 |
| 10⁴ | 0.329686 | 3.463 | 4.633 |
| 10⁵ | 0.695135 | 2.108 | 4.640 |
| 10⁶ | 0.914115 | 1.315 | 4.641 |

**`μ ∝ a` early**, then bends toward 1 as the mode enters the horizon. The
reviewer predicted the ratio `10^(2/3) = 4.64` from `μ ∝ a` and it is there in
the first two decades. **"μ = 0.095 at k=0.1" was a snapshot of a superhorizon
transient**, not a property of the model.

### Test 3 — the comoving-gauge fix I tried, which did *not* work

Substituting a comoving reference density `δρ + 3H·q_tot` gives
μ = 0.050 / 0.839 / 0.998. **It does not go to 1**, so that particular
substitution is not the right correction either. The gauge question is left
**open**, not resolved in either direction.

---

## F. Initial-data independence — real, but does not rescue the verdict

| k | `μ(10³)` across 5 very different datasets | spread |
|---|---|---|
| 0.1 | 0.095130 … 0.095834 | **1.0074×** |
| 1.0 | 0.911844 … 0.912166 | **1.0004×** |
| 10 | 0.999041 … 0.999042 | **1.0000×** |

The attractor is real. **But stability is not meaning:** all five datasets are
positive-sign generic data, so what this shows is growing-mode dominance — and
Test 1 kills the interpretation regardless of how stable the number is. A
reproducible number can be a reproducible artefact.

---

## Verdict

**Survives:**

1. **Both constraints are first class** on an `Ḣ`-satisfying background, with the
   algebra `dC₀₀/dt = −3H·C₀₀ + (k²/a²)·C₀ᵢ`. P61's system is **well-posed**.
2. **`Ψ_k(t)` is integrated**, constraints held to `<10⁻⁶` over three decades at
   `k = 0.1, 1, 10`. The object P61 left unresolved now exists.
3. **P71's obstruction is visible in numerics** — the negative control drifts by
   `O(0.1)` on an `Ḣ`-violating background.
4. The corrected continuity sign, *derived* and cross-checked against P71's
   exchange term, with P71 confirmed to need no retraction.

**Retracted:**

- **`FINDING_P60`'s D2-vs-D3 is NOT decided by this file.** It reverts to
  **open** — but now with a *named* reason: `μ` as computed here needs (a) a
  gauge-correct reference density and (b) evaluation at converged `t`, and
  neither is settled.
- The number `μ = 0.095` as a statement about the model.
- **D1 also loses its support here.** `μ→0.999` at `k=10` was cited as ruling D1
  out; since the same behaviour appears with the coupling off, this file no
  longer bears on D1 either way. (D1 was already ruled out on other grounds in
  `FINDING_P60`; that is untouched, but P73 adds nothing to it.)

---

## What this does NOT establish

1. **Any verdict on D2 vs D3.** See above.
2. **That the ≤0.58 % coupling signal is real.** It is not shown to exceed the
   integrator's own systematics; treat it as an upper bound on the effect at
   this `(ĝ, λ)`, not as a detection.
3. **That the relative 00/0i sign was *derived*.** It was **selected** by the
   closure test — nontrivial and discriminating, but not a Christoffel
   computation and not presented as one.
4. **Anything at `k` outside `[0.1, 10]`.** Constraint preservation is stated for
   `t ≤ 10³`; only the single `μ` diagnostic of Test 2 ran to `t = 10⁶`.
5. **That `k` here maps to `h/Mpc`.** Comoving units of *our* construction
   (`G_N=C=1`, P62's `B=D=1`); no calibration performed.
6. **That P69's background is the *right* one** — only that it is internally
   consistent, with P45's *minimal* quartic.
7. **Anything about MULTING itself** (Gate 1): `V` is *our* construction.

---

## Skeptic Verdict (Step 8a)

**`[FALSIFIED]` — with rescue paths.** Review was context-blind (`claim.md` +
code only, no session history, per FL Context Asymmetry). The reviewer had Read
but not Bash, and correctly flagged its own numerical predictions as hypotheses
rather than results — **I ran all three tests myself before accepting anything.**

| # | Concern | Independently re-checked | Response |
|---|---|---|---|
| 1 | `μ`'s `k`-shape is kinematic, not a modification — `k=0.1` is superhorizon (`k/aH = 0.57`) | **CONFIRMED.** Coupling switched fully off reproduces the shape; residual ≤0.58 % | **ACCEPTED — headline retracted.** Test 1 now runs in-file with an assert |
| 2 | `μ` is a transient (`μ ∝ a`), not converged at `t=10³` | **CONFIRMED.** Ratio 4.687→4.277 vs `a`'s 4.755→4.607; `μ→0.914` by `t=10⁶` | **ACCEPTED — the number retracted.** Test 2 now runs in-file |
| 3 | `\|μ−1\| ≈ 10⁻³` at `k=10` is the expected GR gauge correction `(aH/k)² ≈ 3.1×10⁻⁴` | **CONFIRMED in magnitude** by Test 1 (the same `10⁻³` appears with no coupling). My comoving substitution did **not** return `μ→1`, so the exact form is unsettled | **ACCEPTED as to conclusion, open as to mechanism.** Test 3 reported with its negative outcome |
| 4 | Part F's five datasets are all positive-sign generic data ⇒ "attractor" is growing-mode dominance | **ACCEPTED without a separate test** — Test 1 makes it moot, and the criticism is correct on its face | **ACCEPTED.** Part F now states it does not rescue the verdict |

**Kill assessment.** The reviewer's own fallback names what survives: the
constraint-algebra result and the negative-control demonstration of P71's
obstruction. Those were established **before** `μ` was computed and are
independent of it — so this is a **retracted headline, not a dead finding**.
The core predicate of the *surviving* claim ("`Ψ_k` is solvable once `Ḣ` holds")
was never challenged.

**AOG (revision after a null result):** no hypothesis was relaxed to save
anything — a claim was **removed**, and the underlying question returned to open.
AOG does not apply; nothing was promoted.

**Perelman condition 5 (external reconstruction):** still **not met**, as
throughout this campaign.
