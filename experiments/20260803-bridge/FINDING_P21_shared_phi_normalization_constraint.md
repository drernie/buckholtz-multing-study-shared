# P21 — the action's own two couplings force the missing normalization constant to carry Newton's-G units

**Date:** 2026-08-13
**Origin:** P17 found `Ω_φ` (built from P14's self-energy formula) carries units
`kg/m`, not dimensionless — a missing dimensional normalization constant. P19
derived and fixed the *geometric* piece of the field's normalization (the
`1/(4π)` from solving `∇²G=δ³(x)`), but explicitly left the *dimensional*
piece open. P13a (same day) separately established that P1's own action has
**two independent coupling constants** — `g` (monopole, coupled to mass) and
`κ` (dipole, coupled to the second charge) — and that `g` is the term P1's own
text says "renormalises `G`, absorbed." This finding asks the cheapest next
question: does requiring the **same field `φ`** to consistently carry *both*
couplings constrain the missing constant?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P21_shared_phi_normalization_constraint.py`

## 1. What this checks

P1's action (`two_field_action_closure.py`):

```
S = ∫d⁴x (1/2)(∂φ)² + Σᵢ ∫dτ [ g·mᵢ + pᵢ·∇ ] φ(xᵢ),   pᵢ = κ·kᵢ·rᵢ/c²
```

Two coupling terms share the same field `φ` and the same canonical kinetic
term. Each independently requires `[g·m·φ]` = energy and `[p·∇φ]` = energy.
With `g` and `κ` dimensionless (established: `κ` in P14, `g` follows the same
"ordinary coupling constant" convention P13a names), each coupling separately
fixes what `[φ]` must be. **This project had never checked whether those two
independently-derived requirements actually agree** — that is the first thing
this script verifies, symbolically (sympy exponent bookkeeping on kg/m/s), not
assumed.

## 2. Result

```
[phi]_monopole = kg^0 m^2 s^-2   (from g*m*phi = energy)
[phi]_dipole   = kg^0 m^2 s^-2   (from p.grad(phi) = energy, p=kg*m per P14)
SAME requirement from both couplings: True
```

Both couplings independently demand `[φ]=m²/s²` — internally consistent, not
by construction (the two derivations use unrelated inputs: mass alone vs. the
dipole moment `p=κkr/c²`).

The `φ_raw` actually computed throughout P9–P20 (using P19's Green's function
`G(x)=-c_G/r` with `c_G=1/(4π)`, a pure number) has `[φ_raw]=kg/m` for a
monopole source — not `m²/s²`. Defining the missing constant `A := φ_true/φ_raw`:

```
[A] = kg^-1 m^3 s^-2  ==  Newton's G units (kg^-1 m^3 s^-2): True
```

`A` is **forced** to carry exactly Newton's-`G` units — not assumed, not
guessed; it falls out of the shared-`φ` consistency requirement.

Taking P1's own "renormalises `G`, absorbed" claim as a literal force-matching
condition — the monopole exchange force between two masses must equal
Newton's law — gives:

```
A * c_G * g² = G   ,   c_G = 1/(4π) (P19)
=>  A * g² = 4πG
```

## 3. What this does NOT do

**One equation, two unknowns (`A`, `g`).** This derivation narrows the space
(units fixed, one structural equation) but does **not** produce a numeric
value for either `A` or `g` — that requires one more independent input.
P13a already named the natural candidate: Archidiacono et al.'s external
`β<0.0054` (95% CL) bound on a scalar monopole fifth force is, per P13a §2, a
bound on this same `g` — but turning that into a numeric value of `g` (and
hence, via `A·g²=4πG`, of `A`) requires verifying Archidiacono's own
definition of `β` against the actual paper's equations, which has **not been
done here**. This is the concrete next step, not a result of this finding.

## 4. Why this matters for κ, stated narrowly

`Ω_φ`'s formula (P14) is built from the same `φ` field that the dipole
coupling sources, so the same missing constant `A` enters it. Once `A` is
pinned down (even parametrically, in terms of `g`), `Ω_φ`'s absolute
normalization becomes computable in terms of `A` and `κ` jointly — this
finding does not attempt that substitution or re-derive `Ω_φ`'s formula, only
notes the constant is the same one.

## 5. What this does NOT establish

1. **A numeric value for `A`, `g`, or `Ω_φ`.** Only their unit/structural
   relationship.
2. **That Archidiacono's `β` bound applies to `g` without re-verification.**
   P13a already flagged this as a naive-but-unconfirmed mapping; this finding
   does not attempt to close that gap.
3. **Anything about the dipole sector's own remaining open questions** (P18's
   conditional cancellation, P19's near-`r_min` multipole caveat, P20's
   extended-source correction) — this is a monopole/gravity-sector question,
   logically separate from those.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   P1's action, not a claim about any error in TJB's own theory.

## Reproduction

```bash
python experiments/20260803-bridge/P21_shared_phi_normalization_constraint.py
```

## Skeptic verdict (context-blind, Step 8a)

*Pending — to be run with only this file + `P21_shared_phi_normalization_constraint.py`
+ `two_field_action_closure.py` + `FINDING_P14_kappa_normalization_unfixed.md`
+ `FINDING_P19_greens_function_normalization_derived.md` + `FINDING_P13a_archidiacono_bound_scope.md`,
no session history.*
