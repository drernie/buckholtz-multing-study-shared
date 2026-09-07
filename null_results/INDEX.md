# Null Results Index — Buckholtz IDM/MULTING Audit

**Protocol:** Falsification Ladder (FL) — Full-Ladder REJECT registry  
**Rule:** Do NOT retry a REJECT entry without fundamentally different approach.  
**Extended:** Each entry includes `## Mechanistic Insight` — what the failure reveals about the mechanism.


**Two NULL-but-not-REJECT entries added 2026-09-07 (`FINDING_P207`).** `NR-022`
and `NR-023` are not falsified claims: one is an exhausted search, one a test that
failed to discriminate. The registry's own *"do NOT retry without a fundamentally
different approach"* rule therefore does **not** apply to them in the same way —
each carries its own re-entry condition in the linked finding. They are listed here
because they previously existed only as `FINDING_*.md` files and were invisible to
the prescribed pre-work check (`grep -i "keyword" null_results/INDEX.md`), which
reads only this index. That gap is the finding; these rows are the fix.

---

| ID | Date | Slug | Verdict | Why falsified (10 words) |
|----|------|------|---------|--------------------------|
| NR-001 | 2026-06-12 | constant-eps-bridge | REJECT | ε(z) varies 4.7×; constant bridge max residual 0.104 |
| NR-002 | 2026-06-12 | powerlaw-bridge | REJECT | α has 3 sign changes; not a power law |
| NR-003 | 2026-06-12 | ps-comoving-density-model-a | REJECT | PS comoving density monotone; cannot peak at z=0.40 |
| NR-004 | 2026-06-13 | mavs-virial-ps-insufficient | REJECT | virial k_A monotone ∝H(z)^(4/3); all Pearson r negative |
| NR-005 | 2026-06-13 | intrinsic-formation-selection-ambiguity | REJECT (partial) | PS density killed; selection f_sel alone r=0.666 survives |
| NR-007 | 2026-06-13 | sector-count-dm-baryon-ratio | REJECTED_AS_DERIVATION | Author "might suggest" only; 5 required mechanisms all missing |
| NR-008 | 2026-06-18 | merger-epoch-rP-falsified | REJECT | r_P merger correction r=0.682 < 0.75; secondary z=8.5 bump unsolvable by single component |
| NR-009 | 2026-06-23 | s3-geometry-eq32-mechanism | REJECT | (4/3)=(n+1)/n & 12=n(n+1) at n=3 = post-hoc relabeling; ~456 simple (p,h) families coincide |
| NR-010 | 2026-07-01 | cluster-mass-bias-test | KILL | r(delta_M, M_gas×T_x)=0.021 p=0.88; correlation absent; direction reversed (hot clusters show LESS bias) |
| NR-011 | 2026-07-01 | h1d-mass-threshold | KILL | partial r identical high/low mass (−0.732 vs −0.731); Fisher z p=0.498; no mass-threshold effect |
| NR-012 | 2026-07-01 | h1c-morphology-mediator | KILL | partial r unchanged after controlling wX (−0.726 vs −0.714 baseline); morphology does not mediate |
| NR-013 | 2026-07-13 | r011-beta-profile-nesting | REJECTED WITHIN IMPLEMENTATION | true eta_q profile + eta_q→∞ closed form both ≤ Q(0,0)=0.7334; old "optimum" 0.6235 was a box-excluded-baseline artifact |
| NR-014 | 2026-07-17 | h1e-agn-feedback-confound | KILL | r(delta_M,E_ICM\|M_WL,K0)=-0.7181 p=1.33e-08; AGN feedback does not mediate; 4/4 standard-physics alternatives now killed |
| NR-015 | 2026-07-18 | tx-shared-variable-artifact | WEAKENED (mechanism unresolved) | r(delta_M,M_gas\|M_WL,T_X)=-0.08 p=0.58, signal vanishes once T_X controlled; T_X alone r=-0.81 stronger than E_ICM itself; reclassifies NR-011/012/014's "robust to 4 confounds" framing as overclaim. NOTE: file's own "ARTIFACT-CONFIRMED" first-draft label was retired 2026-07-18 by skeptic review — do not cite it |
| NR-016 | 2026-07-19 | shtanov-bridge-naive-mapping | REJECT | phi=V/(m_A m_P) not universal kernel; B,C depend on per-cluster k_A/m_A, k_P/m_P not just m_A*m_P product |
| NR-017 | 2026-07-22 | 79-17-rg-boundary-condition | REJECT | tan²θ_W(m_Z)=0.301 already exceeds target 2/7=0.286, runs monotonically AWAY with scale; no non-post-hoc high-scale μ* exists; companion to T3b's same-day pole-mass REJECT — exhausts 7:9:17's mechanism search |
| NR-018 | 2026-08-03 | naive-pair-fluid-virial-mapping | REJECT | positive-density virial mapping of U~r^-n gives w=n/3, so no dark-energy EoS; Ground2 CONDITIONAL: Omega_pair ~1e-7 [1e-8,1e-6] per independent impl; our 3.9e-5 and '46 R_H' RETRACTED (abundance = 252% of matter). SCOPE: closes ONE mapping, NOT generalized Layzer-Irvine, NOT all bridges |
| NR-019 | 2026-08-17 | lie-group-numerology-eq32-mechanism-consolidated | REJECT (consolidated, 3 attempts) | S³ (NR-009), F₄/G₂/J₃(O) (f4-eq32-synthesis C10), SM-gauge-dim (pearl 06-24) all post-hoc relabel {4/3,12}; no single invariant gives both, no independent prediction; Eq.32 itself survives unexplained |
| NR-020 | 2026-09-02 | eq32-numerology-negative-space-mining | REJECT (H1 timing-axis, skeptic-falsified) | Balmer 1885 counter-example kills a-priori/post-hoc timing rule; DoF-based fallback survives, unattacked, applied to Eq.32 |
| NR-021 | 2026-09-02 | h1prime-formalization-data-collection | REJECT/INCONCLUSIVE (real N=11 not 60, DoF-ratio not reliably codeable) | Blind inter-rater check: DoF-ratio estimates diverge 2-6x between coders; regression point estimate runs OPPOSITE H1's predicted direction (not significant, N too small) |
| NR-022 | 2026-08-24 | 4th-observable-literature-search | **NULL (search exhaustion — NOT a REJECT)** | No class-(i) monomial found; P206 later showed none can exist |
| NR-023 | 2026-08-26 | completion-positivity-non-discriminating | **NULL (non-discriminating — NOT a REJECT)** | BOTH-SAFE on this trajectory range; test separates nothing |

