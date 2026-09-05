# CLAIM P196 — independent rebuild + overdensity-definition correction
# for the Girardi-R_vir vs TJB-style R200(z) comparison (TJB's own
# Section II.F Class III circularity)

**Date:** 2026-09-06
**Origin:** TJB's own letter (2026-08-30), pointing to Section II.F of
v82 — his own 3-class evidentiary system, flagging `r_X(z)` built via
`ρ_crit(z)` (the Friedmann equation) as "the most serious residual
dependence" and inviting continued scrutiny. A prior, separate chat
session ran a first version of this check (Girardi 1998's `R_vir=
0.002σ` vs a `ρ_crit(z)`-based `R200` on 123 real HeCS-SZ clusters,
`r=0.883`, mean ratio `1.128±13%`, scatter `±14%`) but left its files
only in that session's scratchpad, and did not control for the
overdensity-definition mismatch between the two radii.
**Authorization:** explicit user go-ahead, 2026-09-06 ("хочу", after a
structured 10-point evaluation naming this as priority 1-2 of a 5-step
plan).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (comparing two radius-estimation
routes on real data — not a causal claim).

**Correction (2026-09-06, caught mid-analysis, before any number was
finalized):** this claim's own title and Endpoint 1/2 text below still
say "R200," reflecting the prior chat's own stated method — kept
unedited here per this project's no-silent-correction convention. Once
code was written and run at Δ=200, the raw ratio (1.61) did not match
the prior chat's reported 1.128, which is what surfaced a real error:
v82's own Section II.F (verified directly, lines 602-604 of this
project's markdown conversion) calls its `r_X(z)` construction "the
standard R500-type definition" — Δ=500, not Δ=200. `P196`'s own script
was rewritten to retarget R500 (matching this project's own earlier,
same-session `P158_addendum2_real_mass_function.py` convention,
`OVERDENSITY=500`). See `FINDING_P196` for the full, corrected
analysis and its own further finding that the prior chat's headline
number likely also has a separate units bug.

## What is independently re-verified before this file (this session, not
## the prior chat's self-report)

- `[VERIFIED-arXiv]` v82 Section II.F (lines 540-643 of the project's
  own markdown conversion): Class I/II/III system exists exactly as
  described, including the verbatim quotes "the most serious residual
  dependence" and "a starting point for a broader, symmetric practice."
- `[VERIFIED-arXiv, primary source, full text downloaded]` Girardi et
  al. 1998 (astro-ph/9804187): `R_vir≈0.002·σ_P (h⁻¹Mpc)` (their Eq. 11)
  is derived from (a) the virial theorem mass estimator (their Eq. 5)
  and (b) the spherical-collapse virial-density criterion `ρ_vir(t₀)=
  18π²ρ₀=18π²·3H₀²/8πG` for an `Ω₀=1` universe (their Eq. 9), combined
  with an empirical `R_PV(A)` relation from real galaxy distributions
  (Girardi et al. 1995, their Eq. 10). **No N-body calibration step
  anywhere in this derivation** — confirms the prior chat's own
  self-correction (they first wrongly assumed N-body calibration,
  caught it via skeptic + primary source, corrected before reporting).
- `[VERIFIED-arXiv]` HeCS-SZ (Rines et al. 2015/2016, arXiv:1507.08289,
  VizieR `J/ApJ/819/63/table4`): real catalog, "123 clusters from
  optical spectroscopy," columns `z [0.02,0.3]`, `sigma [305,1261]
  km/s`, `M200c [0.4,12.4]×1e14 Msun` (**labeled "Caustic mass"** —
  i.e., the catalog's own `M200c` is itself a caustic-technique mass
  estimate, not independently re-derived here; this file uses it only
  as the mass input to a `ρ_crit(z)`-based radius, reproducing TJB's
  own Class III construction, not re-validating the mass itself).

## Real correction to the prior chat's own framing, found this session

Girardi's `R_vir` is **not** "genuinely independent of GR/Friedmann" as
the prior chat's handoff stated. It depends on `H₀` (needed for any
absolute physical scale, unavoidable) **and** on a static `Ω₀=1`
assumption embedded in the `18π²` virial-density constant — this is
much lighter than TJB's own Class III circularity (`ρ_crit(z)=
ρ_crit,0·E(z)²`, the FULL z-evolving Friedmann relation, with no
z-dependence in Girardi's formula at all), but it is not zero
cosmological content either. The precise, defensible framing: Girardi's
`R_vir` is independent of the z-EVOLUTION of the Friedmann equation
(no `E(z)`, no `Ωm/ΩΛ`) that TJB's Class III specifically flags, but
still depends on `H₀` and a fixed-epoch `Ω₀=1` collapse constant — by
TJB's own 3-class system this places it closer to Class I/II, not
Class III, but "genuinely independent" overstates it.

## New estimand element specific to this file (the actual new work)

**Population**: the 123 real HeCS-SZ clusters (`z∈[0.02,0.3]`,
`σ∈[305,1261]` km/s), re-fetched independently this session via
`astroquery.vizier` (same pattern as this project's own
`src/cluster_data_pipeline.py:_vizier_download`), not copied from the
prior chat's inaccessible scratchpad files.

**Endpoint 1 (reproduction)**: `R_vir(Girardi)=0.002·σ_P` vs
`R200(TJB-style)=(3·M200c/(4π·200·ρ_crit(z)))^(1/3)`, raw ratio and
scatter across all 123 clusters — an independent rebuild of the prior
chat's own number, not a copy of it.

**Endpoint 2 (the actual fix, per the user-approved plan's priority 1-2)**:
same comparison, but with `R_vir` converted to an `R200c`-equivalent in
**two explicit, separately-reported steps** (found while designing this
correction, not in the prior chat's framing):

- **Step 2a — reference-density correction (EXACT, no free parameter)**:
  Girardi's formula (their Eq. 9) sets `ρ_vir(t₀)=18π²·ρ_crit,0` — the
  criterion is referenced to TODAY's critical density, using `H₀` only,
  with no `E(z)` anywhere. For a cluster observed at `z>0`, this is a
  different reference than `ρ_crit(z)` (TJB's own, and HeCS-SZ's
  `M200c`'s own convention). Converting to the same density reference
  at fixed `Δ=178` is exact and mass-conserving:
  `R_vir,z-ref = R_vir · [ρ_crit,0/ρ_crit(z)]^(1/3) = R_vir / E(z)^(2/3)`.
  At the sample's high-z end (`z≈0.3`, `Ωm=0.3,ΩΛ=0.7`), `E(z)²≈1.36`,
  an **~11% radius correction from this step alone** — analytically
  exact, no concentration assumed.
- **Step 2b — overdensity-shape correction (approximate, concentration-
  dependent)**: convert `Δ=178` (now on the same `ρ_crit(z)` reference,
  after 2a) to `Δ=200`, via the NFW mass profile and a literature
  concentration-mass relation (Duffy et al. 2008, cited explicitly, its
  own ∼0.1 dex scatter reported as this step's real uncertainty, not
  hidden).

Reporting both steps separately (not just their combined effect) lets
the write-up state which part of any shift is exact vs. model-dependent
— required per this project's own evidence-marking discipline.

**Endpoint 3 (diagnostic, cheap, discovered while designing Endpoint 2)**:
does the raw (uncorrected) ratio or residual correlate with `z`? Since
Girardi's formula carries no `E(z)` at all while `ρ_crit(z)` does,
a real z-trend in the raw ratio would be diagnostic of this specific,
separate mechanism (not just the static Δ-definition mismatch).

**Falsifiable predicate**: if Endpoint 2's Δ-correction moves the mean
ratio from `1.128` materially toward `1.0` and/or shrinks the `±13-14%`
scatter, the original raw finding is largely a definitional artifact of
comparing `Δ_vir` to `Δ_200c`, not informative about GR/Friedmann-
dependence specifically. If the ratio and scatter survive the
correction largely unchanged, the original finding is strengthened —
it is not explained away by the definitional mismatch.

**MCID (pre-registered before running)**: the correction is judged
material if it moves the mean ratio to within `[0.95,1.05]` (i.e.
closes at least half the gap from `1.128`) **or** reduces the scatter
by more than 5 percentage points (from `±14%` toward `≤9%`). Below
both thresholds, the raw finding is judged ROBUST to this specific
correction — real, not explained by Δ-definition alone.

## Positive control (specific to this file)

Reproduce Girardi 1998's own headline internal consistency claim as a
sanity check on the imported formula/constants before trusting any
comparison: the `R_c=0.17 h⁻¹Mpc` and `α≈0.70` values feeding Eq. 10-11
must reproduce the paper's own stated `R_vir≈0.002·σ_P (h⁻¹Mpc)`
numerical coefficient to reasonable precision when Eq. 9-10 are
combined symbolically.

## What this does NOT establish

1. Does not re-validate HeCS-SZ's own `M200c` caustic-technique mass
   estimates — reused as given, with the caustic method's own known
   systematics (filling-factor N-body calibration, per the prior
   chat's own already-completed investigation of Gifford, Miller &
   Kern 2013) as an acknowledged, separate limitation not addressed
   here.
2. Does not attempt the caustic-technique-from-scratch reimplementation
   — the prior chat correctly scoped this as a multi-day undertaking
   and parked it; this file does not revisit that decision.
3. The NFW concentration-mass relation used for the Δ-conversion
   (Endpoint 2) is itself a modeling assumption with real scatter
   (∼0.1 dex in `c(M,z)` is typical) — the correction's own uncertainty
   is reported, not treated as exact.
4. Does not resolve whether TJB's Class III circularity is a fatal
   problem for MULTING/v82 — a narrower, real question: does an
   independent (of `ρ_crit(z)`-evolution) radius measurement roughly
   agree with the construction TJB himself flagged as circular, once
   overdensity-definition differences are controlled for.
5. Does not draft or send anything to TJB — per this project's own
   standing constraint, that step follows only after this file's own
   Step 8a skeptic pass, and only on a separate, explicit request.
