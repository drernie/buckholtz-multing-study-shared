# FINDING P203 — Zych–Rudnicki–Pikovski (2018, arXiv:1808.05831):
# standard GR bookkeeping gives internal energy exactly ONE channel
# (additive to total mass, same monopole coupling) — sharpens
# FINDING_P172's own residual branch #1 from the opposite direction

**Date:** 2026-09-07
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (does standard, equivalence-principle-
consistent GR bookkeeping give a bound system's internal energy a
second, separately-scaling coupling to gravity, distinct from the
ordinary monopole mass term? — a literature check, not a claim about
v82's own construction)
**Trigger:** user supplied two PDFs (`2407.11929v3`, `2308.07373v2`) plus
an external AI-generated critique ("Суд") proposing a "Thermal-Energy
Bookkeeping Gate" for MULTING's `F^(1)~k_A r_A/s³` term, citing
`arXiv:2308.07373` for the composite-gravitational-mass result — a
citation the critique's own text flags elsewhere as wrong provenance
(the real composite-mass paper is `1808.05831`). Both attached PDFs
were read in full and confirmed off-topic for this specific question
(`2308.07373`: single-particle-only, explicitly names composite systems
as future work in its own Discussion, p.34; `2407.11929`: single-
graviton-detection experiments, unrelated). `1808.05831` was then
fetched and read in full via the arXiv MCP.
**Continues/answers:** `FINDING_P171`'s residual branch #1 (`docs/131`,
"a `k_A` that is somehow NOT its own mass-energy, contradicting the
preprint's definition") and `FINDING_P172`, which checked the same
branch from the EXOTIC-mechanism side (spontaneous scalarization — the
one known real theory class where a scalar "charge" is genuinely
distinct from an object's mass-energy) and found it does not naturally
trigger at cluster compactness (`GM/(Rc²)~10⁻⁵`-`10⁻⁶` vs. the neutron-
star threshold `~0.21`). This FINDING checks the SAME branch from the
opposite, non-exotic side: does ORDINARY, equivalence-principle-
consistent GR already contain a separate channel, with no exotic field
required?

## Status tags (per `docs/151_status_separation_rule.md`)

> **Empirical/Model status:** N/A — literature check, no fit, no code.
> **Ontological/mechanistic interpretation status:** the real result
> below (Zych–Rudnicki–Pikovski 2018) sharpens, but does not resolve,
> the open question of what physically licenses MULTING's `k_A`-sourced
> `F^(1)`/`F^(2)` terms as a channel separate from ordinary mass-energy.
> **Causal/cosmological claim status:** N/A.

## What the paper actually establishes `[VERIFIED-arXiv, read in full]`

Prior literature (Eddington & Clark 1938, and several subsequent
derivations) found that the *passive* gravitational mass of a bound
N-particle system — the quantity that couples to an external
gravitational potential `φ` — is not simply its total energy. To first
order in `c⁻²`, it appeared to be `M(G) = (R + 3T + 2U)/c²` (rest +
**3×**kinetic + **2×**potential/binding energy), rather than the naive
`R+T+U`. This "anomaly" was historically patched only by invoking the
virial theorem and time-averaging (`⟨2T+U⟩=0`), which the authors note
does not hold instantaneously or at the quantum level — a real,
long-standing puzzle, not a settled non-issue.

Zych–Rudnicki–Pikovski show the anomaly is a **coordinate artifact**.
Redone with two *concurrent* coordinate systems — arbitrary external
coordinates for the centre-of-mass world line (which couples to `φ`),
and the system's own **local, comoving rest-frame** coordinates for the
internal degrees of freedom (proper time/proper length, not
`φ`-redshifted external time/length) — the Hamiltonian collapses to the
clean single-particle form:

```
H = [Mc² + T_rest + U_rest] · (1 + φ/c²)
```

i.e. the gravitational mass **is** the total internal energy
(rest + kinetic + potential, all with equal, unit weight) evaluated in
the system's own local rest frame — no `3T`, no `2U`, and this equals
the *active* (ADM) mass, resolving the passive/active tension too.
Demonstrated explicitly for an EM-bound two-charge system, a
gravitationally-bound two-body system (Newtonian and full-PN), and a
"box of photons" — the "anomalous" terms in each prior derivation
traced directly to using `φ`-redshifted *external* coordinates to
describe what should be *local*, rest-frame internal quantities.

## Why this is the sharper half of P172's own question

P172 asked: *is there a real physics mechanism that lets a charge
sourcing a force be something OTHER than the object's own mass-energy?*
Answer found: yes, in principle (spontaneous scalarization), but it
does not trigger at cluster compactness under standard assumptions.

This paper answers the complementary question P172 did not ask:
*does ORDINARY, no-exotic-field-required GR bookkeeping itself already
contain some subtlety that could give internal energy (thermal,
kinetic, binding — of any kind) a second, differently-scaling coupling
channel, distinct from the plain monopole mass term?* The answer here
is **no** — once bookkeeping is done correctly (local rest frame for
internal DOFs), internal energy of *any* kind gets exactly one channel:
it adds, at unit weight, into the single scalar `Mc²+T_rest+U_rest`
that sources/responds to the ordinary `1/r²`-type coupling. The
"anomalous virial terms" that might have looked like a second channel
were never a real second channel — they were a coordinate mistake.

**Combined with P172:** MULTING's `F^(1)~k_A r_A/s³` construction (a
thermal-energy-sourced term with a DIFFERENT radial scaling than the
ordinary monopole, i.e. structurally a second channel) has no natural
home in either of the two most obvious candidate mechanisms this
project has now checked: not the exotic route (scalarization, blocked
by P172's own compactness argument at cluster scale) and not the
ordinary route (standard GR bookkeeping, closed off by this paper —
internal energy just adds to mass, full stop, no second channel "for
free"). This does not prove no mechanism exists; it narrows what kind
of mechanism MULTING would need — genuinely new physics beyond both of
these, independently motivated, not inherited from either standard GR
or the one known real exotic-charge theory class.

## Two real limits — where this result does NOT directly transfer to MULTING

1. **Scope mismatch: one body in an external field, not two mutually-
   interacting extended sources.** The paper's own physical setup
   throughout (Introduction, p.2; every worked example) is a *small*
   composite system's own mass coupling to an *external* potential from
   *a much more massive object* ("like the Earth"), under the explicit
   assumption that tidal forces are negligible across the small system.
   MULTING's node-pair force law is a mutual interaction between two
   *comparable-mass*, spatially *separated* extended sources, each
   contributing its own charges to a two-body force `F(s)`. Nothing in
   this paper's derivation addresses that two-body, mutual-sourcing
   case directly — extending the argument there is a further step this
   paper does not take.
2. **"Standard GR gives no such channel for free" ≠ "no mechanism could
   ever give MULTING one."** MULTING is explicitly a modified/extended
   framework, not vanilla GR — this paper only closes off the option of
   inheriting a free, no-new-physics channel from ordinary equivalence-
   principle bookkeeping. It does not, and does not attempt to, survey
   every possible modified-gravity construction that could license a
   `k_A`-sourced separate term.

## What this does and does NOT establish

**Does establish:** a real, verified, directly relevant result — under
standard, equivalence-principle-consistent GR bookkeeping, a bound
system's internal energy of any kind contributes to gravity through
exactly one channel (additive to total mass, local rest frame), not
two. This is new to the project (`grep -rl "Zych\|Rudnicki\|1808.05831"`
— zero prior hits) and sharpens, from the non-exotic side, the same
open question P172 already narrowed from the exotic side.

**Does NOT establish:**
1. Whether MULTING's own `k_A`/`F^(1)`/`F^(2)` construction is
   physically wrong — `NO_AUTHOR_ERROR`; this bears on what license
   *standard* physics gives for free, not on whether MULTING's own,
   explicitly-extended framework is internally consistent or correct.
2. Anything about the two-body, mutual-sourcing case MULTING actually
   needs — this paper's own scope is one small system in an external
   field from a much larger mass, not two comparable, separated,
   mutually-interacting extended sources.
3. That no mechanism could license a separate channel — only that
   neither of the two candidates this project has now checked
   (ordinary GR bookkeeping; spontaneous scalarization) supplies one
   "for free" at cluster scale.

## Addendum (2026-09-07) — the two-body/mutual generalization exists,
## but in a different, older literature, and is only checked at
## abstract level here — not a full read

Searched for it directly (arXiv `search_papers` + Semantic Scholar
citation-graph of `1808.05831` itself). Result:

- **None of `1808.05831`'s own 40 citing papers** (checked in full,
  Semantic Scholar) do this — that citation tree is entirely quantum-
  information-flavored follow-on (atomic clocks, decoherence, quantum
  time dilation, Unruh-DeWitt detectors), still single-composite-body-
  in-an-external-field, never extended to mutual N-body.
- **A separate, older, more mature literature already solves the real
  N-body/mutual case**: the **DSX formalism** (Damour, Soffel & Xu,
  1991-1994 — already in `1808.05831`'s own reference list, [40]-[42],
  but not built on there) derives post-Newtonian equations of motion
  for `N` **mutually-interacting, arbitrarily-structured, including
  strongly self-gravitating**, extended bodies, each with its own full
  set of mass and spin multipole moments. Real, verified extensions
  `[VERIFIED-arXiv, abstract-level]`: Damour & Vokrouhlicky (`gr-qc/
  9503041`, 1995, conservation laws); Racine & Flanagan (`gr-qc/
  0404101`, 2004, explicit translational equations of motion, extends
  DSX to strongly self-gravitating bodies); Kopeikin (`1810.11713`,
  2018, and `2006.08029`, 2020, arbitrary mass+spin multipoles, using
  the Blanchet-Damour multipole formalism — the SAME formalism this
  project's own `docs/123` solution-space already cites for `F_oP`);
  Mitchell & Will (`0704.2243`, 2007, binary systems, finite-sized
  bodies, explicitly studies "contributions of the internal structure"
  to the strong equivalence principle at 2PN).
- The relevant classical-GR name for the underlying question is the
  **effacing principle** — whether a body's equations of motion depend
  on its internal structure beyond a handful of multipole moments.
  Kopeikin & Vlasov (`gr-qc/0612017`, 2006) address this directly for
  `N`-body systems.

**Honest limit of this addendum**: only abstracts were read, not the
derivations. It is `[INFERRED, not verified]` — not yet checked — that
these frameworks reach the SAME conclusion Zych–Rudnicki–Pikovski did
(internal energy of any kind, thermal included, contributing through
exactly one channel, no separate long-range term) rather than a
weaker, purely-geometric-multipole-only statement that leaves thermal/
kinetic internal energy's own coupling unaddressed. Confirming that
requires actually reading Racine–Flanagan and/or Kopeikin's derivations
— a real, scoped next step, not attempted here.

## Addendum 2 (2026-09-07) — Racine & Flanagan read IN FULL:
## scope-limit #1 is CLOSED, and the requirement on MULTING is now
## much sharper than "new physics needed"

`[VERIFIED-arXiv: gr-qc/0404101v3 read in full, 256,514/256,514
characters]`. This is the mutual N-body case, done properly: explicit
post-1-Newtonian translational equations of motion for `N`
**mutually-interacting, arbitrarily-structured** bodies, with coupling
to **all** mass and current multipole moments, valid for arbitrarily
strong internal gravity (black holes not excluded).

**Four findings, in ascending order of consequence for MULTING:**

1. **Internal energy is inside the mass multipoles, explicitly.** The
   post-Newtonian mass moment is defined (Eq. 63) as
   `pn_M_L = ∫ {[pn_T⁰⁰ + n_T^jj + ...] x^<L> - ...} d³x`. The
   `n_T^jj` term is the trace of the spatial stress tensor — i.e.
   **pressure and internal kinetic (thermal) energy**. So thermal
   energy enters exactly where Zych–Rudnicki–Pikovski's single-body
   result says it should: inside `M`, at PN order. Same one channel,
   now confirmed in the mutual case.
2. **The equations of motion close on the multipoles and nothing
   else.** Eq. (7a), made explicit in Eq. (198):
   `z̈^A_i = F^A_i[z^B, ż^B, M^B_L, Ṁ^B_L, M̈^B_L, S^B_L, Ṡ^B_L]`.
   No other property of a body's interior appears anywhere. The stated
   organizing idea (§I.2): *"the equations of motion are determined
   entirely by the local field equations in weak field regions between
   the bodies"* — each body is surrounded by a vacuum **buffer
   region**, and everything about it that can reach the others is
   encoded in that region's multipole expansion.
3. **There is no mass dipole at all.** `n_M^A_i = pn_M^A_i = 0`
   identically (Eqs. 82, 87, 150), by the mass-centering gauge that
   defines the centre-of-mass worldline. Mass corrections start at
   `l=2`; the schematic force expansion (Eq. 1) is
   `F ~ (M²/D²){1 + O(M/D) + O(M²/D²) + ... + O[(R/D)^l] + ...}` with
   minimum `l=2` for Newtonian tidal coupling (`l=1/2` post-Newtonian,
   from gravitomagnetic spin-orbit). Truncating to monopoles recovers
   the Lorentz–Droste–Einstein–Infeld–Hoffmann equations.
4. **The decisive one — the theorem does not assume GR inside the
   bodies.** Footnote to Eq. (111), quoted verbatim: *"a different
   theory of gravity could be applicable in the strong field region
   `r<r_-`, with the correction to the field equations being
   incorporated into the definition of `T^μν`. **Our application of the
   conservation law (111) to derive the equation of motion (104b) will
   therefore apply to any theory of gravity for which the vacuum field
   equations coincide with those of general relativity.**"*

**What (4) does to the question this FINDING was asking.** The
requirement on a `k_A`-sourced `F^(1)~k_A r_A/s³` term is no longer
the vague "MULTING needs some new mechanism." It is specific: **such a
term requires modifying the VACUUM field equations in the region
BETWEEN the clusters** — modifying the internal physics of clusters is
provably not enough. If v82's vacuum equations agree with GR's, then
Racine–Flanagan applies verbatim to its own node pairs, and the mutual
force is exhausted by the multipole moments, inside which the thermal
energy already sits as part of `M`. That is a sharp, checkable
condition, and checking it is a question about v82's own construction
rather than about the literature.

**Honest limits of this addendum:**
- Post-1-Newtonian. That is not a problem for the target regime —
  cluster compactness `GM/Rc² ~ 10⁻⁵`-`10⁻⁶` (this project's own
  `FINDING_P172` number) and `v/c ~ 10⁻³` sit comfortably inside PN
  validity — but it does mean nothing here constrains post-2-Newtonian
  and higher terms.
- Requires non-intersecting buffer regions and multipole convergence,
  i.e. `R/D < 1`. For v82's own node pairs (`R` a few Mpc, `D~40-45`
  Mpc) this holds with room to spare, but it is an assumption, not a
  theorem-free statement.
- Says nothing about theories that DO modify the vacuum equations —
  by construction, that is exactly the escape hatch it identifies.
- **NOT CHECKED:** whether v82 in fact modifies its vacuum field
  equations. That is the next step, it is cheap, and it is a question
  about v82's own text — not about this literature. `NO_AUTHOR_ERROR`
  applies throughout: nothing here is a claim that v82 is wrong.

## Pearl Registry / next step

Scope-limit #1 is closed. The single, cheap, well-posed next step is
now: **read v82's own construction to determine whether it modifies
the vacuum field equations between node pairs, or only the physics
inside/at the nodes.** Racine–Flanagan's own universality footnote
makes that binary the whole question — if the vacuum sector is GR,
the `k_A`-sourced separate channel has no room in the mutual dynamics
at post-1-Newtonian order; if it is not GR, the theorem is silent and
the term is unconstrained by any of this.
