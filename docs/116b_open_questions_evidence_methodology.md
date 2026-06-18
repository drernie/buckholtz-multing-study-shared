# docs/116b — Open Questions (§4.8) + Evidence vs Authority Methodology

**Date:** 2026-06-19
**Items:** p27 (60%→75%), p32 (60%→75%)
**Source:** buckholtz_preprints202511.0598.v6.md §4.8 [VERIFIED-tool]

```
Safety: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
```

---

## ITEM p32: Open Questions Enumeration from Preprint §4.8

Section 4.8 "Potential Future Endeavors and Directions for Observational,
Experimental, and Theoretical Physics" organizes open questions in 6 categories.

### 1. Observations

| # | Open Question | Our Status |
|---|---------------|------------|
| 1a | Collect more H(z) data to support/extend/refute the work | CC Moresco 2022 used; BAO not yet integrated |
| 1b | Find direct evidence of MULTING dipole repulsion between galaxy clusters | Not attempted; requires detailed cluster dynamics data |
| 1c | Determine if dark matter comports with cold DM or MESI (marginally EM self-interacting) | Not attempted |
| 1d | Find notable dark-matter : ordinary-matter ratios (beyond those in §2.6) | Not attempted |
| 1e | Determine which of 1:1 or 0:1 CMB hyperfine depletion ratio pertains | Not attempted |
| 1f | Gravitational wave signatures from neutron star / black hole collisions (same vs different isomer) | Not attempted |
| 1g | Characterize dark-matter IGM / plasma; narrow IDM candidate descriptions | Not attempted |

**Our coverage: 1/7 (1a partially)**

### 2. Experiments

| # | Open Question | Our Status |
|---|---------------|------------|
| 2a | Detect or rule out MULTING non-monopole gravitation | Not attempted; LHC/satellite data needed |
| 2b | Detect or rule out quantum interactions between ordinary matter and gravity | Not attempted |
| 2c | Make or detect IDM dark-matter elementary particles | Not attempted |
| 2d | Detect or rule out inflaton particle at ~30.4 GeV | Checked via idm_masses.py: no detection at LEP/LHC; future prediction |
| 2e | Detect or rule out other possible elementary bosons (§2.12) | Not attempted |

**Our coverage: 1/5 (2d: numerically framed, unobserved)**

### 3. Models and Modeling

| # | Open Question | Our Status |
|---|---------------|------------|
| 3a | Develop multi-object / continuous-distribution modeling for MULTING+IDM | Bridge computation: BLOCKED (BETA-1 HOLD) |
| 3b | Determine parameter space where dipole (n_F=3) repulsion dominates | dipole_threshold.py: analytical framing, β_d/β_q ratio required |
| 3c | Determine extent to which cluster interactions underlie H(z) data; close gaps | MULTING bridge: BLOCKED |
| 3d | IDM vs ΛCDM dark matter: galaxy cluster collision aftermath | Not attempted |
| 3e | IDM vs ΛCDM dark matter: galaxy collision aftermath | Not attempted |
| 3f | Quasar accretion/ejection: roles of n_F=2,3,4 gravitation | Not attempted |
| 3g | Galaxies: transition between spin-related and random motion (n_F=3) | Not attempted |
| 3h | Galaxy clusters: transition between spin-related and random motion (n_F=3) | Not attempted |
| 3i | Filaments: evidence for distinct large objects bigger than filaments | Not attempted |
| 3j | Explore usefulness of n_F≥4 MULTING terms | Not attempted |
| 3k | When is GR/MULTING/other adequate | Not attempted |

**Our coverage: ~1/11 (3b partially via dipole_threshold.py)**

### 4. Applications of Physics Theory

| # | Open Question | Our Status |
|---|---------------|------------|
| 4a | Determine MULTING+IDM applicability limits (early universe cutoff time) | Not attempted |
| 4b | MULTING+IDM implications for inflation, nucleosynthesis, early universe | Not attempted |
| 4c | MULTING vs GR: when can MULTING theoretically replace GR? | Not attempted |
| 4d | Explain (5+):1 DM:OM ratio given IDM 5:1 isomer ratio | idm_masses.py: N_opt=5.364≠5, gap framed as Planck vs IDM |
| 4e | Dark matter baryon acoustic oscillations implications | Not attempted |
| 4f | Early universe n_F=5 octupole era implications | Not attempted |
| 4g | Dark matter electromagnetism early universe implications | Not attempted |
| 4h | IDM compatibility with collision ratio data [refs 247-250] | Not attempted |
| 4i | Narrow IDM dark matter candidate class | Not attempted |
| 4j | Reach of weak/strong interaction across isomers | Not attempted |
| 4k | Predict 1:0 vs 0:1 galaxy ratios (dark-only vs ordinary-only) | Not attempted |

**Our coverage: ~1/11 (4d partially via idm_masses.py)**

### 5. Physics Theory

| # | Open Question | Our Status |
|---|---------------|------------|
| 5a | β_d: connection to gravitomagnetic permeability (gravitoelectromagnetism) | BRAI quantified via brai_beta.py; derivation still open |
| 5b | β_q: connection to gravitational field constant | BRAI quantified; derivation still open |
| 5c | Full field equations and Lagrangian for MULTING+IDM | Not attempted |
| 5d | Symmetry groups for the six isomers | Not attempted |
| 5e | Deeper principles for relationships between physics constants | fermion mass formula verified (p21); inflaton verified (p25) |
| 5f | Reduce number of independent constants | Not attempted |
| 5g | Explore attribute choices: nature vs model | Not attempted |
| 5h | Replace "rate of expansion of universe" with cluster-based terminology | Not attempted |
| 5i | Symmetry between quark masses/generations and lepton masses/flavours | Eq.21-24 verified for leptons; quarks match Table 7 |

