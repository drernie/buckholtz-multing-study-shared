# docs/140 — v25 Source Map, Status Mapping, and Clean-Room Reimplementation Attempt

**Date:** 2026-07-24
**Origin:** user supplied "Универсальный атомизатор проектов v1.1" (external methodology
document, Source Map / Verification Ledger two-layer discipline), applied to TJB's v25 paper
(`260723_1330_to_MULT_260717_0525_v25_first_13_pages.pdf`, re-read in full this session for
exact transcription). Follow-on autonomous work: attempted the clean-room reimplementation
already offered to TJB in [docs/137](137_tjb_immediate_help_brief.md) item 4.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION
**Related:** [docs/137](137_tjb_immediate_help_brief.md), [docs/138](138_tjb_optional_technical_modules.md), [docs/139](139_internal_null_and_hypothesis_registry.md), `scripts/clean_room_v25_reimplementation.py`

---

## 0. Headline finding

**Our own R011 pipeline (`src/pearson_fit.py:10`) computes `H_MULTING = H_0·sqrt(phi/phi_ref)`
— a DIFFERENT bridge than v25's actual model (Eqs 5–9: reduced-mass two-body dynamics →
Kinematic Translation Protocol).** [VERIFIED-GREP, re-checked this session]. Every "reproduction"
claim in this session's prior work (R011, docs/135 Audit 3, its `r=0.7334/0.6235` numbers) tested
the Φ(z)/Φ(z_anchor) bridge, not v25's `r=0.9525` result (Table III). This is not an arithmetic
bug in R011 — it reproduces its own bridge internally-consistently — it is a claim that R011 was
never testing *this* model.

**New this session, from attempting the correction:** building the *correct* kinematic-route
bridge from Eqs 5–9 turns out to require one more initial condition than the 13 available pages
specify, and it is load-bearing for the *shape* of H(z), not just its normalization. See §4.

---

## 1. Status mapping — what's already done, in the new framework's vocabulary

4-axis status = **Epistemic verdict** (PASS/FAIL/UNRESOLVED/CONFLICTING) × **Evidence mode**
(SOURCE-CONFIRMED/ANALYTIC/NUMERICAL/STATISTICAL/EMPIRICAL/REPRODUCED/...) × **Operational state**
(READY/BLOCKED-*/INVALIDATED-PENDING-RERUN/PARKED/...) × **Generality** (LOCAL/CONDITIONAL/
DOMAIN-LIMITED/GLOBAL).

| # | Claim / result | Epistemic | Evidence mode | Operational state | Generality | Where |
|---|---|---|---|---|---|---|
| 1 | Kinematic-route bridge (Eqs 5–9) is the model's real generating spec | PASS | SOURCE-CONFIRMED | READY | LOCAL | v25 p.4–5 |
| 2 | Our R011/docs/135 reproduction used a different bridge (Φ-route) | PASS (self-audit) | ANALYTIC + code-read | INVALIDATED-PENDING-RERUN | LOCAL-TO-OUR-PIPELINE | this session, grep-verified |
| 3 | Eq 8's z-space prose ("integrating 2(ä/a)/(1+z) yields H²−H0²") is only exact as a simple quadrature if the H² term in `ä/a = H² − (1+z)H·dH/dz` is dropped | **PASS — tool-verified** | ANALYTIC (sympy, cross-checked against the paper's OWN Eq. 18) | READY (the finding itself, not a claim about the paper being wrong) | LOCAL | this session, §4 |
| 4 | χ²_MULT=13.565, χ²_ΛCDM=14.500, r=0.9525/0.9494 (Table III) | SOURCE-CONFIRMED, not independently reproduced | SOURCE-CONFIRMED | BLOCKED-REPRODUCIBILITY (missing v0, §4) | LOCAL | v25 p.11 |
| 5 | Case1/Case2 β-degeneracy (identical χ²/r at ~5× different couplings) | PASS — author-demonstrated, Table IV | SOURCE-CONFIRMED | READY | author already scopes it: "H0,anchor only weakly constrained" | v25 p.11–12 |
| 6 | DESI z=2.33 extrapolation fails (−4.55σ to −5.03σ) | FAIL — author-reported, honestly scoped | SOURCE-CONFIRMED | READY (as a reported negative result) | LOCAL (author explicitly declines to generalize) | v25 p.13, Table VI |
| 7 | r_d-convention dependence of DESI H(2.33) (docs/137 item 3) | UNRESOLVED | our RECOMPUTED-SAME-PIPELINE | BLOCKED-EXTERNAL | LOCAL | docs/137 |
| 8 | r_X(z) circularity (Friedmann eq. used to build an input for a Friedmann-alternative) | PASS — author self-flags, "Class III, circular... most serious residual dependence" | SOURCE-CONFIRMED | READY (acknowledged, not resolved) | author: "not resolvable simply by sourcing additional data" | v25 p.9 |
| 9 | AIC/BIC undefined/inappropriate for MULTING (docs/135 Audit 3, PIVOT) | PASS — convergent finding | our STATISTICAL, his SOURCE-CONFIRMED | READY, both sides agree independently | matches spec's own `CONDITIONAL DIAGNOSTIC` category | docs/135 + v25 p.10 |
| 10 | k_X(z) self-similar thermal scaling (Eqs 12–14), T0 recalibrated | PASS (transcription); author flags own T-M tension (3.3–3.6 keV implied vs ~7 keV independent) | SOURCE-CONFIRMED | CONDITIONAL DIAGNOSTIC (author's words) | DOMAIN-LIMITED (z<1.07 rigorous, author's own Table V split) | v25 p.6 |
| 11 | Birge-ratio "genuine underdetermination" claim (docs/139 R-1) | UNRESOLVED, downgraded | our STATISTICAL | PARKED (frozen PASS/FAIL never set before computing R_B) | LOCAL | docs/139 |

