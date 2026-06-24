# Related Work — C9 (Eq.32) Novelty Assessment

**Date:** 2026-06-23
**Atom:** C9 = `(4/3)(m_τ/m_e)^12 = α_EM/α_G` (0.17σ; look-elsewhere 1/5040; Sabine PROMISING)
**Method:** `/lit-search` — 3 targeted queries, 81 papers retrieved, 13 OA PDFs indexed (TF-IDF RAG).
**Goal:** is the specific relation novel, and how to position it in the paper (pre-empt "naive numerology").

---

## Corpus (persisted, not discarded)

| Query | Source file | Papers | Focus |
|---|---|---|---|
| Q1 `"large numbers hypothesis" lepton mass EM gravitational coupling` | `q1_dirac_large_numbers.json` | 37 | Dirac-LNH lineage |
| Q2 `Koide formula lepton mass relation gravitational constant` | `q2_koide_gravity.json` | 29 | nearest empirical relations |
| Q3 `mass ratio coincidence alpha_EM alpha_G fundamental constants` | `q3_mass_ratio_coincidence.json` | 15 | novelty of Eq.32 itself |

PDFs: `literature/papers/` (13 OA). Index: `literature/sci_index`.

---

## Novelty verdict

**The CATEGORY is not novel; the SPECIFIC relation appears novel.** `[INFERRED]`

1. **Established lineage (C9 is NOT a new idea-class):** empirical lepton-mass relations tied to
   fundamental constants are a recognized published subfield — the Koide formula and its
   gauge-theoretic derivations, plus Dirac Large Numbers Hypothesis and fundamental-constants reviews.
2. **Specific form NOT found:** `(4/3)(m_τ/m_e)^12 = α_EM/α_G` did **not** appear in any of the 81
   papers across 3 queries; the RAG probe for its exact form scored **0.0073** (essentially nothing).
   → C9's specific relation is **not in the indexed literature**. `[INFERRED-ABSENT]`
   **Caveat:** indexed literature only (OpenAlex/S2/arXiv, 2018+ weighted), 3 queries — NOT exhaustive.
   Before any published novelty claim: add Google Scholar manual pass + 1 query round on
   "lepton mass gravitational fine structure constant relation".

---

## Closest prior art (cite these — positions C9, blunts the numerology charge)

| Paper | Year | DOI | Why relevant to C9 |
|---|---|---|---|
| **Sumino, Family Gauge Symmetry as Origin of Koide's Mass Formula** | 2008 | 10.1088/1126-6708/2009/05/075 | The model that *derives* a lepton-mass relation — the standard C9 should aspire to (mechanism) |
| Koide-like relations for running masses | 2006 | 10.1016/j.physletb.2006.02.051 | scheme/energy-scale dependence of such relations — relevant to C9's PDG-mass sensitivity |
| Energy-scale independence of Koide's relation | 2006 | 10.1103/PhysRevD.73.013009 | argues a mass relation is RG-stable — a property C9 has NOT yet been checked for |
| **Why Do Elementary Particles Have Such Strange Mass Ratios? (Quantum Gravity)** | 2022 | 10.3390/physics4030063 | **closest conceptual neighbor** — mass ratios ↔ gravity (403-blocked, abstract only) |
| Koide Lepton Mass Formula and Geometry of Circles | 2012 | — | a *geometric* reading of a mass relation — parallels the (failed) S³ angle, NR-009 |
| A geometrical meaning to the electron mass (Lorentz breakdown) | 2005 | — | geometric origin of m_e — the honest precedent for "geometry → mass" attempts |
| Uzan, Fundamental constants (Living Reviews) | 2025 | 10.1007/s41114-025-00059-y | authoritative review framing α_EM/α_G as a fundamental ratio (Dirac-N context) |

---

## How to position C9 in the paper (concrete)

1. **Frame within the Koide/Dirac-LNH lineage, not as a standalone marvel.** Open the C9 paragraph
   with: "In the tradition of empirical lepton-mass relations (Koide; Sumino) and large-number
   coincidences (Dirac), we note that ...". This pre-empts the "naive numerology" reviewer reflex.
2. **State explicitly what is novel:** C9 relates the *τ/e ratio* to the *EM-to-gravity coupling*
   α_EM/α_G — distinct from Koide (a Q=2/3 sum rule over e,μ,τ) and from Dirac's cosmological N.
3. **Be honest it is empirical (mechanism open).** Cite Sumino (2008) as the example of what a
   *derived* relation looks like, and state C9 has no such derivation yet (G3). Do NOT claim S³
   origin — that route is falsified (NR-009).
4. **RG-stability is an untested gap:** the Koide energy-scale papers (2006) raise the question
   "does C9 hold for running masses?" — flag as future work, since C9 used pole masses (PDG).

### refs.bib keys to add
- `sumino2008koide` (10.1088/1126-6708/2009/05/075)
- `koide2006running` (10.1016/j.physletb.2006.02.051)
- `koide2006rgindependence` (10.1103/PhysRevD.73.013009)
- `strangemassratios2022` (10.3390/physics4030063)
- `uzan2025constants` (10.1007/s41114-025-00059-y)
- `dirac1937` (already planned — Large Numbers Hypothesis)

---

## Manual web pass — 2026-06-24 (closes the open novelty debt)

Two independent search channels now both return the specific relation as absent:
1. **OA index** (81 papers, 3 queries): RAG probe on exact form scored 0.007.
2. **Open web / Scholar-style search** for `(4/3)(m_tau/m_e)^12 = alpha_EM/alpha_G`:
   no hit for the Buckholtz relation. Adjacent results only (fine-structure-constant
   formulas; Koide; lepton mass-hierarchy Lagrangians, e.g. arXiv:1903.12081;
   tauon-mass predictions arXiv:hep-ph/0509043). `[VERIFIED-WEB-ABSENT]` across two channels
   (still not exhaustive: paywalled venues + books not fully covered).

**Singh 2022 obtained** (was HTTP 403 on MDPI; open at arXiv:2209.03205): it derives the
mass ratios of quarks and charged leptons from an octonionic non-commutative pre-spacetime
Lagrangian unifying the SM with SU(2)_R chiral gravity, and explains the Koide value 2/3 and
its departure via left--right symmetry breaking. It is the closest *mechanism-providing*
neighbor --- the kind of derivation C9 lacks. Cite as the contrast: others attempt to derive
mass ratios from deeper structure (Singh, octonions); we present C9 as empirical pending such
a mechanism. Novelty verdict therefore stands: category established, specific relation novel.

## Caveats / honesty

- Novelty now `[VERIFIED-WEB-ABSENT]` across OA index + open web (was `[INFERRED-ABSENT]`); still
  not a proof of absence (paywalled/book literature not exhaustively covered).
- This corpus is persisted (`literature/`) --- re-runnable, not search-and-discard.

*Companion: C9 is PROMISING (Sabine); S³ mechanism REJECTED (NR-009); proof harness = verify_all_claims.py.*
