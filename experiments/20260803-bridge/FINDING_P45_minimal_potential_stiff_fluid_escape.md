# P45 — Minimal `V(φ)=λφ⁴/4`: reopens `w_φ≠1` and closes P44's stability loop — two corrected precision errors (a backwards regime claim, an undersold sign result)

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — Part 2's regime-of-validity
claim was exactly backwards, and Part 3 undersold a trivially-available
result.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
**Origin:** thirteenth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), third and final of three
symmetry/action-theoretic checks the user authorized in sequence
("го все по очереди"). Directly closes P34's own §4 point 8 gap
(canonical no-potential scalar is a forced stiff fluid, `w_φ=1`) and
P44's own corrected requirement (`V` must be non-quadratic for a
solution-specific stability question to exist at all).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P45_minimal_potential_stiff_fluid_escape.py`, ruff clean,
all assertions pass.

## 0. A scope check performed before choosing `V`, not after

An earlier working assumption carried into this session (from an
interrupted pre-compaction summary) held that adding *any* `V(φ)` here
would collide with `FINDING_P11`'s masslessness requirement. Before
writing any code, `FINDING_P11` was re-read directly (Gate 1 discipline —
never recall a prior finding's exact claim from memory). **That
requirement is about the κ/dipole-sector mediator** (`β_q/β_d=√6/2 ⟺
Λ=3/2`, requiring an exactly-massless Green's function in that sector) —
a different sector from the monopole-sector `φ` studied throughout
`P34`–`P44`. **The expected conflict does not apply**, corrected here
before it could become a silent, uninspected premise. The real,
applicable constraint is self-contained: adding a *mass term*
(`V''(0)≠0`) would turn `FINDING_P35`'s long-range Coulomb-like
`φ(r)=ĝM/(4πr)` into a short-range Yukawa profile — that is what
actually needs checking, done in Part 2 below.

## Part 1 — the chosen `V(φ)=λφ⁴/4`, both required properties verified

Two properties required, both checked symbolically (not asserted):

```
V(φ)    = λφ⁴/4
V'(φ)   = λφ³
V''(φ)  = 3λφ²
V'''(φ) = 6λφ   (nonzero for φ≠0)
```

- **`V''(0)=0`** — massless at the natural vacuum, unlike a mass term
  `m²φ²/2` whose `V''=m²` is nonzero everywhere (script assertion).
- **`V''(φ)` genuinely `φ`-dependent** (not constant) — satisfies
  `FINDING_P44`'s own corrected requirement that `V'''≠0` somewhere for a
  solution-specific stability question to exist at all (script assertion).

**[CORRECTED after skeptic review — added justification, not a
retraction]** The choice of *quartic* specifically has additional
standard reasons not originally stated: (i) **boundedness below** for
`λ>0` — a cubic (also `V''(0)=0`-trivially, but `V''=6λφ`, genuinely
`φ`-dependent too) is *unbounded below*, pathological; `φ⁴` is bounded.
(ii) **`Z₂` symmetry `φ→−φ`**, preserved by `φ⁴`/`φ⁶`, broken by `φ³`.
(iii) `φ⁴` is the *lowest-degree monomial* satisfying `V''(0)=0` *and*
bounded-below *and* `Z₂`-symmetric simultaneously — considerably
narrower than "one choice among several."

## Part 2 — field equation re-derived, `λ=0` positive control, and the residual on P35's own solution

Euler-Lagrange (not by hand) on `L` with `−λφ⁴/4` added gives:

```
φ̈ − ∇²φ + λφ³ = ĝρ
```

**At `λ=0`: reduces exactly to `FINDING_P35`'s own `φ̈−∇²φ=ĝρ`**
(script assertion, positive control).

Plugging `P35`'s own static solution `φ₀(r)=ĝM/(4πr)` into the *new*
equation, for `r>0`:

```
λφ₀(r)³ = M³ĝ³λ/(64π³r³)   — NONZERO
```

`φ₀(r)` is no longer an *exact* solution once `V` is added.

**[CORRECTED after skeptic review]** The original text claimed this
residual is small "near the source" — **exactly backwards**. Computed
directly:

```
λφ₀(r)² as r→0:   ∞
λφ₀(r)² as r→∞:   0
d/dr[λφ₀²] < 0 for all r>0 (monotonically decreasing)
threshold: r* = ĝM√λ/(4π)   (where λφ₀²=1)
```

The perturbative criterion `λφ₀²≪1` holds **far** from the source
(`r≫r*`), **not near it** — `φ₀` itself diverges as `r→0`, so the
residual actually *dominates* closest to the source, the opposite of
where the original text claimed the approximation was valid. (The same
`ĝφ≪1` regime `FINDING_P34` already uses has the identical direction
problem — both are *outer*, large-`r` criteria; calling the new one
"more restrictive" did not fix that.) **Solving the full nonlinear
equation, valid down to small `r`, is not attempted here — flagged
explicitly as future work, now correctly scoped to where it is actually
needed (near the source, not far from it).**

## Part 3 — `δ²L` now genuinely depends on the background, closing P44's loop

Redoing `FINDING_P44`'s own generic-background second-variation
calculation with `V(φ)=λφ⁴/4` included:

```
d²L/dε²|_(ε=0) = δ̇²−(∇δ)² − 3λφ_bg²δ²
∂/∂φ_bg (above) = −6λφ_bgδ²   — NONZERO
```

**Confirmed: `L₂` now genuinely depends on `φ_bg`** (script assertion) —
unlike `P44`'s `V=0` case. This closes the loop `P44` predicted: "is
*this* solution stable" is now a well-posed, solution-specific question.

**[CORRECTED after skeptic review]** The original text left "the sign of
the resulting mass-squared term" as an unresolved next step — that
undersold what was already computable from `d²L|_0` alone. Matching
`d²L/dε²=δ̇²−(∇δ)²−m_eff²δ²`:

```
m_eff² = 3λφ_bg²
```

Since `λ>0` (declared throughout) and `φ_bg²≥0` for any real background,
**`m_eff²≥0` identically — no evaluation at the specific `φ₀(r)` is even
needed for this much: no tachyonic instability at the linearized level,
for any background, given `λ>0`.** This is a one-line consequence of
`λ`'s sign, not a genuine open next step. **What is still genuinely
open:** `m_eff²→∞` as `r→0` for `φ_bg=φ₀(r)` (the linearized problem is
singular at the origin, mode analysis not uniformly valid there), and
positive `m_eff²` alone does not establish full *nonlinear* stability
(collapse, radiative decay) — a mode-decomposition question genuinely
beyond this step's scope.

## Part 4 — is `w_φ=1` still forced?

Using the same `ρ_φ=(1/2)φ̇²+V`, `p_φ=(1/2)φ̇²−V` formula that reproduces
`FINDING_P34`'s own `V=0` result exactly (`ρ_φ=p_φ=φ̇²/2` — checked
first, before trusting the formula for `V≠0`):

```
w_φ = p_φ/ρ_φ = (2φ̇²−λφ⁴) / (2φ̇²+λφ⁴)
λ=0:                              w_φ = 1   (P34's forced stiff fluid)
kinetic-dominated (φ→0):          w_φ → 1   (recovers P34's dead end)
potential-dominated (φ̇→0):        w_φ → −1  (de-Sitter-like)
```

**`w_φ=1` is no longer forced** — it now depends on the actual balance of
kinetic vs. potential energy along the solution's own trajectory. Both
limits are structurally available. **This does not show the actual
dynamics of this system (with the `ĝρ` source term driving `φ`) reaches
the potential-dominated regime** — that requires solving the modified
EOM from Part 2 for specific initial conditions, a dynamical-systems
question not attempted here.

## What this establishes, precisely

1. A minimal `V(φ)` that satisfies both the requirement `FINDING_P44`
   derived (non-quadratic `V''`) and preserves `FINDING_P35`'s static
   solution *far* from the source (Parts 1–2, corrected direction),
   verified symbolically, with additional standard justification
   (boundedness, `Z₂` symmetry) for the specific quartic choice.
2. `δ²L` now genuinely depends on the background, and — **[CORRECTED]**
   — `m_eff²=3λφ_bg²≥0` identically for any background given `λ>0`: no
   tachyonic instability at the linearized level, for *any* background,
   established directly rather than left as an open question (Part 3).
3. `w_φ=1` is no longer forced by the theory — both the stiff-fluid dead
   end and a de-Sitter-like limit are structurally available (Part 4).
4. A prior expected conflict with `FINDING_P11`'s masslessness
   requirement, checked directly against `P11`'s own text and found not
   to apply — the requirement is about a different sector (§0).

## What this does NOT establish

1. **That this system's actual dynamics reaches the potential-dominated
   (accelerating) regime** — Part 4 shows the possibility is reopened,
   not realized; that requires solving the modified EOM for specific
   initial conditions.
2. **[CORRECTED]** **Full nonlinear stability of `φ(r)=ĝM/(4πr)` once `V`
   is added** — the linearized mass-squared is `≥0` everywhere (Part 3,
   established, not open), but `m_eff²→∞` at `r→0` (singular origin,
   mode analysis not uniformly valid there) and positive `m_eff²` alone
   does not rule out nonlinear collapse or radiative decay.
3. **[CORRECTED]** **A solution valid near the source once `λ≠0`** —
   Part 2 shows `φ₀(r)` is only approximate *far* from the source
   (`r≫ĝM√λ/(4π)`); the residual actually *dominates* near the source,
   the opposite of the originally (wrongly) stated regime, and no
   near-source solution is derived here.
4. **That `λφ⁴/4` is the unique minimal `V(φ)`** — narrower than
   originally stated (§Part 1 correction adds boundedness + `Z₂` as
   selection criteria) but still not a uniqueness proof; e.g. `φ⁶` would
   also qualify.
5. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 1/2 (Euler-Lagrange derivation, sign convention, `λ=0` reduction to P35) | **CONFIRMED** — independently re-derived by hand | No change. |
| Part 2 ("residual small... near the source") | **FALSIFIED** — exactly backwards; the criterion holds far from, not near, the source | **Fixed.** Independently re-verified (`λφ₀²→∞` as `r→0`, `→0` as `r→∞`, monotonically decreasing) before accepting — matches skeptic exactly. Script now computes the threshold radius explicitly; finding doc corrected with struck-through original claim. |
| Part 3 (`ρ_φ`/`p_φ` formula, matter coupling not silently dropped) | **CONFIRMED** (minor: re-derivation of Bianchi conservation with `V` included is implicit, not shown) | No change to the claim; noted as a documented limitation already covered by "does NOT establish" #1. |
| Part 3 (mass-squared sign "left as next step") | **FALSIFIED** — trivially `m_eff²=3λφ_bg²≥0` from `λ>0` alone, no evaluation needed | **Fixed.** Independently re-derived before accepting — matches exactly. Script now computes and states this directly, with the genuine remaining caveats (origin singularity, nonlinear stability) separated out precisely. |
| Part 1 (`λφ⁴/4` "one choice among several") | **WEAKENED** — hedge is real but understates the standard reasons (boundedness, `Z₂`) that favor the specific choice | **Fixed.** Boundedness-below and `Z₂`-symmetry arguments added explicitly, narrowing (not resolving) the "one choice among several" framing. |
| Scoping: "does NOT establish" list misses the above | **Confirmed gap** | **Fixed** — items 2–4 rewritten to reflect the corrections above. |

No FALSIFIED verdict here meets the Step 8a "true kill" bar (core
predicate false, no viable response) — Parts 1 and the core of Part 2/3
survive; the two FALSIFIED items were precision/direction errors in
prose claims layered on top of otherwise-correct computations, fixed by
computing the correct claim explicitly rather than softening language,
consistent with this campaign's established correction discipline (cf.
`FINDING_P43`, `FINDING_P44`).

**This closes the "го все по очереди" three-step authorization
(P43→P44→P45); the standing "one step, slowly" cadence resumes.**

## Reproduction

```bash
python experiments/20260803-bridge/P45_minimal_potential_stiff_fluid_escape.py
```
