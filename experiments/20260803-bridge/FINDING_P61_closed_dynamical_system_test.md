# P61 — closing `Ψ_k(t)` self-consistently: the closed dynamical system, and the decisive constraint-propagation test

**Date:** 2026-08-19
**Status:** Built, run, ruff clean, all assertions pass. **Skeptic review
(Step 8a): COMPLETE — found two further real bugs (a missing substitution
and a sign error, structurally identical in kind to two of the three
self-caught before review) AND a genuine overclaim in the original
Verdict. Both bugs fixed with real computation; the Verdict corrected to
a narrower, more honest D5 — not softened language. See § Skeptic
Verdict below.**
**Origin:** direct continuation of `FINDING_P60`, per the user's own
explicit instruction: close `Ψ_k(t)`'s own self-consistency properly —
build the actual dynamical system first, and only *then* ask whether it
reduces to an algebraic `μ(a,k)` — rather than reuse `FINDING_P50A`'s ad
hoc `Ψ̇_k=cHΨ_k` closure ansatz, which `FINDING_P60` already flagged as
leaving `Ψ_k` genuinely unresolved.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P61_closed_dynamical_system_test.py`, ruff clean, all
assertions pass (run time: several minutes — this is a genuinely heavy
symbolic computation, documented as such, not hidden).

**[NOTE on file location]:** built at the repo root, not
`experiments/20260803-bridge/`, due to the same directory-scoped
write-permission block already documented in `FINDING_P60`'s own header
— unresolved as of this file's build. Both files are to be moved once
that is fixed.

## Scope gate (user's own, explicit, load-bearing)

Strictly the same `V=0` truncation as every prior finding in this
sub-arc. **No ad hoc closure ansatz anywhere** — `FINDING_P48`'s own
*exact* (non-quasi-static) `G₀₀^(1)=2[∇²Ψ/a²−3HΨ̇]` already supplies
`Ψ`'s own evolution equation directly, with no extra assumption needed.

## Unknowns and components (user's own structure)

**Unknowns** (functions of `t`, at fixed `k`): `Ψ_k`, `δφ_k`, `δρ_{A,k}`,
`V_{x,k}` (or `W_k:=(1-ĝφ̄)V_{x,k}`). **Background** `a(t)`, `H(t)`,
`φ̄(t)`, `ρ̄_A(t)` treated as given coefficients — matching
`FINDING_P46`'s own long-standing convention (a(t) not required to
satisfy the Friedmann constraint) — **until Parts F–I, which directly
test the consequences of that choice.**

**Reused verbatim** (not recomputed from Christoffels except where
marked new): `FINDING_P48` (exact `G₀₀`), `FINDING_P54` (exact `G₀ᵢ`,
`Φ` substituted by `Ψ`), `FINDING_P49` (`Φ=Ψ`), `FINDING_P57`
(`Φ,Ψ`-extended scalar field equation), `FINDING_P59`/`FINDING_P50A`
(the `Ψ=0`/`θ=0` special cases the new equations below reduce to
exactly), `FINDING_P60` (the `ρ_phys` Route-B logic).

**New in this file** (not previously derived anywhere in the campaign,
each explicitly named as a not-yet-started step in a prior finding's own
scope list): `Q⁰`/`Q¹` on the `Ψ`-perturbed metric; `T_{0i}` for both the
scalar and matter[`ρ_phys`] sectors; the matter continuity + Euler
equations with **general** `V_x` (not `θ=0`) on the `Ψ`-perturbed
metric; the decisive constraint-propagation test itself.

## Part A — machinery setup, positive control

`Φ=Ψ` substituted into the metric from the start (`FINDING_P49`).
`box(φ)^(1)` on this metric, checked directly against `FINDING_P57`'s
own already-verified geometric terms (excluding the `-ĝδρ` field-equation
source, which is not part of the pure geometric `box` operator) —
**confirmed, zero residual.** This validates the Christoffel/box
machinery before anything downstream relies on it.

## Part B — `Q⁰`, `Q¹` on the `Ψ`-perturbed metric (new)

```
Q⁰ = ĝ(2Ψρ̄_Aφ̄̇ − δρ_Aφ̄̇ − ρ̄_Aδφ̇)
Q¹ = ĝρ̄_A∂_xδφ/a²        (no Ψ-dependence at all — checked, not assumed:
                            ∂ˣφ̄=0 kills the would-be Ψ-source term exactly)
