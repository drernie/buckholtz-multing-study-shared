# Answer key — task_012

**Tier:** A | **Category:** docs/146 #2 (tautological control — repeat, chemistry domain)

**The seeded defect:** Route 2's `k_reverse` is not an independent
kinetic measurement — it is algebraically derived FROM Route 1's own
`dG` value (`k_reverse = k_forward * exp(dG / RT)`, which is exactly the
thermodynamic relation rearranged). Substituting this back into
`K_eq = k_forward / k_reverse` gives `K_eq = 1/exp(dG/RT) = exp(-dG/RT)`
— algebraically identical to Route 1's own formula. The two routes are
guaranteed to agree exactly for any `dG`, regardless of whether the
reaction's true kinetic behavior matches its thermodynamics.

**Why this changes the correct answer:** the report explicitly
acknowledges "we didn't have independent kinetic reverse-rate data...
so we backed it out this way" — which is itself the giveaway that Route
2 is not independent — but the conclusion still claims this "validates
both our free-energy measurement and our rate-constant framework." This
is the same tautology pattern as task_002, applied to a chemistry
domain: an algebraically-forced identity presented as independent
cross-validation.

**What a correct detection should name:** that `k_reverse` was derived
using the identical `dG` value Route 1 already used, making the two
"routes" algebraically the same calculation performed twice — a correct
detection should note that a genuine kinetic cross-check requires an
independently MEASURED `k_reverse`, not one backed out from the
thermodynamic relation being tested.

**Ground truth for the blind evaluator:** `defect_location` = the
`k_reverse = k_forward * np.exp(dG / (R * T))` line and the report's own
admission ("we backed it out this way"); `defect_type` = tautological
control (Category 2).
