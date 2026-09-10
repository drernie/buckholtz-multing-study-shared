# FINDING P130 — The matter-Λ resonant transient: **`MECHANISM IDENTIFIED, NOT YET QUANTITATIVELY DERIVED`**

**Status:** built, ran cleanly after one self-caught float-equality bug;
result is honest and internally consistent, but does not complete the
user's original request.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P130_matter_lambda_resonance_characterization.py`

> User-directed: "попробуй построить genuinely independent hand-off, не
> из full system" (try to build a genuinely independent hand-off, not
> from the full system) — following `FINDING_P129`'s own skeptic-corrected
> conclusion that a hand-off must not be read off the already-solved full
> trajectory to count as independent evidence.

---

## What was tried first, and why it failed before a line of code was written

The plan was a small-perturbation, matter-dominated early-time
linearization (drop `pb³`, approximate `H(N)≈H0·exp(-1.5N)`).
**Reconnaissance, run before committing to that design** (Compute
First), killed it directly: `pb` does stay small throughout (peak
≈0.086 at N≈3), but `psi`/`dph`/`drA_hat`/`qm_hat` do **not** — they
undergo a violent, `~10⁷`–`10¹⁰`-fold amplification in a narrow window
around N≈11–16, for both k=0.3 and k=0.5. A small-perturbation
linearization assumes exactly what fails here.

## The mechanism

`rho_A(N) = C_MATTER·exp(-3N)` (matter) equals `Λ_cc` (the Λ-like
additive term) at

```
N_eq = -ln(Λ_cc / C_MATTER) / 3 = 11.512925
```

— a closed-form prediction from two **fixed constants**, computed
directly, never read off a solved trajectory. This is where `H(N)`'s own
friction is transitioning from matter-dominated decay toward its
late-time constant value — friction is weakest relative to the
perturbation-sourcing terms right around this transition, the same
qualitative setup as reduced-damping amplification (parametric
resonance / particle production during reheating in inflationary
cosmology; that formalism's quantitative machinery was not applied
here).

## Result

| | k=0.3 | k=0.5 |
|---|---|---|
| peak `\|psi\|` | 2.6436 | 11231.95 |
| peak location N | 13.455 | 13.620 |
| offset from `N_eq` | +1.942 | +2.107 |

- **Peak-N difference: 0.165 e-folds** — close, consistent with an
  approximately k-independent trigger (matter-Λ equality). The earlier
  coarse (0.1-resolution) reconnaissance found both peaks at *exactly*
  N=13.600 — this refined (0.005-resolution) scan shows that was a
  grid-resolution coincidence, not a true exact match. Reported
  honestly rather than kept as the more dramatic coarse number.
- **Peak-amplitude ratio: 4248.7** — same order of magnitude as
  `FINDING_P126`'s own `A_hat=6678.998` (`|log10(ratio)-log10(A_hat)|
  =0.20`, within a factor of ~3).

## One self-caught bug

`CONTROL 1`'s first pass failed on `coarse_n03 == RECON_PEAK_N03_COARSE`
— exact float equality on an `np.linspace`-derived value
(`13.600000000000001 ≠ 13.6`). Fixed with a `1e-6` tolerance; the
underlying numbers were already correct, only the comparison was wrong.

---

## Verdict — **`MECHANISM IDENTIFIED, NOT YET QUANTITATIVELY DERIVED`**

The matter-Λ transition triggers a resonant amplification that is
approximately k-independent in *where* it happens and strongly
k-dependent in *how strong* it is, with a magnitude in the right
ballpark to plausibly be the real origin of `A≈6679`. `FINDING_P127`'s
reduced system starts *after* this resonance and simply inherits its
outcome — this is the first time in the P127–P130 arc that the question
"why does the amplitude take the value it does" has a concrete,
partially-verified physical answer, rather than being an unexplained
input.

### Not established

- A genuinely independent, **quantitative** prediction of `A≈6679` —
  this file identifies *where* and roughly *how strong* the resonance
  is; it does not compute an amplification factor from first
  principles. The user's original request remains open, now more
  precisely scoped.
- Why peak `|psi|` specifically (rather than the late-time settled
  `qm_hat`, or some other combination) is the right proxy for the
  quantity that determines `A` — used here only as an order-of-magnitude
  plausibility check.
- A WKB / adiabatic-invariant calculation through the friction
  transition — the kind of machinery used for reheating/preheating
  particle production in inflationary cosmology — named as the concrete
  next step if this line is continued, not attempted here.
- Anything at Lambda values, or `(k, IC)` combinations, other than
  k=0.3/k=0.5's main case tested throughout `FINDING_P119`–`P129`.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.

---

## ADDENDUM (2026-09-10) — the `psi<->dph` coupling this file left out of its
## "not attempted here" step, quantified: real, ~2.5-4.9%, and Picard-convergent

**Labels:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive`
**Artifact:** `P130_ADDENDUM_driven_bogoliubov_picard.py`

