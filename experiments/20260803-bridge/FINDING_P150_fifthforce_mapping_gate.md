# FINDING P150 — Q3a: fifth-force experimental mapping gate — no single,
# non-arbitrary mapping exists; two candidate readings diverge sharply

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0
construct-validity (reasoning, not computation — per this project's own
Structure-Bias Guard, this question is answered in prose, then the
consequence is serialized)
**Verdict:** `MAPPING-AMBIGUOUS` — two internally-coherent readings of
MULTING's own `k_A` definition give qualitatively different answers to
whether it applies to laboratory/solar-system test bodies at all, and
this project's own prior work already used BOTH readings inconsistently
without resolving which is intended.
**Origin:** `P148`'s corrected order (internal consistency → observable
mapping → external constraint) — this is the second step, run before any
numerical MICROSCOPE/LLR bound is attempted, per the user's own explicit
instruction not to repeat the "similar magnitude ⇒ assumed same
observable" error.

---

## 1. The seven sub-questions, answered from this project's own record

### Q1 — What is the fifth-force charge of ordinary matter?

MULTING's own preprint, checked directly against the primary source
(`data/source_material/buckholtz_preprints...v6.md` line 640, quoted
verbatim in `docs/124`): *"`k_A` denotes the internal kinetic energy of
object-A"* — a general-sounding definition. But the preprint's own
**worked instantiation** is exclusively for *"protoclusters/galaxy
clusters specifically, IGM thermal energy"* (`docs/124`) — i.e., the hot
intracluster/intergalactic medium's thermal energy. This project's own
independent, earlier audit (`docs/29`, `docs/30`, `docs/34`, dating to
before the P1/two-charge work) already flagged this exact gap:

> `docs/30_multing_solar_system_limit_questions.md`: *"3. k_A definition |
> No values or formula for ordinary matter | Cannot compute dipole
> contribution"* — sent as an author question (`docs/26`), status left
> `UNKNOWN — author clarification required`.

**No formula for `k_A` applied to ordinary (non-cluster) matter exists in
MULTING's own preprint, per this project's own already-completed source
check.**

### Q2 — Do Ti, Pt, Earth, Moon have a nonzero analog of `k_ir_i`?

