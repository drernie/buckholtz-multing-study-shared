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

**Option D [CHECKED 2026-07-17, PARTIAL — real bypass of the LOGIN wall, but wrong data]:**
`tng-project.org/files/TNG-Cluster_Catalog.zarr/` — publicly readable directory
(HTTP 200, no auth header, [VERIFIED-BASH] via direct `curl`), released 2025-03-05
alongside Nelson et al. 2024 "Introducing the TNG-Cluster simulation"
(arXiv:2311.06338). Confirmed real per-cluster zarr arrays (352 clusters,
float32) for: `mhalo_200c`, `mhalo_500c`, `r200c`, `r500c`, `fgas_r500`,
`richness_{9.5,10.0,10.5,11.0}`, `sfr_30pkpc`, `szy_r500c`, `temp_10kpc`,
`xray_0.5-2.0kev`, `coolcore_*`, `peakoffset_{sz,xray}_{x,y,z}`, `mass_smbh`,
`zform`, `mstar_{30kpc,100kpc}`, `mhi_halo`, `Bmag_10kpc`, `ne_10kpc`, `origID`.
**Verdict: does NOT unblock H1b.** No hydrostatic mass estimate anywhere in
this catalog (`mhalo_*` are gravitationally-bound/FoF masses, not X-ray
hydrostatic M_HE); all thermodynamic quantities are central/interior
(`_10kpc`, `_r500`), none reach the R200-5×R200 WHIM annuli this claim needs.
The interactive raw-particle/cutout API (`/api/TNGCluster/snapshots/`) remains
gated — confirmed still returning HTTP 403 [VERIFIED-BASH] on the same date.
This catalog is real and open, but it is a "headline derived-properties" table,
not the raw gas-cell data required to compute E_WHIM per cluster.

**Option E [CHECKED 2026-07-17, DEAD as a technical bypass — genuine human-contact
lead surfaced]:** The Three Hundred project (324 clusters, Gadget-X +
Gizmo-Simba) has exactly the right physics split across two papers from the
same collaboration:
- Li et al. 2025 (arXiv:2503.05011, A&A) — WHIM gas properties (T, density,
  mass fraction) out to 5×R200c, same T-range definition (10^5-10^7 K) this
  project already adopted from a related paper (Vladutescu-Zopp, Option C).
  [VERIFIED-BROWSERFETCH, full text read]: **zero Data Availability
  statement**; every result (Figs. 1-8) is a **median/stacked profile across
  all 324 clusters** — no per-cluster table exists in or alongside the paper.
- Gianfagna et al. 2021 (arXiv:2111.01903, EPJ Web Conf.) — hydrostatic mass
  bias for ~300 of the same clusters, z=0.07-1.3. [VERIFIED-BROWSERFETCH]: short
  conference proceedings (not a full journal article), "Code, Data, Media"
  section on the arXiv page is empty — no public per-cluster table found.
- **the300-project.org itself is unreachable** — confirmed independently two
  ways: direct `curl` (DNS/connection failure, `000`) and browser `navigate`
  (denied/failed), not merely a single tool's sandbox limitation. The project's
  own mirror page (weiguangcui.github.io/the300) states "all simulations and
  derived data products are publicly available" but the concrete download
  mechanism could not be located; a separate "Projects (restricted access)"
  pbworks page requires permission.
- **Verdict: not a usable technical bypass today**, but structurally the
  *best-fit* combination if pursued as a **human contact**, not a download —
  same collaboration, same 324 clusters, same simulation codes underlie both
  papers, so the per-cluster catalog plausibly exists internally even though
  neither paper published it. Direct email to the corresponding authors (Cui,
  W. — listed on both papers, or Li, R. for the WHIM paper) requesting the
  per-cluster E_WHIM(annulus) + M_HE table is a genuine, not-yet-tried,
  cheap next step. **Not sent this session** — requires explicit user
  approval (correspondence, not a technical action).

