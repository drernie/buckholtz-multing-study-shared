# P38 — solving the sourced trace-free ij Einstein equation for the metric slip Φ−Ψ, from a self-contained linearized-Einstein-tensor derivation

**Date:** 2026-08-14
**Status:** **CORRECTED after context-blind skeptic review, same day.**
Core numeric result `Φ−Ψ=-G_N·ĝ²·M²/(16π·r²)` **survived intact** — the
reviewer independently re-derived the linearized Einstein tensor by hand
and confirmed it. Two framing overclaims were found (not physics bugs)
and both were given a genuine *fix*, not just a caveat: the "positive
control" text was oversold, and Step 8 was mislabeled "independent" when
it shares the same code path as the solving step. A new Step 9 (a
structurally different equation — the trace, not the trace-free, part of
the sourced Einstein equation) now supplies the genuine independent
cross-check, and confirms the exact same coefficient. Full verdict in the
new §6 below.
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

**Positive control (Gate 3, run before trusting the `ij`-sector result) —
[CORRECTED, see §6]:** `G₀₀` derived from this same code reduces
*exactly* to `2∇²Ψ`, matching the single most well-established fact in
weak-field GR — the Newtonian limit `G₀₀=8πG_N T₀₀` gives the ordinary
Poisson equation. Confirmed by direct symbolic comparison (script
assertion, exact zero difference), not eyeballed. This is the same
convention family used throughout P34–P37 (`G_N` — standard, unmodified
Newton's constant, per P34's own explicit flag never to silently assume a
gravitational sector). ~~This confirms the derivation's conventions are
the standard ones — the ij-sector extraction below uses the SAME,
now-checked, code path.~~ **Corrected:** for this static ansatz, `G₀₀`
depends *only* on `Ψ`, never on `Φ` — this control validates the
`Ψ`-side conventions and the overall linearized-gravity code path, but
cannot by itself catch a `Φ`-side sign or index error in the `ij` sector.
The genuinely independent check for that is §2's Step 9, added below.

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

