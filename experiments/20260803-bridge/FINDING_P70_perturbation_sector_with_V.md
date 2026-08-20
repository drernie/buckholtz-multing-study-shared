# FINDING P70 — the perturbation sector with `V≠0`: `V` breaks the *background* machinery but not the *perturbation* machinery, and the screening it introduces is **intermittent**

**Status:** Skeptic-reviewed (Step 8a) and corrected. Verdict **WEAKENED**.
Two withdrawals: this file's own first headline (self-caught), and its claim
about the `Ψ_k` blocker (skeptic-caught, confirmed by computation). Two of the
reviewer's four concerns were dismissed with data they could not run.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P70_perturbation_sector_with_V.py`

---

## Why this, and why it is pre-registered

`FINDING_P69` concluded that the perturbation sector — derived throughout at
`V=0` — must be redone before any `μ` or `γ` result from that arc can be quoted.

This is **not** a step invented after a null result. `FINDING_P57` names it in
its own text: it verified that linearising `V′(φ)=λφ³` gives
`V″(φ̄)δφ = 3λφ̄²δφ` exactly, and recorded that adding this to the LHS was
*"not built here, an explicit future step, needed before this equation can be
called the field equation of the full committed monopole action."* P70 is that
step.

---

## A. The `ε¹` equation, re-derived with `V`

Re-derived from the covariant equation rather than patched onto P57's result, so
that the `λ=0` check is a genuine reproduction test rather than a tautology.

**Positive control:** at `λ=0` the `ε¹` equation reduces to `FINDING_P57`'s
equation **exactly** — zero symbolic residual by direct subtraction.
`[VERIFIED-SYMPY]`

**What `V` adds:**

```
+ V″(φ̄)·δφ  =  + 3λφ̄²·δφ          and nothing else
```

**Structural check, and it is the main result of Part A:** the added term
contains **neither `Φ` nor `Ψ`**. `V` is not metric-dependent, so it cannot
source new gravitational couplings — the extension is a **pure mass term**.

**Consequence, stated at the width it actually supports** *(narrowed after
review — the first draft said "the perturbation machinery" and that was too
broad)*: `V≠0` breaks the **background** machinery (P69: the first integral) but
leaves the **scalar equation of motion's** `Φ,Ψ` structure intact, so P57's
analysis *of that equation* survives unchanged. It does **not** follow that the
whole perturbation sector is untouched — `V` does source the Einstein equations
through `δT_μν`, see §E.

---

## B. `V″` is a mass: an exact Yukawa transfer function

In `k`-space, quasi-static:

```
(k²/a² + m_eff²)·δφ_k = ĝ·δρ_k + [Φ,Ψ source],      m_eff² = 3λφ̄²
```

Dividing by the `V=0` solution gives, exactly:

```
T(k) = k² / (k² + a²m_eff²)          T(k→∞)=1,  T(k→0)=0
```

Every modification carried by `δφ` is multiplied by `T(k)` relative to the `V=0`
sector. This follows from the **field equation alone**. At `V=0` the scalar was
massless and therefore infinite-range; that was an artifact of the truncation.

**⚠️ DEMOTED after review.** The reviewer's sharpest observation: the three
`k`-regimes *partition* `k`, and this file disqualifies all three.

| regime | `T(k)` | what it multiplies | status |
|---|---|---|---|
| `k ≫ k_J` | → 1 | unchanged | D1 already ruled out — **nothing new** |
| `k ≪ k_J` | → 0 | a `V=0` answer that may itself be 0 (D2) | **no residual manufactured** |
| `k ~ k_J` | O(1) | the only novel regime | **quasi-static known violated** (§C) |

Their phrasing — *"the file derives a formula and then disqualifies every regime
where it would matter"* — is accurate. The formula is correct; its useful domain
is **not established**. Recorded as a **derived formula awaiting a
time-dependent treatment**, not as a standing result.

---

## C. ⚠️ My own first headline was wrong, and the correction is the better result

