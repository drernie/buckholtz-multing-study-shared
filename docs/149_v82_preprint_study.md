# docs/149 — v82 preprint study: TJB's current work supplies exactly the
# reopen condition `docs/147` named for bottleneck 1

**Date:** 2026-08-30
**Origin:** TJB's 2026-08-29 reply to Sergey's 2026-08-27 progress-report
email flagged (a) a wording imprecision ("ordinary matter-dominated,"
resolved same day, see `lessons_learned.md`) and (b) uncertainty about
which of his own preprint versions the letter's remarks addressed — he
pointed to his current work, `...v82` (Zenodo record 22004287). Sergey
supplied both the PDF and the Zenodo zip (identical file); this document
records a full read of the primary source (pp. 1–33 of 40, the entire
theoretical/methodological body — Sections I–V and Acknowledgments; the
remaining pages are bibliography, not re-read here).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (a provenance/content study, not a
falsification-ladder experiment)
**Source, read directly from the PDF (page images), not the markdown
conversion, for anything equation-level** — see `data/source_material/
README.md`'s own fidelity caveat for why. Prose content is grep-able in
`data/source_material/buckholtz_202608.0943v1.v82.md`.

## 0. What this document is and is not

This is a **content study**, not a promoted falsification-ladder finding.
It records what v82 says, compares it structurally to v6 (the version this
project's entire reconstruction — `docs/124`–`127`, `two_charge_
completion.py`, `two_field_action_closure.py`, `P1`–`P155` — is built on),
and flags what it means for this project's own tracked bottlenecks
(`docs/147`). It does **not** re-derive, re-verify, or promote/reject any
of v82's own claims — that is future work, if and when undertaken, and
would need its own Zero-Signal Gate, estimand, and controls per this
project's standing methodology, not be smuggled in here as a side effect
of reading the paper.

## 1. Identity — two different documents, not two versions of one

**Artifact Identity (Gate 1) check, run explicitly, not assumed:**

| | v6 (this project's basis) | v82 (TJB's current work) |
|---|---|---|
| Title | "Gravitational and Dark-Matter Concepts that Can Help Explain and Predict Cosmic Data" | "Multi-Tier Newtonian Gravity: A Cosmic-Node-Based Alternative to LCDM for the Hubble Tension" |
| Identifier | Preprints.org 10.20944/preprints202511.0598.v6 | Preprints.org 202608.0943v1; Zenodo record 22004287 |
| Posted | 21 May 2026 | August 2026 |
| Local file | `data/source_material/buckholtz_preprints202511.0598.v6.pdf` | `data/source_material/buckholtz_202608.0943v1.v82.pdf` |
| Submission history (per TJB's 2026-08-29 email) | — | Rejected by MDPI *Universe*; Springer's *Foundations of Physics* mentioned as a possible next venue |

These are **different papers with different titles**, not two version
numbers of the same manuscript — "v82" in the filename is Preprints.org's
own revision-count suffix for the *newer* paper, not a v6→v82 lineage of
the *same* one. Whether/how the two share underlying physics (they
plainly do — both build a multipole two-body force law from node mass and
ICM thermal energy) versus how much genuinely changed between them is
exactly what §2 below works through.

## 2. Section-by-section structure of v82's core methodology (Sec. II)

| Subsection | Content | Relation to this project's own work |
|---|---|---|
| **II.A** Force formulation | Eqs. (1)–(4): `F_P = F⁽⁰⁾ − F⁽¹⁾ + F⁽²⁾`, monopole `F⁽⁰⁾=−Gm_Am_P/s²`, dipole `F⁽¹⁾=β₁(−Gk_Ac⁻²m_Pr_A/s³)+β₁(−Gm_Ak_Pc⁻²r_P/s³)`, quadrupole `F⁽²⁾=β₂(−Gk_Ak_Pc⁻⁴r_Ar_P/s⁴)` | **This is structurally our `F_oP`.** Same monopole/dipole/quadrupole tier structure, same `(m_i,k_i,r_i)` charge ingredients. **Confirms TJB's own guess** ("the remarks below... relate at least to Section II.A") — our sent letter's F_oP bilinear-factorization and alternating-sign-rule claims address exactly this section. |
| **II.B** Kinematic effects formulation | Eqs. (5)–(7): Newton's second law for time-varying mass (node accretion), general momentum-conserving form, reduced-mass two-node equation `μ_reduced·s̈ = F_P + [accretion correction]` | **Genuinely new to this project.** Our sent letter never addresses this — our own cosmological-background work used the Shtanov–Sahni generalized-cosmic-energy-equation route (`docs/124`–`127`), a *different* framework from TJB's own accretion-kinematics one. |
| **II.C** Kinematic translation protocol | Eq. (8): `ä/a = s̈(z)/s(z)`; Eq. (9): `dz/dt=−(1+z)H(z)`; integrated to `H(z)²−H₀²` | **This is an explicit F→H(z) bridge**, TJB's own — see §3 below for why this matters for `docs/147`'s bottleneck 1. |
| **II.D** Empirical scaling laws | Eq. (10) `m_X(z)=m₀(1+z)^(−1.1)` (theoretical power law); Eq. (11) `r_X(z)` via `R₅₀₀`/`ρ_crit(z)` (**TJB's own "Class III circular" flag** — assumes the Friedmann equation to build an input feeding a force law meant to independently predict `H(z)`); Eqs. (12)–(14) `k_X(z)` via a 3-step mass→temperature→gas-mass→thermal-energy chain, grounded in real X-ray scaling relations | **This is the `m_A(z)`/`r_A(z)`/`k_A(z)` cluster-property schedule `docs/54`'s own Blocker 2 flagged as missing/unspecified** in this project's earlier work on v6. |
| **II.E** Non-isotropic mass accretion | `f_merge=0.25`, `v_infall(z)=√(Gm_X(z)/r_X(z))`, `f_coh` (coherence fraction, bounded not derived), `F_acc(z)` accretion-correction force | Additional physics not present in this project's own reconstruction at all. |
| **II.F** Empirical grounding, 3-class provenance | TJB's own **Class I (data-proximate) / Class II (retained-theoretical) / Class III (circular)** classification of every input | Methodologically close in spirit to this project's own `artifact-provenance-gates.md` — an independently-arrived-at parallel discipline, not something this project taught him or vice versa. |
| **II.G** Computational details | 3 free parameters: `β₁`, `β₂`, `H₀,anchor`; Nelder-Mead χ² fit against 33 points (31 Cosmic Chronometer + SH0ES + DESI) | `β₁≈1.4×10¹⁰`, `β₂≈7.7×10¹⁷` (Table II, best-fit row) — **dimensional, large-magnitude values**, structurally different from this project's own dimensionless `β_d=2, β_q=√6` (`P1`/`docs/125`). These are not obviously the same fitted quantities under a unit change; not checked here. |

## 3. Why this matters for `docs/147`'s bottleneck 1

`docs/147`'s own text for bottleneck 1 (`F→H_MULT(z)`) states it is
**BLOCKED, not derived**, and gives the explicit reopen condition:
*"не появилось новой информации, разрешающей direct derivation reopening
(k_A(z)/r_A(z)/D_cAB(z) от TJB, **или новая публикация**)"* — no new
information enabling direct-derivation reopening (`k_A(z)/r_A(z)/D_cAB(z)`
from TJB, **or a new publication**).

**v82 is precisely that reopen condition, on both of its own named
branches simultaneously:**
- It is **a new publication** from TJB.
- It supplies explicit **`k_A(z)`, `r_A(z)`, `m_A(z)`** evolution laws
  (Sec. II.D) — the exact missing cluster-schedule `docs/54`'s Blocker 2
  named — with an honest three-class provenance audit of each.
- It supplies an **explicit F→H(z) derivation** (Sec. II.B–II.C) — via a
  *different* mechanism (accretion-corrected two-body kinematics) than
  this project's own Shtanov–Sahni route, not a confirmation or
  contradiction of `docs/127`'s own `G_eff=0` result, which addresses a
  structurally different question (does the pair-kernel correction
  survive an `r→∞`/isotropic-population background limit) than TJB's own
  bridge (does a *specific pair's* kinematics, integrated, reproduce the
  observed `H(z)` curve).

**This document does not itself reopen bottleneck 1** — that is a
decision for the project's own gate process (`gate-check`), informed by
this study, not a side effect of reading a paper. What this document
establishes is narrower and unambiguous: **the specific, named condition
`docs/147` set for reopening bottleneck 1 has now been met, as a plain
factual matter — a decision about what to do with that is still open.**

## 4. Cross-checks against this project's own prior findings

Several items in v82 independently corroborate or bear on findings this
project reached from v6 alone, before this session had ever seen v82:

1. **Table IV** (Sec. IV.D) lists MULTING's own "Empirical scope" as
   *"Dark-energy-free"* against ΛCDM's *"Dark-energy-dependent."* This
   directly matches this project's own `FINDING_P85_internal_time_to_
   redshift.md` conclusion ("matter-dominated, **no dark energy**") —
   reached independently, from v6, via a completely different method
   (direct numerical integration of a covariant two-field action) than
   TJB's own accretion-kinematics route in v82. Two independent methods,
   two different source-preprint versions, same qualitative conclusion.
2. **Sec. IV.F** ("Bases for gravitationally dipole effects") gives the
   electromagnetism/magnetic-moment analogy for why thermal energy (not
   bulk kinetic motion) sources the dipole term, and explicitly resolves
   the "an isotropic quantity sourcing a dipole-like force" tension by
   noting the axis comes from *outside* the thermal energy itself (the
   line connecting the two nodes) — this matches the already-established
   project memory finding (`docs/123`, "магнитный момент analogy, строки
   467-470") and the mirror-symmetric/externally-supplied-axis convention
   this project's own `two_charge_completion.py`/`P1` construction
   already uses.
3. **Table III / Sec. IV.K**: force-term decomposition shows `F⁽¹⁾`
   (dipole, ≈+53%) and `F⁽²⁾` (quadrupole, ≈−46.5%) nearly cancel, net
   `4–6%` — confirms and extends what `docs/144` had already found from a
   partial read of this same document (focused on the SH0ES-fit question,
   not Sec. II specifically).
4. **Sec. IV.H** ("Circumstances where this framework should not be
   expected to be accurate") is TJB's own, highly candid limitations
   catalogue — multi-body superposition not validated ("we do not
   currently know how much this simplification costs"), non-monopole
   internal mass distribution, non-monopole bulk kinematics, internal
   mergers, **"typical objects, not distributions"** (every quantity in
   Sec. II.D is a single representative value per redshift, not a
   population average — a genuinely different question from, but
   adjacent to, this project's own isotropic-*orientation*-population
   averaging work in `P154`/`P155`), a formal Newtonian high-velocity
   boundary, and a hard, self-reported extrapolation failure (`H²` goes
   negative beyond `z≈17.5`).
5. **Sec. IV.U** — TJB states plainly that the paper was produced through
   "sustained, iterative collaboration" with AI systems, including an
   independent AI-regeneration verification pass on the archived results,
   and discloses two real gaps that pass caught (missing force-law
   formulas in one regeneration draft, a stale ingredient-growth-factor
   figure). A parallel methodological posture to this project's own
   stack, arrived at independently.

## 5. What this document does NOT establish

1. **Not a claim about whether v82's own results are correct** — no
   equation was re-derived, no fit was re-run, no control was checked.
   This is a content/provenance study, not a falsification-ladder
   experiment (`NO_AUTHOR_ERROR` applies in full).
2. **Does not establish that `β₁`/`β₂` map onto this project's own
   `β_d`/`β_q` (or `A`/`g`/`κ`)** under any specific unit convention — the
   two parametrizations look structurally different (dimensional/large
   vs. dimensionless/`O(1)`) and this was not checked.
3. **Does not itself reopen bottleneck 1** — see §3's own scope note.
4. **Does not resolve whether v82's own `G_eff`-type background behavior
   agrees or disagrees with `docs/127`'s S–S result** — these are
   different bridge mechanisms (TJB's accretion-kinematics vs. this
   project's population-averaged pair-kernel), not yet compared.
5. **Markdown-conversion equations are not to be trusted at face value**
   — see `data/source_material/README.md`'s fidelity caveat; every
   equation cited above was read from the PDF page images directly.
6. **Pages 34–40 (bibliography) were not re-read** — no claim is made
   about their content.
