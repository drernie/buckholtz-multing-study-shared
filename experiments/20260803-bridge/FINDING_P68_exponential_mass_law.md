# FINDING P68 — the exponential mass law removes the pathology, but it is a *different* completion, and an honest AOG puts it at `parked`

**Status:** Skeptic-reviewed (Step 8a) and corrected. Verdict CONFIRMED-REAL with a
**medium-severity honesty issue on the AOG scoring**, which was my own — re-scored
downward after independent verification.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P68_exponential_mass_law.py`
**Final status: `parked`** (not `weak_alive`, not `alive`).

---

## Why this was next

`FINDING_P67` established that `x := ĝφ̄` grows logarithmically without bound for
any `ĝ≠0`, and that backreaction does **not** stop it at `O(ĝ)`. Under the
**linear** mass law `m/m₀ = 1−x` that is fatal at `x=1`: `ρ_phys = (1−x)ρ_A`
vanishes and then changes sign. The exponential law `m/m₀ = e^{−x}` never crosses
zero, and agrees with the linear law at `O(ĝ)` — so nothing already computed
would be lost.

That is the attractive story. Checking it changed how it must be reported.

---

## The provenance check comes first, and it is load-bearing

The linear law is **not** a convenience we may swap. `FINDING_P33` established it
is **exact** given the source's own interaction term, itself linear in `φ`:

```
S/dτ = −m·c + g·m·φ      ⟹      m_eff/m = 1 − (g/c)·φ      exactly
m_exp/m₀ − m_lin/m₀ = +(1/2)ĝ²φ² − (1/6)ĝ³φ³ + (1/24)ĝ⁴φ⁴ − …
```

First difference at `O(ĝ²)` (asserted). Those are worldline self-interaction terms
**not present in the source**. `[VERIFIED-SYMPY]`

### The skeptic attacked exactly this, and the attack half-succeeded

The reviewer proposed `φ = (1/g)(1 − e^{−gχ})`, which turns the **linear** mass
law into an exponential one with **no added worldline terms**:

```
1 − g·φ  =  e^{−gχ}        ✓ verified symbolically
```

On the worldline term alone, the attack **lands**. It is defeated only by the
kinetic term:

```
∂φ = e^{−gχ}∂χ    ⟹    (1/2)(∂φ)²  →  (1/2)e^{−2gχ}(∂χ)²     NON-canonical
```

So the theory with a **canonical** kinetic term *and* an exponential mass law is
genuinely distinct from the one with a canonical kinetic term *and* a linear mass
law. The added `φ², φ³, …` terms are precisely what cannot be redefined away
while keeping `(∂φ)²/2` canonical.

**The claim survives — but it is convention-relative, and an earlier draft left
that convention implicit.** It is now stated as load-bearing, not decoration.

---

## What survives, and what changes

**Survives.** `d(m/m₀)/dĝ|₀ = −φ` for both laws — identical. Every `O(ĝ)` result
of `P66`/`P67` carries over verbatim, **including P67's negative result**: the
swap does not rescue backreaction-driven stabilisation, because at `O(ĝ)` the two
are the same theory. `[VERIFIED-SYMPY]`

**Changes.** The scalar EOM source is `−(d ln m/dφ)·ρ_phys`:

| law | `d ln m/dφ` | source |
|---|---|---|
| linear | `ĝ/(ĝφ−1)` | `ĝρ_A` |
| exponential | `−ĝ` | `ĝρ_A·e^{−x}` |

The linear row is a **positive control** — it reproduces exactly the `ĝρ_A` used
throughout P62–P67 (asserted). **[Skeptic-caught gloss]** that reproduction
happens via a `0/0`-style cancellation *at the pathological point*: `d ln m/dφ`
diverges at `x=1` while `ρ_phys` vanishes there, and only the product is regular.
Nothing downstream uses the factors separately, so no damage — but any quantity
seeing `d ln m/dφ` alone (a per-particle Yukawa force, say) *would* be singular
where the composite source is not.

The exponential row is the content: the source **suppresses itself**. This is a
*different* stabilisation mechanism from the one P67 ruled out — P67 killed
stabilisation via the **expansion**; this is stabilisation via the **source**.

---

## Consequence: `ln t` becomes `ln ln t` — and converges far more slowly than I first said

Eliminating the momentum from `d/dt(a³φ̄̇) = ĝC e^{−x}` and `ẋ = ĝ(a³φ̄̇)/a³` with
`a³ → 6πt²`, in `s = ln t`:

```
x″ + x′ = k·e^{−x},        k := ĝ²C/(6π)
```

**[Skeptic-caught, and this correction matters.]** An earlier draft went straight
from "the ODE residual of the ansatz is `−1/s²`" to an implied convergence rate.
Those are different quantities. Linearising `x = ln(k·s) + f(s)`:

```
f″ + f′ + f/s ~ 1/s²      ⟹      f = ln(s)/s  at leading order
```

The correction to `x` decays as **`ln(s)/s`**, far slower than `1/s²`. Verified
over four decades, `k=1`:

| s | `diff = x − ln(k·s)` | `diff/[ln(s)/s]` | `diff/[1/s²]` |
|---|---|---|---|
| 10³ | 6.467×10⁻³ | **0.9363** | 6.47×10³ |
| 10⁴ | 8.783×10⁻⁴ | **0.9536** | 8.78×10⁴ |
| 10⁵ | 1.109×10⁻⁴ | **0.9631** | 1.11×10⁶ |
| 10⁶ | 1.339×10⁻⁵ | **0.9693** | 1.34×10⁷ |

`diff/[ln(s)/s]` is flat near 1.0; `diff/[1/s²]` varies by four orders of
magnitude. **Refined asymptote: `x = ln(k·ln t) + ln(ln t)/ln t + …`**

Subtracting the correction improves the residual 20.6× → 31.6× across `s=10⁴…10⁶`
(asserted), so the term is real, not curve-fitting.

**Uniqueness [skeptic-added]:** four different initial conditions give `x(10⁴)`
with spread `1.8×10⁻⁴` — the asymptote is an **attractor**, so treating it as
*the* late-time behaviour rather than one of a family is legitimate.

**Negative control:** removing the `e^{−x}` suppression gives `x″+x′=k`, and the
same machinery returns `x → k·s`, linear in `s`, to `10⁻³` relative. So `ln ln t`
is a consequence of `e^{−x}`, not of the integrator.

---

## The pathology is genuinely gone

| x | linear `1−x` | exponential `e^{−x}` | linear status |
|---|---|---|---|
| 0.9 | 0.100 | 0.407 | OK |
| 1.0 | 0.000 | 0.368 | **ρ_phys = 0** |
| 1.5 | −0.500 | 0.223 | **negative mass** |
| 5.0 | −4.000 | 0.0067 | **negative mass** |

`e^{−x} > 0` for all `x`. The `x=1` surface that motivated P65–P67 does not exist
in this completion.

---

## Anti-Overfitting Gate — re-scored downward after review

| # | check | first draft | **corrected** | why |
|---|---|---|---|---|
| AOG-1 | pre-registration | PARTIAL | **PARTIAL** | the *function* was available beforehand; the *motivation* arrived only after the null. |
| AOG-2 | specificity | PASS | **PASS** | one parameter, same as linear; genuinely clean. |
| AOG-3 | novel prediction | ~~PASS~~ | **PARTIAL** | predictions exist, but *this same file* concedes they sit at `t = e^10000` with no observational channel. |
| AOG-4 | non-triviality | ~~PASS~~ | **PARTIAL** | forbids the `x=1` crossing, so not empty — but the laws differ only at `O(ĝ²)` with no channel attached. |
| AOG-5 | independent motivation | FAIL | **FAIL** | source term is linear (P33, exact); the exponential adds `φ², φ³, …` with no independent basis. |

**First draft: 3 PASS / 1 PARTIAL / 1 FAIL → claimed `weak_alive` eligibility.**
**Corrected: 1 PASS / 3 PARTIAL / 1 FAIL → `parked`.**

The skeptic's point, which I verified before accepting: scoring AOG-3 a clean
PASS while conceding unreachability *in the same document* is precisely the
pattern AOG exists to catch. My final decision (do not promote) was already
right — but a wrong score that happens to reach the right verdict is still a
wrong score, and it is corrected here rather than quietly amended.

---

## What this does NOT establish

1. **That MULTING implies an exponential law.** It does not — the source is
   linear. This is *our* alternative, and AOG-5 fails.
2. **The "different completion" claim outside the canonical kinetic-term
   convention.** A redefinition moves the mass law but makes `(∂φ)²`
   non-canonical. Convention-relative, now stated.
3. **That the exponential is preferable.** It removes a pathology at the cost of
   unjustified terms; that trade is not resolved here.
4. **Anything about `V(φ̄) ≠ 0`** — separate variant, deliberately not bundled
   (Minimal Relaxation Rule).
5. **That the asymptotic regime is reachable.** `s = ln t`, so `s=10⁴` is
   `t = e^10000` — and since the correction decays only as `ln(s)/s`, the form is
   approached even more slowly than `ln ln t` alone suggests. A law, not an epoch.
6. **Anything about MULTING itself** (Gate 1) — this is a reconstruction.

---

## Verdict

The linear law's pathology is real and the exponential removes it, but at a cost
the AOG makes explicit — and on an honest re-score the AOG yields only **one**
clean PASS, putting this at **`parked`**. Two live completions, identical at
`O(ĝ)`, differing at `O(ĝ²)`. **Neither is promoted.**

The most useful result here is arguably the negative one: because the two laws
coincide exactly at `O(ĝ)`, **`FINDING_P67`'s result is not escapable by this
route.** Any rescue of backreaction-driven stabilisation must come from `O(ĝ²)`
or from `V(φ̄) ≠ 0`, not from the mass law.

---

## Skeptic Verdict (Step 8a)

Context-blind review: finding.md + source only, no session history, no other
project files. Reviewer re-derived the reduction to `x″+x′=k e^{−x}` by hand and
confirmed it exact; found no fatal flaw.

**Verdict: CONFIRMED-REAL, with a medium-severity honesty issue on AOG-3/AOG-4.**

| # | Concern | Severity | Response |
|---|---|---|---|
| 1 | Reduction to `x″+x′=k e^{−x}` — term dropped? | — | **No change needed.** Reviewer re-derived it independently; exact. |
| 2 | Is the correction really `1/s²`, or slower — does `diff` converge to a nonzero constant? | low | **Fixed with real computation.** Correction is `ln(s)/s`; verified over four decades (`diff/[ln(s)/s]` flat at 0.94–0.97) plus a refinement check (20.6→31.6× improvement). `diff` → 0, not a constant. |
| 3 | Field redefinition could make "different completion" wrong | low | **Fixed.** Verified the redefinition works on the mass law but breaks the canonical kinetic term. Claim survives, now explicitly convention-relative. |
| 4 | Positive control passes via `0/0` at the pathological point | low | **Fixed (documented).** Noted that `d ln m/dφ` diverges where `ρ_phys` vanishes and only the product is regular. |
| 5 | Is the asymptote IC-dependent? | low | **Fixed.** Four ICs, spread `1.8×10⁻⁴` — attractor confirmed. |
| 6 | **AOG-3/AOG-4 self-flattering** | **medium** | **Accepted and re-scored.** 3 PASS → 1 PASS; status `weak_alive` → `parked`. Final decision unchanged, intermediate score corrected. |

Every concern was independently re-verified with standalone computation before
acceptance (`audit-verification-gate.md`). All four substantive claims — the
`ln(s)/s` rate, the redefinition caveat, the IC-independence, and the AOG
re-score — checked out and were adopted.
