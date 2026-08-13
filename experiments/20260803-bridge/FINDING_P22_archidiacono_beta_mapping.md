# P22 — Archidiacono's β verified against the primary source; maps onto A·g², but a real target-population gap surfaces

**Date:** 2026-08-13
**Origin:** P21 derived `A·g²=4π·ΔG` (`A` the missing normalization constant,
`g` the monopole coupling, `ΔG` the small fifth-force contribution to
Newton's `G`) and named Archidiacono et al.'s external `β` bound on a
scalar fifth force as the natural second equation — but explicitly did
**not** attempt to verify Archidiacono's own definition of `β` against the
actual paper, flagging that as the concrete next step. This finding does
that verification.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P22_archidiacono_beta_mapping.py`

## 1. Source verification

Fetched directly (WebFetch, this session, cross-checked across three
independent fetches of `arxiv.org/abs/2204.08484` and
`arxiv.org/html/2204.08484`): Archidiacono, Castorina, Redigolo, Salvioni,
*"Unveiling dark fifth forces with linear cosmology,"* published JCAP 10
(2022) 074 (arXiv v4, Nov 2025) — confirmed as the same paper P13a cited.

Verified quotes (not paraphrased):

- **Eq 2.10:** `β ≡ G_s/(4π·G_N)`.
- **Eq 2.17:** `G_s = g_D²/m_χ²` (their specific fermionic-mediator UV
  completion).
- **Eqs 2.15–2.16:** coupling terms `−g_D·φ·χ̄χ` (fermionic DM) and
  `−g_D·m_χ·φ·χ²` (scalar DM) — `φ` couples **only** to the dark-matter
  field `χ`.
- **Confirmed twice, independently:** *"baryons are completely unaffected by
  the scalar fifth force"* — zero baryon coupling in this model, not merely
  a small one.
- **Abstract headline bound:** *"less than a percent of gravity"* →
  `β≲0.01`, from Planck + BAO (no DESI in this version — v4 predates DESI
  DR2), for `m_φ≲H₀` — the same long-range regime this project's own
  `μ~H₀/c` mechanism (P11) lives in.
- **Not independently confirmed at higher precision:** the tighter
  `β<0.0054` figure P13a originally cited. Section 5's precise tables were
  not accessible this session (PDF mirror returned HTTP 403; the HTML
  excerpt tool could not surface table values). Flagged as an open
  precision gap — the `0.01` figure used below is the number this session
  actually verified from primary text, not the more precise one.

## 2. The mapping (sympy-verified)

`Archidiacono: β = G_s/(4π·G_N)  ⟹  G_s = 4π·β·G_N`

`This project's own P21-corrected force law: F_MULT(r) = A·c_G·g²·m₁m₂/r²
= (A·g²/4π)·m₁m₂/r², defining ΔG via F_MULT(r) ≡ ΔG·m₁m₂/r²:  ΔG = A·g²/4π`

Identifying `ΔG ≡ G_s` (both defined the same way — the coefficient of an
inverse-square force, same convention as Newton's `G`) gives, verified
symbolically (not by hand):

```
A·g² = 16π²·β·G_N
```

Using the independently-verified `β≲0.01` and `G_N=6.6743×10⁻¹¹` (SI, same
constant already used in `P17_kappa_bounds_consistency_check.py`):

```
A·g² ≲ 1.05×10⁻¹⁰  (SI units, m³kg⁻¹s⁻²)
```

## 3. The identification `ΔG≡G_s` is an assumption, not a free equivalence

Both quantities are *defined* the same way, but they are not the same
*measurement*. This is the central caveat of this finding, sharper than
anything P13a established:

- **Archidiacono's `φ` couples only to dark matter — zero baryon coupling,
  stated explicitly, twice confirmed.** MULTING's `g·mᵢ·φ` term (P1's own
  action) couples to a body's mass `mᵢ` generically, with no restriction to
  a dark-matter-only component anywhere in the cited files.
- Using `β≲0.01` as a stand-in for MULTING's `g` therefore requires an
  **additional, unverified assumption**: that a hypothetically *universal*
  fifth force (coupling to baryons too, as MULTING's `g` appears to) would
  be constrained *at least as tightly* as Archidiacono's DM-only coupling.
  This is often true in practice (universal fifth forces face additional,
  typically *stronger* equivalence-principle and laboratory bounds that a
  DM-only coupling entirely evades) but is **not the same bound**, and this
  finding does not verify it either way.
- This is a genuinely new, independently-sourced sharpening of P13a's own
  §2, which named the mismatch as "independent coupling constants" but did
  not have direct textual confirmation that the target *populations* of
  matter differ this starkly (zero vs. generic coupling, not just
  independent coefficients on the same population).

## 4. What this does NOT establish

1. **A numeric value for `A` or `g` individually.** Only their *product*
   `A·g²` is conditionally bounded — `Ω_φ` (P14, built from `κ`, not `g`)
   is **not** thereby fixed; extracting `A` alone requires an independent
   estimate of `g`.
2. **That Archidiacono's `β` bound legitimately applies to MULTING's `g`.**
   §3's identification is stated as an assumption, not verified — if
   MULTING's `g` is meant to be a genuinely universal (baryon+DM) coupling,
   this bound is a plausible but unconfirmed proxy, not a direct
   measurement of the same quantity.
3. **The precise `β<0.0054` figure.** Only the independently-verified
   `β≲0.01` order-of-magnitude figure is used; if the tighter number is
   later confirmed, the bound above tightens by roughly a factor of ~2, not
   an order of magnitude — doesn't change the qualitative picture.
4. **Anything about the dipole sector's own remaining open questions**
   (P18, P19, P20) — this is entirely a monopole/gravity-sector question.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   and about what an external, independently-published paper's own text
   says, not a claim about any error in TJB's own theory.

## Reproduction

```bash
python experiments/20260803-bridge/P22_archidiacono_beta_mapping.py
```

Source verification is WebFetch-based (not locally reproducible from the
repo alone) — see §1 for exact URLs and quotes; a future session could
re-fetch `arxiv.org/abs/2204.08484` to re-confirm.

## Skeptic verdict (context-blind, Step 8a)

*Pending — to be run with only this file + `P22_archidiacono_beta_mapping.py`
+ `FINDING_P21_shared_phi_normalization_constraint.md` (corrected version)
+ `FINDING_P13a_archidiacono_bound_scope.md`, no session history.*
