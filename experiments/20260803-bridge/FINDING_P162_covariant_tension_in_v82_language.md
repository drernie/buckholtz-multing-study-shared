# FINDING P162 — docs/150 §6 item 3: does the covariant-completion sign
# tension (docs/130/131) survive re-expression in v82's own language?

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math + direct primary-source reading
**Script:** `P162_covariant_tension_in_v82_language.py` — the one sympy
check this file relies on (`ρ+3P/c² > ρ` for `P>0`), pulled out of an
inline Bash check into a standalone, re-runnable script, matching the
`P156`-`P161` precedent of pairing every FINDING with its own script.
**Verdict (final, post-skeptic — see "Correction" below for what changed
and why):** `THE FORCE LAW docs/130/131 TESTED IS UNCHANGED IN v82
(VERIFIED, P159) — THE TENSION IS NOT SHOWN TO BE AN ARTIFACT OF
two_field_action_closure.py's OWN CONSTRUCTION. v82's Sec IV.F passage,
READ AS ITS SINGLE MOST LITERAL CANDIDATE MECHANISM (Tolman/Komar active
gravitational mass, ρ+3P/c²), FAILS FOR ORDINARY POSITIVE THERMAL
PRESSURE — but that mechanism is a MONOPOLE-level quantity, and the
passage is motivating a DIPOLE effect, so this failure is illustrative of
the absence of an identified mechanism rather than a direct refutation of
what the passage itself claims. v82's OWN EXPLICIT DENIAL of internal
anisotropy ("no intrinsic axis") forecloses the one standard route
(anisotropic internal pressure/stress) that could have bridged monopole
to dipole — so, taken together, NO STANDARD GR CHANNEL BY WHICH ISOTROPIC
PRESSURE-SOURCING COMBINED WITH AN EXTERNALLY-SUPPLIED AXIS WOULD PRODUCE
A DIRECTIONAL FORCE HAS BEEN IDENTIFIED, in the passage or in this file.
THIS IS NOT A CRITICISM OF v82's THEORY (the passage is explicitly
hedged, "might"/"under the right conditions," and the force law's own
sign is POSTULATED in Eq. 1, not derived from this passage). v82's OWN
many-body "node" ontology does NOT, on inspection, surface a genuinely
new escape route via simple statistical/mean-field averaging — coarse-
graining many equivalence-principle-respecting positive-energy particles
reduces to exactly the same ρ+3P/c² mechanism already tested (this is
what the Tolman formula itself already is). A genuinely different class
of physics — CORRELATION/FLUCTUATION-INDUCED forces between the two
extended nodes (a gravitational analogue of the Casimir/van der Waals
effect) — is NOT UNSPECIFIED, per a 2026-08-30 literature-check
correction (below): it is a real, peer-reviewed effect ("gravitational
Casimir-Polder," Ford-Hertzberg-Karouby PRL 2016, `arXiv:1512.07632`),
directly verified — but it is ATTRACTIVE for similar-composition bodies
(matching the EM precedent's own sign, not contradicting it), the one
known repulsive channel (`arXiv:2501.02470`) is explicitly subdominant
for identical polarizabilities, and the entire effect is a one-loop
quantum-gravity correction, astronomically negligible at galaxy-cluster
mass/distance scales regardless of sign. Re-expression in v82's language
neither resolves nor dissolves the tension, and does NOT surface a
usable escape route — the one channel initially left unspecified has now
been checked against the literature and found both wrong-signed and too
small; no working mechanism, standard or exotic, has been identified
anywhere in this project's work.`
**Correction (2026-08-30, context-asymmetric skeptic-caught, four points,
all independently re-verified before being applied — not accepted on the
skeptic's word alone):** the first draft (a) treated the ρ+3P/c² reading
of Sec IV.F as effectively the intended mechanism rather than flagging it
as the most literal candidate among possibly-looser alternatives; (b) did
not notice that ρ+3P/c² is a MONOPOLE-level quantity being used to test a
DIPOLE-motivating passage — a real scope mismatch, independently
confirmed below, though shown NOT to rescue the passage once v82's own
"no intrinsic axis" denial is accounted for; (c) buried the NO_AUTHOR_ERROR
hedge in a late section instead of stating it as a premise governing how
much weight the whole analysis is entitled to; (d) **the most substantive
correction** — originally called the "many-body node" ontology a
"genuinely different, untested escape route," when in fact simple
statistical/mean-field averaging of many EP-respecting particles reduces
to the identical ρ+3P/c² mechanism already tested (independently
re-derived below, not just asserted) — the one channel that IS genuinely
different (correlation/fluctuation-induced forces) was not named in the
original draft at all, and even that channel's nearest physical precedent
points the wrong way. All four re-checked independently below (sympy for
the mean-field-reduction argument's premises, direct primary-source
re-reading for (a)-(c)), not merely re-worded from the skeptic's report.
**Continues/answers:** `docs/150` §6 item 3 ("Would this project's own
covariant-completion tensions (`P148`, `docs/131`) survive being
re-expressed in v82's own node/kinematic language, or are they specific
to the particular construction `two_field_action_closure.py` chose?").

## 0. Premise, stated first — `NO_AUTHOR_ERROR` (moved up per correction (c))

Everything below bounds only this project's own attempted covariant
reconstruction of MULTING's dipole term. It is not, and cannot be, a
claim about v82's own theory being wrong, for three independent reasons
that govern the weight every later section is entitled to carry:

1. The Sec. IV.F passage this file tests is explicitly hedged ("might,"
   "under the right conditions," "one might consider") — a plausibility
   gesture, not a claimed derivation.
2. v82's own force law does not derive its sign from this passage. The
   repulsive `−F^(1)` structure is stated directly in Eq. (1) as
   something "MULTING suggests" — a postulated structural choice. There
   is no claimed derivation here to be right or wrong about.
3. This project has no standing to judge whether TJB's own qualitative
   motivation is intended as more than plausibility color — only to
   check, as charitably as possible, whether taking it as a literal
   mechanism (the only way to test it against `docs/130`/`docs/131`'s own
   rigorous standard) would supply what's needed.

Because of (1)-(3), every verdict below is read as "this project could
not identify a working mechanism," never as "the mechanism does not
exist" or "v82 is wrong to invoke it."

## 1. What the existing tension actually is

`docs/130` (2026-07-22): tested whether a **local, ghost-free scalar-
mediator field theory** could reproduce MULTING's dipole term. Found:
"stable scalar–scalar exchange is attractive; MULTING's dipole is
repulsive. Repulsion requires vector mediation → vector charge →
angular" — a clean, mechanism-independent obstruction, not specific to
any one scalar theory.

`docs/131` (2026-07-22): tested a **vector-type internal-dipole medium**
(Blanchet–Le Tiec action, `CANDIDATE-L1`) — a structurally different,
more general construction than a bare scalar mediator. Found the sign
obstruction survives at a *deeper* level: "MULTING's repulsive dipole
requires the internal kinetic energy `k_A/c²` — a POSITIVE mass-energy —
to produce a net REPULSIVE gravitational effect. Positive energy
gravitates attractively (equivalence principle)... the repulsive dipole
is **not** the static weak-field limit of any equivalence-principle-
respecting, positive-energy, ghost-free local realization in which `k_A`
gravitates as the energy it is defined to be."

**Two independent mechanism classes tried (scalar exchange, vector
dipolar medium), both killed on the same underlying obstruction**: `k_A`
is defined (v6 and v82 both) as ordinary positive kinetic/thermal
energy, and standard, ghost-free, EP-respecting gravity does not let
positive energy repel.

## 2. The force law being tested is unchanged in v82 — `[VERIFIED, FINDING_P159]`

This session's own `FINDING_P159` §2 already established, by matching
v6's own raw Eqs. (14)-(17) directly against v82's own Eqs. (2)-(4)
(two independent primary sources, sympy-exact match): v82's dipole term
`F^(1)` is the **same mathematical object** `docs/130`/`docs/131` tested
— same `k_A/c²`-as-mass-energy structure, same repulsive sign (the `−`
in `F_P=F^(0)−F^(1)+F^(2)`, v82's own Eq. 1), same `1/s³` radial
dependence. **Nothing about the force law itself changed between v6 and
v82** — so any tension in reproducing *this specific mathematical
object* covariantly is not a property of which paper's notation is used.

## 3. v82's own stated motivation, read as a literal mechanism, at the CORRECT multipole level — `[VERIFIED-PDF p.17]`, corrected scope

v82's Sec. IV.F offers a qualitative motivation for the dipole's sign,
quoted precisely (already used in `FINDING_P160` for a different
purpose — the axis question, not the sign question addressed here):

> "General relativity suggests that pressure itself sources gravity,
> contributing to effective repulsion **under the right conditions**.
> Thermal motion is, physically, a pressure term..."

**Corrected reading (skeptic-caught gap (a)):** this is not necessarily
a commitment to a specific quantitative mechanism — it could be read as
a loose gesture toward the general GR fact that pressure contributes to
gravitational sourcing, without asserting that ordinary thermal pressure
specifically achieves the needed magnitude or sign. There is no fully
unambiguous alternative reading available, however: the passage's own
"under the right conditions" hedge only makes sense as a qualifier on a
*specific* mechanism (some conditions work, some don't) — a mechanism-
free rhetorical gesture would not need that hedge. So the ρ+3P/c²
(Tolman/Komar active gravitational mass) reading, tested below, remains
the single most literal, most charitable candidate — but is held with
the explicit caveat that it may not be the mechanism TJB intends, only
the one this file can test.

**Corrected scope (skeptic-caught gap (b), the more important
correction):** `ρ+3P/c²` is a **monopole-level** quantity — it describes
how much a region's internal pressure adds to or subtracts from the
*total, spherically-symmetric* active gravitational mass an outside
observer feels (the Tolman/Raychaudhuri focusing source, appearing in
both the Friedmann acceleration equation and the static weak-field limit
of why internal pressure increases a star's self-gravity). It carries no
intrinsic directionality. Sec. IV.F, by contrast, is motivating a
**dipole** (directional) effect. Applying a monopole-level fact to
critique a dipole-motivating passage is a genuine scope mismatch unless
an explicit bridge is supplied — e.g., an *anisotropic* internal pressure
distribution (`P_∥ ≠ P_⊥`), which sources a genuine quadrupole/directional
correction to the external field and is the standard way "pressure"
becomes "directional" in GR.

**v82's own text forecloses exactly this bridge.** The same Sec. IV.F
passage states explicitly: "a node's own thermal energy has no intrinsic
axis... one might consider that the line connecting the two nodes, not
any internal property of either node, supplies the direction, with a
node's thermal energy setting only the **magnitude**." This is a
denial of internal anisotropy, not an assertion of it — TJB is not
claiming an anisotropic-pressure mechanism sources the dipole; he is
positing an isotropic magnitude combined with an externally-supplied
axis. So the standard monopole→dipole bridge (anisotropic stress) is not
what the passage claims, and my `ρ+3P/c²` computation does not directly
refute what he wrote.

**What survives this correction:** neither TJB's own passage nor this
file has identified *any* standard GR channel — monopole active mass,
anisotropic stress, or otherwise — by which "pressure sources gravity"
combines with an externally-supplied axis to produce a directional
force. The `ρ+3P/c²` failure for ordinary pressure (below) is therefore
best read as evidence that the single most literal candidate mechanism
does not work, illustrating the absence of an identified mechanism,
rather than as a direct refutation of the (differently-shaped) claim
Sec. IV.F actually makes.

`[VERIFIED-sympy, P162.py]`, elementary: for **ordinary** thermal/gas
pressure (`P>0`, as any real intracluster-medium thermal pressure is),
`ρ+3P/c² > ρ` — **strictly more attractive**, not less. Repulsion via
this specific channel requires `P < −ρc²/3` — a dark-energy-like
*negative* pressure (tension), which is not a property ordinary thermal
(kinetic) pressure has. v82's own "under the right conditions" qualifier
is precisely correct and is not satisfied by ordinary thermal pressure —
so this specific literal reading, even granting it the most charitable
possible scope, does not supply the repulsion MULTING's dipole needs.

## 4. What v82's own many-body ontology does NOT surface: mean-field averaging is not a new mechanism

`docs/130`'s own text (2026-07-22, before v82 existed) named an escape
route neither it nor `docs/131` pursued: "central-vs-angular is a
DIAGNOSTIC, not a 3-way theorem; radiality can also arise from...
**statistical averaging**..." Both tested constructions (`docs/130`'s
scalar mediator, `docs/131`'s `CANDIDATE-L1`) model a node as an
effective **single point-particle** carrying one internal degree of
freedom. v82's own "node" ontology is different in kind: an **extended,
many-sub-particle thermodynamic object** ("the total of the kinetic
energies of the nucleons and electrons that comprise the intracluster
medium," v82 p.4). The original draft treated this structural difference
itself as a "genuinely different, untested escape route." **This was
overstated (skeptic-caught gap (d)) — corrected below.**

**Why mean-field averaging is NOT a new mechanism.** Suppose a node's
many constituent particles each individually respect the equivalence
principle — each is ordinary positive mass-energy, gravitating only
attractively, with no per-particle exception. Coarse-graining (replacing
the discrete particles by a smooth `ρ(x)`, `P(x)` and computing the
region's total stress-energy) does not introduce any new way for energy
to gravitate: the classical GR field equations map `T_μν → gravity` at
every scale, and the coarse-grained `T_μν` is just the sum of the
microscopic ones. **This is not an analogy — it is how the Tolman/Komar
active-mass formula is itself derived**: integrating `ρ+3P/c²` over a
distribution of ordinary matter *is* the statement of what a many-body
collection of EP-respecting particles sources, at the level the whole
node is being treated in §3. A "genuinely different escape route" would
need to point to physics **not already captured** by the mean `ρ(x)`,
`P(x)` fields — simple statistical averaging over many identical,
non-interacting-beyond-mean-field particles does not do this. Re-stating
"the node is made of many particles" does not by itself supply new
physics; it restates the premise `ρ+3P/c²` was already built from.

**What WOULD be genuinely different, and its status.** Correlation- or
fluctuation-induced forces between the two extended nodes — a
gravitational analogue of the Casimir or (thermal) van der Waals effect,
sourced by correlations in the many-body matter distribution that are
*not* captured by the mean fields alone — are a structurally distinct
class of physics from anything `docs/130`/`docs/131`/§3 above tested.

**Correction (2026-08-30, literature check — this file's original claim
"none is known to this project to exist in the literature" was checked
and found FALSE, not merely unverified):** a real, peer-reviewed
"gravitational Casimir-Polder" literature exists and is directly on
point. `[VERIFIED-arXiv, direct abstract fetch, not agent-report alone]`:
Ford, Hertzberg & Karouby, *Quantum Gravitational Force Between
Polarizable Objects*, Phys. Rev. Lett. 116, 151301 (2016),
`arXiv:1512.07632` — computes exactly this class of effect (a quantum
correction to the gravitational potential between two distant,
polarizable extended bodies, from induced quadrupole moments via
two-graviton exchange, "in close analogy to the Casimir-Polder... force
between a pair of atoms"). Its own far-field result, quoted directly from
the abstract: `V(r) = −3987·ℏcG²α_1S·α_2S/(4π·r¹¹)` — **negative**, i.e.
**attractive**, for two bodies with the same-sign (ordinary, positive)
static gravitational quadrupole polarizability. A follow-on line of work
(Hao, Hu & Yu, *Repulsive quantum gravitoelectric-gravitomagnetic
interaction*, `arXiv:2501.02470`, 2025) finds one genuine repulsive
channel — a cross-coupling between gravitoelectric and gravitomagnetic
polarizability — but its own abstract, quoted directly: "for two
isotropically polarizable objects with **identical** gravitoelectric and
gravitomagnetic polarizabilities... the repulsive quantum interaction
**cannot surpass** the attractive interactions." Since MULTING's own two
nodes are modeled as same-type objects (both ordinary galaxy-cluster
thermal-energy sources, no asymmetry named anywhere in v82's own
construction), this is exactly the "identical polarizabilities" case in
which the one known repulsive channel is explicitly subdominant.
Separately: every result in this literature is a **one-loop quantum-
gravity correction** (two-graviton exchange, `ℏ`-suppressed by
construction) — astronomically far below any classical, macroscopic
effect at galaxy-cluster mass and distance scales, regardless of sign.
**Corrected label: this channel is SPECIFIED in the literature, not
unspecified — but remains sign-unfavorable (attractive for similar
bodies; the one known repulsive term is explicitly subdominant for
identical polarizabilities) and separately magnitude-irrelevant
(quantum-loop-suppressed, not a candidate classical mechanism at all at
these scales).** This strengthens, not weakens, this section's own
conclusion — the escape route is not merely unbuilt, it is built,
checked, and found both wrong-signed and far too small.

Its *nearest available physical precedent* was already correctly
characterized as unfavorable even before this correction: ordinary EM
Casimir and thermal van der Waals forces between two bodies of
**similar** material are generically **attractive** (Lifshitz theory) —
a sign reversal (as in the Dzyaloshinskii–Lifshitz–Pitaevskii
configuration) requires an *asymmetric* three-medium geometry that has
no obvious analogue named for two similar galaxy-cluster nodes. The
literature check above confirms this EM intuition transfers correctly to
the gravitational case: the actual gravitational-Casimir-Polder result
is attractive for similar bodies, matching the EM precedent's own sign,
not contradicting it.

## 5. Answer to item 3

**The tension is not shown to be specific to `two_field_action_closure.py`'s
own construction choice.** The mathematical object both `docs/130` and
`docs/131` tested is unchanged in v82 (§2). v82's own offered qualitative
motivation, read as literally and as charitably as the standard GR
mechanism it most plausibly invokes allows, fails for ordinary thermal
pressure at the monopole level (§3) — and, once the scope-correct
reading is applied, neither the passage nor this project has identified
*any* standard mechanism, monopole or directional, that would produce
the needed effect (§3). v82's own many-body node ontology does not, on
correct inspection, supply a new escape route via simple statistical
averaging (§4) — that reduces to the same tested mechanism. The one
genuinely distinct class of physics that remains conceivable
(correlation/fluctuation-induced forces) is, per the 2026-08-30
literature-check correction in §4, not unspecified — it has been built,
in the published literature, and checked directly: attractive for
similar-composition bodies, the one repulsive term subdominant for
identical polarizabilities, and quantum-loop-suppressed in magnitude
regardless of sign. **Re-expressing in v82's language does not dissolve
the tension, and does not surface a usable escape route** — the honest
state is: no mechanism has been found, and the one remaining speculative
class of physics, now actually checked against the published literature
rather than merely named, is confirmed both wrong-signed and too small.

## What this file does NOT establish

1. **Not a claim about v82's own theory being wrong** (`NO_AUTHOR_ERROR`,
   §0) — v82's own force law does not depend on the Sec. IV.F passage
   this file checked; that passage's status (motivation vs. derivation)
   is TJB's own to characterize, not this project's to judge.
2. **Does not independently re-derive the gravitational-Casimir-Polder
   result cited in §4's correction** — the abstracts of `arXiv:1512.07632`
   and `arXiv:2501.02470` were fetched and quoted directly, not re-derived
   from first principles; this file trusts the published result's own
   stated sign and scaling, standard practice for citing an established
   literature result rather than reproducing it.
3. **Does not re-examine `docs/130`'s own two "residual open branches"**
   (a `k_A` that is somehow not its own mass-energy; a driven
   non-equilibrium theory) beyond what `docs/131` already concluded.
4. **Does not address `P148`'s own separate promoted-with-qualifiers
   status** for the covariant completion program as a whole — only the
   specific sign-tension question `docs/150` §6 item 3 asked about.
5. **Does not prove no mechanism exists** — only that none has been
   identified by this project, TJB's own hedged passage, or the standard
   GR channels (monopole active mass, anisotropic stress, mean-field
   many-body averaging) checked here.