**Notable convergences (rows 5, 8, 9):** TJB independently runs something close to this same
discipline in his own paper — a 3-class provenance taxonomy (data-proximate/retained-theoretical/
circular, p.8–9) matching the Atomizer's own provenance distinctions, and an independent decision
to withhold AIC/BIC for reasons matching our own docs/135 finding. Worth naming this convergence
to him directly at some point.

---

## 2. Source Map — Formula Registry (Table B), v25 Eqs 1–18, EXTRACTION_ONLY

Per the spec's own discipline: no verdicts in this table, only what the paper states, page-cited.

| ID | Eq#/page | Formula | Role | Depends on | Author's own caveat |
|---|---|---|---|---|---|
| F-01 | (1) p.4 | F_P = F⁽⁰⁾ − F⁽¹⁾ + F⁽²⁾ | force sum | F-02,03,04 | monopole=attract, dipole=repel, quad=attract by sign convention |
| F-02 | (2) p.4 | F⁽⁰⁾ = −Gm_Am_P/s² | monopole | — | none stated |
| F-03 | (3) p.4 | F⁽¹⁾ = β₁(−Gk_Ac⁻²m_Pr_A/s³) + β₁(−Gm_Ak_Pc⁻²r_P/s³) | dipole | F-02's convention | β₁ "suggested to be approximately node-independent" |
| F-04 | (4) p.4 | F⁽²⁾ = β₂(−Gk_Ak_Pc⁻⁴r_Ar_P/s⁴) | quadrupole | F-02's convention | β₂ "suggested to be approximately pair-independent" |
| F-05 | (5) p.4 | F_P = m_P(dv_P/dt) + (dm_P/dt)v_P | variable-mass 2nd law | — | explicitly the SPECIAL case (matter joins at v_P) |
| F-06 | (6) p.5 | m_P(dv_P/dt) = F_P + (dm_P/dt)(u_P−v_P) | general momentum-conserving form | F-05 | general case, u_P=v_P recovers F-05 |
| F-07 | (7) p.5 | μs̈ = F_P + μ[ṁ_P(u_P−v_P)/m_P − ṁ_A(u_A−v_A)/m_A] | reduced-mass 2-body eq | F-06 ×2 | "in general independent" accretion histories per node |
| F-08 | (8) p.5 | ä/a = s̈(z)/s(z) | Kinematic Translation Protocol | F-07 | "not an assumption this framework otherwise relies on" — bridging device only |
| F-09 | (9) p.5 | dz/dt = −(1+z)H(z) | standard FLRW redshift-time map | — | none stated |
| F-10 | (10) p.6 | m_X(z) = m0·(1+z)⁻¹·¹ | node mass evolution | — | exponent is "a simplification" of a wider-range simulation [18] |
| F-11 | (11) p.6 | r_X(z) = r0·(m_X(z)/m0)^(1/3)·E(z)^(−2/3) | effective radius (R500-type) | F-10 | Class III — **circular**, author's own words (p.9) |
| F-12 | (12) p.6 | T_X(z) = T0·(m_X(z)/m0)^(2/3)·E(z)^(2/3) | self-similar X-ray temperature | F-10 | T0=3.7163 keV recalibrated; implies T~3.3–3.6 keV vs ~7 keV independent M-T |
| F-13 | (13) p.7 | M_gas,X(z) = M_gas,piv·(T_X/T_piv)^B·(E(z)/E(z_piv))^C | gas-mass fit, real relation [22] | F-12 | catalog covers 0.05<z<1.07 only; 6/31 CC points lie beyond it |
| F-14 | (14) p.7 | k_X(z) = (3/2)·(M_gas,X/μ_mol·m_proton)·T_X | total ICM thermal energy (= k_A/k_P) | F-12,F-13 | none additional |
| F-15 | (15) p.7 | v_infall(z) = √(Gm_X(z)/r_X(z)) | characteristic merger infall velocity | F-10,F-11 | explicit: not literal circular-orbit motion |
| F-16 | (16) p.8 | Δv_coh(z) = f_coh·f_merge·v_infall(z) | coherent velocity mismatch | F-15 | f_coh "a stated modeling assumption, not measured" |
| F-17 | (17) p.8 | F_acc(z) = ṁ_X(z)·Δv_coh(z) | accretion-correction force | F-10,F-16 | sign "a first-pass modeling choice... not independently derived" |
| F-18 | (18) p.10 | q(z) = (1+z)(dH/dz)/H(z) − 1 | deceleration parameter (diagnostic only) | fitted H(z) | reported "for comparability", not the framework's primary diagnostic |

