# Frozen claims C1–C4 — criteria fixed BEFORE certification

**Date frozen:** 2026-08-03, before any Path B run
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

Every criterion below is written before the independent runs. A verdict reached
by adjusting these afterwards is not a certification.

**Prior-work check performed** (the step skipped last time):
`null_results/INDEX.md` NR-001 … NR-018 and `parked/INDEX.md` NW-001 read in
full. No prior entry covers provenance, transcription, the virial identity, or
the amplitude bound. NR-016 covers a *different* bridge mapping and is cited in
NR-018. **NR-015 is the governing precedent for procedure**: its own first-draft
label was retired by skeptic review, and it reclassified three neighbouring
entries' framing as overclaim. NR-018 is presently in that same position.

---

## C1 — provenance of Table A1

> **Claim.** The material available to us does not contain a deterministic,
> published, reproducible operator `F ↦ H` that produced Table A1. The table is
> presented in the source as the response of an online AI service to a prompt.

**Scope.** Table A1 only. Figure 3 is a separate object and is **not** covered —
see the note below.

**Assumptions.** The PDF text layer faithfully represents the published PDF.

| verdict | condition, fixed in advance |
|---|---|
| **PASS** | an independent reader, given only the source pages and no output of ours, states that the table is an AI service's response, and finds no separate published calculation |
| **FAIL** | the reader locates a published equation, algorithm or table-generation rule in the source that yields the H-MULT column |
| **UNRESOLVED** | the reader cannot determine the provenance either way from the pages supplied |

**What this claim does NOT assert**, even on PASS:

- Not that no operator existed. The service applied *some* procedure; we
  observe only that it is not published, not identifiable from the table, and
  not shown to follow from the force law.
- Not that the author misrepresented anything. He labels the table accurately.
- Not that MULTING is wrong, unsupported, or untestable.
- Not anything about Figure 3, whose provenance is a separate question with its
  own evidence.

---

## C2 — transcription fidelity

> **Claim.** `data/table_a1_reported.csv` contained four erroneous fields out of
> 108, all in row 1, and the corrected `table_a1_source_verified.csv` matches the
> source.

**Scope.** The twelve rows × nine numeric fields of Table A1.

| verdict | condition |
|---|---|
| **PASS** | an independent extraction reproduces exactly the same 4 discrepancies and the same 104 matches |
| **FAIL** | the independent extraction finds a different set of discrepancies |
| **UNRESOLVED** | the text layer is ambiguous at a field the two extractions disagree on |

**What this does NOT assert.** Nothing about whether the *source* numbers are
correct — only about whether our copy of them is faithful.

---

## C3 — the virial identity `w = n/3`

> **Claim.** Under the mapping
> `ρ = (1/2V) Σ U`, `p = −(1/6V) Σ s dU/ds`,
> a pair potential `U(s) = C·s^(−n)` gives `p = (n/3)ρ`, hence `w = n/3`,
> independent of `ξ`, of the amplitude, and of any cutoff.

**Scope.** The stated mapping only. The identity is a property of that mapping
applied to a pure inverse power, not a statement about cosmology.

| verdict | condition |
|---|---|
| **PASS** | an independent analyst, given only the two definitions and the potential form and **not told the expected answer or its sign**, derives `w = n/3` |
| **FAIL** | the analyst derives a different exponent or sign |
| **UNRESOLVED** | the analyst reports the mapping as ill-posed without a stated averaging volume or background subtraction |

**What this claim does NOT assert** — the correction that matters most:

- **Not** that no inverse-power pair potential can produce `ρ + 3p < 0`. If
  `ρ < 0` — which is the case for the attractive monopole, whose binding energy
  is negative — then `ρ + 3p = (1+n)ρ < 0` identically. Such a component *does*
  satisfy the acceleration inequality while **reducing** `H²`; it is not a
  positive-density dark-energy component. The correct statement is:
  **a positive-density effective-fluid mapping of a pure inverse-power pair
  potential cannot give a dark-energy equation of state.**
- Not that the generalised Layzer–Irvine formalism is closed. The formalism is
  a valid energy balance; what is closed is one mapping built on top of it.
- Not that other averaging prescriptions (comoving separation, non-power-law
  potentials, anisotropic stress) obey the same identity.

---

## C4 — amplitude bound

> **Claim.** With published or observationally admissible coefficients, the
> pair-interaction energy density of a cluster population is `Ω_pair ≲ 10⁻⁴`,
> far below what a cosmologically relevant component requires.

**Scope.** Cluster-scale pair interactions under the stated population model.
This is the one claim of the four whose value is **model-dependent by
construction**.

| verdict | condition |
|---|---|
| **VERIFIED** | an independent implementation reproduces the order of magnitude, **and** the sign and order are stable across the full sensitivity envelope below |
| **CONDITIONAL** | reproduced at the central choice, but the envelope moves it by more than one order |
| **FAIL** | the independent implementation differs in sign, or by more than two orders at the central choice |

**Sensitivity envelope, fixed in advance.** The claim is `VERIFIED` only if the
verdict is unchanged across every cell:

```
ξ(r) form        : power law · power law + exponential cutoff · measured ξ_hh
correlation r0   : 15 Mpc · 25 Mpc
mass function    : fixed mass · Press–Schechter · Tinker
s_min            : 0.5 · 1 · 2 Mpc
s_max            : 100 · 200 · 500 Mpc
coordinates      : physical · comoving
units            : dual run
```

**What this does NOT assert.**

- **Not** that the amplitude result is cutoff-independent. `w = n/3` is; the
  amplitude is not. The `n = 2` and `n = 3` integrals diverge at small
  separation, so their value is set by `s_min`. Any statement of the form
  "independent of ξ, cutoff and amplitude" applies to C3 alone.
- Not that pair energy can never matter cosmologically in any model — only that
  it does not, at these coefficients, for this population.
- Not a likelihood, and not an observational limit. It is a forward estimate.

---

## Cross-cutting: what none of C1–C4 establishes

- **The local force law is NOT ADJUDICATED.** Nothing in C1–C4 tests
  `F = −A₂/r² + A₃/r³ − A₄/r⁴` as a description of cluster interactions.
- **Covariant MULTING+ is OPEN.** An action whose stress-energy sources the
  background, with the force law as a non-relativistic limit, is untouched by
  any of these four.
- **kSZ constrains, it does not settle.** The kSZ analysis tests pair velocities
  and the local force directly. It does not determine the operator carrying the
  force to `H(z)`, but any bridge relating the same force law to structure
  growth must remain consistent with it.
- **Backreaction is not adjudicated.** Buchert's `Q_D` is built from
  `⟨θ²⟩ − ⟨θ⟩²` and `⟨σ²⟩`, not from pair potential energy. The amplitude of the
  force poses a challenge to it; C1–C4 do not close it.

---

## Independence requirements for Path B

Binding. A run violating any of these does not count as certification.

| requirement | applies to |
|---|---|
| no import of any Path A function or module | C4 |
| a different order of operations, not a re-run | C4 |
| the reader is not told the expected answer or its sign | C3 |
| the reader is not told that "AI" is the suspected provenance | C1 |
| the reader does not see our CSV or our diff | C2 |
| all four run before any is consolidated | all |

A second execution of the same code is a re-run, not a reproduction — the
distinction this project already records under `CROSS-IMPLEMENTATION REPLICATION`
versus `INDEPENDENTLY REPRODUCED`.
