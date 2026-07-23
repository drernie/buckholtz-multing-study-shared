# docs/133 — C1: Source-to-Prediction Closure Trace

**Date:** 2026-07-22
**Origin:** External adversarial re-review (HD-MAVP audit), gate decision PIVOT+NEEDS_DATA,
crucial next test "C1 Source-to-Prediction Closure." Built here with values already established
and verified this session — no new computation, a consolidation artifact.
**Purpose:** one table, one glance, showing exactly which links in the chain
`{k_A, r_A, D(z), β_d, β_q} → F_d/F_m → H_MULT(z)` are RESOLVED (real data, verified) vs
UNRESOLVED (author-undisclosed, non-identifiable, or phenomenological-not-derived).
**Status column legend:** 🟢 RESOLVED (real, verified, reproducible) · 🟡 PARTIAL (real proxy
exists but author's own convention/normalization unconfirmed) · 🔴 UNRESOLVED (author-blocked,
non-identifiable, or never independently derived).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

## The trace

| Quantity | Definition | Units | Source | Value (this pipeline) | Code consumer | Status |
|---|---|---|---|---|---|---|
| **k_A** | `E_ICM/c²`, cluster kinetic/thermal mass — TJB-confirmed 2026-06-14 voice call | M☉ | Real: MCXC/PSZ2, two independent physical paths — Path A (X-ray M_gas+T_X, `e_thermal_path_a`), Path B (SZ Compton-Y, `e_thermal_path_b`, actually used, n=548) | median k_A/M = 1.7×10⁻⁶ | `src/cluster_data_pipeline.py`, `src/pearson_fit.py` | 🟡 **PARTIAL** — real physical proxy exists and is used throughout our pipeline; but the supplementary's own **illustrative** worked example used k_A/c²=3.16×10¹² M☉, ~599× larger than the (3/2)mσ² formula it states next to it implies (external-review catch, coordinator-verified 2026-07-22) — TJB's own preferred normalization for Table A1 itself is not confirmed to match either our real-data path or his stated formula |
| **r_A** | Cluster radius (r₅₀₀) | Mpc | Real: MCXC meta-catalogue | per-cluster, real | same as k_A | 🟢 **RESOLVED** — standard, independently-cross-checkable X-ray catalogue quantity |
| **D(z)** | Inter-cluster (pair) distance, `D₀/(1+z)`, D₀=100 Mpc | Mpc | **Author-undisclosed convention** — paper's own text (§results, line ~488) explicitly labels this "a phenomenological hypothesis, not a derivation" | D₀=100 Mpc (our audit's own choice, never confirmed against TJB's) | `src/pearson_fit.py` `phi()` | 🔴 **UNRESOLVED — THE #1 untested load-bearing assumption** (deep audit, 2026-07-22): the entire Track-A edifice (R011, T4, the cosmological STOP, "MULTING≡ΛCDM@73") is conditional on this specific functional form, never independently tested or derived (Q005 HOLD) |
| **β_d, β_q** | Dipole/quadrupole coupling coefficients | dimensionless | Three independent AI-service extractions, wildly inconsistent: Claude/Table A1 (4.5, 18.0), Gemini (4.25, 8.10), ChatGPT (0.78, 0.19) — BRAI Birge Ratio R_B=15.9/24.1, p<10⁻⁴ | no single value — non-identifiable | `phi()` formula | 🔴 **UNRESOLVED** — Q004 HOLD; author's own words: derivation "remains to be determined" (facts.json, docs/122) |
| **F_d/F_m — analytical formula** | `ε = β_d[(k_A/M_Ac²)(r_A/D) + (k_P/M_Pc²)(r_P/D)]` | dimensionless (formula) | Direct algebra from the published force law | exact, formula-level | `paper/main.tex Eq.(epsilon)` | 🟢 **RESOLVED** — the formula itself is not in dispute, only its inputs |
| **F_d/F_m — for a specified pair** | Same formula, evaluated at real (k_A,r_A) with an assumed D | dimensionless (number) | Real MCXC/PSZ2 k_A,r_A + our own D₀=100 Mpc convention | median ε≈1.6×10⁻⁷ at β_d=4.5; requires β_d≳2.9×10⁵ for ε≳1% | `scripts/t4_monopole_dominance.py`, `paper/main.tex §beta` | 🟡 **CONDITIONAL** — correct *given* our D(z) convention and *given* a specified β_d; changes if either input changes (T11, commit c125179, fixed a ~30-65× illustrative-number error in this row specifically) |
| **F_d/F_m — cosmological effective value** | ε(z) as actually entering TJB's H_MULT(z) | dimensionless (function of z) | Requires D(z), β_d, β_q, and an averaging/selection rule over the real cluster population — none independently confirmed | not computable without the 🔴 rows below | — | 🔴 **UNRESOLVED** — this is the row that actually matters for the cosmological claim; do not read the 🟡 row above as settling it |
| **H_MULT(z)** | `H_anchor·√(φ(z)/φ(z_ref))` | km/s/Mpc | **Phenomenological formula**, not derived from an action/Lagrangian (Q006 open, no MULTING Lagrangian exists) | Underperforms trivial (1+z)² baseline AND monopole-only at every tested (β_d,β_q) — R011 v2-v6, T4 (2026-07-22) | `src/pearson_fit.py` | 🔴 **TESTED-AND-FAILS** (within this pipeline) — the STOP (R011/docs122 v6) is analytically proven *for this implementation*, but the D(z)/β conventions feeding it are themselves 🔴, so the STOP's scope is explicitly "this pipeline," not "any possible MULTING closure" (docs/122's own careful scoping, reaffirmed here) |

---

