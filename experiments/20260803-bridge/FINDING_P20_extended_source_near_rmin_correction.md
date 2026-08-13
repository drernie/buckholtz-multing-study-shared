# P20 — the point-dipole self-energy formula deviates by ~5.7% from the exact extended source, at exactly the ratio this project's own convention uses; self-dominance survives, absolute-magnitude numbers get a real but moderate correction

**Date:** 2026-08-12 · directly answers the concern `FINDING_P19`'s own
skeptic review flagged and left open: `E_self` is dominated by `r~r_min`,
exactly where the point-dipole idealization (used to derive the `1/(4π)`
normalization) is weakest for a real, physically extended source. This
finding computes how much that actually matters, numerically, at the
specific `d/r_min` ratio this project's own convention implies.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P20_extended_source_near_rmin_correction.py`, ruff clean.
Positive control (exact two-charge integral converges to the point-dipole
formula as `d/r_min→0`, to `1e-5` precision) must pass before the
realistic-regime result is trusted. Convergence in the integration's
outer radius checked independently (stable to 6+ significant figures).

**[CORRECTED after skeptic review — read before the rest of this file]**
A context-blind skeptic review raised two legitimate, well-reasoned
concerns and one fair critique of an unverified assertion: (1) whether
the numeric ratios at the largest tested `d/r_min` (`1.5`, `1.9`) were
actually numerically reliable, given a sharp, narrow near-pole feature in
the integrand the original convergence check (run only at `d/r_min=1.0`)
never stress-tested; (2) whether `FINDING_P14`'s own prose ("the
cluster's own physical size") is genuinely ambiguous about whether
`d/r_min=1` is really this project's convention, versus a possible
`d/r_min=2` reading; (3) that the cross/self "safety" claim was asserted
on physical grounds, not independently computed. Concerns (1) and (2)
were checked directly and the original results survive; (3) is a fair
critique, corrected below.

## The gap this addresses

`FINDING_P14` §2 states plainly: *"this project's own construction
(`two_charge_completion.py`) identifies the internal charge-separation
length with `r_A` itself, so `r_min=r_A` ... is the principled choice."*
That is: `r_min` is set **equal to** the two-charge dipole's own
charge-separation distance `d`. This is exactly `d/r_min=1` — nowhere
near the `d/r_min→0` point-dipole limit `FINDING_P19`'s normalization was
derived for. `FINDING_P19`'s own skeptic flagged this as an unaddressed
possibility; this finding tests it directly rather than leaving it as a
named-but-unexamined concern.

**[CORRECTED after skeptic review.]** The skeptic pointed out that
`FINDING_P14`'s parenthetical "(the cluster's own physical size)" could
colloquially be read as a *radius* (half the separation), which would
imply `d/r_min=2` — the divergent boundary — rather than `d/r_min=1`.
Checked directly against the actual code, not just P14's prose:
`two_charge_completion.py`'s own §"MAP" (line 158) substitutes
`{dA: rA, dB: rB}` — a direct, unambiguous identification of `r_A` with
the **full** charge separation `dA` (the same convention used throughout
this script, charges at `±d/2`), with no factor of 2 anywhere in that
mapping. **`d/r_min=1` is the project's own actual, code-level
convention — P14's prose could be clearer, but the underlying
construction is not ambiguous.**

## Method

Built the **exact** field of two point charges `+q` at `z=+d/2` and `-q`
at `z=-d/2` (matching `two_charge_completion.py`'s own construction,
dipole moment `p=qd`), using the correctly-normalized Green's function
`φ=q/(4πr)` established in `FINDING_P19`. Numerically integrated the
exact field energy `∫_{r≥r_min}|∇φ_total|²d³x` (for `r_min>d/2`, the
integration domain naturally excludes both point-charge singularities —
no extra regularization needed), and compared directly against the
point-dipole approximation `E_self=(8π/3)p²/(4π)²/r_min³` used throughout
`FINDING_P14`/`P15`/`P16`/`P17`.

