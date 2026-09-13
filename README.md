# Buckholtz IDM/MULTING Study

![python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)
![license](https://img.shields.io/badge/license-MIT-green)

<sub>**Status, re-measured 2026-09-11 on this tree** (the previous line here read "908 tests … mypy clean (0 errors, blocking in CI)" and was wrong on both counts — corrected rather than quietly refreshed): `pytest --co` collects **991 tests across 67 files**; a 68th file, `tests/test_e15_jensen_gap_real_scatter.py`, **does not collect from a clean clone** — it imports the author's supplemental code, which `data/source_material/*` deliberately git-ignores (fetch from [Zenodo](https://zenodo.org/records/22004287) to run it). `mypy src` → clean, 39 files, **locally**. `ruff check .` → clean. **The CI badge above is red**, and has been since 2026-09-08: CI fails at the `mypy` step, so the test job never runs — an unresolved discrepancy between CI and local, not a known source defect. Treat the badge as live truth and this line as a dated local measurement.</sub>

<sub>**Program phase, 2026-09-13: `WAITING + CONSOLIDATION`, not active discovery.** The research campaign reached its own stop-rule end-state — all four `docs/147` bottlenecks are `CLOSED/BOUNDED`, `STOPPED/UNRESOLVED`, `DISSOLVED`+`EXHAUSTED`, or `SEARCH-CAMPAIGN-EXHAUSTED` (never "solved," see [`PROGRAM_CLOSEOUT_LEDGER.md`](PROGRAM_CLOSEOUT_LEDGER.md) for the precise, non-interchangeable vocabulary). No new physics computation is planned absent one of five explicit "new input" triggers (a new dataset, an external definition, a new publication, a found logical conflict, or a genuinely new differentiating test — never "we could still compute something"). Three external replies are pending (none received as of this date); the methodology paper is `CORRECTED, NOT RE-REVIEWED` and not yet submitted anywhere.</sub>

---

## START HERE if you are reviewing this as a physicist

**The framing, first, because the internal vocabulary is blunter than the intent.**
This repository's own working language — `null_results/`, "failure-mode taxonomy",
"adversarial", `docs/119` ("what critics could raise") — is the machinery of a
falsification-discipline applied by the author of *this repository* to *his own
reconstruction* of MULTING. Every finding carries the label `NO_AUTHOR_ERROR`:
it is a statement about this reconstruction, never a claim that Dr. Buckholtz
erred. Where a result runs against the framework, it is reported plainly; where
it runs for it, likewise. Nothing here is an audit *of him*.

**Fifteen-minute path:**

1. [`PROGRAM_CLOSEOUT_LEDGER.md`](PROGRAM_CLOSEOUT_LEDGER.md) — the
   fastest orientation: a 1-2 page, claim-by-claim index (13 major
   claims, each with evidence IDs, status, strongest support, strongest
   counterevidence, and its own explicit reopen condition), frozen as a
   2026-09-13 baseline, plus the program's current governance mode
   (`WAITING + CONSOLIDATION` — see the status line above).
2. [`CURRENT_EVIDENCE_STATE.md`](CURRENT_EVIDENCE_STATE.md) — the full
   detail behind the Ledger: what is reproduced, what is refuted or
   weakened, the open bottlenecks, and an explicit list of what cannot
   be claimed publicly. (`PROJECT_STATUS.md` further down is an
   older, explicitly-superseded snapshot kept for history only.)
3. [`docs/151_status_separation_rule.md`](docs/151_status_separation_rule.md) —
   the rule every verdict here obeys: empirical status, ontological
   interpretation, and causal claim are three separate fields, never collapsed.
4. [`null_results/INDEX.md`](null_results/INDEX.md) — 21 registered dead ends.
   These are the point, not an embarrassment: the register exists so a killed
   direction cannot quietly return.

**If you came with two specific questions, these are the two files:**

| Question | File |
|---|---|
| Is there a falsifiable prediction? | [`PREREGISTRATION_v82_prospective_tests.md`](PREREGISTRATION_v82_prospective_tests.md) — three predictions frozen 2026-09-07 with PASS/FAIL thresholds, each graded for discriminating power by its own author (two of three: *weak*) |
| Best-fit vs best-fit, not against published values? | [`FINDING_P166`](experiments/20260803-bridge/FINDING_P166_aic_bic_from_v82_own_table_ii.md) — AIC/BIC on the preprint's *own* two re-fitted ΛCDM benchmarks; and [`FINDING_E8`](experiments/20260906-evidence-authority/FINDING_E8_full_covariance_propagation.md) — every defensible `\|Δχ²\|` lands in `[−1.27, +2.64]`, i.e. the 33-point dataset does not discriminate in either direction |

**Source material is not redistributed here.** `data/source_material/` is
git-ignored: the preprints and the author's supplemental code live on
[Zenodo](https://zenodo.org/records/22004287) and
[preprints.org](https://doi.org/10.20944/preprints202608.0943.v1), and must be
fetched from there to re-run everything. That is why one test file does not
collect from a clean clone.

---

**Personal study notes and reproducibility scaffolding for understanding Thomas J. Buckholtz's IDM/MULTING framework.**

**⚠️ IMPORTANT DISCLAIMERS:**
- This project does **NOT** validate, refute, or officially audit the IDM/MULTING theory
- This is a **personal learning exercise** in epistemic auditing and source verification
- All interpretations and analyses are my own and may contain errors
- This work is **not endorsed** by Dr. Buckholtz or any institution
- The goal is **transparency and learning**, not criticism or validation

> **What this actually reproduces:** an **AI-service-mediated computation** (Table A1
> and its fitted beta parameters from ChatGPT / Claude / Gemini), **not** Buckholtz's
> physical theory — the H_MULT(z) formula is under-specified in the source. The candidate
> beta values {4.25, 0.78, 8.10, 0.19} are **AI-service outputs, not model versions**.
> Full framing: [`docs/WHAT_THIS_REPRODUCES.md`](docs/WHAT_THIS_REPRODUCES.md).

---

## What This Repository Does

It provides a small reproducibility and epistemic-audit layer for selected definitions, equations, parameters, and claims from Thomas J. Buckholtz's work on Isomeric Dark Matter (IDM) and MULTING (multipole tiers) cosmology.

---

## The Source

This repository audits the numerical claims in:

> Thomas J. Buckholtz, *"Gravitational and Dark-Matter Concepts that Can Help Explain and Predict Cosmic Data,"* Preprints.org (2026).
> [DOI: 10.20944/preprints202511.0598.v6](https://doi.org/10.20944/preprints202511.0598.v6) · mirrored on [ResearchGate](https://doi.org/10.13140/RG.2.2.34270.19523)

Read the preprint first — this repo assumes familiarity with its notation (Table A1, β_d, β_q, IDM isomers, MULTING multipole terms).

## About Dr. Thomas J. Buckholtz

Dr. Thomas J. Buckholtz is an independent researcher affiliated with the [Ronin Institute for Independent Scholarship](https://ronininstitute.org/) (Montclair, NJ) and the National Coalition of Independent Scholars (Brattleboro, VT). His recent work proposes Isomeric Dark Matter (IDM) and MULTING (multipole gravity), a framework in which most elementary particles have six "isomers," five of which associate with dark matter — see the preprint linked above for the full framework.

This repository is an **independent, non-affiliated audit** of that work's numerical claims. It does not represent Dr. Buckholtz's own code, endorsement, or conclusions — see the disclaimers throughout this README.

---

## Key Numerical Results (2026-06-17) — NOT_VALIDATION · OUR_RECONSTRUCTION

| Test | Result | Script |
|------|--------|--------|
| Eq.32 fermion-gravity link | **1.00σ** (0.0608%) from PDG 2024/2025 | `code/eq32_verify.py` |
| IDM N=5 vs Planck 2018 ω_DM/ω_b | **5.8σ excluded** | `code/chi2_idm.py` |
| β_d=4.5 dipole at cluster scale | **ε ≈ 6×10⁻⁶** (negligible) | `code/beta_rescaling.py` |
| MULTING H(z) ΔAIC vs ΛCDM | **+2.5** (ΛCDM preferred) | `data/pearson_r_test_results.md` |
| Pearson r MULTING/H_CC | **0.62** (MCXC n=443), **0.70** (XMM n=22) | ibid |

Strong Inference summary: H4 (empirical mass relations) ✅ · H3 (IDM as CDM) ❌ · H1 (full replacement) ⚠ conf=0.12

---

## Goals

1. **Audit beta_d and beta_q definitions** — clarify values, units, normalizations
2. **Reproduce selected numerical relations** — verify arithmetic (e.g., Eq.15)
3. **Classify claims** — separate derived / fitted / assumed / unknown
4. **Detect numerology** — penalize arbitrary formulas without mechanisms
5. **Prevent data leakage** — ensure beta formulas don't circularly use H0, Omega_m
6. **Prepare respectful technical brief** — document what's clear and what requires clarification

---

## Non-goals

- ❌ No full cosmological simulation (no serious H(z) solver)
- ❌ No claim that IDM/MULTING is **true**
- ❌ No claim that ΛCDM is **false**
- ❌ No unsupported physics derivations
- ❌ No use of AI-generated supplementary values as verified data

**Guiding principle:**  
> Do not implement physics that is not clearly defined. First build the epistemic registry.

---

## Quick Start

```bash
# Clone or download repository
cd buckholtz-multing-study-shared

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_eq15_constants.py -v
```

---

## Project Structure

```
buckholtz-idm-multing-mvp/
├── src/              # 38 core modules — epistemic registry, beta provenance, bridge candidates, force-law records
├── tests/            # 68 test files (991 collected; 1 file needs the non-redistributed source material) — invariants, controls, dimensional checks, reverse-engineering
├── code/             # standalone verified scripts — eq32_verify, chi2_idm, beta_cv, beta_rescaling
├── scripts/          # 54 pipeline/report scripts — recompute_n4_aic, jeans_nfw_multing, build_report_ru
├── audit/            # self-consistency diagnostics
├── data/             # PDG/CODATA constants + real catalogs (MCXC, XMM T_X) + Moresco+2022 CC H(z)
│                     #   ⚠ author preprint PDF & supplementary CSVs are gitignored (local-only)
├── docs/             # 96 documents — see docs/INDEX.md for the full map
├── paper/            # LaTeX manuscript skeleton (main.tex, refs.bib)
├── reports/          # 21 machine-readable result JSONs
├── notebooks/        # 3 exploration notebooks
├── null_results/     # falsified-hypothesis records (FL protocol)
└── pearl_registry/   # tool-verified side-insights (FL protocol)
```

> Full per-document navigation: **[`docs/INDEX.md`](docs/INDEX.md)**. Key source modules:
> `epistemic_registry.py`, `beta_provenance.py` (single source of truth for β), `constants.py`
> (fundamental constants only — no cosmological fits), `rosetta.py` (terminology mapping).

---

## Status Labels (Epistemic Taxonomy)

Every claim, parameter, and equation is marked with one of these statuses:

| Status | Meaning | Example |
|--------|---------|---------|
| **fact** | Verified measurement/observation | Electron mass from PDG |
| **calculation** | Reproduced numerical result | Eq.15 numerical reproduction |
| **hypothesis** | Proposed but not yet tested | 6 isomers structure |
| **inference** | Logical conclusion from verified facts | Ratio derived from masses |
| **assumption** | Chosen premise without derivation | 5 dark / 1 ordinary split |
| **fitted** | Phenomenological fit to data | Beta values from H(z) fit |
| **derived** | Mathematically derived from other claims | Formula consequence |
| **unknown** | Status not determined | Missing information |
| **unclear** | Conflicting or ambiguous information | Multiple beta values |
| **requires_source_verification** | Source needed or source unclear | Equation mentioned but not sourced |

---

## Test Suite

*The full suite is **68 test files, 991 tests collected** (measured 2026-09-11). One file,
`tests/test_e15_jensen_gap_real_scatter.py`, will not collect until the author's supplemental code is
fetched from Zenodo; run `pytest --ignore=tests/test_e15_jensen_gap_real_scatter.py` without it. The six below
are representative of the core invariants, not the complete list; see `tests/` for all.*

### Core Tests

1. **`test_eq15_constants.py`** — Reproduces Eq.15 numerical relation
   - Verifies: `(4/3) * (m_tau^2 / m_e^2)^6 ≈ k_e * e^2 / (G * m_e^2)`
   - **Does NOT** establish physical mechanism
   - **Does NOT** prove the relation is fundamental

2. **`test_eq15_numerology.py`** — Tests alternative formulas
   - Checks if Eq.15 is unique or part of large search space
   - Tests: different exponents, prefactors, muon vs tau

3. **`test_no_cosmology_leakage.py`** — Prevents circular reasoning
   - Ensures beta formulas don't use H0, Omega_m, Planck fits
   - Flags formulas with `uses_cosmological_observations=True`

4. **`test_beta_status_required.py`** — Enforces registry discipline
   - Every beta must have: symbol, units, status, source, interpretation
   - Conflicting values must have normalization notes

5. **`test_epistemic_registry.py`** — Tests invariants
   - Claims marked `fact` must have sources
   - Parameters marked `fact` with values must have sources

6. **`test_assumption_graph.py`** — Validates dependencies
   - H(z) fit depends on beta_d, beta_q
   - MULTING terms depend on PPN constraints

### Running Tests

```bash
# All tests
pytest

# With coverage report
pytest --cov=src --cov-report=term-missing

# Specific category
pytest tests/test_eq15*.py -v

# Stop on first failure
pytest -x
```

---

## Key Modules

### `constants.py`
Physical constants from PDG 2024/2025 and CODATA 2018.

**WARNING:** This file contains ONLY fundamental constants (m_e, m_tau, G, k_e, e, c, hbar).  
**DO NOT** add cosmological fitted parameters (H0, Omega_m, etc.) here.

### `epistemic_registry.py`
Core data models: `Claim`, `Parameter`, `EquationRecord`, `SourceRef`.

Every record MUST have an explicit `status` to prevent silent assumptions.

### `beta_definitions.py`
Legacy-but-active candidate registry of beta values, each **attributed to its
AI-service origin** (source-confirmed, `docs/93`):

- `beta_d` 4.25 — **Gemini** output
- `beta_d` 0.78 — **ChatGPT** output
- `beta_q` 8.10 — **Gemini** output
- `beta_q` 0.19 — **ChatGPT** output

**All marked `status="unclear"`** and **NOT Buckholtz model versions**. The actual
Table A1 caption pair (β_d=4.5, β_q=18.0, Claude) lives in `beta_provenance.py`,
the **single source of truth** for provenance and use-permission. Always consult
`beta_provenance.py` before using any value for modeling.

### `numerology_penalty.py`
Anti-numerology scoring:
- Complexity penalty for arbitrary choices
- Data leakage penalty for using cosmological observations
- Mechanism bonus for physical derivations

### `assumption_graph.py`
Dependency graph: tracks which claims depend on which assumptions.

Example:
```
H(z) fit
  ├── beta_d
  ├── beta_q
  ├── cluster radius definition
  └── sub-object kinetic energy definition
```

### `data_anchoring.py`
Registry of observational datasets with leakage risk flags.

**High leakage risk:**
- Planck CMB (Omega_m, H0)
- Cosmic chronometers H(z)
- Pantheon+ SNIa

**Safe inputs:**
- PDG particle masses
- CODATA fundamental constants

### `rosetta.py`
Buckholtz terminology ↔ mainstream physics mapping.

Example:
- "Isomeric Dark Matter" → "Hidden sector / mirror-matter-like dark sector"
- "MULTING" → "Modified gravity with multipole terms"
- "beta_d" → "Phenomenological scale parameter (definition unclear)"

---

## What This Repository Reproduces

✅ **Eq.15 numerical relation** — arithmetic verified to ~1% precision  
⚠️ Physical mechanism for exponent 6 and prefactor 4/3 is **unclear**  
⚠️ Dimensional analysis requires careful unit tracking

---

## What Remains Unclear

❓ **Beta definitions** — Are 4.25/8.10 and 0.78/0.19 different normalizations, versions, or different parameters?  
❓ **MULTING functional forms** — Exact equations for monopole, dipole, quadrupole terms  
❓ **PPN constraints** — Do dipole/quadrupole terms violate Solar System tests?  
❓ **6 isomers structure** — What defines an "isomer" in this context?  
❓ **Derived vs fitted** — Are beta values phenomenological fits or derivable from IDM structure?

---

## Dependencies

Source of truth: [`requirements.txt`](requirements.txt) + [`pyproject.toml`](pyproject.toml).

```
python >= 3.11
numpy  scipy  sympy  pandas  matplotlib       # core
pytest  pytest-cov  ruff  mypy                 # dev / CI
astropy  astroquery  requests                  # cluster data pipeline (src/cluster_data_pipeline.py)
```

Optional:
```
pydantic
networkx
jupyter
```

---

## Contributing

This is a **personal research-engineering project** for epistemic audit purposes.

If you wish to contribute:
1. Maintain the non-goals (no overclaiming, no refutation)
2. Add sources for all new claims/equations/parameters
3. Mark status explicitly for all new records
4. Write tests for new functionality

---

## License

[MIT License](LICENSE) © 2026 Sergey Boyko ([ORCID 0009-0009-2178-5701](https://orcid.org/0009-0009-2178-5701), Ronin Institute for Independent Scholarship)

---

## Acknowledgments

This repository organizes and audits claims from:
- Thomas J. Buckholtz's work on Isomeric Dark Matter (IDM) and MULTING cosmology

Physical constants from:
- Particle Data Group (PDG) 2024/2025
- CODATA 2018

---

## Disclaimer

**This repository is NOT:**
- An endorsement of IDM/MULTING
- A refutation of IDM/MULTING
- A claim about ΛCDM validity
- A complete implementation of IDM/MULTING physics

**This repository IS:**
- An epistemic audit tool
- A reproducibility scaffold
- A definition clarification aid
- A structured way to separate what is clear from what requires verification

**Use responsibly. Science advances through clarity, not through premature claims.**
