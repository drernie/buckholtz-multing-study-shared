# Buckholtz IDM/MULTING Study

![tests](https://img.shields.io/badge/tests-533%20passed-brightgreen)
![coverage](https://img.shields.io/badge/coverage-72%25-yellow)
![ruff](https://img.shields.io/badge/lint-ruff%20clean-brightgreen)
![python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)
![license](https://img.shields.io/badge/license-MIT-green)

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
cd buckholtz-idm-multing-mvp

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
├── docs/                      # Documentation and audits
│   ├── 01_beta_definition_audit.md
│   ├── 02_equation_inventory.md
│   ├── 03_derived_fitted_assumed_unknown.md
│   ├── 04_assumption_dependency_graph.md
│   ├── 05_data_anchoring_map.md
│   ├── 06_rosetta_stone.md
│   ├── 07_numerology_audit_eq15.md
│   ├── 08_supplementary_audit.md
│   ├── 09_meeting_brief.md
│   ├── 10_time_budget.md
│   ├── 11_beta_normalization_math.md
│   ├── 12_beta_clarification_brief.md
│   ├── 13_internal_anchor_uniqueness.md
│   ├── 14_beta_source_trace_audit.md
│   ├── 15_notebooklm_beta_candidates.md
│   ├── 16_beta_provenance_reconciliation_summary.md
│   ├── 17_table_A1_manual_verification_protocol.md
│   ├── 18_fit_reproduction_requirements.md
│   ├── 19_sabine_audit.md (from /sabine epistemological review)
│   └── 22_discovery_ledger.md (10 findings: gold/copper/diamond/fool-gold classification)
│
├── notebooks/                 # Jupyter notebooks for exploration
│   ├── 01_eq15_reproduction.ipynb
│   ├── 02_beta_candidate_audit.ipynb
│   └── 03_ppn_constraints.ipynb
│
├── src/                       # Core Python modules
│   ├── __init__.py
│   ├── constants.py           # Physical constants (PDG, CODATA)
│   ├── epistemic_registry.py  # Claim/Parameter/Equation data models
│   ├── beta_definitions.py    # Beta parameter candidates
│   ├── equations.py           # Equation records
│   ├── numerology_penalty.py  # Anti-numerology scoring
│   ├── assumption_graph.py    # Dependency graph
│   ├── data_anchoring.py      # Observational data registry
│   └── rosetta.py             # Buckholtz↔mainstream terminology
│
└── tests/                     # Pytest test suite
    ├── test_eq15_constants.py
    ├── test_eq15_numerology.py
    ├── test_no_cosmology_leakage.py
    ├── test_beta_status_required.py
    ├── test_epistemic_registry.py
    └── test_assumption_graph.py
```

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
Physical constants from PDG 2022 and CODATA 2018.

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

## Safe Questions for Dr. Buckholtz

> **Preamble:**  
> "Dr. Buckholtz, I am trying to build a small reproducibility notebook for my own understanding. My goal is not to validate or challenge the model, but to separate definitions, fitted quantities, derived quantities, and testable predictions."

**Questions:**

1. Are beta_d and beta_q currently intended as **fitted phenomenological parameters**, or do you see a path toward **deriving them** from the internal IDM/MULTING structure?

2. The values beta_d = {4.25, 0.78} and beta_q = {8.10, 0.19} appear in different contexts. Do these represent:
   - Different normalizations?
   - Different versions of the model?
   - Supplementary calculations vs main predictions?

3. For MULTING dipole and quadrupole terms: do you have explicit functional forms H(z, beta_d, beta_q) that I could implement?

4. Have the MULTING dipole/quadrupole modifications been checked against Solar System PPN constraints (gamma, beta parameters from light deflection, perihelion precession)?

---

## Communication Protocol

### Do ✅

- Start with what was reproduced or organized
- Frame the project as **strengthening reproducibility**
- Ask clarification questions
- Use "I may have misunderstood..." when raising issues
- Avoid claims of validation or refutation

### Do NOT ❌

- ❌ Do not say "your model is wrong"
- ❌ Do not say "AI proved the relation"
- ❌ Do not say "this validates IDM"
- ❌ Do not say "this disproves ΛCDM"
- ❌ Do not lead with accusations about GR violation

---

## Dependencies

```
python >= 3.11
pytest
numpy
scipy
sympy
pandas
matplotlib
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

[MIT License](LICENSE) © 2026 Sergey Kuts

---

## Acknowledgments

This repository organizes and audits claims from:
- Thomas J. Buckholtz's work on Isomeric Dark Matter (IDM) and MULTING cosmology

Physical constants from:
- Particle Data Group (PDG) 2022
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
