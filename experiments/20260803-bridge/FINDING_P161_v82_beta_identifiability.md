# FINDING P161 — v82's own (β1,β2,H0,anchor) are LOCALLY identifiable at
# leading order, unlike this project's own (A,g,κ) — via a fully-crossed
# 2×2 control grid, an explicit accretion-term check, and a proven (not
# observed) symbolic independence

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math (symbolic derivation, 4-cell control grid)
**Verdict (final, post-skeptic — round 2 correction):**
`LOCALLY-JOINTLY-IDENTIFIABLE-AT-LEADING-ORDER (rank(J)=3,
det(J)=11492·G²k0³r0³/(375·d0⁹m0)≠0, PROVEN symbolically β1/β2-free via
.free_symbols on all 9 Jacobian entries — not inferred from a clean
final formula); ROBUST TO INCLUDING THE SELF-REFERENTIAL ACCRETION TERM
(determinant identical); EITHER radial-power difference OR z-shape
difference ALONE is sufficient for rank 3 (full 2×2 grid run — matched
z-shape+matched power is the ONLY degenerate cell); NEITHER mechanism is
individually necessary or dominant — the original claim that radial
power was "THE distinguishing mechanism" is WITHDRAWN as overstated.
Requires H0,anchor≠0 (always true physically). SCOPE UNCHANGED: LOCAL,
LEADING-ORDER ONLY — not a full 33-point numerical fit, and not
inconsistent with a practical near-degeneracy such a fit might reveal.`
**Correction (2026-08-30, context-asymmetric skeptic-caught, round 2,
four points, all independently re-verified — not accepted on the
skeptic's word alone):** the first draft (a) asserted symbolic
independence from a "clean final formula" rather than proving it; (b)
never stated the `H0,anchor≠0` precondition; (c) framed Eq. 23 as
carrying independent physical content "analogous to" the FLRW
acceleration equation, when it is a pure quotient-rule consequence of
`H≡ṡ/s`'s own definition; (d) tested only one of the two controls needed
to isolate "radial power" from "z-shape" as the identifiability
mechanism, and its own untested complementary case (real z-shape,
matched radial power) also gives rank 3 — meaning the original "radial
power is THE mechanism" claim was wrong, not merely under-supported; (e)
dropped the accretion term on budget-share grounds without checking
whether its self-referential `H(z)`-dependence could affect *rank*
specifically (a different question from magnitude). All four re-checked
computationally below, not just re-worded.

## 1. The question, and why it's the same shape as `FINDING_P133`'s

`FINDING_P133` found this project's own `(A,g,κ)` are **not** jointly
identifiable from the observable combinations available
(`rank(Jacobian)=2<3`, an *exact* algebraic degeneracy: `O2=O1·O3²`).
`docs/150` §6 item 1 asked the natural next question: does v82's own
3-parameter fit (`β1, β2, H0,anchor`, Sec. II.G) suffer an analogous
degeneracy? If it did, the *specific* fitted point v82 reports
(`β1≈1.4×10¹⁰, β2≈7.7×10¹⁷`) would not be uniquely meaningful — a whole
family of `(β1,β2,H0,anchor)` triples could fit the data equally well,
undercutting any comparison against it (including `FINDING_P159`'s own
ratio comparison).

## 2. Method

Solved the coupled `(s(t), z(t), H(t))` system perturbatively in cosmic
time `t`, using v82's own equations directly:

- Eqs. (1)-(4) [`VERIFIED-PDF` p.4-5]: the force law, both nodes treated
  as identical "typical" objects (`m_A=m_P=m_X(z)`, etc.).
- Eqs. (10)-(14) [`VERIFIED-PDF` pp.6-7]: evolution laws, using
  `FINDING_P158`'s own verified exponent chain (`k_X(z)~m_X(z)^2.16`).
- Eq. (7) (`μ_reduced·s̈=F_P`) and the redshift relation `dz/dt=-(1+z)H`.
- Initial conditions `s(0)=d0`, `ṡ(0)=H0,anchor·d0` [`VERIFIED-PDF p.6`].
- **Eq. (23)** (`Ḣ=s̈/s−H²`, `[VERIFIED-PDF p.29]`) is used, but is **not
  independent physical input**: given `H≡ṡ/s` by v82's own definition
  (Eq. 19, "`s` in place of `a`"), this identity is the quotient-rule
  consequence of that definition alone — `Ḣ=d/dt(ṡ/s)=s̈/s−(ṡ/s)²`. All
  physical content is already in the equation of motion and the
  kinematic redshift relation; Eq. 23 contributes no new information and
  is not "analogous to" the FLRW acceleration equation the way a first
  reading might suggest (that equation carries independent field-
  equation content; this one does not).
- **Requires `H0,anchor≠0`** — the `t↔z` reparametrization divides by
  `z1=−H0,anchor` at every order. Always true physically (an expanding
  universe has `H>0`), stated here as an explicit precondition rather
  than left implicit.

From this, extracted `(H(0), dY/dz|_0, d²Y/dz²|_0)` (`Y≡H²`) and built
their `3×3` Jacobian w.r.t. `(H0,anchor, β1, β2)`.

## 3. Verification — a fully-crossed 2×2 control grid, not one control

A single "same z-shape, different radial power → rank 3" control (the
original draft's only test) shows radial-power difference is
**sufficient**. It does not show z-shape difference is **not** also
sufficient, or that radial power is the *dominant/necessary* mechanism.
Both cells of the missing 2×2 grid were run:

| | same radial power | different radial power (v82's own: `1/s³` vs `1/s⁴`) |
|---|---|---|
| **same z-shape** | `rank=2`, `det=0` — **the only degenerate cell** | `rank=3` |
| **different z-shape (v82's own m_X/r_X/k_X exponents)** | `rank=3` — **the missing control** | `rank=3` (**v82's own construction**) |

`[VERIFIED-sympy]`, all four cells, `P161.py`'s own 4 test functions.
**Corrected conclusion**: degeneracy requires **both** z-shape and
radial power to be matched simultaneously; **either difference alone is
independently sufficient** to restore full rank. The original claim that
radial power specifically was "the distinguishing mechanism, not
z-dependence" is **withdrawn** — it was never tested against its own
complementary case, and that case also gives rank 3.

**Symbolic independence, proven not observed** `[VERIFIED-sympy]`:
`test_jacobian_entries_are_symbolically_beta_free` checks `.free_symbols`
on all 9 Jacobian entries directly — `β1`, `β2` are absent from *every*
entry (not merely from the final determinant after simplification),
confirming no fiducial `(β1,β2,H0,anchor)` point was ever substituted
anywhere in the derivation. Only the `H0,anchor`-column entries (rows 2,
3) depend on `H0,anchor`; the `β1`, `β2` columns are pure functions of
the fixed background constants.

**Accretion term, included not dismissed** `[VERIFIED-sympy]`:
`test_accretion_term_does_not_change_rank` re-runs the full calculation
with `F_acc` (Eqs. 15-17, `mdot_X(z)=1.1·H(z)·m_X(z)`, an explicitly
`H(z)`-dependent, self-referential correction) included in the equation
of motion. Result: **`det(J)` is byte-identical** to the no-accretion
case. This is not a coincidence requiring further explanation — `F_acc`
never depends on `β1` or `β2` at all (no dipole/quadrupole-type
dependence in its own definition), so it structurally cannot alter their
Jacobian columns; only the `H0,anchor` column could shift, and the rank
verdict is unaffected regardless.

## 4. Result — v82's own construction

```
det(J) = 11492·G²·k0³·r0³ / (375·d0⁹·m0)
rank(J) = 3
```

Nonzero for **any** positive physical values of `G, k0, r0, d0, m0` — a
symbolic fact, not a numerical coincidence at some special point (proven,
§3). At this leading order, `(H0,anchor, β1, β2)` are **jointly, locally
identifiable** — structurally *unlike* this project's own `(A,g,κ)` case,
where the degeneracy was an *exact* algebraic identity holding for *any*
values of the constants involved. The mechanism is: matching **both**
the z-shape and the radial power of the dipole/quadrupole tiers
simultaneously (an artificial, non-physical construction — §3's negative
control), not either feature alone.

## 5. What this does NOT establish

1. **Not a claim about v82's own theory being wrong** (`NO_AUTHOR_ERROR`)
   — if anything, the opposite of a criticism: v82's own fitted
   parameters are not subject to the *specific kind* of exact structural
   degeneracy this project found in its own reconstruction.
2. **Not a full identifiability analysis.** Checks only 3 leading Taylor
   moments of `H(z)` near `z=0` — not the full information content of
   the actual 33-point fit spanning `z∈[0.07,2.33]`. A full numerical
   Fisher-information/covariance analysis using v82's own actual data
   could still reveal a **near**-degeneracy (formally rank 3, but a very
   small smallest singular value) even though the leading-order
   structural degeneracy checked for here is absent. Not hypothetical:
   an external analysis the user shared this session reported v82's own
   Table II rows show `β1`, `β2` moving in near-lockstep as `H0,anchor`
   is varied — not independently verified against Table II's own raw
   entries here, and not inconsistent with this file's rank-3 result
   (formal identifiability and practically-tight parameter constraints
   are different things).
3. **Assumes both nodes are identical "typical" objects** — if the
   actual fit is sensitive to genuine `A≠P` node pairs in a way this
   simplification misses, the result could differ.
4. Does not connect to `FINDING_P159`'s own ratio finding beyond
   confirming v82's own fitted point is not, at this order, an arbitrary
   member of an exactly-degenerate family — says nothing new about the
   `19.5×` ratio discrepancy itself.
