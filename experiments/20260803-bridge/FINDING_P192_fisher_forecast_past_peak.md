# FINDING P192 — the requested Fisher-forecast at z∈{20,30,50} is
# TASK_INFEASIBLE: TJB's own real fitted (β1,β2) make H²(z) go negative
# (mathematically undefined) at z≈16.96, well before any requested z

**Date:** 2026-09-05
**Continues:** `FINDING_P191`'s own Pearl Registry entry (`next_check`
2026-12-01) — the falsifiable prediction that synthetic z past the
level-set slope's own peak (found in P191, z≈3) would give a measurably
different realistic-σ shrinkage than P191's own z∈{3,5,7,10}.
**Authorization:** explicit user go-ahead, 2026-09-05 ("запусти второй
Fisher-forecast на z∈{20,30,50}").
**Script:** `P192_fisher_forecast_past_peak.py` (2 positive controls,
ruff clean, project's own 908 tests unaffected).
**Skeptic review:** dispatched context-blind (claim.md + script only) —
verdict **CONFIRMED-REAL** (static trace, no execution available to the
agent; independently re-verified by me with a real `pytest`/script run
before and after the skeptic pass, both stable). One real bug caught
**by this file's own positive control failing on a real pytest run**
(not by the skeptic) — see Correction below.
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** SUPPORTED — the boundary location
> (z≈16.957) is grid-converged (4 densities, spread <0.02) and
> straddle-confirmed (H²>0 just before, H²<0 just after).
> **Ontological/mechanistic interpretation status:** N/A — a structural/
> mathematical fact about the reconstructed model's own real fitted
> parameters, not a claim about physical mechanism.
> **Causal/cosmological claim status:** N/A (`NO_AUTHOR_ERROR`).

## Correction (2026-09-05, caught by a real pytest run failing, not by
review — the exact same failure class already caught once in `P191`)

The first version of `find_h2_negative_onset` located the boundary via
bisection, refining with `H2_of_z(np.array([0.0, z_mid]), ...)` inside
the loop — a bare 2-point array. `H2_of_z`'s cumulative-trapezoid
integration needs a real, densely-sampled path; a single 2-point
trapezoid from 0 to z_mid, integrated across a function
(`addot_over_a`) that changes sign partway through, is a wildly coarse
approximation. Running the positive control for real caught it
immediately: the straddle check failed (`H2(z-0.05)` and `H2(z+0.05)`
both came out negative — the bisection had converged to a wrong
point). **Fixed** by never calling `H2_of_z` again during refinement:
linear-interpolate the root directly from the single dense-grid `H2`
array already computed for the initial coarse localization. Also
strengthened the grid-convergence check itself from 3 densities to 4
(added npts=24000) after the first 3-point spread (0.0108) landed just
over an initially-too-tight 0.01 threshold — widened the sweep to
confirm genuine convergence rather than loosen the bar to hide possible
non-convergence.

## Result

Requested test could not be constructed: `augmented_chi2`'s own
convention (a synthetic point is pinned to "the fiducial model's own
prediction") requires `H_fid` at each `synth_z` — and at z∈{20,30,50},
`H_of_z_kms` returns `NaN` for all three, because `H²(z)` itself is
negative there (would require `sqrt` of a negative number).

```
H^2(z) sign flip: z=16.957 (grid-converged to <0.02 across 4 densities,
                             straddle-confirmed: H2(z-0.05)>0, H2(z+0.05)<0)
Requested z=20, 30, 50: all past this boundary -> H_fid = [NaN, NaN, NaN]
```

**Mechanism** (traced from `forces()`, not guessed): `F1` (dipole-like,
enters `addot_over_a` with a MINUS sign) and `F2` (quadrupole-like,
enters with PLUS) are both ~3×10³⁴ in magnitude at z~10-20 and nearly
cancel. Their differing z-scaling makes `(F0 - F1 + F2 - F_accretion)`
flip sign around z≈10-13 — `addot_over_a` goes from positive
(acceleration) to negative (deceleration). The cumulative integral of
that negative quantity, accumulated from `z_ref=0.0233` upward, drives
`H²(z)` below zero once enough negative area has accrued, at z≈16.957
for TJB's own real fitted `(H0_anchor=73.22, β1=1.4335×10¹⁰,
β2=7.8067×10¹⁷)`.

## Verdict

**TASK_INFEASIBLE**, per this project's own Floor-Ceiling discipline
(`falsification-ladder.md` FL Step 4a): "the experiment could not have
been informative" is a distinct outcome from "the claim failed," and
must not be recorded as evidence against the claim. Here the
infeasibility is discovered even *before* the floor/ceiling
construction — the fiducial reference point itself is undefined at the
requested z, so no augmented χ² can be built at all. This is **not**
evidence against `P190`'s or `P191`'s own findings, and does not
falsify the pearl's own prediction (which was never tested, because the
test could not be constructed) — it identifies a **prior, more basic
constraint** the pearl's own z-choice needed to respect and didn't: any
future Fisher-forecast attempt past `P191`'s z≈3 peak must first check
this same boundary before picking synthetic z-values.

## Pearl 1 — the H²(z)<0 boundary itself (flagged by the skeptic review,
not initially planned as a separate pearl)

The skeptic review noted correctly: `H²(z)<0` at TJB's own real fitted
parameters is a fact about the reconstructed model's own viability past
the observed data range — broader in scope than this file's narrow
z∈{20,30,50} question, and worth its own registry entry, not buried
inside a "task infeasible" note. Logged separately below.

## What this does NOT establish

1. Does **not** mean v82's own theory is wrong (`NO_AUTHOR_ERROR`) — a
   reconstructed model's fitted parameters producing an unphysical
   extrapolation far outside the calibration range (z=0.02-2.33) is a
   property of extrapolation, not necessarily of the underlying theory;
   TJB's own construction was never claimed to be valid at z=17-50.
2. Does **not** mean bottleneck 3 is closed or that `P191`'s own
   findings are wrong — `P191`'s z∈{3,5,7,10} sit comfortably before
   this boundary (z<10.5) and are unaffected.
3. Does **not** exhaustively rule out a Fisher-forecast "past the
   peak" — z∈(10, 17) remains a well-defined, not-yet-tested region,
   between `P191`'s own z≤10 and this file's found boundary at z≈17.
4. Does **not** identify whether the H²<0 boundary itself moves under
   different fitted `(β1,β2)` (e.g. other Table II rows) — only checked
   at the spotlighted row, same convention `P176`/`P190`/`P191` use.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
