# docs/138 — TJB Optional Technical Modules (AMBER tier)

**Date:** 2026-07-24
**Origin:** see docs/137's Origin note — same harvest-and-triage lineage.
**Purpose:** internal menu, not drafted for sending. Each module needs its own short technical
memo (not a one-liner) before it could go out to Dr. Buckholtz — the caveats below are the
minimum required content of that memo, not decoration. Sergey decides which modules, if any, are
worth developing further. Same evidence scale and labels as docs/137.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

## Module A — Identifiable reparametrization for the β1/β2 degeneracy

**Corrected claim (was overstated in dossier v1):** the Case1/Case2 ridge (identical χ²=13.565 at
β pairs ~5× apart) is **structurally analogous** to a degeneracy we found in our own R011
pipeline (quadrupole-saturation: as one coupling term dominates, the fit becomes invariant to the
other). It is **not proven to be the same mechanism** — that would require an explicit mapping
(β1,β2)_v25 ↔ (η_d,η_q)_R011 showing both ridges arise from the same reduced combination, which we
have not done.
**Status:** `SAME PHENOMENON — NOT PROVED` / `ANALOGOUS IDENTIFIABILITY FAILURE — SUPPORTED`.
**If pursued:** offer to attempt the explicit mapping first, before proposing crossover-z +
amplitude as a fix — the reparametrization suggestion is currently a guess at the right fix, not
a derived one.

## Module B — Real cluster X-ray/SZ cross-check of k_X(z)

**Claim:** we hold 443–548 real MCXC/PSZ2 clusters with ICM thermal energy computed two
independent ways (X-ray M_gas+T_X; SZ Compton-Y). This is a real, usable dataset that could test
your Eqs. 12–14 self-similar scaling and the T0 tension you already flag (3.3–3.6 keV implied vs.
~7 keV from independent mass-temperature relations).
**Caveat:** we have not yet run this cross-check — this module is an offer to do the work, not a
result. Framing it as already informative would be premature.

## Module C — Background-invisibility result, correctly scoped

**Corrected claim (was overstated in dossier v1):** under **one specific closure** we chose
(Shtanov-Sahni-style background closure, our own mapping choice), the multipole terms vanish from
ä/a to machine precision. This is an **our-completion result**, not a statement about MULTING as
a theory, and not a statement about your v25 kinematic construction, which is a different,
author-specified bridge and is untouched by it.
**Status:** `OUR-COMPLETION RESULT — NOT AN AUTHOR-THEORY RESULT`. Explicitly does not contradict
your v25 finding that the fitted curve DOES carry E(z) shape information (a different construction
was used in each case — no tension once separated).

## Module D — Growth branch (fσ8/S8) map

**Corrected claim (was overstated in dossier v1):** the bell-shaped ε(z)/fσ8 pattern and the
intrinsic-vs-induced-polarization branch split are a **hypothesis map**, not a recommendation for
the paper's growth section. Nothing here is a MULTING prediction until an author-specified
response law (the η parameter, or equivalent) fixes which branch applies.
**If useful:** offered as background for Sec. IV P, explicitly labeled speculative until Q006
(Lagrangian/action) or an equivalent response law is specified.

## Module E — Blanchet dipolar-DM literature note

**Corrected claim (was overstated in dossier v1):** this is a **literature-awareness note**, not
a constraint on MULTING. It applies only if MULTING's dipole is shown to map onto Blanchet's
gravitationally-polarizable dipole field — a mapping (of fields, initial conditions, and the
observable itself) that has not been demonstrated. Presenting it as an existing bound on MULTING
would be premature.
**If useful:** flag as "if your 2nd-order dipole construction turns out to resemble this class of
model, these two constraints (Planck non-gaussianity bound, exponential instability timescale)
are worth checking against" — conditional, not asserted.

## Module F — Eq.32 / 7:9:17 look-elsewhere framing, corrected

**Corrected claim (was overstated in dossier v1):** "rank 1 of 83,160" and "P_random≈1/624" are
**rank/probability within a specific, recorded search grid** (149 rational prefactors × 24
exponents × 3 lepton pairs for Eq.32; integer pairs to n=50 for 7:9:17), not global p-values. A
defensible global p-value requires the grid to have been defined before the coincidence was
observed, or an argument for why the grid's boundaries are natural rather than chosen after the
fact. We can state exactly how and when each grid was constructed (available on request) but
have not independently audited whether the grid definition itself is free of hindsight bias.
**Suggested wording, if used:** "rank 1 within a predefined 5,640-combination grid of rational
prefactors and integer exponents (Eq.32) / the unique integer pair up to n=50 at a 2% threshold
(7:9:17) — offered as a quantified sensitivity result, not a claim about the probability the
relation is a coincidence in an absolute sense."
**Additional nuance the dossier compressed away:** a broadened-search-space check (larger grids,
up to ~841k combinations) was separately run on Eq.32 and found some rank degradation (#1 in the
narrower/baseline space, #3–#5 in the broadest tested space) — worth citing alongside the
headline rank, not instead of it, so the sensitivity to grid choice is visible rather than hidden.

## Module G — N_opt reinterpretation, with the model switch made explicit

**Corrected claim (was overstated in dossier v1):** N_opt=5.366 (5.79σ from integer 5, Planck) is
one measurement. The claim "consistent with 5 isomers at 0.46σ via mean mass ratio 1.074" is a
**different model** (5 unequal-mass sectors, not 5 equal-density copies) fitted to reproduce the
same number — not automatically implied by the first result.
**Suggested wording, if used:** "N=5 exactly is excluded at 5.79σ. A model with five sectors of
slightly unequal mass (mean ratio ≈1.074 to baryon mass) reproduces N_opt=5.366 — a distinct,
model-dependent reading, not a direct consequence of the equal-copies postulate."

---

**Reminder for whoever picks this file up next:** none of the above are ready to paste into a
message. Each needs the caveat paragraph included, not dropped for brevity — the caveat is the
part that keeps the item honest.
