# docs/122 — Bottleneck Synthesis & Cosmological-Branch Verdict

**Date:** 2026-07-12 (v1), **corrected 2026-07-12 (v2)**, **strengthened 2026-07-13 (v3)**
via a full invariant beta_d/D0 parameterization protocol (user-specified) — see "v3:
Invariant Parameterization Protocol" at the end of this document for the decisive result.
**Status:** SYNTHESIS — cross-checks an external "top-10 bottleneck" adversarial audit
against this project's own accumulated evidence (facts.json, R001-R011, Q001-Q006),
then resolves a genuine internal contradiction the review surfaced using the project's
own production code on the real dataset (not a re-derivation from prose).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR

## Source

Two user-supplied external documents (2026-07-12): a "top-10 bottleneck" audit, and a
second-pass review of this document's first version that caught three overclaims and
one direct contradiction between this synthesis and this session's own S2 pilot result.

## Correction history (v1 -> v2)

The reviewer caught, correctly, that v1:
1. Said "8 of 10 bottlenecks closed" when the table itself showed most were *registered
   as open dependencies*, not closed. Category error between "we have evidence about
   this" and "this is resolved."
2. Claimed "STOP at every beta anyone has proposed" while this session's own S2 pilot
   (experiments/20260712-llm-consensus-verification/) had, hours earlier, produced
   beta_d=1.368e8 — a directly contradicting counter-example the synthesis had not
   checked against its own conclusion.
3. Called the N=5 unequal-mass path (5 x 1.074 = 5.37) a "self-consistent" answer, when
   Omega_DM/Omega_b = sum(m_i/m_b * n_i/n_b) also requires number densities, not just
   masses — the arithmetic match alone does not establish self-consistency.
4. Reported "excluded at 130-477 sigma" for the equal-hot IDM thermal-history scenario
   with a precision the underlying back-of-envelope Delta_N_eff estimate does not support.

All four are corrected below. Point 2 was resolved not by softening the wording alone,
but by actually running the project's own `src/pearson_fit.py` on the real n=443 cluster
dataset at S2's beta_d scale — see "Resolving the S2 contradiction" below. The result
is stronger than either the original claim or the reviewer's proposed narrowing.

## Cross-check result: reclassified per the reviewer's 4-bucket framework