```

**Positive control:** `Ψ→0` (function) reduces exactly to
`FINDING_P55`/`FINDING_P56`'s own already-verified `Q⁰`/`Q¹` — confirmed,
zero residual.

## Part C — `T_{0i}`, `T_{00}` (new for `T_{0i}`; `T_{00}` reuses `FINDING_P60`)

`T_{01}^{(φ)}=φ̄̇∂_xδφ` (standard); `T_{01}^{(int)}=0` identically (`g_{01}=0`
in this gauge, per `FINDING_P49`'s own structural argument) — both
confirmed. `T_{01}^{(matter)}` built from `ρ_phys` directly, per
`FINDING_P60`'s Route-B logic.

## Part D — the closed continuity and Euler equations (new)

**Positive control:** `Ψ→0`, on-shell, reduces exactly to `FINDING_P59`'s
own already-verified `ν=0` result (`M·[bare bracket]`) — confirmed, zero
residual.

The full (`Ψ≠0`) continuity equation factors exactly as
`M·[matter_continuity_bare − 3ρ̄_AΨ̇]` — confirmed by direct sympy
subtraction. Since `M` is generically nonzero, the closed continuity
equation is:

```
δρ̇_A = −3Hδρ_A − ρ̄_A∂_xV_x + 3ρ̄_AΨ̇
```

— the **standard Newtonian-gauge (Ma & Bertschinger) continuity
equation**, now with the general velocity-divergence term
`FINDING_P50A`'s own `θ=0` case did not have.

The Euler equation, under the same `W_x:=(1-ĝφ̄)V_x` rescaling that
collapsed `FINDING_P59`'s own Euler equation, is confirmed to reduce
*exactly* to:

```
Ẇ_x + 2HW_x = ĝ∂_xδφ/a² − M∂_xΨ/a²
```

— `FINDING_P59`'s own `Ψ=0` result, **plus** the standard Newtonian
gravitational-force term, rescaled by the same `M` factor as the density
conversion. A clean, beautifully standard-form result. **Parts A–D are
unaffected by the skeptic's corrections below** — the bugs found live
entirely in the `k`-space constraint-propagation test (Parts F onward).

## Part E — assembling the `k`-space system

Real-space `∂_x`-integrals over general field profiles are not
symbolically tractable (sympy leaves them as unevaluated `Integral`
objects) — switching to an explicit single Fourier mode (`∂_x→ik`,
`∇²→−k²`), matching this campaign's own established `k`-space
convention throughout `FINDING_P50A`/`P59`/`P60`, applied to the
**already-verified** real-space formulas above (not re-derived).

## Part F — the decisive test: constraint route vs. evolution route

The user's own proposed decisive experiment: solve the `0i` momentum
constraint (`C:=2ik(Ψ̇+HΨ)−8πG_N T_{01}`, kept in raw affine-in-`V_x`
form to avoid the huge quotient-rule expressions dividing produces),
differentiate it once, and substitute **every** first-time-derivative
that appears via the 00 equation, the continuity equation, the scalar
field equation, and the Euler equation. If the system is genuinely
consistent (the standard GR Bianchi-identity guarantee), this must
reduce to zero once the constraint `C=0` is also imposed — checked via
cross-multiplication (`A·Q−B·P=0`, avoiding an expensive explicit solve).

**Sanity control, `ĝ=0`, this campaign's own free-background convention**
(`a(t)` unconstrained by Friedmann): the residual is **nonzero** —
confirmed by direct symbolic computation, robust across every background
tested in this file (Parts F, H, I below).

## Part G — a real, narrow positive result: the scalar-free special case

With an explicit Friedmann-satisfying background substituted
(matter-dominated `a=t^{2/3}`, **`φ̄=const`**, chosen so
`3H²=8πG_N ρ̄_A` exactly, verified before use): the residual is
**exactly zero.**

**This result is real and stands** — verified twice (before and after
the skeptic-caught fixes below changed nothing here, since `φ̄=const`
makes every buggy term's coefficient vanish independently). It shows
that standard GR+dust, with **no scalar sector at all**, is internally
consistent once its own background solves its own Einstein equation —
exactly as expected, and a genuine, if narrow, confirmation that this
file's machinery is not fundamentally broken.

## Two further genuine bugs, caught by the context-blind skeptic (Step 8a)

The skeptic, working from the finding doc and script alone (no session
history), correctly identified that Part G's `φ̄=const` choice — while a
valid background in its own right — **cannot by itself support the
causal claim "Friedmann is precisely the missing ingredient"**, because
setting `φ̄̇=0` also kills every term through which a bug in the scalar
sector's own substitution chain could show up. Two such bugs were found,
independently re-verified in a standalone scratch computation before
accepting (per `audit-verification-gate.md`), and confirmed genuinely
present:

1. **A missing substitution.** `dCdt_sub` (the differentiated 0i
   constraint) genuinely contains an un-substituted `δφ̈_k` term after
   every substitution the original script actually applied — confirmed
   directly: `dCdt_sub.has(sp.diff(deltaphi_k, t, 2))` returns `True`
   even after applying all four of the script's own substitutions. This
   is structurally the *same* class of bug as self-caught bug #2 below
   (a derivative reintroduced by differentiating an already-substituted
   expression, never fed back in) — just for `δφ̈` instead of `δρ̇_A`.
2. **A sign error.** `dphi_ddot_sub`'s `k²` term had the wrong sign
   (`+k²δφ_k/a²` instead of `−k²δφ_k/a²`) — independently re-derived
   from scratch from this file's own already-verified `p57_geometric_part`
   (Part A) and confirmed: the residual between the script's version and
   the freshly-rederived correct version is exactly `2k²δφ_k/a²`, i.e.
   precisely twice the sign flip. This bug was **inert** in the original
   script (the substitution it feeds was never reached, due to bug 1),
   but would have produced a further wrong result the moment bug 1 was
   naively patched without also checking this.

Both fixed with real computation (not by weakening any check). **After
both fixes, Part F's free-background residual and Part G's
Friedmann-background residual are unchanged** — confirming the bugs,
while real, were genuinely inert for the specific `φ̄=const` comparison,
exactly as the skeptic's own diagnosis predicted.

## Parts H–I — the isolation test the skeptic demanded, and what it actually shows

**Part H:** the same matter-only-Friedmann background (`a`, `ρ̄_A` as in
Part G), but with a **genuine, nonzero** `φ̄(t)=-1/t` — independently
verified to satisfy *its own* background Klein-Gordon equation
(`φ̄̈+3Hφ̄̇=0` at `ĝ=0`), not an arbitrary choice. **Result: nonzero.**
The matter-only-Friedmann fix does **not** generalize beyond the
scalar-free special case.

**Part I:** does imposing Friedmann for the **total** (matter+scalar)
background energy (`3H²=8πG_N(ρ̄_A+φ̄̇²/2)`) restore consistency, even at
the cost of `ρ̄_A(t)` no longer separately satisfying matter's own
background continuity (`ρ̄_A∝a⁻³`)? **Result: also nonzero.**

**Both isolation tests are now hard-asserted** (`assert not is_zero_iso1`,
`assert not is_zero_iso2`) so a future run that silently flips either
result is caught immediately, not just printed.

## Verdict — corrected, narrower, and more honest than the original

**D5 still confirmed, but not for the reason originally claimed.** The
closed dynamical system built in Parts A–D is **not** Bianchi-consistent
under this campaign's own free-background convention — this core claim
is robust across every background tested (Parts F, H, I all agree).

**What Part G alone actually establishes** (real, narrow, and still
valid after the fixes): in the **degenerate special case where the
scalar background is entirely absent** (`φ̄=const`), matter-only
Friedmann restores full consistency. This is exactly what one would
expect from ordinary GR+dust with no scalar sector — a genuine, if
narrow, confirmation that the machinery is not fundamentally broken.

**What the original Verdict overclaimed, and what Parts H–I correct:**
"Friedmann consistency is precisely the missing ingredient" was **not**
demonstrated in general — it happened to hold only in the `φ̄=const`
case. With a genuine, self-consistent nonzero scalar background, neither
matter-only Friedmann (Part H) nor total-energy Friedmann without
separate matter continuity (Part I) restores consistency. The most
likely explanation: full Bianchi consistency requires the **entire**
background (`a`, `φ̄`, `ρ̄_A`) to be a genuinely **mutually** self-consistent
joint solution of Friedmann + matter's own continuity + the scalar's own
Klein-Gordon equation, **simultaneously** — not "add one relation on top
of an otherwise free choice." Constructing such a solution (a coupled
matter+scalar-field FRW cosmology) is a genuinely larger task, not
attempted here.

**This is still the user's own pre-registered D5 — if anything, a
deeper version of it.** What is missing is not one relation (Friedmann)
but a genuinely self-consistent background solution this campaign has
never constructed — tied to the same long-open `FINDING_P39`
SI-normalization gap (binding `ĝ` to `G_N` numerically), now shown to be
even more load-bearing than the original Part G result suggested.

**`D1`/`D2`/`D3` from `FINDING_P60` are unaffected.** `FINDING_P60`'s
own robust leading-order result (`μ_phys→1` exactly as `k→∞`, D1 ruled
out) does not depend on closing `Ψ_k(t)`'s self-consistency at all — it
holds before any closure is applied. What this file establishes is that
the finite-`k` D2-vs-D3 question `FINDING_P60` left open cannot be
decided by closing the system as currently completed — the system, as
completed, does not have a unique closure to decide it with, and the
path to one is deeper than a single missing relation.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Parts A–D (positive controls, closed continuity/Euler equations) | **CONFIRMED-REAL / not directly disputed** — the skeptic's findings concentrate entirely on the `k`-space decisive test | No change. |
| `sp.Poly` extraction over `V_x` is safe (no higher powers silently dropped) | **CONFIRMED-REAL** — independently traced: `C_raw`/`C_sub` linear in `V_x`, `Vxdot_euler` linear, `MM` multiplication preserves linearity | No change. |
| "D5: free background gives nonzero, Friedmann background gives exactly zero" (original framing) | **FALSIFIED-AS-STATED** — the two-way comparison could not, by itself, distinguish "Friedmann is the fix" from "`φ̄=0` masks a bug" | **Fixed**, not merely reworded: two real bugs found (missing `δφ̈` substitution; `k²` sign error), both independently re-verified as genuinely present, both fixed with real computation. |
| "Three genuine self-caught bugs" narrative | **WEAKENED** — a fourth (and structurally a fifth, currently-inert) bug was present, masked by the same `φ̄=0` choice used to diagnose the first three | **Fixed.** Both new bugs documented explicitly above, with the same evidentiary standard (independently re-derived, not merely patched) as the original three. |
| "Machinery is correct, only Friedmann is missing" | **FALSIFIED as originally stated** — not demonstrated for a nontrivial scalar background | **Fixed with real computation, not softened language.** Ran the exact isolation tests the skeptic proposed (Parts H, I) — both nonzero, confirming the original causal claim does not generalize. Verdict rewritten to state precisely what survives (Part G's narrow result) and what does not (the general claim). |
| `phibar=const` degenerate scalar background (skeptic's Finding 6) | **CONFIRMED-REAL concern** | **Addressed directly** — Parts H/I are exactly the "nontrivial scalar background" stress test the skeptic asked for. |
| Verdict lines not asserted (skeptic's Finding 4) | **CONFIRMED-REAL** — `is_zero_free`/`is_zero_fried` were printed, not regression-tested | **Fixed.** All four `is_zero_*` booleans (`free`, `fried`, `iso1`, `iso2`) now carry real `assert` statements with messages that fire if the result ever flips. |
| `G₀₀`/`G₀ᵢ` forms imported from prior findings, not re-derived in-file (skeptic's Finding 5) | **Noted, `[WEAK]`** — a real, acknowledged scope limit | **Not fixed here** — an independent re-derivation of `FINDING_P48`/`FINDING_P54`'s own results is out of scope for this file; those findings carry their own independent skeptic reviews already. Flagged explicitly as inherited, unverified-in-this-file scope, consistent with this campaign's own established convention for reused machinery. |
| Bug #1's diagnostic phrase ("must vanish in standard GR") implicitly assumes Friedmann (skeptic's Finding 8) | **CONFIRMED-REAL, narrative imprecision** | **Acknowledged** — bug #1 was indeed caught using a Friedmann-consistent diagnostic background, not a fully general one; this is consistent with (not contradicted by) the corrected Verdict above, which no longer claims Friedmann alone is sufficient in general. |

**True kill assessment:** no, but a real, substantial correction. Parts
A–D (the actual closed continuity/Euler/`Q^ν` equations) survive fully —
the skeptic did not dispute them. The constraint-propagation test's
**headline causal claim** did not survive in its original, overclaimed
form — replaced with a narrower, fully-tested claim (Part G's
scalar-free result stands; the general claim does not, per Parts H–I).
This is exactly the kind of correction this campaign's own discipline is
built to produce: caught before the finding was allowed to stand
unchallenged, fixed with real computation, and the resulting picture is
more precise, not merely softer.

## What this establishes, precisely

1. The `Φ,Ψ`-extension of `FINDING_P59`'s own continuity and Euler
   equations, with general `V_x` — genuinely new, cross-checked exactly
   against `FINDING_P59`'s own `Ψ=0` result and `FINDING_P50A`'s own
   `θ=0` continuity result, both confirmed. **Unaffected by the
   skeptic's corrections** — the bugs found live entirely downstream, in
   the `k`-space constraint-propagation test.
2. `Q⁰`/`Q¹` on the `Ψ`-perturbed metric — genuinely new, cross-checked
   exactly against `FINDING_P55`/`FINDING_P56`'s own flat-metric results.
3. **D5**, correctly scoped: this campaign's own long-standing "`a(t)`
   free" convention is directly responsible for the closed system's lack
   of Bianchi consistency — demonstrated across three independent
   background choices (free; matter-only-Friedmann scalar-free;
   matter-only-Friedmann with nonzero KG-consistent scalar; total-energy
   Friedmann with nonzero scalar) — with the narrower positive result
   (Part G) correctly isolated from the general negative one (Parts H–I).
4. A worked, high-stakes example of this campaign's own "no silent
   fixes" discipline: a skeptic-caught overclaim in the headline Verdict
   itself, not just a supporting detail, corrected with real computation
   (two new bugs found and fixed, two new isolation tests run) rather
   than softened language.

## What this does NOT establish

1. **D2 vs. D3 from `FINDING_P60`.** Cannot be decided without first
   resolving D5 — and D5's resolution now looks like it requires a
   genuinely self-consistent coupled background solution, not a single
   missing relation.
2. **A genuinely self-consistent (`a`, `φ̄`, `ρ̄_A`) coupled background
   solution.** Named as the natural next step by Parts H–I's own
   negative result — not attempted here.
3. **The `ĝ≠0` (coupled) case of the decisive test.** Computationally
   prohibitive within this session even at `ĝ=0`; entirely untested.
4. **Whether Friedmann should be imposed using `ρ̄_phys` (`FINDING_P60`'s
   own physical density) rather than `ρ̄_A`** — extending `FINDING_P60`'s
   insight to the background level. Well-motivated, not attempted.
5. **A numeric value.** `ĝ`, `φ̄`, `ρ̄_A` remain symbolic throughout
   (except in the specific background diagnostics of Parts G–I, which
   use illustrative solutions, not a claim about this project's own
   background).
6. **D4** (history-dependent/kernel response) as a positive result —
   preempted by D5: without a closed, Bianchi-consistent system, there
   is no well-posed dynamical system to check for kernel-type behavior
   in the first place.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python P61_closed_dynamical_system_test.py
```
(To be run as `python experiments/20260803-bridge/P61_closed_dynamical_system_test.py`
once the file is moved there. Run time: several minutes — Parts F–I are
genuinely heavy symbolic algebra.)