**Continues:** this file's own §"Not established" — "A WKB / adiabatic-invariant
calculation through the friction transition... named as the concrete next
step, not attempted here." This addendum builds that machinery and uses it
to answer a narrower, prior question: does the `psi`-sourced coupling this
file's `dphdd` equation carries even matter for the resonant amplitude, or
is the amplification purely a property of the homogeneous (parametric) part?

### 1. The field redefinition that makes the machinery applicable

`P119`'s `dphdd` equation (`make_system_lna`) is a damped, driven oscillator:
```
dphdd + 3H·dphd + (kk²e^{-2N}+Vpp)·dph = source(ψ,ψ',drA_hat,pd)
```
The substitution `u ≡ a^{3/2}·dph` removes the `3H·dphd` friction term
exactly (standard for a canonical perturbation in an FRW-like background;
verified twice — direct substitution, and independently via `χ=u·a^{-3/2}`,
both giving the same result):
```
u'' + Ω²(t)·u = a^{3/2}·source(t)
Ω²(t) = [kk²e^{-2N} + Vpp] − (9/4)H² − (3/2)Ḣ
```
`H`, `Ḣ` are already computed at every step of `make_system_lna`'s own
`rhs()` — no new physics, only bookkeeping. `[VERIFIED-sympy]`: the
variation-of-parameters step needed to solve this via Green's-function-style
driven-Bogoliubov (α',β' from the homogeneous adiabatic-mode pair, sourced
by the driving term) was verified symbolically before any numeric run —
`u''+Ω²u−F` reduces to `0` identically, not assumed.

**A boundary this redefinition surfaced, not previously known:** `Ω²(N)`
goes negative for `N∈[15.108,18.0]` (k=0.3) and `N∈[15.162,18.0]` (k=0.5) —
a *second* tachyonic window past the resonance peak (distinct from the
low-`k` one found separately). The standard "read `β` at `t→∞`" Bogoliubov
recipe does not directly apply there; `β` should be read off right after the
peak (`N≈13.5-13.6`), while `Ω²>0`, not at late `N`.

### 2. Why a pointwise check of the source term is misleading here

A first, cheap diagnostic — comparing `|F(t)|` to `|Ω²(t)·u(t)|` pointwise,
on the real `ψ(t)` trajectory — gave `|F|/|Ω²u| ~ 1e-6` at the resonance,
suggesting the source is negligible. **This proxy is wrong by 4-5 orders of
magnitude.** A resonantly-unstable window can integrate even a tiny
per-instant forcing into a large accumulated effect — the same reason a
weak but phase-locked force produces secular terms in perturbed orbital
mechanics. Do not use a pointwise `|F|` vs. `|Ω²u|` ratio as a proxy for
the *integrated* contribution of a source term in a resonant system;
compute the actual driven solution.

### 3. Real convolution / driven-vs-homogeneous decomposition

Solving `u''+Ω²u=F` with the REAL `F(t)` (built from the true, self-consistent
`ψ(t)` trajectory) reproduces `a^{3/2}·dph(t)` from the original 9-dim solve
to `<3×10⁻⁹` relative error — `[VERIFIED-REAL]`, confirms `Ω²`/`F` are
derived correctly, not a source of the numbers below.

Decomposing `u = u_hom (F=0) + u_p (source-only correction)`:

| | k=0.3 | k=0.5 |
|---|---|---|
| `\|u_p\|/\|u_full\|` at `ψ`-peak (N=13.4537/13.6188) | 4.665×10⁻² | 2.485×10⁻² |
| same ratio at window end (N=18) | 4.667×10⁻² | 2.488×10⁻² |
| RMS ratio over N∈[9,18] | 4.667×10⁻² | 2.488×10⁻² |

