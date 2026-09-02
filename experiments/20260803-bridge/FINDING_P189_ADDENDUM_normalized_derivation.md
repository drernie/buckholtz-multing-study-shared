# FINDING P189 — Addendum: correctly-normalized c_d/c_q derivation

**Date:** 2026-09-02
**Trigger:** user explicit request, "попробуй пересчитать нормировку
c_d/c_q правильно" (try to correctly recompute the c_d/c_q
normalization), following P189's REJECT (see
`FINDING_P189_finite_r_preconditions.md`).
**Status:** WEAKENED (Step 8a Response Matrix — see below). ADDENDUM,
not a reopening of P189's verdict. P189's REJECT stands unchanged.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR

---

## What was asked, and what this does NOT claim

The user asked specifically to fix the normalization bug flagged in
`FINDING_P189_finite_r_preconditions.md` — P189's `precondition_3()`
guessed `c_d = (k/c²)·R` by analogy with v82's own `F1` coefficient and
got a units-mismatched, physically-absurd ratio to `G` (~1e37–1e75). A
units-consistent derivation now exists, replacing that guess. **But a
context-blind Step 8a skeptic pass (run before this was ever shown to
the user — see "Skeptic pass" below) found the framing overstated what
that derivation actually establishes, on two of its three strongest
points.** This write-up presents the corrected, weaker framing directly,
not the original overclaimed one — the overclaimed draft was never
finalized as a separate artifact.

**This addendum does NOT claim to answer `docs/153`'s 3 pre-conditions.**
`FINDING_P189`'s central objection — that `docs/127`'s `r→∞` limit is a
population-averaging construct, and reusing "r" for v82's single-pair
separation is a category error — is completely untouched by this work.

## The derivation

**Setup.** v82's own two-body force law (`multing_core.py::forces()`):
`F_total = F0 - F1 + F2`, monopole/dipole/quadrupole. The two MULTING
nodes are identical (`m_A = m_P = M`, one `M_of(z)` used for both).

**The choice made, stated as a choice, not a derivation.** There is no
unique, physically-forced way to turn a two-body mutual force law into a
single-source-style potential `φ(r) = -(G/r)f(r)` with `f(monopole)=1`
— multiple conventions are available:

- **This addendum's choice:** each identical node's own acceleration
  under the mutual force, `a = F_total/M` (dividing by each node's own
  mass, not the reduced mass). Integrating gives, at `β₁=β₂=0`,
  `φ(d) = -GM/d` exactly — the standard test-particle-in-a-source-field
  potential, so `f(monopole)=1` falls out with no rescaling needed.
- **The alternative rejected:** the two-body reduced-mass equation of
  motion, `s̈ = F_total/μ` with `μ = M/2` — the equation that correctly
  describes how the physical separation `d(t)` itself evolves in v82's
  actual dynamics. This gives `f(monopole) = 2`, not `1`.
- Other conventions (e.g. "each node sources half the field") are also
  available and were not worked out.

**This addendum's choice was selected because it reproduces
`docs/127`'s own convention — not because it is independently the
physically correct description of two identical, mutually-interacting
nodes.** For two identical bodies there is no privileged "source vs.
test particle" split; the reduced-mass convention is arguably the more
natural description of v82's actual physical setup (a genuinely
symmetric two-body problem), not the one used here. **This is a real,
acknowledged weakness, not a resolved question — flagged directly by
the skeptic pass below, and accepted after independent re-derivation
confirmed the alternative convention is equally defensible.**

The resulting (chosen-convention) `f(r)`:

```
f(d) = 1 - R·β₁·k/(M·c²·d) + R²·β₂·k²/(3·M²·c⁴·d²)
```

`c_d = -R·β₁·k/(M·c²)` (length), `c_q = R²·β₂·k²/(3·M²·c⁴)` (length²) —
dimensionally consistent, unlike P189's original guess. That much is a
real improvement over P189.

## Controls — downgraded after skeptic review: pass, but do not discriminate

