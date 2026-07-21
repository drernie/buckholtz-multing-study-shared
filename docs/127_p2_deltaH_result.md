# docs/127 — P2 Constructive Test: ΔH(a) Result

**Date:** 2026-07-21
**Status:** `docs/126` non-uniqueness lemma **FALSIFIED for the Shtanov–Sahni
background closure** — ΔH(a) = 0 exactly. This is a self-critical negative result
against our own lemma, with a passing positive control.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Artifact:** `scripts/p2_closure_deltaH.py` (numeric toy + positive control) +
symbolic `G_αβ` limits (sympy, inline). exit 0, ruff clean.
**L0:** descriptive/mathematical.

---

## Result

| Closure | ΔH (max frac) | Meaning |
|---|---|---|
| **REAL** Shtanov–Sahni background (Sec. II ä/a) | **0.000e+00** (machine zero) | q(a) does not enter background H |
| **CONTROL** deliberately-wrong (q does not wash out) | 7.3e-02 (nonzero) | the test *can* detect non-uniqueness — so the null is physics, not a broken test |

The two admissible laws were `q₁(a)=1` (frozen, `dq/da=0`) and `q₂(a)=a²` (virial
`q ∝ GM²` with `M ∝ a`, `dq/da=2a`), sharing identical initial data `q(1)=1`
(docs/126 A5). Under the real closure they give **bit-identical** H(a).

## Why (the decisive computation)

Shtanov–Sahni's background coupling for a pair kernel `φ = -(G/r)f(r)` is
`G_eff = G·lim_{r→∞}[f - r f']` (their Eq. 22). Computed symbolically (sympy) for
each MULTING multipole:

| Multipole | kernel `φ` | `f(r)` | `G·lim[f-rf']` |
|---|---|---|---|
| monopole (mass) | `-G/r` | `1` | **G** |
| dipole (cross) | `∝1/r²` | `∝1/r` | **0** |
| quadrupole | `∝1/r³` | `∝1/r²` | **0** |

The dipole and quadrupole couplings vanish **for any coefficient `k`, including a
time-dependent `k=k(a)`** — the `r→∞` limit kills them regardless of evolution. So
the background `ä/a = -(4πG/3)ρ_m + Λ/3` couples to the **mass density only**;
`q(a)` enters nowhere. This matches Shtanov–Sahni's own three worked examples, all
of which give `G_eff = G` (their Eq. 30) for sub-`1/r` corrections.

## What this means (three honest statements)

1. **The docs/126 lemma is FALSIFIED for the S–S background closure.** The missing
   evolution law `q(a)` does **not** make the background `H(z)` ambiguous under this
   closure. The background `H` is **uniquely** `G_eff=G` (ΛCDM-like) — the whole
   `F_d`/`F_q` (dipole/quadrupole) apparatus contributes **zero** to background
   expansion.

2. **This validly re-derives what NR-016 got by an invalid route.** NR-016's naive
   single-kernel *mapping* was wrong (per-pair non-factorization), but its
   *conclusion* — "dipole/quadrupole absent from background H(z)" — is now
   established correctly, via the proper `G_αβ` computation for the matrix kernel
   with time-dependent `q`. The skeptic's "no conserved background `ϱ_q`" objection
   (docs/125) is real but **moot for the background**: you do not need a background
   for `ρ_q` when its coupling to `ä/a` is identically zero.

3. **The physical obstruction was aimed at the wrong observable.** The `q`-freedom,
   whatever it does, cannot be seen in background `H(z)` under this closure. If a
   MULTING cosmological signature exists, it lives in **Sec. III structure-formation
   observables** (peculiar velocities, growth `fσ₈`) — consistent with this
   project's earlier `beta_cv.py` pearl ("MULTING dipole degenerate with ΛCDM at
   first perturbative order; distinguishable only at second order").

## Scope caveats (what is NOT claimed)

- **C1 — Scoped to the S–S background closure.** A genuinely different closure —
  full covariant completion, or an N-body treatment that keeps the dipole's **odd
  (anisotropic) vector character** rather than the scalar-radial form used here —
  could reintroduce `q`-dependence. Non-uniqueness for *arbitrary* closures is
  **not** settled; only the S–S background route is.
- **C2 — Falsifies the lemma, does NOT prove a no-go.** "Background H is unique
  under S–S" is the opposite of a no-go; there is no under-determination to exploit
  *at the background level*. The old P4 (scoped no-go on non-uniqueness) is **moot
  at the background level** — there is nothing to prove non-unique.
- **C3 — The control is illustrative.** The positive control's specific 7.3% is not
  physical; it exists only to show the test detects ΔH≠0 when `q` genuinely enters.
- **C4 — Toy background.** A flat Ωm=0.3/ΩΛ=0.7 toy; the ΔH=0 result is exact and
  independent of these numbers (q enters no term), so the toy choice does not affect
  the verdict — but a full treatment would carry the real S–S energy-equation
  machinery, not a bolted-on Friedmann form.

## Consequence for the priority ladder

The P1→P2→P4 line (prove non-uniqueness → scoped no-go) is **closed at the
background level**: under the S–S closure the background `H` is unique and
`q`-blind, so there is no background non-uniqueness to prove and no background no-go
to state. The correctly-scoped open questions that survive:

- **P3 (redirected):** does the `q(a)` freedom affect **structure-formation**
  observables (`fσ₈`, peculiar-velocity statistics) — the Sec. III route — where the
  dipole/quadrupole are NOT guaranteed to wash out? This is the only place a MULTING
  cosmological signature could live, given P2.
