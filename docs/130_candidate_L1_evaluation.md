# docs/130 — CANDIDATE-L1 (covariant reconstruction): evaluation + step-1 kill-test

**Date:** 2026-07-22
**Status:** proposal evaluated; step-1 symbolic test done (sympy) + skeptic-reviewed +
three user corrections applied (all three verified). No-go WEAKENED, not falsified.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Continues:** docs/129 (Q006). Artifacts: `scripts/l1_twobody_limit.py`,
`scripts/{factorization_gate,q006_lagrangian_check}.py` (dipole coefficient corrected,
see below).
**L0:** descriptive/mathematical.

---

## The proposal (user, 2026-07-22)

Build a covariant candidate `CANDIDATE-L1` for MULTING from the Blanchet–Le Tiec
dipolar-medium action `S = S_EH + S_ordinary + S_dip` (dynamical dipole vector `ξ^μ`,
`u_μ ξ^μ=0`, internal potential `W(Π_⊥)`) plus a matching sector
`ΔS_multipole = ∫√-g λ_q Π^μ Π^ν E_μν` (dipole²×tidal curvature) to generate the
quadrupole and keep `β_d, β_q` independent. Coefficients fixed by WEAK-FIELD MATCHING,
never by H(z). Mapping `m_A ξ_A ↔ k_A r_A/c²`.

## Three user corrections — ALL VERIFIED, applied

1. **No factor-of-2 error — MINE was the error.** I earlier flagged the user's dipole
   potential `V_d = G(d_A m_B + d_B m_A)/(2r²)` as a factor of 2 short. **Wrong.**
   Re-reading the clean OCR (preprint Eqs. 14-16, line 784): `Fd = (G kA c⁻² mP |rdA|
   + G kP c⁻² mA |rdP|)/r³` — the "c⁻²" is `1/c²` (the PN factor), which I had misread
   in docs/125 as a coefficient `−2` (while correctly reading `c⁻⁴` in the quadrupole
   — an inconsistent misread). The correct dipole force coefficient is `Gβ_d/c²` (no
   2); the user's `V_d` with the `½` reproduces it exactly. **Fixed** in
   `scripts/{factorization_gate,q006_lagrangian_check}.py` and docs/125/129 (residual
   still 0). **Cosmologically immaterial** — every P2/C1/P3/Q006 conclusion depends on
   r-powers and bilinear structure, not this coefficient — but corrected for the
   matching program. `EXACT NR LAGRANGIAN — DERIVED, ½ RETAINED (correct).`
2. **Central-vs-angular is a DIAGNOSTIC, not a 3-way theorem.** My "3 branches" was not
   exhaustive; radiality can also arise from minimizing internal-orientation d.o.f.,
   statistical averaging, integrating out an auxiliary field, scalar-tensor coupling,
   worldline-EFT for extended objects, or a nonlocal/multifield completion. The skeptic
   independently produced a concrete counterexample (unparticle, below). So radiality
   is a STRONG diagnostic constraint, **not** proof of a specific mechanism. Also:
   the preprint ties the dipole/quad to internal kinetic energies + Lorentz-invariance
   and DEFERS the field equations/Lagrangian to future work — so identifying MULTING
   with a polarizable vector medium is OUR hypothesis (NOT_VALIDATION).
3. **Induced polarization does NOT guarantee a linear fσ8 signature.** My "if induced
   ⇒ η≠0 ⇒ distinguishable linear fσ8" was an overreach. Verified from the primary
   source (arXiv:0804.3518 abstract, WebFetch): Blanchet–Le Tiec's dipolar fluid is
   *"undistinguishable from standard dark energy (Λ) plus standard dark matter"* at
   FIRST-order cosmological perturbations; differences are 2nd-order / nonlinear. So
   `induced ⇏ distinguishable linear fσ8` — one must DERIVE `μ(k,a)` from the candidate
   action; it may be 1, ≠1, scale-dependent, or Ωm/σ8-degenerate. (This is the same
   marginalization point the P3 skeptic raised, docs/128.)

## Step-1 result (symbolic, `scripts/l1_twobody_limit.py`)

MULTING's dipole needs the CONJUNCTION: fixed magnitude `∝ k_A` (property of A alone),
always RADIAL, `1/r³` force, repulsive-capable. Standard permanent dipole → 1/r³ but
ANGULAR (`⟨cos θ⟩=0`); induced dipole → radial but 1/r⁵ and magnitude `∝ m_B/r²`. No
STANDARD mechanism supplies the conjunction. Sign (repulsion) is not the obstruction.

## No-go verdict — skeptic-reviewed (WEAKENED, not falsified)