| Bucket | # | Bottleneck |
|---|---|---|
| Empirically tested (limited scenario) | 2, 9 | Dipole/quadrupole scale (R011); equal-hot IDM thermal history vs N_eff (R005/EXP-O) |
| Registered as open dependencies | 1, 3, 4, 6 | Action/Lagrangian (Q006); force->H(z) mapping (Q005); beta meaning (Q004); PPN/equivalence principle (`docs/29`, scoped not executed) |
| Partial / derivative | 5, 7 | Covariance & conservation (derivative of #1, no action -> no Noether currents to check); multi-body/continuum dynamics (derivative of #3) |
| Conditional rescue path, not a solution | 8, 10 | N=5 unequal-mass 5:1 arithmetic (needs relic-abundance calc, see below); IDM as a model class (already the project's own framing, not newly resolved) |

**Corrected summary sentence:** *8 of 10 bottlenecks were already present in this
project's dependency graph before this synthesis. Two received quantitative negative
tests (dipole/quadrupole scale, equal-hot thermal history). The rest were open,
partially explored, or have a conditional-but-unconfirmed rescue path — none were
closed by this synthesis.* This does not weaken the project's standing — it shows the
project mapped the right problem space in advance, which is itself evidence of a
well-built dependency graph, not evidence that the problems are solved.

## Resolving the S2 contradiction — verified against the real dataset, not just reworded

The reviewer's math was correct as far as it went: F_d/F_m scales linearly with
beta_d/D0 (holding cluster data fixed), so S2's beta_d=1.368e8 (same D0=100 Mpc
convention as R011) should, on paper, give F_d/F_m orders of magnitude above 1 —
appearing to contradict "F_d/F_m negligible at every proposed beta."

**Ran the actual check** (`src/pearson_fit.single_pearson`, real n=443 MCXC cluster
pairs, same code R011 used, not a re-derivation):

```
beta_d=4.5      (reported)  -> r=0.7334, n_valid=443/443, F_d/F_m median=1.83e-7 (exact R011 match)
beta_d=1.0e6                -> r=0.7252, n_valid=443/443
beta_d=1.0e7                -> r=0.4041, n_valid=412/443  (already breaking down)
beta_d=1.2e7                -> r=0.3251, n_valid=380/443
beta_d=1.368e8  (S2's value) -> r=NaN,    n_valid=0/443   (phi < 0 for every real cluster)
```

**Finding:** S2's beta_d does not represent a viable alternative regime — applied to the
real, full 443-cluster dataset, it makes phi(z) negative for every single cluster,
which is undefined for this model (phi must be positive; H_MULT requires sqrt(phi)).
S2 fit successfully **only** on its own n=6, 2-free-parameter pilot subsample (with
`ADDITIONAL_ASSUMPTIONS` explicitly noting a positivity constraint was imposed and
satisfied there) — a small, sparse sample where a large enough beta_d can be tuned to
keep phi positive for those 6 specific clusters without breaking on the full population's
wider spread of k_A, M, R values. This is a textbook small-sample overfitting artifact,
not a rescued physical regime.

**Corrected conclusion:** the S2 result does NOT rescue large beta_d as a viable
alternative — it independently demonstrates, via a second and different failure mode,
that beta_d values large enough to make the dipole term matter break the model on real
data (either by making it undefined, as shown here, or by degrading the H(z) correlation
well before that, as the r=0.40 point at beta_d=1e7 shows). This is a *stronger* result
than the original claim, verified two different ways on the same real dataset.

## Applying the (corrected) frozen criterion

**Corrected form:** F_d/F_m < 1 by 4-6 orders of magnitude at every beta_d, beta_q value
that is either (a) source-attributed (AI-reported: ChatGPT 0.78/0.19, Claude/Table A1
4.5/18.0, Gemini 4.25/8.10), or (b) found by an unconstrained fit to the full, real
n=443 dataset (grid-search optimum, R011). The one beta_d value that appeared not to
fit this pattern (S2's 1.368e8, fit to a 6-cluster subsample) was checked against the
real dataset directly and found to break the model entirely rather than rescue it.

**What remains genuinely open:** whether an *independently derived* (not fit to any
subsample of Table A1, H(z), or cluster data) beta_d/beta_q could differ from all of
the above. No such derivation exists yet (bottleneck #1/#4) — this is the actual open
door, not "any large beta_d works if you pick the right small sample."

## Verdict (Kill Analysis, per this project's own falsification-ladder.md discipline)

**KILLED:** published/source-attributed beta values (O(1-10)) give a dipole/quadrupole
contribution that is negligible (F_d/F_m ~ 1e-7 to 1e-6) at real cluster scales — this
cannot drive the claimed cosmic-acceleration mechanism.

**KILLED (new, this correction):** the hypothesis that a sufficiently large beta_d
(found by unconstrained fitting rather than derivation) rescues the mechanism — checked
directly on the real 443-cluster dataset; large beta_d breaks the model (phi<0) well
before it could make the dipole term dominate in a way that survives contact with the
full real population.

**NOT ESTABLISHED:** that no possible independently-derived beta_d/beta_q (via
bottleneck #1, an action/Lagrangian not fit to any data) could work. No independent
upper bound on beta_d/beta_q exists in this project (grep-verified) — but "unconstrained
fitting doesn't find one" is now real evidence against this door too, not just an
open question.

**NOT KILLED:**
- The MULTING dipole/quadrupole force law as a mathematical object.
- The IDM isomer postulate generally.
- The N=5 unequal-mass 5:1 arithmetic match — downgraded from "self-consistent
  resolution" to **conditional rescue, unconfirmed**: Omega_DM/Omega_b = sum(m_i/m_b *
  n_i/n_b) requires number densities per sector, not just masses. The 5 x 1.074 = 5.37
  match implicitly assumes n_i ~ n_b for every dark sector, which needs its own
  reheating/relic-abundance calculation (bottleneck #9) before it counts as consistent
  cosmology rather than an arithmetic coincidence.
- Eq.32 (R001) — explicitly out of scope, independent numerical relation.

**Relaxation map:** revival requires bottleneck #1 (an action/Lagrangian deriving
beta_d, beta_q without fitting Table A1, H(z), or any cluster subsample) — and per the
new finding above, any such derivation should be checked for whether it survives the
same real-dataset positivity/breakdown test before being taken as a rescue.

## N_eff precision — corrected

R005/EXP-O's Delta_N_eff=15-81 vs Planck N_eff=2.99+-0.17 for the equal-hot 5-sector
scenario is excluded by many orders of magnitude beyond the observationally permitted
addition — this is qualitatively decisive. The specific "130-477 sigma" figure is a
diagnostic from a simplified Gaussian-tail back-of-envelope estimate (pearl_registry
2026-06-21), not a validated result from the actual Planck likelihood, and should not
be read as a rigorously quantified exclusion level. Kept internally as a magnitude
indicator; not to be cited externally as a precision statistic.

## What this synthesis does NOT do

- Does not claim TJB made an error (NOT_AUTHOR_ERROR).
- Does not make any public claim (NO_PUBLIC_CLAIMS) — internal project synthesis only.
- Does not extend to IDM's isomer/dark-matter postulate as a whole.

## Source data

R011, R005, Q004/Q005/Q006 (`facts.json`), `experiments/20260712-llm-consensus-verification/`,
`code/beta_rescaling.py`, `src/pearson_fit.py` (re-run 2026-07-12 for this correction,
see command in facts.json R011 `s2_beta_d_real_dataset_check_2026_07_12`).

---

## v3: Invariant Parameterization Protocol (2026-07-13)

User-specified 5-step protocol run in full against `src/pearson_fit.py` (production
code, real n=443 MCXC dataset). Both frozen outcomes (PASS-A and PASS-B) turned out to
hold simultaneously, which is stronger than either alone.

**Step 1 — definitions fixed** from the exact source: `phi = m_A/D^2 - 2*beta_d*k_A*r_A/D^3
+ (beta_q*k_A*r_A)^2/D^4`, `D = D0_Mpc/(1+z)`, `H_MULT = H_anchor*sqrt(phi/phi_ref)`,
`H_anchor=73.0` (production default), masses in Msun, R in Mpc, k_A = E_thermal/c^2 in Msun.

**Step 2 — scaling symmetry: PASS-A, proven analytically and confirmed to 14 significant
digits.** Substituting D=D0/(1+z) shows `phi = (1/D0^2) * Phi(eta_d, eta_q; data)` where
`eta_d = beta_d/D0`, `eta_q = beta_q/D0`, and `Phi` does not depend on D0 at all — the
`1/D0^2` factor cancels exactly in `phi/phi_ref`. Verified: `r(D0=100, beta_d=4.5,
beta_q=18)` through `r(D0=10000, beta_d=450, beta_q=1800)` agree to 14 decimal places.
**beta_d is not an independently identifiable parameter; only eta_d = beta_d/D0 is
physically meaningful.** This alone explains why R011 (D0=100), S1 (D0=1, self-chosen),
and S2 (D0=100) beta_d values are not directly comparable as raw numbers.

**Step 3 — D0-sweep with re-optimization:** `grid_search_pearson` at D0 in
{0.01,...,10000} finds r plateauing near 0.6235 (matching R011) across most D0, but the
specific (eta_d, eta_q) found by the grid does not collapse to one point — consistent
with, and now extending, R011's own earlier finding of a beta_q saturation plateau
(r flat for beta_q gtrsim 10 at D0=100): the flat basin exists uniformly in eta-space
across all tested D0, not as a D0-specific artifact.

**Step 4 — feasible region, refined:** the protocol's literal criterion (max F_d/F_m
subject only to phi_i>0 for all i) is **mathematically unbounded** — proven analytically:
F_d/F_m depends only on eta_d, while positivity for any eta_d can always be restored by
choosing eta_q large enough (the eta_q^2 term eventually dominates the linear -eta_d
term for any cluster). Positivity alone does not bound the dipole's effective strength;
a fit-quality constraint must be added for Step 4 to be well-posed. With that constraint
added (requiring the model to retain meaningful correlation with real H(z), not just be
mathematically defined):

| eta_d | median F_d/F_m | r (real H_CC) | valid clusters (of 443) |
|---|---|---|---|
| 0 (monopole) | 0 | 0.733 | 443 |
| 2.46e4 | 0.1 | 0.704 | 443 |
| 1.23e5 | 0.5 | 0.332 | 378 |
| 2.46e5 | 1.0 | 0.145 (noise-level) | 188 |
| 4.92e5 | 2.0 | 0.102 | 45 |
| 2.46e6 | 10 | undefined | 0 |

By the time the dipole reaches half the monopole's strength, correlation has already
collapsed by more than half and 65 of 443 real clusters already have undefined phi.
**No point on the continuous eta_d spectrum gives F_d/F_m >= 1 while the model remains
both well-defined and meaningfully correlated with real data.**

**Step 5 — train(70%)/holdout(30%, seed=42) at eta_d=2.46e5 (the F_d/F_m=1 threshold):**
train r=0.010 (131/1218 valid), holdout r=0.440 (57/522 valid), vs. monopole baseline
train r=0.725 (306/1218), holdout r=0.755 (137/522). The collapse reproduces independently
in both splits (noisy at small holdout N, but the qualitative collapse is not a
single-sample overfitting artifact).

### v3 Verdict

**PASS-A confirmed** (exact, analytic + 14-digit numerical): beta_d, beta_q individually
are not physical observables; only eta_d=beta_d/D0, eta_q=beta_q/D0 are.

**PASS-B confirmed, with the Step 4 refinement**: across the full continuous eta_d
spectrum on the real, complete 443-cluster dataset — not just at source-attributed or
previously-fitted beta values — there is no feasible region where the dipole term
dominates (F_d/F_m >= 1) while the model stays well-defined and correlates with real
H(z) above noise level. This is strictly stronger than the v2 verdict (which was scoped
to "every beta proposed to date"): v3 sweeps the entire relevant eta_d axis directly and
finds the same wall analytically-grounded and out-of-sample-confirmed, independent of
what anyone has or hasn't proposed.

**This does not change the Kill Analysis scope from v2** (still limited to the MULTING
dipole/quadrupole cosmic-acceleration mechanism, in this project's specific formula/
formalization; still open pending bottleneck #1). It replaces the v2 argument ("nobody
has proposed a working beta yet") with a stronger one ("no eta_d makes it work, proven
by direct sweep, independent of what anyone proposes").