- **P5 (unchanged):** Candidate G remains an independent phenomenological benchmark.
- The covariant-completion question (former P4/P5) is the only route that could
  overturn C1 — a different closure keeping the dipole's vector character.

**Net:** the audit conclusion sharpened from "MULTING's H is ambiguous" (the lemma,
now false) to a cleaner, stronger statement — **under the Shtanov–Sahni background
closure, MULTING's dipole/quadrupole/isomer machinery is invisible to the background
expansion; H(z) is uniquely ΛCDM-like, and any signature must be sought in
structure formation, not H(z).** This is a NOT_REFUTATION statement about our
reconstruction under one closure, not about TJB's theory.

## Verification status

Symbolic `G_αβ=0` (sympy) + numeric ΔH=0 with a passing positive control + agreement
with Shtanov–Sahni's own Eq. 30 examples. This is same-session self-verification;
the next independent rung (per `falsification-ladder.md` Independent Verification
Strength Ladder) would be an independent human/textbook check of the `G_αβ=0`
background-coupling claim, or an independently-coded N-body background that keeps the
dipole anisotropy (which would test caveat C1).

## Independent verification of G_αβ=0 (2026-07-21, user-requested)

The original `G_αβ=0` used Shtanov–Sahni's `G_eff = G·lim_{r→∞}[f−rf']` — one
derivation. Re-running that formula, or the divergence route (`∇·g = −∇²φ`, the same
physics S&S used), is only Weak–Medium on the Independent Verification Strength
Ladder. `scripts/verify_Gab_independent.py` re-derives the result by a genuinely
**different method** ("independently-written derivation" = Strong): direct
Monte-Carlo summation of Newton's force law on a test particle displaced from the
centre of a uniform spherical shell — **no potential, no Laplacian, no S&S formula**.

Results (all MC-measured, nothing analytic injected):
- **Angular factor** `⟨1−(n+1)cos²θ⟩` measured by brute-force finite difference:
  `0.00000` (n=2), `−0.33333` (n=3), `−0.66667` (n=4) — matches `(2−n)/3` exactly.
- **Built-in control:** the monopole (n=2) factor is `0` — the MC independently
  reproduces Newton's **shell theorem** (exterior shells exert no interior force), so
  the machinery is sound; the monopole background comes from ENCLOSED mass instead.
- **Radial scaling** measured by MC at R=1,2,4,8: per-source tidal coeff `∝ R^−(n+1)`;
  the bulk shell weight `R²·coeff` **shrinks** with R for n=3,4 → far/background
  matter contributes nothing → `G_dipole = G_quad = 0`.

**Two independent methods (S&S limit + brute-force MC) agree**, and the MC carries
its own positive control (shell theorem at n=2). The round values `0, −1/3, −2/3` are
the exact analytic angular factors the MC reproduced — a convergence of methods, not
a red flag (self-audited: `(2−n)/3` is the comparison target, never an input to the
force sum). The `∇·g` divergence route is NOT counted as independent (same physics as
S&S).

## Caveat C1 tested: anisotropic (vector) dipole N-body (2026-07-22, user-requested)

C1 was the one route that could overturn "background H is q-blind": P2 and the G_αβ
check reduced the dipole to a SCALAR radial `1/r³` force, but the MULTING dipole is an
ODD multipole — a genuine VECTOR (the preprint describes object-A as two
spatially-separated sub-masses, so the effect depends on the orientation of A's
internal axis). `scripts/c1_anisotropic_dipole_nbody.py` keeps the full anisotropic
force `F_dip ∝ [p_j − 3(p_j·r̂)r̂]/r³` (vector dipole moment `p_j = q·n̂_j`), sums it
over a uniform ball of objects, and measures the background tidal coefficient for two
orientation ensembles:

- **RANDOM (isotropic) orientations** — the physical background (A1): ensemble-mean
  tidal `= +0.085 ± 0.58 (SEM)`, **z-score +0.15σ → consistent with zero**. The
  monopole-dipole force is LINEAR in `p_j` and `⟨n̂_j⟩ = 0` for isotropic
  orientations, so the mean washes out **exactly** — a MORE robust mechanism than
  P2's scalar-radial limit (odd-multipole isotropy, not a limit artifact).
- **ALIGNED (∥z) control** — coherent, NON-isotropic: tidal `= +9.9` (definite,
  nonzero). So the anisotropic vector force IS real and the test detects it; the
  washout is a property of isotropic averaging, not of a broken/insensitive test.
- **Per-realization STD `= 36.6`** (can exceed the aligned value): the dipole's real
  dynamical action is LARGE fluctuations — the SECOND-ORDER (structure-formation)
  signal — consistent with the `beta_cv.py` pearl ("degenerate with ΛCDM at first
  order, distinguishable only at second"). Real physics, but NOT in background H(z).

**C1 does NOT overturn the result.** Keeping the full dipole anisotropy, an isotropic
background still gives a q-blind background H (mean tidal 0.15σ from zero). The ONLY
way to source the background is a globally coherent dipole alignment (a preferred
direction) — which violates isotropy (A1) and is independently excluded by CMB
isotropy. Tidal/partial alignment is a perturbative (structure) effect → second
order, not background.

## Verification status — closed rungs

The "background H is q-blind under the S&S closure" conclusion is now robust to:
(a) time-dependent `q(a)` (P2, ΔH=0); (b) the same-formula-independence concern
(brute-force MC, its own shell-theorem control); (c) the scalar-radial-reduction
concern (C1, full vector dipole N-body, its own aligned control). The only remaining
rung on the Independent Verification Strength Ladder is an **external human/textbook
or blind-replication** check — inherently outside a single session. All three
in-session independent routes agree.