Coverage: Eqs 1–18, all numbered equations in the 13 available pages. Does not cover the full
manuscript beyond page 13, and does not include a separate Table C (numeric registry) or Table D
(assumptions) beyond what's folded into the caveat column above.

---

## 3. Clean-room reimplementation attempt (`scripts/clean_room_v25_reimplementation.py`)

Per the offer already made in docs/137 item 4: built independently of `src/pearson_fit.py`,
from F-01..F-18 only.

### 3.1 The literal z-space prose is an implicit ODE, not a quadrature — tool-verified

The paper's own words (p.5): "Integrating 2(ä/a)/(1+z)... with respect to redshift yields
H(z)²−H0²." The standard FLRW identity, verified symbolically against the paper's OWN Eq. 18
(q(z) = (1+z)dH/dz/H − 1) via `sympy` this session:

```
ä/a = H² − (1+z)·H·dH/dz
```

confirms `q_from_this_identity == q_eq18` exactly (zero residual). This means Eq 8 is a genuine
(and, once posed in cosmic time t rather than z, *explicit*) ODE, not a one-line quadrature
independent of H — a distinction the Atomizer spec's own §21.3 (coupled-equation gate) is
specifically designed to catch ("нельзя представлять такую задачу как простую явную квадратуру
без доказательства"). This is a finding about the *prose description*, not a claim that Eqs
1–9 themselves are wrong.

### 3.2 Reformulating in cosmic time resolves the implicit trap, but exposes a missing initial condition

Working in t (state vector `[s, v=ds/dt, z]`) makes the system explicit and integrable, because
F_P and F_acc (Eqs 1–4, 15–17) depend only on `(s, z)`, never on `v`:

```
ds/dt = v
H(z)  solves  mu*s*H^2 + [1.1*m_X(z)*Delta_v_coh(z)]*H - F_P(s,z) = 0   (Eq 7+8+17 combined)
dv/dt = H(z)^2 * s                         (Eq 8, rearranged)
dz/dt = -(1+z) H(z)                        (Eq 9)
```

`F_acc` (Eq 17) is linear in `H(z)` itself (`F_acc = 1.1·H·m_X(z)·Δv_coh(z)`), so `H(z)` is not a
free-standing unknown to be assigned a stale/external value — it is *solved for*, exactly, via the
quadratic above, at every `(s,z)` along the trajectory (`h_self_consistent()` in the script). An
earlier version of this script got this wrong: it passed the *constant* `H0,anchor` into `F_acc`
at every `z`, not the true local `H(z)`. Caught by an `Agent(reviewer)` pass (per CLAUDE.md's 3+
file checklist) run before this doc was finalized — confirmed to shift `F_acc` by up to ~97% at
z≈0.5–1.0. **Fixed, and the fix does not change the qualitative conclusion below** (numbers moved
slightly; the non-monotonic shape is the same before and after) — worth stating explicitly, since
"we found and fixed a bug" could otherwise read as casting doubt on everything reported here.

This is a 2nd-order ODE in `s`, needing **two** initial conditions at z=0: `s0=s(0)` and
`v0=ds/dt(0)`. The paper states three free parameters (β1, β2, H0,anchor, p.10) — no fourth. That
constrains `s0`: requiring self-consistency with the fitted `H0,anchor` (`H0,anchor² = [F_P(s0,0)
− F_acc(0)]/(μ(0)·s0)`) gives one equation, solvable for `s0` by root-finding, using only
already-specified quantities. **`v0` is not pinned by anything in Eqs 1–17** (neither F_P nor
F_acc depends on velocity) — it is a genuinely missing initial condition.

### 3.3 What we tried, and what it shows

- `s0` closure: root-find works and is exact (`H(z=0)` reproduces `H0,anchor=76.46` to 10+ digits
  by construction) for identical-node baseline masses in the range `m0 ≈ 8×10¹⁴–1×10¹⁵ M☉` — a
  physically ordinary galaxy-cluster/group mass, consistent with "node = one cluster or a few
  clusters" (p.2). For smaller `m0` (≲6×10¹⁴), the self-consistency equation has **no solution at
  all** (the dynamics never gets fast enough to reach `H0,anchor²`, at any `s`).
- `v0` closure: no equation constrains it, so we tried the single most parsimonious,
  zero-new-parameter choice — `v0 = H0,anchor·s0` (the node pair also participates in ordinary
  local Hubble flow at z=0). **This produces a non-monotonic H(z):** rising from 76.46 at z=0 to
  a peak of ≈152 km/s/Mpc around z≈0.6–0.8, then falling back to ≈68 by z=2.5 (m0=8×10¹⁴ case;
  `H(z=2.33)≈76.2`, i.e. back down near the starting value). Table II/III's H(z) is monotonically
  increasing across the same range. This specific closure choice is therefore qualitatively wrong,
  not just numerically off — and, per the note in §3.2, this shape is unchanged by the `h(z)`
  self-consistency bugfix, so it is not an artifact of that bug.

**We stopped here rather than searching for a `v0` that happens to produce a monotonic match** —
doing so would be tuning a free parameter against the target curve, which is exactly the
validation-theater failure mode this project's rules exist to prevent (a 4th, hidden free
parameter dressed as a "derivation"). `docs/137` item 4's offer to TJB stands, but its honest
status is now **BLOCKED-REPRODUCIBILITY**, more precisely characterized than before: not "we
haven't tried yet" but "we tried, the formulas as printed are under-determined by exactly one
initial condition (`ds/dt` at z=0), and it is load-bearing for the *shape* of the result, not
just its scale."

