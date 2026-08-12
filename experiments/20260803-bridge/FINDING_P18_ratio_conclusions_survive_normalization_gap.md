# P18 — κ cancels unconditionally from P15/P16's cross/self ratio; the missing normalization constant cancels only if it takes a specific, plausible-but-unproven form

~~P17's normalization-constant gap does not touch P15/P16's ratio
conclusions; both κ and the missing constant cancel exactly from
cross/self~~ **[CORRECTED after skeptic review — retitled]**

**Date:** 2026-08-12 · corrected 2026-08-12 after context-blind skeptic
review · originally set out to answer: `FINDING_P17` found `Ω_φ`
(`FINDING_P14`'s cosmological energy-density fraction) is not
dimensionless — a missing field-normalization constant is silently
assumed `=1`. Does that same gap also undermine `FINDING_P15`/
`FINDING_P16`'s central conclusion (self-energy dominates cross-terms for
realistic discrete clusters), or are those — being ratios — immune?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P18_ratio_invariance_under_normalization_gap.py`, ruff clean.
Three symbolic checks (κ-cancellation, constant-cancellation, and a new
sensitivity check on the constant's assumed form) must pass before the
verdict is trusted.

**[CORRECTED after skeptic review — read before the rest of this file]**
A context-blind skeptic review found the κ-cancellation genuinely
unconditional (CONFIRMED-REAL) but caught that the constant-cancellation
claim was **tautological as originally argued**: multiplying both formulas
by the same `C²` and then observing the ratio is unchanged proves nothing
beyond sympy's algebra — the physical content was smuggled into the
*choice* to model the missing constant that way, not derived from
anything. The skeptic's sharpest point: `E_self` is UV-divergent (that is
*why* it needs the `r_min` cutoff at all) — the classic signature of a
quantity needing renormalization — while `U_cross(d)` at a real separation
is IR-finite and needs no such treatment. A proper fix for the former
need not act as a uniform multiplier on the latter. Added a new Part 3
(sensitivity check) confirming this precisely: if the missing constant
carries any `r_min`-dependent power, the cancellation breaks. The
constant-cancellation claim is downgraded from unconditional to
conditional throughout below.

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
collinear dipole-dipole cross-term formula (the general formula was not
re-checked symbolically here; the extension is algebraically
straightforward since both special cases share the same bilinear
`p1·p2`-type structure, but this is inherited plausibility, not a
separate proof):

```
ratio WITHOUT C : -3*p2*r_min**3/(4*pi*d**3*p1)
ratio WITH C    : -3*p2*r_min**3/(4*pi*d**3*p1)     <- identical
assert C cancels exactly -- PASSES (given the C^2-on-both premise)

ratio in terms of kappa: -3*k2r2c2*r_min**3/(4*pi*d**3*k1r1c2)   <- no kappa symbol present
assert kappa cancels exactly -- PASSES

[CORRECTED after skeptic review -- Part 3, added] sensitivity check: does
the assumed C^2-on-both premise survive a more general fix with an
r_min-dependent power alpha in E_self only (mimicking a renormalization
counterterm)?

