# P54 — Step B1: the Einstein 0i momentum constraint, `G_0i^(1)=2∂_i(Ψ̇+HΦ)`, curl-free and vanishing in the static limit — geometry only, not the matter Euler equation

**Date:** 2026-08-17
**Status:** Built, run, ruff clean, all assertions pass. **Skeptic review
(Step 8a): COMPLETE. Not a true kill — the formula itself is correct
(independently hand-derived by the skeptic from first principles, and
independently re-verified by standalone sympy execution before accepting
any correction), but two of the three internal checks supporting it were
substantially weaker than claimed — one a Schwarz-theorem tautology, one
essentially non-functional in this sympy version. Both fixed with real
computation. See Skeptic Verdict below.**
**Origin:** first sub-step of the user's refined "Euler/`G_matter`"
milestone — explicitly split into **B1** (Einstein 0i momentum
constraint) and **B2** (matter Euler equation from the coupled action),
checked for compatibility afterward, rather than treated as "one 0i
calculation." The user's own correction: `G_0i=8πG·T_0i` is the momentum
*constraint* (part of the Einstein equations' geometry side), not the
matter Euler equation itself — conflating the two is one of the user's
seven pre-registered kill-gates for this whole milestone.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P54_einstein_0i_momentum_constraint.py`, ruff clean, all
assertions pass.

## Scope, stated up front

This file supplies **only** the Einstein momentum-constraint side (LHS
geometry) of the milestone. It is explicitly **not** the matter Euler
equation (KG-B1a) — that requires varying the coupled matter+`φ` action
directly (`∇_μT_m^μν=Q^ν`, `Q` sourced by the `g·ρ·φ` coupling), a
separate, not-yet-started step (**B2**). Comparing B1's `G_0i` to B2's
matter momentum-conservation equation to extract `G_matter(a,k)` and test
the user's own pre-registered H0/H1/H2 split is a third, also
not-yet-started step (the compatibility check) — none of that is
attempted here, kept out of scope per this campaign's established
granularity (cf. the P46/P47/P48/P49 split for the same reason).

## Pre-registered claim for this file

**C1 — curl-free gradient structure.** `G_0i^(1)`, for this scalar-only
perturbation ansatz (no vector d.o.f. anywhere in P38–P53's own metric
convention), must have the required gradient/curl-free structure:
`G_0i^(1)=∂_i[F]` for some scalar `F` built from `Φ,Ψ` and their
time-derivatives — forced by general covariance whenever the metric
perturbation itself carries no vector mode, checked directly, not merely
cited.
**C2 — fails.** Some sign/coefficient/structural inconsistency is found
(the curl does not vanish), signaling either an algebra error or a
genuinely vector-sourced piece this ansatz should not have.

## Kill-gates applicable to this file (subset of the user's seven)

**KG-B1a:** do not mistake `G_0i` for the matter Euler equation itself —
stated explicitly throughout, this is geometry only.
**KG-B1b:** continuity/momentum-constraint conventions must not silently
mix gauges — this file stays in the same conformal-Newtonian gauge
P46–P53 have used throughout (`h_00=-2Φ, h_ii=-2Ψ`, zero shear/vector
modes), stated explicitly.
**KG-B1c:** `θ=0` (irrotational dust) must not be substituted here — not
applicable, this file contains no matter-sector variable at all, only
the metric/geometry side.

## Part 1 — same exact perturbed FRW metric as `FINDING_P48`, reused verbatim

```
ds² = −(1+2εΦ)dt² + a²(1−2εΨ)(dx²+dy²+dz²)
```

`christoffels_exact`, `ricci_exact`, and the `G(μ,ν)` helper are reused
**verbatim** from `FINDING_P48`'s own already-verified code (same
positive controls — background Ricci vs. textbook FRW; `G_00`/`G_12`
already verified — apply unchanged, not re-run here to avoid duplicating
P48's own work). `FINDING_P48` computed the full upper-triangle
`R_components` dict (all `μ≤ν` pairs, including `(0,1)`) but only
extracted `G_00` and `G_12` — `G_01` was already implicitly available,
simply never pulled out. This file pulls it out.

## Part 2 — extract linearized `G_01`

```
G_01^(1) = 2∂_x(Ψ̇) + 2(ȧ/a)∂_x(Φ) = 2∂_x(Ψ̇+HΦ)
```

## Part 3 — C1/C2: curl-free structure, checked directly

`G_02^(1)`, computed independently from the same `G(μ,ν)` machinery (not
via a symbol-swap trick — sympy's `subs` on `Function`/`Derivative`
objects proved unreliable for that during the build, caught and fixed by
computing `G_02` fresh instead):

```
G_02^(1) = 2∂_y(Ψ̇+HΦ)   (script assertion: matches exactly, isotropy confirmed)
```

Curl check:

```
∂_y(G_01) − ∂_x(G_02) = 0   (script assertion)
```

~~**Confirmed: `G_0i^(1)` is curl-free**, consistent with a pure scalar
source — no hidden vector-mode contamination.~~

**[CORRECTED after context-blind skeptic review, Step 8a]** The curl
vanishing here is **not independent evidence** beyond the isotropy
assertion just above: once `G_02` is asserted to equal `G_01`'s own
pattern with `x→y` (a real, non-trivial check on its own, verified
against the independently-computed `G(0,2)`), the curl vanishing is then
a **Schwarz-theorem tautology** (`∂_y∂_x[F]−∂_x∂_y[F]=0` for *any* scalar
`F`, whether `F` is the physically correct one or not) — it cannot fail
once isotropy is confirmed, and adds zero independent evidence for the
formula's own correctness. Retracted as originally overclaimed. Curl-free
structure and isotropy remain confirmed; this does not by itself verify
the formula's coefficients/signs.

## Part 4 — explicit scalar potential

Integrating `G_01^(1)` with respect to `x` recovers, up to a
`t,y,z`-dependent integration constant (checked to be genuinely
`x`-independent — `∂²F/∂x²` reduces to the same expression as the
original integrand's own `x`-derivative structure, not a spurious
residual):

```
F = 2H·Φ + 2Ψ̇
```

## Part 5 — [CORRECTED after context-blind skeptic review, Step 8a] direct independence checks, replacing a non-functional substitution check

~~A genuinely static spacetime (all time-derivatives of `Φ,Ψ,a` vanish)
has no momentum flux — `G_0i^(1)` must vanish identically. A cheap,
genuinely discriminating check (a formula with a stray non-time-
derivative term would fail this): `G_01^(1)|_{Φ̇=Ψ̇=ȧ=0} = 0` (script
assertion). **Confirmed.**~~

The original substitution-based "static limit" check
(`G01_lin.subs({∂Ψ/∂t:0, ∂Φ/∂t:0, ∂a/∂t:0})`) was claimed to catch
spurious extra terms. **Independently re-verified via a standalone sympy
script, before accepting the skeptic's critique**, that this claim was
wrong: in sympy 1.14.0, `.subs()` on a first-derivative `Derivative`
object propagates through nested/higher derivatives in a way that
silently zeroes out terms it should *not* catch. Six deliberately-wrong
variants of the formula were tested (wrong coefficient, wrong sign,
missing term, an extra `Ψ̈` term, an extra `ä` term) and **all six passed
the substitution-based check trivially** — including cases the skeptic
itself did not expect to pass. The check had essentially zero
discriminating power, not merely "weaker than claimed." Retracted, not
merely reframed.

**Replaced** with the same direct-independence-assertion pattern
`FINDING_P48` already established (after its own skeptic review) for
`G_12` — checking the coefficient of each higher-derivative atom directly
via `sp.diff()`, not via a substitution that can silently propagate
through nested `Derivative` objects:

```
d(G_01^(1))/d(Ψ̈) = 0
d(G_01^(1))/d(Φ̈) = 0
d(G_01^(1))/d(ä) = 0     (all three: script assertions)
```

**Confirmed, all three** — genuinely discriminating (a formula *with*
such a term, e.g. the "extra `Ψ̈`" variant independently tested above,
would have a nonzero derivative here and fail this specific check).

**Honest limitation, stated explicitly:** these independence checks, like
the retracted substitution check, do **not** by themselves rule out a
wrong coefficient or sign on the surviving `Ψ̇`/`HΦ` terms (e.g.
`5HΦ_{,x}` instead of `2HΦ_{,x}` would pass every check in this file
identically). The strongest evidence for the formula's correctness
remains reuse of `FINDING_P48`'s own already-verified exact
Christoffel/Ricci machinery — no genuinely external (textbook-citation)
check is attempted here, deliberately, per `FINDING_P48`'s own
convention-labeling caveat (`Φ`/`Ψ` role assignment is not universal
across sources) — a real, stated gap, not resolved by this finding.

## Verdict [CORRECTED after context-blind skeptic review, Step 8a]

**C1 confirmed, with two evidentiary corrections applied.**
`G_0i^(1)=2∂_i(Ψ̇+HΦ)`, derived from the same exact-metric +
eps-linearization machinery `FINDING_P48` already verified (reused
verbatim), has the required curl-free gradient structure for a
scalar-only perturbation — though the curl check itself is a
Schwarz-theorem tautology given the isotropy assertion, not independent
evidence (retracted from the original overclaim). The formula has zero
dependence on any second time-derivative (replacing a substitution-based
static-limit check independently shown to have ~zero discriminating power
in this sympy version). Neither check rules out a wrong coefficient or
sign on the surviving terms — stated as an honest, unresolved limitation.
The strongest evidence for correctness remains reuse of `FINDING_P48`'s
own already-verified exact Christoffel/Ricci machinery. No genuinely
external (textbook-citation) check is attempted here, deliberately, per
`FINDING_P48`'s own convention-labeling caveat — a real, stated gap for a
future step to close if needed.

This supplies only the Einstein momentum-constraint side of the
milestone. B2 (matter Euler equation) and the B1↔B2 compatibility check
(which will test the user's own pre-registered H0/H1/H2 split —
full linear degeneracy / real fifth-force growth channel / closure
requires missing matter-sector structure) are separate, not-yet-started
steps.

## What this establishes, precisely

1. `G_0i^(1)=2∂_i(Ψ̇+HΦ)`, in the same conformal-Newtonian gauge and
   metric convention used throughout P46–P53.
2. The curl-free structure required by general covariance for a
   scalar-only perturbation, verified computationally (not cited from a
   specific textbook equation, avoiding a possible sign/convention
   mismatch with an external source).
3. A clean example of reusing already-verified machinery (`FINDING_P48`'s
   Christoffel/Ricci/Einstein-tensor code) for a new extraction, matching
   this campaign's established anti-hand-algebra discipline.

## What this does NOT establish

1. **The matter Euler equation.** B2, not yet started.
2. **`G_matter(a,k)`, or any test of the user's H0/H1/H2 split.** Requires
   B2 and the compatibility check.
3. **Anything about `μ_metric` or `Ag²`'s numeric value.** Unrelated to
   this file's scope.
4. **A citation to a specific external textbook formula for `G_0i`.**
   Deliberately avoided, to prevent a possible sign/labeling-convention
   mismatch (per `FINDING_P48`'s own explicit note that `Φ`/`Ψ`'s roles
   are not universally labeled the same way across sources) — a real,
   acknowledged gap, not resolved here; a future step could close it via
   an independent Bianchi-identity derivation from `FINDING_P48`'s own
   already-verified `G_00`/`G_ij`, a genuinely different computational
   route, if a stronger anchor is ever needed.
5. **That a wrong coefficient or sign on the surviving `Ψ̇`/`HΦ` terms is
   excluded.** Neither the curl check nor the independence checks catch
   this error class — stated explicitly, not smuggled past.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Central formula `G_0i^(1)=2∂_i(Ψ̇+HΦ)` | **CONFIRMED-REAL** — independently hand-derived by the skeptic from Christoffel/Ricci first principles, matches exactly | No change. |
| Machinery reuse from `FINDING_P48` (verbatim) | **CONFIRMED-REAL** — character-by-character check, byte-identical `christoffels_exact`/`ricci_exact`/`G(μ,ν)`/metric ansatz | No change. |
| Scope discipline (KG-B1a/b/c: geometry not Euler equation) | **CONFIRMED-REAL** — correct GR terminology, no conflation | No change. |
| Curl check "checked directly, not merely cited" | **WEAKENED** — once `G_02`'s form is asserted (isotropy), the curl vanishing is a Schwarz-theorem tautology, zero independent evidence | **Fixed.** Reframed explicitly; downgraded from independent evidence to a consequence of the isotropy check. |
| Static-limit check "genuinely discriminating" | **WEAKENED**, then **independently re-verified to be essentially non-functional** (not merely weaker than claimed) via a standalone sympy test of six deliberately-wrong variants, all of which passed trivially | **Fixed.** Replaced with direct independence assertions (`∂G_01/∂Ψ̈`, `∂G_01/∂Φ̈`, `∂G_01/∂ä`, matching `FINDING_P48`'s own hardened pattern for `G_12`), genuinely discriminating for that error class; honest limitation stated for the coefficient/sign class neither check catches. |
| Part 4 "`d²F/dx²` should be 0" comment | **MINOR — confused reasoning**, wrong on the physics (F genuinely retains x-dependence) though not asserted, so no runtime failure | **Fixed.** Removed the misleading printout, replaced with an honest description of what the integration-consistency assertion actually shows. |
| Missing external validation (vs. `FINDING_P48`'s two genuinely external controls) | **WEAKENED** — this file relies entirely on internal checks; the convention-mismatch worry is real but doesn't preclude *all* external anchoring | **Accepted as an open gap**, not fixed in this pass — stated explicitly in "What this does NOT establish," with a concrete candidate route (Bianchi identity from already-verified `G_00`/`G_ij`) named for a future step if needed. |
| sympy version / `.subs()` propagation behavior | **Flagged as a potential reproducibility issue** — behavior may differ across sympy versions | **Addressed indirectly** — the fix (direct `sp.diff()` independence assertions) no longer depends on the `.subs()` propagation behavior that caused the original check to be non-functional. |

**True kill assessment:** no. The central formula is correct (independently
hand-derived by the skeptic, and independently re-verified via standalone
sympy execution before accepting any correction, per this campaign's
`audit-verification-gate.md` discipline). What required correction was
the *evidentiary strength* of two of the three supporting checks, not the
formula itself — a real, non-trivial correction (one check was retracted
entirely as non-functional, not merely reframed), but qualitatively
different from P51/P52's true-kill-adjacent verdicts, where the core
claim itself did not survive.

## Reproduction

```bash
python experiments/20260803-bridge/P54_einstein_0i_momentum_constraint.py
```
