# NR-015 — T_X-degenerate: M_gas independent contribution does NOT survive (mechanism unresolved)

**Date:** 2026-07-18 (pre-registered 2026-07-01, pearl_registry row 34; executed 2026-07-18
after a boyko-agent test flagged the overdue pearl and a structural concern about M_hydro)
**Verdict:** NOT-SURVIVES the pre-registered criterion (pearl row 34: `|r|>0.40` required to
SURVIVE). **Mechanism is NOT established** — see Skeptic Response Matrix below. Original
draft of this file used the label "ARTIFACT-CONFIRMED"; downgraded after independent
context-asymmetry skeptic review (2026-07-18) found the mechanism claim overreaching and the
point estimate statistically fragile. Do not cite the retired "ARTIFACT-CONFIRMED" label.
**Branch:** P001 redesigned test — the non-circular thermal-proxy retest promised in
`null_results/20260701-nr012-h1c-morphology-mediator.md`'s addendum, never executed until now
(next_check 2026-07-15, run 3 days late)

---

## Claim (falsified)

The partial correlation `r(delta_M, E_ICM | M_WL) ~= -0.70 to -0.73` (NR-010/011/012/014)
reflects a genuine, T_X-independent thermal-mass signal: `M_gas` alone (not multiplied by
`T_X`), after controlling for both `M_WL` AND `T_X`, would still show `|r| > 0.40` with the
mass gap. **This specific pre-registered claim is falsified** — the point estimate is
-0.08, far short of 0.40, and a 10,000-resample bootstrap 95% CI of [-0.39, 0.27] never
reaches 0.40 in either direction.

## Why falsified (what is solid)

`E_ICM_proxy = M_Gas * T_X` contains `T_X` by construction. Separately, `delta_M = M_WL -
M_hydro`, and `M_hydro` is a hydrostatic-equilibrium (HSE) mass — HSE mass estimation
generically requires the cluster temperature profile as an input (standard formula, e.g.
`M_HE,X ~ -r*kT(r)/(G*mu*m_p)*[dlnrho/dlnr + dlnT/dlnr]`, confirmed by direct reading of
Gianfagna et al. 2023, MNRAS 518,4238, eq. 2-3, and by a general WebSearch confirming CCCP
masses are HSE reconstructions from XMM-Newton/Chandra temperature data). So `T_X`
*plausibly* sits on both sides of the correlation. **This is a real, verified structural
possibility, not yet a demonstrated mechanism** — see Skeptic Response Matrix item 2.

| Test | r | p | Evidence |
|------|---|---|----------|
| Baseline (reference) r(delta_M, E_ICM \| M_WL) | -0.7008 | 1.46e-08 | `[VERIFIED-REAL]` N=50, matches NR-010 |
| **KEY TEST (exact pre-registration, pearl row 34):** r(delta_M, M_Gas \| M_WL, T_X) | **-0.0801** | **0.580** | `[VERIFIED-BASH]`, independently re-derived by skeptic code review; bootstrap 95% CI [-0.39, 0.27] |
| Secondary (looser, T_X not controlled) r(delta_M, M_Gas \| M_WL) | -0.6055 | 3.18e-06 | `[VERIFIED-BASH]` this number alone would have looked like SURVIVES -- see self-caught gap below |
| Context: r(M_Gas, T_X \| M_WL) | 0.7059 | 1.03e-08 | `[VERIFIED-BASH]` M_gas and T_X are strongly entangled at fixed M_WL -- expected under standard cluster self-similarity, not necessarily suspicious on its own |
| Context: r(delta_M, T_X \| M_WL) | -0.8108 | 9.58e-13 | `[VERIFIED-BASH]` T_X ALONE is the single strongest predictor found in the entire H1 program to date |
| Pre-registered SURVIVES threshold (pearl row 34, the ONLY threshold actually pre-registered on 2026-07-01) | \|r\|>0.40 required | NOT MET (point estimate -0.08, CI never reaches 0.40) | Clean, solid falsification of the SURVIVES prediction |

