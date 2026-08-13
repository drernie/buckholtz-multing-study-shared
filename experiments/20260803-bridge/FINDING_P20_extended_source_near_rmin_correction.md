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

## Result

**At the project's own stated convention, the exact self-energy is
`1.0570×` the point-dipole approximation — a real, computed `~5.7%`
correction, growing sharply toward the physical boundary
(`d/r_min→2`, where the charges sit directly on the cutoff sphere).**
This confirms the concern `FINDING_P19`'s skeptic raised is real and
numerically significant at the ratio this project actually uses — not
merely a theoretical possibility.

**Consequence for the cross/self ratio (`FINDING_P15`/`P16`/`P18`):
safe, and if anything strengthened.** The correction makes `E_self`
*larger* than the point-dipole approximation, which makes cross/self
*smaller* — self-energy dominance is understated, not undermined, by the
point-dipole formula. `FINDING_P15`/`P16`'s qualitative conclusion (self
dominates at realistic separations) is unaffected in direction; if
anything, the true margin is slightly wider than reported.

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
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P20_extended_source_near_rmin_correction.py
```

The positive-control assert must pass before the realistic-regime numbers
are trusted.
