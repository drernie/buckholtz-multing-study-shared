# FINDING P69 — the P65–P67 pathology is an artifact of the `V=0` truncation, and the campaign's own prior potential removes it

**Status:** Skeptic-reviewed (Step 8a) and corrected. Verdict **WEAKENED** →
all four concerns tested by computation the reviewer could not run. Outcome:
**one CONFIRMED (and it overturned my own first dismissal of it), two dismissed
with data, one accepted as a framing correction.**
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P69_potential_restores_stability.py`

---

## Why this was the last remaining route

`FINDING_P67` ruled out backreaction-driven stabilisation at `O(ĝ)`.
`FINDING_P68` ruled out escaping it by changing the mass law — the linear and
exponential laws coincide exactly at `O(ĝ)`. That left **one** untouched
assumption from the whole P65–P68 arc: `V(φ̄)=0`.

---

## Provenance — the *opposite* of P68's

`V=0` is not what the source has. It is a **truncation this campaign imposed
for tractability**, and said so in its own text:

- `FINDING_P57`: "a `V=0` truncation (kinetic + monopole `g`-sector only),
  excluding `FINDING_P45`'s own `λ₄φ⁴/4` potential"; `FINDING_P58`: same label.
- `FINDING_P45` established that quartic on **independent grounds** — a
  canonical no-potential scalar is a *forced stiff fluid* (`w_φ=1`), and `λ>0`
  is the minimal escape, giving `m_eff² = 3λφ² ≥ 0`.

So restoring `V` **removes** an assumption. P68 had to **add** `φ², φ³, …`
terms absent from the source.

---

## What is established

### A. `V≠0` breaks the first integral P66/P67/P68 all rest on

```
d/dt(a³φ̄̇) − ĝC = −a³·V′(φ̄)          [VERIFIED-SYMPY]
a³φ̄̇ = √2 + ĝ(t−1) − ∫₁^t a³V′ dτ
```

**Stated before any result:** P66's perturbative construction, P67's fate
criterion, and P68's `O(ĝ)` equivalence all rest on that first integral being
exact. **None of them transfer.** Positive control: `V=0` restores
`d/dt(a³φ̄̇)=ĝC` identically, so this generalises P66–P68 rather than
contradicting them.

### B. Two mechanisms, kept separate

- **Mechanism 1 — restoring force.** `V′>0` subtracts directly from the driving
  term in the numerator; needs no change to the expansion.
- **Mechanism 2 — Λ-like expansion.** `V>0` raises `H`, growing `a³`. But a `V`
  that drives the expansion **is** dark energy — self-defeating for a non-ΛCDM
  model.

### C. The attractor decays

`V′=λφ³` ⟹ `φ_eq = (ĝρ_A/λ)^{1/3}`, and with `ρ_A = C/(6πt²)`:
`φ_eq(t)/φ_eq(1) = t^{−2/3}` `[VERIFIED-SYMPY]`. The source dilutes while the
restoring force does not, so `x` is driven toward **zero**. Also
`x_eq³ = ĝ⁴ρ_A/λ`.

### D. Numerics — every `λ>0` turns over

**Positive control** (`λ=0`), run only where P67's `x≪1` condition holds:

| ĝ | `x(10⁶)` | `dx/dln t` | P67 predicts | rel |
|---|---|---|---|---|
| 0.01 | 0.000832 | 5.3124×10⁻⁶ | 5.3092×10⁻⁶ | **0.0006** |
| 0.1 | 0.014518 | 5.3758×10⁻⁴ | 5.3459×10⁻⁴ | **0.0056** |

| λ | `x_max` | `t` at `x_max` | turns over? |
|---|---|---|---|
| 1 | 0.1283 | 1.0×10¹ | **YES** |
| 10⁻² | 0.2149 | 4.5×10¹ | **YES** |
| 10⁻⁴ | 0.3241 | 2.5×10² | **YES** |
| **0** | 1.0485 | still rising at 10⁵ | **no** |

**Negative control:** `λ=−10⁻²` cannot even be integrated — it runs away and
`solve_ivp` fails at `t≈104` with `x≈2×10¹²`, while `λ=+10⁻²` completes and
stays bounded. The stabilisation follows from the **sign** of `λ`.

### E. The pathology is reached far sooner than P67's out-of-scope figure

```
FULL NONLINEAR crossing x=1 at t = 8.1877×10⁴
```

**Mechanism:** positive feedback. As `x→1`, `ρ_phys = ρ_A(1−x) → 0`, matter
drops *out* of the Friedmann equation, `H` falls, `a³` grows more slowly, and
`ẋ = ĝ(…)/a³` **grows**. The approach accelerates rather than creeping
logarithmically.

**[Skeptic-corrected framing.]** My first draft headlined this as "461× earlier
than P67's figure". That is beating a strawman: P67 *explicitly declined* to
extrapolate and flagged the `3.8×10⁷` figure as out-of-scope. The real result is
the **absolute** number and its mechanism, not a scored hit on P67. The 461× is
context for how badly a naive extrapolation would mislead — nothing more.

---

## Skeptic review (Step 8a) — reviewer had no execution tools; I ran their tests

The reviewer flagged four concerns and was explicit that, lacking Bash, all
four were untested hypotheses. I ran all three of their proposed tests.

### Concern 1 (MEDIUM) — "`λ_crit` may be an artifact of a fixed `t_end=10⁶`"

Their reasoning: `t_max ~ λ^{−1/2}`, so near `λ_crit≈10^{−10.54}` the turnover
would sit at `t≈4.7×10⁵`, at the window edge, making `x_max_of` return `x(10⁶)`
rather than the true maximum.

**Tested with an adaptive `t_end` (×100 until the peak is interior), at ĝ=1:**

| λ | `x_max` @ fixed 10⁶ | `x_max` adaptive | peak interior? |
|---|---|---|---|
| 10⁰ … 10⁻¹² | *identical at every λ* | *identical* | **YES at every λ** |

`x_max` is **monotone** in λ (0.1283 → 2.8908 as λ runs 10⁰ → 10⁻¹²), and
re-bisecting returns **`λ_crit = 10^{−10.54}` — ratio 1.00×**. Their
`t_max ~ λ^{−1/2}` scaling over-estimated the turnover times *at ĝ=1*.

**⚠️ CORRECTION TO MY OWN DISMISSAL.** I first wrote this up as "dismissed by
computation" — that was **over-broad, because I tested only ĝ=1**. On adding
the interiority assertion the reviewer's process point demanded, it **fired
immediately** at a case I had not scanned:

```
AssertionError: peak not interior at lambda=1e-12, g=0.5:
                argmax at index 3999 of 4000 -- x_max is truncated
