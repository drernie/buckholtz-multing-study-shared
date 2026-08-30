# FINDING P169 — recomputing MULTING's own χ² under the Cosmic Chronometer
# systematic covariance (Moresco et al. 2020), the gap FINDING_P168 named
# as genuinely open

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR
**Verdict (post-skeptic — see "Correction" section for what changed):**
**UNDER A GLS (COVARIANCE-WEIGHTED) REFIT, USING TJB'S OWN PUBLISHED
H_MULT(z) CONSTRUCTION AND HIS OWN CITED SUPPLEMENTAL CODE, MULTING'S OWN
BEST-ACHIEVABLE χ² BARELY IMPROVES ON ITS DIAGONAL VALUE (15.75→15.51 to
15.75, DEPENDING ON SCOPE), WHILE THE PHYSICALLY-EMPTY DUMMY MODEL FROM
`FINDING_P167`/`FINDING_P168` IMPROVES SUBSTANTIALLY MORE UNDER THE SAME
TREATMENT. THE MARGIN BY WHICH THE DUMMY MODEL BEATS MULTING (~1.7 χ²
UNITS UNDER THE ORIGINAL DIAGONAL TREATMENT, `FINDING_P167`) SURVIVES
UNDER THE FULL GLS-COVARIANCE TREATMENT AND, UNDER THE MORE CONSERVATIVE
OF THE TWO SCOPE VARIANTS, WIDENS TO ~2.1 UNITS. THIS DIRECTLY CLOSES THE
GAP `FINDING_P168` LEFT OPEN.**
**Continues/answers:** `FINDING_P168`'s own "does NOT establish" point —
whether MULTING's own χ² would also decrease under the same covariance
treatment, by a comparable or larger amount than the dummy model's.
**Correction (2026-08-31, context-asymmetric skeptic-caught, two points,
both independently re-verified before applying):** the first draft (a)
had an untested risk that the Nelder-Mead refit for MULTING under GLS —
searching over `(H0,anchor~10¹, β1~10¹⁰, β2~10¹⁷)`, coordinates spanning
~16 orders of magnitude, with `xatol`/`fatol` in absolute units — could
have converged prematurely to a bad local optimum rather than the true
best-achievable χ², since an absolute tolerance of `1e-4` is meaningless
relative to a `~10¹⁷`-scale coordinate. **Independently re-verified**,
not accepted on the skeptic's word alone: reran the refit with all three
parameters rescaled to O(1) around the starting guess and 16 different
random starting points (±30–50% of the published fit) — the result
matched the original single-start refit to within numerical noise in
every case (Variant A: `15.5126→15.5126`, `15.5338→15.5338`; Variant B:
`15.7484→15.7484`, `15.7758→15.7758`). This is now a permanent, re-
runnable positive control in `P169_...py` (`test_robust_refit_matches_
plain_refit_no_hidden_local_optimum`). The refit was not stuck — the
headline numbers stand. (b) §3's original mechanistic explanation
("dummy model has more flexibility to exploit the covariance's
correlation direction, per Loewner ordering") is **not actually
consistent with the Variant A numbers**: MULTING's own diagonal→GLS-
refit improvement under Variant A (`15.75→15.513`, `Δ=0.237`) is LARGER
in absolute terms than the dummy model's own improvement there
(`14.073→13.989`, `Δ=0.084`, per `FINDING_P168`) — the opposite of what
that story requires. Only Variant B shows the dummy improving more.
§3 is rewritten below to state this honestly: the *margin* (MULTING
minus dummy) survives and widens under Variant B, but no mechanistic
account of *why* is established by this file, and the one offered in
the original draft directly contradicts the Variant A row.

## 0. Premise — `NO_AUTHOR_ERROR`

This file evaluates only this project's own attempt to answer a
statistical-methodology question (does a specific χ² margin survive a
more realistic error treatment) using TJB's own published construction
and his own cited numerical code. It is not a claim that TJB's own theory
is right or wrong, well- or poorly-motivated, or that his own reported
Table II numbers (computed under a simpler diagonal treatment, which
v82's own text never claims is the only defensible choice) are in error.

## 1. Method

### 1.1 Source of the physical construction — `[VERIFIED-zenodo]`

`FINDING_P161`/`FINDING_P165` (2026-08-30) already established that v82's
own paper text never states the numeric node-mass baseline `M0` needed to
evaluate its own force law in absolute physical units — confirmed by a
full-file search of the ~2279-line paper-text extraction. v82's own
Sec. IV.T points to a cited supplemental Zenodo archive (ref [33],
`T.J. Buckholtz, "Supplemental material for 'Multi-Tier Newtonian
Gravity...'", Zenodo, DOI: 10.5281/zenodo.21204955`) as containing "every
specific numerical claim this paper makes." With the user's explicit
permission, this file downloaded that archive (`zenodo_archive_v17.zip`,
2.14 MB, md5 `9cc38e1b5a4ac6286b635910acf0f5c2`) and **read, but never
executed**, two of its files: `code/multing_core.py` (the physics
functions) and `code/assumptions.yaml` (the numeric constants, which
state explicitly they are "the single source of truth for VALUES"). The
two files were cross-checked against each other for internal consistency
(they agree exactly) before any constant was used here. `P169_multing_
own_chi2_under_covariance.py` re-types these functions and constants
independently — the archive's own code is never imported or run.

The key previously-missing number: `M0_kg = 1.193082e45` (≈6.0×10¹⁴
M☉ — consistent with, though not identical to, the "5–6×10¹⁴ M☉"
illustrative comparison mass v82's own text mentions in an unrelated
sanity-check paragraph). Also newly available: `d0 = 45 Mpc` (already
independently spotted in the paper's own prose, `[VERIFIED-PDF]`), and
the full mass→temperature→gas-mass→thermal-energy chain (Eqs. 10–14),
none of which actually depends on `M0`'s absolute value except through
`M(z)` and `R(z)` themselves (confirmed algebraically before writing the
code, not merely assumed).

### 1.2 Methodological correction to this project's own prior framing

`FINDING_P168` stated this recomputation "would need full numerical
integration of v82's own dynamics," a framing inherited from
`FINDING_P161`'s own LOCAL (near-`z=0` Taylor-expansion) machinery, which
solved a coupled 2nd-order `(s,z,H)` system perturbatively in cosmic time
`t`. Reading TJB's own actual code shows the real global construction is
simpler than that framing assumed: `d(z)=d0/(1+z)` is a **fixed kinematic
power law**, not itself integrated from the force law, and `H²(z)` is
built by **direct 1-D quadrature** (trapezoidal rule, `scipy.integrate.
cumulative_trapezoid`) of a single algebraic integrand computed pointwise
at each `z` — no iterative ODE-shooting method is needed. This made the
full-range recomputation this file performs tractable in a way the prior
framing did not anticipate. (Named as a correction to this project's own
expectation, not a claim about v82's own theoretical content.)

### 1.3 Positive control — `[VERIFIED-INLINE]`

Before trusting anything computed from the reimplementation, this file's
own `test_positive_control_reproduces_table_ii_unconstrained`/`..._sh0es_
anchored` reproduce v82's own reported `χ²₃₃=15.75` (unconstrained,
`H0,anchor=73.22, β1=1.4335×10¹⁰, β2=7.8067×10¹⁷`) and `χ²₃₃=15.78`
(SH0ES-anchored) to within `0.02`, via the same diagonal-sigma objective
and the same fine-grid-plus-interpolation fit procedure his own
`generate_all_results.py` uses. Both pass. Two further positive controls
confirm the GLS machinery itself: at zero systematic amplitude, GLS
matches the diagonal result exactly (`<0.01`), and refitting from v82's
own published optimum under a zero-amplitude GLS objective does not
"improve" on it by more than numerical noise.

### 1.4 Covariance and comparison

Same Cosmic Chronometer systematic covariance as `FINDING_P168`
(Moresco et al. 2020, `arXiv:2003.07362`, rank-1 outer-product
construction, restricted to the 31 real CC points — SH0ES and DESI
excluded, same scoping fix already applied there). Two things computed:

- **(A) Evaluate v82's own PUBLISHED best-fit under GLS, without
  refitting** — the direct "does this exact published curve's χ² move"
  check.
- **(B) Refit MULTING's own model under GLS** (same functional form, same
  free parameters — `(H0,anchor,β1,β2)` unconstrained or `β1,β2` alone
  with `H0,anchor` fixed at SH0ES's `73.04`) — the fair, apples-to-apples
  comparison against `FINDING_P168`'s own GLS-refit of the dummy model,
  since a comparison between a refit dummy and a non-refit MULTING would
  be biased against MULTING.

## 2. Results

### (A) Published fit, evaluated (not refit) under GLS

| Variant | Row | χ²(GLS, published fit) | diagonal χ²(paper) | Δ |
|---|---|---|---|---|
| A (all 31 CC pts) | unconstrained | 15.692 | 15.75 | −0.058 |
| A | SH0ES-anchored | 15.716 | 15.78 | −0.064 |
| B (paper's own [0.2,1.5] range) | unconstrained | 15.749 | 15.75 | −0.001 |
| B | SH0ES-anchored | 15.778 | 15.78 | −0.002 |

MULTING's own already-published curve barely moves under GLS at all —
consistent with `FINDING_P168`'s own Loewner-ordering argument (enlarging
a covariance can only weakly lower χ² *at fixed parameters*), but the
effect here is tiny in absolute terms.

### (B) MULTING refit under GLS vs `FINDING_P168`'s own dummy-model GLS refit

| Variant | Row (k) | MULTING refit χ²(GLS) | dummy refit χ²(GLS, P168) | MULTING − dummy |
|---|---|---|---|---|
| A | unconstrained (k=3) | 15.513 | 13.989 | **+1.524** |
| A | SH0ES-anchored (k=2) | 15.534 | 14.008 | **+1.526** |
| B | unconstrained (k=3) | 15.748 | 13.637 | **+2.111** |
| B | SH0ES-anchored (k=2) | 15.776 | 13.637 | **+2.139** |

For reference, `FINDING_P167`'s original diagonal margin (dummy vs
MULTING's own reported `χ²₃₃`) was `−1.677` (unconstrained) / `−1.673`
(anchored) — i.e. the dummy beat MULTING by ~1.7 units before any
covariance treatment.

## 3. Interpretation

Under refit — the fair comparison — the **margin** by which the dummy
model beats MULTING (`FINDING_P167`'s own original finding) **survives**
the GLS-covariance treatment in both scope variants (`+1.524`/`+1.526`
under Variant A, `+2.111`/`+2.139` under Variant B — MULTING minus dummy,
both positive means the dummy still wins), and **widens** (from the
original diagonal ~1.7 to ~2.1) under the more conservative variant
(systematic restricted to the paper's own analyzed z-range).

**No mechanistic account of *why* is established here (corrected, see
above).** The improvement each model gets from diagonal to GLS-refit
does NOT follow a consistent "more flexible model benefits more"
pattern: under Variant A, MULTING's OWN improvement (`0.237`) is larger
in absolute terms than the dummy's (`0.084`) — yet the margin still
favors the dummy throughout, because the dummy started from a lower
diagonal baseline and stayed lower. Only under Variant B does the dummy
improve more than MULTING (`0.436` vs `0.002`) in a way that would fit a
"the dummy exploits the correlated systematic better" story — and even
there, this file does not test WHY (e.g. whether it is really about
functional-form flexibility, or something else, such as where each
model's own residual pattern happens to sit relative to the specific
`[0.2,1.5]`-range systematic direction). The honest summary is: **the
margin survives and, in one of two scope variants, widens — the
mechanism behind the size of that widening is not established.**

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory being right or wrong**
   (`NO_AUTHOR_ERROR`, §0) — this compares a physically-empty
   curve-fitting exercise against MULTING's own construction on a single
   statistical axis (χ² under one specific covariance model), not a
   verdict on the theory's physical content.
2. **Not the full 31-point Moresco et al. Table 3 covariance** — this
   file, like `FINDING_P168`, uses only the paper's own two headline
   abstract endpoint values (5.4% at z=0.2, 2.3% at z=1.5) linearly
   interpolated, not the actual 29-bin table (`FINDING_P168`'s own scope
   limitation 1, inherited unchanged here).
3. **Does not resolve whether the SAME systematic fraction genuinely
   applies to the non-Moresco-group points in the 31-point compilation**
   (Simon et al. 2005, Stern et al. 2010, Zhang et al. 2014, Ratsimbazafy
   et al. 2017 — different methodology) — `FINDING_P168`'s own scope
   limitation 2, unchanged here.
4. **Does not test other AIC/BIC-style structural comparisons** —
   `FINDING_P166`'s own finding (v82 outperforms a fixed-Planck ΛCDM
   benchmark, both under and without a parameter-count penalty) is
   unaffected by this file and stands independently.
5. **No mechanism is established for WHY the margin moves as it does**
   (corrected, §3) — the diagonal→GLS improvement is larger for MULTING
   than for the dummy under Variant A, the opposite of a naive
   "dummy is more flexible" story; only Variant B fits that pattern.
   This file reports the outcome, not its cause.
6. **The positive control (§1.3) confirms self-consistency at ONE
   reference point** (v82's own published optimum), not full-landscape
   correctness of the reimplementation — a coordinated error (e.g. a
   wrong `M0` compensated by different `β1,β2`) could in principle pass
   it. Partially mitigated by the robustness check in the Correction
   above, which explored a wide neighborhood (±30–50%, 16 starts) around
   that point and found smooth, consistent behavior — but this is not a
   full independent-reconstruction check of the reimplementation against
   a second, unrelated method.
6. **Does not address the h0_anchor_circularity_check or other named
   open items in v82's own text** (Sec. IV.M et al.) — orthogonal to
   this file's own narrow question.
7. **Zenodo archive provenance:** the file was downloaded with explicit
   user permission from the DOI v82's own text cites as its supplemental
   material; this file did not independently verify that the archive's
   own `results/generate_all_results_output.txt` reproduces without
   discrepancy end-to-end (only the two specific Table II rows needed
   here were checked, via this file's own positive control, not the
   archive's full internal self-check suite).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
