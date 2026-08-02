# docs/132 — First direct empirical test of the MULTING force layer (kSZ)

**Date:** 2026-08-02 · **L0:** descriptive
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Artifacts:** `experiments/20260802-ksz-force-law/`
**Supersedes:** all earlier β_d estimates in this session's chat, including β_d < 9×10⁵.

---

## 1. Why this matters

Every previous test of MULTING ran through the unresolved bridge
`F_oP → H_MULT(z)` (Q1/Q5, BETA-1 HOLD). This one does not. It tests the
**force law itself** against a published measurement of the pairwise
gravitational acceleration between halos — an earlier node in the causal chain.
If the force layer fails, no argument about the Friedmann bridge is needed.

Data: public release accompanying arXiv:2604.14327 (ACT + SDSS pairwise kSZ,
`github.com/patogallardo/pairwiseksz_mond`). Their headline: g ∝ 1/rⁿ with
n = 2.1 ± 0.3 over 30–230 Mpc.

## 2. Headline result

> Public kSZ data do **not** require a 1/r³ term.
> **ℓ_d = A₃/A₂ < 15 Mpc (95%)**, robust to the UV prescription within ×1.56.
> Δχ² = 0.09–0.35 across all variants; q_obs = 0.246 against a calibrated
> threshold of 3.508 → **no detection**.

Uncertainty budget, largest first:

| Source | Contribution |
|---|---|
| UV prescription (hard exclusion vs Plummer, s_min 1–5 Mpc) | **×1.56 — dominates** |
| Bin policy (15 vs 18 bins, leave-one-out) | ±10% |
| Coverage threshold (calibrated vs naive) | ±5% |
| ξ(r) measurement error | ±3% |

Conversion to β_d gives 2–3×10⁵, but that step is **assumption-laden** (a single
k, a single r_A, no averaging over the pair population, β_d constant). **ℓ_d is
the primary result**; β_d is derived and should be quoted with its assumptions.

## 3. The kernel — what took four attempts to get right

The published analysis uses a Newtonian kernel `K(r) = ∫₆^r ξ(r′)r′²dr′ / r²`
(excess enclosed mass over r²). Newton's shell theorem makes the point-mass
reduction exact for 1/r² **only**. For 1/r³ two separate things go wrong:

**(a) Extended mass, both sides.** A shell at radius r′ acting on a point at r
contributes `C_k(ρ)` times the point-mass value, ρ = r′/r:

```
C_3(ρ) = 1/(2(1-ρ²)) + ln|(1+ρ)/(1-ρ)| / (4ρ)      [both sides of ρ=1]
C_2(ρ) = 1 (ρ<1), 0 (ρ>1)                          [Gauss]
```

Verified against direct μ-quadrature to 1e-7…1e-11 at ρ = 0.5, 0.9, 1.5, 3.0.
Mass **outside** R contributes with **opposite sign** for k=3: C_3(1.5) = −0.132,
C_3(2.0) = −0.029. At R=100, s_min=2 the split is inside +1.856e-2,
outside −2.923e-3 → the outside term **weakens the kernel by 15.8%**.

**(b) UV divergence.** C_3(ρ) ~ +1/(4(1−ρ)) as ρ→1⁻, so `∫dρ/(1−ρ)` diverges
logarithmically; C_4 ~ 1/(6(1−ρ)²) diverges linearly. Proof by node refinement:

| n_node | K₃(100) | K₄(100) | ℓ_d |
|---|---|---|---|
| 240 | 0.02218 | 0.0046 | 2.10 |
| 61440 | 0.03075 | **1.1049** | 1.30 |

A UV prescription is therefore **mandatory**, and every number is conditional
on it. For the quadrupole the cutoff dependence is not mild — **no β_q bound is
obtainable this way at all**.

## 4. UV robustness (the PASS criterion, set before the run)

Criterion stated in advance: the 95% bound must stay within ×2 across
physically distinct prescriptions.

| Prescription | K₃(100) | ℓ_d | 95% upper | Δχ² |
|---|---|---|---|---|
| hard s_min=1 | 0.015853 | 4.60 | 14.30 | 0.302 |
| hard s_min=2 | 0.015633 | 4.80 | 15.80 | 0.248 |
| hard s_min=5 | 0.015046 | 4.60 | 20.80 | 0.091 |
| Plummer rc=1 | 0.015641 | 4.40 | 13.30 | 0.349 |
| Plummer rc=2 | 0.015766 | 4.60 | 14.30 | 0.307 |
| Plummer rc=5 | 0.015330 | 5.10 | 17.20 | 0.219 |