```

So **Concern 1 is CONFIRMED at ĝ=0.5**, exactly the failure mode described,
even though it does not occur at ĝ=1. `x_max_of` is now genuinely **adaptive**
(extends `t_end` ×100 until the peak is interior) rather than merely asserting.
With that fix the ĝ=0.5 bisection completes and reports no crossing in
`λ ∈ [10⁻¹², 10²]`, and ĝ=1 still gives `λ_crit = 10^{−10.54}` — so the
*conclusions* are unchanged, but they are now computed rather than truncated.

The reviewer's framing — "correct by luck, not by construction" — was exactly
right, and the check they demanded found a real case within minutes of being
added.

### Concern 2 (LOW) — "the ablation may be uncalibrated, not discriminating"

Fair: a near-null shift could mean "mechanism 2 absent" *or* "this diagnostic
cannot see mechanism 2". **Ran their positive control** — insert a genuine
constant `Λ_bg` and ablate *that*:

| `Λ_bg` | `Λ/ρ_A` at turnover | `x_max` with | `x_max` ablated | shift |
|---|---|---|---|---|
| 0 | 0 | 0.324107 | 0.324107 | +0.00 % |
| 10⁻⁷ | 0.12 | 0.323099 | 0.324107 | +0.31 % |
| 10⁻⁶ | 1.18 | 0.315278 | 0.324107 | +2.80 % |
| 10⁻⁵ | 11.78 | 0.278829 | 0.324107 | **+16.24 %** |

Versus **+0.30…+0.60 %** for removing `V`. A dominant Λ produces a signal
**27–54× larger**, so the diagnostic *can* see mechanism 2 and its near-null
result for `V` is informative, not vacuous. **DISMISSED.**

*Honest limit they were right about:* at *comparable* magnitude (`Λ/ρ≈1.2`) the
shift is only 2.80 %, so the discriminator is sharp but not enormous. One
asymmetry works in the conclusion's favour: `V=λφ⁴/4` **decays** as `φ` decays
while `Λ_bg` is constant and compounds — so `V` is even less Λ-like than its
energy fraction at one instant suggests.

### Concern 3 (LOW-MED) — "`t=8.19×10⁴` may be a solver artifact; `461×` is a strawman"

**Ran the solver sweep:**

| method | rtol=10⁻¹¹ | rtol=10⁻¹³ |
|---|---|---|
| RK45 | 8.1877×10⁴ | 8.1877×10⁴ |
| LSODA | 8.1877×10⁴ | 8.1877×10⁴ |
| Radau | 8.1877×10⁴ | 8.1877×10⁴ |

All six agree to **five significant figures**. **Numerically DISMISSED.**

**Rhetorically ACCEPTED** — the `461×` framing was a strawman comparison and has
been rewritten (see Part E above). This is the one concern that changed the text.

### Concern 4 (MEDIUM) — "AOG 5/5 is generous"

- **AOG-1.** They argue PARTIAL: P45 pre-registered the *form*, not the claim
  that it resolves *this* pathology. I keep **PASS** on the criterion as
  written — AOG-1 asks whether the *modification* was predictable before the
  null, and this one was not merely predictable but **already written down**
  months earlier. Whether its *consequence* was predicted is what AOG-3 asks.
  Their narrower reading is recorded here so a reader can apply it.
- **AOG-5.** Their objection was **conditional**: "if `λ_crit` is genuinely
  tiny, no tuning; if not, this is tuning a free parameter." Concern 1 resolved
  that condition — `λ_crit = 10^{−10.54}`, so the safe region spans **more than
  ten orders of magnitude** below the natural `O(1)` value. That is the opposite
  of fine-tuning, which requires a *narrow* window. **PASS stands.**
- **Their deeper methodological point, which I accept and record:** "restoring a
  truncation" is close to a free pass for *any* prior-invoked term, so AOG-5 is
  weaker as a discriminator than its clean PASS suggests. The contrast with P68
  (which had to add non-source terms and failed AOG-5) is real, but AOG-5 should
  not be treated as strong independent evidence on its own.

**Score: 5/5 as written; 4/5 under their narrower AOG-1 reading. The promotion
decision is unchanged either way** — `[HYPOTHESIS]`, not promoted, because
Perelman condition 5 (external reconstruction) is not met.

---

## Self-caught bugs, before skeptic contact

1. **Control applied outside its own regime.** The `λ=0` positive control first
   ran at `ĝ=1` over `t=10⁴…10⁵` and failed (`rel=1.82`). P67 holds only while
   `x≪1`, and at `ĝ=1` that window ends near `t≈6`. Same class as P67's own
   bug 1. *This bug is what surfaced result E.*
2. **Negative control asserted the wrong signature.** Asserted
   `x_end(λ<0) > x_end(λ>0)` and crashed, because for `λ<0` the integrator never
   *reaches* `t_end`. The failure **is** the destabilisation signal.
3. **Arbitrary threshold masquerading as a test.** Part F asserted
   `V/ρ_total < 0.1` and failed at `λ=1` (0.123). But 12 % is not
   Λ-domination — the test drew a line rather than discriminating. Replaced with
   the ablation, which the skeptic then correctly asked me to calibrate.
4. **[During skeptic verification]** My first `Λ_bg` positive control put
   `Λ_bg = ρ_A(t=1)` and integrated to `t=10⁵`. A constant Λ gives `a ~ e^{Ht}`
   with `H≈0.685`, so `a³ ~ e^{2×10⁵}` — guaranteed overflow. Test-design bug,
   not a finding; fixed by scaling `Λ_bg` to `ρ_A` at the *turnover* epoch.

5. **Over-broad dismissal of a skeptic concern.** I first reported Concern 1
   as "dismissed by computation" after testing only ĝ=1. The assertion the
   reviewer asked for then fired at ĝ=0.5, λ=10⁻¹². Corrected above; the
   lesson is that dismissing a concern requires scanning the parameter the
   concern is about, not one slice of it.

All documented inline, not silently repaired.

---

## What this does NOT establish

1. **That the quartic is the right potential.** P45 called it a *minimal*
   escape, and its own skeptic review retracted part of the justification for
   choosing quartic *specifically*.
2. **Anything about MULTING itself** (Gate 1) — `V` is *our* construction.
3. **The perturbation-sector consequences.** Everything in P66–P68 was derived
   at `V=0` and does **not** carry over. It must be redone.
4. **That `λ` is determined.** Part E gives a *constraint*, not a measurement.
5. **That the initial conditions are right.** They are P62's `V=0` background
   values, kept for comparability. `V(0)=0` so the `t=1` constraint is
   untouched — but the history *before* `t=1` would differ.
6. **That AOG-5 is strong evidence.** Per the reviewer's methodological point
   above, "removing a truncation" is a weak discriminator in general.

---

## Verdict

**The P65–P67 pathology is an artifact of the `V=0` truncation**, and the
campaign's own previously-established potential removes it — via the restoring
force, not a disguised cosmological constant, at every `λ>0` tested, with the
safe region spanning ten-plus orders of magnitude in `λ`.

Two results deserve equal weight, and the second is uncomfortable:

- the pathology **is removed** by a potential the campaign already had, on
  grounds predating the problem;
- the pathology **is also more real than P67's out-of-scope figure implied** —
  reached at `t≈8.2×10⁴` (solver-independent to five figures), because of a
  positive feedback invisible from inside P67's perturbative window.

**Immediate consequence for the programme: P66/P67/P68's machinery does not
survive `V≠0`**, since the first integral they rest on is broken. The
perturbation sector must be redone with `V` restored before any `μ`, `γ` result
from that arc can be quoted.