Depends entirely on which reading of "internal kinetic energy" is used —
see §2 below. Under the most literal reading (total internal
thermal/vibrational kinetic energy of a body's own constituents), *yes*,
trivially — any body at nonzero temperature has some. Under the reading
this project's own prior work actually used for a non-cluster body (§2,
`docs/118`'s "solar corona" choice), *no* — solids have no analog of a
stellar corona, so the mechanism simply does not apply to Ti/Pt at all.

### Q3 — Is `pᵢ/mᵢ` universal, or composition-dependent?

Composition-dependent, and *severely* so, under **both** readings
checked (§2) — this is the one sub-question with a clean, convergent
answer regardless of which reading is used.

### Q4–Q6 — Force scaling, mediator range, screening

Already established elsewhere in this project's own chain, not
re-derived here: `1/r³` dipole force (`docs/125`), mediator effectively
massless at every scale up to and including cluster separations
(`P149`, deviation `~10⁻⁷`% at cluster scale) — meaning at
laboratory/solar-system scales (`r≪` cluster scale), the mediator is
*even more* exactly massless, no screening, genuine long-range `1/r³`
force if `k_ir_i≠0` for the bodies involved.

### Q7 — Is Earth's source charge the same object as cluster `kᵢrᵢ`?

Only under the literal reading (§2.2) — under the corona-type reading
(§2.1), Earth (no corona in the relevant sense) has no defined charge at
all, so the question does not arise.

## 2. Two readings, both internally coherent, giving opposite answers

### 2.1 — Reading A: "identifiable hot/energetic sub-component"
### (this project's own prior choice for a non-cluster body)

`docs/118_journal_readiness_section_draft.md` (2026-06-17,
`DRAFT_FOR_TJB_REVIEW`, `NOT_VALIDATION`, `OUR_RECONSTRUCTION` — this
project's own speculative extension, **not** TJB-confirmed) proposed, for
the Sun specifically:

```
k_Sun ≡ E_corona/c² ≈ 3×10⁻¹⁷ M_☉
```

— using the Sun's hot, magnetically-confined coronal plasma as the
"internal kinetic energy" analog, by loose analogy to a cluster's hot
ICM. This gives `k_Sun/M_☉ ≈ 3×10⁻¹⁷`, contrasted in the same document
against `k_cluster/M_cluster ~ 10⁻⁶` — **a 13-orders-of-magnitude
difference between the cluster and solar values**, already computed by
this project's own prior work, independent of anything derived here.

**Under this reading, Q2's answer is `NO` for Ti/Pt (and arguably for
Earth/Moon treated as solid, non-stellar bodies):** solids have no
corona-type hot outer plasma layer. The mechanism this project's own
prior work actually used to extend `k_A` beyond clusters simply does not
generalize to laboratory test masses or (in any obvious way) to
Earth/Moon. `MAPPING UNAVAILABLE` under this reading.

**A flaw in this reading worth naming:** choosing *corona* energy
specifically — not the Sun's total internal kinetic/thermal energy,
which is dominated by the much hotter, far more massive core — is
itself unmotivated within `docs/118` (it is not derived from anything in
MULTING's own text; it reads as chosen because it gives a
comfortably-small, sub-Cassini-bound number, not because it is the
principled generalization of "internal kinetic energy"). This is an
internal weakness in this project's own earlier attempt, not a
MULTING-attributable claim (`NO_AUTHOR_ERROR`).

### 2.2 — Reading B: literal total internal thermal/vibrational energy
### (not previously used in this project, worked out here)

Take "internal kinetic energy of object A" at face value: the total
kinetic energy of A's own constituent particles' motion relative to A's
center of mass — i.e., ordinary bulk thermal energy, `E_thermal ≈
(3/2)N k_B T` for `N` constituent particles at temperature `T`. This
**does** generalize to any body at any temperature, including solid
laboratory test masses:

```
k_i/(m_i c²) ≈ (3/2) k_B T / (m_atom,i c²)
```

For a room-temperature (`T≈300`K) test mass, this is directly
computable and manifestly **composition-dependent through `m_atom`**:
titanium (`m_atom≈48` amu) vs. platinum (`m_atom≈195` amu) — the two
MICROSCOPE test-mass materials, chosen by that experiment specifically
*for* their different composition — differ in `k_i/m_i` by roughly the
inverse mass ratio, **~4×**, from atomic mass alone, before even
accounting for each material's own heat capacity and vibrational-mode
structure (which would shift this further). **Under this reading, Q2's
answer is `YES` for any ordinary body, and Q3's composition-dependence is
not just present but of a magnitude MICROSCOPE-type experiments are
specifically designed to probe.**

## 3. Why this project's own record already shows the ambiguity, not
## just infers it

`docs/118` (reading A) and the literal preprint quote *"internal kinetic
energy of object-A"* (reading B's own textual basis) sit in the same
project's own record without ever being reconciled — `docs/118` never
states why coronal energy, specifically, is the correct instantiation of
"internal kinetic energy" rather than total thermal energy, and no later
document in this project revisits the choice. This is not a new tension
introduced here; it is a pre-existing one, surfaced by asking the
construct-validity question directly rather than reusing whichever
reading a given document happened to need.

## 4. Verdict

**`MAPPING-AMBIGUOUS`**, not a clean `MAPPING-VALID` or
`MAPPING-UNAVAILABLE` — the honest record, per the user's own explicit
instruction to report an ambiguous result honestly rather than force a
binary:

- MULTING's own preprint supplies no formula for `k_A` applied to
  ordinary matter (`docs/29/30/34`, author question sent, unanswered).
- This project's own one prior attempt to extend it (`docs/118`, reading
  A) does not generalize to laboratory test masses at all — under that
  specific reading, `Q3a → MAPPING-UNAVAILABLE`.
- A more literal, arguably more defensible reading (B, worked out here
  for the first time) **does** generalize, and gives a real,
  computable, and MICROSCOPE-relevant composition-dependent signal —
  under that reading, `Q3a → MAPPING-VALID`, and `P151` (Q3b) becomes
  attemptable.
- **Neither reading is licensed by MULTING's own text as *the* intended
  one** — reading B is this project's own construction, offered here as
  the more defensible option, not as a TJB-confirmed definition.

## 5. What this means for P151 (Q3b)

`P151` is attemptable **only** under Reading B, and **only** with that
scope stated explicitly and prominently — not as "MULTING predicts a
fifth-force bound," but as "under this project's own reconstruction
choice B for extending `k_A` beyond clusters, the resulting
composition-dependent signal compares to MICROSCOPE thus." If `P151`
proceeds, it must carry Reading B's label on every number it produces,
per this project's own `NO_AUTHOR_ERROR` discipline — a bound derived
under an unconfirmed reconstruction choice is a bound on *this
project's own candidate*, not on MULTING.

## What this file does NOT establish

1. **Not a claim about MULTING's own intended definition** (Gate 1) —
   MULTING's own text does not specify one for ordinary matter; both
   readings here are this project's own reconstruction attempts.
2. **Does not compute any numerical bound** — that is `P151`'s job, and
   only under Reading B, explicitly labeled.
3. **Does not resolve which reading (A or B) is "more correct"** — both
   are internally coherent extrapolations of an underspecified textual
   definition; this file documents the ambiguity rather than resolving
   it by fiat.
4. **The `~4×` Ti/Pt figure (Reading B) is an order-of-magnitude
   estimate**, not a precision calculation — real heat capacities and
   vibrational spectra of the actual MICROSCOPE test-mass alloys were
   not looked up or used; if `P151` proceeds, this should be refined,
   not reused as-is.
