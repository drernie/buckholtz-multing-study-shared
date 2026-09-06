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

## Pearl Registry / next step

The two-body/mutual generalization this FINDING originally flagged as
unexamined **does exist** (DSX/Racine-Flanagan/Kopeikin/effacing-
principle line, above) — the open step is now narrower: read at least
one of these derivations (Racine & Flanagan, `gr-qc/0404101`, is the
most directly relevant — explicit equations of motion, extends DSX to
strongly self-gravitating bodies) to confirm whether THERMAL/KINETIC
internal energy specifically (not just geometric shape multipoles)
gets the same single-channel treatment there, closing this FINDING's
own scope-limit #1.
