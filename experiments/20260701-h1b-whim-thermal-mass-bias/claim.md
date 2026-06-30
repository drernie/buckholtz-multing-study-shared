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
[OPTION A — recommended] IllustrisTNG-300, snapshot 67 (z≈0.2) or 99 (z=0):
  API: https://www.tng-project.org/api/TNG300-1/
  Reference: Springel et al. 2018, MNRAS 475, 676

[OPTION C — fastest] Vladutescu-Zopp et al. 2025, arXiv:2506.18459:
  138 TNG clusters with soft X-ray excess (WHIM proxy) + dynamical state
  Check if mass bias b_HSE is tabulated → direct correlation possible

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
[NEEDS-DATA] Experiment designed. Data access pending.
Current experimental status: IN-PROGRESS (literarure survey complete; data analysis not started)
Next action: Check arXiv:2506.18459 for per-cluster mass bias data (Option C, cheapest).
