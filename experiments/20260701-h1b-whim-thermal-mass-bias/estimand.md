# Estimand — H1b: WHIM Thermal Energy vs Cluster Mass Bias

## EstimandOps L0 Classification
**Question type:** Predictive (observational correlation test)

## Population
Galaxy clusters in cosmological simulations (IllustrisTNG-300 or Three Hundred),
M_200c > 5×10^13 M_sun, z = 0.0–0.5.

**Inclusion criteria:**
- Relaxed + unrelaxed clusters (all dynamical states)
- Mass range: 10^13.7 – 10^15.5 M_sun (group → massive cluster)
- Redshift: z < 0.5 (to match observational counterpart CCCP, WtG)

**Exclusion criteria:**
- Halos in merging pairs (< 3 R_200 separation) — avoid mass bias confusion
- Central subhalos only (not satellite halos)

## Intervention
N/A — observational/predictive study.

## Comparator
Null hypothesis: r(delta_M, E_WHIM) = 0 — WHIM thermal energy does NOT predict
the lensing-to-hydrostatic mass gap.

## Endpoint
E_WHIM = integral of n_e × kT × dV for gas cells with T in [10^5, 10^7] K,
n_e < 10^-4 cm^-3 (WHIM density cut, following Vladutescu-Zopp et al. 2025
methodology [VERIFIED-REAL], see Data requirements Option C below).

**Radial binning (revised 2026-07-01, per boyko-method atomization):** compute
E_WHIM separately in 5 annuli [0-1], [1-2], [2-3], [3-4], [4-5] × R_200, NOT as
a single bulk R_200-3×R_200 shell. Rationale: near R_200 the gas transitions
from ICM (already tested and KILLED in H1a) to WHIM; a single bulk shell would
mix regimes and could mask or manufacture a signal. Report r(delta_M, E_WHIM)
per annulus AND for the bulk sum, pre-registered as co-primary endpoints.

delta_M = M_WL − M_HE  (or equivalently M_true − M_HE for simulations)

Units: E_WHIM in erg (or keV/cm^3 × Mpc^3); delta_M in 10^14 M_sun.

## Summary Measure
Pearson correlation r(delta_M, E_WHIM).
Secondary: Spearman ρ (non-parametric, robust to outliers).
Tertiary: partial r controlling for M_WL (or M_true).