**Completeness check [CORRECTED label, see §6 — was called "independent
verification," is not]:** substituting this `C` back into the *full*
symbolic trace-free equation and checking all 9 `(i,j)` components at a
*generic* point `(x,y,z)` — not just the single component/axis used to
solve for `C` — gives an exact zero residual for every component (script
assertion). Valuable (rules out the ansatz being under-constrained by a
single component), but it shares the *same*
`linearized_christoffels`/`linearized_ricci`/`linearized_einstein_tensor`
code as the solving step — a latent bug in that shared code would pass
both checks identically.

**Genuine independent cross-check (added after skeptic review — Step
9):** the *trace* of the spatial Einstein equation, `G_ii=8πG_N T_ii`, is
a structurally different physical constraint than the trace-free equation
solved above — it fixes `Φ−Ψ` via the trace of `T_ij`, not the traceless
part. Solved independently for the same ansatz, it gives the *exact same*
`C`. This closes the gap the skeptic named precisely: an overall-scale
bug in how `(Φ−Ψ)` enters `G_ij` would evade *both* the `G₀₀` positive
control (involves only `Ψ`) *and* the `Φ=Ψ` self-consistency check
(insensitive to a common factor multiplying `Φ,Ψ` equally) — but would
generically break agreement between the trace and trace-free equations,
since they combine `G_ij`'s components differently. Agreement between two
structurally different equations is the genuinely independent check the
original Step 8 was mislabeled as being.

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
specific mistake cannot silently recur on a re-run. **[CORRECTED per
skeptic review — see §6:]** ~~consistent with this campaign's established
pattern (P6, P9, P37) of scripts catching their own arithmetic before a
human or skeptic has to~~ — that comparison overstated it: P6/P9/P37
caught actual arithmetic or logic errors in the computation itself; this
was a mismatched *print string*, the computation was correct throughout.
Distinct, smaller class of self-catch, not the same pattern.

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
6. Independent re-verification of `T_ij` itself (P37's own derivation,
   already skeptic-reviewed there — out of scope for *this* finding's own
   review, which took `T_ij` as a given input per its own review
   instructions). If P37's `T_ij` normalization were ever found to be
   non-standard, that error would propagate directly into this finding's
   `C`, since `T_ij` is used, not re-derived, here.

## 6. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with the finding + script, **no session history**, per
Falsification Ladder Context Asymmetry Rule. The reviewer independently
re-derived the linearized Einstein tensor by hand, hand-computed the
trace-free operator acting on `Φ−Ψ`, verified the `8πG_N` normalization
and the uniqueness of the `C/r²` ansatz, and cross-checked the numeric
value of `C` from first principles.

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | Linearized-gravity `Γ·Γ`-drop shortcut applied correctly? | CONFIRMED-REAL | No fix needed — reviewer's independent hand-derivation matched exactly |
| 2 | `G₀₀` "positive control" — does it actually validate the `ij`-sector's `Φ` conventions? | WEAKENED — real overclaim | Fixed (§1): text now states only `Ψ`-side + code-path sanity is validated |
| 3 | Is `Φ−Ψ=C/r²` the unique solution under standard boundary conditions? | CONFIRMED-REAL — reviewer independently proved the homogeneous-solution space is trivial | No fix needed |
| 4 | `8πG_N` factor and coefficient placement | CONFIRMED-REAL — reviewer's independent hand-solve reproduced `C=-G_N ĝ²M²/(16π)` exactly | No fix needed |
| 5 | Step 8 "independent verification" — genuinely independent, or same code path twice? | WEAKENED — real overclaim, shares code with the solving step | Fixed (§2): relabeled "completeness check"; genuine independence supplied by new Step 9 (trace equation), reviewer's own suggested fix |
| 6a | "Self-caught arithmetic" compared to P6/P9/P37 | Minor prose overclaim | Fixed (§3): distinguished as a narrative-text catch, not an arithmetic catch |
| 6b | `T_ij` inherited from P37, not re-verified here | Flag, not a finding (explicitly out of scope per review instructions) | Noted explicitly (§5, item 6) |
| 6c | Suggested cross-check: does `Φ_φ=0` follow from pairing with the `00`-sector solve? | Suggestion, not adopted at the time | ~~**Declined** — an independent hand-check during correction found this specific claim does *not* hold exactly (`Φ_φ` came out nonzero)~~ **[ADDENDUM, `FINDING_P40`, same day, itself skeptic-confirmed]** That hand-check was itself never mechanically verified and its own arithmetic does not survive re-derivation — `FINDING_P40` redid this properly with sympy, reusing this finding's own already-verified `G₀₀=2∇²Ψ` relation, and found `Φ_φ=0` **exactly**, confirming the skeptic's original suggestion — independently confirmed a second way by `FINDING_P40`'s own reviewer (`T₀₀+T_kk=0` for any canonical static scalar ⟹ `∇²Φ_φ=0` identically, a general result, not specific to this configuration). The exact mechanism of the original hand-check's error cannot be reconstructed from the record (an initial "factor-of-2, wrong Poisson form" guess was itself checked and withdrawn in `FINDING_P40` §2 — the two forms are algebraically equivalent, so that could not have been the actual cause). **Declining the claim at the time remained the correct process move** (an unverified claim, right or wrong, should not be adopted without independent verification) — see `FINDING_P40` §2 and §7 for the full reconciliation. |
| 6d | Sign of `ĝ` (does it matter, given `T_ij` is `ĝ²`)? | CONFIRMED-REAL — reviewer confirmed no issue | No fix needed |

**What survives:** the core numeric result — independently re-derived by
the reviewer from scratch and now additionally confirmed by a second,
structurally different equation (§2's Step 9) this finding did not
originally have. **What was corrected:** two framing overclaims (the
positive control's actual coverage; Step 8's actual independence), both
given genuine fixes rather than caveats, plus one prose overclaim.
**What was explicitly declined:** the reviewer's own suggested "`Φ_φ=0`"
embellishment — an independent check found it does not hold, so it was
left out rather than propagated unverified, per this project's own
evidence discipline. Kill classification: framing/completeness only, the
second clean survival in a row this session (after P37), the first
review to also add genuine new verification content (Step 9) rather than
only correct or caveat existing content.

**[ADDENDUM, `FINDING_P40`, same day, itself skeptic-confirmed — corrects
the paragraph above.]** The declining check on item 6c was itself never
mechanically verified. `FINDING_P40` redid it with sympy and found
`Φ_φ=0` **exactly**, matching the skeptic's original suggestion — and
independently confirmed a second, structurally different way by
`FINDING_P40`'s own reviewer, who showed `Φ_φ=0` is a general result for
any canonical static scalar (`T₀₀+T_kk=0`), not specific to this
configuration. The exact mechanism of the original hand-check's error is
not reconstructable from the record; an initial guess (a factor-of-2 from
using the generic Poisson form instead of this finding's own derived
`G₀₀=2∇²Ψ`) does not hold up — the two forms are algebraically
equivalent. Declining an unverified claim was still the right process
call at the time; the claim itself turned out to be correct. See
`FINDING_P40` §2 and §7 for the full reconciliation and §3 for what this
enables (a closed-form, nonzero slip ratio `γ`).

## Reproduction

```bash
python experiments/20260803-bridge/P38_metric_slip_from_phi_anisotropic_stress.py
```