- **CONFIRMED 2026-07-17 [VERIFIED-BROWSERFETCH, official MNRAS Data
  Availability Statement, quoted verbatim]:** the FULL journal version of the
  Three Hundred hydrostatic-mass-bias study — Gianfagna et al. 2023, MNRAS
  518, 4238-4248, arXiv:2211.08372, DOI 10.1093/mnras/stac3364 (the
  conference proceedings 2111.01903 above is its condensed preview by the
  same authors, same ~300-cluster sample, same GADGET-X code as the WHIM
  paper) — carries this exact statement:
  > "DATA AVAILABILITY — The data underlying this article were produced as
  > part of THE THREE HUNDRED Project (Cui et al. 2018). They will be shared
  > on request to THE THREE HUNDRED collaboration, at
  > https://www.the300-project.org."
  This is not an inference — the authors' own words confirm the per-cluster
  data (including the hydrostatic mass bias half of what H1b needs) exists
  and is obtainable **on request**, not by public download. Combined with the
  WHIM paper (2503.05011, same collaboration, same clusters, same code) this
  makes the "email the collaboration" path in Option E the CONFIRMED correct
  access route, not merely a plausible guess. Verified corresponding-author
  contact: Giulia Gianfagna, [third-party email redacted] (from
  2111.01903v2 p.1, [VERIFIED-DIRECT-READ]). **SENT 2026-07-17** [USER-REPORTED]
  — data request drafted per this Option E, citing both papers (2503.05011 +
  2211.01903/MNRAS 518,4238), requesting per-cluster b_SZ/b_X at
  R200/R500/R2500 + WHIM thermal energy/mass fraction in radial annuli to
  ~5xR200. Awaiting reply — no fixed next_check date yet, suggest checking
  back in ~2-3 weeks if nothing arrives sooner.

**Observational cross-check catalog (for the REAL-DATA promotion step, NOT a
TNG bypass) — CHEX-MATE:** [VERIFIED-REAL via WebFetch of arXiv:2010.11972,
2026-07-08]
- What it is: "Cluster HEritage project with XMM-Newton — Mass Assembly and
  Thermodynamics at the Endpoint of structure formation", a 3 Ms XMM Heritage
  programme. 118 galaxy clusters, Planck-SZ selected, **minimally-biased /
  S/N-limited** (a real improvement over the flux-limited, Malmquist-biased
  MCXC catalog we used for the earlier H1a-style Pearson test).
- Two tiers: Tier-1 0.05<z<0.2, M ≈ 2–9×10^14 M_sun; Tier-2 z<0.6,
  M500 > 7.25×10^14 M_sun.
- Provides: individual hydrostatic masses (M_HE) to 15–20% accuracy + gas
  thermodynamics (T_X, density → M_gas) — exactly the ingredients for the
  cluster-interior side of delta_M = M_WL − M_HE (M_WL to be cross-matched
  from a weak-lensing survey, not in CHEX-MATE itself).
- **Honest limitation for H1b specifically:** CHEX-MATE outskirt coverage
  BEYOND R500 (the R200–3R200 WHIM zone H1b actually targets) is NOT confirmed
  in the overview paper, and X-ray outskirts are photon-starved. So CHEX-MATE
  is a strong real-data anchor for the mass-bias / interior-thermodynamics side
  and for an H1a-style re-test on a less-biased sample, but the WHIM-filament
  proxy itself still leans on the TNG simulation (Option A) or on SZ/filament
  data. It is the OBSERVATIONAL cross-check for a TNG-derived result
  ([VERIFIED-SYNTHETIC] → [VERIFIED-REAL] promotion), not a replacement for it.
- Source of this lead: consolidated-map review 2026-07-08 (CHEX-MATE was the
  one net-new item in an otherwise-already-covered project map).

## Status
[BLOCKED — WAITING_FOR_THE300_REPLY, second correspondence blocker alongside
TJB reply and TNG API] Claim defined. Estimand refined (5-ring binning,
T-covariate prohibition added). Options B, C, D all checked and confirmed
NOT to provide a bypass of TNG API access — full findings above. Option E
(The Three Hundred) is DEAD as a public download, but its own MNRAS Data
Availability Statement (Gianfagna et al. 2023, arXiv:2211.08372) explicitly
confirms the data "will be shared on request to THE THREE HUNDRED
collaboration" — outreach drafted per this confirmed route and **SENT
2026-07-17** [USER-REPORTED] to [third-party email redacted], requesting
per-cluster b_SZ/b_X + WHIM annulus data.
Next step: await a reply from either (a) The Three Hundred collaboration
(sent 2026-07-17, no fixed next_check yet — check back in ~2-3 weeks if
silent), or (b) TNG API approval (submitted 2026-07-01, login attempt
2026-07-04 returned "invalid email/password combination" — 16+ days
unresolved, no separate action pending). When either path opens, execute per
the revised 5-annulus design, and piggyback the NW-001 topology data pull in
the same session.
