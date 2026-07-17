# Claim — H1b: WHIM Filament Thermal Energy vs Cluster Mass Bias

## Question type (EstimandOps L0)
[x] Predictive — does E_WHIM (filament thermal energy) predict delta_M (mass bias)?

## Relationship to H1 hierarchy
H1 (broad TJB): cosmic web IGM thermal energy = 2nd gravitational source
H1a (KILLED 2026-07-01): cluster ICM thermal energy → WL-HE mass gap; r=0.021 p=0.883
H1b (THIS): WHIM gas (T=10^5-10^7 K) in R_200-3×R_200 shell → mass gap

H1b tests a MORE PHYSICALLY MOTIVATED proxy than H1a:
- H1a used ICM (inside cluster, T>10^7 K) — confirmed NULL
- H1b uses WHIM (outside cluster, T=10^5-10^7 K) — the actual filament gas TJB refers to

## Falsifiable claim
H1b: Within a simulated cluster sample (N>100), the mass gap (M_true - M_HE)
correlates POSITIVELY with the WHIM thermal energy E_WHIM in the cluster
outskirts (R_200 < r < 3×R_200, T=10^5-10^7 K), such that clusters
embedded in denser/hotter WHIM show a larger true-to-hydrostatic mass gap.

**Pre-registered KILL criterion:** r < 0.15 AND p > 0.20 → H1b KILLED
**Pre-registered PROMOTE criterion:** r > 0.30 AND p < 0.10 → H1b PROMOTED

## Source for data
[OPTION A — only remaining path] IllustrisTNG-300, snapshot 67 (z≈0.2) or 99 (z=0):
  API: https://www.tng-project.org/api/TNG300-1/
  Reference: Springel et al. 2018, MNRAS 475, 676
  Status: registration submitted 2026-07-01, pending approval as of 2026-07-04

[OPTION C — CHECKED, DEAD 2026-07-01] Vladutescu-Zopp et al. 2025, arXiv:2506.18459:
  138 TNG clusters with soft X-ray excess (WHIM proxy) + dynamical state.
  Paper states verbatim: "we do not discuss hydrostatic masses." No mass
  bias data of any kind — cannot bypass Option A. (Radial-annulus design
  and WHIM T-range definition were still useful and adopted, see estimand.md.)

[OPTION B — CHECKED, PARTIAL 2026-07-01] Barnes et al. 2020, arXiv:2001.11508
  ("Characterizing hydrostatic mass bias with Mock-X"): has b_HSE for TNG
  clusters, but confirmed ZERO WHIM/IGM data — does not bypass Option A either.

## Counterfactual Frame
In what world is H1b true?
  → Clusters embedded in denser WHIM have larger lensing-to-HE mass gap
  → The WHIM thermal energy contributes to total gravitational potential
  → At fixed M_WL: more WHIM → more "hidden" gravity → more discrepancy

Alternative worlds (that could produce r > 0.30 WITHOUT TJB mechanism):
  1. Dynamical state mediator: disturbed clusters have both more WHIM accretion
     AND larger mass bias (from non-thermal ICM pressure) — confounded
  2. Mass scaling: more massive clusters have more WHIM AND more mass bias
     due to merger history — controlled by partial correlation

→ If r > 0.30 survives partial correlation controlling for M_true AND dynamical
  state → H1b is genuinely supported (not confounded)

## Claim Entropy (Perelman)
N_unsupported_HIGH = 1 (TJB mechanism; awaiting empirical test)
N_hidden_assumptions = 2 (WHIM in R_200-3R_200 is relevant; T range 10^5-10^7 K captures TJB's component)
N_missing_negative_controls = 1 (no negative control yet)
N_ambiguous_definitions = 1 (WHIM boundary: some papers use 3R_200, some use 5R_200)
N_unresolved_blockers = 1 (TNG API access not yet set up)
Total claim_entropy = 6 → must decrease with each experimental step

## Literature context
- Three Hundred (2024): CONNECTIVITY ≠ mass bias [VERIFIED-REAL] — but this tests count, not E_WHIM
- FLAMINGO (2024): external pressure IS relevant but non-thermal motions dominate
- Vladutescu-Zopp+2025: WHIM soft X-ray excess ∝ cluster dynamical state
- H1b test: GENUINELY NOVEL — no paper tests E_WHIM(shell) vs delta_M directly

## Status
[NEEDS-DATA, WAITING_FOR_THE300_REPLY] Experiment designed. Data access pending.
Current experimental status: IN-PROGRESS (literature survey complete, including a
2026-07-17 re-check for TNG-API bypasses — see estimand.md Options D/E; data
analysis not started).
Next action: Options B/C/D (Barnes 2020, Vladutescu-Zopp 2025, TNG-Cluster public
zarr catalog) all checked and confirmed dead as technical bypasses. Option E
(The Three Hundred, arXiv:2503.05011 + arXiv:2111.01903, same 324-cluster
collaboration) is dead as a public download, but the CONFIRMED-CORRECT access
route per the collaboration's own MNRAS Data Availability Statement (Gianfagna
et al. 2023, arXiv:2211.08372: "shared on request to THE THREE HUNDRED
collaboration") — data request drafted and **SENT 2026-07-17** [USER-REPORTED]
to [third-party email redacted]. Now awaiting reply (no fixed next_check date
yet; check back in ~2-3 weeks if silent). Otherwise: await TNG API approval
(16+ days unresolved, no action pending on that front).
