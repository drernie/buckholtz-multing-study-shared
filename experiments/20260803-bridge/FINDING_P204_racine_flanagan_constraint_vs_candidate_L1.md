# FINDING P204 — applying `P203`'s Racine–Flanagan constraint to
# `CANDIDATE-L1`: all four first-draft claims WEAKENED by Step 8a
# skeptic; the surviving result is sharper than the one drafted —
# `docs/131` is internally inconsistent about what its own `ξ_A` is

**Date:** 2026-09-07
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive
**Trigger:** user instruction to check `P203` addendum 3's constraint
against `docs/131`'s `CANDIDATE-L1`, autonomously.
**Post-hoc disclosure:** analysis preceded this file; no pre-registered
`claim.md`. Disclosed, not hidden — same deviation as `E20`.
**Step 8a skeptic (context-blind, primary quotes + full argument
pasted): all four claims WEAKENED.** Every skeptic point below was
independently re-verified against the primary text before being
accepted — not taken on the skeptic's word (`audit-verification-gate`).

## Positive control

`scripts/l1_weakfield_matching.py` runs and reproduces `docs/131`'s
verdict verbatim (branch H FAIL on `1/r⁴`; branch S structure matches,
attractive). The artifact under discussion is the one described.

## Correction 1 — the constraint's mechanism was wrong (Claim 1)

**Drafted:** Racine & Flanagan is evaded by making the inter-node
region non-empty; Blanchet–Le Tiec take that route.

**Skeptic, verified correct:** R&F contain two logically separate
things, and I conflated them.

| | requires vacuum in the buffer? |
|---|---|
| (A) the surface-integral derivation of the equations of motion | **yes** |
| (B) Eqs. 71/82, the mass-dipole gauge argument | **no** — it is the kinematic identity that the first moment of a mass distribution shifts as `M̄_i = M_i − M z_i` under translation of the origin |

Filling the region breaks (A) but **not** (B). So "non-empty region"
does not by itself restore a dipole degree of freedom.

**The actual reason Blanchet–Le Tiec escape:** their dipole is a
**polarization** — a dipole moment *per unit volume of a continuous
medium*, a field. Eq. 71 does not apply to it because there is **no
worldline to shift**. `[VERIFIED-arXiv 0804.3518]`: *"the dynamics of a
dipolar medium, i.e. one endowed with a dipole moment vector, and
polarizable in a gravitational field."* A polarization field is not a
body's mass dipole.

