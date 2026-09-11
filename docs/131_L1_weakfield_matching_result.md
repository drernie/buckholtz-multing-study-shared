# docs/131 — CANDIDATE-L1 weak-field matching: result

**Date:** 2026-07-22
**Status:** matching computed (sympy) + skeptic-reviewed + two cheap kill-checks.
**Verdict: CANDIDATE-L1 FAILS weak-field matching on the repulsive dipole SIGN** — the
1/r³ ∝ k_A m_B structure is matchable (sombrero branch, alignment DERIVED not assumed),
but MULTING's *repulsive* sign requires internal kinetic energy `k_A/c²` (positive
mass-energy) to anti-gravitate, contradicting the equivalence principle. Scope precisely
bounded below (skeptic corrected an "ANY medium" overreach). NOT_REFUTATION.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Continues:** docs/130. Artifact: `scripts/l1_weakfield_matching.py`. **L0:** math.

---

## Setup (the real matching, per docs/130 step B)

A Blanchet–Le Tiec-type polarizable point particle: position `x_A`, mass `m_A`,
internal dipole vector `ξ_A` with internal potential `W(ξ_A)`; monopole-dipole
interaction `U_md = −G m_B (p_A·r̂)/r²`, `p_A = m_A ξ_A`. Two natural `W`:

- **(H) harmonic** `W=½κξ²` (min at ξ=0) → dipole INDUCED by the field.
- **(S) sombrero** (min at `|ξ|=ξ₀ ∝ k_A`) → FIXED magnitude, free orientation.

## Branch (H) — induced: FAIL

EoM `κ ξ_A = m_A g_B`, `g_B = G m_B/r²` → `ξ_A = G m_A m_B/(κ r²)` (radial). Substituting:
`U_md = −G² m_A² m_B²/(κ r⁴)` → **1/r⁴ potential, 1/r⁵ force, ∝ m_A² m_B²**. This is the
wrong power AND the wrong mass-scaling versus MULTING's dipole (1/r² potential, ∝ k_A m_B).
**Induced polarization cannot reproduce MULTING's dipole.** (Consistent with the docs/130
step-1 induced result.)

## Branch (S) — sombrero / fixed magnitude: structure matches, alignment DERIVED

Fixed `|p_A| = P ∝ k_A`, orientation `θ` free. `U_md(θ) = −G m_B P cosθ/r²`. Stationary
points: `θ=0` (energy MINIMUM, stable) and `θ=π` (energy MAXIMUM, unstable). At the
stable `θ=0`: `F = −2 G m_B P/r³` — **central, 1/r³ force, ∝ k_A m_B** — MULTING's dipole
STRUCTURE, with the radial alignment **DERIVED by energy minimization, NOT assumed**
(so this is NOT the `ASSUMED ALIGNMENT` = BLOCKED case). But `F < 0` ⇒ **ATTRACTIVE**.

## The sign confrontation

MULTING's dipole is REPULSIVE (`F_oP = F_m − F_d + F_q`, dipole subtracted). Branch (S)'s
stable aligned dipole is ATTRACTIVE. MULTING's repulsion would require `θ=π`
(anti-aligned) = the unstable energy MAXIMUM — a stable dipole cannot sit there.

**Flagged trap (handed to the skeptic):** Blanchet DDM is KNOWN to produce dark-energy-
like (repulsive/accelerating) *cosmological* behavior. Is that a repulsive *pairwise*
force (which would falsify this verdict), or does it come from the internal potential
`W`'s energy density acting as a dark-energy-like term (NOT a repulsive pairwise force)?
MULTING's `−F_d` is an explicit *pairwise* repulsion — which of the two does it match?

## Verdict — skeptic-reviewed (context-asymmetry, 2026-07-22): FAIL on SIGN

