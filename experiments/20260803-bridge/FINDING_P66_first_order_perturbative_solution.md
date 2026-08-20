# FINDING P66 — a first-order-in-ĝ perturbative solution of the coupled background, genuinely useful at small ĝ, marginal at ĝ~1

**Status:** Skeptic-reviewed (Step 8a) and corrected. Verdict WEAKENED →
fixed with real computation (two new positive controls, a second time
point, a computed scaling analysis) and honest reframing, not just
softer wording.
**Script:** `P66_first_order_perturbative_solution.py` (`experiments/20260803-bridge/`)
**Scope:** `V=0`, background order, `ĝ≠0`. ODE derivation/closure is
`[VERIFIED-SYMPY]`; the solved `δ(t),φ̄₁(t)` and all cross-validation
numbers are `[VERIFIED-NUMERIC]`.

NOT_VALIDATION — NOT_REFUTATION — OUR_RECONSTRUCTION — L0: descriptive.

---

## Direct response to the user's request

The user asked to "attempt an actual solution of the coupled system" —
the question `FINDING_P63` opened and `FINDING_P64`/`FINDING_P65` scouted
numerically without ever constructing one. This finding builds a genuine,
verified, first-order perturbative solution — useful in a specific,
honestly-characterized regime, not a universal fix.

## Key reframing, established first

`FINDING_P65` labeled `a³φ̄̇=√2+ĝ(t-1)` a "test-field" (no-backreaction)
approximation. It is not. Verified symbolically here for a *generic,
unspecified* `a(t)`: `d/dt(a³φ̄̇) − ĝC = 0` follows purely from `E_φ` and
`E_ρ` (`ρ̄_A a³=C` exactly, per `FINDING_P58`) — true for the *real*,
fully-coupled `a(t)`, whatever it is, not an approximation. `FINDING_P65`'s
approximation was using `FINDING_P62`'s uncoupled `a(t)` *inside* this
exact relation, not the relation itself. This reframing is what makes a
genuine perturbative construction possible.

**[Skeptic-added, inherited-assumption caveat]** This exactness is only
as good as `ρ̄_A a³=C` itself. That relation comes from `FINDING_P58`'s
own construction (bare density `ρ̄_A` tracking conserved particle number
times a *fixed* mass, independent of `ĝ`) — a real, previously-proven
result within this campaign, but an *inherited* premise this file does
not re-derive. In coupling structures where matter conservation instead
picks up an explicit source term (common in some scalar-tensor/chameleon
constructions), `ρ̄_A a³` would not stay constant and the entire
construction below would need to be redone.

## Method

Expand around `FINDING_P62`'s own exact `ĝ=0` solution:

```
a(t)      = a₀(t)·[1 + ĝδ(t) + O(ĝ²)]
φ̄(t)      = φ̄₀(t) + ĝφ̄₁(t) + O(ĝ²)
```

Expanding the *exact* Friedmann equation to `O(ĝ)` (via `sp.diff(...,
ĝ).subs(ĝ,0)`, not hand Taylor expansion) and eliminating `φ̄₁̇` using the
exact relation above gives, after independent verification that no
`φ̄₁` (bare or differentiated) survives, a **single linear ODE for
`δ(t)` alone**, sourced entirely by the known `P62` background:

```
A(t)·δ̇ + B(t)·δ + D(t) = 0
A(t) = 8πt/(6πt²−1),  B(t) = 8π(6πt²+1)/(6πt²−1)²
```

Solved via integrating factor: `μ(t) = t − 1/(6πt)` (exact closed form,
confirmed). The full closed-form antiderivative of `μ(t)Q(t)` did not
complete within 5 minutes of `sp.integrate` — the same class of
sympy-performance issue this campaign has repeatedly hit with
nested-log/cube-root expressions. **Fell back to numeric quadrature of
the already-verified, closed-form integrand** — a genuine semi-analytic
solution (exact ODE, exact integrand, numeric definite integral), not a
retreat to pure numerics. `δ(t)` was then confirmed, via finite
difference, to solve its own ODE to `2×10⁻¹¹` precision — a positive
control run *before* using it for anything downstream.

`φ̄₁(t)` follows from the same exact relation
(`φ̄̇₁=(t-1)/a₀³−3δφ̄̇₀`), integrated numerically the same way, and —
**added in response to skeptic review** — independently confirmed via
its own finite-difference check to solve that defining relation to
`7.9×10⁻⁸` (a coarser but still solid tolerance than `δ(t)`'s own check,
honestly attributed to `φ̄₁` involving a *nested* numeric integral over
`δ(t)` itself, compounding quadrature error).

## Self-caught bugs, before skeptic contact (all fixed)

1. **`K` left as an untied free symbol**, silently failing the `P62`
   background's own Friedmann positive control. Fixed.
