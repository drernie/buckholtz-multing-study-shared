# Decision — 20260713-h1e-agn-feedback-confound

**Date:** 2026-07-17 (test executed; pre-registration was 2026-07-13)
**Status:** KILL (H1e)
**Evidence grade:** B (N=47/50 real observational data [VERIFIED-REAL])

## Data source

`artifacts/cccp_mahdavi2013_merged.csv` — Mahdavi et al. 2013 (arXiv:1210.3689) Tables 1+2,
re-extracted via `pdfplumber` direct PDF read (superseding an earlier unreliable WebFetch
AI-summarized partial extraction). 50/50 clusters, zero name mismatches between Table 1
and Table 2. [VERIFIED-DIRECT-READ]

**Coverage:** 47/50 CCCP clusters have both K0 and wX populated — same 3 exclusions as
NR-012 (Abell0115S, Abell2104, Abell2219).

## Numerical results [OUR-RECONSTRUCTION]

Computed by `artifacts/h1e_partial_correlation_test.py`, re-runnable against the committed CSV.

### Baseline (K0/wX-available subsample, N=47)
| | r | p |
|--|---|---|
| partial r(delta_M, E_ICM \| M_WL) | −0.7143 | 1.72×10⁻⁸ |

Matches NR-012's own baseline on the same 47-cluster subsample (−0.714) to 3 decimals —
internal consistency check passes.

### KEY TEST — residual partial correlation controlling for K0 (AGN-feedback proxy)
| | r | p |
|--|---|---|
| partial r(delta_M, E_ICM \| M_WL, K0) | **−0.7181** | 1.33×10⁻⁸ |

**Change in \|r\| after adding K0 as covariate: +0.0038** (i.e. \|r\| essentially
unchanged — K0 adds no explanatory overlap with the delta_M/E_ICM relationship).

### Secondary checks (does K0 itself predict the outcome variables at fixed M_WL?)
| Test | r | p | Interpretation |
|------|---|---|----------------|
| r(K0, delta_M \| M_WL) | 0.0180 | 0.904 | AGN-feedback state does NOT predict mass bias at fixed M_WL |
| r(K0, E_ICM \| M_WL) | 0.0795 | 0.595 | K0 is NOT confounded with the thermal-energy proxy at fixed M_WL |

### A2 check — is K0 just a relabeling of wX (already tested in H1c)?
| Test | r | p | Interpretation |
|------|---|---|----------------|
| raw r(K0, wX) | 0.3091 | 0.0345 | Correlated but far from identical (r²≈0.096 shared variance) — consistent with the source paper's own Spearman r=0.52±0.10 (also non-degenerate). H1e tests a mechanistically distinct channel from H1c, not a restatement. |
| partial r(delta_M, E_ICM \| M_WL, wX) | −0.7260 | 7.73×10⁻⁹ | Reproduces NR-012's exact number — cross-check that the merged dataset is consistent with the original H1c computation. |

## Verdict

**H1e KILLED** by pre-registered criterion (`claim.md`):
- \|r_residual\| = 0.7181 > 0.40 (kill threshold), p = 1.33×10⁻⁸ < 0.10
- AGN-feedback activity (proxied by central entropy K0) does NOT mediate or explain
  away the partial correlation between the ICM thermal-energy proxy and mass bias.

The partial correlation r(delta_M, E_ICM | M_WL) ≈ −0.71 to −0.72 is **NOT** an artifact
of AGN-feedback / cool-core state. K0 is essentially orthogonal to both delta_M and
E_ICM once M_WL is controlled (both secondary checks p > 0.5, not significant) — the
same pattern H1c found for morphology (wX).

## Kill Analysis

**What was killed:**
H1e — the hypothesis that standard cluster physics (AGN radio/kinetic-mode feedback,
proxied by central entropy K0) explains the partial anti-correlation between ICM
thermal energy and lensing-hydrostatic mass gap, WITHOUT invoking a TJB-style second
gravitational source.

Conditions: {CCCP N=47 (K0/wX-available subset), K0 as the AGN-feedback proxy, linear
partial correlation method, OUR_RECONSTRUCTION}.

**What was NOT killed:**
1. H1 (broad TJB mechanism) — H1e was the third natural standard-physics alternative;
   its failure does not confirm H1, but removes another major competing explanation.
2. H1b — WHIM filament thermal energy correlation (still NEEDS-DATA, TNG API, blocked
   16+ days as of this writing).
3. The reality and strength of the partial r ≈ −0.70 to −0.73 — now verified robust
   against FOUR independent falsification attempts (raw NR-010, mass-split NR-011,
   morphology-split NR-012, AGN-feedback-split H1e), all converging on the same
   magnitude with four different covariates.

