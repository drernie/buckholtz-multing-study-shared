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

**[CORRECTED after skeptic review, same day.] §2's force-matching step was
wrong: it equated monopole exchange to the FULL Newton force
(`A·g²=4πG`). `two_field_action_closure.py`'s own text calls `φ` "**a fifth
force, not gravity**" and says its exchange "**renormalises `G` (attractive,
absorbed)**" — standard fifth-force phrasing for a *small* addition to an
already-existing `G`, not that `φ`-exchange supplies all of it. "Fifth
force" presupposes gravity already exists separately; the original equation
silently set `G_bare=0`, contradicting the source's own wording. Corrected
below to `A·g²=4π·ΔG`, `ΔG≪G` required. Two further framing overclaims
softened (§1: "not by construction" downgraded; g's dimensionlessness
reclassified from established fact to stated assumption). See Skeptic
Verdict section at the end for the full five-way breakdown.**

## 1. What this checks

P1's action (`two_field_action_closure.py`):

```
S = ∫d⁴x (1/2)(∂φ)² + Σᵢ ∫dτ [ g·mᵢ + pᵢ·∇ ] φ(xᵢ),   pᵢ = κ·kᵢ·rᵢ/c²
```

Two coupling terms share the same field `φ` and the same canonical kinetic
term. Each independently requires `[g·m·φ]` = energy and `[p·∇φ]` = energy.
`κ` is dimensionless (established in P14). **`g`'s dimensionlessness is an
assumption made here, not established in any cited prior finding** — P13a
names `g` as independent of `κ` and structurally matching Archidiacono's `β`,
but does not fix `g`'s units. Taking `g` dimensionless (matching `κ`'s
convention) as a working assumption, each coupling separately fixes what
`[φ]` must be. **This project had never checked whether those two
independently-derived requirements actually agree** — that is the first thing
this script verifies, symbolically (sympy exponent bookkeeping on kg/m/s), not
assumed. **[Softened after skeptic review]** — the agreement is real but less
surprising than first framed: both derivations share the same underlying
premises (dimensionless couplings, standard scalar-action energy bookkeeping,
a single `φ`), so the match is close to guaranteed by that shared structure,
not an independent discovery.

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

`A` carries exactly Newton's-`G` units given this placement of the missing
factor — it falls out of the shared-`φ` consistency requirement, not
guessed. **[Softened after skeptic review]** — this placement (the missing
factor living in the coupling normalization, `φ_true=A·φ_raw`) is a
convention, not a forced discovery: the identical physics results from
placing an equivalent factor in the kinetic term instead (`(1/2A)(∂φ)²`).
What is convention-independent is only that *some* factor with `G`'s units
must exist *somewhere* in the action; *where* it formally lives is a choice.

**[CORRECTED after skeptic review — this paragraph originally equated
monopole exchange to the FULL Newton force, which is wrong; struck through
below, corrected version follows.]**

~~Taking P1's own "renormalises `G`, absorbed" claim as a literal
force-matching condition — the monopole exchange force between two masses
must equal Newton's law — gives: `A * c_G * g² = G` , `c_G = 1/(4π) (P19)`
=> `A * g² = 4πG`~~

`two_field_action_closure.py`'s own text calls `φ` "a **fifth force**, not
gravity" and describes its m-m exchange as "renormalises `G` (attractive,
**absorbed**)." "Fifth force" is a term of art that presupposes gravity
already exists independently of `φ`; "absorbed" is standard phrasing for a
*small* shift to an already-measured `G`, not for `φ`-exchange being the sole
source of `G`. The corrected target is:

```
A * c_G * g² = ΔG   ,   c_G = 1/(4π) (P19),  ΔG ≪ G required
=>  A * g² = 4π·ΔG
```

where `ΔG` is the (small, currently unmeasured here) fifth-force contribution
to the observed `G` — not `G` itself.

## 3. What this does NOT do