**Correction to the first draft of this file:** the original version stated an
"ARTIFACT-CONFIRMED... `\|r\|<0.20` required... Criterion set 2026-07-01" threshold as if it
were part of the 2026-07-01 pre-registration. **This was inaccurate.** Pearl row 34 only
pre-registered the SURVIVES threshold (`|r|>0.40`). The finer `<0.20 / 0.20-0.40 / >0.40`
tri-partition was written into `h1c_p001_mgas_only_retest.py` on 2026-07-18, the same day as
the run — a post-hoc scoring rubric, not a pre-registered one. Caught by independent skeptic
review, not by the author before writing the first draft. The SURVIVES-vs-NOT-SURVIVES
verdict is unaffected (point estimate and full CI both fail SURVIVES cleanly either way), but
the stronger "ARTIFACT-CONFIRMED" framing that depended on the un-pre-registered `<0.20`
line has been retired.

**Self-caught methodology gap during this run:** the first pass of this test controlled only
for `M_WL` (giving r=-0.6055, which would have read as SURVIVES) — that was NOT the
pre-registered criterion. Re-checked pearl_registry row 34's exact wording ("partial r(delta_M,
M_gas | M_WL, T_x)") before reporting anything, and re-ran with the correct double control.

## Skeptic Response Matrix (independent context-asymmetry review, 2026-07-18)

Per FL Step 8a, ran `Agent(skeptic)` on the first draft of this file + the script + the data,
with no session history. Verdict: **WEAKENED**, not FALSIFIED. Concerns and responses:

| Concern | Response | Status |
|---|---|---|
| Numbers not independently re-executed by the reviewer (no Bash access in that session) | Re-ran the bootstrap myself post-review: point estimate and CI both confirmed, code logic independently read as correct by the skeptic | **Accepted, addressed** — CI computed and reported above |
| "T_X drives M_hydro" is a general astrophysics fact, not verified for Mahdavi et al. 2013's specific pipeline (∂ln M_hydro/∂ln T_X not quantified) | Correct — this project has not read Mahdavi 2013's exact HSE reconstruction method in enough detail to quantify the coupling strength | **Accepted limitation** — title and verdict downgraded from "ARTIFACT-CONFIRMED" to "mechanism unresolved"; Relaxation Map item added (below) |
| A live, equally-consistent alternative exists: cluster dynamical state (relaxation/merger stage) as a COMMON PHYSICAL DRIVER of both T_X (shock heating) and delta_M (HSE-equilibrium-assumption breakdown, independent of the T_X *input* itself) — this test does not distinguish "definitional artifact" from "real physical non-equilibrium effect" | Correct, and this project's own prior work is relevant context: NR-011/NR-012 already found mass-threshold and morphology/wX do NOT mediate — but wX (X-ray centroid shift) is exactly the standard proxy for the merger/relaxation state this alternative invokes, which weakens (does not eliminate) the common-driver reading, since NR-012 already tested one operationalization of "dynamical state" and found it orthogonal | **Accepted as open, added as a named competing hypothesis below — NOT dismissed** |
| Pre-registration date claim for the `<0.20` threshold was inaccurate | Confirmed by re-reading pearl row 34 verbatim and the script's write date | **Accepted, corrected above** |
| CI (bootstrap) not computed in the original draft — point estimate alone overstates confidence | Computed: 95% CI = [-0.39, 0.27], overlapping the INCONCLUSIVE zone entirely | **Accepted, addressed** — verdict retitled to avoid implying near-zero-effect is established |

**True kill condition (per FL Step 8a) not met:** the core predicate — "the pre-registered
SURVIVES prediction is falsified" — is NOT contested by the skeptic and stands. What is
retired is the stronger, additional claim this file originally layered on top of that clean
result.

## Two competing, undistinguished explanations for r(delta_M, M_gas | M_WL, T_X) collapsing