**Positive control (as run):** at `β₁=β₂=0`, `f(r)=1` exactly and
`G_eff(r→∞)=G` exactly; with dipole/quad included, `G_eff(r→∞)` is
*still* exactly `G`. Both hold as hard sympy asserts.

**Why this control carries less weight than a first read suggests
(skeptic finding, independently re-verified):** the prefactor in
`f(r) = -d·φ(r)/(G·M)` was chosen *specifically* so that the pure-
Newtonian monopole term reduces to exactly `1`. Re-derived directly:
for any acceleration-divisor `μ` and any reference mass `M_ref` used in
the `f(r)` formula's denominator, the monopole term evaluates to
`M²/(μ·M_ref)` — which equals `1` if and only if `μ·M_ref = M²`. Setting
`μ = M_ref = M` (this addendum's choice) satisfies that by construction.
**The control cannot fail for this class of ansatz — it verifies
algebraic self-consistency of the chosen convention, not that the
convention is the physically correct one.** The negative control
(dipole `~1/d` vs. quadrupole `~1/d²` being distinct forms) is
similarly guaranteed by construction for any power-law correction
structure and does not discriminate a correct derivation from an
incorrect one either.

Both controls are still worth keeping in the script (they do catch a
real class of bugs — e.g. an arithmetic slip that broke the r→∞ limit
would have been caught) — but they should not be read as validating the
choice of convention, only its internal arithmetic.

## Numeric evaluation and instability — real, but not a new independent finding

Evaluated at v82's own real archive values (`M_of(z)`, `k_of(z)`,
`R_of(z)`, `d_of(z) = d0_m/(1+z)`), spotlighted `β₁=1.4335e10,
β₂=7.8067e17`, at `z=0`: `G_eff,total/G = +33.2`, itself a cancellation
between `G_eff,dipole/G = -1084.2` and `G_eff,quad/G = +1116.4` — the
"correction" terms are ~1000× *larger* than the monopole term. A ±10%
perturbation of `β₁` alone swings the total from +33.2 to −75.2 or
+141.6; ±20% swings it to −183.6 or +250.0 — sign-flipping,
order-of-magnitude-unstable.

**This is a real, computed fact about this specific construction at
these specific `β` values — but it is a corollary, not an independent
finding, and the corrected citation matters:** this project's own
`FINDING_P176_v82_real_chi2_hessian_degeneracy.md` already established
(2026-08-xx, real archive data, positive-controlled, `H0,anchor`-
independent to <0.1%) that **`β₁` and `β₂` are degenerate in v82's own
real fit** — a robust, previously-verified fact about exactly this
parameter pair. *(Note: an earlier draft of this addendum, before the
skeptic pass below, mis-cited this as `P133` — a different finding, about
this project's own separate `(A,g,κ)` action-closure parameters, not
v82's `β₁,β₂`. Caught by independently checking both files directly
before finalizing, per this project's own audit-verification-gate.md
discipline: a skeptic's claim is `[INFERRED]`, not `[VERIFIED]`, until
re-checked.)* Given a known degeneracy in exactly this pair, that *any*
function built from them is unstable along the degenerate direction is
close to expected, not a new discovery this addendum is entitled to
claim credit for. What this addendum adds beyond `P176` is only: a
concrete magnitude for the resulting cancellation and instability *in
this one derived quantity, in this one convention* — a narrower, more
modest contribution than "independent evidence of instability."

## Skeptic pass (Step 8a, context-blind)

Run before this finding was shown to the user, per this project's
standing discipline (especially warranted given `FINDING_P189`'s own
history). Given the claim and the full script, with no session history.
**Verdict: WEAKENED**, on three points:

1. **Positive/negative controls are tautological for this ansatz class**
   — re-verified independently above (the monopole-term=1 condition
   reduces to `μ·M_ref=M²`, trivially satisfiable by choice).
