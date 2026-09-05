# FINDING P193 — the pearl's own prediction is CONFIRMED: z∈{12,14,16}
# gives 5.4× more discriminating power than P191's z∈{3,5,7,10} at
# matched precision — but the standard finite-difference method breaks
# down near the domain boundary, requiring an independent analytic
# cross-check to trust the result

**Date:** 2026-09-05
**Continues:** `FINDING_P191`'s own Pearl Registry prediction and
`FINDING_P192`'s own found domain-of-validity boundary (z≈16.957).
**Authorization:** explicit user go-ahead, 2026-09-05 ("запусти третий
Fisher-forecast на z∈{12,14,16}").
**Script:** `P193_fisher_forecast_last_window.py` (8 positive controls,
ruff clean, project's own 908 tests unaffected).
**Skeptic review:** dispatched context-blind **twice**. First pass
verdict **WEAKENED** — found a real unit-conversion bug in the analytic
Fisher matrix (100% mismatch, caught by a real pytest run before the
skeptic even needed to find it) and a real methodological gap (the
analytic-vs-finite-difference cross-check only validated agreement at
baseline, not in the augmented case where the synthetic term
dominates). Both fixed; second targeted pass on the fix confirmed no
remaining issue.
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** SUPPORTED — at σ=10% (the one σ where the
> standard finite-difference method converges), the result is
> confirmed by two independent methods agreeing to <0.15%. At σ=1%/3%,
> the result rests on the analytic method alone, cross-validated
> against finite-difference at both baseline (0.3%/0.08% agreement)
> and the one augmented case both methods can reach (0.1%/0.01%
> agreement) — strong but not identical-method confirmation.
> **Ontological/mechanistic interpretation status:** N/A — a
> statistical/information-theoretic property of TJB's own real χ²
> surface, not a physical mechanism claim.
> **Causal/cosmological claim status:** N/A (`NO_AUTHOR_ERROR`).

## Correction (2026-09-05, two rounds of context-blind Step 8a skeptic
review, both real, both fixed before finalizing)

**Round 1 finding (real bug):** the analytic Fisher matrix
(`analytic_fisher_matrix`) mixed unit systems — `E1(z),E2(z)` are
derivatives of `H²(z)` in SI units (`H2_of_z` works entirely in SI via
`KMSMPC_TO_SI`), but `H_of_z_kms` returns km/s/Mpc. A straight
`E_i/(2·H)` produced a **100% mismatch** against the finite-difference
Hessian on the baseline — caught by this file's own positive control
failing a real pytest run, not by the skeptic finding it first. Fixed:
`dH_kms/dβ_i = E_i(z) / (2·H_z·KMSMPC_TO_SI²)`.

**Round 1 finding (real methodological gap):** the fix's own positive
control validated analytic-vs-finite-difference agreement **only at
baseline** (33 real points, zero synthetic contribution) — exactly the
regime where the synthetic term (which dominates at tight σ) plays no
role. Fixed by adding a second positive control comparing both methods
in the **augmented** case at σ=10% (the one σ where finite-difference
converges): agreement improved to 0.1%/0.01%/0.0001% (small eigenvalue/
large eigenvalue/slope) — even tighter than baseline — directly
supporting trust in the analytic-only σ=1%/3% numbers, not merely
extrapolating from a baseline-only check.

## Method (as pre-registered in `CLAIM_P193`, plus what was discovered
along the way)

Same estimand, MCID, and machinery as `P191`/`P192`, at
z∈{12,14,16} — inside the domain of validity `P192` established, in
the last window before its found boundary (z≈16.957). **Pre-flight
margin check** (done before writing the script, then formalized as
Positive control 4): all 8 finite-difference corners at
h∈{1e-4,1e-5,1e-6} keep `H²(z=16)>0`, and the perturbed boundary itself
stays stable at z≈16.956-16.957.