My sharpened no-go ("a scalar A-charge can't give a central 1/r³ force because coupling
to `∂_i g_j` is tensorial → angular") is **too strong**: it ignored anomalous-dimension
mediators. The skeptic exhibited a concrete counterexample and then killed it on MULTING-
specific grounds:

- **Unparticle (Georgi, `d_U=3/2`)** — a scale-invariant hidden-CFT sector gives a
  `1/r²` static Green's function (flat spectral density), hence a STATIC, CENTRAL,
  `1/r³` force from a SCALAR charge. So the *structure* is reproducible by a
  (nonstandard-but-local) theory. BUT it fails MULTING on:
  - **Sign:** scalar–scalar exchange between real charges is ATTRACTIVE (`Γ(1/2)>0`);
    MULTING's dipole is REPULSIVE. Repulsion requires vector mediation → vector charge
    → angular. This is a clean, mechanism-independent obstruction.
  - **Coefficient isolation:** a single mediator with mixed coupling `(αk+βm)` produces
    `k_Ak_B`, `(k_Am_B+k_Bm_A)`, AND `m_Am_B` all at the SAME order. MULTING instead
    puts each bilinear at a DIFFERENT r-power (mm→1/r, km→1/r², kk→1/r³, its "multi-
    tier" structure). No single local mediator does that; it needs one mediator PER
    tier (fine-tuned).
- All other candidates die harder: tidal-tensor `E_ij` invariants scale as `1/r⁶⁺`
  and `∝m_B^{n≥2}`; bi-derivative couplings give `∝m_B²`; Yukawa/massive-spin-2 have no
  `1/r²` regime; gravitomagnetism (the preprint's `r_dA∝S_A` hint) is VELOCITY-dependent
  → zero in the static limit.

**Weakened no-go (survives):** *no local, isotropic, ghost-free field theory with a
scalar A-charge reproduces a **REPULSIVE** static central `1/r³` force whose coefficient
is **exclusively** `k_A m_B` (no companion `k_Ak_B`, `m_Am_B` at the same order).
Obstruction: (a) stable scalar–scalar exchange is attractive → repulsion needs a vector
→ angular; (b) isolating the `km` tier from `kk`/`mm` needs a mediator-per-tier
conspiracy.* Escape hatches (all non-minimal): two-mediator cancellation; a
constraint-derived radial alignment (`ξ∥∇Φ` derived, not assumed); non-uniform
extended-object averaging with a preferred internal mode.

## Sharpest cheapest test (skeptic + user, aligned) — supersedes the abstract debate

Do NOT argue scalar-vs-vector in the abstract. Two concrete checks:

**(A) Corpus companion-term test (minutes).** Any local scalar mediator generates all
three bilinears at one order. MULTING is written as if the dipole tier has ONLY `km`
and the quad tier ONLY `kk`. Does the corpus have companion `m_Am_B/r³` (a G-
renormalization) and `k_Ak_B/r³` (a dipole-order `kk`) terms? Their **absence** is a
hard falsifier of the single-mediator interpretation — it forces the multi-tier /
mediator-per-tier reading. [Cheap; corpus-only.]

**(B) User's exact weak-field matching of CANDIDATE-L1 (the real next step).** Solve the
`ξ^μ` equation of motion, substitute back, read off the effective two-body potential,
and check WITHOUT hand-tuning:

```
V_target(r) = -G m_A m_B/r + G(d_A m_B + d_B m_A)/(2r²) - G q_A q_B/(3r³)
              d_A = β_d k_A r_A/c²,  q_A = β_q k_A r_A/c²
```

| verdict | criterion |
|---|---|
| PASS  | r⁻¹, r⁻², r⁻³ all reproduced; correct signs; A↔B symmetry; β_d, β_q independent — with NO hand-imposed orientation |
| FAIL  | irreducible angular dependence; correct sign needs negative KE / ghost; radiality imposed by hand; coefficient depends on a third body; β_d, β_q not independently matchable; match works for only one chosen pair |
| BLOCKED | centrality achieved by ASSUMING `ξ^μ ∥ ∇^μΦ` when that alignment does NOT follow from the EoM → `ASSUMED ALIGNMENT`, not matching |

Only after PASS does deriving `μ(k,a)` and returning to fσ8 make sense.

## Updated status

| element | status |
|---|---|
| NR potential | `DERIVED`; the ½ is correct (my earlier ×2 flag was wrong, fixed) |
| CANDIDATE-L1 | `CONSTRUCTIBLE` |
| central-vs-angular | `PRIMARY DIAGNOSTIC` — not an exhaustive classification |
| repulsive sign | `SHARP MATCHING TEST` (scalar-scalar is attractive → repulsion needs vector) |
| induced polarization | does NOT guarantee a linear fσ8 difference (must derive μ(k,a)) |
| weak-field matching | `OPEN` — the real next step |
| ghost/stability audit | `NOT TESTED` |
| author attribution | `ABSENT` (our reconstruction, labeled) |

**Net:** the program is sound and correctly disciplined. My contributions were two
sharp negative sub-results (repulsive-sign obstruction; multi-tier coefficient-isolation
obstruction) that make the weak-field matching test more pointed, plus three corrected
overreaches. The right next action is the user's exact-matching computation (B), gated
by the cheap corpus companion-term check (A).
