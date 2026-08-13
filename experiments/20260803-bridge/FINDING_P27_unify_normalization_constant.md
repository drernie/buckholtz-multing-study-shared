# P27 — the "missing normalization constant" flagged five separate times since P14 is one unknown, `A`, not several

**Date:** 2026-08-13
**Origin:** user-directed redirect — a frozen external prediction (the
originally-planned P27) is premature without a numeric `ρ_φ`, which is
blocked by the normalization gap `FINDING_P14` §6 first flagged and
`FINDING_P17`, `FINDING_P21`, `FINDING_P22`, `FINDING_P26` each
re-encountered without ever asking whether they were the *same* gap.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P27_unify_normalization_constant.py`

## 0. Honest scope, stated before anything else

**Dimensional analysis alone can never produce a number** — only units and
structural relationships between constants. This finding does **not**, and
cannot, fix `κ` or `A`'s numeric value. What it *can* do, and does:
determine whether the normalization gaps flagged in five separate findings
are the *same* single unknown or genuinely independent ones, and derive
the exact formula connecting that unknown to every downstream quantity.

## 1. Method

Made the action's kinetic-term prefactor `C` explicit — every prior
finding (P9–P26) used it implicitly `=1`:

```
S = ∫d⁴x (C/2)(∂φ)² + Σᵢ∫dτ[g·mᵢ + κ·(kᵢrᵢ/c²)·∇]φ(xᵢ)
```

Derived `[C]`'s required units from action-level dimensional consistency
(sympy, M/L/T exponent bookkeeping), then **re-derived the field equation
from the Euler–Lagrange equations with `C` explicit** (not assumed), and
checked whether the result matches `FINDING_P21`'s own `φ_true=A·φ_raw`
convention — from a completely independent starting point.

## 2. Result

`[φ]` from both couplings reproduces P21 exactly (`m²/s²`) — a first
cross-check that this derivation is set up consistently with prior work.

**`[C]` carries exactly `1/G`'s units** (`M¹L⁻³T²`) — verified, not
assumed.

**Re-deriving the field equation with `C` explicit** (monopole term,
static limit):

```
δS/δφ(x) = −C·∇²φ + g·m·δ³(x) = 0
⟹ ∇²φ = (g·m/C)·δ³(x)
⟹ φ(x) = (g·m/C)·G(x),   G(x)=−1/(4πr)  [P19's own Green's function]
```

Compare to `φ_raw` (P9–P20's own convention, `C` implicitly `=1`):
`φ_raw(x)=g·m·G(x)`. So:

```
φ_properly_normalized(x) = φ_raw(x)/C
```

**`A = 1/C` reproduces P21's own `φ_true=A·φ_raw` exactly** — verified
symbolically. This is a genuine **cross-validation** of P21, arrived at
from action-level first principles (dimensional consistency +
Euler–Lagrange), not a restatement of P21's own force-matching argument.

**Conclusion**: every "missing normalization constant" flagged since P14
§6 (P14 §6, P17, P21, P22, P26) is **the same single unknown, `A`** — not
several independent gaps, as the fragmented flagging across five findings
might have suggested.

**Applying this to `E_self`** — verified by two independent routes:

```
Route 1:  A · E_self,correct(P26) = A · p²/(12πr_min³)
Route 2:  C · ∫(∇φ_true)²dV   (direct kinetic-term integral)
```

Both give **exactly energy units** (`kg·m²/s²`), and both routes agree
with each other. `E_self,physical = A·p²/(12πr_min³)` is a genuine energy
**for the first time in this project** — `ρ_φ=n·E_self,physical` and
`Ω_φ=ρ_φ/ρ_crit` are now dimensionally well-posed, a true dimensionless
number, *once `A`'s numeric value is known*.

## 3. What this does NOT establish

1. **A numeric value for `A`, `κ`, `E_self`, `ρ_φ`, or `Ω_φ`.** Only
   `P22`'s own `A·g²≲1.05×10⁻¹⁰` (SI) soft ceiling exists — a bound on the
   *product*, not `A` alone. Extracting a number for `A` (hence for
   `Ω_φ`) still requires an independent estimate of `g` or `κ` from
   outside this project's own internal derivations — not attempted here.
2. **That `A`'s placement (kinetic term vs. coupling normalization) is
   forced rather than a convention.** P24's own skeptic review already
   established this is a convention choice; this finding shows the *two*
   conventions (rescale `φ` via `A`, or rescale the kinetic term via
   `C=1/A`) are reciprocal and give identical physics — a clarification
   of that convention-freedom, not a removal of it.
3. **Anything about `κ`'s own value** — this finding is entirely about the
   *field-normalization* constant `A`, shared by both the `g` and `κ`
   sectors; `κ` itself remains exactly as unfixed as `FINDING_two_charge_completion.md`'s
   own "zero free parameters after `κ`" originally stated.
4. **A resolution of P25's WEP kill-gate**, P23's target-population
   question, or any other open item from the P21–P26 arc — this finding
   is narrowly about unifying the normalization-constant bookkeeping.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   of P1's action, not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P27_unify_normalization_constant.py
```

## Skeptic verdict (context-blind, Step 8a)

*Pending — to be run with only this file + `P27_unify_normalization_constant.py`
+ `two_field_action_closure.py` + `FINDING_P21_shared_phi_normalization_constraint.md`
(corrected version) + `FINDING_P26_stress_tensor_equation_of_state.md`
(corrected version), no session history.*
