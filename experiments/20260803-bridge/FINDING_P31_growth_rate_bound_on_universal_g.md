# P31 — a phenomenological soft ceiling under Bean & Tangmatitham's Q-mapping, not yet an established direct bound on MULTING's own worldline-coupling completion

**Date:** 2026-08-13
**Origin:** direct continuation of `FINDING_P30`'s own corrected §3 —
explicitly deferred a literature search for a real growth-of-structure
bound on `ΔG/G_N`, using P30's own derived equation
(`δ_m''+ℋδ_m'=4π·G_eff·ρ_m·a²·δ_m`) as the target functional form. This
finding does that search and mapping.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P31_growth_rate_bound_on_universal_g.py`

**[CORRECTED after skeptic review, same day — the most consequential
catch reverses the finding's headline conclusion, not just its framing.]**
The original version used the wrong edge of Table 1's **asymmetric**
interval `Q∈[0.97,1.01]`. `Q=0.97` corresponds to `ΔG<0` (a *repulsive*
modification); `Q=1.01` corresponds to `ΔG>0` (*attractive*). But
`FINDING_P21`'s own corrected relation `A·g²=4π·ΔG` forces `ΔG≥0` always —
both `A` (established `G`-units, positive) and `g²` (a square) are
structurally non-negative, matching the physical fact that a scalar-
mediated exchange force between like masses is always attractive, exactly
like gravity itself. The physically-relevant one-sided bound is therefore
`Q−1≤0.01` (the upper edge), not `|Q−1|≤0.03` (which used the physically-
excluded lower edge). Independently re-derived before accepting: confirmed
`ΔG≥0` follows directly from the already-established `A·g²=4π·ΔG` relation,
not a new assumption. **This changes the result from `2.52×10⁻¹¹` to
`8.39×10⁻¹²` — essentially identical to `FINDING_P22`'s own corrected
Archidiacono-based ceiling, not 3× looser.** The entire "topological
correctness costs numerical tightness" headline moral is withdrawn. A
second, more minor issue is also fixed: §2's "verified by direct equation
comparison" overstated the licensing of `Q≡G_eff/G_N` — a Poisson equation
and a growth equation are structurally different kinds of equation; the
identification is physically correct but follows from a derivation *chain*
(Poisson-source → Friedmann identity → growth equation), not a direct
comparison. See the Skeptic Verdict section for the full 6-sub-verdict
breakdown.

**[USER-FLAGGED CORRECTION, same day, after the skeptic pass above — a
real, additional gap the skeptic review did not surface.]** A collaborator
identified a further, more fundamental caveat, independently verified
before accepting: Bean & Tangmatitham's `(Q,R)` framework assumes **matter
remains minimally coupled** — the extra physics lives entirely in a
*modified metric Poisson equation*, and matter (and light) moves on
standard geodesics of that modified metric. `two_field_action_closure.py`'s
own action (re-checked directly: `S=∫d⁴x(1/2)(∂φ)² +
Σᵢ∫dτ[g·mᵢ+pᵢ·∇]φ(xᵢ)`, explicitly documented as *"a fifth force, not
gravity"*) contains **no Einstein-Hilbert term at all** — this project's
own reconstruction is a **worldline-coupled** scalar force acting directly
on matter's equation of motion, layered on top of an implicitly-standard
GR metric, not a modification of the metric Poisson equation itself. These
are two structurally different mechanisms that can produce an *identical*
growth equation (both give `G_N→G_eff`) while diverging on other
observables — most importantly, lensing/ISW, which depend on the metric
potentials themselves, not on whatever extra force massive matter alone
feels. Since `g·mᵢ·φ` is proportional to rest mass, a massless photon gets
**zero** direct coupling to `φ` in this construction — a specific,
checkable consequence explored in `FINDING_P32`. Bean & Tangmatitham's own
likelihood combines CMB + growth + **lensing** data to constrain `Q` (with
a stated `Q`–`R` degeneracy) — meaning their reported `Q` bound is
calibrated to a scenario where growth and lensing move *together*. If
MULTING's actual mechanism leaves lensing unmodified while growth is
modified, applying their `Q` bound directly to MULTING's `ΔG` is not yet
licensed — the *bound itself* is real and the *mapping arithmetic* is now
correct (§3), but whether the *right physical quantity* is being bounded
remains open. **Consequence for this finding's status:** downgraded from
"a real, topologically-correct external bound" to a **phenomenological
soft ceiling under the Q-mapping** — plausible, useful as a scale-setting
cross-check, but not yet established as a *direct* bound on MULTING's own
worldline-coupling completion. Two further, smaller corrections applied
per the same review: (a) §3's "one-sided 95% limit" language overstated
what a published *two-sided* interval's upper edge, reused as a
conservative ceiling, actually is — corrected below; (b) the P22/P31
numeric coincidence (§3) is **not** independent convergence of two
measurements of the same observable — both external inputs happen to be
~1%-level bounds, mapped through the *same* `A·g²=4πG_N·ε` formula, so the
near-equal result is closer to a units-and-scale coincidence than
evidence of anything physical.

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

## 2. Method — licensing the identification `Q≡G_eff/G_N`

`FINDING_P30`'s own corrected §2(c) derived a **growth equation** (a
dynamical, second-order-in-time equation for `δ_m`):

```
δ_m'' + ℋδ_m' = 4π·G_eff·ρ_m·a²·δ_m,   G_eff = G_N + ΔG
```

Bean & Tangmatitham's eq. 6 is a **Poisson equation** (an algebraic/elliptic
relation for the potential `φ` at fixed time, sourced by the density
perturbation) — a structurally *different kind* of equation:

```
k²φ = −4π·G_N·Q·a²·Σᵢ ρᵢΔᵢ
```

**[Corrected after skeptic review]** ~~These are the same functional form
— `Q` occupies exactly the position `G_eff/G_N` occupies in P30's own
equation. Identifying `Q≡G_eff/G_N` (verified by direct equation
comparison, not symbol-name similarity)~~ — a Poisson equation and a growth
equation cannot be directly compared as if they were the same object; doing
so was the same "same-looking prefactor ⇒ same physical equation" pattern
this project's own P29/P30 corrections already flagged. **The
identification `Q≡G_eff/G_N` is physically correct**, but is licensed by a
*derivation chain*, not a direct comparison: the Poisson-equation source
`4πG_N·Q·ρ` is exactly what the standard Friedmann identity
`(3/2)Ω_mℋ²=4πG_N·ρ_m·a²` propagates into the growth equation's own source
term (the same chain P30 itself used to derive its own equation from
Archidiacono's quoted baryon equation). Once propagated through that chain,
`Q` genuinely plays the role of `G_eff/G_N` in P30's growth equation — this
is the correct, narrower statement of what licenses the mapping:

```
ΔG/G_N = Q − 1
```

**[Corrected after skeptic review]** ~~|ΔG/G_N| ≲ 0.03 (95% CL)~~ — this
was the wrong reading of Table 1's asymmetric interval; see §3.

## 3. Result (corrected — a conservative soft ceiling from the published interval's upper edge)

Table 1's interval `Q∈[0.97,1.01]` is a published **two-sided** 95%
marginalized interval, and `[VERIFIED — own established relation]`
`FINDING_P21`'s `A·g²=4π·ΔG` forces `ΔG≥0` always (both `A` and `g²`
structurally non-negative). **[Corrected per user-flagged review]** using
`Q≤1.01` as a fresh, independently-derived one-sided 95% limit would
require re-normalizing Bean & Tangmatitham's own posterior under a `Q≥1`
prior — not done, and not attempted here. What *is* legitimate: treating
the *published* upper edge as a **conservative soft ceiling**, since any
`Q` value the data allows up to `1.01` is, by definition, not excluded at
95% — this is weaker than a genuine one-sided limit but adequate for the
scale-setting purpose this finding serves:

```
Q − 1 ≲ 0.01  (conservative soft ceiling — the published upper edge, NOT
               a re-derived one-sided limit; NOT the lower edge Q−1=−0.03,
               which corresponds to a repulsive ΔG<0 that MULTING's own
               g² structure excludes)