**The sign-FAIL SURVIVES for the tested channel (HIGH confidence); the earlier "ANY
stable local polarizable medium" wording OVERREACHED and is corrected.** The skeptic
confirmed objections 1-4 and flagged scope (5); two cheap kill-checks then closed the
main escape branch and tightened the verdict:

- **(1) Blanchet's cosmological repulsion is NOT a counterexample** [CONFIRMED]: it comes
  from the internal potential `W`'s energy density acting as a Λ-like term (an
  equation-of-state effect), and its MOND regime is *enhanced attraction*. Neither is a
  repulsive *pairwise* force. MULTING's `−F_d` is an explicit pairwise repulsion — a
  different channel. The trap is avoided.
- **(2) The monopole-dipole sign is forced** [CONFIRMED] for a mass dipole (multipole
  expansion of `∫ρ_A Φ_B` with `ρ_A≥0`, `m_B>0`); no hidden geometric sign freedom
  (unlike dipole-dipole, monopole-dipole orientation enters only via `p·r̂`).
- **(3) tidal/velocity rescue** [CONFIRMED fails]: `λ_q Π²E` → 1/r⁵⁻⁶; retardation is
  1/c²-suppressed and MULTING's dipole is static. Nothing flips the 1/r³ sign at order.
- **(4) driven anti-aligned state** [CONFIRMED, scope-tag added]: `θ=π` is an unstable
  energy maximum; a driven/parametric anti-aligned state needs an external pump and a
  non-conservative term — a *different theory*, not a static weak-field limit.
- **(5) scope** [WEAKENED → then re-closed by cheap checks]:
  - **k_A as a distinct free-sign charge?** CLOSED by MULTING's OWN definition: `k_A` =
    "internal kinetic ENERGY of object-A." By mass-energy equivalence `k_A/c²` is a
    MASS — and the `1/c²` in `F_d = (G/c²)(k_A r_A m_B + …)/r³` is exactly that
    mass-energy factor. Positive energy gravitates ATTRACTIVELY (equivalence
    principle), so `k_A`'s gravitational coupling sign is NOT free — it is fixed
    attractive. The "distinct-charge sign-freedom" escape does not exist for a `k_A`
    that IS energy.
  - **Vector-mediator channel?** A spin-1 exchange between conserved currents gives a
    `1/r` (or Yukawa) potential, not `1/r³`; a static `1/r³` from a vector needs
    higher-derivative couplings → ghost. Closes on power/ghost.

**Decisive physical statement (the clean bottom line):** MULTING's *repulsive* dipole
requires the internal kinetic energy `k_A/c²` — a POSITIVE mass-energy — to produce a
net REPULSIVE gravitational effect. Positive energy gravitates attractively (equivalence
principle); the energy-minimized mass-dipole is attractive (branch S, `θ=0`), and the
repulsive configuration is the unstable maximum. So MULTING's repulsive dipole is **not**
the static weak-field limit of any equivalence-principle-respecting, positive-energy,
ghost-free local realization in which `k_A` gravitates as the energy it is defined to be.
The 1/r³ ∝ k_A m_B **structure** is reproducible (sombrero branch); the **repulsive
sign** is not, without negative mass, a tachyon (`κ<0`), a ghost, or a driven
non-equilibrium state.