2. **The instability finding is a corollary of an already-established
   degeneracy, not new independent evidence** — the skeptic's own
   citation (`P133`) was wrong; re-checked directly and corrected to
   `P176` above. The underlying point (degeneracy → instability is
   expected, not novel) held up under independent verification even
   after fixing the citation.
3. **A further, different-shaped category-error risk**: integrating
   `F_total(d)` over `d` while holding `M, k, R, β₁, β₂` fixed at their
   `z`-evaluated values treats `d` as a free spatial displacement — but
   in v82's own model, `d_of(z) = d0_m/(1+z)` is tied to the *same* `z`
   that also sets `M, k, R`. This addendum's own construction is best
   read as "the force law's formal `r`-dependence at fixed epoch" (a
   defensible, common move — e.g. a potential snapshot at fixed cosmic
   time) — but that reading was never stated explicitly before the
   skeptic raised it, and doing so is an additional, undefended
   assumption layered on top of `FINDING_P189`'s original, still-open
   category-error objection, not a resolution of it. **Assessed as real
   but likely less severe than points 1–2**: unlike the original P189
   category error (reusing a population-averaging-limit variable for a
   single-pair separation, no available fix), this one has a plausible
   defense (fixed-epoch snapshot) — it just was not made until this
   review forced it, and is recorded here as an open, unresolved
   assumption rather than a settled one.

Response, per the Skeptic Response Matrix (`falsification-ladder.md`
Step 8a): points 1 and 2 are **accepted** (not disputed after
independent re-verification — this write-up is the corrected version,
not a defense of the original framing). Point 3 is **accepted as an
open, undefended assumption**, recorded rather than dismissed.

## Kill Analysis

**What is killed:** the framing (present in an earlier, unreleased draft
of this same addendum) that fixing P189's units bug amounts to a
"correct" derivation with independent, discriminating controls, and
that the resulting numerical instability is new evidence beyond what
this project already knew from `P176`.

**What is NOT killed:**
- A dimensionally-consistent `f(r)` now exists, replacing P189's
  units-mismatched guess — real, if modest, progress.
- `docs/127`'s own published asymptotic result — untouched.
- `FINDING_P189`'s central category-error objection — untouched, and
  now joined by a second, related but distinct framing question (point
  3 above) about treating `d` as a free spatial variable at fixed epoch.
- `FINDING_P176`'s β₁-β₂ degeneracy result — untouched, and is in fact
  the correct explanation for why this addendum's own numbers are
  unstable, superseding this addendum's original (wrong) attribution.

## What this does NOT establish

1. Not an answer to `docs/153`'s 3 pre-conditions — unchanged from
   `FINDING_P189`.
2. Not evidence that this addendum's normalization convention (single-
   node acceleration) is the physically correct one for v82's actual
   symmetric two-body construction — the reduced-mass alternative is
   at least equally defensible and was not chosen only because it does
   not reproduce `docs/127`'s convention.
3. Not new, independent evidence of instability beyond what `P176`'s
   β₁-β₂ degeneracy already implies for any function of these two
   parameters.
4. Not a claim about v82's own fit quality for its intended purpose
   (fitting `H(z)`) — this is about the stability of one *derived*
   quantity built on top of that fit, in one convention.
5. Not authorization for, or progress on, the actual finite-r closure
   calculation `docs/153` names.

## Artifacts

- `P189b_normalized_finite_r_derivation.py` — the derivation, both
  controls (hard asserts — now understood as testing arithmetic
  self-consistency, not convention correctness), numeric evaluation,
  and sensitivity sweep. Code and printed output unchanged by the
  skeptic pass; only the interpretation in this write-up changed.
- `FINDING_P189_finite_r_preconditions.md` — the original REJECT this
  addendum extends, kept unedited per this project's no-silent-
  correction convention.
- `FINDING_P176_v82_real_chi2_hessian_degeneracy.md` — the correct
  source for the β₁-β₂ degeneracy this addendum's instability finding
  is a corollary of.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