2. **Float pollution in exact coefficients** — substituting the
   module-level Python float `G_N=1.0` (rather than `sp.Integer(1)`)
   polluted exact rational coefficients (visible as "48.0" instead of
   "48"). Fixed.
3. **Mislabeled comparison baseline.** The first cross-validation pass
   compared this file's first-order result against `φ̄₀(t)` *alone*
   (`f(t)=√2` only) and called it "`FINDING_P65`'s test-field" — it
   wasn't. `P65`'s own test-field used the *full* `f(t)=√2+ĝ(t-1)`
   numerator with the zeroth-order `a₀³` denominator — already partially
   `O(ĝ)`. This made the first (buggy) improvement numbers dramatically
   overstated (falsely "12.9×" at `ĝ=1.0`, corrected to "1.1×" below).
   Fixed by properly reproducing `P65`'s own quantity as the baseline.

## Skeptic review (Step 8a) — the framing itself needed correction

Context-blind review confirmed both central symbolic claims (the exact
first integral, and the closure of the `O(ĝ)` equation into a `δ`-only
ODE) by independent hand derivation — both correct, no algebra bug. But
it found the **Verdict's framing of the results itself was rhetorical
spin, not analysis**:

> "'A flat, ĝ-independent improvement factor would have been the
> suspicious result here' preempts one class of criticism... it doesn't
> address the honest reading: the correction reduces the error at ĝ=1 by
> 10% — that is a marginal improvement... Not fraud — but the finding
> should ADMIT that the ĝ=1 result is unimpressive rather than presenting
> it as an intended feature."

Independently checked before accepting: computed the actual log-log
scaling of the improvement factor across the three tested `ĝ` (rather
than asserting a qualitative story). Result: slope `−0.69` between
`ĝ=0.01–0.1`, slope `−0.31` between `ĝ=0.1–1.0` — weaker than the naive
`O(ĝ)/O(ĝ²)` expectation of slope `≈−1`, and flattening further as `ĝ`
grows. This confirms the skeptic's point with real computation: the
improvement is real at small `ĝ` but genuinely tapers off, not a clean
scaling law, and the `ĝ=1` result (`1.1×`, i.e. ~10% error reduction) is
honestly marginal, not "the expected pattern."

**Two further gaps, both fixed with real computation, not just noted:**

- **No positive control for `φ̄₁(t)`** (only `δ(t)` had one). **Fixed**:
  added the finite-difference check described above.
- **Only one time point (`t=51`) tested**, leaving open whether the
  improvement pattern was a single-snapshot artifact. **Fixed**: added
  `t=25` alongside `t=51` — the improvement direction is consistent at
  both (`18.2×→10.7×` at `ĝ=0.01`; `2.7×→2.2×` at `ĝ=0.1`;
  `1.1×→1.1×` at `ĝ=1.0`), confirming the pattern is not a `t=51`-only
  coincidence.

## Results (post-correction)

| `t` | `ĝ` | full nonlinear `φ̄(t)` | P65 test-field (rel. err) | this file, +`δ` (rel. err) | improvement |
|---|---|---|---|---|---|
| 25 | 0.01 | 0.07460715 | 0.07459950 (`1.0×10⁻⁴`) | 0.07460673 (`5.7×10⁻⁶`) | 18.2× |
| 25 | 0.1 | 0.08554887 | 0.08542753 (`1.4×10⁻³`) | 0.08550440 (`5.2×10⁻⁴`) | 2.7× |
| 25 | 1.0 | 0.20179508 | 0.19370785 (`4.0×10⁻²`) | 0.19448112 (`3.6×10⁻²`) | 1.1× |
| 51 | 0.01 | 0.07650577 | 0.07649862 (`9.3×10⁻⁵`) | 0.07650511 (`8.7×10⁻⁶`) | 10.7× |
| 51 | 0.1 | 0.09078887 | 0.09063347 (`1.7×10⁻³`) | 0.09071794 (`7.8×10⁻⁴`) | 2.2× |
| 51 | 1.0 | 0.24609978 | 0.23198197 (`5.7×10⁻²`) | 0.23284626 (`5.4×10⁻²`) | 1.1× |

## Verdict — corrected, stated plainly

**This is a genuine, working first-order perturbative solution of the
`ĝ≠0` coupled system, in its actual regime of validity: small `ĝ`.**
Built from an exact first integral, an exact `O(ĝ)` reduction to a
single linear ODE, solved semi-analytically, and *confirmed* — with two
independent positive controls and a second time point — to improve on
`FINDING_P65`'s own test-field at genuinely small `ĝ` (a real `2–18×`
error reduction at `ĝ≤0.1`).

**Stated plainly, not softened: at `ĝ=1.0` the correction reduces error
by only ~10% (`1.1×`) — a marginal improvement.** The first-order-in-`ĝ`
expansion should **not** be trusted as a good approximation at `ĝ~1` on
its own. It is a real tool for the genuinely-small-`ĝ` regime, not a
general-purpose correction across the whole tested range — and this
finding states that directly rather than framing the weak result as
"the expected pattern."

