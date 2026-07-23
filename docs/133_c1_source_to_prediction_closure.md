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

## Appendix A1 self-consistency check (2026-06-09 finding, re-verified 2026-07-23)

**This section did not exist when this document was first written on 2026-07-22 — it was found
during today's C1-R follow-up and folds in a result that predates this whole trilogy by six
weeks, was never previously cross-referenced into docs/133, and is materially stronger evidence
for the H_MULT(z) row's 🔴 status than anything in the trace table above.**

**Source:** `audit/self_consistency_diagnostic.py` (2026-06-09), re-run and independently
hand-verified 2026-07-23 (one z-value recomputed by hand from the raw formula, matched to 2
significant figures; H_MULT/H_FLRW/β_d/β_q inputs cross-checked line-by-line against the raw
source, `data/supplementary_extracted/claude_approximate_matches.csv` — exact match). This test
uses TJB's own v6-preprint Table A1 (12 rows, z=0–8.5) and TJB's own stated bridge formula
`H²(z)/H²_anchor = Φ(z)/Φ(0)`, `Φ = m_A/D² − 2k_Aβ_dr_A/D³ + (k_Aβ_qr_A)²/D⁴` — the exact same
formula `src/pearson_fit.py` uses throughout this trilogy.

**Provenance split (important, a skeptic pass this session caught an earlier draft blurring this):**
- β_d=4.5, β_q=18.0 — **from Table A1 itself**, machine-readable, [VERIFIED-BASH] against the raw CSV.
- m_A, k_A, r_A, D per row — **not from Table A1**; reconstructed (2026-06-09) as geometric means
  of ranges described in the PDF's accompanying text. Their transcription fidelity against the
  original PDF was **not** independently re-verified today — inherited, not re-checked.

**Two-tier evidentiary split (user correction, 2026-07-23 — the original single-tier framing
overclaimed the exact number; corrected here, do not revert):**

### M1 — CONFIRMED (from the raw CSV, unconditional)