## MCID (Minimum Clinically Important Difference)
r > 0.30 required for H1b to be considered practically significant.
(Lower than H1a threshold of 0.40, because WHIM is the MORE physically
motivated proxy for TJB's mechanism.)

## ICE (Intercurrent Events)
**ICE strategy: treatment-policy**

Potential ICEs in simulation context:
- Major merger event (mass ratio > 1:3) occurring between snapshots → include cluster
  as-is at snapshot time; do not remove. Merging state is part of the real-world
  variation we are testing.
- Gas shell below density threshold (no gas cells in R_200–3R_200 shell) → treat as
  E_WHIM = 0; include in analysis. Absence of WHIM is a valid physical state.

Rationale: treatment-policy strategy preserves the full heterogeneity of cluster
environments, consistent with a real-world observational interpretation. Excluding
merging clusters would bias toward relaxed systems and underestimate variance.

**Significance threshold (for MCID confirmation):**
p < 0.10 required alongside r > 0.30 for PROMOTE verdict.
(One-tailed test; H1b predicts positive correlation.)

## Natural Language Statement

"We estimate the Pearson correlation between (M_true − M_HE) and the
warm-hot intergalactic gas thermal energy (T = 10^5–10^7 K) in the
R_200 to 3×R_200 shell for 100+ simulated galaxy clusters at z < 0.5,
comparing clusters with different WHIM environments to test whether
higher filament thermal energy predicts a larger true-to-hydrostatic
mass gap."

## What this does NOT mean

1. Does NOT test TJB's mechanism at cosmological (z > 1) scales
2. Does NOT test WHIM acting as a gravitational source — only tests
   statistical correlation (which is necessary but not sufficient for H1)
3. A positive r does NOT prove causality (WHIM → mass bias could be
   explained by cluster dynamical state → both higher WHIM + higher mass bias)
4. Does NOT apply to the WHIM in the true cosmic web (filaments between
   clusters, Mpc scale) — here we test WHIM in the cluster outskirts only
5. Simulation result [VERIFIED-SYNTHETIC] if from IllustrisTNG — must be
   followed by observational cross-check [VERIFIED-REAL] for promotion
6. **T as a direct covariate is FORBIDDEN in any partial-correlation test
   here.** E_WHIM = n_e × kT × dV is multiplicatively built from T — testing
   "does T mediate the E_WHIM/delta_M relationship" by adding T as a separate
   covariate is the SAME circular-covariate trap that produced a retracted,
   invalid result in H1c (see null_results/20260701-nr012, Addendum). If a
   temperature-mediation question is genuinely needed, use n_e alone (not
   multiplied by T) as the alternative proxy, analogous to the M_gas-only
   redesign proposed for H1c's retracted test.

## Prior literature summary (FL Step -4: Source Trace)

| Claim | Status | Source |
|-------|--------|--------|
| Connectivity (filament count) NOT correlated with mass bias | [VERIFIED-REAL] | Sayers et al. 2024, A&A (Three Hundred, N=3000) |
| External pressure contributes to sub-virial behavior | [VERIFIED-REAL] | Braspenning et al. 2024, MNRAS (FLAMINGO) |
| Non-thermal motions dominate mass bias | [VERIFIED-REAL] | FLAMINGO (Braspenning et al. 2024) |
| WHIM soft X-ray excess ∝ cluster dynamical state | [VERIFIED-SYNTHETIC] | Vladutescu-Zopp et al. 2025 arXiv:2506.18459 (TNG, N=138) |
| WHIM thermal energy in filaments vs mass bias: NO PRIOR TEST | [VERIFIED-ABSENT] | This work (H1b is novel) |

## Pre-registered criteria (set BEFORE seeing data)

- PROMOTE (H1b survives): r > 0.30, p < 0.10 (lower threshold justified by
  more physically motivated proxy vs H1a)
- INCONCLUSIVE (REPEAT): 0.15 ≤ r ≤ 0.30 or 0.05 < p < 0.10
- KILL (H1b fails): r < 0.15 AND p > 0.20

## Data requirements (FL Step -2: Cheapest differentiating test)

**Option A (only remaining path): IllustrisTNG-300 API**
- URL: https://www.tng-project.org/api/
- Registration: free (tng-project.org account) — submitted 2026-07-01, pending
  admin approval as of 2026-07-04 (no confirmation email received in 14 days,
  checked via Gmail search [VERIFIED-tool])
- Need: API key for gas particle data
- Per-cluster: gas cells, T-filter, r-shell filter (5 annuli — see Endpoint
  section above), sum n_e×kT×dV
- M_HE: compute from pressure gradient of gas within R_200 (standard X-ray hydrostatic)
- M_true: SubhaloMassType[0+1] (DM + gas + stars within R_200)
- Sample: ~200 clusters at M > 5×10^13 M_sun at z=0.2 (snapshot ~67)
- Cost: ~4-8h Python + API
- **Piggyback opportunity:** the same per-cluster TNG pull should also compute
  the network/topology metric φ_i needed to revive `parked/NW-001`
  (cosmic-web-topology-audit) — one API session, two experiments.

**Option B [CHECKED 2026-07-01, PARTIAL — does not bypass Option A]:**
Barnes et al. 2020 "Characterizing hydrostatic mass bias with Mock-X"
(arXiv:2001.11508) [VERIFIED-REAL via WebFetch, confirmed title/authors:
David J. Barnes, Mark Vogelsberger, Francesca A. Pearce, Ana-Roxana Pop,
Rahul Kannan, Kaili Cao, Scott T. Kay, Lars Hernquist].
- Confirmed: uses IllustrisTNG (+ BAHAMAS + MACSIS); reports mass-dependent
  hydrostatic bias, up to b=0.3 for most massive clusters (synthetic
  observations) vs ~0.13 (simulation-derived profiles)
- Confirmed ABSENT: no mention of WHIM/IGM/cosmic-web filaments anywhere
- No public machine-readable per-cluster table found: checked arXiv abstract
  page for data-availability statement, GitHub link, Zenodo/Vizier/CDS release
  — none found [VERIFIED-tool, WebFetch 2026-07-01]. Caveat: this checks
  arXiv metadata only, not the full PDF body text, so a data-availability
  line inside the paper itself is [INFERRED-ABSENT], not fully [VERIFIED-ABSENT].
- Verdict: provides an existing b_HSE methodology/reference for TNG clusters,
  but does NOT provide WHIM data — Option A (TNG API) is still required to
  get the WHIM side of the correlation.

**Option C [CHECKED 2026-07-01, DEAD — cannot bypass Option A]:**
Vladutescu-Zopp et al. 2025 (arXiv:2506.18459) [VERIFIED-REAL via WebFetch
ar5iv, direct quote confirmed].
- Sample confirmed: TNG300-1, z=0, log(M200[M_sun/h])>14 (mean 1.97e14 M_sun/h),
  138 clusters, 5 radial annuli [0-1]...[4-5] R_200 — this is the source of
  the revised radial-binning design above
- WHIM definition confirmed: 10^5 < T < 10^7 K, n_e < 10^-4 cm^-3 — matches
  and refined our own T-range definition
- **Killed as a shortcut:** paper states verbatim "we focus instead on the
  relative ratios of baryonic masses, and we do not discuss hydrostatic
  masses." No mass bias of any kind is measured. Cannot be used to bypass
  TNG API access.

## Status
[BLOCKED — Option A only] Claim defined. Estimand refined (5-ring binning,
T-covariate prohibition added). Options B and C both checked and confirmed
NOT to provide a bypass of TNG API access — full findings above.
Next step: await TNG API approval (submitted 2026-07-01, login attempt
2026-07-04 returned "invalid email/password combination" — ambiguous between
wrong password and account not yet activated; user troubleshooting via
password reset). When API access is confirmed, execute per the revised
5-annulus design, and piggyback the NW-001 topology data pull in the same
session.
