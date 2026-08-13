# P27 — an explicit formula for `A`'s role in `E_self`, working out in detail a convention P21 had already flagged as equivalent

**Date:** 2026-08-13
**Origin:** user-directed redirect — a frozen external prediction (the
originally-planned P27) is premature without a numeric `ρ_φ`, which is
blocked by the normalization gap `FINDING_P14` §6 first flagged and
`FINDING_P17`, `FINDING_P21`, `FINDING_P22`, `FINDING_P26` each
re-encountered without ever asking whether they were the *same* gap.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P27_unify_normalization_constant.py`

**[CORRECTED after skeptic review, same day — a real self-consistency
failure, not just framing.]** `FINDING_P21`'s own §2 (corrected version,
read and cited by this finding) **already states**, verbatim: *"the
identical physics results from placing an equivalent factor in the
kinetic term instead (`(1/(2A))(∂φ)²`)... What is convention-independent
is only that some factor with `G`'s units must exist somewhere in the
action; where it formally lives is a choice."* This finding's central
claim — that deriving `C=1/A` from the kinetic term is an "independent
cross-validation" of P21 — is therefore **not accurate**: P21 already
told us this equivalence holds. What this finding actually did is work
out that already-flagged-equivalent convention *in explicit detail*
(deriving `[C]`'s units, re-deriving the field equation with `C`
present, and connecting it to `E_self`) — a real, useful piece of
bookkeeping, but not an independent discovery of the equivalence itself.
Also corrected: the "two independent routes agree" verification (§2) is
a **tautology** under this finding's own substitutions (`C=1/A`,
`φ_true=A·φ_raw`) — algebraically guaranteed to match, not an independent
check — and Route 2's stated formula was missing the canonical `1/2`
factor. The title and §2 are corrected below; §0's own honest-scope
framing was already adequate and is unchanged. See the Skeptic Verdict
section for the full breakdown.

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
symbolically. **[Corrected after skeptic review — struck through below,
the original framing overstated this.]**

~~This is a genuine cross-validation of P21, arrived at from action-level
first principles (dimensional consistency + Euler–Lagrange), not a
restatement of P21's own force-matching argument.~~

P21's own §2 (corrected) already states this equivalence directly —
`(1/(2A))(∂φ)²` as an alternative, physically identical convention was
named there, not discovered here. What this section actually shows is
that *carrying that already-flagged equivalence through explicitly* — real
units for `C`, a real re-derivation of the field equation with `C`
present — reproduces `φ_true=A·φ_raw` with no inconsistency. A useful
consistency check that the two conventions really are interchangeable in
detail, not merely asserted — but not an independent discovery of the
equivalence itself.

**Conclusion, corrected**: the claim that every "missing normalization
constant" flagged since P14 §6 is the same unknown, `A`, was **already
stated** in `FINDING_P21` §4 (*"the same missing constant `A` enters
it"*) and `FINDING_P26` §2 corrected (*"the same one P14 §6, P17, P21,
and P22 already flagged"*). This finding's real contribution is narrower
and more concrete: an **explicit formula** — `C=1/A`, and (below)
`E_self,physical=A·p²/(12πr_min³)` — connecting that already-identified
shared unknown to `E_self` for the first time, not the unification claim
itself.

**Applying this to `E_self`:**

```
Route 1:  A · E_self,correct(P26) = A · p²/(12πr_min³)
Route 2:  (C/2) · ∫(∇φ_true)²dV   (direct kinetic-term energy density)
```

**[Corrected after skeptic review]** These were originally presented as
"two independent routes" that "agree with each other." **They are not
independent.** Substituting this finding's own definitions
(`C=1/A`, `φ_true=A·φ_raw`) into Route 2 gives
`(1/(2A))·A²·∫(∇φ_raw)²dV = A·(1/2)∫(∇φ_raw)²dV = A·E_self,correct(P26)` —
*algebraically identical* to Route 1, guaranteed by construction, not an
independent check. (The original Route 2 formula also omitted the
canonical `1/2` factor from the kinetic-term energy density, now added
above.) What *is* genuinely verified — via sympy, not by hand — is that
`A·E_self,correct(P26)` carries exactly energy units (`kg·m²/s²`), which
was not obvious before this finding traced through `A`'s exact power.

`E_self,physical = A·p²/(12πr_min³)` is dimensionally an energy for the
first time in this project — **a statement about units, not about a
numeric value**. `ρ_φ=n·E_self,physical` and `Ω_φ=ρ_φ/ρ_crit` are now
dimensionally well-posed formulas, ready to become a true dimensionless
number *once `A`'s numeric value is known* — which this finding does not,
and cannot, provide.

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
   is narrowly about the normalization-constant bookkeeping.
5. **[Added after skeptic review] That the unification claim itself
   (one shared unknown, not several) is new.** `FINDING_P21` §4 and
   `FINDING_P26` §2 corrected both already stated this. This finding's
   contribution is the explicit `C=1/A` formula and its consequence for
   `E_self`, not the underlying unification insight.
6. **[Added after skeptic review] That the "two independent routes"
   verification is an independent check.** It is a consistency check
   under this finding's own substitutions, algebraically guaranteed to
   match — see §2's correction.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   of P1's action, not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P27_unify_normalization_constant.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `two_field_action_closure.py`,
`FINDING_P21_shared_phi_normalization_constraint.md` (corrected), and
`FINDING_P26_stress_tensor_equation_of_state.md` (corrected) — no session
history. The skeptic independently re-derived the Euler-Lagrange step for
the *dipole* coupling by hand (this finding's own Step 4 explicitly
derives only the monopole case and asserts "the same argument applies to
the dipole term" without showing it) — confirmed correct, no hidden
sign or power-of-`C` asymmetry between sectors. Six sub-verdicts, per
Step 8a (not merged):

- **(a)** `[C]=1/G`'s units: **CONFIRMED-REAL**, but follows immediately
  from P21's own `[φ]=m²/s²` — not independent new input, dimensional
  bookkeeping downstream of P21.
- **(b)** Field-equation re-derivation (monopole + dipole): **CONFIRMED-REAL**
  — independently re-derived the dipole case by hand (this finding's own
  text left it unshown), no asymmetry found.
- **(c)** "Genuine cross-validation of P21... not a restatement":
  **WEAKENED — the sharpest overreach**, quoting P21 §2 (corrected)
  verbatim: *"the identical physics results from placing an equivalent
  factor in the kinetic term instead."* P21 already stated this
  equivalence; this finding works it out in detail, it does not discover
  it independently. *Applied: FIXED — title and §2 corrected.*
- **(d)** "`E_self,physical=A·E_self,correct(P26)`, verified by two
  independent routes": **WEAKENED** — the two routes are not independent;
  substituting this finding's own `C=1/A` definition into Route 2 reduces
  it algebraically to Route 1, a tautology under the finding's own
  substitutions, not two separate checks. Also found: the original Route
  2 formula omitted the canonical `1/2` kinetic-term factor. *Applied:
  FIXED — §2 corrected, both issues stated explicitly.*
- **(e)** "All five... flags are the same single unknown": **WEAKENED** —
  already stated in `FINDING_P21` §4 and `FINDING_P26` §2 corrected; not
  a new claim of this finding. *Applied: §2's conclusion and §3 corrected
  to attribute the unification claim to those findings, narrowing this
  finding's own contribution to the explicit `C=1/A` and `E_self` formulas.*
- **(f)** Adequacy of the "honest limit" framing: **WEAKENED** — §0/§3's
  disclaimers are accurate, but §2's result narrative ("genuine energy...
  for the first time," "genuine cross-validation") created a stronger
  impression of numeric progress than the disclaimers alone convey.
  *Applied: §2's language brought in line with §0/§3 throughout.*

**Not a core-predicate-false kill.** Every piece of mathematics survives
independent re-derivation intact — `[C]=1/G`, the field equation for both
sectors, `A=1/C`, and the units of `A·E_self,correct(P26)`. What was
withdrawn is entirely about *framing*: presenting a detailed working-out
of an already-known equivalence as an independent discovery, and
presenting an algebraically-guaranteed consistency check as two separate
verifications. The skeptic's own summary: *"a real, useful piece of
bookkeeping, but not a discovery."*
