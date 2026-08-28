# FINDING P145 — non-minimal vector operator-basis gate: two candidates
# remain genuinely open, none closes cleanly

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 mixed
(reasoning classification + symbolic checks)
**Verdict:** `TWO-OPERATORS-OPEN` — corrected from an earlier draft's
`NO-HEALTHY-VECTOR-ESCAPE`, per independent skeptic review, §0 below.
**Origin:** third step of `P142`'s cheapest differentiating test, testing
the single candidate `P144` left open (non-minimally-coupled vector
construction), per the user's own explicit protocol for this step.
**Script:** `P145_nonminimal_vector_operator_gate.py` (symbolic + numerical
checks, ruff clean, does not touch the 881-test suite)

---

## 0. Correction (same day, independent skeptic review) — read this first

An earlier draft of this file closed `R_μνA^μA^ν` as contributing
**exactly zero** to the two-body interaction, based on verifying the
linearized Ricci tensor vanishes for `r ≠ 0` (vacuum Ricci-flatness away
from a point-mass source). An independent, context-asymmetric skeptic
review (this file + script + `P144` + `docs/131` only, no reasoning chain)
**FALSIFIED** that closure: `R_μν` is proportional to the stress-energy
tensor `T_μν` via the (trace-reversed) Einstein field equation itself —
`R_00 = 4πGMδ³(x)` for a point mass — so it is zero *away* from a source,
but **not zero at the source itself**, where it has delta-function support.
The original check only verified the away-from-source region and wrongly
inferred a global "contributes nothing" statement from it. Independently
re-verified (§3 below, not just accepted on the skeptic's say-so): the
operator, evaluated with its delta-function support at body B's own
location, gives a genuine `1/r³` force — reaching MULTING's target power
law directly, with a coupling sign not fixed by anything established so
far. This is the same class of error as `P143`'s original overreach (§3a
there) and `P144`'s title imprecision: a narrow, correctly-computed fact
licensing a broader closure it does not actually cover. Corrected in place,
not silently — the original (wrong) closure is not reproduced below.

The skeptic separately WEAKENED §4's framing (Check 2, magnetization
coupling): `docs/131`'s Branch S is a *monopole-dipole* configuration
(body B is a plain mass, body A carries the dipole); Check 2 as computed is
a *dipole-dipole* configuration (both bodies carry the magnetization
moment). The qualitative parallel drawn between them (both have an
attractive stable / repulsive unstable structure) is correct as a
*separate* finding, but is not a matched calculation of the same target
configuration — stated explicitly in §4 below, not implied as identical.

---

## 1. Question, exactly as posed