**Our coverage: 3/9 (5a via BRAI, 5e via fermion formula, 5i via quark geom means)**

### 6. Science and Society

| # | Open Question | Our Status |
|---|---------------|------------|
| 6a | How work can focus/accelerate cosmology/particle physics research | Not addressed (outreach scope) |
| 6b | Society benefits from work and extensions | Not addressed |
| 6c | Small vs large datasets: advantages/disadvantages | Not addressed |
| 6d | Evidence vs authority in science — relationships | Addressed below (p27) |
| 6e | Relative extent of reliance on evidence vs authority | Addressed below (p27) |
| 6f | Improve communications about science | Not addressed |

**Our coverage: 2/6 (6d-e via p27 analysis)**

### Summary: Open Questions Coverage

```
Category             Questions   Our coverage   Notes
─────────────────    ─────────   ────────────   ─────
1. Observations          7           1/7        1a partially
2. Experiments           5           1/5        2d framed
3. Models               11          ~1/11       3b partially
4. Applications         11          ~1/11       4d partially
5. Physics theory        9           3/9        5a,5e,5i
6. Science/society       6           2/6        6d-e
─────────────────    ─────────   ────────────   ─────
TOTAL                   49          ~9/49       ~18%

Item p32: 60% → 75% [VERIFIED-tool from preprint §4.8]
```

---

## ITEM p27: Evidence vs Authority Methodology (§4.8.6.d-e + overall)

TJB explicitly frames his methodological position in §4.8.6:

> *"Explore, across subsets of scientific work or other work, relationships between evidence
> (such as data), authority (such as assumptions and popular modeling), and other factors."* (§4.8.6d)

> *"Explore, across subsets of scientific work or other work, the relative extents of reliance on
> evidence (such as data), reliance on authority (such as assumptions and popular modeling),
> and reliance on other factors."* (§4.8.6e)

### TJB's Evidence-First Methodology

From the Appendix A prompt (lines 1743-1750 of preprint):

> *"If you have a choice between relying on data and relying on outputs from models or theories,
> please try, as much as is practical, to emphasize using data. (My work includes an attempt to
> fit data empirically. My work attempts to develop a complement or alternative to some models
> or theories.)"*

TJB's position (our classification): **Data-first empiricism**

| Aspect | TJB Position |
|--------|--------------|
| Primary criterion | Data match (empirical fit) |
| Role of theory | Provides framework; does NOT override data |
| Role of authority | Popular modeling = one reference, not truth |
| Falsifiability | Explicit criterion: data can refute |
| ΛCDM | One framework among others; TJB offers "complement or alternative" |

### Our Audit Methodology (aligned with TJB)

Our audit follows the same evidence-first principle:

| Claim | Our approach | Evidence type |
|-------|-------------|---------------|
| H_FLRW provenance | Fitted TJB's 11 data points, NOT Planck by assumption | [VERIFIED-inline] power-law fit |
| β_d / β_q values | Three AI services measured → BRAI quantified inconsistency | [VERIFIED-tool] BRAI |
| Fermion masses | Formula tested against PDG 2024 measured values | [VERIFIED-inline] |
| DM:OM ratio | Used Planck Ωcdm/Ωb data, not IDM postulate | [VERIFIED-inline] |
| NR-008 falsified | Used actual r=0.682 < 0.75 threshold | [VERIFIED-inline] |

### Authority vs Evidence: Where We Differ from Popular Modeling

| Question | Authority (ΛCDM) answer | Data answer | Source |
|----------|------------------------|-------------|--------|
| H_FLRW form | Standard flat ΛCDM, Planck params | Power-law H(z)=54.07(1+z)^0.884 fits better | hflrw_grid.py |
| f×σ8 tension | ΛCDM predicts bell-shaped fsig8(z) | Real RSD data is flat (r=-0.086 vs ε) | fsig8_robustness.py |
| β_d / β_q | No ΛCDM analog | Phenomenological, 5.8×-95× spread across AI | brai_beta.py |
| DM mass | CDM: all cold, featureless | IDM: 5+1 isomers, neutron-like | idm_masses.py |

### Operational Definition for Outreach

*"TJB's methodology treats ΛCDM as a convenient baseline, not an authority.
Our independent audit follows the same principle: we test every number against data,
not against established models. Where our fits conflict with Planck (e.g. H_FLRW form),
we report the conflict and flag it for author confirmation — we do not override TJB's
data-fit with Planck assumptions."*

```
Item p27: 60% → 75%
Evidence: [VERIFIED-tool] from preprint text at lines 1743-1750, 1565-1576
```

---

## Cross-reference to Docs

| Related doc | Content |
|-------------|---------|
| docs/101 | Error correction after authority-vs-evidence audit |
| docs/107 | Post-M8 evidence lock |
| docs/111 | β provenance evidence lock |
| scripts/brai_beta.py | BRAI quantification of AI divergence |
| scripts/hflrw_grid.py | Data-fit for H_FLRW (not Planck-imposed) |
| scripts/idm_masses.py | PDG verification of TJB predictions |
