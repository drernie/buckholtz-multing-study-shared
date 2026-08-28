# FINDING P150 — Q3a: fifth-force experimental mapping gate — three
# candidate readings, two of three favor MAPPING-UNAVAILABLE for solids

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0
construct-validity (reasoning, not computation — per this project's own
Structure-Bias Guard, this question is answered in prose, then the
consequence is serialized)
**Verdict:** `MAPPING-DEFINITION-DEPENDENT, LEANING UNAVAILABLE` —
corrected from an earlier draft's `MAPPING-AMBIGUOUS` (which implied a
roughly symmetric 1-vs-1 split), per independent skeptic review (§0
below): a third reading was missing, and once included, two of three
internally-coherent readings of MULTING's own `k_A` converge on
`MAPPING-UNAVAILABLE` for solid laboratory test masses; only one allows
`P151` to proceed at all.
**Origin:** `P148`'s corrected order (internal consistency → observable
mapping → external constraint) — this is the second step, run before any
numerical MICROSCOPE/LLR bound is attempted, per the user's own explicit
instruction not to repeat the "similar magnitude ⇒ assumed same
observable" error.

---

## 0. Correction (same day, independent skeptic review) — read this first

The skeptic found the original two-reading framing (A vs. B) was **not
exhaustive** and, worse, subtly biased toward letting `P151` proceed. Four
issues, all fixed below:

1. **A third reading was missing.** Reading C (§2.3, *virial/self-
   gravitating internal kinetic energy* — the kinetic energy of a body's
   own sub-parts insofar as it supports the body against its own
   self-gravity) is at least as physically motivated as Readings A or B
   for a *gravity* theory, and for a solid, EM-bound laboratory test
   mass it gives `k≈0` — the same conclusion as Reading A, via a more
   principled route (not corona-analogy, but "does this energy do
   gravitational work"). Added below.
2. **Arithmetic imprecision.** The original draft's "13 orders of
   magnitude" figure for the cluster-vs-solar `k/M` gap conflated two
   different quantities: `k_cluster/M_cluster ÷ k_Sun/M_☉ ≈ 3×10¹⁰` is
   **~10.5 orders of magnitude**, independently reverified here
   (`log₁₀(10⁻⁶/3×10⁻¹⁷)≈10.5`) — the "13 orders" figure in `docs/118`
   itself refers to the *full dipole-correction ratio* `F_d/F_m`
   (which carries extra `β_d·r_A/D` factors), not the `k/M` ratio alone.
   Corrected throughout.
3. **`docs/118`'s corona choice was characterized uncharitably.**
   `docs/118` line 47 states an explicit (if unproven) principle —
   *"MULTING self-suppresses wherever ICM-like kinetic energy is
   absent"* — treating coronal plasma as the closest solar analog to a
   cluster's ICM. That is a stated physical argument, not an
   unmotivated number-shopping choice. The weak point is the *analogy
   step* (is coronal plasma really the right ICM analog?), not the
   arithmetic. Corrected in §2.1.
4. **Reading B was never applied consistently to the Sun.** If "internal
   kinetic energy" means *total* thermal/binding energy (Reading B), the
   Sun's own value is dominated by its core, not its corona — order
   `GM_☉/(R_☉c²)`, independently computed here as **`≈2.1×10⁻⁶`** — nine
   to ten orders of magnitude *larger* than `docs/118`'s corona-only
   figure, and on the *same order* as `k_cluster/M_cluster~10⁻⁶`. This
   is a real, previously-uncomputed downstream consequence: under
   Reading B applied consistently, the solar-system dipole test would be
   roughly as constraining as the cluster-scale case, not fourteen
   orders of magnitude safer as `docs/118` concluded using Reading A's
   corona value. Added in §2.2.

**Net effect on the verdict:** Readings A and C both give `k≈0` for
solid test masses (`MAPPING-UNAVAILABLE`, via different but each
individually principled arguments); only Reading B gives a nonzero,
computable signal, and Reading B is not obviously *more* defensible than
A or C — it is defensible *only if* one presupposes "the reading must
generalize to solids," which is precisely what is in dispute. Verdict
rebalanced from a symmetric "ambiguous" to a leaning one.

---

## 1. The seven sub-questions, answered from this project's own record

### Q1 — What is the fifth-force charge of ordinary matter?

MULTING's own preprint, checked directly against the primary source
(`data/source_material/buckholtz_preprints...v6.md` line 640, quoted
verbatim in `docs/124`): *"`k_A` denotes the internal kinetic energy of
object-A"* — a general-sounding definition. But the preprint's own
**worked instantiation** is exclusively for *"protoclusters/galaxy
clusters specifically, IGM thermal energy"* (`docs/124`'s own
characterization of the primary source's usage, not a direct Buckholtz
quote) — i.e., the hot intracluster/intergalactic medium's thermal
energy. This project's own independent, earlier audit (`docs/29`,
`docs/30`, `docs/34`, dating to before the P1/two-charge work) already
flagged this exact gap:

