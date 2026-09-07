# P214 — RETRACTION after Step 8a. Four of five claims FALSIFIED.
# The `k` question is **not** answered, and the ambiguity is **internal**,
# not a version conflation.

**Date:** 2026-09-07
**Supersedes:** `FINDING_P214_k_is_defined_in_v82_the_fork_was_version_conflation.md`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Every skeptic finding below was independently re-read from the source
files by me before acceptance** (`audit-verification-gate.md`: its
`[VERIFIED]` = my `[INFERRED]`). Line numbers are mine, re-checked.

---

## 0. Verdict table

| claim | verdict | why |
|---|---|---|
| **P1** "v82 defines `k` explicitly as ICM thermal energy; **not ambiguous within v82**" | **WEAKENED** — first half stands, second half **FALSIFIED** |
| **P2** "the broad reading is v6's; the author narrowed between versions" | **FALSIFIED** |
| **P3** "§5's open question was a v6/v82 conflation" | **FALSIFIED** |
| **P4** "the periastron bound does not reach v82" | **FALSIFIED** |
| **P5** "this is a loss of testable content" | **FALSIFIED** as unconditional |

---

## 1. P1 — half stands `[VERIFIED-source]`

**Stands:** v82 line 207 *is* a definition. It sits inside the continuous
symbol-definition paragraph for Eqs. (1)–(4), in order: `s` → `G` → `m_A`
→ `m_P` → `r_A` → `r_P` → **`k_A` (207)** → `k_P` (210) → `β₁` (213) →
`β₂` (218). Not a caption, not a footnote. The table artifacts are
dropped subscripts.

**FALSIFIED:** *"It is not ambiguous within v82."* v82 states the scope of
the **same equations** at two different levels:

| line | scope | text |
|---|---|---|
| **188** | **node** | *"MULTING suggests that Eqs. (1) through (4) pertain for gravitational effects of a **node-A** on a **node-P**."* |
| **1354-1355** | **object** | *"We suggest than MULTING, **including Eq. (1)**, associates with a source (**such as** object-A) and with a probe (such as object-P)…"* |
| **1449-1452** | **object** | *"MULTING (**including Eqs. (1) through (4)**) suggests that one needs to consider at least one property, the energy of motion of nonzero-mass sub-objects… for each one of an **object-A**… and an **object-P**…"* |

Plus v82:999-1000 keeps the class open: *"some non-mass properties,
**such as** thermal kinetic energy, of a node might couple significantly
to another node's mass."* **"Such as" is an example, not an exhaustion.**

## 2. P2 — FALSIFIED in both directions `[VERIFIED-source]`

The claim rested on an asymmetry. Both halves fail.

**v6 already has the thermal specialization** — v6:671-675, verbatim:

> *"**For protoclusters and galaxy clusters**, the notion that `k_A`
> associates only with the rotation of a uniform ring of mass does not
> pertain. **Typical ratios of total thermal energies** of sub-objects to
> total kinetic energies of bulk linear motions of gas and galaxies are
> generally large [80–82]."*

**v82 already has the broad phrasing** — 1354-1355, 1386-1387, 1449-1452
above.

**So the two-level structure (general definition + cluster-thermal
specialization) is present in BOTH versions.** What actually changed
between them is *operationalization* — Eq. (14), the X-ray calibration,
`IGM` → `ICM`, and which level occupies the symbol-definition line — not
the definition's breadth.

## 3. The enumeration in `MODEL_SPEC_AUDIT` §5 matches **neither** document

§5's broad reading was *"binding, rotational, degeneracy"*. Checked:

- **binding — excluded by BOTH.** v6:601-602: *"Modeling does not need to
  consider potential energies that, within objects, **bind sub-objects
  into objects** or that affect the motions of sub-objects."*
  v82:1381-1383: *"…de-emphasize… structural aspects or **potential
  energies within objects**. (…MULTING emphasizes rest energies and
  kinetic energies.)"*
- **rotational — excluded by v6's own definition.** v6:640: *"`k_A`
  denotes the internal kinetic energy of object-A. (…the total of the
  energies of **linear motion**, relative to the center-of-mass…)"*
  Linear, not rotational.
- **degeneracy — addressed nowhere in either.**

So the fork §5 posed was mis-enumerated from the start, in a third way
neither P214 nor §5 noticed.

## 4. P4 — FALSIFIED, and the reading was backwards `[VERIFIED-source]`

P214 argued: a neutron star has no ICM ⇒ `k` undefined ⇒ the pulsar bound
does not apply.

**v82 says the opposite in two places.**

- **1354-1355** claims Eq. (1) — the full force law including the
  `k`-dependent terms — at the **object** level, with node as *"such as"*.
- **1386-1387** *invites* exactly this application: *"MULTING opens
  possibilities to model directly trajectories for gravitationally
  influenced objects… for which **internal energies that associate with
  the motions of sub-objects are significant**."* A neutron star is that
  case.