**Files:**

- [NR-009: S³ geometry as Eq.32 mechanism — rejected](20260623-nr009-s3-geometry-eq32-mechanism.md)
- [NR-001/NR-002: constant-eps and powerlaw bridge](20260612-bridge-candidates-fail.md)
- [NR-003: PS comoving density Model A](20260612-ps-comoving-model-a-fail.md)
- [NR-004: MAVS virial+PS insufficient](20260613-mavs-virial-ps-insufficient.md)
- [NR-005: Intrinsic formation vs selection ambiguity](20260613-intrinsic-formation-selection-ambiguity.md)
- [NR-007: Sector count DM/baryon ratio](20260613-nr007-sector-count-dm-baryon-ratio.md)
- [NR-008: Merger-epoch r_P falsified](20260618-nr008-merger-epoch-rP-falsified.md)
- [NR-010: H1a cluster ICM thermal energy — killed](20260701-nr010-cluster-mass-bias-test.md)
- [NR-011: H1d mass-threshold — killed](20260701-nr011-h1d-mass-threshold.md)
- [NR-012: H1c morphology mediator — killed](20260701-nr012-h1c-morphology-mediator.md)
- [NR-013: R011 beta_d/beta_q profile vs nested monopole — rejected within implementation](20260713-nr013-r011-beta-profile-nesting.md)
- [NR-014: H1e AGN feedback confound — killed](20260713-nr014-h1e-agn-feedback-confound.md)
- [NR-015: T_X shared-variable artifact — reclassifies NR-011/012/014](20260718-nr015-tx-shared-variable-artifact.md)
- [NR-017: 7:9:17 RG boundary condition — rejected, exhausts mechanism search](20260722-nr017-79-17-rg-boundary-condition.md)
- [NR-016: Shtanov-Sahni bridge naive mapping — rejected](20260719-nr016-shtanov-bridge-naive-mapping.md)
- [NR-018: pair-potential effective-fluid virial mapping — rejected](20260803-nr018-pair-potential-effective-fluid.md)
- [NR-019: Lie-group numerology Eq.32 mechanism, consolidated — rejected](20260817-nr019-lie-group-numerology-eq32-mechanism-consolidated.md)
- [NR-020: Eq.32 numerology negative-space-mining — H1 falsified, DoF fallback](20260902-nr020-eq32-numerology-negative-space-mining.md)
- [NR-021: H1' formalization data collection — real N=11, coding-reliability problem](20260902-nr021-h1prime-formalization-data-collection.md)
- [NR-022: 4th-observable literature search — NULL, search exhausted, structurally superseded by P206](../experiments/20260803-bridge/FINDING_P137_bottleneck3_literature_search.md)
- [NR-023: completion positivity — NULL, BOTH-SAFE, test does not discriminate](../experiments/20260803-bridge/FINDING_P140_completion_positivity_check.md)

---

## Duhem–Quine Classification (all 22 entries, 2026-09-07)

**Why this exists.** Every row above says a claim was rejected. None of
them said *what kind of thing* was rejected — a whole theory, one bridge
form, one parameterization, or just a test that could not discriminate.
That distinction is the difference between "stop" and "try another form",
and it was carried only in prose. `pearl_registry` row 97 (2026-07-18)
proposed the vocabulary and classified 8 entries; this completes the other
14. Its own rule is followed here: **an entry that resists clean
classification is informative, not a nuisance** — two do, and both are
recorded as resisting rather than forced into a box.

### The headline, unchanged and now complete

**`theory_killed`: ZERO entries out of 22.** MULTING's actual core claim
(`F_m − F_d + F_q` with TJB's own undisclosed `k_A(z)`/`D(z)` schedule) has
never been directly tested. Every rejection above kills a *reconstructed*
form, a mediating mechanism, a parameterization, or a test — never the
theory. Row 97 established this for its 8; it survives the full set.

### Per-entry

| ID | class | note |
|---|---|---|
| NR-001 | `bridge_family_killed` | constant bridge FORM (row 97) |
| NR-002 | `bridge_family_killed` | power-law bridge FORM (row 97) |
| NR-003 | `bridge_family_killed` | Press–Schechter `k_A(z)` schedule (row 97) |
| NR-004 | `bridge_family_killed` | virial `k_A(z)` schedule (row 97) |
| NR-005 | `bridge_family_killed` | **partial** — `f_sel` sub-component survives (row 97) |
| NR-007 | `specification_missing` | the derivation was never specified: author "might suggest" only, 5 required mechanisms all absent. Nothing was tested and failed — there was nothing to test |
| NR-008 | `bridge_family_killed` | + informative byproduct: revealed the two-hump `ε(z)` structure, which is not itself a kill (row 97) |
| NR-009 | `mechanism_killed` | S³-geometry for Eq.32 — a DIFFERENT track, targets Eq.32's coefficients, not a bridge candidate (row 97) |
| NR-010 | **`signature_absent`** ⚠️ *new class* | the proposed correlation is simply not in the data (`r=0.021`, `p=0.88`) and its direction is reversed. Not a mechanism kill — the base signature never appeared |
| NR-011 | `mechanism_killed` | mass threshold does not mediate. Verdict **unaffected** by NR-015; see the framing note below |
| NR-012 | `mechanism_killed` | morphology does not mediate. Verdict **unaffected** by NR-015; see the framing note below |
| NR-013 | `parameterization_killed` | `β_d`/`β_q` profiling inside a given force ansatz (row 97) |
| NR-014 | `mechanism_killed` | AGN feedback/K0 does not mediate. Its own addendum: *"NR-014's own KILL verdict ... is unaffected — K0 genuinely does not explain the correlation"* |
| NR-015 | **`signature_absent`** (retagged 2026-09-07, see correction below) | the pre-registered claim — that `M_gas` has a `T_X`-**independent** contribution with abs(r) above 0.40 — is cleanly falsified: `r=-0.08`, `p=0.58`, bootstrap 95% CI `[-0.39, 0.27]` never reaches 0.40. The test DID discriminate, so NOT `test_inconclusive`. Its *mechanism* is separately unresolved |
| NR-016 | `bridge_family_killed` | Shtanov–Sahni naive mapping: `φ=V/(m_A m_P)` is not a universal kernel |
| NR-017 | `mechanism_killed` | RG-running boundary condition — `tan²θ_W` already exceeds the target at `m_Z` and runs monotonically away |
| NR-018 | `bridge_family_killed` | pair-fluid virial mapping gives `w=n/3`, so no dark-energy EoS from that form |
| NR-019 | `mechanism_killed` | consolidated, 3 attempts (S³, F₄/G₂/J₃(O), SM-gauge-dim) — all post-hoc relabelling; **Eq.32 itself survives unexplained** |
| NR-020 | **RESISTS** ⚠️ | kills a *meta-criterion* (the a-priori/post-hoc timing rule, via the Balmer 1885 counter-example), not a physics claim. No class in this vocabulary is about methodology. Its DoF-based fallback survives, unattacked |
| NR-021 | **RESISTS** ⚠️ | **conflates two kills in one experiment** — exactly what row 97 predicted resistance would reveal. It is `dataset_inadequate` (real `N=11`, not 60) *and* an instrument failure (DoF-ratio estimates diverge 2–6× between blind coders). Either alone would end the test; the entry does not separate them |
| NR-022 | **`search_exhausted`** ⚠️ *new class* | a literature search returned nothing. Since 2026-09-07 `FINDING_P206` upgrades this for class (i) specifically: no such monomial *can* exist while remaining rescaling-invariant, so the null is structural, not a matter of search coverage |
| NR-023 | `test_inconclusive` | BOTH-SAFE: positivity does not discriminate the two completions on this trajectory range. Row 97's own category, matched exactly |

### What the classification surfaced that the prose did not

1. **`NR-011`/`012`/`014`: verdicts stand, the AGGREGATE framing does not.**
   ⚠️ **Correction, 2026-09-07 (same day).** The first version of this
   section said they *"rest on a signal `NR-015` says is not there."*
   **That was wrong**, and it was wrong because it was written from this
   index's own one-line summary of `NR-015` instead of from the file. The
   file says something narrower. Reading the summary rather than the
   source is the exact failure this classification exists to prevent, so
   it is recorded rather than quietly fixed.

   What `NR-015` actually establishes: the pre-registered claim that
   `M_gas` carries a `T_X`-**independent** contribution is falsified
   (`r=-0.08`). It **reproduced** the base correlation the three files
   studied (`r(delta_M, E_ICM | M_WL) = -0.7008`), and it explicitly
   **declines** to establish the artifact mechanism — its own
   "ARTIFACT-CONFIRMED" label was *retired* after skeptic review and the
   file forbids citing it.

   `NR-014`'s own addendum is the authority here: *"NR-014's own KILL
   verdict (AGN feedback/K0 does not mediate) is unaffected — K0 genuinely
   does not explain the correlation."* All three `mechanism_killed` tags
   are therefore **correct and unchanged**.

   What IS superseded is the inference *"4/4 standard-physics alternatives
   killed, therefore the correlation is unexplained by standard physics."*
   **None of the four controlled for `T_X`**, and `T_X` alone is the
   strongest predictor in the whole program (`r(delta_M, T_X | M_WL) =
   -0.81`, stronger than the `E_ICM` proxy the tests were built on). `T_X`
   is a **live, unresolved fifth candidate** with two readings a skeptic
   found the test cannot separate: a definitional artifact (HSE mass needs
   the temperature profile, so `T_X` sits on both sides) versus cluster
   dynamical state as a genuine common driver.

   Forward pointer from the same addendum: **H1b is structurally immune**
   to this concern (WHIM is a different gas phase and radius range from the
   interior `T_X` used in `M_hydro`) and is named there as the sole
   remaining real test of H1.

2. **Three classes were missing from the proposed six.** Row 97 already had
   to add `mechanism_killed` for `NR-009`. Completing the set needed two
   more — `signature_absent` (a predicted correlation simply absent) and
   `search_exhausted` (a search returned nothing) — plus two entries that
   fit nothing. A vocabulary that needs 3 extensions and leaves 2 residuals
   over 22 entries is useful but not complete; treat it as a working
   taxonomy, not a closed one.
3. **The Eq.32 track is a separate arc.** `NR-009`, `NR-017`, `NR-019`,
   `NR-020` all target Eq.32's coefficients, not the F→H(z) bridge. Four of
   22 entries belong to a different question and were only ever grouped
   with the rest by filing order.