**What I first claimed and have withdrawn.** `FINDING_P69` found the attractor
`φ̄ → (ĝρ_A/λ)^{1/3}`, and with `ρ_A = C/a³` the scale factor cancels in
`a·m_eff`, giving a **constant comoving screening scale**
`k_J = √3·λ^{1/6}·(ĝC)^{1/3}`. The algebra is right — `a` genuinely cancels,
verified at four spread points to `<10⁻¹²`.

**But the premise is false.** `φ̄` does **not** settle onto the attractor.
Checked directly against the integrated background:

| ĝ | λ | zero crossings of `φ̄` on `t∈[1,10⁵]` | `φ̄/φ_eq` range after `t=10³` |
|---|---|---|---|
| 1.0 | 1 | **21** | `[−0.667, +1.780]` |
| 1.0 | 10⁻² | **10** | `[−1.123, +1.935]` |
| 0.1 | 1 | **15** | `[−2.224, +2.571]` |

`φ̄` **oscillates through zero**, tens of times, and never converges to `φ_eq`.
So `m_eff = √(3λ)|φ̄|` **vanishes periodically** and there is **no constant
screening scale**.

*How I caught it:* the numeric check I had written to confirm `k_J` failed —
`a·m_eff` read 0.169 at `t=10³` and 1.075 at `t=10⁴` against a predicted 1.732,
i.e. not converging. Rather than loosen the tolerance I asked what `φ̄` was
actually doing, and found it oscillating. The failing assertion was correct and
the claim was wrong.

**What is actually true, and it is more interesting.** `a·m_eff` becomes
asymptotically **periodic with a constant comoving envelope** — the
scale-factor cancellation is real, it fixes the *envelope*, not the value:

| ĝ | λ | last 4 peaks of `a·m_eff` | drift per period | mean/`k_J` |
|---|---|---|---|---|
| 1.0 | 1 | 1.1558, 3.0787, 1.1558, 3.0787 | **2.4×10⁻⁵** | 1.222 |
| 1.0 | 10⁻² | 1.5504, 0.9026, 1.5499, 0.9025 | **5.7×10⁻⁵** | 1.525 |
| 0.1 | 1 | 1.7846, 2.0640, 1.7845, 2.0639 | **6.0×10⁻⁵** | 2.393 |

Same-parity peaks repeat to better than `10⁻³` per period across decades. (The
peaks alternate between two values because `φ̄`'s positive and negative
excursions are asymmetric.)

**Robustness [skeptic-demanded].** The reviewer argued the `2×10⁻⁵` drift could
be **log-grid aliasing** — at `t=10⁵` a 200k log grid has spacing ≈5.8, so an
`O(1)` period would be undersampled. Re-measured:

| grid / rtol | drift (ĝ=1, λ=1) |
|---|---|
| log 2×10⁵ pts, rtol 10⁻¹² | 2.396×10⁻⁵ |
| log 2×10⁶ pts, rtol 10⁻¹² | 2.392×10⁻⁵ |
| **linear** 2×10⁶ late, 10⁻¹² | 2.392×10⁻⁵ |
| linear 2×10⁶ late, rtol 10⁻⁸ | 2.398×10⁻⁵ |

Identical to **three significant figures** across a 10× grid refinement, a
log→linear grid change, and a 10⁴× tolerance change. **Not an aliasing or
integrator artifact — concern dismissed with data.** Their arithmetic assumed an
`O(1)` period; it is not — only ~21 peaks occur over five decades, so the period
grows with `t` and the log grid is in fact the appropriate one. Their *premise*
was wrong, not their logic.

**Structural consequence: the screening is INTERMITTENT** — at each zero
crossing `m_eff` vanishes and the Yukawa suppression switches off.

