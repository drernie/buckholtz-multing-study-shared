# docs/122 — Bottleneck Synthesis & Cosmological-Branch Verdict

**Date:** 2026-07-12
**Status:** SYNTHESIS — cross-checks an external "top-10 bottleneck" adversarial audit
against this project's own accumulated evidence (facts.json, R001-R011, Q001-Q006).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR

## Source

User-supplied external audit (2026-07-12, not this project's own text) prioritizing 10
structural bottlenecks in the MULTING/IDM program, with a proposed first cheapest test
(max F_d/F_m, max F_q/F_m on real cluster data, frozen criterion: F_d/F_m<1 everywhere
admissible -> STOP for the cosmological branch).

## Cross-check result: this is confirmatory, not novel, for 8 of 10 items

| # | Bottleneck | This project's existing evidence |
|---|---|---|
| 1 | No action/Lagrangian | = Q006 (OPEN). Candidate template found (Blanchet & Le Tiec 2008, arXiv:0804.3518), not completed. |
| **2** | **Dipole/quadrupole cannot dominate** | **= R011, already measured**: F_d/F_m ~ 6e-6 on real MCXC cluster data (M500, R500, k_A), no H(z) fitting involved. Independently confirmed by an earlier external audit's own T1 test this session (same order of magnitude). |
| 3 | No force->H(z) mapping | = Q005 (HOLD, "BETA-1 HOLD blocks numerical bridge"). Also directly confirmed today by the LLM-consensus pilot (S1: a blind model self-flagged exactly this gap as one of 7 missing specifications; experiments/20260712-llm-consensus-verification/). |
| 4 | beta_d/beta_q physically undefined | = Q004 (HOLD), same wording: "first-principles values ... waiting for TJB response". |
| 5 | Covariance / conservation not proven | Not separately tracked before; a real, derivative consequence of #1 (no action -> no Noether currents to check). Genuinely adds a named checklist item. |
| 6 | PPN / equivalence principle not checked | `docs/29_ppn_quick_check_requirements.md` exists (scoped, not executed). Partially new — flags this as still-open, not previously closed out. |
| 7 | No multi-body/continuum dynamics | Derivative of #3 (Q005); not separately tracked. |
| **8** | **N=5 does not imply Omega_DM/Omega_b=5** | **External document is incomplete here.** Q006's `cross_domain_3runs_2026_07_09` note already found a partial, self-consistent resolution: unequal isomer masses, m_bar=1.074 m_p, gives 5 x 1.074 = 5.37 ~ 5.36 (matches Planck/DESI N_opt). This is an ASYMMETRIC-DM-class answer competing with mirror-DM (Berezhiani), not refuted — see also `boyko_specialist_DDM_2026_07_09` on the mirror-DM/proton-mass literature (arXiv:2512.14119). |
| **9** | **IDM thermal history / N_eff not set** | **= R005/EXP-O, already done**: Delta_N_eff = 15-81 for pure SM-thermal 5-sector history, vs Planck N_eff=2.99+-0.17 -> excluded at 130-477 sigma. MSSM-style g*S variant brings it into a testable-but-not-yet-excluded range (Simons Observatory, pearl_registry 2026-06-21). |
| 10 | No full microphysics / unique signal | Consistent with this project's own long-standing framing (README: "IDM is a class of possible specifications, not a single model"). |

## The proposed "first cheapest test" is not a new step — it has already been run

The external document's own recommended first action (max F_d/F_m, F_q/F_m on real,
non-cosmology-fitted cluster data) is **item #2 above, already computed** (R011,
`code/beta_rescaling.py`, `src/pearson_fit.py`). No new computation is required to
apply their own frozen criterion.

## Applying their own frozen criterion — with one necessary correction

Their criterion as stated: *"if F_d/F_m < 1 in the entire physically admissible region,
the MULTING cosmic-acceleration mechanism does not work; STOP for the cosmological
branch."*

**Checked before accepting this:** does an independently-derived upper bound on
beta_d/beta_q exist anywhere in this project, separate from fitting Table A1 or H(z)?
`grep`-searched `src/`, `docs/` for any such bound — **none exists**. beta_d/beta_q
remain fundamentally undetermined (Q004, bottleneck #4/#1). This means "the entire
physically admissible region" is not itself defined yet — the criterion cannot be
applied as a strict all-parameter-space proof.

**Corrected, honest form of the same criterion:** F_d/F_m < 1 (by 4-6 orders of
magnitude) at **every beta_d, beta_q value anyone has proposed so far** — all three
AI-service outputs (ChatGPT 0.78/0.19, Claude/Table A1 4.5/18.0, Gemini 4.25/8.10),
the grid-search optimum (~10 at saturation), and today's independent Codex pilot
(beta_q=8.25 at full specification). None come remotely close to the ~10^2-10^6 scale
that would be needed for F_d/F_m to reach 1 on real cluster scales (epsilon = k/mc^2 ~
1.7e-5 to 1e-2 for realistic cluster velocity dispersions).

## Verdict (Kill Analysis, per this project's own falsification-ladder.md discipline)

**What this kills:** the specific claim that MULTING's dipole/quadrupole terms, evaluated
with any beta_d/beta_q value proposed to date (fitted, AI-reported, or grid-searched),
dominate the monopole term at real cluster scales and thereby drive the cosmic-acceleration
mechanism as currently specified. This branch is **STOPPED pending bottleneck #1**
(an independent derivation of beta_d, beta_q from an action/Lagrangian that is not itself
fit to Table A1 or H(z) data).

**What this does NOT kill:**
- The MULTING dipole/quadrupole force LAW itself as a mathematical object (untested at
  the yet-undetermined beta scale where it could plausibly matter).
- The IDM isomer postulate generally — item #8's partial resolution (asymmetric masses)
  remains a live, self-consistent, non-refuted candidate.
- Eq.32 (R001) — explicitly out of scope; the external document itself notes Eq.32 is
  "not a solution to these bottlenecks," a numerical relation independent of the MULTING
  force-law/cosmology branch. No change to Eq.32's own status (rank #2/132,000, 1.00 sigma,
  4/3 origin still open per Q001).
- The possibility that a future, independently-derived beta (solving bottleneck #1/#4)
  could land in the O(10^2-10^6) range needed for F_d/F_m ~ 1. Nothing in this project
  rules that out a priori — it has simply never been proposed by any source checked so far.

**Relaxation map (what would revive the cosmological branch):**
1. An action/Lagrangian (bottleneck #1) that independently derives beta_d, beta_q
   without reference to Table A1 or any H(z) fit.
2. If that derivation yields beta values in the O(10^2+) range (vs. all currently
   proposed O(1-10) values), re-run the F_d/F_m, F_q/F_m scale test with the derived
   values — this is the correct cheapest differentiating test for that scenario.

## What this synthesis does NOT do

- Does not claim TJB made an error (NOT_AUTHOR_ERROR) — the preprint itself already
  states beta_d, beta_q are "AI-assisted thought experiment" outputs and defers the
  full field-theory treatment to future work; this document formalizes what follows
  from that admission plus real data, not a hidden mistake.
- Does not make any public claim (NO_PUBLIC_CLAIMS) — internal project synthesis only.
- Does not extend to IDM's isomer/dark-matter postulate as a whole, only to the specific
  MULTING dipole/quadrupole cosmic-acceleration mechanism at currently-proposed beta.

## Source data

R011 (`facts.json`), R005 (`facts.json`), Q004/Q005/Q006 (`facts.json`),
`experiments/20260712-llm-consensus-verification/`, `code/beta_rescaling.py`,
`src/pearson_fit.py`.
