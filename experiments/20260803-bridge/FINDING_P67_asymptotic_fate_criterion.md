# FINDING P67 — asymptotic-fate criterion: the proposed backreaction rescue is absent at O(ĝ)

**Status:** Skeptic-reviewed (Step 8a) and corrected. Verdict CONFIRMED-REAL with
WEAKENED framing → framing fixed, two missing controls added with real computation.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive — a structural property of an
ODE system, not a causal claim. No DAG required.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`

**Artifact:** `P67_asymptotic_fate_criterion.py`

---

## The question

`FINDING_P65` found that `x := ĝφ̄` drifts logarithmically without bound on the
*uncoupled* background, heading for the surface `x=1` where `ρ_phys = (1−x)ρ_A`
vanishes. The user proposed that the **full coupled backreaction might stop that
drift** — that if the universe expands fast enough, `1/a³` suppresses `φ̄̇` and the
field freezes below `x=1`.

The proposal reduced this to convergence of `I_∞ = ∫^∞ t/a³(t) dt`, with a
trichotomy for `a ~ t^p` (`p<2/3` power-divergence, `p=2/3` log, `p>2/3`
convergence) and three outcomes: A (`I_∞=∞`, doom), B (converges, `x_∞>1`),
C (converges, `x_∞<1`, **stabilisation**).

The answer is **A, not C**. But the honest form of that answer is narrower than
it first sounds — see the Verdict.

---

## Established exactly (no approximation)

**1. The criterion is inherited, not assumed.** `P66`'s first integral
`a³φ̄̇ = √2 + ĝ(t−1)` is re-verified here from scratch for a generic `a(t)`.
Multiplying by `ĝ` gives `ẋ = (√2ĝ + ĝ²(t−1))/a³` exactly, so the fate question
*is* the convergence question. `[VERIFIED-SYMPY]`

Corollary: at late `t` the `ĝ²(t−1)` term dominates, and `ĝ² > 0` for **either
sign** of `ĝ`. This retroactively **explains** `FINDING_P64`'s otherwise
unexplained observation that negative `ĝ` showed no sign pathology.

**2. Our background sits exactly on the knife-edge.** `FINDING_P62`'s background
is `a₀³ = 6πt² − 1` identically, so `a₀ ~ t^(2/3)` **exactly**. `[VERIFIED-SYMPY]`

This was **missed by the proposal**, which treated `p=2/3` as one of three
generic outcomes. It is not generic — it is the boundary. *The leading power
decides nothing;* the fate is decided by the **subleading** behaviour of `a³`,
i.e. by the `O(ĝ)` correction `δ(t)` that `P66` already computed. P67 is
therefore not a new programme but one asymptotic question about an ODE in hand.

**3. The criterion machinery discriminates** (Part C): `p=1/3` power-diverges,
`p=2/3` log-diverges, `p=1` converges, de Sitter converges. `[VERIFIED-SYMPY]`

---

## Established at first order in ĝ

**4. `δ(t)` saturates, in closed form.** `Q(t) ~ c/t` and `μ(t) ~ t` ⟹ `μQ ~ c`
⟹ `δ = (1/μ)∫μQ → c`:

```
δ_∞ = lim t·Q(t) = −0.0254656728…       (sympy)
δ(10⁷) numeric   = −0.0254655920         |Δ|/|c| = 3.2×10⁻⁶
```

**[Skeptic-improved]** The reviewer re-derived this by hand in a far more
readable equivalent form, which I verified agrees to `<10⁻²⁰` before adopting:

```
c = −φ̄₀(∞)/3,   φ̄₀(∞) = ∫₁^∞ √2/(6πt²−1) dt = 0.07639702
```

This is not merely tidier — it says what `c` *means*: the asymptotic scale-factor
correction is the **total accumulated zeroth-order field displacement, over 3**.

**5. The power is unchanged.** `a³ → a₀³(1+ĝc)³` is a *constant* rescaling, so
`a³ ~ [6π(1+ĝc)³]t²` — still exactly `t²`. The `O(ĝ)` backreaction **cannot
change the convergence class.** It moves only the log coefficient:

| ĝ | −1.0 | −0.1 | −0.01 | +0.01 | +0.1 | +1.0 |
|---|---|---|---|---|---|---|
| `(1+ĝc)⁻³` | 0.927 | 0.9924 | 0.9992 | 1.0008 | 1.0077 | 1.0805 |
| vs ĝ=0 | −7.27 % | −0.76 % | −0.08 % | +0.08 % | +0.77 % | +8.05 % |
| direction | slower | slower | slower | faster | faster | faster |

**[Skeptic-caught, independently verified]** My first version tabulated only
`ĝ>0` and asserted a bare "wrong sign". That was incomplete: since `c<0`, the
shift **reverses** for `ĝ<0`. But the `ĝ²` numerator of `ẋ` is sign-blind, so
**neither sign changes the divergence class** — negative `ĝ` slows a divergent
drift, it does not stop one. The `|ĝ|=1` rows are a formal evaluation of the
small-`ĝ` expansion and are *not* covered by the cross-check, which stops at 0.1.

---

## Cross-check and ablation

Positive control on initial data: `H(1)` from the state vector reproduces `P62`'s
closed form to `10⁻¹²`.

| check | window | result |
|---|---|---|
| full `x(T)` vs full `O(ĝ)` prediction | `T=50, 200`; `ĝ=0.01, 0.1` | rel.diff `1.1×10⁻⁴ … 2.1×10⁻⁴` |
| full `dx/d ln t` vs predicted asymptote | `t=10⁵…10⁶` | `0.0006` (`ĝ=0.01`), `0.0056` (`ĝ=0.1`) |

**[Skeptic-demanded ablation — the sharpest catch of the review.]** The reviewer
correctly observed that Part C's four controls test the *integral classifier*,
not the `δ` derivation: a sign error in `Q`, a missing term in `B`, or a wrong
`c` would sail straight through them. Added: compare the *same* measured rate
against three predictions.

| ĝ | rel.diff true `c` | rel.diff `c=0` | rel.diff `−c` | best |
|---|---|---|---|---|
| 0.01 | **0.00060** | 0.00137 | 0.00213 | true `c` |
| 0.1 | **0.00560** | 0.01332 | 0.02108 | true `c` |

Strict ordering at both couplings, asserted in code. The check therefore
**resolves** the `c`-correction rather than tolerating it — which makes the sign
of `c` an empirical result here, not only a symbolic one.

**[Skeptic-corrected naming.]** Both sides solve the *same* Friedmann+KG
equations. This validates the **derivation** (it caught both bugs below), **not**
the physics choices — Lagrangian, coupling form and initial data are shared and
therefore untested by it. The accurate label is "self-consistency against
numerical integration of the same equations", not "independent check".

**[Skeptic-added]** `μ` was previously hardcoded without deriving `B`, so a
miscopy could not be self-detected. Now `B` is extracted and `μ̇/μ = B/A` is
asserted.

---

## Self-caught bugs, before skeptic contact

**Bug 1 — the test compared incommensurable quantities.** The first cross-check
compared full `x(t)` against the *asymptotic* log-rate over `t=50…200`. It
**failed** at `ĝ=0.01` (rel.diff 1.52). The physics was right; the *test* was
wrong. `ẋ`'s two terms cross over at `t ~ 1 + √2/ĝ` — `t≈142` for `ĝ=0.01`. At
`t=50` the **dropped** transient still dominated the **retained** asymptotic
term. Fixed by comparing to the full `O(ĝ)` prediction near, and testing the
asymptotic rate only far past the crossover.

**Bug 2 — double-counted coupling.** `x_pred` came out exactly `1/ĝ` too small.
The tell was `x_full/x_pred = 100.000` at `ĝ=0.01` — a round number equal to
`1/ĝ` rather than anything physical. `x_semianalytic` already integrates `ẋ`;
the call site multiplied by `ĝ` again. Error went from 99 % to `1.1×10⁻⁴`.

Both documented inline, not silently repaired.

---

## What this does NOT establish

1. **That `x` ever reaches 1.** **[Skeptic-caught, and the binding bound is not
   the obvious one.]** I originally named `x ≪ 1` as *the* validity bound. There
   are two, and the *second* binds far earlier:
   - *Bound 1:* `x ≪ 1`, since `x = ĝφ̄` enters Friedmann at `O(ĝ)`.
   - *Bound 2:* the `φ̄` series needs `|ĝφ̄₁| ≪ φ̄₀`, but `φ̄₀ → 0.0764` (finite)
     while `φ̄₁` grows **secularly** as `ln t/(6π)`. This fails at
     `ln t ~ 1.44/ĝ` — versus `ln t ~ 6π/ĝ²` for `x→1`. For `ĝ=0.01` that is
     `ln t ≈ 144` vs `≈1.9×10⁵`: **three orders of magnitude in `ln t` earlier.**

   This does not weaken the `O(ĝ)` negative result, which lives in the valid
   window. It *strengthens* the refusal to say anything about the crossing.
2. **Anything at `O(ĝ²)`** — where a genuine change of power would have to come
   from, if it comes at all.
3. **Anything with `V(φ̄) ≠ 0`.** Both `P66` and `P67` assume `V=0`, and a
   potential is precisely the kind of term that *can* change the late-time `p`.
4. **Generality of `ρ̄_A a³ = C`**, inherited from `FINDING_P58`.
5. **Anything about MULTING itself.** This concerns *our* completion, a
   reconstruction. Per Gate 1, no verdict here transfers to Dr. Buckholtz's model.
6. **That the drift is physically fast.** Logarithmic divergence; time to `x=1`
   is exponential in `1/ĝ²`. "Eventually" is not "soon".

---

## Verdict

**[Rewritten after the skeptic called the first version's framing rhetorically
overpitched — magnitude now stated first.]**

The proposed rescue is **absent because it is negligible**: the log coefficient
moves by 0.08 % at `|ĝ|=0.01` and 0.77 % at `|ĝ|=0.1`. Its direction is a
secondary detail on a tiny effect (faster for `ĝ>0`, slower for `ĝ<0`). The
correct summary is *"negligible, and not helpful"* — **not** *"a large effect in
the wrong direction"*, which is what my first draft implied by saying the
mechanism "has the WRONG SIGN, not merely a small magnitude."

What is solid: **no choice of `ĝ`, of either sign, changes the divergence
class at `O(ĝ)`.** Backreaction-driven freezing does not happen at the order
where it was proposed. The ultimate fate of the completion remains **open**.

Live candidates now shift to the two assumptions this file leaves untouched: a
nonlinear mass law `m(φ)` (→ **P68**, where `m₀e^{−ĝφ}` never crosses zero while
agreeing with the linear law to `O(ĝ)` — so every P66/P67 result survives the
substitution), and `V(φ̄) ≠ 0`. Per the Minimal Relaxation Rule these are
separate variants, one assumption each, not bundled.

---

## Skeptic Verdict (Step 8a)

Context-blind review: finding.md + source only, no session history, no other
project files. Reviewer independently re-derived the first integral, the
background Friedmann check, the `δ` ODE, the integrating factor, and `c` in
closed form — reproducing `c ≈ −0.02547` **by hand** to 5 significant figures.

**Verdict: CONFIRMED-REAL with WEAKENED framing.**

| # | Concern | Severity | Response |
|---|---|---|---|
| 1 | `δ_∞ = lim t·Q(t)` correct? Homogeneous mode dropped? | — | **No change needed.** Reviewer confirmed: homogeneous piece `∝ 1/μ ~ 1/t` decays; `δ(1)=0` drops nothing. |
| 2 | `a³ → a₀³(1+ĝc)³` legitimate? | low | **No change needed.** Cubic comes from the ansatz, not an `O(ĝ)` truncation; `ĝ|c|≤0.025` even at `ĝ=1`. |
| 3 | Sign claim correct? | — | **Confirmed for `ĝ>0`** — but see #4. |
| 4 | `sign(ĝ)` asymmetry never disentangled | low | **Fixed.** Independently verified the reversal, added both-sign table, stated that neither sign changes the divergence class. |
| 5 | Rhetoric outstrips effect: "WRONG SIGN, not merely small magnitude" describes a 0.08 % shift | low-med | **Fixed.** Verdict rewritten magnitude-first; the overpitched clause removed and its removal recorded above. |
| 6 | **Part C controls the integral classifier, not the `δ` calculation** — a wrong `c` would pass untouched | **medium** | **Fixed with real computation.** Added the three-way ablation (true `c` / `c=0` / `−c`); true `c` fits strictly best at both couplings, asserted in code. |
| 7 | Far-window agreement of 0.0006 suspiciously good; is it circular? | low | **Partly fixed, partly accepted.** Not vacuous — it caught both bugs. But reviewer is right that it shares equations with the prediction; relabelled "self-consistency", not "independent check". |
| 8 | Temporal (secular) validity bound never stated, only `x≪1` | low-med | **Fixed.** Independently re-derived; the secular bound binds ~3 orders of magnitude in `ln t` earlier. Now Bound 2 in Part F and item 1 of "does NOT establish". |
| 9 | `μ` hardcoded, `B` never derived — miscopy undetectable | low | **Fixed.** `B` extracted, `μ̇/μ = B/A` asserted. |
| 10 | `|ĝ|=1` row formal only, outside cross-checked range | low | **Fixed.** Labelled "formal only" in the table and in the text. |

Every concern was independently re-verified with a standalone computation before
being accepted (`audit-verification-gate.md`: the agent's `[VERIFIED]` is my
`[INFERRED]`). All three substantive claims — the readable closed form, the sign
asymmetry, the earlier secular bound — checked out and were adopted. None
overturned the finding; all tightened it.