> `docs/30_multing_solar_system_limit_questions.md`: *"3. k_A definition |
> No values or formula for ordinary matter | Cannot compute dipole
> contribution"* — sent as an author question (`docs/26`), status left
> `UNKNOWN — author clarification required`. (`docs/30` line 58 does note
> the manuscript names a *concept* — "sub-object kinetic energy" — just
> no formula for non-cluster bodies.)

**No formula for `k_A` applied to ordinary (non-cluster) matter exists in
MULTING's own preprint, per this project's own already-completed source
check.**

### Q2 — Do Ti, Pt, Earth, Moon have a nonzero analog of `k_ir_i`?

Depends on which of three readings is used — see §2. Readings A and C:
`NO` for solid test masses (no corona; no self-gravitational virial
role). Reading B: `YES`, trivially, for any body at nonzero temperature.

### Q3 — Is `pᵢ/mᵢ` universal, or composition-dependent?

Where nonzero at all (Reading B only), severely composition-dependent.
Under A/C, the question doesn't arise for solids (`k≈0`).

### Q4–Q6 — Force scaling, mediator range, screening

Already established elsewhere in this project's own chain, not
re-derived here: `1/r³` dipole force (`docs/125`), mediator effectively
massless at every scale up to and including cluster separations
(`P149`, deviation `~10⁻⁷`% at cluster scale) — meaning at
laboratory/solar-system scales (`r≪` cluster scale), the mediator is
*even more* exactly massless, no screening, genuine long-range `1/r³`
force *if* `k_ir_i≠0` for the bodies involved.

### Q7 — Is Earth's source charge the same object as cluster `kᵢrᵢ`?

Only under Reading B — under Readings A or C, Earth's own solid,
EM-bound structure gives it no defined (or effectively zero) charge, so
the question does not arise the same way it does for a self-gravitating
gas cloud.

## 2. Three readings — two converge on `k≈0` for solids

### 2.1 — Reading A: "identifiable hot/energetic sub-component,
### analogous to ICM" (this project's own prior choice for a non-
### cluster body)

`docs/118_journal_readiness_section_draft.md` (2026-06-17,
`DRAFT_FOR_TJB_REVIEW`, `NOT_VALIDATION`, `OUR_RECONSTRUCTION` — this
project's own speculative extension, **not** TJB-confirmed) proposed,
for the Sun specifically:

```
k_Sun ≡ E_corona/c² ≈ 3×10⁻¹⁷ M_☉
```

— stating an explicit principle (`docs/118` line 47): *"MULTING
self-suppresses wherever ICM-like kinetic energy is absent"* — treating
the Sun's hot, magnetically-confined coronal plasma as the closest solar
analog to a cluster's hot ICM. This gives `k_Sun/M_☉ ≈ 3×10⁻¹⁷`,
contrasted in the same document against `k_cluster/M_cluster ~ 10⁻⁶` —
a **`~10.5`-orders-of-magnitude** difference (independently reverified
here; `docs/118`'s own "13 orders" figure is for the *dipole-force
ratio* `F_d/F_m`, a different, larger quantity carrying extra `β_d·r_A/D`
factors, not this `k/M` ratio alone).

**Under this reading, Q2's answer is `NO` for Ti/Pt (and for Earth/Moon
treated as solid, non-stellar bodies):** solids have no corona-type hot
outer plasma layer. `MAPPING UNAVAILABLE` under this reading.