1. **Definitional-artifact reading:** `M_hydro` mechanically depends on the temperature
   profile via the HSE formula; residualizing on `T_X` removes a derivational pathway, not
   physics. `T_X` is then a near-tautological proxy for part of `delta_M` itself.
2. **Common-physical-driver reading:** cluster dynamical state (merger/relaxation stage)
   drives both elevated `T_X` (shock heating) and larger HSE-equilibrium violations (hence
   `delta_M`) through genuinely separate physical channels — `T_X` would then be a real
   physical confound, not a definitional one, and correcting for it removes real (not
   spurious) explanatory power from `M_gas`.

**This test does not distinguish (1) from (2).** Both predict the same observed pattern.
Resolving this requires either Relaxation Map item 1 or item 2 below, not another partial
correlation on this same dataset.

## Kill Analysis

**What this KILLED:** the SPECIFIC pre-registered claim that `M_gas` alone, controlling for
`M_WL` AND `T_X`, would show `|r| > 0.40`. It does not — cleanly, with a CI that never
approaches 0.40.

**What this reclassifies (does NOT kill, but seriously qualifies):**
- **NR-011 (H1d, mass-threshold), NR-012 (H1c, morphology/wX), NR-014 (H1e, AGN/K0):** each
  remains correctly KILLED for the SPECIFIC confound it targeted — that part is unaffected.
  But none of the three controlled for `T_X`, so none can be cited (alone or cumulatively) as
  evidence the delta_M/E_ICM correlation is "unexplained by standard physics." That broader
  reading of "4/4 killed" was an overclaim before this test, and remains an overclaim after
  it — now for a documented, specific reason (T_X-degeneracy, mechanism TBD) rather than a
  vague "something might explain it."
- **What genuinely changed:** a fifth candidate explanation (T_X, via either reading 1 or 2
  above) was not previously tested. It is now tested, and is NOT eliminated — unlike
  NR-011/012/014's confounds, which WERE eliminated. This is a materially different epistemic
  state: three confounds ruled out, one live and unresolved.

**What survives unconditionally:** the raw existence of `r(delta_M, E_ICM | M_WL) ~= -0.70`
is real, reproducible, and not a coding artifact (N=50, p<1e-7, independently re-verified
this session via a fresh sub-agent re-run of the committed script, and the partial-correlation
logic independently code-reviewed by the skeptic agent). What is undermined is confidently
interpreting it as "unexplained by standard physics" — the honest state is "not explained by
the four confounds tested; a fifth candidate (T_X) is live and unresolved."

**H1b (WHIM) is NOT undermined by this finding** — WHIM thermal energy is measured in the
cluster OUTSKIRTS (R200-5xR200), a physically distinct gas phase and radius range from the
interior T_X used in M_hydro's HSE calculation, under EITHER reading (1) or (2) above. H1b
remains the one test in the H1 program structurally independent of this specific concern.

## Relaxation Map

| Variant | Changed assumption | Prediction | Status |
|---------|--------------------|-----------|--------|
| Quantify M_hydro's actual T_X sensitivity | Read Mahdavi et al. 2013's exact HSE derivation, extract effective ∂ln M_hydro/∂ln T_X for their specific XMM+Chandra combined pipeline | If leverage is low (≲0.3), reading (1) alone cannot produce r=-0.81 and reading (2) gains support; if leverage is high, reading (1) remains viable | Not tested — cheapest next step, literature-only, no new data needed |
| Cool-core/non-cool-core stratification | Split N=50 at K0≈30 keV·cm² (standard CC/NCC cut, K0 already in hand); recompute r(delta_M, T_X \| M_WL) per subsample | If the T_X-delta_M signal is similar strength in both bins → favors reading (1); if concentrated in NCC (disturbed) clusters → favors reading (2) | Not tested — cheap, one script, existing data (skeptic-proposed Test B) |
| Bootstrap-aware re-scoring | Report CI alongside point estimate for all H1-program partial correlations, not just this one | May reveal other H1a-e numbers are less statistically crisp than their point estimates suggest | Not tested — general methodology improvement, applies retroactively |
| T_X-independent M_hydro proxy | Use a mass estimate NOT derived from HSE (e.g. weak-lensing-only M_WL itself as the sole mass estimate, or a caustic mass) in place of M_hydro entirely | delta_M redefined without any T_X dependence would test whether the correlation persists under EITHER reading | Not tested — would need a fully independent second mass estimate, not in hand |
| H1b / WHIM | Independent gas phase, independent radius range, not subject to this specific coupling under either reading | r(delta_M, E_WHIM) tested per existing pre-registered criteria | NEEDS-DATA (TNG API / The Three Hundred correspondence, both pending) |

