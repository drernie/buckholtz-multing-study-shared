# CLAIM P223 — does v82's own single-pair kinematic bridge keep
# k_A(z)-dependence in H(z), and does docs/127's S-S closure say
# anything about that construction specifically?

**Date:** 2026-09-12
**Continues:** `docs/153` §0/§3a (causal-compatibility bottleneck),
`FINDING_P156_v82_bridge_vs_ss_closure.md`, `FINDING_P157_
representative_pair_vs_population_average.md`, `FINDING_P189_finite_r_
preconditions.md` (a shortcut attempt, killed by skeptic — see below).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive/mathematical

---

## Primary-source equations (read directly, this session,
## `data/source_material/buckholtz_202608.0943v1.v82.md` lines 226-320 —
## not `docs/149`'s paraphrase)

```
F_P    = F^(0) - F^(1) + F^(2)                                    (1)
F^(0)  = -G m_A m_P / s^2                                         (2)
F^(1)  = -G beta_1 c^-2 (k_A m_P r_A + m_A k_P r_P) / s^3         (3)
F^(2)  = -G beta_2 c^-4 (k_A k_P r_A r_P) / s^4                   (4)

m_P (d/dt)(v_P) = F_P + (dm_P/dt)(u_P - v_P)                      (6)
mu_reduced * s_ddot = F_P + mu_reduced * [correction]              (7)
  mu_reduced = m_A m_P / (m_A + m_P)

a_ddot/a = s_ddot(z)/s(z)                                         (8)
dz/dt = -(1+z) H(z)                                               (9)
```
integrated to `H(z)^2 - H0_anchor^2`, `H0_anchor := s_dot(0)/s(0)`.

