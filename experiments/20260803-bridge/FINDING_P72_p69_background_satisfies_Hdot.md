# FINDING P72 — `P69`'s background satisfies the `Ḣ` equation **structurally**, not to a tolerance: P71's precondition is met unavoidably

**Status:** Skeptic-reviewed (Step 8a) and **reframed**. Verdict **WEAKENED** —
the numbers were right, the *interpretation* was inflated. All three of the
reviewer's tests were run; one concern confirmed, one dismissed with data, one
fixed as a design smell. **The reframing makes the answer stronger, not weaker.**
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P72_p69_background_satisfies_Hdot.py`

---

## The question

`FINDING_P71` identified the obstruction to constraint closure exactly:

```
dC/dt |_{C=0}  =  −Ψ · [ Ḣ + 4πG(ρ_tot + p_tot) ]
```

and listed in its own *"NOT ESTABLISHED"* that it had **not** checked whether
`FINDING_P69`'s background satisfies the `Ḣ` equation.

---

## The answer, and it is structural

In P69's integrator the Friedmann relation is **not a constraint the trajectory
earns — it is the *definition* of `H`**, recomputed algebraically at every step
and never evolved. Together with the background KG and `ρ_A = C/a³` (also
algebraic, not evolved), the identity

```
d/dt(Friedmann) − 6H·[Ḣ + 4πG(ρ_tot+p_tot)]  =  0        exactly   [VERIFIED-SYMPY]
```

makes the `Ḣ` equation an **analytic identity of the ODE system**. It cannot fail
on an exact solution.

**So P71's precondition is met structurally and unavoidably — a stronger answer
than any tolerance could give.**

---

## ⚠️ What the reviewer corrected, and why they were right

My first draft presented the numerics as a *validation* and called the central
difference *"an independent measurement"*. The reviewer:

> *"H and ρ+p are two analytic functions of the SAME state, equal by construction
> of the ODE. They are not independent; they are the two sides of an identity
> that Part A itself proved."*

**Correct.** And their proposed test settled it. **Tolerance sweep:**

| rtol | worst residual | reading |
|---|---|---|
| 10⁻⁴ | 1.25×10⁻⁴ | tracks rtol |
| 10⁻⁶ | 4.02×10⁻⁶ | tracks rtol |
| 10⁻⁸ | 5.19×10⁻⁸ | tracks rtol |
| 10⁻¹⁰ | 4.65×10⁻¹⁰ | tracks rtol |
| 10⁻¹² | 1.22×10⁻¹⁰ | **floor reached** |
| 10⁻¹³ | 8.28×10⁻¹¹ | **floor reached** |

The residual **tracks `rtol`** down to ~10⁻¹⁰, then plateaus on a
finite-difference truncation floor. **The "1.3×10⁻¹⁰" was reporting scipy's
tolerance, not a property of the `Ḣ` equation.** The phrase *"an independent
measurement"* is **withdrawn**.

**What the numerics genuinely deliver** is narrower but real: a **QA check on the
implementation** — three specific code hazards ruled out.

---

## Concern-by-concern

| # | Concern | Sev | Response |
|---|---|---|---|
| 1 | The test is circular — H is *defined* by Friedmann, so this measures integrator error, not physics | **MED-HIGH** | **CONFIRMED.** Tolerance sweep run and reported. Framing corrected throughout; "independent measurement" withdrawn. **But this makes the answer stronger**: the `Ḣ` equation is not a condition P69 *happens* to satisfy, it is automatic. |
| 2 | The sabotages change the *trajectory*, not the *evaluator* — they show "different dynamics give different numbers" | MED | **DISMISSED with data.** Ran their proposed evaluator-mutation control: flipping the coupling sign in `ρ+p` on the **unchanged trajectory** raises the residual by **10⁶–10⁹**. The check *does* discriminate transcription bugs. Their instinct that this control was missing was right; the outcome favours the check. |
| 3 | `CLAMP_HITS` is a global whose zero could mask a later hit; Part D's clamp is never re-checked | LOW | **ACCEPTED as a design smell, fixed.** Part B's count is now snapshotted before the assertion, and the counter is reset before Part D so those runs are checked separately. (Both are 0 — verified, previously invisible.) |
| 4 | Part A's framing implies a physics statement where `F≡0` is a definition | MED | **ACCEPTED and reframed** — see "The answer, and it is structural" above. |

**Pattern, fourth file running:** the reviewer's *process instinct* was right even
where their prediction wasn't. They expected the evaluator-mutation test might
expose blindness; it didn't — but demanding it converted an assumption into a
measured fact.

---

## What the numerics rule out

- **The `max(arg, 0.0)` clamp never engaged** — 0 hits in Part B, and 0 in Part
  D's sabotaged runs (checked separately). A real hazard: had the Friedmann
  argument gone negative, `H` would have been silently wrong.
- **Evaluator transcription** — the mutation control above.
- **Gross integrator failure** over four decades of `t`, at four `(ĝ,λ)` pairs.
- `ρ_A·a³ = C` holds to `1.1×10⁻¹⁶` — **reported honestly as a tautology**
  (`ρ_A` is *computed as* `C/a³`, never evolved), listed only because Part A's
  derivation uses it.

---

## What this does NOT establish

1. **That the numerics validate the `Ḣ` equation.** They cannot — Part A shows it
   is an identity of the ODE system, so the numbers can only detect code and
   integrator faults.
2. **That `Ψ_k` is therefore solvable.** P71 showed the constraint **closes** once
   `Ḣ` holds. Closure is a *consistency* property, not a *solution*. `P61`'s
   system is still not solved for `Ψ_k`, and this file does nothing toward it.
3. **`μ(a,k)` or `γ`.** Unchanged.
4. **Anything beyond `t=10⁴`** or outside the four `(ĝ,λ)` pairs.
5. **That P69's background is the *right* one** — only that it is internally
   consistent. The quartic remains P45's *minimal* choice.
6. **Anything about MULTING itself** (Gate 1): `V` is *our* construction.

---

## Verdict

**P71's remaining precondition is met — structurally.** The obstruction P71
named, an unimposed `Ḣ` equation, is *not present and cannot be present* in a
background built the way P69 builds it.

The numerics do not validate that; they cannot. What they do is rule out three
implementation hazards that could have made the structural argument inapplicable
to the actual code. That is a smaller claim than the first draft made, and it is
the claim the evidence supports.