And v82's own exclusion (1453-1456) is about **collisions and mergers** —
*"MULTING does not (yet) adequately discuss **overlapping objects or
colliding objects**"* — with ref [125] a NS-**merger** paper. **A binary
pulsar on a stable eccentric orbit is neither overlapping nor colliding.**
It is precisely the spatially-separated, point-like case MULTING claims
as its domain. P214 read that sentence as excluding compact objects; it
excludes collisions.

`NEEDS-REAL-DATA` sub-item, correctly raised: the periastron calculation's
own source was not re-read, so *which* energy it substituted for `u_NS`
(binding vs degenerate-kinetic) is unverified here. Binding is excluded by
both documents; degenerate **kinetic** energy is not.

**[2026-09-07] ANSWERED — `FINDING_P215_periastron_survives_on_degenerate_energy.md`.** The finding used *binding* (`f=0.105`) and *rotational* (`P=22.7 ms`); degeneracy was named in its conclusion and never computed. It has been: `β_d < 2.2e-5 – 3.0e-5`, i.e. the bound **survives** on the one internal energy the corpus admits, 5.2–5.3 orders below Table A1's fitted 4.5. Both original rows reproduced as positive controls.

## 5. P5 — FALSIFIED as unconditional `[VERIFIED-source]`

v82 **adds** testable content around `k`, it does not remove it:
the explicit `m→T→M_gas→k` chain (Eqs. 12–14, executable in
`multing_core.py:79-91`); a data-proximate class with a **named boundary**
`0.05<z<1.07` and the admission that 6 of 31 CC points already lie beyond
it; a separate fit restricted to the data-grounded subset; the unresolved
`T₀` tension (*"There is no single T_0 that simultaneously satisfies"*);
and explicit failure points (`H(z)` turnaround at `z≈10.6`, `H²<0` beyond
`z≈17.5`).

## 6. My own methodological error, recorded

The zero-hit greps that P214 leaned on were run **singular-only**:

```
internalenergy    : 0     <- what I searched
internalenergies  : 1     <- what the file contains
```

The single hit is v82:1386 — **the very line I had quoted as an example of
word-gluing while reporting its concept as absent.** I checked for glued
words and did not check for plurals. A space-insensitive search is not a
morphology-insensitive one.

## 7. What SURVIVES — and it is stronger than P214 was

### 7.1 A real, citable internal scope inconsistency in published v82

**[2026-09-07] Now recorded on its own as `FINDING_P216_v82_internal_scope_inconsistency.md`** — including a third scope asymmetry found afterwards (`β₁` per-node vs `β₂` per-pair, v82:213-218).

`v82:188` (node) against `v82:1354-1355` and `v82:1449-1452` (object), for
the **same Eqs. (1)–(4)**. This needs no version comparison and no
inference. It is the honest form of what P214 was reaching for.

### 7.2 The genuine version change is in **β**, not `k` `[VERIFIED-source]`

**[2026-09-07] Now recorded on its own as `FINDING_P217_beta_universality_axis_swapped_between_versions.md`, which CORRECTS the word "narrowing" used below.** Re-reading both sources showed the universality claim was not narrowed along one axis but **moved to a different axis**: v6 constrains `β` across *time* and is silent on object-class; v82 constrains it across *nodes* and is silent on time (v82 has no `β` time-invariance statement at all — `[VERIFIED-grep]`). Neither statement implies the other. The sentence below is kept verbatim, not edited, per no-silent-correction.

| | universality claim |
|---|---|
| **v6:680-681** | *"β_d and β_q are nonnegative numbers **that do not vary significantly with time**."* — a *time* constraint, no object-class restriction |
| **v82:215-216** | *"β₁ is a positive number that we suggest might be approximately **independent of the choice of a specific node**."* — a *node-class* constraint |

**That is a real narrowing between versions, and it lands on exactly the
parameter the pulsar bound constrains.** The defensible restatement of
P214's intent:

> *v82 narrowed the claimed universality of `β₁` from objects generally to
> nodes, so an external bound on `β` derived from compact objects needs
> re-justification against v82's own scope statement — which v82 itself
> gives inconsistently (§7.1).*

That version is **not** contradicted by either file.

## 8. Actions taken

- `MODEL_SPEC_AUDIT` §5's correction banner from P214 is **itself
  withdrawn** — the question is NOT answered, though §5's enumeration of
  the broad reading is separately wrong (§3 above).
- `P3_k_definition_question_DRAFT_HELD.md`'s `SUPERSEDED` header is
  **withdrawn** — the question stands, and if anything is sharper: v82's
  own scope statements disagree.
- All four "consequences" claimed by P214 are **withdrawn**: §5 is not
  answered; `P213`'s fork does not resolve; MICROSCOPE's status is
  unchanged; the periastron bound is not excluded.

## 9. Skeptic's own scope limits, stated

Its Bash was unavailable — findings were line-anchored reads, not shell
output. It read v82 lines 1–1829 with gaps at 736–930 and past 1829, and
v6 selectively. Unread regions could add counterexamples but cannot
remove the ones found, since every verdict rests on a positive citation.
I re-read every load-bearing line myself.
