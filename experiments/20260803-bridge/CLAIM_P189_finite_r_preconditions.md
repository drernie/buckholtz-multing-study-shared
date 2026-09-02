**[STATUS UPDATE 2026-09-02] REJECTED — see `FINDING_P189_finite_r_
preconditions.md`.** A context-blind skeptic pass (Step 8a) found the
central shortcut below does not hold (category error on what "r" means
between the population-limit and single-pair regimes; the "nonzero at
finite r" result is a tautology of power-law functions, not a MULTING-
specific finding — verified independently with `sympy` before
accepting). Kept below exactly as originally written, per this
project's no-silent-correction convention.

# CLAIM P189 — Answering `docs/153` §3a's 3 pre-conditions for bottleneck 1's reopen

**Date:** 2026-09-02
**Trigger:** user explicit autonomous go-ahead, following today's Zenodo
21204955 archive indexing + `FINDING_P188` (accretion-term cross-check).
**Scope, explicitly bounded (per `docs/153`'s own text):** this answers
the 3 named pre-conditions — it is **NOT** the finite-r/single-pair
closure calculation itself, and does **not** constitute a GO on that
calculation. If the pre-conditions turn out favorable, that remains a
**separate** decision requiring its own explicit go-ahead, per `docs/
147`'s stop-rule and `docs/153`'s own closing line ("does not authorize
any specific next computation").
**L0:** descriptive — a scoping/feasibility question, not a new physics
claim about MULTING or v82.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR

---

## The 3 pre-conditions (verbatim from `docs/153` §3a)

1. Does a finite-r analog of the S-S closure calculation exist in closed
   form, or would it require a genuinely new derivation?
2. Is the single-pair, externally-oriented regime tractable with this
   project's existing machinery (`two_charge_completion.py`,
   `two_field_action_closure.py`)?
3. What would each outcome (compatible/incompatible) actually change
   about this project's own standing results — is the cost proportionate
   to the consequence?

## Falsifiable claim under test (pre-condition 1)

`docs/127`'s own closure quantity is `G_eff = G·lim_{r→∞}[f(r) - r·f'(r)]`
(their Eq. 22), computed per multipole tier from a scalar kernel
`φ(r) = -(G/r)f(r)`. The claim: **the same expression, evaluated at
finite `r` instead of taking the `r→∞` limit, is already a closed-form
function of `r`** — no new derivation is needed, only removing one
limit step from an already-derived formula. If true, pre-condition 1's
answer is YES (closed form exists) via the cheapest possible route.

**Falsifier:** if `f(r) - r·f'(r)` for MULTING's dipole/quadrupole
kernels does not have a well-defined value at finite `r` (e.g. requires
information not already present in `docs/127`'s own derivation, or the
"closed form" turns out to need re-deriving `f(r)` itself from scratch
for the single-pair non-averaged regime rather than reusing the existing
one), the claim is false and pre-condition 1's answer is NO.

## Positive control

Reproduce `docs/127`'s own asymptotic result first: confirm that taking
`lim_{r→∞}` of the same finite-r expression this claim computes
reproduces `G_eff(monopole)=G`, `G_eff(dipole)=0`, `G_eff(quadrupole)=0`
exactly, using `sympy`. If the positive control fails, the finite-r
expression itself is wrong and nothing downstream can be trusted.

## Negative control

Evaluate the same finite-r expression at a deliberately wrong kernel
power (e.g. a monopole-tier kernel treated as if it were dipole-tier) and
confirm it does NOT reproduce the dipole result — i.e. the calculation is
sensitive to which tier's kernel is used, not a tautology that returns
the same number regardless of input.

## Method for pre-condition 2 (tractability)

Check directly against the two named files' actual function signatures
(`two_charge_completion.py::interaction/series_uf`,
`two_field_action_closure.py::tiers_from_kernel`) — do they already
operate on a single pair at finite `r` (yes/no, from source inspection,
not inference), and can the finite-`r` `G_eff` expression from
pre-condition 1 be evaluated using kernel forms these files already
derive, or does it need a materially different construction?

## Method for pre-condition 3 (cost/consequence)

Evaluate the finite-r expression **numerically**, using v82's own real
values now available from the freshly-indexed supplemental archive
(`data/source_material/zenodo_21204955_supplemental/code/
multing_core.py`: `M0_kg`, `d0_m=45 Mpc`, `k_of(z)`, `R_of(z)`) at
`r = d0` (v82's own node-pair separation) and at `z=0`. Report the sign
and order of magnitude of the finite-r dipole/quadrupole "G_eff-analog"
relative to `G` itself, and state explicitly what this would or would
not change about `docs/127`'s own standing `G_eff=0` background-closure
result (which is an `r→∞`, population-averaged statement — a nonzero
finite-r value does not contradict it, per the Cheapest Differentiating
Test Protocol's own diagnosticity check: does this number actually
discriminate between "compatible" and "incompatible" readings, or does
it leave both still viable?).

## What this does NOT establish

1. Not a claim that v82's bridge and this project's S-S closure are
   compatible or incompatible — that is `docs/153`'s named NEXT question,
   gated separately.
2. Not a re-derivation of `docs/127`'s own asymptotic result, which
   stands unchanged — this only extends the same formula to finite `r`.
3. Not a claim about the vector/anisotropic (Caveat C1) orientation-
   averaging step, which is a structurally separate calculation from the
   scalar-radial `G_eff` this claim addresses (see `FINDING_P189` for
   why these are kept separate, if that distinction turns out to matter).

## Artifacts

- `P189_finite_r_G_eff_preconditions.py` — the calculation.
- `FINDING_P189_finite_r_preconditions.md` — the write-up, verdict, and
  explicit statement of what happens to `docs/153`'s 3 pre-conditions.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
