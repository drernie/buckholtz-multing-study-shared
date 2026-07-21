# docs/126 — Non-Uniqueness of Cosmological Closure for F_oP (scoped lemma)

**Date:** 2026-07-21
**Status:** LEMMA STATED + PROOF SKETCH + COUNTEREXAMPLE DESIGN. The lemma is NOT yet
proved (the constructive counterexample, P2, is designed here but not executed).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Supersedes framing in:** `docs/125` (three overclaims corrected there in place —
see its "Correction 2026-07-21" note).
**L0:** descriptive/mathematical (non-uniqueness of a functional map), not causal.

---

## Honest status labels (adopted verbatim from user review 2026-07-21)

```
MATRIX FACTORIZATION      — PASS        (docs/125, sympy-exact; reusable)
COSMOLOGICAL CLOSURE FOR q — MISSING     (absent from corpus; NOT proven non-existent)
DIRECT SHTANOV APPLICATION — BLOCKED     (not "closed" — blocked pending q-evolution)
NO-GO THEOREM             — NOT YET PROVED (this lemma targets weaker non-uniqueness)
```

**Verification-independence caveat.** The `docs/125` skeptic verdict ("the
obstruction is physical") came from a **same-model, isolated-context** review —
"Weak-Medium" on `falsification-ladder.md`'s Independent Verification Strength
Ladder, NOT independent physical/formal verification. It is now corroborated by an
independent **human** review (the user, 2026-07-21), which is stronger, but the
claim "closure for q is missing" still rests on *absence of evidence in the corpus*,
not a *proof of non-existence*. The robust confirmation is the constructive
counterexample below (P2), which is designed but not yet computed.

---

## Setup (what is already established)

`docs/125` proved (sympy-exact) that `F_oP = F_m - F_d + F_q` is a 2-species
bilinear form: with per-object charge `Q_i = (m_i, q_i)`, `q_i = k_i r_i`, the pair
potential is `Q_iᵀ K(r) Q_j`, `K` a global symmetric 2×2 kernel matrix. So a global
kernel EXISTS (factorization is not the obstruction). The open question is whether
the corpus determines a unique cosmological `H(a)` from this force.

---

## Lemma (Non-uniqueness of closure)

**Statement.** Under assumptions (A1)–(A6) below, the background expansion history
`H(a)` is **not uniquely determined**: there exist at least two admissible evolution
laws `q_i^{(1)}(a)`, `q_i^{(2)}(a)` for the second charge that share identical initial
data and identical pairwise force `F_oP`, yet yield `H^{(1)}(a) ≠ H^{(2)}(a)` under
the same fixed closure procedure.

**Explicit assumptions (all required; none hidden):**

| # | Assumption | Role |
|---|-----------|------|
| A1 | Background is FLRW: spatially homogeneous and isotropic. | Defines what "H(a)" means; also makes odd-multipole orientation averaging well-posed (see caveat C3). |
| A2 | The only interaction is the pairwise `F_oP` (no extra fields/forces). | Fixes the microscopic input. |
| A3 | Object number conserved per comoving volume; mass density has the standard conserved background `ρ_m ∝ a⁻³`. | Gives the monopole (mass) sector a well-defined background `ϱ` for subtraction. |
| A4 | `H(a)` is produced by a **fixed closure** `C` mapping (microscopic state + interaction) → `H(a)`. Concretely instantiated by the Shtanov–Sahni generalized cosmic energy equation (arXiv:1010.6205, their Eqs. 36 & 48) as the representative closure. | The map whose uniqueness is in question. |
| A5 | Identical initial data at `a = a₀`: positions, peculiar velocities, `{m_i}`, and `{q_i(a₀)}`. | Isolates the evolution law as the ONLY difference. |
| A6 | The corpus specifies **no evolution law** for `q_i = k_i r_i`; `q_i(a)` is a free function on `[a₀, 1]`, constrained only by admissibility: positivity, `C¹` regularity, boundedness. | The crux — the underdetermination lives here. |

**Proof sketch (analytic, WITHIN closure C = Shtanov–Sahni energy equation):**

The generalized cosmic energy equation (their Eq. 36) contains an explicit
`∂φ(a,r)/∂a` term:
```
⟨Ė⟩ = -2H⟨K⟩ + 2πHϱ ∫ ξ(r) [ (∂φ/∂r)·r + (∂φ/∂a)·a ] r² dr
```
and the expansion history is recovered as `H = -⟨Ė⟩ / (2⟨K⟩ + ⟨U⟩)` (their Eq. 48).
For the MULTING matrix kernel, the potential `φ` contains q-dependent pieces (the
`κ_mq` cross term and the `κ_qq` quadrupole term). Hence
```
∂φ/∂a  ∝  ∂q/∂a   (nonzero whenever q evolves).
```
Because A6 leaves `∂q/∂a` free, `⟨Ė⟩` — and therefore `H(a)` via Eq. 48 — is a
**functional of the unspecified `∂q/∂a`**. Two admissible laws with
`q^{(1)}(a₀) = q^{(2)}(a₀)` (A5) but `∂q^{(1)}/∂a ≠ ∂q^{(2)}/∂a` give
`⟨Ė⟩^{(1)} ≠ ⟨Ė⟩^{(2)}` hence `H^{(1)} ≠ H^{(2)}`. ∎ (sketch)

**Why this is only a SKETCH, not a proof:** it assumes (i) closure C is the S–S
energy equation specifically, and (ii) the q-dependent `∂φ/∂a` term does not
cancel against the `∂φ/∂r` term after the `∫ξ(r)…` integration for the two chosen
laws. Both are plausible but unverified. The constructive counterexample removes
both gaps by exhibiting explicit laws and computing the integral.

---

## Constructive counterexample (P2 — designed, NOT executed)

The 4-step minimal test that upgrades the sketch to a proof:

1. **Two admissible evolution laws**, identical `q_i(a₀)`:
   - **Law 1 (frozen charge):** `q_i(a) = q_i(a₀) = const` ⟹ `∂q/∂a = 0`.
   - **Law 2 (virial charge):** by the cosmic virial theorem `k_i(a) ≈ G M_i(a)²/(2 R_i(a))`,
     so `q_i(a) = k_i R_i ∝ G M_i(a)²`, with `M_i(a)`, `R_i(a)` following a standard
     cluster-growth history ⟹ `∂q/∂a ≠ 0`.
   Both satisfy A6's admissibility (positive, `C¹`, bounded on `[a₀,1]`); neither is
   forbidden by the corpus.
2. **Hold fixed:** initial data (A5), the pairwise force `F_oP` (A2), the mass
   background `ρ_m ∝ a⁻³` (A3).
3. **Apply the same coarse-graining** (closure C) to both.
4. **Show `H^{(1)}(a) ≠ H^{(2)}(a)`** — a nonzero `ΔH(a)`, computed, with the
   magnitude reported (not just "different"): if `ΔH/H` is below numerical noise the
   test is inconclusive, not a proof.

**If step 4 gives a resolved `ΔH ≠ 0`:** non-uniqueness is proved constructively —
the published pairwise law plus admissible-but-corpus-unspecified `q(a)` supports
≥2 incompatible cosmologies. This is a self-contained, peer-reviewable mathematical
result and does **not** require proving the impossibility of all bridges.

**If step 4 gives `ΔH ≈ 0` (cancellation):** the lemma is false as stated for these
two laws — the closure is insensitive to `∂q/∂a` after averaging, which would itself
be an informative (and surprising) result pointing back toward a possible unique H.

---

## Scope caveats (explicit — what this lemma does and does NOT claim)

- **C1 — Scoped to closure C.** Proved (once P2 runs) only for the Shtanov–Sahni-class
  energy-equation closure. Non-uniqueness for *arbitrary* local closures is a broader
  conjecture, NOT this lemma. The full "scoped no-go" (old P4) is downstream of this.
- **C2 — Non-uniqueness ≠ impossibility.** This shows the corpus *underdetermines* H,
  not that MULTING is wrong or unclosable. Supplying `q_i(a)` (author, P0) may make it
  well-posed. This is a statement about the *published corpus*, not the theory.
- **C3 — Odd-multipole averaging unaddressed.** The dipole (`κ_mq`) is an odd
  multipole; whether it survives isotropic averaging (A1) is a separate question not
  settled here. The lemma's `∂q/∂a` dependence runs through the quadrupole (`κ_qq`,
  even) as well, so it does not hinge on the dipole surviving — but this should be
  made explicit when P2 is computed (compute the dipole and quadrupole contributions
  to ΔH separately).
- **C4 — Admissibility is doing work.** "Physically admissible `q(a)`" (A6) is stated
  loosely (positivity, `C¹`, bounded). A referee could demand a tighter admissibility
  class; if the class is narrowed enough to force a unique `q(a)`, the lemma weakens.
  The counterexample's two laws are both *uncontroversially* admissible, which is why
  it is robust to reasonable tightenings.

---

## Updated priority ladder (adopted from user 2026-07-21)

```
P0  author answer + fix source corpus                         [blocked on TJB]
P1  theorem of non-uniqueness of closure                      [THIS DOC — sketch only]
P2  constructive counterexample: two admissible q_i(a) → different H(a)   [designed]
P3  kinetic / virial coarse-graining                          [if closure is chosen]
P4  scoped no-go under explicitly listed assumptions          [only AFTER P1+P2]
P5  Candidate G as independent phenomenological benchmark
P6  MCMC / CC / DESI — only after a closure is chosen
```

**Immediate next action if pursued:** execute P2 step 4 — pick the concrete S–S
closure, implement the two `q(a)` laws over a toy cluster population, compute
`ΔH(a)` with its magnitude and a numerical-noise floor. That single computation
either proves the lemma (resolved `ΔH ≠ 0`) or falsifies it (cancellation).