**Spread ×1.56 → PASS.** Hard exclusion and smooth softening are physically
different recipes and agree.

## 5. Statistics done properly

MULTING's dipole is repulsive, so the physical prior is ℓ_d ≥ 0 — a boundary
parameter, where the naive χ²₁ threshold does not have 95% coverage. Calibrated
on 2000 synthetic nulls drawn from the measured covariance:

- P(q = 0) = **0.466** (Chernoff predicts 0.5)
- empirical 95th percentile = **3.508** (naive 3.841, Chernoff mixture 2.706)

The empirical value sits between the two because the amplitude is profiled.
Bound is insensitive: 14.50 / 15.50 / 15.80 Mpc for the three thresholds.

ξ(r) uncertainty (60 redraws from its quoted per-bin errors): median 15.40,
16–84% [15.20, 15.60]. Bin policy: 14.00 (all 18) … 16.90 (drop innermost);
most influential bin is r = 25 Mpc, the innermost — expected, since that is
where the UV model matters most.

## 6. Force-ratio arithmetic at the published β

With k = internal kinetic **energy** (preprint p.11 line 775 — the explicit
c⁻²/c⁻⁴ factors ARE the conversions) and κ = k/(mc²) = 1.669e-5, r_A = 2 Mpc:

```
F_d/F_m = 2 β_d κ (r_A/r)        ← factor 2: the dipole has TWO symmetrised terms
F_q/F_m = β_q² κ² (r_A/r)²       ← β_q SQUARED
```

At β_d = 4.5: F_d/F_m = 6.0e-6 at 50 Mpc. Dipole equals monopole only at
r ≈ 3.0e-4 Mpc — **6658× inside** the cluster radius, where the pair multipole
expansion in (r_A/r) is outside its own validity domain.

## 7. Figure-3 scale mismatch (NOT a no-go)

At published β the multipole contribution to H² is ~6e-6 at 50 Mpc, while the
anchor-free shape difference carried by the 2026-08-02 figure is ~0.20 — a gap
of **3.3×10⁴**.

**This is a scale-mismatch challenge, not a proof.** A force ratio of 1e-6 need
not map linearly to δH/H of 1e-1 without the explicit operator
`M : F(r,a) → H(a)`, which does not exist in the corpus. Verbal confirmation of
a kinematic route is not an equation. The correct output is a question, not a
verdict:

> Using the published β_d = 4.5, k/(mc²) = 1.67e-5 and cluster-scale
> separations, the direct dipole-to-monopole force ratio is of order 1e-6,
> while the anchor-free variation represented by Figure 3 is of order 1e-1.
> What explicit dynamical equation maps the former into the latter, and where
> does the required amplification enter?

## 8. Error log — six corrections, none found by the author of the number

| # | Error | Found by |
|---|---|---|
| 1 | β_d < 9×10⁵ was an artifact of the sign-change wall, not a likelihood | kSZ agent, on obtaining real data |
| 2 | Factor 2 missing in the symmetrised dipole; β_q not squared | force-law agent (sympy) |
| 3 | K₃/K₄ divergence hidden by discretisation | **blind analytic skeptic, with no code execution at all** |
| 4 | Kernel integrated only r<R, omitting opposite-sign outside mass | Task 2 |
| 5 | v-substitution normalisation 1/(4ρ) should be 1/(8ρ) | k=2 control |
| 6 | Spurious extra /R³ in the Plummer branch | rc→0 vs s_min→0 limit check |

Every one was caught by an independent check — a second implementation, a limit
test, or a positive control. None was caught by re-reading the original work.

## 9. Reproduction

```bash
cd experiments/20260802-ksz-force-law
python task2_3d_kernel_derivation.py   # expected to FAIL its control — that IS the result
python ksz_exact_kernel_fit.py         # inside-only kernel (superseded, kept for the record)
python task1_full_kernel_refit.py      # FINAL: full kernel, 3 UV prescriptions
python task345_stats.py                # calibrated coverage, xi errors, bin policy
```

`dr6.hdf`, `xi_zbin2.dat` are the upstream public files, unmodified.

## 10. What would make this definitive

The **halo catalogue with positions and mass proxies** (public for SDSS/BOSS,
better with DESI). It removes the only systematic that more statistics cannot
fix: with positions one computes the pairwise acceleration by direct summation
under the three-term law, instead of assuming a point mass and correcting
geometrically. Runner-up, cheaper: the 5 and 15 Mpc bins the paper cuts — the
dipole signal scales as ℓ_d/r and lives at small separations.