ratio, general alpha: -3*p2*r_min**(3-alpha)/(4*pi*d**3*p1)
r_min survives in the ratio for alpha != 0: True   <- cancellation is CONDITIONAL on alpha=0
```

## Result

~~Both cancellations hold exactly, proven not assumed.~~

**[CORRECTED after skeptic review.]** The two cancellations are NOT on
equal footing:

- **`κ`-cancellation: unconditional, genuinely proven.** `κ` enters both
  `E_self` and `U_cross` only through `p_i`, linearly, with no other
  complication — the `κ²` factor is structurally identical in both
  formulas regardless of what `E_self`/`U_cross` otherwise represent.
- **`C`-cancellation: conditional, not unconditionally proven.** The
  original symbolic check (`E_self_true=C²·E_self_raw`,
  `U_cross_true=C²·U_cross_raw`) is a tautology — multiplying two
  quantities by the same factor and dividing necessarily returns the
  original ratio, by algebra alone; it does not establish that the
  *actual* missing physics takes that form. A new Part 3 sensitivity
  check makes the condition explicit: if the missing constant instead
  carries an `r_min`-dependent power (`C²·r_min^α` in `E_self`, with `α`
  representing, for instance, a renormalization counterterm structure
  tied to `E_self`'s own UV divergence as `r_min→0`, which does not touch
  `U_cross(d)` — an IR-finite, well-separated quantity needing no such
  treatment), the ratio retains `r_min` and does **not** cancel for
  `α≠0`. Verified symbolically: `ratio(α) = -3p₂r_min^{3-α}/(4πd³p₁)`,
  `r_min`-dependent for any `α≠0`.

**The "pure overall multiplier" form is a physically plausible working
hypothesis** — analogous to a Green's-function/propagator normalization
constant (like `1/(4πε₀)` in electrostatics), which genuinely would apply
identically to both formulas — but it is not independently derived from
the action here, and `E_self`'s own UV-divergent character (needing a hard
`r_min` cutoff at all) is exactly the kind of feature that historically
signals a renormalization-style fix is needed instead, which would break
the assumption.

## Consequence — a clean split by claim type

| Claim type | Examples | Affected by the C/κ gap? |
|---|---|---|
| **Ratio-based** | `FINDING_P15`/`FINDING_P16`: self-energy dominates cross-terms by `~4×10⁻⁵` (ring) to `~1.4×10⁻⁴` (sphere), for any tested `N` at realistic separations | **Unaffected by `κ`, unconditionally.** Unaffected by `C` **only if** `C` is a pure, `r_min`-independent overall multiplier — plausible but unproven. If the actual missing physics has `r_min`-dependent structure, the ratio would not be immune. |
| **Absolute-magnitude** | `FINDING_P14`'s `Ω_φ(κ=1)=3.28×10¹¹`; `FINDING_P17`'s `κ_cosmo_bound=1.75×10⁻⁶` | **Yes, remains blocked**, unaffected by anything in this finding. These depend on `E_self`'s absolute value, which needs both `κ` and `C` fixed. Neither is fixed anywhere in this project. |

**Revised, defensible statement:** `FINDING_P15`/`FINDING_P16`'s central
physical claim is fully protected from `κ`'s own unfixed value, and is
protected from `FINDING_P17`'s normalization gap *conditional on that
gap's actual form* — a condition this finding names precisely but does not
resolve. This is weaker than "unaffected by either open normalization
problem" (the original claim), and should not be read as fully closing
the question of whether P15/P16 are immune to P17's gap.

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
4. **[Added after skeptic review.] That the missing normalization
   constant `C` actually takes the "pure overall multiplier" form this
   finding's cancellation proof requires.** This is a named, plausible
   working hypothesis (analogous to a Green's-function normalization
   constant), not something derived from the action or established by
   any prior finding. `E_self`'s own UV-divergent character (requiring the
   `r_min` cutoff) is exactly the kind of feature that could instead call
   for a renormalization-style fix, which would break the cancellation
   (Part 3's sensitivity check shows this explicitly). Actually deriving
   `φ`'s correct normalization from the action's own field equation,
   rather than assuming a form for the fix, remains an open item.
5. **That P15/P16 tested or "relied on" κ-independence numerically.**
   [Corrected wording — a context-blind skeptic review found the original
   phrasing overstated this.] Neither finding's own script ever varied
   `κ` as a free parameter; `κ` never entered their numerics as a
   variable at all. This finding shows the ratio WOULD be `κ`-independent
   if it had been varied — a structural fact those findings never
   encountered, not one they relied on.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic verdict (Step 8a, context-blind — claim + code + cited files only)

Two separate verdicts, not merged:

**(1) Math/symbolic content: CONFIRMED-REAL for the narrow scope of what
the code actually does, with a significant framing caveat.** Both
`assert`s pass and correctly demonstrate: given the `C²`-on-both premise,
the ratio is unchanged (algebraically trivial once that premise is
granted); given `p_i` linear in `κ`, the ratio is `κ`-free (genuinely
substantive, since κ could in principle have entered asymmetrically and
did not). The framing caveat: calling the `C`-cancellation "proven, not
assumed" (original draft) mischaracterized a tautological substitution as
a derivation — the skeptic's phrase: "the asserts prove that sympy
correctly simplifies expressions with a common factor... nothing more."

**(2) Interpretive claim ("P15/P16's ratio conclusions are unaffected for
ANY value of κ and ANY value of C"): FALSIFIED for the "ANY value of C"
strength, WEAKENED overall.** The `κ` half survives as CONFIRMED-REAL and
unconditional. The `C` half does not survive as stated — it holds only
conditional on `C` taking a specific, unproven, though physically
plausible, form. Applied per Response Matrix: retitled (Fix), Part 3
sensitivity check added to the script proving the condition explicitly
rather than hiding it (Fix), "Result" and "Consequence" sections rewritten
to split the unconditional κ result from the conditional C result (Fix),
new "does NOT establish" items 4-5 added (Fix), general-vs-collinear
formula scope limitation now stated explicitly (Accept-with-doc). No
response fell to core-predicate-false — the κ-invariance result survives
fully intact; only the C-invariance claim is downgraded from unconditional
to conditional.

## Reproduction

```bash
python experiments/20260803-bridge/P18_ratio_invariance_under_normalization_gap.py
```

Both symbolic cancellation asserts must pass before the verdict is
trusted.