**⚠️ Downgraded after review.** An earlier draft called this a *"distinctive
phenomenology"*. It is **not**, on this evidence: the crossings are a
**measure-zero set in time** and contribute **nothing** to any time-integrated
observable. "Momentarily massless" describes the algebra, not a predicted
effect. Establishing observable consequences needs a time-dependent
mode-equation treatment — an oscillating quartic condensate sourcing
perturbations is the standard **preheating** setup, with its own resonance
analysis and literature. This file performs none of it. Honest status:
**an unresolved regime, not a prediction.**

---

## D. `λ^{1/6}` — what survives

`k_J` survives as the **envelope** scale, so the compression argument survives as
a statement about a scale rather than a value: `λ`'s 10.54 allowed decades
(P69's bound) map to **1.76 decades** of `k_J` — exactly a factor 6, by
construction.

**Honest limit:** the factor 1.2–2.4 scatter between `k_J` and the actual
envelope is itself ~0.3 decades, which is *not* negligible against 1.76.

---

## E. What this settles for `FINDING_P60`'s D1/D2/D3

- **D1** (a genuine leading modification survives, `lim_{k→∞} μ ≠ 1`) was ruled
  out at `V=0`. Since `T(k→∞) = 1`, the `k→∞` limit is **unchanged**. **D1 stays
  ruled out** — no revival.
- **D2 vs D3** was undecided, blocked on `Ψ_k`. `V≠0` introduces a *definite*
  new `k`-dependence with a computable scale — structurally a D3-type
  signature — **but** `T(k)` *multiplies* whatever the `V=0` sector delivered.
  If that was identically zero (D2), then `T(k)·0 = 0`. **A transfer function
  cannot manufacture a residual out of nothing.** So `V≠0` does **not** decide
  D2 vs D3.
- **Does `V` help close `Ψ_k`?** ⚠️ **My first answer was WRONG and is
  withdrawn.** I argued: Part A shows `V` adds no `Φ/Ψ` coupling, therefore it
  cannot alter `FINDING_P61`'s constraint structure. **That inference skips a
  sector.** Part A is about the *scalar EOM*. But `V` also enters the scalar
  *stress-energy*, which sources Einstein — computed:

  ```
  V-piece of δT₀₀ = +λφ̄³δφ = +V′(φ̄)δφ
  V-piece of δT_ii = −λφ̄³δφ     (equal and opposite, as expected for a potential)
  ```

  Both nonzero. **The Einstein constraints `Ψ_k` must satisfy ARE modified by
  `V`.** Whether that helps or hurts closure is **open** and needs P61's chain
  redone with these sources — which this file does not do.

**Negative control:** `λ<0` gives `m_eff²<0`; `T(k)` then has a finite-`k` pole
and **changes sign** across it (`−0.333` below, `+1.333` above) — an unmistakable
instability signature. The formalism detects the wrong-sign case rather than
silently returning something plausible.

---

## What this does NOT establish

1. **`μ(a,k)` itself.** `T(k)` multiplies the `V=0` sector's answer, which is
   still unknown at finite `k` because `Ψ_k` is unclosed.
2. **D2 vs D3.**
3. **That `k_J` is observable.** It is a comoving scale in *our* units
   (`G_N=C=1`, P62's `B=D=1`); mapping to `h/Mpc` needs a calibration not done
   here.
4. **`T(k)` as a *static* filter.** It is exact in the quasi-static limit for a
   given *instantaneous* `m_eff` — but Part C shows `m_eff` oscillates on the
   very timescale that sets the screening scale. Near `k ~ k_J` the static
   reading is **not justified**. This is no longer hypothetical: the assumption
   is known to be violated exactly where the effect lives. A time-dependent
   treatment of the `δφ` mode equation is the next step, and this file does not
   attempt it.
5. **That the quartic is the right `V`** — P45 called it minimal, and its own
   review retracted part of the case for quartic *specifically*.
6. **Anything about MULTING itself** (Gate 1): `V` is *our* construction.

---

## Verdict

**One structural result, two withdrawals, two dismissals.**

**Structural (survives):** the `ε¹` equation with `V` is exactly P57's plus
`+3λφ̄²δφ` and nothing else — verified by reproduction, not patching. The
*scalar EOM's* `Φ,Ψ` structure is untouched by `V`.

**Withdrawal 1 (self-caught):** this file's own first headline — a *constant*
comoving screening scale — was **wrong**. The algebra was right; the premise
(that `φ̄` settles on P69's attractor) was not. `φ̄` oscillates through zero.
Caught by its own failing numeric assertion, not by loosening it.

**Withdrawal 2 (skeptic-caught, confirmed by computation):** the claim that the
`Ψ_k` blocker is *untouched* by `V`. `V` sources `δT₀₀` and `δT_ii` with
`V′(φ̄)δφ`, so the Einstein constraints `Ψ_k` must satisfy **are** modified. I
had generalised a scalar-EOM result to a sector the file never computes.

**Dismissed with data (the reviewer could not run code):** the envelope drift is
grid- and tolerance-independent to three significant figures; and it is not
integrator noise.

**Demoted:** `T(k)` — a correct formula whose every `k`-regime this file's own
caveats disqualify. **Not a standing result.**

**Net for the programme.** The redo is *begun*, not finished. What is solid is
the corrected `ε¹` equation. What P69 asked for — a perturbation sector safe to
quote `μ`/`γ` from — is **not** delivered, and the obstacle is now sharper than
before: `Ψ_k` was already unclosed at `V=0`, and `V` **adds** source terms to
the very constraints it must satisfy. The next step is P61's constraint chain
redone with `δT_μν(V)` included.


---

## Skeptic Verdict (Step 8a)

Context-blind review: finding.md + source only. The reviewer had **Read+Edit
only, no execution**, and said so plainly — marking every prediction as their
own hypothesis rather than a finding. I ran all three of their proposed tests.

**Verdict: WEAKENED.** Two concerns confirmed, two dismissed with data.

| # | Concern | Sev | Response |
|---|---|---|---|
| 1 | "`V` adds no `Φ/Ψ` coupling ⟹ `Ψ_k` blocker untouched" skips the Einstein sector | MOD | **CONFIRMED — claim WITHDRAWN.** Computed `δT₀₀` and `δT_ii`: both gain `V′(φ̄)δφ`, equal and opposite. The constraints `Ψ_k` must satisfy **are** modified. I had generalised a scalar-EOM result to a sector the file never computes. |
| 2 | envelope drift `2×10⁻⁵` may be log-grid aliasing (spacing ≈5.8 at `t=10⁵`) | HIGH | **DISMISSED with data.** Identical to 3 s.f. across log-2×10⁵ / log-2×10⁶ / **linear**-2×10⁶ grids. Their premise — an `O(1)` period — was wrong: only ~21 peaks in five decades, so the period grows with `t` and the log grid is the appropriate one. |
| 2b | drift may sit at the integrator's noise floor | HIGH | **DISMISSED with data.** Varying rtol `10⁻⁸→10⁻¹²` (10⁴×) moves the drift by 0.25 %. |
| 3 | "intermittent screening / momentarily massless" is measure-zero and over-dramatised | MOD | **ACCEPTED.** Downgraded to a structural statement plus an explicitly unresolved regime; noted that the proper treatment is the preheating-style mode analysis, which this file does not perform. |
| 4 | `T(k)`'s three `k`-regimes are *all* disqualified by the file's own caveats ⟹ self-cancelling | HIGH | **ACCEPTED.** `T(k)` demoted from result to "derived formula awaiting a time-dependent treatment", with the three-regime partition stated explicitly in §B. |

Every concern was tested by standalone computation before being accepted or
dismissed (`audit-verification-gate.md`). Note the pattern, identical to P69:
the reviewer's **process instinct** on #1 was right even though their **#2
arithmetic** was wrong. Both halves matter — a reviewer can be wrong about the
specifics and still be pointing at a real hole.