**Corrected constraint (supersedes both `P203` addendum 3's version and
this file's first draft):** a completion retaining `F^(1)` needs its
dipole to be an object **to which the mass-dipole gauge argument does
not apply** — i.e. a field-level (fluid) polarization with no
associated worldline, not a body-level dipole. Being in a non-empty
region is neither sufficient nor the operative mechanism.

## Correction 2 — the failure mode of `docs/131` is not the one drafted
## (Claim 3), and the real one is worse

**Skeptic's catch, re-verified by direct reading of `docs/131` lines
17-19:** the setup is internally inconsistent about what `ξ_A` is.

> *"A Blanchet–Le Tiec-type polarizable point particle: position `x_A`,
> mass `m_A`, **internal dipole vector `ξ_A` with internal potential
> `W(ξ_A)`**; monopole-dipole interaction **`U_md = −G m_B (p_A·r̂)/r²`,
> `p_A = m_A ξ_A`**."*

- The words *"internal dipole vector with internal potential `W`"*
  assert a **physical internal degree of freedom** with its own
  dynamics — call it reading (ii).
- The formula `U_md = −G m_B (p_A·r̂)/r²` is the standard coupling of a
  **mass dipole** to an external Newtonian potential — reading (i).

These are different objects, and the two halves of one sentence
presuppose different ones.

**Consequence — the failure is real either way, but neither branch is
what the first draft said:**

| reading | what `p_A` is | why it fails |
|---|---|---|
| (i) `ξ_A` = displacement of the worldline from the mass centroid | a genuine mass dipole | pure gauge (Eqs. 71/82); the `F = −2Gm_B P/r³` is a coordinate artifact — *this* is the first draft's claim, and it holds only here |
| (ii) `ξ_A` = physical internal dof, mass dipole about the CM still zero | `≈` reduced-mass × internal length — **not** a mass dipole | then `U_md` **does not follow from standard GR at all**: GR couples matter through `T^μν`, and a monopole–dipole coupling for a non-mass-dipole internal moment is a hidden extension of the theory, not a derivation within it |

`docs/131`'s own language points at (ii); its formula assumes (i).
So the drafted claim ("the structure is gauge") is correct **only** for
reading (i), and mis-scopes the failure for reading (ii).

## Correction 3 — the reduction itself was the error (skeptic's own
## sharper formulation, adopted)

> **Blanchet–Le Tiec escape R&F because they work with a polarization
> field — a fluid-level object with no worldline. `docs/131` compresses
> that fluid-level construction into a point-particle limit, and in
> doing so destroys precisely the property (having no worldline) that
> did the escaping.**

The skeptic's supporting point, which I had not seen: *"«polarizable
point particle» is structurally an oxymoron"* — a polarization is
coarse-grained collective displacement inside a medium; contracting it
to a point discards the collective structure. `docs/131`'s object is
therefore **not a limit of Blanchet–Le Tiec — it is a different model.**

This formulation is better than the first draft's because `docs/131`'s
failure follows from it directly, with no separate EP argument needed.

## Correction 4 — "same obstruction" overstated (Claim 4)

Drafted: `docs/131`'s EP argument and R&F's `M_i ≡ 0` are one
obstruction seen twice. **Corrected:** they are *partially independent,
converging on a common root premise* — universal metric coupling. They
share that root (so they must **not** be counted as independent
evidence), but they can come apart: `[HYPOTHESIS, skeptic's, not
verified here]` a scalar–tensor theory with universal coupling keeps EP
while changing the vacuum equations; a non-minimal coupling can violate
EP while leaving the vacuum equations GR-like.

## What survives, and what it establishes

**Survives, verified independently:** R&F do forbid a Newtonian `1/r³`
force between bodies whose buffer regions are vacuum. Monopole–monopole
gives `1/r²`; monopole–quadrupole `1/r⁴`; current multipoles are
PN-suppressed. The only Newtonian source of `1/r³` is
mass-dipole × monopole, and that moment is identically zero. `docs/131`'s
FAIL verdict is **not overturned** — it is re-scoped, and its stated
reason (the sign) turns out to sit downstream of a prior problem about
what its own `ξ_A` is.

**Does NOT establish:**
1. That `CANDIDATE-L1`'s parent theory fails. It does not — it escapes
   R&F legitimately, via the polarization/no-worldline route.
2. That the medium-mediated route works. Nothing here computes it, and
   `docs/131`'s separate objection stands untouched: the medium's
   contribution is *"the internal potential `W`'s energy density acting
   as a Λ-like term... not a repulsive pairwise force."*
3. Anything about v82. `NO_AUTHOR_ERROR`: `CANDIDATE-L1` is this
   project's own reconstruction (`docs/130`: *"identifying MULTING with
   a polarizable vector medium is OUR hypothesis"*), and v82 specifies
   no vacuum sector at all (`P203` addendum 3).
4. Which reading `docs/131` intended. The inconsistency is verified;
   the intent is not recoverable from the text.

## Pearl Registry / next step

Two, both cheap and now well-posed:

1. **Add the missing row to `FINDING_P171`'s assumption ledger.** Its 8
   rows do not include *"the node's dipole is a body-level moment with
   a worldline, not a fluid-level polarization"* — verified absent
   (`grep -i "inter-node|between the nodes|vacuum|empty"` returns one
   hit, in an unrelated Ostrogradski context). That is the assumption
   this whole exercise turned out to hinge on.
2. **If `CANDIDATE-L1` is ever revisited, do it at fluid level** — a
   polarization field between the nodes, never a "polarizable point
   particle." The point-particle version is not a limit of the parent
   theory and cannot inherit its escape.