`H_MULT ≈ 1.074 × H_FLRW`, scatter 2.6%, corr=0.9996 — [VERIFIED-BASH] against
`data/supplementary_extracted/claude_approximate_matches.csv` directly, no reconstructed inputs
involved (only the table's own H_MULT and H_FLRW columns).

```
Table A1 H_MULT is nearly a rescaled H_FLRW column   — CONFIRMED
Independent redshift-shape signal in Table A1        — NOT DEMONSTRATED
Reason or intent behind this construction            — UNKNOWN
```

**Do not write** "the AI service just rescaled ΛCDM" — the numbers show near-scaling, they do
not establish the AI service's intent or exact procedure. Say "numerically close to a constant
rescaling," not "was rescaled."

### M2 — ROBUST DIRECTION, CONDITIONAL EXACT MAGNITUDE

Φ(z) computed from the bridge formula + reconstructed cluster parameters **decreases** from
z=0→8.5 while Table A1's own reported H_MULT **increases** — opposite trends. The *direction* of
this mismatch is robust (survives the geometric→arithmetic representative-value swap, Part F).
The *exact* ×4365 magnitude at z=8.5 is **conditional**: it depends on cluster parameters
(m_A, k_A, r_A, D) reconstructed from PDF-text ranges (2026-06-09), not read from an unambiguous
Table A1 row, and their fidelity against the original PDF was not independently re-checked today.

```
Bridge reconstruction gives opposite redshift trend   — ROBUST INDICATION
Exact ×4365 discrepancy                                — CONDITIONAL (depends on reconstructed inputs)
Cluster-input transcription from PDF                   — NEEDS SOURCE-FIDELITY RECHECK (not done)
```

M3 (dataset-independent, Gemini cross-check) and the Part F robustness swap (×4365→×3944 under
geom→arith) both still stand as supporting M2's *direction*, not as certifying the *exact number*.

### The critical contradiction this reveals (2026-07-23, likely the most valuable single result of this whole check)

M1 and the July-20 chart are, on their face, **mutually inconsistent**. If H_MULT is (per M1)
numerically close to a *constant* rescaling of H_FLRW, the two could not produce a curve that
*crosses* H_FLRW/ΛCDM — a constant ratio between two curves never crosses zero difference more
than once (in fact never, if the ratio stays >1 or <1 throughout, as M1's 1.02–1.11 range does).
Yet the July-20 chart's red and blue curves visibly cross near z≈1.6–1.7 (already the basis of
letter Q1). **This is a clean logical deduction from M1 alone — it does not depend on M2's
conditional cluster-parameter reconstruction, so it survives even if the ×4365 number does not.**

At least one of the following must be true:
- the July curve is built by a different/revised procedure than produced Table A1's H_MULT column;
- a different H_FLRW/Ωm baseline or normalization was used for the July chart;
- an additional redshift-dependent step was applied after whatever produced Table A1;
- the July chart is a new phenomenological reconstruction, not a direct extension of Appendix A1.

```
Table A1 and the July-20 chart are probably NOT the same computational procedure — LIKELY
```

This reframes the open question from "how was the bridge closed" to something sharper and more
answerable: **is the July figure the same calculation as Appendix A1, or a revised one?** — this
is now folded into letter Q1 (2026-07-23 update, v10).

### CORRECTION 2026-07-24 — the gate below checked the wrong document; retracted where wrong

**The user caught this, and was right.** Everything below this note was based on reading
`data/source_material/buckholtz_preprints202511.0598.v6_pymupdf-clean.md` (the main paper) alone.
That file explicitly says the actual AI-service working (the formula, the typical-value
derivations, the full Table-A1-generating computation) lives in **Supplemental Material [251]** —
a SEPARATE document, already digitized in this repo at
`data/source_material/buckholtz_supplementary202511.0598.v6.md` (1602 lines), which was **not
checked** before writing gate item 4's "DOES NOT EXIST IN SOURCE" verdict below. This is exactly
the "read the full call chain, not one file" failure audit-verification-gate.md warns about —
committed by the same session that wrote that rule.

**What the supplementary transcript actually contains, verified by direct read
(lines 1127–1335 and 560–639), not grep snippets:**

- **The Φ(z)/Φ(z_anchor) formula is real, explicit, and attributed to Claude** (dated 2026.05.07,
  "MULTING study via Claude"): `H²(z) = H²_anchor × [Φ(z)/Φ(z_anchor)]`, `Φ(z) = A_m(z) − A_d(z) +
  A_q(z)`, with `A_m, A_d, A_q` spelled out term-by-term (lines 1201–1207) — this is not "our
  interpretation," it is the literal source text, verbatim.
- **A full "Galaxy Cluster Parameters" table exists** (lines 1127–1158): explicit ranges for
  `m_A, r_A, D_C:AB, k_A/c²` at all 12 time points — e.g. at z=0: `m_A∈[1e14,1e15]`,
  `r_A∈[1.0,3.0] Mpc` (a **radius** range, stated as such — the earlier "diameter-vs-radius"
  transcription concern below turns out to be a false alarm, this really is the radius range),
  `D_C:AB∈[20,100] Mpc`, `k_A/c²∈[1e12,1e13]`.
- **The exact method for turning ranges into single numbers is stated**: "geometric means of
  log-ranges for m_A, k_A; arithmetic means for r_A, D_C:AB" (line 1252–1253), with the resulting
  typical values given explicitly at z=0 (`m_A=3.16e14, r_A=1.7, D=50, k_A/c²=3.16e12`) and a full
  `r_A(z)` trend across all 12 points (1.7→0.15 Mpc). D_C:AB(z)'s own trend is derivable from the
  same range table but was not extracted here.
- **β_d=4.5, β_q=18.0 are not arbitrary** — the transcript states the explicit optimization
  criteria used to find them (line 1216–1223): quadrupole must dominate at z>2, dipole must
  dominate at z<0.5, and subject to that, minimize RMS σ_MULT against H-data. Table A1's H-MULT
  column, σ_MULT values, and β's all match this transcript exactly — **Table A1 = this Claude
  transcript's output**, not a mysterious black box.
- **A second, genuinely different procedure exists too, attributed to ChatGPT** (dated
  2026.05.07): before settling on anything, ChatGPT explicitly listed 4 candidate force→H(z)
  mappings (Newtonian-shell `D̈∝F/M`; energy-balance; phenomenological `H²∝⟨FD⟩`;
  effective-fluid) and asked TJB which to use (lines 566–586); TJB specified "Newtonian
  approximation"; ChatGPT then used `D̈ ≈ F_oP/m_eff`, `H ≈ Ḋ/D` (lines 588–639). This is real,
  not fabricated — the user's correction on this point (in the previous turn) was correct, and
  my own dismissal of it as an unverified "phantom source" claim was wrong.

**What this means for the M1/M2 findings and the "gate," corrected:**

- **Gate item 4 ("normalization does not exist in source") — RETRACTED.** It exists, twice, each
  attributed to a specific named AI service, each internally documented in detail.
- **Gate item 1 ("no canonical range exists") — PARTIALLY RETRACTED.** A real, explicit range
  table exists (above). What remains genuinely open is only *which* typical-value choice (this
  transcript's geometric/arithmetic split, a different one, or TJB's own independent judgment)
  corresponds to what actually generated the plotted red curve on the July-20 chart specifically
  — a different, later artifact than this May transcript.
- **M2 (the June self-consistency reconstruction, ×4365 gap) — re-scoped, not re-validated.** The
  June script's own typical values (geometric mean for r_A and D too, D0=100 fixed) do not match
  what this transcript actually specifies (arithmetic-ish mean for r_A/D, D=50 at z=0, not 100).
  Given Table A1 was *generated by* this exact transcript's procedure, a correct re-implementation
  of it will trivially reproduce Table A1 well (the transcript itself reports |σ_MULT|<0.5
  throughout) — so the ×4365 finding says something about **the fidelity of the June
  reconstruction to this transcript**, not about whether TJB's own procedure is self-consistent.
  The genuinely open, still-unresolved question is whether *our own real MCXC/PSZ2 cluster data*
  (used throughout R011/Audit 3) is consistent with these typical-value ranges, and whether our
  D(z)=D0/(1+z) convention matches this transcript's D_C:AB(z) trend — neither re-checked here.
  **Do not cite the ×4365 number or "opposite direction" framing as established until this
  re-check is actually done** — same caution as before, now for a more precise reason.

This correction does not restore M2's earlier "robust direction" status — it removes the basis
for evaluating M2 at all until it is re-run against the real transcript values, which is now
possible and comparatively cheap (the full parameter table exists in-repo) but was not done
today. M1 (`H_MULT≈1.074×H_FLRW`) is fully unaffected by any of this — it never depended on the
formula's existence or provenance.

---

### Source-fidelity gate — RUN 2026-07-23 (direct read of Appendix A.1, pp.32–38 of the v6 PDF)
**[Superseded in part by the correction above — kept verbatim for the record, do not delete.]**

Run against `data/source_material/buckholtz_preprints202511.0598.v6_pymupdf-clean.md`, lines
2090–2578 (Appendix A "Using MULTING to calculate the Hubble parameter H(z)", the full A.1
prompt-text, A.2, A.3, and Table A1's own caption). Page/line-cited, not memory.

| # | Gate item | Result |
|---|---|---|
| 1 | Confirm (M_A,k_A,r_A,D) ranges as stated | **FAILS AS SPECIFIED — no canonical range exists.** The PDF (Step 4, "Galaxy Cluster Parameters") instructs the AI service to *generate its own* ranges ("Explain how you found, chose, or estimated the values") and explicitly grants discretion (Step 5: "use your discretion about how to choose... typical values"). Appendix A.3 confirms services' ranges "disagreed somewhat." Section 4.2's general background text (line 1400: "Diameters of 1 to 3 Mpc," "separations... 20 to 90 Mpc") is **not** stated as the per-z input table — and even taken as a loose match, the June reconstruction used the 1–3 Mpc **diameter** range directly as a **radius** range (r_A=1.73=geom(1,3), no ÷2), and used a separation ceiling of 100 Mpc where the text says 90. Both are concrete, found-today transcription risks, not resolved by this gate. |
| 2 | Why geometric mean | **PARTIAL PASS.** The PDF itself uses "geom.mean.mass" as its own convention elsewhere (line 955, quark-mass tables) — geometric mean is a precedented choice in this document for range→representative-value, though not proven to be what the Claude service specifically did for cluster parameters. |
| 3 | Sign convention `F_m − F_d + F_q` | **CONFIRMED, verbatim.** Lines 2226–2239: monopole attracts (`F_m=Gm_Am_P/r²`), dipole **repels** (`F_d`, subtracted), quadrupole attracts (`F_q`, added); `F_oP = F_m − F_d + F_q` stated exactly. `r_dA=β_d·r_A`, `\|r_qAB\|²=β_q²·r_A·r_P` also confirmed verbatim (line 2312) — matches this project's φ() formula structure exactly. |
| 4 | Normalization `Φ(z)/Φ(0)` matches PDF | **DOES NOT EXIST IN SOURCE.** The PDF gives no H(z)-combination formula at all — only qualitative design constraints (item below) and "feel free to use any or all the information... try to avoid using FLRW/ΛCDM outputs." Our `Φ(z)/Φ(0)∝H²` convention (used throughout `src/pearson_fit.py`/R011, and in the June self-consistency script) is **entirely this project's own interpretation**, not sourced from TJB's text. This confirms and sharpens the H_MULT(z) row's existing 🔴 status — not just "not derived," but literally not attempted by the source prompt. |
| 5 | Does Appendix A1 share a calc version with the July-20 chart | **Not resolvable from the PDF alone** (dated 21 May, two months before the chart) — this is exactly what the new Q1 addition asks TJB directly. |

**New finding from this gate run, not previously known — materially affects M2:** Step 5 (line
2337–2340) gives the AI service an explicit **design constraint**: *"Ensure that quadrupole
attraction dominates at high redshift. Ensure that dipole repulsion dominates at low redshift."*
Whatever cluster parameters actually produced Table A1 must satisfy this ordering by construction.
The June reconstruction's own Part D found **quadrupole dominates at every tested z, including
z=0** (ε_q≈1.5×10⁹ at z=0) — the opposite of the low-z regime TJB required. This is a concrete,
identified reason the June reconstruction's cluster-parameter choice likely does **not** represent
whatever parameters the real Claude-service run actually used to satisfy this constraint.

**Verdict on M2, downgraded from the previous revision:** the reconstruction is a **valid
demonstration that a naive/literal application of the stated force law, using generically-derived
cluster parameters that do not enforce the low-z dipole-dominance requirement, fails badly** — but
it is **no longer a reliable claim about what the real Table A1-generating process would show**,
because it likely used a different parameter regime by design. Both the exact ×4365 figure and
the qualitative "opposite direction" framing should be treated as **illustrative of a naive
attempt, not evidence about TJB's actual process** — this is a stronger downgrade than the prior
revision's "conditional magnitude, robust direction."

**What remains solid and independent of all of this:** M1 (`H_MULT≈1.074×H_FLRW`, corr=0.9996) —
untouched by any cluster-parameter question, since it uses only Table A1's own two reported
columns. **New, fully author-sourced corroboration found this gate run** (Appendix A.3, lines
2511–2518, TJB's own words, no reconstruction needed): *"The services reported somewhat different
ranges of values regarding... masses of galaxy clusters, radii of galaxy clusters, and distances
between neighboring galaxy clusters... Disagreements regarding values, that the services
suggested, for βd and βq were noticeable. Disagreements between values, calculated via MULTING,
for H(z) were noticeable."* TJB himself confirms H_MULT(z) is service-and-run-sensitive — this
is safer to cite in the letter than any of this project's own reconstruction, and does not
require the source-fidelity gate at all.

## Relation to the standing TJB letter draft

The Hubble-chart letter (`reply_to_TJB_EMAIL_READY.txt`, Desktop, now v9) asks Q2 ("explicit
functional form and parameters of the red curve") — the H_MULT(z) row of this table, narrowly
scoped to his July chart — and Q4 now also carries the Appendix A1 self-consistency finding above
(2026-07-23 update), asking directly whether the same D(z)/parameter mismatch explains it. It
still does **not** ask separately about β_d/β_q's first-principles derivation or the k_A
normalization discrepancy as standalone items — those remain open, lower-priority asks, a scope
decision for the user.

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
| 5 | What equation generates H_MULT(z)? | 🔴 **NEEDS_DATA** — no action/Lagrangian exists (Q006 open); the published curve's exact form is unknown to us — **this is letter Q1, the single most direct ask**. Sharpened (2026-07-23): M1 (confirmed) shows Table A1's H_MULT is a near-constant rescaling of H_FLRW, which structurally could not cross ΛCDM the way the July curve does — Table A1 and the July chart are **likely not the same computational procedure** (see new section above; this specific deduction does not depend on M2's conditional ×4365 figure). Gate run confirms: **the PDF itself specifies no H(z)-combination formula at all** — Q5 is genuinely unanswerable without TJB, not merely under-documented. M2 (bridge reconstruction) downgraded to illustrative-only after the gate run found the reconstruction likely violates TJB's own stated low-z dipole-dominance design constraint (Step 5) — do not cite ×4365 or "opposite direction" as evidence about TJB's real process. |
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