**The source contributes a real, non-negligible ~2.5-4.9% correction to
`dph`, stable across the entire post-resonance window** (varies only in the
4th significant digit from N=12.45 to N=17.6+) — not a transient spike, a
locked-in fraction. The homogeneous/parametric mechanism still accounts for
`~95-97.5%` of the amplitude. **k-dependence, found live, not predicted in
advance:** the fractional contribution is *larger* at the smaller tested `k`
(4.7% at k=0.3 vs. 2.5% at k=0.5) — the opposite ordering from the
amplitude ratio itself (k=0.5 amplifies far more in absolute terms).

### 4. Genuine 2-step Picard iteration — converges fast, geometrically

The above uses the *exact* `ψ(t)` as the source (an algebraic identity, not
an iteration). A real Picard scheme, iterating the `(ψ,ψ',drA_hat,qm_hat)`
sub-system against successive `dph` approximations (background `pb,pd,H,Ḣ`
taken as real/exact throughout — `make_system_lna`'s own `pdd`/`H`/`Ḣ` never
depend on the perturbation sector, no backreaction at linear order):

`[VERIFIED-REAL]`, two independent regression controls, both run before any
iterate was trusted:
- psi-sector formulas, fed the TRUE `dph,dphd`, reproduce the true `ψ` to
  `2.3-2.8×10⁻¹¹` relative error.
- the `u`-equation, fed `F` from the TRUE `ψ`, reproduces the true `dph` to
  `0.9-2.4×10⁻⁹` relative error.

| | k=0.3 | k=0.5 |
|---|---|---|
| step 0→1 (`\|u¹-u⁰\|/\|u⁰\|`) | 4.881×10⁻² | 2.532×10⁻² |
| step 1→2 (`\|u²-u¹\|/\|u¹\|`) | 1.246×10⁻⁴ | 1.648×10⁻⁴ |
| ratio (step1→2 / step0→1) | 2.55×10⁻³ | 6.51×10⁻³ |
| `\|u¹-u_true\|/\|u_true\|` | 1.247×10⁻⁴ | 1.653×10⁻⁴ |
| `\|u²-u_true\|/\|u_true\|` | 1.392×10⁻⁷ | 5.183×10⁻⁷ |

**Picard convergence is geometric and fast**: each iteration shrinks the
error by ~150-400×. Two iterations already reach `~10⁻⁷` relative accuracy
against the true, fully-coupled trajectory — the ratio step1→2/step0→1
(`2.5×10⁻³`, `6.5×10⁻³`) matches the naive expectation `(step0→1)²` to
within a factor of ~2, consistent with ordinary Picard/Born-series behavior
for a genuinely small (not marginal) coupling constant.

### Verdict

```
psi<->dph coupling:  REAL, ~2.5-4.9% of the resonant amplitude, stable
                     across the post-peak window -- not the ~1e-6 the
                     naive pointwise proxy suggested (proxy invalidated,
                     see §2).
Picard iteration:    CONVERGES, geometrically, ~150-400x error reduction
                     per step -- the homogeneous/parametric mechanism is
                     the dominant (~95-97.5%) but not sole contributor.
New boundary found:  Omega^2(N) < 0 for N gtrsim 15.1-15.2 (both tested k)
                     -- a second tachyonic window past the resonance peak,
                     not previously identified; affects where a future
                     WKB/Bogoliubov beta-extraction should read off its
                     "out" state.
```

### What this addendum does NOT establish

- Does not complete the still-open request from this file's own Verdict —
  a genuinely independent, quantitative, first-principles prediction of
  `A≈6679` from a full WKB/adiabatic-invariant amplification-factor
  calculation. This addendum characterizes the *coupling*, not the
  amplification factor itself.
- The Picard scheme here holds the background (`pb,pd,H,Ḣ`) exact and only
  iterates the perturbation sector — correct at linear order (no
  backreaction), but the full nonlinear coupled system was never solved by
  any method other than the original 9-dim `run_lna` integration itself.
- Tested only at k=0.3/k=0.5, the same two points used throughout
  `FINDING_P119`–`P130`. The k-dependence of the source fraction (larger at
  smaller k) is reported as observed, not derived from a closed form.
- `NO_AUTHOR_ERROR`: entirely about this project's own reconstruction, not
  a claim about Dr. Buckholtz's own theory.

`REGRESSION/TESTS: ruff clean; pytest tests/ exit 0, no failures (baseline unchanged).`