**Positive control** — as `d/r_min→0` (the true point-dipole limit), the
exact integral must converge to the point-dipole formula:

```
d/r_min=1e-04: ratio(exact/point-dipole) = 0.99999999
d/r_min=1e-03: ratio(exact/point-dipole) = 0.99999999
d/r_min=1e-02: ratio(exact/point-dipole) = 0.99999999
```

Converges to `1.0000000` exactly, as required.

**Realistic regime** — `d/r_min~O(1)`, including the project's own stated
value `d/r_min=1`:

```
d/r_min=0.10: ratio = 1.000005
d/r_min=0.30: ratio = 1.000434
d/r_min=0.50: ratio = 1.003361
d/r_min=0.90: ratio = 1.036581
d/r_min=1.00: ratio = 1.056976   <- this project's own stated convention
d/r_min=1.50: ratio = 1.389991
d/r_min=1.90: ratio = 4.512144
```

**Convergence check** (outer integration radius, at `d/r_min=1.0`):
stable to 6+ significant figures by `R_max=5000` (used throughout above;
`R_max=100000` changes the 8th significant figure only).

**[Added after skeptic review.] Stress test at the two largest,
most-scrutinized ratios (`d/r_min=1.5` and `1.9`).** The skeptic
correctly noted that as `d/r_min→2`, points on the cutoff sphere near the
poles (`θ→0,π`) approach the charges' own locations, creating a narrow,
sharp feature in the integrand (analytically estimated: angular width
`~0.03` rad, peak `~10⁴×` the equatorial value at `d/r_min=1.9`) that the
original convergence check — run only at `d/r_min=1.0`, where no such
sharp feature exists — never stress-tested. Checked directly, three
independent ways, at `d/r_min=1.9`:

```
tolerance refinement (epsrel 1e-9 -> 1e-13, R_max fixed): ratio = 4.512144 (all cases, unchanged)
R_max refinement (500 -> 100000, epsrel fixed):            ratio = 4.512136 -> 4.512144 (converged)
manual angular subdivision (explicit fine bins near theta=0,pi): ratio = 4.512144 (exact match)
```

All three agree to the reported precision. The same check at
`d/r_min=1.5` also confirms `ratio=1.389991` under both looser and
much tighter tolerances. **The originally reported values at `d/r_min∈
{1.5, 1.9}` are numerically reliable, not just directionally correct** —
`scipy`'s adaptive quadrature resolved the near-pole feature correctly,
independently confirmed by forcing explicit resolution of that exact
region.

## Result

**At the project's own stated convention, the exact self-energy is
`1.0570×` the point-dipole approximation — a real, computed `~5.7%`
correction, growing sharply toward the physical boundary
(`d/r_min→2`, where the charges sit directly on the cutoff sphere).**
This confirms the concern `FINDING_P19`'s skeptic raised is real and
numerically significant at the ratio this project actually uses — not
merely a theoretical possibility.

