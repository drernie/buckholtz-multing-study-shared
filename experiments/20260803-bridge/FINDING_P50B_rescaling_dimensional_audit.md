# P50B — is `ĝ` physical or convention-dependent? Field-rescaling audit gives a real, useful check (weaker than "independent"); the dimensional audit's headline result turned out to be Reading-1-specific, not reading-independent — caught by testing it directly, not just hedging

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — three real issues found, all
fixed with real computation, not softened language.** Most consequential:
the headline claim that `[A]=[G_N]` is "reading-independent" was **tested
directly** (self-consistently re-deriving `[φ]` under P39's own Reading 2
instead of holding it fixed at the Reading-1 value) and found **false** —
under that genuinely independent re-derivation, `[A]` comes out as a
completely different dimension. Retracted as originally overclaimed; the
corrected verdict is substantially narrower.
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
**Origin:** the user's own narrow, single-purpose staging after P50A:
"P50B — restore a dimensionally and physically correct normalization,"
pre-registering three outcomes (B1/B2/B3) before any computation, with six
explicit kill-gates named in advance. Scope, stated by the user and
honored throughout: **no Euler equation, no external bounds, no numbers
before P39's gap is closed.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P50B_rescaling_dimensional_audit.py`, ruff clean, all
assertions pass.

## 0. Pre-registered outcomes and kill-gates (stated before any computation)