## Reading the table

**What is solid (🟢), independent of TJB:** r_A, and the ε *formula* itself. The statistical
verdict that this pipeline's H_MULT(z) does not beat trivial baselines is also solid, but note
the ε row's own split above — a 🟢 formula and a 🟡 conditional numeric value do not automatically
make the 🔴 cosmological-effective value resolved. **Do not collapse those three levels** —
formula-resolved, pair-conditional, and cosmologically-effective are different claims, and only
the first is unconditionally true independent of TJB.

**What is genuinely blocked (🔴), cannot be resolved by any further audit:** D(z)'s functional
form, β_d/β_q's first-principles values, the cosmological-effective ε(z), and the Lagrangian/
action generating H_MULT(z) in the first place. No amount of additional computation on real
cluster data changes this — the audit has data, not the author's closure.

**What is ambiguous (🟡) and worth a direct question:** k_A's normalization. We have a real,
defensible physical proxy (SZ/X-ray) that we use throughout; TJB's own supplementary text states
a formula (K≈(3/2)mσ², σ~1000 km/s) that, applied to his own quoted Table A1 example, does not
reproduce his own quoted number (~599× discrepancy). This is the cleanest, most concrete,
NOT_AUTHOR_ERROR-framed single question available: *"which k_A normalization did Table A1
actually use?"* — answerable in one sentence by TJB, unblocks nothing else on its own, but is the
cheapest possible confirmation to request alongside the harder D(z)/β/H_MULT(z) asks.

## Relation to the standing TJB letter draft

The Hubble-chart letter (`reply_to_TJB_EMAIL_READY.txt`, Desktop) already asks Q2 ("explicit
functional form and parameters of the red curve") — this is the H_MULT(z) row of this table,
narrowly scoped to his chart. It does **not** currently ask about D(z)'s convention, β_d/β_q's
derivation, or the k_A normalization discrepancy — those remain open, separate asks. Whether to
fold them into an expanded letter or hold them for a follow-up is a scope decision for the user,
not made here.

## Success / Kill criteria (per the external review's own framing, adopted)

**Success:** TJB supplies a single fixed formula + parameter set that (a) predicts H(z)'s shape
without per-point fitting, (b) reproduces the red/blue crossing from the model itself (not from
choosing different H₀ anchors), (c) survives held-out data, (d) uses k_A/r_A/D values consistent
with real cluster physics.

**Kill:** no such formula exists; the red curve was AI-interpolated point-by-point; D(z) was
chosen heuristically per-point; physically-consistent k_A/r_A/D make the dipole/quadrupole
negligible (already the case in this pipeline); the published chart cannot be reproduced outside
the original AI session that generated it.

---

## Formal verdict (Audit 1 of 3, 2026-07-23 — PASS / PIVOT / FAIL / NEEDS_DATA)

Per the six key questions (k_A physical meaning; D definition; are β_d/β_q constant or z-dependent;
population-averaging rule; the equation the red curve comes from; was H(z) used in choosing the
curve's form/parameters) — current status against each:

| # | Question | Status |
|---|---|---|
| 1 | What does k_A mean physically? | 🟡 real proxy used (E_ICM via SZ/X-ray); Table A1's own worked example disagrees with its own stated formula by ~599× — **open, asked directly (letter Q2/Q3)** |
| 2 | What does D mean (physical/comoving/nearest-neighbour/averaged)? | 🔴 **NEEDS_DATA** — never stated by TJB; our D₀/(1+z)=100 Mpc is our own audit convention, not his |
| 3 | Constant β_d, β_q, or z-dependent? | 🔴 **NEEDS_DATA** — three AI-service extractions disagree 5.8×/95× (BRAI R_B=15.9/24.1); no z-dependence specified anywhere |
| 4 | Population-averaging rule over the cluster sample? | 🔴 **NEEDS_DATA** — never specified; our pipeline uses per-cluster φ(z), no stated averaging rule from TJB |
| 5 | What equation generates H_MULT(z)? | 🔴 **NEEDS_DATA** — no action/Lagrangian exists (Q006 open); the published curve's exact form is unknown to us — **this is letter Q1, the single most direct ask** |
| 6 | Was H(z) used in choosing the curve's form/parameters? | 🔴 **NEEDS_DATA** — cannot be determined without TJB; explicitly asked (letter Q1) |

**Overall C1 verdict: NEEDS_DATA**, closer to PIVOT than FAIL. Reasoning: nothing found this
session shows the closure is impossible (no contradiction proving no formula can exist) — but
nothing found shows a fixed, non-fitted formula DOES exist either. Every one of the six links
that would need to resolve to PASS depends on information only TJB has. This is the honest
midpoint the external review's own framing predicts for "the branch is real, but not yet
theory-closed" — **not a verdict this audit can move further without a reply**.

**What would flip it:**
- → **PASS**: TJB supplies fixed D(z)/β_d/β_q/averaging-rule + confirms H(z) points were NOT used
  in building the curve, AND the resulting formula survives held-out CC data.
- → **PIVOT** (phenomenological, not first-principles): TJB confirms the curve is a genuine
  fit-to-data exercise (consistent with his own July-6 framing) — downgrades the cosmological
  branch from "candidate fundamental theory" to "reconstructible phenomenology," which is still
  a legitimate, testable object (feeds directly into Audit 3's fair model comparison).
- → **FAIL**: no fixed formula exists at all, or D(z)/β were chosen per-point to match H(z).

---

*This table is a consolidation, not new evidence — every cell traces to an artifact already
committed this session (commits 4196f9a through af3d5c4) or to facts.json/docs/122. No
independent verification beyond what those artifacts already carry.*