**Consequence for the cross/self ratio (`FINDING_P15`/`P16`/`P18`):
~~safe, and if anything strengthened~~ [CORRECTED after skeptic review]
plausibly safe on physical grounds, not independently verified here.**
The argument — the correction makes `E_self` *larger*, which makes
cross/self *smaller*, so self-dominance is understated rather than
undermined — rests on the assumption that the cross-term itself is
unaffected, because `FINDING_P15`/`P16` computed it at large inter-cluster
separations (`~20:1`), well into the point-dipole far-field regime where
multipole corrections should be small. **This is a reasonable physical
argument, but this finding does not compute the cross-term correction the
same way it computed the self-energy correction** — doing so (an exact
two-dipole cross-integral at realistic separation, analogous to this
script's own method) would convert "asserted" into "shown," and is a
natural, cheap follow-up this finding stops short of.

**Consequence for absolute magnitudes (`FINDING_P14`/`P17`): a real but
moderate correction, not a resolution of the larger open problems.**
`Ω_φ` and `κ_cosmo_bound` should, in principle, be corrected by this
`~1.057×` factor at the project's own `d/r_min=1` convention. This is
genuinely smaller than the other uncertainties already flagged — κ's own
unfixed scale (orders of magnitude) and the missing dimensional
normalization constant (`FINDING_P17`, currently unbounded) — so it does
not change the qualitative status of either open problem. No corrected
numeric `Ω_φ`/`κ_cosmo_bound` value is computed here, consistent with
`FINDING_P19`'s own discipline of not implying a partial correction
resolves a larger open problem.

## What this does NOT establish

1. **A resolution of `FINDING_P17`'s dimensional problem or `FINDING_P14`'s
   κ-unfixed problem.** Both remain exactly as open as before; this
   finding adds one more, much smaller, correction to a number that is
   still not absolutely trustworthy for other, larger reasons.
2. **A precise correction factor for real clusters.** This uses an
   idealized two-point-charge model at a specific `d/r_min` value; real
   clusters are not literally two point charges, and the true internal
   mass/charge distribution could give a numerically different (though
   likely similarly-signed and similarly-scaled) correction.
3. **That the renormalization/regularization concern from `FINDING_P18`'s
   skeptic review is addressed.** This finding is about finite-size
   (extended-source) corrections to a fixed `r_min`, not about taking
   `r_min→0` — a different question, still untouched.
4. **A general formula for the correction factor at arbitrary `d/r_min`.**
   Only spot values were computed; no closed-form fit was attempted.
5. **[Added after skeptic review.] That the cross-term correction is
   negligible — only that it is plausibly so.** The safety argument for
   `FINDING_P15`/`P16`'s cross/self conclusion is physical reasoning, not
   an independent computation of the same kind performed here for
   self-energy.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic verdict (Step 8a, context-blind — claim + code + cited files only)

Two separate verdicts, not merged:

**(1) Math/numerical content: CONFIRMED-REAL, with two concerns raised and
both independently resolved.** The skeptic independently re-derived the
point-dipole formula by hand and confirmed the setup. Two specific
concerns: (a) whether the `d/r_min∈{1.5,1.9}` numbers were numerically
reliable, given a sharp near-pole feature the original convergence check
never stress-tested — checked directly, three independent ways (tolerance
refinement, `R_max` refinement, manual angular subdivision), all confirm
the original values exactly; not falsified. (b) whether `d/r_min=1` is
genuinely this project's convention, given `FINDING_P14`'s own
potentially-ambiguous prose — checked directly against
`two_charge_completion.py`'s own code (the `{dA:rA}` mapping), confirmed
unambiguous; not falsified.

**(2) Interpretive claims: WEAKENED on one specific point, CONFIRMED-REAL
otherwise.** The claim that a real, numerically-significant correction
exists at the project's own convention is CONFIRMED-REAL, now with
additional stress-testing evidence. The absolute-magnitude scoping
("moderate, does not resolve the larger open problems") is CONFIRMED-REAL
and was already appropriately hedged. The cross/self "safe, if anything
strengthened" claim is WEAKENED — the *direction* of the argument is
sound, but it was asserted on physical grounds rather than independently
computed the same way this finding computed the self-energy correction;
downgraded to "plausibly safe, not independently verified here," with the
missing computation named as a natural next step. Applied per Response
Matrix: two stress-test sections added (Fix, both confirm the original
work), `r_A` ambiguity resolved via direct code check (Fix), cross/self
claim downgraded (Fix), new "does NOT establish" item added. No response
fell to core-predicate-false — every numeric result in this finding
survives independent re-verification.

## Reproduction

```bash
python experiments/20260803-bridge/P20_extended_source_near_rmin_correction.py
```

The positive-control assert must pass before the realistic-regime numbers
are trusted.
