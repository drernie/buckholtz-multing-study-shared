# P18 — P17's normalization-constant gap does not touch P15/P16's ratio conclusions; both κ and the missing constant cancel exactly from cross/self

**Date:** 2026-08-12 · direct follow-up to `FINDING_P17`'s correction:
`Ω_φ` (`FINDING_P14`'s cosmological energy-density fraction) is not
dimensionless — a missing field-normalization constant is silently
assumed `=1`. Does that same gap also undermine `FINDING_P15`/
`FINDING_P16`'s central conclusion (self-energy dominates cross-terms for
realistic discrete clusters), or are those — being ratios — immune?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P18_ratio_invariance_under_normalization_gap.py`, ruff clean.
Two symbolic asserts (constant-cancellation, κ-cancellation) must pass
before the verdict is trusted — proven, not assumed.

## The question, precisely

`FINDING_P17` found that `Ω_φ = ρ_φ/ρ_crit`, built from `FINDING_P14`'s
self-energy formula `(8π/3)p²/r_min³`, has units `kg/m` rather than being
dimensionless — meaning a normalization constant `C` (with units to fix
this, separate from `κ`) is silently being treated as `1`. Since
`FINDING_P15`/`FINDING_P16`'s central result is a **ratio** (cross-term
energy over self-energy), built from the same underlying field `φ` via
the same coupling, the natural next question is whether that ratio
inherits the same problem, or cancels it out.

## Method

Both `E_self=∫(∇φ)²d³x` and `U_cross=∫∇φ₁·∇φ₂d³x` are **quadratic in
`φ`** — one is a square, the other is a bilinear (symmetric) form in the
same field. If the true field is `φ_true=C·φ_raw` for some unknown
constant `C` (the normalization gap `FINDING_P17` found), both energies
pick up a factor `C²`, and the ratio should cancel it exactly. The same
argument applies to `κ` itself: `p_i=κk_ir_i/c²` is linear in `κ`, so both
`E_self~p_i²` and `U_cross~p_i·p_j` scale as `κ²`, and the ratio should be
`κ`-independent too — a fact `FINDING_P15`/`FINDING_P16` already
implicitly relied on (both used `κ=1` in their Regime B/B' numbers without
proving the ratio doesn't depend on that choice).

Verified symbolically (sympy), using the project's own already-verified
formulas unchanged — `FINDING_P14`'s self-energy formula, `FINDING_P15`'s
collinear dipole-dipole cross-term formula:

```
ratio WITHOUT C : -3*p2*r_min**3/(4*pi*d**3*p1)
ratio WITH C    : -3*p2*r_min**3/(4*pi*d**3*p1)     <- identical
assert C cancels exactly -- PASSES

ratio in terms of kappa: -3*k2r2c2*r_min**3/(4*pi*d**3*k1r1c2)   <- no kappa symbol present
assert kappa cancels exactly -- PASSES
```

## Result

**Both cancellations hold exactly, proven not assumed.** The missing
field-normalization constant `C` (`FINDING_P17`'s new gap) and `κ`'s own
unfixed value (`FINDING_P14`'s original gap) both drop out of the
cross-term/self-energy ratio completely.

## Consequence — a clean split by claim type

| Claim type | Examples | Affected by the C/κ gap? |
|---|---|---|
| **Ratio-based** | `FINDING_P15`/`FINDING_P16`: self-energy dominates cross-terms by `~4×10⁻⁵` (ring) to `~1.4×10⁻⁴` (sphere), for any tested `N` at realistic separations | **No.** Holds for any value of `κ` and any value of the missing constant `C` — the qualitative conclusion (self dominates) and the specific numeric ratios reported are unaffected. |
| **Absolute-magnitude** | `FINDING_P14`'s `Ω_φ(κ=1)=3.28×10¹¹`; `FINDING_P17`'s `κ_cosmo_bound=1.75×10⁻⁶` | **Yes, remains blocked.** These depend on `E_self`'s absolute value, which needs both `κ` and `C` fixed. Neither is fixed anywhere in this project. |

**This strengthens confidence in the ratio-based findings specifically**:
`FINDING_P15`/`FINDING_P16`'s central physical claim (self-energy is real
and dominant for realistic discrete clusters) does not depend on either
of the two open normalization problems — it would hold under any eventual
resolution of `κ` or `C`. It does **not** strengthen or weaken the
absolute-magnitude findings — those remain exactly as blocked as
`FINDING_P17` left them, now clearly understood to be blocked by two
independent unfixed constants rather than one.

## What this does NOT establish

1. **A value for either `κ` or the missing normalization constant `C`.**
   Neither is fixed by this finding — it only shows their *product's
   effect on the ratio* is trivial (cancels), not their individual
   values.
2. **That `FINDING_P14`'s or `FINDING_P17`'s absolute numbers are
   otherwise fine.** They remain blocked exactly as those findings
   describe; this finding only clarifies which downstream claims are and
   are not affected.
3. **That no other, un-examined quantity in this project depends on `C`
   in a way that does not cancel.** Only the specific cross/self ratio
   used in `FINDING_P15`/`FINDING_P16` was checked here. Any future
   absolute-energy or absolute-force claim built from `φ` should be
   checked individually before being trusted.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P18_ratio_invariance_under_normalization_gap.py
```

Both symbolic cancellation asserts must pass before the verdict is
trusted.
