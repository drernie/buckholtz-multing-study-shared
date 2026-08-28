# FINDING P144 — docs/131's "vector/antisymmetric sector" residual branch
# narrows: two of its three natural readings collapse into already-tested cases

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 structural/reasoning
**Verdict:** `BRANCH-2-NARROWED-NOT-ELIMINATED` — a reasoning-based result
(no numerical script; the question is structural, per
`falsification-ladder.md`'s Structure-Bias Guard, same class as `FINDING_P139`)
**Origin:** second step of `P142`'s cheapest differentiating test, following
`P143` (vector-mediator, monopole order)

**Precision note (title corrected after skeptic review, §1a below):** this
file does *not* claim two of `docs/131`'s three *residual branches* collapse
— branches 1 (`k_A` not its own energy) and 3 (driven non-equilibrium) were
already dispatched by `docs/131` itself, not by this file (§2). This file's
actual contribution is narrower and more specific: of the *sub-readings* of
branch 2 ("vector/antisymmetric sector"), two collapse into already-tested
obstacles, leaving one genuinely open. The original title conflated these
two claims; corrected here rather than silently.

---

## 1a. Independent skeptic review (same day, context-asymmetric)

Dispatched with only this file + `docs/131` + `FINDING_P143` (no reasoning
chain, no session history), per `falsification-ladder.md`'s Context
Asymmetry Rule. Verdict: **CONFIRMED overall** — all three direct quotes
from `docs/131` verified exact; the core physics of all three arguments
(spin-independent propagator power-counting; multipole-geometry-fixed
`cosθ` angular form; static-source vector-field reduction to its timelike
component) independently re-derived and confirmed; no misquote, no missed
escape route (magnetic-dipole-via-static-source, non-standard minimal
coupling, current-loop internal structure, and higher-spin mediators were
all separately probed and found already covered). Three precision repairs
were required and are applied below (§3, §4, §5): the Kalb-Ramond line in
Argument A overstated what "redundant with P143" means for a field with no
natural minimal point-source coupling; Argument B needed its implicit
rotational-invariance assumption on `W(ξ)` stated explicitly; Argument C
needed its strict-E&M reading of "static" (zero internal currents, not
merely a fixed center of mass) stated explicitly as a dependency on how
MULTING's own text is read, not a physics gap. None of the three repairs
changes the bottom-line conclusion — full review text kept in this session's
record, not reproduced verbatim here per this project's own economy norms.

---

## 1. Why this file

`P143` tested one alternative construction (vector field, monopole-order
coupling) and found a *different* obstacle (derivative-coupling cost) than
`docs/131`'s scalar branches (EP-tension). Before building a *third*
numerical alternative, this file asks a cheaper question first, per the CDT
Protocol's own "differentiation" criterion (`falsification-ladder.md`): **do
the remaining named alternatives actually probe something new, or do some of
them collapse into cases already tested?** Two do. This is itself a valid,
low-risk CDT step — narrowing the search space costs nothing but careful
reading, before spending more derivation effort.

## 2. The three residual branches, verbatim

`docs/131` line 95-99, its own listed residual branches, each explicitly
flagged as "requires abandoning a standard assumption":

1. "a `k_A` that is somehow NOT its own mass-energy (contradicting the
   preprint's definition)"
2. "a genuinely exotic ghost-free vector/antisymmetric sector engineered to
   give static `1/r³` repulsion (not known to exist)"
3. "a driven non-equilibrium theory (not a static force law)"

Branch 1 is closed by definition (`docs/131` line 73-79, `k_A` IS energy by
MULTING's own text — not re-litigated here). Branch 3 is explicitly named as
*not a static force law*, i.e. it changes the target, not a completion of
it — also not re-litigated. This file's question is about branch 2 only:
does "vector/antisymmetric sector" name one open alternative, or several,
and are they all genuinely untested?

## 3. Argument A — mediator-spin power-counting is spin-independent at
## monopole order (tensor/2-form would repeat P143, not extend it)

`P143`'s Riesz-potential result (`Δα=1` needed to reach MULTING's target
power law from a monopole-order coupling) comes entirely from the
propagator's *momentum-power* in its denominator (`~1/k^α`), which is fixed
by the number of derivatives in the field's quadratic kinetic term. Every
standard minimally-coupled massless field — scalar, vector (Maxwell `F²`),
symmetric tensor (linearized Einstein-Hilbert), antisymmetric 2-form
(Kalb-Ramond `H²`) — has a two-derivative kinetic term, giving the *same*
`α=2` at tree level; the field's spin/index structure changes the
*numerator* (polarization sum, tensor contractions), not this radial power.
This is standard QFT power-counting, not a new derivation.

**Consequence:** testing a standard massless *vector* or symmetric-tensor
mediator at monopole order would reproduce `P143`'s own `Δα=1`-required
conclusion by the identical mechanism — not a new data point. The
antisymmetric 2-form case is subtler: a rank-2 antisymmetric field's minimal
source is a string worldsheet current, not a scalar point-mass density, so
strictly speaking a Kalb-Ramond field has *no* minimal monopole coupling to
MULTING's charges to test in the first place — either the coupling doesn't
exist minimally, or (if force-fitted) it inherits the same `α=2` propagator
power as any other minimally-coupled massless field and reproduces `Δα=1`.
Either way, not a genuine third alternative. Building a `P145` numerical
script for the vector/tensor case would be redundant work; the 2-form case
would need a non-minimal coupling to exist at all, which is already covered
by §5's "non-minimally-coupled" open case, not a separate branch. Recorded
here so neither is silently attempted later as if untested.

## 4. Argument B — the sign question does not depend on the internal
## potential's shape `W(ξ)` (already implicit in docs/131, not new)

`docs/131`'s own Branch S sets the interaction energy
`U_md(θ) = −G m_B P cosθ/r²`, where `P = |p_A|` is *fixed* by the internal
potential `W(ξ)` (`W` only fixes the magnitude, not `U_md`'s angular form —
`U_md`'s `cosθ` dependence comes from the standard monopole-dipole multipole
expansion `∫ρ_A Φ_B`, independent of what pins `|p_A|`). So no alternative
choice of `W` — harmonic, sombrero, or a third shape — can change which
orientation (`θ=0` vs `θ=π`) is the energy minimum; `docs/131` already
implies this by constructing `U_md(θ)` separately from `W(ξ)`. Not presented
as a new result — recorded so a future pass does not mistake "try a third
`W(ξ)` shape" for an untested alternative.

**Scope caveat (added after skeptic review):** this argument assumes `W(ξ)`
is *rotationally invariant* — i.e. `W` depends only on `|ξ|`, fixing the
dipole's magnitude but not privileging any direction. Both branches `docs/131`
actually built (harmonic, sombrero) satisfy this. An *anisotropic* `W(ξ)`
(one that itself prefers an internal direction, independent of the external
field — e.g. a crystal-like or coupled-internal-spin potential) is outside
this argument's scope and is not claimed to be closed here.

## 5. Argument C — the genuinely open part of branch 2, and why it narrows
## further under MULTING's own staticity claim

The one part of "vector/antisymmetric sector" not yet covered by Argument A
(monopole order, spin-independent) or Argument B (shape-independence) is a
vector field entering at **dipole order** — i.e. body A's internal moment
coupling to the *gradient* of body B's vector-sourced potential, mirroring
Branch S's own mechanism but for a spin-1 mediator. If this construction had
a genuinely different angular structure than `cosθ` (e.g. the
`[m_A·m_B − 3(m_A·r̂)(m_B·r̂)]/r³` form of magnetic dipole-dipole coupling in
electromagnetism), it could in principle prefer a different stationary
orientation than Branch S — a real, not-yet-closed alternative.

**But:** a magnetic-dipole-type angular structure requires the *source* to
carry a genuine vector/current character (a moving or rotating charge — in
electromagnetism, a static charge sources zero magnetic field; the magnetic
sector requires `J ≠ 0`, i.e. motion). `docs/131` line 68 states directly:
*"MULTING's dipole is static."* [CODE, direct quote] A minimally-coupled
massless vector field sourced by a **static**, non-rotating mass reduces, in
the static limit, to its timelike component alone — a genuine, standard
E&M/gravity fact (a static point charge has `A_i = 0`, hence `B = ∇×A = 0`;
only `A_0`, the "electric"/scalar-like potential, survives). A vector field
in this regime carries no more angular structure than a scalar potential —
so a "vector-dipole" construction built on a *static* monopole source
inherits the *same* `cosθ` angular form as Branch S, not a genuinely new one.

**Consequence:** the magnetic-dipole-type escape from branch 2 requires
either (a) a moving/rotating source, which `docs/131`'s own text excludes
for MULTING's dipole (would be branch 3's territory — "not a static force
law" — not a completion of the *same* target), or (b) a vector field with a
non-standard (non-minimal) coupling that manufactures vector structure
without source motion — which is not a "vector/antisymmetric sector" in the
plain sense `docs/131` named, but a *further* exotic modification on top of
it, and would need its own separate justification not yet given.

**Definitional caveat (added after skeptic review):** this closure reads
"static" in the strict E&M/gravity sense used throughout — `J^i = 0`,
literally zero internal currents, not merely a time-independent center of
mass. If MULTING's own notion of "static" is the weaker "steady-state, but
internal currents/rotation permitted" reading, a current-loop-like internal
structure in body A could source `B ≠ 0` even without net translational
motion, and this closure would not apply to that case. This is a dependency
on how MULTING's own text is read, not a physics gap in the argument above
— already flagged generally in §6 below, stated explicitly here per its own
term.

## 6. What this file does NOT establish

1. **Not a general no-go for all vector/antisymmetric constructions.**
   Argument C's closure is conditional on MULTING's own stated staticity
   (`docs/131` line 68) — if that premise is ever revised by TJB himself,
   this closure would need revisiting. This file does not touch MULTING
   (Gate 1); it only uses `docs/131`'s own already-established textual
   claim about MULTING's dipole being static.
2. **Does not rule out (b) above** — a non-minimally-coupled vector field
   engineered to carry vector structure without source motion. Named as
   genuinely open, not attempted here; would need its own construction and
   power-counting, likely inheriting a `P143`-style derivative-coupling cost
   (adding non-minimal structure to a vector coupling is exactly the kind of
   modification `P143` showed has a derivative-count price).
3. **Not a claim that P142's decision tree is now complete.** This file
   closes 2 of 3 ways to read "vector/antisymmetric sector" (monopole-order
   repeat, and static-source dipole-order collapse to Branch S), leaving (b)
   above as the one remaining, not-yet-constructed genuine alternative in
   this specific residual branch.
4. Nothing about MULTING itself — this is entirely reasoning about this
   project's own candidate completions and `docs/131`'s own prior text.

## 7. Answer to P142's cheapest-test question, so far

Combined with `P143`: of `docs/131`'s three named residual branches, one
(`k_A` not its own energy) is closed by definition, one (driven
non-equilibrium) changes the target rather than completing it, and the
third (vector/antisymmetric sector) is now shown to be narrower than it
first read — two of its three natural readings (monopole-order tensor/2-form
repeat; static-source vector-dipole) collapse into already-tested obstacles
(derivative-coupling cost, EP-tension respectively), leaving only a
non-minimally-coupled vector construction as a genuinely open, unconstructed
candidate. This is consistent with — and now somewhat stronger evidence
for — `P142`'s "structural tension" hypothesis: the space of *simple,
minimally-coupled* completions compatible with MULTING's target is smaller
than `docs/131`'s own listing suggested, without yet being provably empty.

**Per `P142`'s own decision tree:** this is not yet a verdict. One more
genuine construction attempt (the non-minimally-coupled vector case named in
§6.2, or the two-scalar construction named in `P142`'s prior update) is
needed before "2-3 alternatives, same tension" can be honestly claimed.