**This reading's genuine weak point** is the analogy step itself — is
coronal plasma really the right solar analog to a cluster's ICM, as
opposed to (say) the Sun's much larger core thermal reservoir? — not the
arithmetic, and not an accusation of number-shopping (corrected per §0
point 3).

### 2.2 — Reading B: literal total internal thermal/vibrational energy
### (not previously used in this project, worked out here)

Take "internal kinetic energy of object A" at face value: the total
kinetic energy of A's own constituent particles' motion relative to A's
center of mass. For a solid, this is ordinary bulk thermal energy,
`E_thermal ≈ (3/2)N k_B T`; for a self-gravitating body, applied
*consistently* this should instead be dominated by its total internal
(largely gravitational-virial) energy budget, **not** an arbitrarily
chosen sub-component:

```
k_i/(m_i c²) ≈ (3/2) k_B T / (m_atom,i c²)          [solid, thermal]
k_Sun/M_☉    ≈ G M_☉/(R_☉ c²) ≈ 2.1×10⁻⁶            [self-gravitating, consistent]
```

**For solids**, this generalizes to any body at any temperature and is
directly computable and manifestly composition-dependent through
`m_atom`: titanium (`m_atom≈48` amu) vs. platinum (`m_atom≈195` amu) —
the two MICROSCOPE test-mass materials, chosen by that experiment
specifically for their different composition — differ in `k_i/m_i` by
roughly the inverse atomic-mass ratio, **~4×** (`8.7×10⁻¹³` vs.
`2.1×10⁻¹³`, independently computed here from `k_BT` at 300 K and each
atomic mass), before accounting for each material's own heat capacity
and Debye-temperature corrections (which shift the ratio to `~3.7×`,
still "~4×" to the precision claimed).