**Sharper question this enables for TJB**, replacing the vaguer "share your generating
specification" ask already sent: *what determines the node pair's initial relative velocity
(`ds/dt` at z=0), separately from the local Hubble-flow rate itself — is it read off the same
merger/infall statistics used for the accretion correction (Eqs 15–16), or fixed by a different,
unstated convention?* Not sent yet — routing decision is the user's (see docs/137/138 triage
discipline: GREEN items still need a final read + cooling-off pass before anything is sent).

### 3.4 Coverage / honesty note

This is not a Statistical Certification Gate pass (no χ²/Pearson-r comparison was computed
against Table III, since a shape-mismatched curve makes that comparison meaningless, not just
premature) and not a Reproducibility Gate PASS. Correct status per the Atomizer vocabulary:
`Epistemic: UNRESOLVED` / `Evidence mode: ANALYTIC+NUMERICAL` / `Operational state:
BLOCKED-REPRODUCIBILITY` / `Generality: LOCAL` — a genuine, well-characterized limitation, not a
claim about whether v25's model is right or wrong.

---

## 4. Что можем сделать дальше — приоритизировано

**P0:** ничего дальше не гадать по v0 — это уже проверено и дало неправильную форму; следующий
реальный шаг требует ответа доктора (сформулированный в §3.3 вопрос), либо явного разрешения
пользователя на дальнейший спекулятивный перебор с пометкой `[SPECULATIVE]`.

**P1 (дёшево, не требует доктора):** Data Attribution Gate для DESI H(z=2.33) в полной табличной
форме (docs/137 п.3 уже содержит суть, не в формальной схеме §22 атомизатора).

**P2 (дёшево):** Table C (numeric registry) для Table II–VI полностью — инкремент, не блокирует
ничего текущего.

**P3:** после ответа доктора на вопрос из §3.3 — перезапустить `clean_room_v25_reimplementation.py`
с правильным v0 и довести до полного χ²/Pearson-r discrepancy log против Table III/VI.
