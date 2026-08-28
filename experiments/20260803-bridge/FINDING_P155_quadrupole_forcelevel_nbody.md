# FINDING P155 — quadrupole (dipole-dipole) tier: force-level computation
# built and run, numerically consistent with washout — but analytically
# reducible to `P154`'s own linearity + independence argument, not a
# genuinely separate rigor tier

**Date:** 2026-08-28 (corrected same day, context-asymmetric skeptic
review)
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
(numerical/code-pipeline corroboration of `P154` §Step 3's elementary
claim — see §0 for why this is a narrower claim than "independent
confirmation")
**Verdict:** `QUADRUPOLE-FORCELEVEL-NUMERICALLY-CONSISTENT` (renamed from
an overclaiming `QUADRUPOLE-FORCELEVEL-WASHOUT-CONFIRMED` — see §0)
**Origin:** `FINDING_P154` §4/§"does NOT establish" item 5 explicitly
named this as the one remaining piece: "a full quadrupole-force N-body
sum analogous to `P154`'s own dipole Step 2 was not built" — the
quadrupole tier's isotropic washout had only been checked via an
elementary independence argument (`E[n̂_A·n̂_P]=0`), not a force-level
tidal-coefficient N-body sum in the same rigor class as `P154`'s own
dipole test or `docs/127`'s original `C1`.
**Script:** `P155_quadrupole_forcelevel_nbody.py` (symbolic sympy
derivation of the screened dipole-dipole force, 3 positive controls,
N-body isotropic-vs-aligned test with a second, fully-isotropic
robustness variant; ruff clean; does not touch the 881-test suite)

## 0. Correction (context-asymmetric skeptic review, same day) — this is
a numerical/code-pipeline corroboration, not a genuinely independent
rigor tier

A skeptic review found the central claim ("agrees with `P154`'s own
elementary independence argument, **independently**, at a **different
level of rigor**") overreaches. The dipole-dipole force `F_dd` is
**linear** in each of `p_src` and `p_test` separately — a property the
script's own positive controls incidentally verify, not a new fact this
file establishes. Given that linearity:

- **Step 2** (fixed test dipole, random background): `E[Σ_j F_dd(p_j)] =
  F_dd(Σ_j E[p_j]) = F_dd(0) = 0` follows from `E[n̂_src]=0` alone —
  this does **not** actually exercise the `E[n̂_A·n̂_P]` dot-product
  structure at all, since the test dipole is fixed, not random.
- **Step 3** (fully isotropic, both random): the vanishing follows the
  same way, from `E[n̂]=0` on either factor via independence — not
  specifically from the two-vector dot-product identity `P154` used.

**What P155 actually adds, accurately stated:** the numerical result
(consistent with zero, coherent control large and definite) is
*analytically derivable* from (a) `F_dd`'s linearity in each moment
(textbook property, positive-control-verified here) and (b) `P154`
§Step 3's own `E[n̂]=0` fact — it is not independent evidence for the
washout in the sense that a structurally different mechanism (the way
`docs/127`'s `C1` mechanism, orientation-cancellation, was genuinely
different from `P2`'s radial-asymptotic mechanism for the dipole tier)
would be. What it **does** provide, honestly: (1) a working, positive-
controlled force-level computation for the quadrupole tier — the actual
artifact `FINDING_P154` flagged as missing — and (2) a real check that
the sympy derivation chain (`Φ_dipole→U_dd→F_dd`) contains no hidden
nonlinearity or sign/algebra bug that could have produced a spurious
result; a nonlinearity bug would have shown up as a nonzero ensemble
mean, and did not. This is a **code-pipeline and internal-consistency
check**, not a second independent physical argument. §3/§4 below are
corrected to state this accurately; the verdict is renamed accordingly.

The skeptic separately confirmed the symbolic derivation (independently
re-derived by hand, including the `μ=0` aligned-case `F_dd,z=6/r₀⁴`
positive control) and the statistical treatment are both correct, and
that removing `sp.simplify()` (§2 below) introduced no numerical risk
(lambdify does not require simplified input; the positive controls
substitute concrete values before their own, separate, simplify calls).

## 1. Method — one consistent sign rule, applied twice, not composed

Per `two_charge_completion.py`'s own established structural fact
(2026-08-10, predates this session): MULTING's "quadrupole" tier
(`docs/125`'s `κ_qq` term) is the **dipole-dipole interaction** between
two objects' own dipole moments — "a genuine quadrupole moment of one
body cannot produce [it]; a product of two bodies' DIPOLE moments does,
automatically." So the force-level analog of `P154`'s dipole test needs
a **test object that itself carries a dipole moment**, not a bare mass.

Built from `P154`'s own, already-verified `Φ_dipole = −(p·∇)[e^{−μr}/r]`
by applying the **same** `+∇` convention (matching
`c1_anisotropic_dipole_nbody.py`'s own declared, opposite-of-textbook
sign — established and verified in `P154`) **twice more**, not by
independently guessing two new sign rules:

```
U_dd  = p_test · ∇[Φ_dipole(r; p_src, μ)]      (energy of test dipole in source's field)
F_dd  = +∇[U_dd]                                (force on the test dipole)
```

**Positive control 1** (`μ=0` must match the standard dipole-dipole
energy `[p_t·p_s − 3(p_t·r̂)(p_s·r̂)]/r³`, up to `P154`'s own documented
sign flip): `U_dd(μ=0) = +U_standard` **exactly** — this time the SAME
sign as the textbook formula (not flipped, unlike `P154`'s own `Φ`/`F`
convention) — a real, checked fact, not assumed to match either sign
blindly; both `+` and `−` differences were computed and compared.
**Positive control 2** (dimensional/scaling check): the aligned-case
`μ=0` force `F_dd,z = 6/r₀⁴` — a clean `1/r⁴` falloff, one power steeper
than the mass-dipole force `P154` tested (`1/r³`), exactly as required
by one additional derivative.

## 2. A self-caught performance snag, not a physics error (documented
per the same no-silent-correction convention, even though nothing here
was wrong)

The first attempt called `sp.simplify()` on the full third-derivative,
10-free-symbol `F_dd` expression — it did not return within 10+ minutes
and was killed. **This was never a correctness issue**: `sp.simplify()`
is a readability nicety for the *printed* formula, not a requirement for
`lambdify`'d numerical evaluation, which works identically on the raw,
unsimplified `sp.diff()` output. Fixed by removing the full-expression
simplify calls (`Φ_dipole` alone, already fast, was kept simplified;
`U_dd` and `F_dd` are left raw) and simplifying only the **small,
already-substituted** expressions the positive controls need — the
rerun completed in well under a minute. Recorded here because a stuck
9-minute background process is exactly the kind of state a future
session reading this file's history should not have to rediscover from
scratch.

## 3. Result

`N_OBJ=2000`, `N_REAL=2000`, `μ=1` (ball `[0.5,5.0]/μ`, the same
physically-relevant-scale regime `P154` used):

```
ALIGNED control (test dipole ∥z, all background dipoles ∥z, non-isotropic):
  tidal = -3.0027e+02   (definite, large — the test CAN detect a real signal)

RANDOM background orientations, test dipole FIXED along z:
  mean = +5.4995e+00 ± 7.22e+00 (SEM)   z = +0.76σ   (consistent with zero)

FULLY isotropic (test dipole's own orientation ALSO randomized per realization):
  mean = -3.5011e+00 ± 6.31e+00 (SEM)   z = -0.55σ   (consistent with zero)
```

Both isotropic variants — a fixed test-object orientation (matching
`C1`/`P154`'s own convention exactly) and a fully-symmetric fully-random
variant — are consistent with zero, while the aligned control remains
large and definite. Per §0's correction: this **numerically corroborates**
`P154`'s own elementary independence argument (`E[n̂_A·n̂_P]=0`) and
verifies the force-law derivation has no hidden nonlinearity or sign
bug — it is not a second, mechanistically independent confirmation the
way `docs/127`'s `C1` was for the dipole tier's *own* two mechanisms
(radial-asymptotic vs. orientation-cancellation); here, both P154's
elementary check and this file's force-level check reduce to the same
underlying fact (`E[n̂]=0` under isotropy) via linearity.

## What this file does NOT establish

1. **Not a claim about MULTING's own theory** (`NO_AUTHOR_ERROR`) —
   entirely this project's own reconstruction.
2. **Reuses `P154`/`C1`'s own filled-ball, uniform-density ansatz** — a
   population with genuine spatial-orientation correlations is not
   re-examined (already excluded on physical, CMB-isotropy grounds by
   `docs/127`'s own `C1` finding, not re-derived here).
3. **Does not scale-robustness-scan across `μ`** the way `P154` did for
   the dipole tier (`R_MAX∈{1,2,5,10,20}/μ`) — this file checks only
   `μ=1`; the elementary independence argument this confirms (`P154`
   §Step 3) is itself scale-independent (`E[n̂_A·n̂_P]=0` does not depend
   on `μ` at all, since it is a property of the orientation sampling,
   not the force law), which is the reason a separate scale scan was
   judged unnecessary here — but this is a judgment call, not an
   exhaustive check.
4. **Reduced statistics relative to `P154`'s own dipole headline run**
   (`N_OBJ=2000, N_REAL=2000` here vs. `4000/4000` there) — a deliberate
   cost reduction given the more expensive (unsimplified, third-
   derivative) force expression; the `z`-scores obtained (`0.76σ`,
   `0.55σ`) are comfortably below the `3σ` threshold either way.
5. **Together with `P154`, this provides both an elementary and a
   force-level numerical treatment of the quadrupole tier's isotropic
   washout** — per §0, these are not two mechanistically independent
   confirmations (both reduce to the same `E[n̂]=0` fact via linearity),
   so this pair should not be cited as "two independent lines of
   evidence" the way `docs/127`'s `P2`+`C1` genuinely were for the
   dipole tier. It does not, on its own or combined with `P154`,
   establish anything about `S2`'s other open questions (`P11`'s
   separate near-field finding, the local/structure-formation channel)
   — see `FINDING_P153`'s own "does NOT establish" list, unchanged by
   this file.
6. **Only the FORCE on the test dipole is measured, not the torque** —
   a source population exerts both on an extended test object; the
   force is what would enter a center-of-mass/background equation of
   motion (the physically relevant quantity for `S2`'s background-
   channel question), but this file does not address whether the
   torque channel behaves the same way, and does not argue it must.
7. **The entire chain (`P154`+`P155`) is scoped to `two_charge_
   completion.py`'s own interpretation** that MULTING's quadrupole tier
   is a cross-term between two different bodies' dipole moments, not a
   single-body rank-2 tensor. That interpretation is itself an inference
   from the preprint's own parametrisation, not an independently proven
   fact — already flagged as inherited, not re-derived, in `FINDING_
   P154` §4, and not re-litigated here. If that interpretation is wrong,
   a genuine single-body rank-2 quadrupole would **not** wash out
   isotropically (`⟨n_in_j⟩=δ_ij/3≠0`), and this entire closure would
   not apply.