**Does not resolve C1 vs. C2 vs. C3.** Provides a real analytic handle
for small `ĝ` and confirms the mechanism `FINDING_P65` proposed
(backreaction via `δ(t)` captures real physics), but says nothing new
about the large-`ĝ` boundary-crossing regime (`ĝ=3,10`), where a
first-order-only expansion should — by the pattern shown here — do even
worse than the already-marginal `ĝ=1` result.

## What this does NOT establish

- **A full closed-form solution of the nonlinear system.** Only a
  first-order (in `ĝ`) semi-analytic correction to `FINDING_P62`'s exact
  `ĝ=0` solution.
- **Convergence of the perturbative series for any `ĝ`.** Only that the
  first-order term measurably helps at small `ĝ` — not that a
  second-order term would help further, or that the series converges.
- **A good approximation at `ĝ~1`.** Directly shown to be only marginally
  better than `P65`'s own (already-imperfect) test-field there.
- **Anything about the `ĝ=3,10` boundary-crossing regime.** Not
  attempted; the pattern found here suggests this expansion is a poor
  tool there.
- **[Skeptic-added]** That `ρ̄_A a³=C` (the load-bearing exactness this
  whole file rests on) holds for coupling structures other than
  `FINDING_P58`'s own specific construction — inherited, not re-derived.
- **[Skeptic-added]** Anything for `V(φ̄)≠0` — the `V=0` scope (stated in
  the header) is load-bearing for the first-integral trick working this
  cleanly; a potential term would likely break it.
- **[Skeptic-added]** That cross-validation against the full nonlinear
  numeric system constitutes an independent physics check — both sides
  solve the *same* `E_00/E_φ/E_ρ` equations; this validates the
  perturbative *solution technique* against a numerical solution of the
  same model, not against independent physics.
- Whether a genuinely closed-form (not semi-analytic) solution exists —
  the `sp.integrate` intractability is suggestive, not a proof of
  non-existence.
- Resolution of `FINDING_P39`'s SI-normalization gap — untouched.
- Adjudication of C1 vs. C2 vs. C3 — deliberately not resolved.

## Not yet done

- Extend to second order in `ĝ`, to see whether it further improves
  small-`ĝ` accuracy and whether the series shows signs of converging or
  diverging as `ĝ` grows.
- Attempt an analogous perturbative construction anchored at large `ĝ`
  for the boundary-crossing regime.
- A genuine further attempt at closed-form integration of `μ(t)Q(t)`
  (e.g. `sp.integrate(..., manual=True)`, or a substitution to remove
  nested radicals first).
- Check whether `FINDING_P58`'s `ρ̄_A a³=C` premise holds under a more
  general coupling structure, to know how load-bearing this file's
  entire foundation actually is beyond this campaign's own construction.
- Returning to the perturbation sector (`Ψ_k(t)`, D2/D3/D4) — still
  blocked on C1/C2/C3.

## Skeptic Verdict table

| # | Claim reviewed | Skeptic verdict | Response |
|---|---|---|---|
| 1 | Central identity `d/dt(a³φ̄̇)=ĝC` exact for generic `a(t)` | Independently re-derived by hand, confirmed correct | No change; inherited-assumption caveat added |
| 2 | `O(ĝ)` closure eliminates `φ̄₁` entirely | Independently re-derived by hand, confirmed correct — noted this is a special structural feature of this Lagrangian, not a generic technique | No change; noted explicitly |
| 3 | "Physically sensible pattern... flat factor would be suspicious" framing | **Spin, not analysis** — the `ĝ=1` marginal result was framed defensively rather than stated plainly, especially given the prior 12.9×→1.1× bug on this exact comparison | **Fixed**: computed actual log-log scaling; Verdict rewritten to state the `ĝ=1` result plainly as marginal |
| 4 | Risk of a fourth mislabeling bug (pattern from 3 prior bugs) | None found on inspection, but base-rate concern from 3 same-class bugs not addressed by the original text | Acknowledged; two new positive controls (`φ̄₁`, second time point) added as concrete mitigation, not just reassurance |
| 5 | Missing caveats: inherited `ρ̄_A a³=C` assumption, `V=0` scope, single-time-point testing, no `φ̄₁` positive control, "internal" cross-validation | Six specific gaps named | **Fixed**: all six addressed — two with real new computation (positive control, second time point), four with explicit caveats added |

**Overall: WEAKENED → fixed.** No algebra bug found at any point — the
math was correct throughout. What needed fixing was the honesty of the
framing around a genuinely mixed result (strong at small `ĝ`, marginal
at `ĝ~1`), plus closing two real robustness gaps with actual
computation.
