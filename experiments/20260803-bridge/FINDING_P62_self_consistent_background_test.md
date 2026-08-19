# FINDING P62 — a genuinely self-consistent (a, φ̄, ρ̄_A) background restores 0i-constraint (Bianchi) consistency, g_hat=0

**Status:** Skeptic-reviewed (Step 8a) and corrected. Not new physics — a
platform-validation / regression result for `FINDING_P61`'s own closed
system, with two skeptic-demanded discriminating tests added to confirm
it isn't vacuous.
**Script:** `P62_self_consistent_background_test.py` (`experiments/20260803-bridge/`)
**Scope:** strictly `V=0`, `ĝ=0` (free/uncoupled background). The `ĝ≠0`
coupled case is NOT tested here — explicitly flagged as still open below.

NOT_VALIDATION — NOT_REFUTATION — OUR_RECONSTRUCTION — L0: descriptive.

---

## Direct continuation of FINDING_P61

`FINDING_P61` (2026-08-19) built the closed dynamical system for `Ψ_k(t)`
and ran the user's own proposed decisive experiment (constraint route vs.
evolution route: does the 0i momentum constraint stay consistent under
the 00+continuity+Euler+scalar evolution, the standard GR Bianchi-identity
guarantee). After a context-blind skeptic review caught an overclaim in
that finding's own headline Verdict, the corrected result was: neither
matter-only Friedmann (Part H) nor total-energy Friedmann without matter's
own separate continuity (Part I) restores consistency once the scalar
background `φ̄(t)` is genuinely nonzero. `FINDING_P61`'s own closing
diagnosis, quoted directly from its corrected Verdict:

> "The most likely explanation: full Bianchi consistency requires the
> ENTIRE background (a, phibar, rhobar_A) to be a genuinely MUTUALLY
> self-consistent joint solution of Friedmann + matter's own continuity +
> the scalar's own KG equation, ALL SIMULTANEOUSLY — not 'add one extra
> relation on top of an otherwise free choice.' Constructing such a
> solution ... is a genuinely larger task, NOT attempted here."

This finding constructs that solution and tests the prediction directly.

## The background: exact two-fluid (dust + free scalar) FRW cosmology

At `ĝ=0`, matter and the scalar field decouple completely at the
background level (`Q^0, Q^1 → 0`), so each sector separately satisfies its
own standard equation:

- Matter continuity: `ρ̄̇_A + 3Hρ̄_A = 0` ⟹ `ρ̄_A ∝ a⁻³` (dust)
- Scalar background KG (`V=0`): `φ̄̈ + 3Hφ̄̇ = 0` ⟹ `φ̄̇ ∝ a⁻³` ⟹
  `ρ̄_φ := φ̄̇²/2 ∝ a⁻⁶` — a free massless scalar behaves EXACTLY as a
  standard "stiff fluid" (`w=1`), a textbook result.
- Friedmann: `3H² = 8πG_N(ρ̄_A + φ̄̇²/2)`

This is the classic, exactly-solvable "dust + stiff fluid" FRW system.
Separating variables on the Friedmann constraint (worked by hand first,
then verified symbolically) gives a closed form:

```
a(t)^3 = (9K/4)*B*t^2 - D/B,   K := 8*pi*G_N/3
```

where `B, D > 0` are the matter/scalar integration constants (`ρ̄_A=B/a³`,
`φ̄̇=√(2D)/a³`). Two concrete instances were used, `(B,D)=(1,1)` and
`(B,D)=(2,3)` — see the skeptic-caught correction below for what these
two instances actually establish (less than originally claimed).
**`H(t)=ȧ/a` comes out exactly rational in `t`** (the cube-root exponent
cancels in the logarithmic derivative) — only bare `a²`/`a⁻²` factors
elsewhere in the perturbation equations carry the leftover `1/3`-power,
which is what made this tractable for sympy.

**Physical domain:** `t² > 4/(9K)` (where `a³>0`) — the late-time branch
of this cosmology. A standard, explicitly-stated restriction for an exact
FRW solution, not a defect of the algebra.

**Three positive controls, all independently verified, symbolically,
exactly, for both `(B,D)` pairs:**

1. Friedmann: `3H² − 8πG_N(ρ̄_A+φ̄̇²/2) = 0` ✓
2. Matter continuity: `ρ̄̇_A + 3Hρ̄_A = 0` ✓
3. Scalar background KG: `φ̄̈ + 3Hφ̄̇ = 0` ✓

All three hold **simultaneously and exactly** — the genuine joint
self-consistency `FINDING_P61` Parts H/I did not have.

## The decisive test

`FINDING_P61`'s own fully-substituted 0i-constraint-propagation residual
(`cross`, at `ĝ=0`) was reproduced verbatim (Parts A–F, same code, same
variable names — cross-checked to reproduce the identical nonzero
free-background result before proceeding, confirming no drift in the
reused machinery). This background was then substituted into it.