```

```
ΔG ≲ 0.01 × G_N = 6.674×10⁻¹³ (SI)
A·g² = 4π·ΔG ≲ 4π × 6.674×10⁻¹³ = 8.387×10⁻¹² (SI, m³kg⁻¹s⁻²)
```

**Compared to `FINDING_P22`'s corrected `A·g²≲8.39×10⁻¹²` (Archidiacono-based):**

```
Ratio (this corrected bound / P22's ceiling) = 0.9997 ≈ 1
```

**Essentially identical — not 3× looser, as the original version of this
finding claimed.** **[Corrected per user-flagged review]** this near-equal
result should **not** be read as independent convergence of two
measurements of the same physical observable. Both external inputs happen
to be `~1%`-level bounds (`β≲0.01` from P22, `Q−1≲0.01` here), mapped
through the *identical* formula `A·g²=4πG_N·ε`. Two ~1%-level inputs run
through the same conversion will always land near the same number — the
coincidence is a fact about the *conversion formula's scale*, not a
physical cross-check between independent mechanisms. What survives from
the original framing, with the mechanism-frame caveat now attached (see
the User-Flagged Correction banner above): `Q`'s own defining Poisson
equation (eq. 6) sums over *all* matter species, making it structurally
closer to a universal coupling than Archidiacono's DM-only `β` — but
whether Bean & Tangmatitham's *likelihood*, calibrated to a metric-MG
scenario, actually constrains the *kind* of force MULTING's worldline
coupling produces remains open (see `FINDING_P32`).

## 4. What this does NOT establish

1. **The tightest available bound.** A 2010-era result; DESI-era or more
   recent growth-rate analyses almost certainly exist and may give a
   *different* number in either direction — not searched for here, an
   explicit open gap (§0). **[Added after skeptic review]** With the
   corrected numbers now essentially matching P22's, the qualitative moral
   this finding can support is weaker than the original claimed: this is
   one data point, not a settled cross-check, and a more recent analysis
   could easily move either number relative to the other.
2. **A re-derivation of `Q`'s own equations from first principles.** Only
   the derivation-chain licensing (§2, corrected) was checked; the
   surrounding machinery (eq. 7, the anisotropic-stress/lensing-slip
   parameter `R`, the full likelihood pipeline) is not independently
   re-derived. **[Added after skeptic review]** Specifically unresolved:
   whether `φ` in eq. 6 is the Newtonian potential (which matter feels
   directly, most relevant to growth) or a different combination (e.g. the
   Weyl potential, more relevant to lensing) — if the latter, the
   growth-relevant effective coupling could involve `Q` combined with `R`,
   not `Q` alone, in a way this finding did not check.
3. **[Corrected after skeptic review] "No topology-mismatch caveat
   needed."** ~~Unlike Archidiacono's β (DM-only)... no topology-mismatch
   caveat is needed here.~~ `Q`'s universality (summing over all species)
   is a **modeling choice** of the (Q,R) parametrization, not a proof that
   any physical mechanism producing this phenomenology is automatically
   universal — real modified-gravity mechanisms (Archidiacono's own being
   one) can and do produce species-dependent couplings that a single-`Q`
   fit would average over, not detect as such. Applying this bound to
   MULTING's `g` still rests on the assumption (P23's reading) that `g`
   itself is genuinely species-uniform — the bound doesn't prove that,
   it's licensed *by* that assumption, same as every other external-bound
   mapping in this sub-arc.
4. **[Added after skeptic review] Sub-horizon regime.** `Q`'s own density
   perturbation `Δᵢ` is a gauge-invariant construction; P30's `δ_m` is the
   sub-horizon Newtonian density contrast. The two coincide only on
   sub-horizon scales — inherited from P30's own §4 regime restrictions
   (sub-Compton, scale-independent `ΔG`), not independently re-verified
   here.
5. **[Added after skeptic review] Full independence of the two bounds.**
   P22's and this finding's bounds are not obviously drawn from disjoint
   data — both rest on cosmological linear perturbation theory and
   CMB-era measurements (Planck-precursor or Planck itself); calling them
   "genuinely different data" (original wording) overstated how
   independent the two checks actually are.
6. **That `A`'s or `g`'s individual value is now known.** Only the
   *product* `A·g²` is bounded, exactly as with P22's Archidiacono route —
   extracting `A` or `g` alone still requires independent input.
7. **A resolution of which bound (P22's or this one) is "the" true
   constraint.** Both are real, externally-sourced ceilings on the same
   product `A·g²`, now numerically coincident (§3) — citing either is
   defensible, but neither should be presented as more authoritative than
   the other without further work.
8. **[Added, user-flagged] That Bean & Tangmatitham's likelihood actually
   constrains MULTING's own worldline-coupling mechanism.** Their `(Q,R)`
   framework assumes matter remains minimally coupled — new physics lives
   in the metric Poisson equation alone, and their joint likelihood (CMB +
   growth + **lensing**, with a stated `Q`–`R` degeneracy) is calibrated to
   a scenario where growth and lensing move *together*. MULTING's own
   reconstructed action has no Einstein-Hilbert term and couples `φ`
   directly to matter's worldline (`g·mᵢ·φ`) — a structurally different
   mechanism that can produce the *same* growth equation while leaving
   lensing/ISW unaffected (see `FINDING_P32`). Whether Bean & Tangmatitham's
   `Q` bound genuinely applies to MULTING's `ΔG`, or only to a
   metric-modification with matching lensing phenomenology, is the open
   question `FINDING_P32` investigates — this finding's status is
   downgraded accordingly to a **phenomenological soft ceiling**, not an
   established direct bound.
9. **Anything about `κ`.** Entirely about `g`, matching every prior finding
   in this sub-arc.
10. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
    and a published external paper's own equations — not a claim about
    TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P31_growth_rate_bound_on_universal_g.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `FINDING_P30_universal_coupling_linear_growth.md`
(corrected, including its own Skeptic Verdict section), and
`FINDING_P22_archidiacono_beta_mapping.md` (corrected) — no session
history. 6 sub-verdicts, per Step 8a (not merged):

- **A** (source-paper physics accurate): **CONFIRMED-REAL** — Bean &
  Tangmatitham 2010 is a real, well-cited paper; the (Q,R) parametrization
  and the quoted equation/table content are consistent with the paper's
  known type; nothing looks fabricated.
- **B** (`Q≡G_eff/G_N` identification and its licensing): **WEAKENED** — the
  identification itself is physically correct, but "verified by direct
  equation comparison" conflated a Poisson equation with a growth equation
  as if they were directly comparable objects — the same
  same-looking-prefactor pattern already flagged in P29/P30's own
  corrections. *Applied: FIXED — §2 rewritten to state the actual licensing
  chain (Poisson-source → Friedmann identity → growth equation).*
- **C** ("genuinely universal, no topology-mismatch caveat needed"):
  **WEAKENED** — `Q`'s universality is a modeling choice of the (Q,R)
  parametrization, not a theorem that any mechanism producing this
  phenomenology is automatically universal; applying it to MULTING's `g`
  still rests on P23's own assumption that `g` is genuinely species-uniform.
  *Applied: FIXED — §4 point 3 added.*
- **D** (numeric mapping and "3× looser than P22" — **the single most
  consequential catch**): **FALSIFIED.** Table 1's `Q∈[0.97,1.01]` is
  asymmetric; the original version used `|Q−1|≲0.03`, including the
  physically-excluded `ΔG<0` (repulsive) edge. `FINDING_P21`'s own
  `A·g²=4π·ΔG` forces `ΔG≥0` (both `A` and `g²` structurally non-negative),
  so the correct one-sided bound is `Q−1≤0.01`. Independently re-derived
  before accepting: confirmed `ΔG≥0` follows directly from the
  already-established relation, not a new assumption. *Applied: FIXED —
  §3 fully rewritten; result changes from `2.52×10⁻¹¹` to `8.39×10⁻¹²`,
  essentially matching P22's ceiling, reversing the finding's headline
  moral entirely.*
- **E** (honesty about the 2010-era vintage): **WEAKENED** — §0/§4's
  disclaimers were present but the original headline ("3× looser," "a
  real, non-obvious result") leaned on a comparison too fragile to support
  that framing once combined with issue D. *Applied: FIXED — §4 point 1
  softened to note the corrected numbers no longer support a strong
  qualitative moral either way.*
- **F** (other: "sympy-verified" language for pure arithmetic; `Δᵢ` vs
  `δ_m` sub-horizon regime; independence of the two bounds): **WEAKENED**
  — same evidence-marker-inflation pattern already corrected in P29/P30's
  own scripts this session. *Applied: FIXED — script relabeled "arithmetic
  checked with sympy"; §4 gains explicit caveats on the sub-horizon regime
  and the two bounds' shared reliance on CMB-era data.*

**Not a core-predicate-false kill of `Q≡G_eff/G_N` itself** — that
identification survives, correctly licensed. **This is the most
consequential correction of the P31/growth-rate sub-thread**: sub-verdict D
reverses the finding's entire headline conclusion, from "topologically
correct but numerically looser" to "essentially the same numeric ceiling as
P22, via a genuinely independent-in-mechanism (if not fully
independent-in-data) route." The skeptic's own one-line summary: *"When
mapped onto A·g² via P21's chain, the physically-relevant one-sided
(ΔG>0) reading gives a ceiling essentially equal to P22's Archidiacono-
derived number, NOT 3× looser — the 'topological correctness costs
numerical tightness' story is not licensed by the data once the sign of
ΔG is fixed by physics."*