**Important interpretive note:** killing H1e does NOT promote H1. All three natural
standard-physics alternatives investigable on existing CCCP data (mass threshold,
morphology, AGN feedback) are now eliminated. Non-thermal pressure support and
instrument/measurement systematics in the weak-lensing mass estimate itself remain
untested and are NOT addressed by any of H1a/c/d/e.

## Relaxation Map (cumulative, H1 Cycle 2 extended)

| Branch | Changed assumption | Prediction | Status |
|--------|--------------------|-----------|--------|
| H1a | ICM thermal energy ~ mass gap (raw) | r > 0.4 | KILLED (r=0.021) |
| H1d | Mass-threshold effect | \|r_high\| >> \|r_low\| | KILLED (r_diff=0.001) |
| H1c | Morphology (wX) mediates partial r | residual r drops to <0.20 | KILLED (r=−0.726) |
| H1e | AGN feedback (K0) mediates partial r | residual r drops to <0.20 | **KILLED (r=−0.718)** |
| H1b | WHIM gas in filaments | r > 0.30 in simulations | NEEDS-DATA (TNG API, blocked) |
| WL measurement systematics | shape-pipeline/triaxiality bias in M_WL itself | untested | **not yet formulated as a branch** |

## Skeptic concerns (pre-answered)

**Concern 1:** "K0 and wX are correlated (r=0.31) — is this test independent of H1c?"
→ ADDRESSED. r²≈0.096 means <10% shared variance; the A2 check confirms controlling
for wX instead of K0 reproduces NR-012 exactly, and controlling for K0 leaves the
partial r essentially unmoved — the two covariates behave independently here, not as
duplicates of the same test.

**Concern 2:** "K0 alone may be a weak/noisy AGN-feedback proxy — a null here doesn't
rule out AGN feedback in general."
→ ACCEPTED as limitation, same class as H1c's wX limitation. A genuinely cleaner test
would use a direct radio-power or X-ray-cavity catalog, not a spectroscopic entropy
proxy. K0 was chosen because it required no new catalog fetch (already in Table 2) and
is the metric the source paper itself uses to define cool-core status.

## Status summary for H1 (all standard-physics alternatives)

| Sub-hypothesis | Status | Data |
|----------------|--------|------|
| H1a | KILLED (2026-07-01) | r=0.021, N=50 CCCP [VERIFIED-REAL] |
| H1c | KILLED (2026-07-01) | r_residual=−0.726, N=47 CCCP [VERIFIED-REAL] |
| H1d | KILLED (2026-07-01) | r_diff=0.001, N=50 CCCP [VERIFIED-REAL] |
| H1e | **KILLED (2026-07-17)** | r_residual=−0.718, N=47 CCCP [VERIFIED-REAL] |
| H1b | NEEDS-DATA | TNG API required (user action, blocked 16+ days) |

**H1 (broad) status: all four testable standard-physics alternatives on existing CCCP
data are now KILLED.** The partial correlation r ≈ −0.70 to −0.73 is:
- NOT explained by raw thermal energy (H1a)
- NOT mass-threshold dependent (H1d)
- NOT explained by morphological/dynamical state (H1c)
- NOT explained by AGN-feedback/cool-core state (H1e)

This does NOT confirm the TJB mechanism. H1b (WHIM/filament, TJB's actual proposed
cosmic-web-scale mechanism) is now the ONLY remaining untested channel among those
originally considered, and remains externally blocked. A genuinely new alternative
(weak-lensing measurement systematics) has not yet been formulated as a testable branch.

**UPDATE 2026-07-18 (NR-015):** "4/4 KILLED" above is correct as stated -- none of H1a/c/d/e
is mediated by the confound each specifically targeted. But this table's implicit reading
("therefore the correlation is unexplained by standard physics") does not follow: none of
the four controlled for T_X, and a dedicated test found `r(delta_M, M_gas | M_WL, T_X)`
collapses to -0.08 (p=0.58, bootstrap 95% CI [-0.39,0.27]) once T_X is controlled, while T_X
alone (r=-0.81) is the strongest predictor found in the whole program. **Mechanism is NOT
established** -- an independent skeptic review (context-asymmetry, no session history) found
a live competing explanation: cluster dynamical state as a genuine common physical driver of
both T_X and delta_M, not distinguished from the definitional M_hydro-T_X-coupling reading by
this test. See `null_results/20260718-nr015-tx-shared-variable-artifact.md` for the full
Skeptic Response Matrix. H1b is unaffected under either reading and remains the correct next
step.

*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