**Self-caught bug, before skeptic review:** the original safety check
(`cross_ghat0.has(PHIBAR)`, meant to confirm the bare, undifferentiated
scalar background field never appears — so its closed form, an inverse
hyperbolic integral, would never be needed) tripped `True` and initially
looked like it blocked the whole approach. Diagnosis: `sympy`'s `.has()`
matches a symbol **anywhere in the expression tree, including inside
`Derivative(φ̄(t), t)` sub-nodes** — so it cannot distinguish "contains
`φ̄̇`" from "contains bare `φ̄`." The correct, term-by-term test (does a
term still reference `φ̄` after **both** `φ̄̇` and `φ̄̈` are zeroed out?)
found **zero** of 27 additive terms with genuinely bare `φ̄` — confirming
the derivative-only substitution was valid all along; the blocker was in
the diagnostic, not the physics. Fixed with the correct check; the run
then proceeded and only `φ̄̇(t)`/`φ̄̈(t)` (both clean, rational — no
inverse-hyperbolic closed form of `φ̄(t)` itself ever needed) were
substituted.

**Result, `(B,D)=(1,1)`:** `cross = 0`, identically.
**Result, `(B,D)=(2,3)`:** `cross = 0`, identically.

## Skeptic review (Step 8a) — the "two independent choices" framing was wrong

Context-blind review (finding.md + code only, no session history) found
no algebra bug in Parts J/K, confirmed the `.has()` diagnosis and fix were
correct, and confirmed the Part J background genuinely satisfies all
three of its own equations. But it identified a real methodological gap:

> "Both (B,D)=(1,1) and (B,D)=(2,3) are in the SAME one-parameter physical
> family ... the standard GR Bianchi identity `∇_μG^μν≡0` guarantees
> `cross=0` for ANY background in this family satisfying its three
> equations, not just one point. A second point-check cannot detect a
> 'coincidence' that the identity would produce anyway at every point."

This is correct and important: at `ĝ=0`, IF the closed system built in
`FINDING_P61` Parts A–D is a bug-free linearization of Einstein's
equations, THEN Bianchi's identity mathematically GUARANTEES `cross=0`
for *any* background jointly solving Friedmann+continuity+KG — regardless
of `(B,D)`. Testing a second `(B,D)` pair checks `sp.simplify`'s own
robustness on a different concrete expression; it is not independent
physical evidence that Parts A–D are correct, and the original wording
("confirmed for two independent choices") overclaimed exactly that.

**Two tests were added directly in response, per the skeptic's own
suggestions, both PASSED:**

**Part M — the actual discriminating test.** Does `cross` detect broken
self-consistency, or does the same algebraic *shape* of background always
give zero regardless of whether it's genuinely on-shell? Following the
Minimal Relaxation Rule (change exactly one assumption), `ρ̄_A` was
deliberately mismatched to a *different* integration constant (`B=5`)
than the one that built `a(t)` (`B=1`) — this breaks Friedmann (confirmed
nonzero residual, `-32πG_N/(6πG_Nt²-1)`) while leaving matter continuity
and the scalar KG equation intact (both independently confirmed still
zero — exactly one equation-of-motion violated, nothing else touched).
**Result: `cross` is genuinely, substantially nonzero** — a large,
honest, non-degenerate expression in `Ψ_k(t)`, `δρ_{A,k}(t)`,
`δφ̇_k(t)`. This confirms `cross` really is sensitive to whether Friedmann
specifically holds, not just to the algebraic family the background comes
from — Part K's zero was not vacuous.

**Part N — numeric cross-check independent of `sp.simplify`'s own
correctness.** A rare but real sympy risk: `simplify()` incorrectly
reducing a genuinely nonzero expression (with fractional-power/branch-cut
terms, exactly the kind present here) to a false symbolic `0`. The RAW,
unsimplified substituted expression was evaluated numerically (50-digit
precision) at two independent `(t,G_N,k)` points, with the free
perturbation functions `Ψ_k`, `δρ_{A,k}`, `δφ̇_k` fixed to generic
non-special rational constants (substituted *before* `t`, to avoid a
first-attempt bug where substituting `t` first turned the generic
function `Ψ_k(T)` into `Ψ_k(3)`, no longer matching a substitution keyed
on the generic object — caught and fixed before this became a false
"can't evaluate" result). **Result: `0.e-166` and `0.e-168`** at the two
points — exact zero to the precision computed, via a computational path
that never calls `sp.simplify` at all. The symbolic zero is not a false
positive.

## Verdict — corrected and scoped after Step 8a

**Within scope (`V=0`, `ĝ=0`, dust+stiff-fluid family, late-time branch):
the 0i constraint DOES stay consistent once the background genuinely,
jointly solves Friedmann+continuity+KG — and this is now backed by a test
that is shown (Part M) to actually discriminate on-shell from off-shell,
not just a repeat of the same guaranteed-zero family (Part L alone).**

**This is best read as a regression/platform-validation result for
`FINDING_P61`'s own Parts A–D, not as new physics.** GR's own Bianchi
identity mandates this outcome for *any* correct linearization once the
background is genuinely on-shell — the value of this finding is
confirming (a) Parts A–D contain no bug that manifests *on-shell*, (b)
this file's own background construction (Part J) is genuinely, doubly
correct, and (c) — most practically — there is now, for the first time,
a valid, Bianchi-consistent platform on which `Ψ_k(t)` could honestly be
solved as an initial-value problem, which was `FINDING_P61`'s original
ask and still has not been carried out.