**Unexpected finding, surfaced while preparing the script (not
anticipated by `CLAIM_P193`):** `H(z)` in this reconstruction does
**not** monotonically increase across the whole domain — it peaks near
z≈10 (~508 km/s/Mpc, matching `P191`'s own diagnostic) and then
**declines** toward zero as z approaches the `P192`-found boundary.
`H_fid` at z=12,14,16 is `[494.0, 429.8, 270.9]` km/s/Mpc — a
decreasing sequence. `P191`/`P192`'s own physicality positive control
required monotonic increase (valid for their z≤10 range) —
reformulated here to check what that control actually guarded against
(the sparse-grid bug's exact failure signature: `H(z)` silently pinned
to `H0_anchor`), plus a golden-value comparison, not monotonicity.

**Second unexpected finding:** the standard finite-difference Hessian
method (used without incident throughout `P176`→`P192`) does **not**
converge at this z-set for σ_synth∈{1%, 3%} across any step size
h∈{1e-4...1e-9} — central-difference error has two competing sources
(truncation ~h², roundoff ~ε/h²), and the "safe middle window" between
them is nonexistent this close to a domain boundary this curved.
Confirmed by widening the h-sweep itself, not loosening the pass bar
(per this project's own weakened-test-guard discipline). Only σ=10%
(the least demanding precision) and the ceiling (σ→0) show a genuine
plateau. **Resolved** by building an independent analytic Fisher
matrix from the already-verified `E1(z)/E2(z)` derivatives (no χ²
subtraction, so immune to this specific instability), cross-validated
against finite-difference wherever the latter converges (baseline AND
the one augmented case at σ=10%) before trusting it where
finite-difference cannot go (σ=1%, 3%).

## Result

| σ_synth | method | condition number | Δχ²=1 semi-axis | shrink | rotation | MCID met |
|---|---|---|---|---|---|---|
| 1% | analytic | 16683 → 113249 | 0.1683 → 0.0251 | **85.07%** | 2.372° | Yes |
| 3% | analytic | 16683 → 31070 | 0.1683 → 0.0392 | **76.70%** | 2.342° | Yes |
| 10% | finite-difference (converged) | 8310 → 4335 | 0.1681 → 0.0456 | **72.87%** | 2.043° | Yes |

**Comparison against `P191`'s own z∈{3,5,7,10} at matched σ** (73.0%,
45.6%, 13.6%): z∈{12,14,16} gives **more shrinkage at every matched
σ**, up to **5.4×** at σ=10% (72.87% vs 13.6%, both finite-difference,
directly apples-to-apples). At σ=1%/3% the comparison mixes methods
(analytic for P193, finite-difference for P191) — Positive control 7's
augmented-case cross-validation (0.1% agreement) makes this comparison
defensible, though the σ=10% comparison alone is the cleanest,
same-method result.

**Shrink is monotonically decreasing as σ loosens** (85.07% → 76.70% →
72.87% for 1%→3%→10%), the physically expected direction (tighter
assumed precision → more information → more shrinkage) — internally
consistent across the method transition at σ=3%→10%, with only a ~4pp
change, not a suspicious jump.

## Verdict

**The pearl's own falsifiable prediction (`FINDING_P191`, 2026-09-05,
`next_check` 2026-12-01) is CONFIRMED, not falsified**: synthetic z
past the level-set slope's own peak (found in `P191`) gives measurably
*more* discriminating power than `P191`'s own z∈{3,5,7,10} — by a
factor of up to 5.4× at matched precision, not merely "measurably
different" as the pearl's own weaker wording allowed for. This is the
first result in the `P176`→`P190`→`P191`→`P192`→`P193` lineage that
demonstrates a concrete numerical benefit of choosing z-values further
from the baseline's χ²-weighted slope, not just characterizing what
already exists (`P176`/`P190`) or finding where the model breaks down
(`P192`).

**A separate, real methodological finding**: standard finite-difference
Hessian computation — this project's default method since `P176` —
is not reliable close to a domain-of-validity boundary, even when the
boundary itself is safely avoided (Positive control 4). Any future
Fisher-forecast work near a found boundary should check convergence
with a wide h-sweep before trusting a result, and have an independent
method (here, the analytic Fisher matrix, now reusable) ready as a
cross-check.

## What this does NOT establish

1. Does not establish z∈{12,14,16} as realistically observable H(z)
   redshifts by any current technique — same caveat as `P191`/`P192`.
2. Does not mean the *entire* window (10,17) is uniformly informative —
   only that these 3 specific points are; a denser scan was not
   attempted.
3. Does not resolve bottleneck 3 — `docs/134`'s absolute-scale/
   observable-mapping question remains untouched.
4. Does not establish that the point-count difference (P191's 4 points
   vs this file's 3) contributes zero to the shrinkage difference — not
   controlled for; a matched-count comparison was not run. Since Fisher
   information adds roughly linearly with point count, this would, if
   anything, mean the z-location effect is *understated* here (3 points
   already outperforming 4), not overstated — but the claim is stated
   for the z-choice actually tested, not decomposed into
   count-vs-location contributions.
5. Does not evaluate whether v82's own theory is correct
   (`NO_AUTHOR_ERROR`).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
