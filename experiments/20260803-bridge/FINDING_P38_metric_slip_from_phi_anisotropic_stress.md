# P38 — solving the sourced trace-free ij Einstein equation for the metric slip Φ−Ψ, from a self-contained linearized-Einstein-tensor derivation

**Date:** 2026-08-14
**Status:** Built, run, self-caught-and-fixed one sign error, ruff clean.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** fifth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction ("продолжай, но
медленнее — по одному шагу за раз", reaffirmed this session as "продолжай
P38, медленно"). Directly picks up the step P37 identified but explicitly
declined to complete: P37 showed `φ`'s own static stress tensor has
genuine anisotropic stress at `O(ĝ²)` and stated the *qualitative*
uniqueness principle (`Φ=Ψ` would require a non-standard boundary
condition), but explicitly refused to adopt the skeptic reviewer's own
independently-computed closed-form value for `Φ−Ψ`, per
`audit-verification-gate.md` ("Agent's `[VERIFIED]` is your
`[INFERRED]`"). This finding does that derivation itself, so the result
is this project's own `[VERIFIED-SYMPY]`, not an adopted, unverified claim.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P38_metric_slip_from_phi_anisotropic_stress.py`, ruff clean,
all assertions pass.

## 0. Honest scope — deliberately narrow, one new ingredient only

This solves the trace-free spatial (`ij`) sector of Einstein's equations,
sourced *only* by `φ`'s own stress tensor (P37's `T_ij`, re-used, not
re-derived), for the static, weak-field, point-source configuration
already used throughout P34–P37. It does **not**:

- solve the `00` or `0i` sectors of Einstein's equations for this source
  (only the Newtonian-limit `G_00` reduction is checked, as a *positive
  control*, not solved as part of this finding's own result);
- include any *other* matter's stress-energy (a real gravitating system —
  e.g. the point mass `M` itself, modeled here only as `φ`'s own source —
  also has its own ordinary baryonic stress-energy; this finding's `Φ,Ψ`
  are the piece sourced *by `φ`'s field alone*, not the full physical
  metric of a real two-component system);
- go beyond leading `O(ĝ²)` order, or address any backreaction of this
  slip on `φ`'s own equation of motion (P35's field, re-used unchanged);