**What this test structurally cannot catch, stated explicitly (skeptic
Point 1):** an algebra error in Parts A–D that happens to be dressed by a
factor proportional to a background equation-of-motion residual is
*invisible* to any on-shell test by construction — such an error
vanishes identically the moment the background goes on-shell, regardless
of whether the error is really there. This limitation is inherent to
on-shell consistency checks generally, not specific to this file.

## What this does NOT establish

- **The `ĝ≠0` (physically coupled) case is completely untested.** At
  `ĝ≠0`, matter and scalar no longer separately conserve (`Q^0,Q^1≠0`),
  so this exact dust+stiff-fluid solution is no longer valid — a genuinely
  coupled background would need to be constructed from scratch. This is
  the physically relevant case for MULTING and remains entirely open.
- **`Ψ_k(t)` has still not actually been solved.** This finding validates
  the platform on which that solve could now honestly be attempted; the
  D2/D3/D4 classification of `μ_phys(a,k)` that was `FINDING_P61`'s
  original goal has not been carried out.
- **Does not mean the "D5, structural endpoint" diagnosis was wrong in
  spirit.** The system genuinely WAS missing something (a
  self-consistent background) — this finding closes that specific gap for
  `ĝ=0`; it does not retroactively mean nothing was missing.
- **On-shell blindness (see above):** the test cannot rule out an algebra
  error dressed by a background-EOM-residual factor.
- **Only two concrete `(B,D)` instances, not a symbolic family — and
  Part L's second instance is NOT independent evidence** (see skeptic
  review above); its value is limited to a `sp.simplify` robustness check.
  A fully general symbolic `(B,D)` proof was not attempted.
- **The early-time branch (`t² ≤ 4/(9K)`) is entirely outside the tested
  domain** — where `a³→0⁺` and `H→∞`. Any behavior specific to that
  regime (e.g. near a cosmological singularity) is untested.
- `RHOBAR_A`'s own bare-occurrence safety was not checked with the same
  explicit termwise diagnostic used for `PHIBAR` — the full-function
  substitution (`.subs(RHOBAR_A, ...).doit()`) handles this correctly
  regardless (confirmed by the skeptic by hand), but the asymmetry in
  which check got the explicit diagnostic is worth noting.

## Not yet done

- The `ĝ≠0` coupled background construction and re-test (the physically
  relevant case).
- Actually solving the now-validated closed system for `Ψ_k(t)` and
  determining D2 vs. D3 vs. D4 for `μ_phys(a,k)`.
- Whether Friedmann should ultimately be sourced by `ρ̄_phys`
  (`FINDING_P60`'s own physical density) rather than `ρ̄_A` once `ĝ≠0`.

## Skeptic Verdict table

| # | Claim reviewed | Skeptic verdict | Response |
|---|---|---|---|
| 1 | Part J background construction (Friedmann/continuity/KG) | Correct, verified by hand | No change needed |
| 2 | Part K substitution completeness (`RHOBAR_A` derivative resolution) | Correct — `.subs(...).doit()` resolves it | No change needed |
| 3 | Self-caught `.has(PHIBAR)` bug and its fix | Correct diagnosis and fix | No change needed |
| 4 | "Confirms Parts A–D has no further hidden algebra bugs" (original caveat wording) | Overreach — on-shell test is blind to EOM-residual-dressed errors | **Fixed**: reworded to state this limitation explicitly in the Verdict |
| 5 | Verdict/caveat framing — caveat doesn't retract the adjacent overclaiming Verdict sentence | Real — reader who skips the caveat is misled | **Fixed**: Verdict section rewritten in one place, states the regression-test framing directly, no separate footnote-vs-headline split |
| 6 | "Two independent (B,D) choices" | **FALSIFIED as stated** — not independent; same Bianchi-guaranteed family | **Fixed**: reworded throughout; Parts M/N added as the tests that actually discriminate |
| 7 | Missing numeric spot-check against `sp.simplify` false positives | Real gap | **Fixed**: Part N added |
| 8 | Missing off-shell discriminating test | Real gap, most important finding | **Fixed**: Part M added, passed (genuinely nonzero) |
| 9 | Early-time-branch domain restriction not in "does not establish" | Real, minor gap | **Fixed**: added |
| 10 | `RHOBAR_A` bare-occurrence asymmetry vs. `PHIBAR`'s explicit check | Minor, not a bug | **Acknowledged**, left as noted asymmetry, not fixed (skeptic itself confirmed no actual issue) |

**True kill assessment:** no. The core claim (on-shell Bianchi consistency
restored by a genuinely self-consistent background, within the stated
scope) survives, strengthened by two new tests. What was killed was the
*framing* — "confirmed for two independent choices" was false as stated,
and the true evidential content is narrower: a validated regression test
for `FINDING_P61`'s own machinery, shown (via Part M) to be non-vacuous,
not an independent new physical discovery.