**B1 — existing-normalization closure.** `A`/`C` fully fixes SI
bookkeeping without a new constant, but `ĝφ̄` (P50A's background factor)
remains its own independent invariant; force strength is separately
controlled by `Ag²`.
**B2 — genuine missing scale.** Neither `A` nor canonical field
normalization closes the dimensions; a genuinely new independent
dimensional constant is needed — a serious underdetermination signal.
**B3 — full invariant closure.** After returning to the unnormalized
action and re-canonicalizing, all physical source/force amplitudes
express only via existing invariants (primarily `Ag²`), and P50A's own
correction also gets a well-defined invariant form without a new
physical constant.
**Stated preference (not a result):** B3 plausible, B1 a real live
alternative — not favored a priori.

**Six kill-gates**, checked explicitly against every step below:
KG1 dimensions must not be "fixed" by a power of `c` alone · KG2 `A`
must not be inserted post-hoc, must be derived from the kinetic
normalization · KG3 canonical and non-canonical fields must never be
compared as the same `φ` · KG4 invariance must not be checked only via
identically-constructed expressions · KG5 field-rescaling invariance
must not be used to conclude SI-correctness · KG6 the P22/P31 numeric
bound is not used anywhere in this script.

## Part 1 — general Lagrangian with kinetic normalization `C` explicit

```
ℒ = −(C/2)(∂φ)² + gJφ + ...,   A ≡ C⁻¹
```

Generalizes what every finding since `FINDING_P34` implicitly fixed at
`C=1` (matching `FINDING_P21`'s own `S=∫d⁴x (1/2)(∂φ)² + Σg·m·φ`).

## Part 2 — field-rescaling transformation, derived not assumed

Substituted `φ=φ'/λ` directly into `ℒ(φ;C,g)` and solved for what `C'`,
`g'` reproduce the result exactly (script assertion, symbolic):

```
C' = C/λ²,   A' = λ²A,   g' = g/λ
```

**Confirmed** — matches the user's own stated transformation rules
exactly, now derived rather than assumed. `φ` (general) and `φ'`
(rescaled) kept as distinct symbols throughout (KG3).

**[CORRECTED after skeptic review, added]** This derivation holds `J`
(the matter source current) **fixed** — unrescaled — while only `φ` is
substituted. Physically justified (`J` represents matter mass/density,
independent of how the separate scalar field `φ` is parametrized), but
this was an **unstated assumption** in the original version — exactly the
kind of gap this campaign's audits exist to catch. Under a different
assumption (e.g. `J'=J/λ`), a different `g'` would result; the
transformation rules hold *given* `J`-invariance, not as a universal fact
independent of that choice.

## Part 3 — candidate invariants `gφ` and `Ag²`, checked

```
gφ = g'φ'    (confirmed, script assertion)
Ag² = A'g'²  (confirmed, script assertion)
```

## Part 4 — the decisive check: two algebraically independent canonicalization routes

**Route 1 — Lagrangian kinetic-coefficient canonicalization.** Solve
`C'=1` for `λ` directly: `λ=√C ⟹ g_canon = g/√C`.

**Route 2 — physical force law**, via the general-`C` Euler-Lagrange
field equation combined with `FINDING_P19`'s own already-established
Green's function (`∇²[1/(4πr)]=−δ³(x)`, reused not re-derived) — a
genuinely different computation, not a relabeled copy of Route 1:

```
−C∇²φ = gJ   ⟹   φ(r) = gAM/(4πr)
|F| (general C,A frame)  = Ag²M/(4πr²)
|F'| (canonical frame, A'=1, coupling g_canon) = g_canon²M/(4πr²)
```

**`|F|−|F'|=0` (script assertion) — the two routes agree exactly.** Both
forms equal `Ag²M/(4πr²)` exactly.

**[CORRECTED after skeptic review]** The original text called this "two
algebraically independent" derivations, claiming full KG4 satisfaction.
The skeptic correctly found this overstated: Route 2 solves the
Euler-Lagrange equation from the **same** Lagrangian as Route 1, using
the **same** coupling `g` for both source and test particle — once the
Lagrangian and `J`-invariance (Part 2) are accepted, Route 1's and Route
2's agreement is a **necessary consequence of standard variational
calculus**, not two independent physical principles converging. A
genuinely independent check would need to leave the Lagrangian-invariance
manifold entirely (a scattering-amplitude or Ward-identity argument) —
not attempted here, outside this campaign's classical-field-theory scope.

**Downgraded, not retracted:** Route 2 remains a real, useful check — it
verifies that the abstract field-redefinition (Route 1) correctly
propagates to an actual physical, measurable quantity (the force law),
catching implementation errors (a wrong Green's-function normalization,
a dropped factor) that Route 1 alone would not catch. But it is a
**propagation-verification**, not independent evidence that
`g_canon=g/√C` is uniquely correct. **KG4 is only partially satisfied.**

## Part 5 — dimensional consistency of `C`/`A`, derived from the kinetic term alone, kept structurally separate from Parts 2–4 (KG5)

Reused `FINDING_P39`'s own dimension-tuple helper functions verbatim
(not reinvented — this campaign's established anti-hand-algebra
discipline). Used `FINDING_P39`'s own established `[φ]=kg⁰m²s⁻²`, derived
in P39's own Step 2 from `g·m·φ=energy` **assuming `g` dimensionless**
(P39's own Reading 1 — quoted exactly, not paraphrased).

The kinetic term `C(∂φ)²` must itself carry Lagrangian-density
dimension — this **fixes** `[C]`, derived here, not inserted after the
fact (KG2):

```
[Lagrangian density]      = kg¹m⁻¹s⁻²
[(∂φ)²]  (Reading-1 φ)     = kg⁰m²s⁻⁴
[A] required (Reading-1 φ) = kg⁻¹m³s⁻²  =  [G_N]  exactly
```

**[CORRECTED after skeptic review]** The original text claimed this
result is "reading-independent" because "`[φ]` only, no `[g]` anywhere"
appears in the arithmetic above. **The skeptic found this misleading**:
`[φ]=kg⁰m²s⁻²` was not derived free of any `g`-assumption — `P39`'s own
Step 2 derived it by *assuming* `g` dimensionless. `P39`'s own Reading 2
never re-derived `[φ]` independently — it held `φ` *fixed* at its
Reading-1 value while asking what `[g]` P33's own formula would then
require. That is `P39`'s own methodological choice, not a mathematical
necessity.

**Direct test, not just a hedge:** what if `φ` is instead
**self-consistently** re-derived from `g·m·φ=energy` using Reading 2's
*own* `[g]` value, instead of being held fixed at the Reading-1 value?

```
[g] Reading 2 (P39's own P33-derived value)      = kg⁰m⁻¹s¹
[φ] self-consistently re-derived under Reading 2 = kg⁰m³s⁻³   (≠ Reading-1 φ)
[A] required under THIS self-consistent φ         = kg⁻¹m⁵s⁻⁴  (≠ [G_N])
```

**Confirmed by direct computation (script assertion): under a genuinely
self-consistent re-derivation of `φ`, `[A]` does *not* come out as
`[G_N]` at all — a completely different dimension.** The
"reading-independent, `[G_N]`-shaped" conclusion is real *only* under
`P39`'s own Reading-1 convention — the one this whole campaign has
implicitly used since `FINDING_P34`'s `ĝ:=g/c` — not a structural fact
independent of which reading is ultimately correct. **Retracted as
originally overclaimed.**

## Part 6 — connecting to P50A: does `gφ̄` reduce further?

`gφ̄` is invariant under rescaling (Part 3) — but `FINDING_P46`'s own
background field equation (already established, reused not re-derived
here — `φ`'s own equation of motion, **not** the matter Euler equation
the user's scope explicitly excludes) already determines `φ̄`
dynamically:

```
φ̄̈ + 3Hφ̄̇ = ĝρ̄    (FINDING_P46)
```

**[CORRECTED after skeptic review]** The original text said `φ̄` is "not
a free background parameter." The skeptic correctly flagged this as
overstated: a second-order ODE's *evolution law* being fixed does not
mean its *solution* is fixed — `φ̄(t)` generically still depends on two
free integration constants (`φ̄(t₀)`, `φ̄̇(t₀)`) unless a specific
attractor/scaling solution is independently established (not done
anywhere in this campaign). **Corrected:** `φ̄`'s time-evolution is fixed
given initial conditions, but `φ̄` itself is not thereby reduced to a pure
function of `Ag²` and the matter background alone — the initial
conditions are a further, unaccounted-for freedom. **The lean toward B3
over B1 is weaker than originally stated** — genuinely open, pending
either an attractor argument or explicit initial-condition tracking.

## Part 7 — B1/B2/B3 verdict

**[CORRECTED after skeptic review]** B2's verdict is **split**, per the
skeptic's own precise reading of the pre-registered wording. B2 said "a
genuinely new independent dimensional constant is needed" — a
same-dimension-but-numerically-different-from-`G_N` constant still fits
that description; the original verdict silently narrowed B2 to mean only
"a new dimension-*type*." Given Part 5's own correction (the `[G_N]`
result is Reading-1-specific, not reading-independent):

**B2-strong** (a totally unconstrained new *dimension*): not supported
**under Reading 1 specifically** — `[A]` is fully pinned to `[G_N]`'s
dimension there. But this does **not** generalize to Reading 2 — under a
self-consistent Reading-2 `φ`, the required dimension is neither `[G_N]`
nor otherwise pinned by anything already known in this campaign.
**B2-strong is therefore only ruled out conditional on Reading 1 being
correct** — which reading is correct remains `P39`'s own, still-open
question.

**B2-weak** (a `[G_N]`-shaped constant numerically different from `G_N`):
**not ruled out** by this finding — dimensional analysis alone cannot
distinguish `A=G_N` from `A=7·G_N` from an unrelated constant of the
same dimension.

**B1 vs B3: not resolved.** Part 6's evidence for B3, after correction,
is weaker than the original text stated — `φ̄`'s free initial conditions
remain unaccounted for.

## What this establishes, precisely

1. Field-rescaling transformation rules, derived via direct Lagrangian
   substitution given an explicit `J`-invariance assumption.
2. `gφ` and `Ag²` confirmed invariant under rescaling.
3. `Ag²` derived (not assumed) as the physically meaningful force-strength
   combination, via two computational routes that converge exactly — a
   real propagation-verification, though not two logically independent
   derivations (KG4 only partially satisfied).
4. `[A]=[G_N]`'s dimension holds under `P39`'s own Reading-1 convention —
   derived purely from `[φ]` and Lagrangian-density-dimension consistency
   — but does **not** generalize to Reading 2 (tested directly, not
   assumed): under a self-consistent Reading-2 `φ`, `[A]` comes out as a
   different dimension entirely.
5. B2-strong (unconstrained new dimension) is not supported, but only
   *conditional on Reading 1*; B2-weak (`[G_N]`-shaped but numerically
   distinct constant) remains fully open. B1-vs-B3 remains genuinely
   unresolved, with weaker evidence toward B3 than originally claimed.

## What this does NOT establish

1. **`A`'s numerical value or its exact relationship to `G_N`.** Only the
   dimension is pinned down, and only conditional on Reading 1.
2. **Which of `P39`'s two readings is correct.** This remains the actual
   open question this whole normalization program hinges on — not
   resolved here.
3. **A decisive B1-vs-B3 verdict.** `φ̄`'s free initial conditions are
   unaccounted for.
4. **That Routes 1 and 2 (Part 4) constitute independent evidence** for
   `g_canon=g/√C` — they are a propagation-verification of the same
   Lagrangian, not independent physical principles.
5. **Any numeric comparison to `FINDING_P22`/`P31`'s ceiling** (KG6 — not
   used anywhere in this script).
6. **The matter Euler equation, or `T₀ᵢ`/`G₀ᵢ`** — explicitly out of
   scope per the user's own staging.
7. **Anything about the κ (dipole) sector** — monopole (`g`) sector only.
8. **The sign of `A`** (attractive vs. repulsive) — Part 4's force check
   used a magnitude (`|F|`), not a signed comparison; not load-bearing to
   any claim made here, but worth flagging before any future sign-
   sensitive use.
9. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 1 (general Lagrangian form) | **CONFIRMED** | No change. |
| Part 2 (rescaling rules derived) | **WEAKENED** — `J`-invariance assumption unstated | **Fixed** — named explicitly as an auxiliary assumption. |
| Part 3 (`gφ`, `Ag²` invariance) | **CONFIRMED** | No change. |
| Part 4 (two "independent" routes, KG4) | **WEAKENED** — Route 2 is not logically independent of Route 1; both are consequences of the same Lagrangian and the same source=test-particle coupling choice | **Fixed** — downgraded to "propagation-verification, not independent derivation"; KG4 marked only partially satisfied. |
| **Part 5 ("[A]=[G_N], reading-independent")** | **FALSIFIED** — `[φ]` itself was derived under P39's own g-dimensionless (Reading 1) assumption; not tested under a self-consistent Reading-2 re-derivation | **Fixed** — direct computation added (self-consistent Reading-2 `φ`), confirming `[A]≠[G_N]` under that reading. Original claim retracted, not softened. |
| Part 6 (`φ̄` "not a free parameter") | **WEAKENED (overclaim)** — an ODE's fixed evolution law does not fix its solution; free initial conditions remain | **Fixed** — corrected to note free initial conditions explicitly; B3 lean downgraded. |
| Part 7 (B2 "not supported") | **WEAKENED (semantic slippage)** — pre-registered B2 wording covers a same-dimension-different-value constant too, which this finding does not rule out | **Fixed** — split into B2-strong (ruled out, conditional on Reading 1) and B2-weak (still open). |

**Overall: not a true kill** — the core algebra throughout (Parts 1–4) is
correct, and `Ag²` genuinely is the invariant, physically meaningful
force-strength combination. But Part 5's headline claim was **actually
wrong as originally stated**, not merely imprecisely framed — caught by
testing it directly (computing what Reading 2 would require) rather than
accepting the "no `[g]` appears in the arithmetic" argument at face
value. This is a stronger correction than most prior findings in this
sub-arc required, consistent with the campaign's standing discipline of
treating every skeptic-flagged claim as `[INFERRED]` until independently
re-verified.

## Reproduction

```bash
python experiments/20260803-bridge/P50B_rescaling_dimensional_audit.py
```