Reconstructed thesis (user's own framing, this session): can the EP/
stability/staticity tension `docs/131` found — and which `P143`/`P144`
showed is not escaped by the constructions checked so far — be lifted by a
**non-minimally-coupled vector completion**, without reopening branches
already closed? Not "does some complicated vector theory work in general,"
but the narrower question: does a *minimal* non-minimal vector operator
exist that flips the dipole branch's sign/stability without breaking
rotational covariance, ghost-freedom, or the static limit?

## 2. Operator basis, filtered against the user's own 6 criteria

The user proposed four candidate operators to classify, explicitly as a
basis to filter rather than a ready model: `A_μJ^μ`, `F_μνF^μν`,
`R_μνA^μA^ν`, `(∇_μA^μ)²`. Criteria (user's own): (1) not reducible to an
already-tested minimally-coupled massless mediator; (2) doesn't require a
genuine current/motion source given the target dipole is static; (3) no
Ostrogradsky ghost; (4) rotational covariance; (5) clear weak-field/static
limit; (6) genuinely new tensor structure, not just a rescaled old term.

| Operator | Verdict | Why |
|---|---|---|
| `A_μJ^μ` (minimal coupling) | **Already tested** | This is exactly `P143`'s own construction (monopole order) or the source-current structure underlying `docs/131`'s Branch S/H (dipole order) — fails criterion 1 as a standalone candidate; kept as the baseline the others are compared to, not re-tested. |
| `F_μνF^μν` | **Not a coupling candidate** | This is the vector field's own free kinetic term (always present for *any* propagating vector theory) — it doesn't couple to matter at all, so it cannot by itself change how `k_A` sources or responds to the field. Fails criterion 6 (no new matter-coupling structure). |
| `R_μνA^μA^ν` | **OPEN — reaches target power law, sign unfixed, §3** | Vanishes *away* from any source, but has delta-function support *at* each source; properly evaluated, gives a `1/r³` force directly with a free-sign coupling. |
| `(∇_μA^μ)²` | **Ambiguous, not cleared — §5** | Splits into a gauge-artifact case (no new physics) and a genuine-Lorentz-symmetry-breaking case (ghost-risk, not resolved here). |
| Magnetization-current coupling (added here, not in the user's original list — §4) | **Closed by computation, §4 — but see monopole-dipole/dipole-dipole caveat** | Motivated directly by `P144`'s own flagged, not-fully-closed loophole (the "static = steady-state, currents permitted" reading). Genuinely satisfies criteria 2, 4, 5, 6 — but is a *dipole-dipole* configuration, not a matched calculation of `docs/131`'s own *monopole-dipole* target — closes on its own terms, not as a literal Branch S re-test. |

## 3. `R_μνA^μA^ν` — does NOT close; reaches the target power law with an
## unfixed sign

**Check 1a** (kept, unchanged) computes the *linearized* Ricci tensor of
the standard weak-field metric sourced by a static point mass
(`h_00 = h_ii = 2GM/r`, harmonic-like gauge) and verifies every component
vanishes identically for `r ≠ 0` — i.e., away from the source. Positive
control: the same computation confirms `∇²(1/r) = 0` for `r ≠ 0`. This part
was correct and remains in the script, but does **not** by itself license
"the operator contributes nothing" — see §0.

**Check 1b** (added post-correction) computes what Check 1a's own scope
missed: `R_μν` is not a free-standing geometric quantity to evaluate at
"generic" points — it is fixed *by the field equations themselves* to be
proportional to the stress-energy tensor, `R_μν = 8πG(T_μν − ½η_μνT)`. For
a point mass at rest, `T_00 = Mδ³(x)`, giving `R_00 = 4πGMδ³(x)` — verified
here via the divergence theorem (`∮∇(1/r)·n̂ dA = −4π` over any sphere
enclosing the origin, `R`-independent — the standard proof that
`∇²(1/r) = −4πδ³(x)`), not asserted from memory.

Evaluating the operator's contribution to the two-body action requires
integrating over *all* space, including body B's own location, where this
delta function sits. With body A's field taking its standard Coulomb-like
form `A_0(x) = k_A/(4π|x−x_A|)` (matching `P143`'s own `1/(4π)`
normalization), the delta function picks out:

```
V(r) = λ · (4πG M_B) · [k_A/(4πr)]²  =  λ G M_B k_A² / (4πr²)
dV/dr = −λ G M_B k_A² / (2πr³)   →   FORCE ~ 1/r³
```

**This reaches MULTING's target power law directly** (`Δα=0` — no extra
derivative needed, unlike `P143`'s minimal-coupling case, which needed
`Δα=1`). The coupling `λ` is this non-minimal operator's own free
coefficient; nothing established anywhere in this project's chain fixes
its sign (the `k_A`-is-energy argument that fixed the *minimal*-coupling
sign in `docs/131` §(5) does not apply here — `λ` multiplies a genuinely
new operator, not `k_A` itself).

**Consequence: NOT closed.** `R_μνA^μA^ν` is a live `VECTOR-ESCAPE-CANDIDATE`
by the power-law criterion — its fate hinges entirely on whether its
coefficient `λ` is constrained in sign by ghost-freedom or EFT positivity
bounds (unitarity/causality constraints on higher-dimension operator
coefficients, e.g. the kind of argument in Adams et al.-type positivity-
bound literature) — a check this file does not perform, same open status
as `(∇_μA^μ)²` below.

## 4. Magnetization-current coupling — closed on its own terms, a
## qualitative (not matched) parallel to Branch S

**Motivation, stated explicitly:** `P144`'s Argument C closed the
static-source escape route under the strict reading "static = zero internal
currents." Its own review flagged this as a *definitional* dependency, not
a physics gap: a fixed, time-independent internal magnetization
(the textbook permanent-magnet mechanism — bound current
`J^i_mag = ε^{ijk}∂_jM_k`, non-zero even with zero translational motion)
genuinely satisfies the user's criteria 2 (no literal motion needed), 4
(rotationally covariant construction), 5 (standard weak-field limit — the
ordinary magnetic dipole field), and 6 (a *bona fide* new angular structure,
`[m_A·m_B − 3(m_A·r̂)(m_B·r̂)]/r³`, not `cosθ`). This is the one candidate
worth actually computing, not just classifying qualitatively.

**Check 2** computes the standard dipole-dipole interaction energy
`U(θ_A,θ_B,φ) = (μ₀/4πr³)[m_A·m_B − 3(m_A·r̂)(m_B·r̂)]` symbolically, finds
its stationary points over the 3 orientation angles, and ranks them by
energy. **Robustness check:** an 8-million-point numerical grid search over
the full `(θ_A,θ_B,φ)` domain confirms the hand-picked symmetric candidates
are in fact the global extrema (matches to `1e-6`) — the symbolic analysis
was not left to rest on 4 guessed points alone.

**Result:** the global energy MINIMUM (stable configuration) is
`θ_A=θ_B=0` — both moments aligned along the separation axis, "head to
tail" — with `U_min = −μ₀M_AM_B/(2πr³) < 0`, i.e. **attractive**. The global
energy MAXIMUM (unstable) is `θ_A=0, θ_B=π` — "head to head" — with
`U_max = +μ₀M_AM_B/(2πr³) > 0`, i.e. **repulsive**.

**Consequence, with the configuration-mismatch caveat stated explicitly
(per skeptic review, §0):** `docs/131`'s Branch S is a *monopole-dipole*
configuration — body B is a plain mass monopole, only body A carries the
dipole moment. Check 2, as computed, is a *dipole-dipole* configuration —
both bodies carry the magnetization moment (required for a genuinely
magnetic-type coupling to exist at all, per `P144`'s own Argument C: a
static mass monopole sources no magnetic field for a lone magnetic dipole
to couple to). These are not the same target problem, and this file does
**not** claim Check 2 is a re-derivation of Branch S under a new mediator —
only that it is a *separate*, independently-computed finding with the same
*qualitative shape* (attractive configuration is the stable minimum,
repulsive is the unstable maximum), for a genuinely different angular form
(`[m·m − 3(m·r̂)(m·r̂)]` vs. `cosθ`). On its own terms, this candidate
closes: the magnetization-current mechanism does not produce a stable
repulsive branch for the dipole-dipole configuration it actually describes.
It does **not**, by itself, establish anything about a monopole-dipole
magnetic construction (which would need body B to source a magnetic-type
field some other way — not attempted here, and not obviously constructible
given `P144`'s own closure of that specific route).

## 5. `(∇_μA^μ)²` — not cleared, flagged honestly as unresolved

This term is the structure of a covariant gauge-fixing term (e.g. Feynman/
Landau/`R_ξ`-gauge in QED: `L_gf = −(1/2ξ)(∂_μA^μ)²`). Two readings:

- **As pure gauge-fixing** (accompanying the correct BRST/ghost sector):
  physical observables — including the static force between two charges —
  are provably independent of the gauge parameter. This reading changes
  nothing: same `α=2` propagator power `P143` already used, no new physics.
- **As genuine new physics** (an explicit term added on top of an already
  gauge-fixed theory, giving the field's longitudinal mode a mass-like
  self-interaction outside the standard Proca/Stückelberg structure): this
  is exactly the kind of construction whose ghost-freedom is *not*
  automatic — it is the specific, well-known difficulty behind
  Lorentz-violating vector-tensor theories (e.g. Einstein-aether)
  needing dedicated constrained-Hamiltonian (Dirac-Bergmann) analysis to
  establish which coefficient signs avoid a ghost.

**This file does not resolve which reading applies, or run that analysis.**
A full ghost-freedom check for this specific coupling requires either a
literature-grounded citation of the relevant no-ghost condition or an
original constrained-Hamiltonian derivation — both are more than this
step's own "cheap structural gate before expensive construction" scope
calls for, and getting the ghost condition wrong by rushing it would be a
worse outcome than leaving it open. **Recorded as: ambiguous, tentatively
ghost-risk-flagged, not established either way.**

## 6. Answer to P145's own decision tree

Per the three-verdict system specified for this step:

- `NO-HEALTHY-VECTOR-ESCAPE` — **not established.** Only the magnetization-
  current candidate closes cleanly (§4), and even that closes a
  *dipole-dipole* configuration, not a matched re-test of `docs/131`'s own
  monopole-dipole target.
- `VECTOR-ESCAPE-CANDIDATE` — **not yet established either.**
  `R_μνA^μA^ν` reaches the right power law with a free-sign coupling (§3) —
  a real candidate on the power-law criterion — but "escape candidate"
  per the user's own success criterion requires a demonstrated stable
  repulsive branch, which needs `λ`'s sign to be shown compatible with
  ghost-freedom/positivity, not merely undetermined by what's checked so
  far. An unconstrained free parameter is not the same claim as a
  positive result.
- `DYNAMIC-ONLY-ESCAPE` — not directly tested here (would require dropping
  staticity, `docs/131`'s branch 3 territory, out of this step's scope).

**Corrected verdict: `TWO-OPERATORS-OPEN`, not `NO-HEALTHY-VECTOR-ESCAPE`.**
Two operators — `R_μνA^μA^ν` (sign of `λ` unconstrained) and `(∇_μA^μ)²`
(ghost status unresolved) — remain genuinely undecided pending checks this
"cheap gate" step was not scoped to perform. Per the user's own stated
success criterion, this state of affairs does **not** yet justify a `P146`
full numerical construction either — but for a different reason than the
original draft gave: not because both candidates are closed, but because
neither open candidate has been shown to actually *work* (only that neither
has been shown *not* to). The next cheap step, before `P146`, is resolving
`R_μνA^μA^ν`'s sign constraint and `(∇_μA^μ)²`'s ghost status — likely via
a literature check (EFT positivity bounds; Einstein-aether-type no-ghost
conditions) rather than original derivation, given both are established
technical literatures this project should consult rather than re-derive.

## 7. Competing hypotheses (M0–M3), scored against what was found

- **M0 (no escape)** — supported only by the magnetization-current
  candidate, and only for the dipole-dipole configuration it actually
  describes (§4's caveat). Not supported for `R_μνA^μA^ν` (§3) or
  `(∇_μA^μ)²` (§5) — both remain open, weakening M0's overall support
  relative to the original (incorrect) draft's stronger claim.
- **M1 (genuine vector escape exists)** — `R_μνA^μA^ν` is now a real,
  not-yet-ruled-out candidate on the power-law axis; whether it survives a
  sign/ghost check is the open question, not settled either direction.
- **M2 (escape only via pathology)** — plausible for both open operators
  (`(∇_μA^μ)²`'s Lorentz-violation reading; `R_μνA^μA^ν`'s possible
  positivity-bound violation for the sign needed to get repulsion) — but
  neither is established, that's exactly what's unresolved for both.
- **M3 (escape only beyond staticity)** — not tested here by design (this
  step's whole point was checking whether a *static* non-minimal vector
  construction could work); remains open as `docs/131`'s own branch 3,
  already flagged as "a different theory, not a completion of the same
  target."

## 8. What this file does NOT establish

1. **Not a complete operator-basis classification.** Only the 4 user-named
   operators plus one user-motivated addition were checked; an EFT
   operator-basis enumeration at a stated order (`docs/123`'s "moonshot"
   category, explicitly out of scope for this cheap-gate step) could in
   principle surface further candidates.
2. **Does not resolve `(∇_μA^μ)²`'s ghost status** — left open, not
   force-closed, per §5.
3. **Does not resolve `R_μνA^μA^ν`'s coupling sign** — reaches the right
   power law (§3), but whether `λ` can consistently take the sign needed
   for a *stable* repulsive branch (not just any sign) is unchecked.
4. **Does not touch `docs/131`'s branch 3** (driven non-equilibrium /
   non-static) — M3 is a different physical target, not this step's
   question.
5. Nothing about MULTING itself (Gate 1) — every operator checked here is
   this project's own candidate completion, not a claim about TJB's theory.
6. **Not yet a full P142 verdict.** Per `P142`'s own decision tree
   (`falsification-ladder.md`'s CDT Protocol), the accumulated picture
   across `P143`+`P144`+`P145` is: every construction actually computed
   hits *some* obstacle or open question, but the specific obstacle
   differs by class (derivative-coupling cost for vector-monopole;
   EP-tension for static-vector-dipole; unresolved sign/ghost status for
   the two non-minimal operators) — consistent with, not yet proof of,
   `P142`'s own "structural tension" hypothesis, and now with two
   genuinely open threads rather than a clean closure.