**Load-bearing structural fact, confirmed directly against the primary
text, not inferred:** `s(z)` is a SCALAR (the "characteristic distance
between adjacent cosmic-web nodes"), and `F_P(s)` (Eqs 1-4) is a pure
scalar radial force with no angular/orientation variable anywhere in the
construction — this is a *modeling choice already made in v82's own
Eqs. 1-4*, not a result of any averaging step. This sharpens `FINDING_
P157`'s own finding (v82's `F^(1)` is "a pure product of scalar
magnitudes with no angular variable") into a fully traced primary-source
fact, and means the "aligned vs. random orientation" vocabulary this
session explored earlier (`c1_anisotropic_dipole_nbody.py`, `FINDING_
dipole_shell_is_a_double_layer.md`) does not apply to v82's own equations
at all — there is no orientation degree of freedom in Eqs 1-9 to average
over in the first place. (This session's own documented false start —
mis-mapping "ALIGNED" from `c1_anisotropic_dipole_nbody.py` onto v82's
construction — is now understood precisely: it conflated a *different*
question, orientation-averaging of a vector dipole population, with
v82's actual construction, which has no such vector at all.)

## Already-known, load-bearing empirical fact (not new — `FINDING_P156`,
## re-cited here because it is directly decisive)

`FINDING_P156`'s own reading of v82's Table IIIa: **the monopole (`F^(0)`)
share of the force budget is only −0.05% to −0.06% at all four tabulated
redshifts; the `k`-dependent tiers (`F^(1)`, `F^(2)`) dominate 96–99.65%.**
By Eqs. (1)/(7)/(8) above, this force feeds `s_ddot` directly, hence
`H(z)` directly — there is no cancellation step anywhere in v82's own
literal construction. **v82's own published bridge manifestly, and
overwhelmingly, keeps `k_A(z)`-dependence in `H(z)`** — this half of
`docs/153` §0's question is already empirically settled by v82's own
Table III and does not need re-deriving; P223's job is the symbolic
confirmation (§ below) plus the actual comparison to `docs/127`.

## The falsifiable claim

**H1 (symbolic confirmation, cheap, expected to pass):** solving Eq. (7)
for `s_ddot` with the full `F_P` from Eqs. (1)-(4) and substituting into
Eq. (8) gives an `H(z)^2` expression in which the `F^(1)`/`F^(2)`
(`k_A(z)`-dependent) terms appear with NO symbolic cancellation against
`F^(0)` — i.e., the coefficient of the `k`-dependent pieces in `H(z)^2`
is nonzero for generic `k_A(z), k_P(z)`, matching Table IIIa's own
96-99.65% dominance figure qualitatively (this is the "does it survive"
half already answered empirically above, now to be shown symbolically).

**H2 (the actual comparison, the genuinely new step):** re-derive the
population-averaged `G_alpha_beta` for the SAME `F^(1)`/`F^(2)` functional
forms (Eqs. 3-4, same `1/s^3`, `1/s^4` power laws already tier-matched
to MULTING's own kernel in `FINDING_P156`), using `docs/127`'s own method
(`G_eff = G * lim_{r->infinity}[f(r) - r f'(r)]`, `scripts/p2_closure_
deltaH.py`'s own machinery) — reproduce `G_alpha_beta = 0` for both
tiers exactly (this MUST reproduce `docs/127`'s own published result
bit-for-bit; failure to reproduce it would mean this file's own
re-implementation is wrong, not that `docs/127` is wrong).

**H3 (the synthesis):** H1 and H2 together, if both confirmed, establish
that v82's own single-pair bridge and this project's own S-S population
closure are not in numerical or logical CONTRADICTION with each other —
they are answers to two DIFFERENT mathematical questions about the same
microscopic force law (one pair's deterministic kinematics vs. an
isotropic population's mean coupling), and `docs/127`'s `G_eff=0` result
therefore says NOTHING about v82's bridge construction, one way or the
other — not because the calculation is unfinished, but because it is
answering a different question by its own construction. This directly
answers `docs/153` §0's causal-compatibility question: **CATEGORICALLY
SEPARATE**, not compatible, not incompatible in the contradicting sense.

## What would falsify H1/H2/H3

- H1 is falsified if the symbolic `H(z)^2` expression shows the `k`-
  dependent terms canceling or vanishing identically for generic
  `k_A(z)`, `k_P(z)` — this would contradict Table IIIa's own 96-99.65%
  figure and require reconciling the discrepancy before anything else.
- H2 is falsified if the re-derived `G_alpha_beta` for Eqs. 3-4's own
  power laws does NOT reproduce `docs/127`'s `0` — this would mean
  either this file's re-implementation has a bug, or the tier-match
  claimed in `FINDING_P156` is not as exact as reported (both would be
  real, useful findings, not failures to hide).
- H3 is not itself independently falsifiable beyond H1+H2 holding — it
  is the interpretive synthesis of both, stated so a reviewer can check
  whether it follows validly from H1+H2 (Recomposition Gate) rather than
  smuggling in an unstated assumption.

## Controls

- **Positive control:** the monopole-only case (`F_P = F^(0)` alone,
  Eq. 2) run through the SAME Eq. 7-9 machinery should reproduce a
  standard matter-dominated `H(z)^2 ~ (1+z)^3`-type scaling (or the
  specific form `docs/149`'s own description implies) — sanity-checks
  the kinematic-translation code before trusting the full 3-tier result.
- **Cross-check control (doubles as H2):** re-deriving `docs/127`'s own
  `G_alpha_beta=0` result via this file's own re-implementation, not
  copying the prior number — must match exactly.

## What this does NOT establish

1. Not a claim about whether v82's own theory is physically correct
   (`NO_AUTHOR_ERROR`) — entirely about whether two of THIS project's
   own reconstruction routes (S-S closure, single-pair bridge) can be
   directly compared, and if so, what that comparison shows.
2. Not a resolution of `docs/153` §3a preconditions 2 (tractability with
   existing machinery — answered affirmatively here, using v82's own
   equations directly rather than needing new machinery) or 3
   (cost/consequence — this calculation IS the answer to precondition 3
   for this specific route, not a separate estimate).
3. Not a claim that `docs/127`'s `G_eff=0` result is wrong or
   superseded — if H2 holds, `docs/127` stands exactly as published; it
   simply does not constrain v82's bridge, which is a different
   question.
4. Not a claim about which of the two routes (if either) correctly
   describes real cosmic structure — an ontological/mechanistic
   question this file does not touch (`docs/151` status separation:
   this file's own verdict is Empirical/Model-status only).

## Artifacts (to be produced)

- `P223_finite_r_single_pair_closure.py` — sympy derivation of H1
  (symbolic `H(z)^2` from Eqs. 1-9) and H2 (re-derived `G_alpha_beta`
  cross-check against `docs/127`).
- `FINDING_P223_finite_r_single_pair_closure.md` — result + Step 8a
  skeptic pass.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