**One equation, THREE unknowns (`A`, `g`, `ΔG`) — corrected from "two
unknowns" after skeptic review.** The original two-unknown framing implicitly
fixed `ΔG=G`, which §2's correction shows was not licensed. This derivation
narrows the space (units of `A` fixed; `g` must be small, consistent with the
source's own "fifth force" framing) but does **not** produce a numeric value
for `A`, `g`, or `ΔG` — that requires independent input. P13a already named
the natural candidate: Archidiacono et al.'s external `β<0.0054` (95% CL)
bound on a scalar monopole fifth force is, per P13a §2, a bound on this same
`g` — and, now correctly read, a *small* bound on `g` is exactly what the
"fifth force" framing predicts, not an awkward retrofit. But turning that
into a numeric value of `g` (and hence, via `A·g²=4π·ΔG`, of `A`) still
requires verifying Archidiacono's own definition of `β` against the actual
paper's equations, which has **not been done here**. This is the concrete
next step, not a result of this finding.

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
4. **[Added after skeptic review] That `g` is dimensionless.** This is a
   working assumption (matching `κ`'s established convention), not something
   established in any cited prior finding.
5. **[Added after skeptic review] That `A`'s placement is a discovery rather
   than a convention.** Only the existence of *some* missing `G`-units factor
   somewhere in the action is convention-independent.
6. **[Added after skeptic review] That `φ`-exchange sources any particular
   fraction of the observed `G`.** Corrected §2 requires only `ΔG≪G` (fifth-
   force phenomenology); this finding does not bound `ΔG` numerically.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   P1's action, not a claim about any error in TJB's own theory.

## Reproduction

```bash
python experiments/20260803-bridge/P21_shared_phi_normalization_constraint.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `two_field_action_closure.py`,
`FINDING_P14_kappa_normalization_unfixed.md`,
`FINDING_P19_greens_function_normalization_derived.md`, and
`FINDING_P13a_archidiacono_bound_scope.md` — no session history. Five
separate sub-verdicts, per Step 8a (not merged):

- **S1** (§1, shared-`φ` dimensional match): **CONFIRMED-REAL** (math) /
  **WEAKENED** (framing) — the match is correct but close to guaranteed by
  the shared premises (dimensionless couplings, single `φ`, standard scalar
  bookkeeping), not an independent discovery as originally framed. *Applied:
  softened.*
- **S2** (§2, `A` carries `G`'s units): **CONFIRMED-REAL** (math) /
  **WEAKENED** (interpretation) — correct given the coupling-normalization
  placement, but that placement is a convention, not a forced result; an
  equivalent factor could live in the kinetic term instead. *Applied:
  softened, caveat added to §5.*
- **S3** (§2, `A·g²=4πG` via literal force-matching): **FALSIFIED** — the
  source's own "fifth force, not gravity" / "renormalises `G`... absorbed"
  language denies `G_bare=0`; "fifth force" presupposes gravity already
  exists separately. *Applied: FIXED — corrected to `A·g²=4π·ΔG`, `ΔG≪G`
  required, per the response matrix (this was a genuine core-mechanism
  error, not a defensible reading; verified by re-reading the exact cited
  source text before accepting the correction).*
- **S4** (§3, one-equation-multiple-unknowns honesty): **CONFIRMED-REAL** —
  correctly and honestly stated in the original; now updated to three
  unknowns (`A`,`g`,`ΔG`) reflecting S3's fix.
- **S5** (§5, "what this does NOT establish" completeness): **WEAKENED —
  INCOMPLETE** — three material caveats were missing (g's dimensionlessness
  assumed not established; A's placement convention-dependent; the S3
  `G_bare=0` assumption). *Applied: all three added.*

**Not a core-predicate-false kill.** The shared-`φ` dimensional argument and
`A`'s required units survive; only the specific numeric force-matching
equation required correction, and the fix strengthens rather than weakens
the finding's connection to P13a — a small `g` (bounded by something like
Archidiacono's `β`) is exactly what "fifth force" phrasing predicts, rather
than the awkward, unlicensed `G_bare=0` reading the original version needed.