**Residual open branches (honestly not ruled out, but each requires abandoning a
standard assumption):** a `k_A` that is somehow NOT its own mass-energy (contradicting
the preprint's definition); a genuinely exotic ghost-free vector/antisymmetric sector
engineered to give static `1/r³` repulsion (not known to exist); a driven
non-equilibrium theory (not a static force law). None is in the corpus.

## ADDENDUM (2026-09-10) — the conservative (non-driven) branch of "driven
## anti-aligned state" checked explicitly: also FAILS, closing that escape hatch

**Continues:** this file's own "(4) driven anti-aligned state [CONFIRMED
fails]" item above, which dismissed the escape only for a NON-conservative,
externally-pumped mechanism ("needs an external pump and a non-conservative
term"). The CONSERVATIVE variant — give `ξ_A` genuine rotational inertia
(a moment of inertia `I` about axes ⟂ its own symmetry axis) instead of the
purely potential-based, adiabatic/auxiliary treatment `U_S(θ)` above
implicitly uses (no kinetic term for `ξ̇_A` was ever written down in this
file) — was never checked. A conserved azimuthal angular momentum `L`
(Noether charge of `U_S(θ)`'s own axial symmetry) then gives the standard
heavy-symmetric-top ("Lagrange top") reduced effective potential:

```
U_eff(θ; L) = U_S(θ) + L² / (2 I sin²θ)         [docs/131's own U_S, unchanged]
```

**Result** (`scripts/l1_gyroscopic_stabilization_test.py`, symbolic series
near `θ=π/2` + independent numerical minimization + a 100,000-point
brute-force grid scan, all three agreeing to 5-6 significant figures —
`[VERIFIED-BASH]`): the centrifugal barrier (which diverges at BOTH poles
for any `L>0`, excluding `θ=0` and `θ=π` as candidates) drags the stable
equilibrium away from `θ=0` — but only ever **toward** `θ=π/2`
(`cos θ_eq → 0`, i.e. the net radial dipole force weakens toward zero), for
every tested `L` up to `L̂=10⁶`. It never reaches, let alone crosses,
`θ=π/2` into the repulsive half. Closed form matches the numeric result
exactly (`θ_eq ≈ π/2 − A·I/L²` for large `L`, i.e. `cos θ_eq ≈ A·I/L²` —
verified: `L̂=10→cos≈0.01`, `L̂=50→cos≈0.0004`, `L̂=1000→cos≈10⁻⁶`, all
exact matches to the closed form).

**Honest note on the script itself:** `sympy.solve` failed to extract the
symbolic root of the perturbative series automatically (returned `[]`) —
a cosmetic tooling gap, not a substantive one; the printed series
(`A·φ + L²φ²/(2I) + const`) makes the root `φ_min = −AI/L²` readable by
inspection, and the independent numeric optimizer + brute-force grid scan
(no symbolic solving involved) reproduce this exact closed form to high
precision, so the conclusion does not rest on the failed `solve` call.

**Verdict: the conservative/angular-momentum variant of "driven
anti-aligned state" also FAILS — a second, independent confirmation of
this file's own FAIL verdict, not merely the same one restated.** Both the
non-conservative (already dismissed above) and the conservative
(this addendum) routes to a physically-accessible repulsive configuration
are now closed. docs/131's own list of residual open branches is updated:
"driven anti-aligned state" is no longer residual — CLOSED, for both its
sub-cases.

`REGRESSION/TESTS: script runs clean; ruff check scripts/l1_gyroscopic_
stabilization_test.py passes (2 issues found and fixed — ambiguous
variable name I -> I_mom, an f-string without placeholders — result
re-verified unchanged after both fixes).`

## Consequence — the covariant program (CANDIDATE-L1) FAILS matching

CANDIDATE-L1 fails weak-field matching on the repulsive sign, for a precise, physical,
equivalence-principle-level reason. Combined with the arc: background `H(z)` is q-blind
(P2), the dipole washout survives full anisotropy (C1), linear fσ8 is intrinsic-branch
degenerate (P3), the Lagrangian exists but hinges on the unfixed `η` (Q006), and now the
natural covariant completion cannot reproduce the *repulsive* dipole with a stable
positive-energy medium (L1). This is a strong **NOT_REFUTATION** result: it does not say
MULTING is wrong — it says the published *repulsive* dipole, read as internal-kinetic-
energy gravity, resists a stable local covariant realization, so any covariant completion
must abandon a standard assumption (EP for `k_A`, ghost-freeness, or staticity) — a
modeling choice only TJB can make. The cosmological branch is closed at the level a
reconstruction can reach.
