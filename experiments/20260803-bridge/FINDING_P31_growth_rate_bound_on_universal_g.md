# P31 — a real, topologically-correct growth-of-structure bound on MULTING's universal g, looser than P22's Archidiacono-based ceiling

**Date:** 2026-08-13
**Origin:** direct continuation of `FINDING_P30`'s own corrected §3 —
explicitly deferred a literature search for a real growth-of-structure
bound on `ΔG/G_N`, using P30's own derived equation
(`δ_m''+ℋδ_m'=4π·G_eff·ρ_m·a²·δ_m`) as the target functional form. This
finding does that search and mapping.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P31_growth_rate_bound_on_universal_g.py`

## 0. Honest scope, stated before anything else

This finding uses a **2010-era result** (Bean & Tangmatitham, *"Current
constraints on the cosmic growth history,"* arXiv:1002.4197, Phys. Rev. D
81, 083534). It is a real, well-established, frequently-cited paper — but
not the most recent available. More recent DESI-era growth-rate analyses
almost certainly exist and may give different, plausibly tighter, numbers
— **not chased down here**, explicitly flagged as an open precision gap
rather than assumed closed (matching `FINDING_P22`'s own precedent of
using a verified-but-not-most-precise `β≲0.01` rather than an unverified
tighter figure). This finding also does **not** independently re-derive
`Q`'s own defining equations from first principles (their eq. 6–7) — only
verifies, via direct WebFetch quotation, that the structural form matches
this project's own derived equation closely enough to license the mapping.

## 1. Source verification (two targeted WebFetch queries, `arxiv.org/html/1002.4197`)

**Query 1** confirmed the headline bound and its provenance:

> "The well measured CMB power spectrum on sub-degree scales provides the
> dominant constraint, limiting the effect of time-independent
> modifications to Newton's constant, `Q-1≲3%` those from standard gravity
> at the 95% confidence level."

Table 1 (time- and scale-independent case, CMB+growth-rate+lensing
combined): `Q∈[0.97,1.01]` at 95% CL.

**Query 2** confirmed `Q`'s exact defining equation (their eq. 6):

> `k²φ = −4πGQa²ΣᵢρᵢΔᵢ`

— a modified Poisson equation, `Q` multiplying `G` exactly where a
`G_eff/G_N` ratio would. **Critically, the source term sums over *all*
matter species** (`ΣᵢρᵢΔᵢ`), not a dark-matter-only subset — a structural,
verified fact, not an assumption from the symbol's name.

## 2. Method — structural match to P30's own derived equation

`FINDING_P30`'s own corrected §2(c) derived:

```
δ_m'' + ℋδ_m' = 4π·G_eff·ρ_m·a²·δ_m,   G_eff = G_N + ΔG
```

Bean & Tangmatitham's eq. 6, rewritten in the same source-term form:

```
S_m = 4π·G_N·Q·ρ_m·a²·δ_m   (schematically, matching φ's Poisson source to δ_m)
```

These are the **same functional form** — `Q` occupies exactly the position
`G_eff/G_N` occupies in P30's own equation. Identifying `Q≡G_eff/G_N`
(verified by direct equation comparison, not symbol-name similarity):

```
ΔG/G_N = Q − 1,   |ΔG/G_N| ≲ 0.03 (95% CL)
```

## 3. Result (sympy-verified)

```
ΔG ≲ 0.03 × G_N = 2.00×10⁻¹² (SI)
A·g² = 4π·ΔG ≲ 4π × 2.00×10⁻¹² = 2.52×10⁻¹¹ (SI, m³kg⁻¹s⁻²)
```

**Compared to `FINDING_P22`'s corrected `A·g²≲8.39×10⁻¹²` (Archidiacono-based):**

```
Ratio (this bound / P22's ceiling) = 2.999 ≈ 3×
```

**This growth-of-structure bound is *looser* (weaker) than P22's** —
despite being, for the first time in this project's P21–P30 arc, a bound
whose **target population and coupling topology genuinely match** MULTING's
own universal `g` (P23). Unlike Archidiacono's `β` (DM-only, per P22/P28/P29's
now-repeated caveat), `Q` is source-democratic across all matter species by
construction, verified directly from its own defining equation — no
topology-mismatch caveat is needed here. **Topological correctness and
numeric tightness are independent axes**: the "correct" bound for MULTING's
actual coupling structure happens to be the looser one, a real, non-obvious
result this finding surfaces rather than assumes either way.

## 4. What this does NOT establish

1. **The tightest available bound.** A 2010-era result; DESI-era or more
   recent growth-rate analyses almost certainly exist and may tighten this
   number — not searched for here, an explicit open gap (§0).
2. **A re-derivation of `Q`'s own equations from first principles.** Only
   the structural match between eq. 6 and P30's own derived equation was
   checked (both are `4π·[G-type coupling]·a²·ρ·δ`); the surrounding
   machinery (eq. 7, the anisotropic-stress/lensing-slip parameter, the
   full likelihood pipeline) is not independently re-derived.
3. **That `A`'s or `g`'s individual value is now known.** Only the
   *product* `A·g²` is bounded, exactly as with P22's Archidiacono route —
   extracting `A` or `g` alone still requires independent input.
4. **A resolution of which bound (P22's or this one) is "the" true
   constraint.** Both are real, externally-sourced ceilings on the same
   product `A·g²`, derived from genuinely different data and mechanisms;
   the *tighter* number (P22's `8.39×10⁻¹²`) is the more conservative
   ceiling to cite if a single number is needed, but this finding's own
   number (`2.52×10⁻¹¹`) is the more *topologically defensible* one for
   MULTING's actual universal coupling — both facts stated together, not
   collapsed into one "the bound is X" claim.
5. **Anything about `κ`.** Entirely about `g`, matching every prior finding
   in this sub-arc.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   and a published external paper's own equations — not a claim about
   TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P31_growth_rate_bound_on_universal_g.py
```
