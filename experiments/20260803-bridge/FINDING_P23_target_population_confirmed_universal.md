# P23 — MULTING's own model spec confirms `g` couples to total cluster mass, not a dark-matter-only population

**Date:** 2026-08-13
**Origin:** P22 flagged, as an *unverified assumption*, that using
Archidiacono et al.'s dark-matter-only `β` bound as a numeric proxy for
MULTING's monopole coupling `g` requires `g`'s target population to be at
least comparable to a DM-only coupling — and noted only that MULTING's
`g·mᵢ·φ` term "appears to couple to mass generically," without checking
further. This finding checks that directly against the project's own
authoritative model-spec registry, rather than leaving it as a hedge.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** internal citation check only — no external fetch, no new
computation (same precedent as P13a).

## 1. The check

`MODEL_SPEC_AUDIT.md` (this project's own adversarially-reviewed symbol
registry, §1, "Force-law primitives — given by MULTING, not touched by this
track") states, verbatim:

```
| Symbol      | Meaning                | Given as | Independent input          | Status |
| m_A, m_P    | monopole (mass) charge | postulate | cluster M500 (MCXC-I/PSZ2) | HOLDS  |
```

`mᵢ` — the coefficient P1's own action couples `g` to (`g·mᵢ·φ`, per
`two_field_action_closure.py`) — is identified with **cluster `M500`**,
sourced from real observational catalogs (MCXC-I X-ray, PSZ2
Sunyaev-Zel'dovich). `M500` is a standard cluster-cosmology mass estimate:
the total mass enclosed within the radius where mean density is 500× the
critical density — **dark matter (the dominant fraction) plus baryonic gas
and galaxies combined**, not a dark-matter-only quantity. `[MEMORY]`,
domain-standard usage of `M500`/MCXC/PSZ2 in cluster cosmology, not
independently re-verified against the catalog papers this session — this is
well-established terminology, not a specific claim requiring external
fetch verification the way Archidiacono's own equations did.

## 2. Consequence

This **confirms**, using the project's own authoritative source (status
`HOLDS`, not `OPEN` or `postulate, not sharply defined` — contrast with the
`k_A, k_P` row on the same table, flagged `OPEN`), that MULTING's `g`
couples to the *same* total mass that dominates real cluster observables —
**not** restricted to a dark-matter-only component. P22's target-population
caveat is upgraded from *"unverified either way"* to *"confirmed real"*:
Archidiacono's `β<~0.01` genuinely bounds a different physical coupling
(dark matter only, zero baryon term) than the one MULTING's `g` needs to be
evaluated against (universal, coupling to `M500` as a whole).

**This does not make P22's numeric ceiling wrong or unusable** — it sharpens
what kind of number it is. Since a genuinely universal coupling is probed by
*strictly more* experimental channels than a dark-matter-only one (galaxy
cluster CMB/BAO physics *plus* equivalence-principle/laboratory tests, which
a DM-only coupling entirely evades), the true constraint on MULTING's `g` is
very plausibly **tighter** than P22's `A·g²≲1.05×10⁻¹⁰` — meaning that number
is best read as a loose, permissive ceiling, not a state-of-the-art
constraint. This matches, and gives independent grounding to, what P22's own
skeptic review already suspected without a source to confirm it.

## 3. What this does NOT establish

1. **A tighter, quantified bound.** Finding the actual equivalence-principle
   constraint on a universal long-range (`m_φ≲H₀`) scalar coupling — the
   natural next number — requires reading a dedicated source (e.g. a
   MICROSCOPE-mission constraints paper, or Archidiacono's own Section 6)
   and has not been attempted here.
2. **Anything about `κ` or `Ω_φ`.** `κ` (the dipole coupling) is coupled to
   `kᵢ`, a *separate* row in `MODEL_SPEC_AUDIT.md` explicitly flagged
   `OPEN` — "postulate, not sharply defined" — a different, already-known
   open problem, untouched by this finding.
3. **That `M500` itself is free of any modeling assumptions.** `M500`
   estimates (X-ray hydrostatic mass, SZ mass-observable scaling relations)
   carry their own systematic uncertainties in the cluster-cosmology
   literature; this finding only established *what* MULTING's `mᵢ` is
   identified with, not the precision of that identification.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   and its own prior model-spec registry, not a claim about any error in
   TJB's own theory.

## Reproduction

No new computation — a citation check against
`experiments/20260803-bridge/MODEL_SPEC_AUDIT.md` §1 (row `m_A, m_P`) and
`two_field_action_closure.py` line 113 (the `g·m_i·φ` coupling term), both
already in the repository.

## Skeptic verdict (context-blind, Step 8a)

*Pending — to be run with only this file + `MODEL_SPEC_AUDIT.md` +
`two_field_action_closure.py` + `FINDING_P22_archidiacono_beta_mapping.md`
(corrected version), no session history.*