- compare the result to any observational `Σ(a,k)`/`γ(a,k)` parametrization
  or to Table A1 (Gate 2, Target Provenance, already closed this project —
  Table A1 is AI-fitted output, not TJB's own calculation, `table_a1_is_
  ai_output.md`).

**The one new physics ingredient this step adds beyond P34–P37:** rather
than *cite* a textbook coefficient for the weak-field trace-free `ij`
Einstein equation (a phantom-citation risk this project's own evidence
policy explicitly warns against — trusting a remembered number), this
finding *derives* the linearized Einstein tensor directly, from the
metric ansatz itself, and checks it against a known result (Gate 3,
Positive-Control Digitization) before trusting the new (`ij`-sector)
result built from the same code path.

## 1. Method — self-contained linearized-Einstein-tensor derivation

Metric ansatz (standard weak-field form, static, Cartesian, same
mostly-plus signature already implicit in P37's own `T₀₀=(1/2)(∂φ)²`):

```
ds² = -(1+2Φ(x,y,z))dt² + (1-2Ψ(x,y,z))(dx²+dy²+dz²)
```

Linearized-gravity shortcut used (standard, not an approximation invented
for this project): each Christoffel symbol `Γ^λ_μν` is already `O(Φ,Ψ)`,
so any *product* of two Christoffels is `O((Φ,Ψ)²)` and drops out
identically at linear order — the Ricci tensor reduces to
`R_μν=∂_λΓ^λ_μν−∂_νΓ^λ_μλ`, with no `Γ·Γ` term. This is implemented via
direct index loops (30 of 64 Christoffels nonzero, found by the
computation itself, not assumed) rather than a hand-shortcut, to avoid
silently dropping a term.

**Positive control (Gate 3, run before trusting the `ij`-sector result):**
`G₀₀` derived from this same code reduces *exactly* to `2∇²Ψ`, matching
the single most well-established fact in weak-field GR — the Newtonian
limit `G₀₀=8πG_N T₀₀` gives the ordinary Poisson equation. Confirmed by
direct symbolic comparison (script assertion, exact zero difference), not
eyeballed. This is the same convention family used throughout P34–P37
(`G_N` — standard, unmodified Newton's constant, per P34's own explicit
flag never to silently assume a gravitational sector).

**Self-consistency check:** setting `Ψ=Φ` (no slip) makes the trace-free
`ij` part vanish identically for *any* smooth `Φ` — the textbook "no
anisotropic stress ⇒ no slip" statement, confirmed directly against this
derivation (not assumed), and confirming the trace-free part depends only
on the *difference* `Φ−Ψ`, matching the structure P37 §0 already
anticipated qualitatively.

## 2. Solving the sourced equation

`Σ_ij` (P37's traceless `T_ij`, re-used unchanged) and the derived
`[G_ij]_tracefree` both have the same pure-quadrupole (`l=2`) angular
structure, so the ansatz `Φ−Ψ=C/r²` is motivated (not guessed blind —
`trace-free[∂_i∂_j(1/r²)]` produces exactly the `x_ix_j/r⁶−(1/3)δ_ij/r⁴`
structure `Σ_ij` has). Setting `[G_ij]_tracefree(ansatz) = 8πG_N·Σ_ij`
(standard Einstein-equation normalization) and solving symbolically
(`sympy.solve`, not hand algebra) gives:

```
C = -G_N·ĝ²·M² / (16π)
```

**Independent verification (a genuinely different code path from the
solving step):** substituting this `C` back into the *full* symbolic
trace-free equation and checking all 9 `(i,j)` components at a *generic*
point `(x,y,z)` — not just the single component/axis used to solve for
`C` — gives an exact zero residual for every component (script
assertion). This is the check P37 itself declined to do for the
reviewer's own unverified closed form; here it is done for this
finding's own derivation, by a different route than the one that
produced the number.

## 3. Result

```
Φ − Ψ = -G_N·ĝ²·M² / (16π·r²)     (r > 0, leading O(ĝ²) order)
```

**Sign: negative for all `r>0`** (`G_N, ĝ², M² > 0`, and the solved
coefficient carries an overall minus sign) — this reconstruction's slip
has `Ψ > Φ` at this order, i.e. the "lensing" potential `(Φ+Ψ)/2` differs
from the dynamical potential `Ψ` in a *specific, computed* direction, not
an unspecified "nonzero somewhere."

### Self-caught error, corrected before this write-up

The script's first draft solved for `C` correctly (Step 7's `sympy.solve`
call was always right) but its own hardcoded final "VERDICT" print
statement asserted **`Φ−Ψ > 0`** — the *opposite* sign from the actually
solved, negative `C`. This is a narrative-text bug, not a computation
bug: the independent verification (Step 8, residual check against the
*correct* negative `C`) had already passed cleanly before the mistaken
print statement was even reached. Caught by re-reading the script's own
printed `C_solved` value against its own printed sign claim before
writing this document — not by the skeptic (this review has not yet
run). Fixed by replacing the hand-typed sign claim with a computed
`C_solved.is_negative` check and a new script-level assertion, so this
specific mistake cannot silently recur on a re-run. Consistent with this
campaign's established pattern (P6, P9, P37) of scripts catching their
own arithmetic before a human or skeptic has to.

## 4. What this establishes, precisely

Given (a) the standard, unmodified Einstein-Hilbert gravitational sector
P34 explicitly chose and flagged, (b) P35's already-derived static field
`φ(r)=ĝM/(4πr)`, and (c) P37's already-derived, now-reused `T_ij`, the
trace-free spatial Einstein equation has a **unique, closed-form
solution** for the metric slip sourced by `φ`'s own stress-energy:
`Φ−Ψ=-G_N ĝ²M²/(16πr²)`. This sharpens P37's own "genuinely open"
status (a source exists, magnitude/sign not yet computed) to a specific,
computed value — the natural endpoint of the chain P37 deferred.

## 5. What this does NOT establish

1. The metric of any *real*, physically complete two-body or cosmological
   system — only the piece of the slip sourced by `φ`'s own field, in
   isolation from any other matter stress-energy.
2. Anything about observational structure-growth parameters `μ,γ,Σ` (the
   campaign plan's own next table row) — this is a static, two-body
   result, not yet embedded in a cosmological perturbation framework.
3. Anything about Table A1 or TJB's own unpublished gravitational
   equations (Gate 1/Gate 2, closed) — `G_N` here is the standard,
   unmodified Newton's constant, not fitted to or compared against any
   published number.
4. Resolution of the `r→0` point-source divergence (`T_ij~1/r⁴`, already
   flagged in P37) — `Φ−Ψ~1/r²` inherits and compounds this divergence;
   not addressed here, same standard point-source caveat as P14–P19.
5. Whether this specific slip signature is large enough to matter next to
   any existing bound (P22/P31's phenomenological ceilings) — no
   numerical comparison against those ceilings is attempted in this
   finding; that would be a natural, separate next step, not assumed here.

## Reproduction

```bash
python experiments/20260803-bridge/P38_metric_slip_from_phi_anisotropic_stress.py
```