**For the Sun**, applying this same "total internal energy" reading
*consistently* (rather than `docs/118`'s corona-only sub-component) gives
`k_Sun/M_☉ ≈ GM_☉/(R_☉c²) ≈ 2.1×10⁻⁶` — **on the same order as
`k_cluster/M_cluster`**, not fourteen orders of magnitude smaller. This
is a real consequence `docs/118` never computed (it used Reading A's
corona value, not B's consistent total): under Reading B, the
solar-system dipole test would be roughly as constraining as the
cluster-scale case, not automatically safe.

**Under Reading B, Q2's answer is `YES` for any ordinary body**, and
Q3's composition-dependence is real and MICROSCOPE-scale relevant for
solids — but this is only *one* of the channels composition enters
MICROSCOPE-type tests through (baryon fraction, isospin, nuclear
binding per nucleon, etc. are others; this reading adds one more
channel, not a uniquely-targeted one).

### 2.3 — Reading C (added per skeptic review): virial/self-gravitating
### internal kinetic energy

"Internal kinetic energy of object A" = the kinetic energy of A's own
sub-parts *insofar as it participates in A's own self-gravitating
dynamics* — the kinetic support against the object's own self-gravity.

- **Cluster:** ICM thermal pressure + galaxy peculiar-velocity
  dispersion support the cluster against its own self-gravity;
  `k/M ~ σ²/c² ~ 10⁻⁶` for `σ~1000` km/s — numerically coincides with
  Readings A and B at cluster scale, because for a virialized system the
  thermal/kinetic support **is** the self-gravitational virial energy;
  the three readings only diverge for non-self-gravitating bodies.
- **Sun:** same order as Reading B applied consistently,
  `~GM_☉/(R_☉c²)~2×10⁻⁶` (virial thermal energy of a self-gravitating
  star, core-dominated).
- **Solid Ti/Pt test mass:** **`k≈0`.** A 100 g laboratory test mass is
  bound by electromagnetic (interatomic) forces, not by its own
  self-gravity — its self-gravitational binding energy is utterly
  negligible, and the atoms' thermal vibration is not "paying against"
  any self-gravitational collapse the way ICM pressure or stellar core
  pressure does. There is no self-gravitating-virial kinetic energy for
  a solid to have. `MAPPING UNAVAILABLE` under this reading too — via a
  structurally different, arguably more principled argument than
  Reading A's corona analogy (this asks "does this energy do
  gravitational work for the body," not "is there a hot sub-component
  by loose analogy").

**Why Reading C is not obviously less defensible than B for a *gravity*
theory:** if `k_A`'s role is to source a *gravitational* dipole force,
tying it to energy that participates in the body's own gravitational
dynamics (Reading C) is at least as natural a generalization as tying it
to *any* internal kinetic energy regardless of whether it has anything
to do with gravity (Reading B) — arguably more natural, since it is the
reading under which the cluster/Sun instantiations and the mechanism's
own physical role (a *gravitational* effect) stay conceptually unified.

## 3. Why this project's own record already shows the tension, not
## just infers it

`docs/118` (Reading A) and the literal preprint phrase (Reading B/C's
shared textual basis) sit in the same project's own record without ever
being reconciled — `docs/118` never states why coronal energy
specifically, rather than the Sun's total energy budget (Reading B) or
its virial-supporting energy specifically (Reading C, numerically
identical to B for a self-gravitating star), is the right instantiation.
This is not a new tension introduced here; it is a pre-existing one,
surfaced by asking the construct-validity question directly.

## 4. Verdict

**`MAPPING-DEFINITION-DEPENDENT, LEANING UNAVAILABLE`** — corrected
framing (§0):

- MULTING's own preprint supplies no formula for `k_A` applied to
  ordinary matter (`docs/29/30/34`, author question sent, unanswered).
- **Two of three** internally-coherent readings (A: ICM-analogy;
  C: virial/self-gravitating) converge on `k≈0` for solid laboratory
  test masses — `MAPPING-UNAVAILABLE` — via structurally different but
  each individually principled arguments, not merely restated versions
  of each other.
- **One** reading (B: literal total internal energy) generalizes to
  solids and gives a real, computable, composition-dependent signal —
  `MAPPING-VALID` — but is only more defensible than A/C if one
  presupposes the very question in dispute (that the reading must
  generalize to solids at all), and applying it *consistently* (not just
  to solids) also raises the solar-system dipole constraint by ~10
  orders of magnitude relative to what `docs/118` reported, a
  consequence this project's own record never previously computed.
- **No reading is licensed by MULTING's own text as *the* intended
  one** — all three are this project's own reconstruction attempts.

## 5. What this means for P151 (Q3b)

`P151` is attemptable **only** under Reading B, and **only** with that
scope stated explicitly and prominently on every number it produces —
not as "MULTING predicts a fifth-force bound," but as "under the one of
three defensible readings that allows any laboratory-scale signal to
exist at all, the resulting composition-dependent signal compares to
MICROSCOPE thus." Given §0 point 4's own consequence (Reading B applied
consistently raises the solar-system-scale prediction to
`~k_cluster/M_cluster`, not `docs/118`'s tiny corona value), `P151`
should check the solar-system-scale (Cassini-type) constraint under
Reading B too, not only the MICROSCOPE/composition-dependent channel —
`docs/118`'s own Cassini-safety conclusion does not survive under
Reading B and needs independent re-evaluation, not reuse.

## What this file does NOT establish

1. **Not a claim about MULTING's own intended definition** (Gate 1) —
   MULTING's own text does not specify one for ordinary matter; all
   three readings here are this project's own reconstruction attempts.
2. **Does not compute any numerical bound** — that is `P151`'s job, and
   only under Reading B, explicitly labeled, including the now-flagged
   solar-system-scale re-check.
3. **Does not resolve which reading is "correct"** — this file documents
   a genuine, structured disagreement among defensible readings rather
   than resolving it by fiat; it does report that 2 of 3 lean one way.
4. **The `~4×` Ti/Pt figure (Reading B) is an order-of-magnitude
   estimate**, not a precision calculation — real heat capacities and
   vibrational spectra of the actual MICROSCOPE test-mass alloys were
   not looked up or used; if `P151` proceeds, this should be refined.
