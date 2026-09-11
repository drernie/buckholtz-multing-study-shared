# 161 — Thermal-pair kSZ fingerprint: from repo audit to a real observational test

**Date:** 2026-09-11. **Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` ·
`OUR_RECONSTRUCTION` · `NO_AUTHOR_ERROR`.
**What this file is:** a strategic synthesis of the whole
`20260911-thermal-pair-fingerprint` branch's journey, written by the
user, spot-checked against the repo by an independent read-only agent
pass (not this project's usual Step 8a skeptic — a narrower factual
verification of a narrative summary), and preserved here because it
does not otherwise exist anywhere as a single document — every step
below lives in its own `FINDING_*.md`/`null_results/*.md`, but the
throughline connecting them was, until now, only in conversation.
**Why this belongs in `docs/`, not only in chat:** exactly the failure
mode `CURRENT_EVIDENCE_STATE.md` itself names repeatedly (§6a, §7a —
"real work sitting disconnected from its own index") — a narrative this
good should not exist only as something someone remembers correctly.

---

## Verification note (before trusting the table below)

Per `method_verify_pasted_ai_reports.md`'s standing discipline in this
project, the 23-row table was independently spot-checked against real
files, not accepted at face value. Rows 14-23 were already personally
`[VERIFIED]` this session (executed directly). Rows 1-13 (pre-session
history) were checked by a separate read-only agent pass against actual
source files. Result: **4 of 5 spot-checked pre-session claims CONFIRMED
verbatim against source**, 1 partially confirmed with two precision
corrections, noted inline below rather than silently absorbed:

- **Row 3:** the literal phrase **"PARKED BY DESIGN" does not appear in
  the repo** (0 grep hits) — the actual verdict in `docs/158_provenance_
  modules_park_decision_20260907.md` is simply **"PARKED."** The
  substance (re-audit found it was a deliberate decision, not a
  forgotten integration; real open debt is a `namespace`/`meaning`
  field missing from `ProvenanceTag`) is confirmed accurate — only the
  three-word label was an embellishment.
- **Row 6:** "old branch checked a smooth trajectory, new one checks
  real population geometry" is a paraphrase, not a verbatim quote. The
  actual source (`experiments/20260911-thermal-pair-fingerprint/
  claim.md` §1.2) contrasts *"the model's own smooth mean z-trajectory
  (one point per z)"* (closed branch) against *"real, individual
  cluster pairs, with their own measured scatter around that mean"*
  (new branch) — same substance, different wording. The "07-09"
  shorthand itself is confirmed verbatim (`pearl_registry/INDEX.md`:
  *"the closed 07-09 branch's own floor"*, referring to
  `experiments/20260907-icm-expansion-correlation`).

Everything else in the table checked out exactly, including the Eq.32
number correction itself (`0.0135%→0.0608%, 1.00σ`, PDG 2024 correction,
`CURRENT_EVIDENCE_STATE.md:35-36`).

---

## The 23-step journey

| # | Step | What was done | What was learned | Status | Scientific value |
|---|---|---|---|---|---|
| 1 | Initial repo audit | Checked claims, code, provenance, CI, statuses, scope of conclusions | Repo is disciplined overall, but `VERIFIED` cannot be accepted automatically | DONE | Built a reliable initial map of what can/can't be trusted |
| 2 | Eq.32 audit | Found discrepancy `0.0135%` vs a real run giving `0.0608%, 1.00σ` | A canonical status file fell out of sync with the code after a PDG input changed | FIXED / incident preserved | Real found bug in status propagation; demonstrates the audit process's own value |
| 3 | Audit of the audit itself | Re-checked the claim about `conflict_resolver`/`source_provenance` | Not a forgotten integration — a deliberate **PARKED** decision (not "PARKED BY DESIGN," see correction above); real open debt is namespace/symbol provenance | CORRECTED | Even the critic was subjected to falsification |
| 4 | Strategy change | Moved away from "fit `H(z)` even better" | `H(z)` is too integrated/weakly-discriminating an observable | DONE | The single biggest strategic improvement to the whole line of work |
| 5 | Thermal-pair fingerprint | Isolated `ξ=KR/(Mc²s)` from the force law and the MULTING correction's shape | The theory makes a specific pair-level prediction depending on thermal content and separation | ALGEBRA VERIFIED | A direct potential test of the mechanism, not just a cosmological fit |
| 6 | Link to the old branch | Compared the new idea against the closed 07-09 branch | Not a duplicate — old branch tested a smooth trajectory, new one tests real population geometry (paraphrase, see correction above) | NOVEL WITHIN PROJECT | Legitimate reopening of the question via a new observable |
| 7 | Crossing / turnover | Checked roots and steepness of the MULTING template | A genuinely sensitive region exists; symmetric crossing and the shape's maximum are different things | VERIFIED algebraically | Gives a pre-specified fingerprint that can be attacked |
| 8 | Claim → estimand → DAG | Separated predictive claim C1 from causal claim C2; built a DAG | Real confounder threats found: `G→τ`, merger state, selection, velocity history | DONE | Removed the risk of calling an ordinary correlation "new gravity" |
| 9 | Temporal problem | Noticed MULTING gives acceleration, kSZ gives velocity | Today's `K` cannot be directly compared to today's `v` without a dynamical bridge | IDENTIFIED / controlled in design, not physically solved | A substantive conceptual correction |
| 10 | Data check | Checked ACT/DESI/eROSITA and Gong et al. | Per-object `τ`/`v` from the key kSZ paper are not publicly released | VERIFIED constraint | Determined a real acquisition strategy instead of an imagined one |
| 11 | Data-acquisition plan | Costed options A/B against real resources | Either request unpublished object-level products, or build a classical kSZ estimator | DONE | The price of the next experiment is now known |
| 12 | Scale error | Caught use of `s_0~30 Mpc` instead of the frozen `d_0=45 Mpc` | A real provenance error | FIXED | Another case where verification changed a scientific conclusion |
| 13 | Exact Pair Census | Used the real ACT-DR5 MCMF catalog and real RA/Dec/z instead of a Poisson mock | Real population geometry differs from the idealized model | DONE | Moved from an imagined catalog to real sky structure |
| 14 | Killed the window design | Scanned window widths around 45 Mpc | Neither statistics nor cluster clustering singles out 45 Mpc as a special observable scale | REFUTED / NR-025 | A genuine negative result: a bad design was eliminated |
| 15 | New continuous design | Assigned each real pair its own `ξ_pred(z,s)` and `S_M` | No artificial window; uses the full shape of the prediction | ACTIVE DESIGN | An order of magnitude better as a falsification test |
| 16 | Positivity | Found, on real `(z,s)`, pairs the frozen model places above crossing | 306/7693 in the original pool, then ~4.7% in the SUTVA-disjoint variant | SUPPORTED | Shows the predicted region is not empty in real geometry |
| 17 | Beam blending | Checked all 306 crossing candidates by angular separation | Only ~1.6% fall in the risk zone; excluding them barely changes the result | THREAT MOSTLY CLOSED | One obvious instrumental counter-argument mostly closed |
| 18 | Stricter shape gate | Required the correct non-monotonic shape, not just a good fit | Power dropped from ~98.6% to ~60% | DONE | The test became harder to pass by accident |
| 19 | SUTVA/dependency audit | Checked cluster reuse across pairs | 43.2% of old sampled pairs shared a halo — a real structural bug | FOUND AND FIXED | A very important statistical-design correction |
| 20 | Disjoint matching | Built pairs without halo reuse, sampling without replacement | Corrected synthetic power ≈ **59.1%** for the chosen scenario | PROVISIONAL POWER | Power of the now-correct estimand — still synthetic |
| 21 | Four-world battery | Ran MULTING / optical-depth-confounded / merger-confounded / null | The synthetic pipeline distinguishes all four operationalized worlds; false-promotion of rivals ~0 | ADEQUATE, with scope caveat | The last major pre-data oracle test passed |
| 22 | Real-data request | Sent Gong/Bean a request for object-level products | Fork 1a open | AWAITING RESPONSE | Possibly the cheapest path to a real test |
| 23 | Fork 1b, Phase 1 | Built + validated the classical pairwise-kSZ estimator math on synthetic data | Estimator (Hand et al. 2012) implemented correctly — independent context-blind review CONFIRMED, no sign/index bugs | PHASE 1 DONE, Phase 2 (real map + catalog) OPEN | Independent path if data isn't granted; de-risked the math before the expensive real-data phase |

(Row 23 updated from the user's original "not started" — Fork 1b Phase 1
was completed the same day this synthesis was requested; see
`pairwise_ksz_estimator.py` + `FINDING_pairwise_ksz_estimator_phase1.md`.)

---

## What specifically is new here

The important result is not the `59.1%` number.

**Before**, the position was roughly: *"MULTING somehow describes
`H(z)`; it's unclear how to directly test its additional force."*

**Now** it is: **there is a concrete pair-level fingerprint of MULTING,
a frozen predictor, a real cluster population that falls into the
regime of interest, and a pre-specified estimator that can be applied to
real data.**

That is a large transition. Two things were learned along the way that
were not known at the start:

1. **The fixed ~45 Mpc window was a bad idea.** The data itself does not
   pick out that scale. The idea was not rescued by tuning the window —
   it was killed and registered as a negative result (`NR-025`).
2. **Using each pair's own real `s`, the MULTING template genuinely
   places part of the existing cluster population in the strong-
   nonlinearity/crossing region.** The "interesting regime" turned out
   not to be a purely formal point in the equation.

This is new knowledge *within this project*, not merely repackaged.

## Is there scientific novelty here?

Three levels, kept separate deliberately:

**1. Novelty relative to this project — yes, unambiguously.** The
continuous thermal-pair fingerprint, the real-pair census, killing the
window design, and checking the crossing population are a branch that
did not exist before.

**2. Methodological novelty — likely present.** Not just "look at kSZ,"
but a specific chain:

```
frozen MULTING force -> S_M(z,s) -> real cluster pairs ->
specific turnover/crossing signature -> rival-world rejection
```

This is substantially more concrete than the generic claim "kSZ can
test modified gravity."

**3. International priority claim — no basis yet.** No systematic
prior-art search has been run on the specific question: *has a test of
MULTING's specific `K/M/R/s` dependence via thermal-SZ + pairwise-kSZ
cluster dynamics been published before?* Safe to say: **a new test
design developed within this project.** Not safe to say: "first such
test proposed in the world." (A dedicated novelty check, per this
project's own Falsification Ladder Steps -4/-3, remains a real, cheap,
not-yet-done next step if a priority claim is ever wanted.)

## How close is this to proving MULTING?

On a ladder: *idea → mathematical prediction → falsifiable test →
synthetic validation → real observational test → independent
replication → mechanistic theory.*

This branch started between the first and second rung. **It now stands
immediately before the real observational test.** That is real
progress — but even a positive thermal-pair result would prove, at
most: *the data support this specific frozen MULTING force fingerprint
better than the alternatives considered.* It would **not** automatically
establish the full IDM construction, the six isomers, the cosmological
`H(z)` bridge, the fundamental origin of `β₁,β₂`, covariant completion,
or the absence of every other explanation. This matches this project's
own standing rule (`docs/151_status_separation_rule.md`): a local PASS
is never silently promoted to a global headline.

## What remains (thermal-pair branch specifically)

1. Get object-level Gong/ACT-DESI products **or** finish building the
   own kSZ estimator (Fork 1b Phase 2).
2. Do a real cross-match of the needed observables and footprint, not a
   linear area-scaling approximation (`data_acquisition_plan.md` Fork 2).
3. Get real `K,M,R` (or admissible proxies) and their uncertainty model.
4. **Freeze code and criteria before looking at the result** (this
   project's own Step 2b/Oracle-Adequacy discipline, already largely in
   place via the four-world battery — the real-data run needs the same
   freeze applied to real inputs).
5. Run the test on real kSZ/tSZ/lensing/X-ray data.
6. Do not change `β`, `S_M`'s shape, cuts, or the PROMOTE criterion after
   seeing the result.
7. After the result: blind/independent reproduction.

After that, an honest answer becomes possible — **SUPPORTED / REFUTED /
INCONCLUSIVE** — for the frozen thermal-pair MULTING prediction
specifically. Not for MULTING as a whole.

## In one sentence

**Started with a repository audit and status-file bug-hunting; ended
with building, attacking, repeatedly breaking, and fixing a concrete
observational experiment capable of testing a specific fingerprint of
MULTING's force on real galaxy clusters.** The theory is not confirmed.
It is, however, **substantially more testable than it was at the
start** — arguably the main scientific product of this entire line of
work.
