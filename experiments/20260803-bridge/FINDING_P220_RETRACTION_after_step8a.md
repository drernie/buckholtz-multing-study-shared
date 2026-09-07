# RETRACTION — P220's headline claim is a frozen-parameter artifact

**Date:** 2026-09-07 (same day P220 was written, committed and pushed)
**Supersedes:** `FINDING_P220_BC_uncertainty_breaks_the_fit_26pct_of_the_time.md`
**Method:** one context-blind Step 8a skeptic pass, every load-bearing claim
independently re-verified by me — three by direct algebraic re-derivation
(confirmed numerically to 6 decimal places), one by grep against source,
one by the skeptic's own proposed kill-test (re-run independently, twice,
with matching results both times).
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## 0. Verdict

**P220's headline — "propagating v82's own two quoted nuisance
uncertainties makes the model undefined in 26% of draws, and moves χ²₃₃
across a range that dwarfs MULTING's own margin over flat ΛCDM" — is a
frozen-parameter artifact, not a property of the model.** Letting
`(β₁,β₂,H0_anchor)` refit — which the skeptic pointed out is mathematically
guaranteed to help, never hurt — absorbs nearly all of it. A small, real,
and much less dramatic residual survives.

| draw | frozen `χ²` (P220's claim) | **refit `χ²`** |
|---|---:|---:|
| `C = −1.30` (−1σ) | 930.3 | **14.08** — *better* than the published 15.75 |
| `C = −0.71` (+1σ) | NaN (undefined) | **41.67** |

---

## 1. The decisive error: T0 is exactly degenerate with `(β₁,β₂)`, and I proved it, not just the skeptic

The skeptic derived, by factoring the code:

```
k(z) ∝ T0^(B+1) · (1+z)^(−11(B+1)/15) · E(z)^(2B/3+C+2/3)
```

— meaning that at **fixed `(B,C)`**, changing `T0` alone rescales `k(z)` by
a single, `z`-**independent** constant `λ = (T0_new/T0_old)^(B+1)`.

I re-derived this independently from the code, then verified it
numerically `[VERIFIED-tool]`:

```
lambda (T0 shift, my own derivation) = 3.272271204435003
  z= 0.00  k(T0b)/k(T0) = 3.272271
  z= 0.50  k(T0b)/k(T0) = 3.272271
  z= 1.07  k(T0b)/k(T0) = 3.272271
  z= 2.33  k(T0b)/k(T0) = 3.272271
```

Exact to 6 decimal places at every tested `z`. Combined with the
elementary fact that `F1 ∝ β₁·k` and `F2 ∝ β₂·k²`, a pure rescaling
`k → λk` is **exactly cancelled** by `β₁ → β₁/λ`, `β₂ → β₂/λ²` — the force
law, and therefore `H(z)` and `χ²`, come back unchanged.

**P220's §5 ("T0 scenario… it breaks") is void.** The reported `NaN` at
`T0 = 5.358 keV` says nothing about the model — it is a artifact of
holding `β` fixed while moving a parameter the model is exactly degenerate
with. `P220_joint_BC_uncertainty_propagation.py`'s new
`test_exact_k_beta_degeneracy` / T0-degeneracy section makes this an
executable, checked fact rather than an assertion.

Beyond voiding §5, this exposed a second, independent problem: v82's own
§II.F (**v82:590-600**) explicitly **rejects** the weak-lensing-calibrated
alternative §5 moved *toward*, on stated grounds it is *"more deeply
cosmology-dependent, not less."* P220 quoted the passage that raises the
`~7 keV` figure (**v82:416-420**) but not the passage, two sections later,
that explains why the author declined to use it. This is the same class
of error `~/.claude/CLAUDE.md`'s new PROCESS RULES (added earlier today)
names: reading the applied passage, not the self-limiting one.

## 2. The decisive test: refitting absorbs nearly all of the claimed fragility

The skeptic's proposed kill-test — refit `(H0_anchor,β₁,β₂)` at
`C = −1.30` and `C = −0.71` rather than holding them frozen — is
mathematically guaranteed to help: the frozen point is one member of the
refit's own search space, so `χ²_refit ≤ χ²_frozen` always. **P220's own
closing verdict claimed the opposite** ("a full refit... would likely
widen this further, not narrow it") — backwards, and now corrected.

I ran the test myself, independently, twice (a throwaway script and then
the properly committed one), with matching results both times
`[VERIFIED-tool]`:

```
refit at (B=2.24,C=-1.00): chi2=15.751  (paper unconstrained_spotlighted: 15.75)
C=-1.30 (-1sigma): chi2_refit = 14.080   (frozen-beta chi2 was 930.3)
C=-0.71 (+1sigma): chi2_refit = 41.670   (frozen-beta chi2 was NaN)
```

**At `C = −1.30`, refitting finds a *better* fit (14.08) than the
published optimum (15.75).** At `C = −0.71`, refitting finds `41.67` —
worse than published, but nowhere near "undefined," and squarely inside
the range v82's **own** Table II already reports for its seven rows
(`15.75` to `47.77`, driven by author-chosen tension-reduction
constraints). This is not a catastrophic failure mode; it is an ordinary,
modest fit-quality tradeoff of the kind the paper's own table already
displays.

## 3. The B-row of the 1-D scan was misread as a "ridge" — mostly it is pure rescaling

`k(z)`'s dependence on `B` at fixed `T0,C` factors through
`T(z)^ΔB` — and `T(z)` varies only mildly across `0 ≤ z ≤ 2.33`, so most
of a `ΔB` perturbation is a near-constant rescaling, exactly the kind
`(β₁,β₂)` can absorb. `k(z)`'s dependence on `C` factors through
`E(z)^ΔC`, and `E(z)` spans roughly a factor of `3.5` across the same
range — a perturbation that changes the **shape**, not just the scale, of
`k(z)`, and which `(β₁,β₂)` cannot fully absorb (only partially, per §2).

P220's §4a treated the `B` and `C` rows of its scan as equivalent evidence
of "a sharp ridge." They are not equivalent — only `C`'s sensitivity
survives scrutiny; `B`'s is mostly the same kind of artifact as `T0`'s,
just less extreme. Committed, reproducible numbers `[VERIFIED-tool]`
(`ABSORBABLE_VS_SHAPE` section):

```
Delta-B = +1sigma (0.03): normalization 1.0128, shape range [0.9985, 1.0021], spread 0.354%
Delta-C = +1sigma (0.29): normalization 1.1624, shape range [0.8282, 1.1919], spread 36.373%
```

**`C`'s non-absorbable shape distortion is ~103× larger than `B`'s.**

## 4. The `16.31` ΛCDM benchmark was mislabeled

P220 (and its sibling `P219`, checked separately — see below) called
`16.31` *"flat-ΛCDM benchmark… no B/C dependence"* and, in one place,
*"ChiSquared_LCDM_flat_planck."* `[VERIFIED-source]`,
`assumptions.yaml`'s `lcdm_benchmarks` block:

```
extant_fixed_planck:      H0=67.4,  Om=0.315,  chi2_33=36.96   <- genuinely fixed Planck
adjusted_freely_optimized: H0=71.83, Om=0.2724, chi2_33=16.31   <- a 2-PARAMETER FIT
```

Both numbers are reproduced exactly in TJB's own
`generate_all_results_output.txt:29,33`. **`16.31` is not "Planck values"
— it is a free 2-parameter fit to the same 33 points.** The genuinely
fixed-Planck comparator is `36.96`.

This is a labelling error, not a choice error: v82's own text
(**v82:675-677**) states its primary comparison **is** the fitted ΛCDM
curve — *"computed identically for this framework and for a flat ΛCDM
curve fit directly to the same 33 points, so that the comparison is
fair"* — so `16.31` remains the author's own preferred comparator. But
calling it "Planck" is wrong, and it inflated P220's headline framing:
against the genuinely fixed benchmark (`36.96`), MULTING's margin is
`21.21` in `χ²`, not `0.56`.

**`P219` does not have this error** — checked directly:
`P219_desi_dr1_cc_oos_bounded_check.py` computes `H_lcdm_kms(z)` with
`H0=67.4, Om=0.315` explicitly and directly, never citing `16.31` at all.

## 5. What survives

- The `C = 2.24… ` sign — no, corrected: **`C = −1.00 (+0.29/−0.30)`
  uncertainty produces a real, non-absorbable distortion of `k(z)`'s shape
  across `z`**, and even after a full refit of `(β₁,β₂,H0_anchor)`, a `+1σ`
  shift costs a real `χ²` degradation (`15.75 → 41.67`) — genuine, though
  far short of "the model breaks."
- The off-anchor positive control (`PC3`, new): predicting v82's own
  quoted `T0=6.0 keV` gas-fraction range (`0.35-0.37`) purely from the `B`
  exponent and the `T0=3.7163` range (`0.118-0.127`) gives `[0.345,
  0.371]` — confirms the `(B,C)`-parameterized code itself is correct,
  independent of the anchor point.
- `PC1`/`PC2` still pass exactly, unchanged.

## 6. Actions

- `P220_joint_BC_uncertainty_propagation.py` rewritten in place: T0
  degeneracy made an executable check, the 1-D scan is now real committed
  code (was previously run only in an ephemeral, uncommitted script — a
  Gate 1/FL Step 2a violation on its own, independent of the numerical
  errors), the absorbable/shape decomposition added, the refit kill-test
  added, the LCDM labels corrected.
- `FINDING_P220_BC_uncertainty_breaks_the_fit_26pct_of_the_time.md` carries
  a **DO NOT CITE** banner pointing here. Text kept verbatim.
- `docs/158`'s own item 3 status needs updating to reflect the corrected,
  much narrower surviving claim.
