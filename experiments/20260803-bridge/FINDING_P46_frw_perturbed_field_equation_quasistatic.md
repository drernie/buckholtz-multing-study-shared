# P46 — FRW-perturbed field equation, solved in the subhorizon quasi-static limit: `δφ_k=ĝa²δρ_k/k²`, with the a-power independently pinned down after skeptic review

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — the original "load-bearing"
consistency check was shown to have essentially zero discriminating
power (adversarial counterexample: any `a^n` passes it); a genuinely
independent check (covariant `□φ` operator) was added instead of just
softening the language.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
**Origin:** first of two steps toward the campaign's original `P36` row
(`PLAN_final_goal_20260814.md`): "quasi-static cosmological reduction,
subhorizon approximation." Explicitly the same category of step (local
static result → broader cosmological context) that produced this
campaign's single worst correction (`P36`, 5/6 skeptic issues FALSIFIED,
per the plan's own status log) — built with maximal explicit derivation
as a direct, deliberate response to that history.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P46_frw_perturbed_field_equation_quasistatic.py`, ruff
clean, all assertions pass.

## 0. Why this step exists, and why it is split in two

`FINDING_P40`'s slip ratio `γ(r)` is a *static, two-body* quantity — not
directly comparable to `FINDING_P31`'s phenomenological ceiling, which
constrains a *cosmological, quasi-static* parameter (Bean &
Tangmatitham's `Q`). The campaign's own governing plan already named the
missing bridge as its `P36` row. This finding builds the first half:
the perturbed field equation and its quasi-static solution for `δφ_k`.
A second step (`P47`, not yet built) will derive the perturbed Einstein
equations in the same limit and assemble `γ(a,k)`.

**Explicit risk acknowledgment, stated before any derivation:** this is
the same *shape* of extension (a locally-proven result generalized to a
broader context) that produced this campaign's worst correction. Every
equation below is therefore re-derived from the action via
Euler-Lagrange — never pattern-matched from a prior result by analogy —
and every new object is checked against an already-established one
before being trusted.

## Part 1 — general FRW field equation, via Euler-Lagrange

Same Lagrangian density `FINDING_P34`/`FINDING_P35` both used, restored
to a flat-FRW background (`√-g=a³`, `g^{ij}=δ^{ij}/a²`):

```
L = a³·(1/2)φ̇² − a·(1/2)(∇φ)² − a³ρ(1−ĝφ)
```

Euler-Lagrange gives:

```
φ̈ + 3Hφ̇ − ∇²φ/a² = ĝρ      (H:=ȧ/a)
```

**Note on `ρ`:** here `ρ` denotes the *physical* (per-physical-volume)
density, consistent with `FINDING_P34`/`FINDING_P35`'s own usage — the
matter term `a³ρ(1−ĝφ)` gives a constant `a³ρ` for dust (`ρ∝a⁻³`),
matching the standard dilution law. Not previously stated explicitly;
added here since the same symbol could otherwise be misread as comoving.

**Note on `a(t)`, `ρ(t)`:** both are treated as *fixed external
functions* throughout this finding — `a(t)` is not required to satisfy
the Friedmann constraint, and `ρ̄(t)` is not required to satisfy the
continuity equation (`ρ̄̇+3Hρ̄=0` for dust). This is the standard
"test-scalar-on-a-background" approach already used by
`FINDING_P34`/`FINDING_P35`, made explicit here rather than assumed.

## Part 2 — three positive controls, all required

**(a) Homogeneous limit.** Not checked by substituting into the
already-derived field equation (that would be tautological — comparing
a formula to itself). Instead, *independently* re-derived from a
genuinely homogeneous (`t`-only) candidate Lagrangian, by the same
method as Part 1:

```
φ̄̈ + 3Hφ̄̇ = ĝρ̄
```

**Matches `FINDING_P34`'s own equation exactly.** Since this reuses the
same underlying Lagrangian as Part 1's general derivation, exact
agreement is *required* by construction, not surprising independent
evidence — the same scoping discipline `FINDING_P43` applied to its own
Noether-current check. It still catches a real class of bug (a wrong
`a(t)`-power or sign slip in Part 1's own general derivation), since
Part 1's derivation itself was not reused here.

**(b) Static + flat limit** (`a=1`, so `H=0`, `1/a²=1`):

```
φ̈ − ∇²φ = ĝρ
```

**Matches `FINDING_P35`'s own equation exactly.**

**(c) [ADDED after skeptic review]** Neither (a) nor (b) actually pins
down the *specific* powers of `a(t)` in the general equation — the
skeptic showed that (b), evaluated at `a=1`, cannot distinguish the
correct `a²` from *any* other power that equals `1` at `a=1` (e.g.
`a¹⁷`). A genuinely independent check: re-derive the same equation via
the standard covariant d'Alembertian, `□φ=(1/√-g)∂_μ(√-g·g^{μν}∂_νφ)` —
a completely different method (metric determinant + inverse-metric
contraction, not Lagrangian variation) that pins down *both* the `a³`
(volume) and `1/a²` (inverse spatial metric) powers independently of
Part 1:

```
□φ = (1/a³)[∂_t(−a³φ̇) + Σᵢ∂ᵢ(a·∂ᵢφ)]
```

**`−□φ` matches Part 1's source-free field equation exactly** (script
assertion), via a genuinely different derivation path. This directly
refutes the skeptic's adversarial counterexample: a wrong power of `a`
on either term would not have matched this independently-built formula,
regardless of what it gives at `a=1` specifically.

## Part 3 — is "perturbation theory" here exact or approximate?

Split `φ=φ̄(t)+εδφ(t,x)`, `ρ=ρ̄(t)+εδρ(t,x)`, take `d/dε` at `ε=0`
(script, not asserted by hand):

```
δφ̈ + 3Hδφ̇ − ∇²δφ/a² = ĝδρ
```

**Exactly the same functional form as the full equation.** This is a
checked consequence of the *scalar-field* equation being exactly linear
in `φ` and `ρ` — no `V(φ)` term exists at this stage of the chain.

**[CORRECTED after skeptic review]** The original text overreached from
this narrow fact to "no perturbative approximation in this step" as a
general claim. Precisely: `δφ`'s *response* to a *prescribed* `δρ` is
exact — true, and that is all this section actually shows. It does
**not** mean the whole perturbation setup is exact or complete:
`ρ̄(t)` here is not required to satisfy the continuity equation
(`ρ̄̇+3Hρ̄=0` for dust); `a(t)` is not required to satisfy the Friedmann
constraint; and `δρ` itself has **no dynamical equation imposed** — no
continuity/Euler equation for the matter perturbation — it is left as a
free external function throughout. This finding computes a **response
function** for `δφ` given an arbitrary `δρ`, not a closed,
self-consistent cosmological perturbation system (that would need the
full coupled scalar+matter+metric system, not attempted here).

## Part 4 — Fourier transform (exact) + subhorizon quasi-static approximation (flagged, not exact)

Fourier space, exact:

```
δφ̈_k + 3Hδφ̇_k + (k²/a²)δφ_k = ĝδρ_k
```

**Subhorizon quasi-static approximation**, validity `k/(aH)≫1`.

**[CORRECTED after skeptic review]** The original justification asserted
`δφ̈~H²δφ` as if it were a general fact — it is not; it is an assumption
*about the solution's own time-dependence*, not derived from anything
above. The actual closure argument (standard in scalar-tensor QSA
literature, stated explicitly here rather than compressed): `δφ` is
taken to be *enslaved* to `δρ` (source-dominated), and `δρ` evolves on a
Hubble timescale (a fact about matter clustering, not itself derived in
this finding) — so `δφ` inherits `d/dt~H`, giving `δφ̈~H²δφ`. The
resulting solution is self-consistent with this assumption: any
time-dependence of `δρ_k` transfers directly to `δφ_k` with no extra
derivative operators, matching the enslaved-response picture. Still an
**approximation** with a stated regime, not an exact result:

```
(k²/a²)δφ_k = ĝδρ_k   ⟹   δφ_k = ĝa²δρ_k/k²
```

**This is the only approximation introduced in this finding.**

## Part 5 — basic sanity check, ~~load-bearing consistency check~~ [CORRECTED: not load-bearing]

~~Static limit (`a=1`) of the quasi-static Fourier solution... This is
the load-bearing consistency check that the whole quasi-static machinery
connects back to already-verified ground.~~

**[CORRECTED after skeptic review]** The original text called this the
"load-bearing consistency check." The skeptic gave a concrete
adversarial counterexample: `δφ_k=ĝaⁿδρ_k/k²` reduces to the *same*
thing at `a=1` for *any* power `n` — this check cannot distinguish the
correct `a²` from a wrong `a¹⁷`. Independently confirmed before
accepting. **Downgraded to a basic sanity check** — Part 2c above is
what actually verifies the `a`-power, via a genuinely different
derivation.

Static limit (`a=1`) of the quasi-static Fourier solution:

```
δφ_k|_(a=1) = ĝδρ_k/k²
```

Matches the standard Fourier-space Green's-function relation for
`−∇²φ=ĝρ`, and via the already-established (`FINDING_P19`,
`CONFIRMED-REAL`) real-space Green's function `∇²[1/(4πr)]=−δ³(x)`,
connects notationally to `FINDING_P35`'s own static solution
`ĝM/(4πr)` — reused, not re-proven, but **not** independent verification
of the `a`-power specifically (see correction above).

## What this establishes, precisely

1. The general FRW field equation, derived (not assumed) and shown to
   contain both `FINDING_P34`'s homogeneous equation and
   `FINDING_P35`'s static equation as exact limiting cases, plus a third,
   *genuinely independent* verification of the `a`-power via the
   covariant `□φ` operator (Part 2c).
2. **[CORRECTED, narrowed]** That the linear perturbation `δφ`'s
   *response to a prescribed `δρ`* obeys the field equation's full
   functional form exactly — not that the full perturbation *system*
   (matter + metric) is exact or complete.
3. `δφ_k=ĝa²δρ_k/k²` in the subhorizon quasi-static limit, resting on an
   explicit enslaved-response closure argument, with its validity regime
   stated (`k/(aH)≫1`).
4. That this quasi-static machinery connects notationally to
   `FINDING_P35`'s already-verified static solution — with the `a`-power
   itself independently verified separately (Part 2c), not by this
   connection alone.

## What this does NOT establish

1. **`γ(a,k)`, `μ(a,k)`, or `Σ(a,k)`.** Only the scalar field's own
   quasi-static Fourier solution is derived here — the perturbed
   Einstein equations are `P47`'s job, not attempted here.
2. **Anything numerically comparable to `FINDING_P31`'s ceiling.** Even
   once `P47` gives a symbolic `γ(a,k)`, `FINDING_P39`'s SI-units gap
   still blocks any numeric comparison — deliberately deferred.
3. **A closed, self-consistent cosmological perturbation system.**
   **[CORRECTED, added]** `ρ̄(t)` has no continuity equation imposed;
   `a(t)` has no Friedmann constraint imposed; `δρ` has no dynamical
   equation of its own (no continuity/Euler equation) — all are free
   external functions. `δφ_k=ĝa²δρ_k/k²` is a **response function**, not
   a closed cosmological equation; the full coupled scalar+matter+metric
   system is not attempted here.
4. **Validity outside the subhorizon regime `k/(aH)≫1`**, or outside the
   enslaved-response closure the quasi-static approximation rests on.
   The full second-order-in-time equation from Part 4 remains exact.
5. **[CORRECTED, added]** **That the physical-vs-comoving interpretation
   of `ρ`** (§ Part 1 note) is the only possible reading — it is the
   reading consistent with `FINDING_P34`/`FINDING_P35`'s own usage, made
   explicit here, not independently re-derived from first principles.
6. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

Given this step's explicitly acknowledged high-risk category, the
skeptic was asked to scrutinize harder than a routine finding.

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 1 (FRW Lagrangian, EL derivation) | **CONFIRMED** (math) / **WEAKENED** (`ρ` interpretation unstated) | **Fixed** — explicit note added on physical vs. comoving `ρ`. |
| Part 2a/2b (positive controls) | **CONFIRMED** with unstated assumption (`a(t)`, `ρ̄(t)` as fixed externals) | **Fixed** — explicit caveat added. |
| Part 2's homogeneous check | **WEAKENED** — cannot catch spatial-gradient-term errors | **Fixed via Part 2c** — a genuinely independent covariant `□φ` re-derivation added, catching exactly this class of error. |
| Part 3 ("no perturbative approximation") | **FALSIFIED as worded** — conflates linearity of the scalar-field operator with a closed perturbation system; matter sector entirely non-dynamical | **Fixed** — narrowed to "response function," explicit list of what's left unconstrained (`ρ̄` continuity, `a(t)` Friedmann, `δρ` dynamics) added. |
| Part 4 (QSA justification) | **WEAKENED** — `δφ̈~H²δφ` presented as fact, actually an unstated assumption about the solution | **Fixed** — explicit enslaved-response closure argument stated. |
| Part 5 ("load-bearing consistency check") | **FALSIFIED as load-bearing** — adversarial counterexample (`a^n` for any `n` passes the `a=1` check) shown concretely | **Fixed** — independently re-verified the counterexample before accepting; downgraded to a sanity check; Part 2c supplies the real verification. |
| Scope-gap list | **FALSIFIED** — missed non-dynamical matter/background, `ρ` interpretation, QSA closure | **Fixed** — items 3 and 5 added above. |

**Comparison to the `P36` precedent this step was explicitly built to
avoid repeating:** the skeptic's own assessment is that this is a
*qualitatively different* kind of correction — every mathematical
derivation survived intact (re-verified independently before accepting
any correction); the failures caught were in *framing and scope
completeness*, not broken math. No verdict here meets the Step 8a "true
kill" bar.

## Reproduction

```bash
python experiments/20260803-bridge/P46_frw_perturbed_field_equation_quasistatic.py
```