## Forbidden use

Do NOT cite this entry's retired "ARTIFACT-CONFIRMED" label — use "T_X-degenerate, mechanism
unresolved." Do NOT cite NR-011/012/014's "KILL" verdicts, individually or cumulatively, as
evidence that the delta_M/E_ICM partial correlation is "unexplained by standard physics"
without this entry's caveat. Do NOT claim the definitional-artifact reading (1) is confirmed
over the common-physical-driver reading (2) — both remain live per the Skeptic Response
Matrix. Do NOT drop the T_X-controlled number (r=-0.08, wide CI) in favor of the
T_X-uncontrolled number (r=-0.61) when citing this test.

## Correct next direction

Cheapest: the cool-core/non-cool-core stratification (Relaxation Map row 2) — existing data,
one script, directly discriminates between the two competing readings. Literature-only
alternative: quantify Mahdavi 2013's actual HSE-T_X leverage (Relaxation Map row 1). Either
is cheaper than acquiring new data, and both are more informative than repeating this test.
Independent of this branch's resolution: H1b/WHIM remains the sole test structurally immune
to the whole T_X question and should not wait on this branch's resolution.

---

*NOT-SURVIVES the pre-registered SURVIVES criterion (pearl_registry row 34) on
[VERIFIED-REAL] CCCP data (N=50). Mechanism unresolved — WEAKENED per independent skeptic
review, not FALSIFIED.*
*Full analysis script: `experiments/20260701-h1c-morphology-mass-bias/artifacts/h1c_p001_mgas_only_retest.py`.*
*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*

## Addendum (2026-09-10) — the Relaxation Map's own "cheapest, correct
## next direction" (row 2) was run: reading (1) is now favored, not
## eliminated

`experiments/20260910-nr015-cc-ncc-stratification/decision.md` ran the
CC/NCC stratification this file named. Positive control PASS (reproduces
this file's own `-0.7008`/`-0.8108` numbers exactly). The pre-registered
`K0` split itself was underpowered on this sample (only `6/45` clusters
are cool-core) — a real finding about this X-ray-selected sample, not a
test failure — but two independent dynamical-state proxies already in
the same dataset (`wX` centroid shift, `P3P0` power ratio), each with a
well-powered `~22`-vs-`23` median split, both show `r(delta_M, T_X |
M_WL)` at comparable strength in relaxed AND disturbed clusters (`wX`:
`-0.866` vs `-0.843`, Fisher `z=-0.265, p=0.791`; `P3P0`: `-0.763` vs
`-0.861`, `z=+0.912, p=0.362`) — neither shows reading (2)'s own
predicted signature (concentration in disturbed clusters). **Reading (1)
(definitional-artifact) is now favored over reading (2) (common-physical-
driver) by this test — not proven to its exclusion**, since a null
difference-test at `N=22/23` per bin has real but limited power, and the
literature-only leverage check (this file's own Relaxation Map row 1,
still unrun) would test the mechanism more directly. Do not cite this
addendum as eliminating reading (2) — cite it as "reading (1) favored,
cross-validated by two independent proxies, reading (2) not observed but
not excluded."
