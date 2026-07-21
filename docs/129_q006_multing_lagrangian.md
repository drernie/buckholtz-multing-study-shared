# docs/129 — Q006: Constructing the MULTING Lagrangian

**Date:** 2026-07-22
**Status:** DERIVATION VERIFIED (non-relativistic many-body Lagrangian, sympy
residual=0). The broad closure claim ("ξ=0 ⇒ cosmologically ΛCDM-degenerate ⇒ Q006
closed") was **FALSIFIED** by a context-asymmetry skeptic; a narrow claim survives.
**Q006 is NOT closed** — it is sharpened into a named missing parameter (η, the scalar
tidal response of k). See the verdict below.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**L0:** descriptive/mathematical (construction + source-text interpretation).

---

## Corpus finding (before any construction)

Grep of the full preprint for `lagrangian | action | variational | euler-lagrange |
field equation | hamiltonian`: **no hits** for an action principle. The MULTING model
is specified ENTIRELY at the level of two-body FORCES (Newton/Coulomb analogy, Eqs.
14-17). There is no action to extract; a Lagrangian must be CONSTRUCTED (reverse-
engineered) from the forces. This confirms Q006 was genuinely open.

Two further verbatim source facts that decide the cosmologically-relevant question:
- **(p.11)** "Modeling does not need to consider potential energies that, within
  objects, bind sub-objects into objects or that affect the motions of sub-objects."
- **(Eqs. 14-16 + p.11)** the dipole is parametrized by the SCALAR internal kinetic
  energy `k_i` (and scalar radius `r_i`), NOT by an orientation vector. Its two terms
  couple `k_A·m_P` and `k_P·m_A` — the cross structure `(m_i q_j + m_j q_i)`,
  `q_i = k_i r_i`.
- (prose only, not in the equations) the preprint separately describes a *spatial*
  two-sub-mass dipole whose effect is orientation-dependent — but this orientation
  dependence does NOT enter Eqs. 14-16.

## Derived Lagrangian (VERIFIED, sympy residual = 0)

The pair force `F_oP = F_m - F_d + F_q` (radial `F_r = -A/r² + B/r³ - C/r⁴`, with
`A=G m_i m_j`, `B=(Gβ_d/c²)(q_i m_j + q_j m_i)`, `C=(Gβ_q²/c⁴) q_i q_j`) is exactly
`F_r = -dV/dr` of the pair potential

```
V_ij(r) = -G m_i m_j / r
          + (Gβ_d / c²) (m_i q_j + m_j q_i) / r²
          - (Gβ_q² / 3c⁴) q_i q_j / r³ ,      q_i = k_i r_i .
```

`sympy` check: `(-dV/dr) - F_oP_radial = 0` identically. Hence a **non-relativistic
many-body Lagrangian** reproduces MULTING by Euler-Lagrange:

```
L = Σ_i ½ m_i ẋ_i²  −  ½ Σ_{i≠j} V_ij( |x_i − x_j| ; Q_i, Q_j ) ,   Q_i = (m_i, q_i).
```

This existence is, by itself, near-trivial: any velocity-independent central pairwise
force `F = -∇V` admits `L = T - V`. The scientific content is therefore NOT "a
Lagrangian exists" but what the construction fixes about the open cosmological
question (ξ), below.

## What the construction fixes (and does not)

1. **Charge is a scalar, taken as given.** `q_i = k_i r_i` is built from the scalar
   internal kinetic energy `k_i`; the author explicitly excludes the internal
   potentials that would make `k_i` (or an orientation) a responsive dynamical d.o.f.
   So in the Lagrangian, `Q_i` is an INPUT PARAMETER, not a field with its own
   equation of motion.
2. **No orientation d.o.f.** The equations carry no `n̂_i`; the many-body Lagrangian
   has only `{x_i}` as dynamical variables.
3. **Non-relativistic only.** `V` is a velocity-independent central potential; the
   `1/c²`, `1/c⁴` are fixed coefficients, not a covariant expansion. A covariant
   field-theoretic action (needed for full cosmological perturbation theory) requires
   choosing a mediator field (scalar/vector/tensor), which the corpus does not
   specify — UNDERDETERMINED.
4. **q-evolution absent.** The cosmological time-dependence `q_i(a)` (the P2 /
   docs/54 Blocker-2 issue) has no Lagrangian in the corpus; `L` above is well-defined
   only for fixed / externally-prescribed `q`.

## Q006 verdict — skeptic-reviewed (context-asymmetry, 2026-07-22)

**Broad closure claim: FALSIFIED. Narrow claim: survives. Q006: NOT closed — deferred
to a named modeling choice.**

**Strongest objection (the one that breaks the closure — I flagged it, the skeptic
confirmed it HIGH-confidence):** the ξ=0 argument kills the *orientation-vector*
coupling `n̂·∇∇Φ`, which was never the only route. The dipole term carries `q = k·r`
with `k` = internal kinetic energy of real sub-object *motions* (the preprint's own
words). In *any* substructure model, external tides pump energy into internal
motions — **tidal heating**: `k_i → k_i⁰ + η·|∇∇Φ|²·τ + …`. Then `δk_i` correlates
with the ambient density `δ`, and the dipole term `∝(m_i q_j + m_j q_i)/r²` picks up
an environment-dependent (induced) piece — an induced-polarization channel **via a
scalar** `η`, needing no orientation vector. The corpus neither includes nor forbids
`η`: the author's "does not need to consider potential energies that affect the
motions of sub-objects" is a *modeling omission*, not a physical statement that the
response is zero. **"Not specified" ≠ "= 0".** An unfixed `η` that controls a
linear-growth signature is, for a cosmology test, worse than either extreme.

**Secondary corrections (skeptic):**
- The scalar `k` in Eqs. 14-16 is an *angular-averaged effective* quantity over a
  substructure that the prose says *has* geometry; the equations *suppress*
  orientation by averaging, they do not *forbid* it. So "no `n̂` in the equations" ⇏
  "no orientation d.o.f. exists" — it means the equations don't resolve one.
- "A non-relativistic Lagrangian exists" is textbook-trivial for any central pair
  potential and contributes nothing to the closure question (it's filler in the Q006
  chain — the sympy residual=0 is an algebra sanity check, not evidence of closure).

**What Q006 IS licensed to claim:**
- Eqs. 14-16 as written contain no orientation-vector d.o.f. `[VERIFIED — text]`
- A pair potential `V_ij(r)` reproducing `F_oP` exists, with a corresponding
  non-relativistic Lagrangian. `[VERIFIED-BASH sympy residual=0]`
- The published model, taken literally as scalar-`k` equations, does not itself
  contain a dynamical orientation coupling `ξ(n̂, ∇∇Φ)`. `[INFERRED]`
- **Under the auxiliary assumption "`k, r` are inert scalars (do not respond to
  external fields)"**, the fσ8 intrinsic-branch degeneracy with ΛCDM (P3) is not
  disturbed by Eqs. 14-16. `[INFERRED, conditional]`

**What Q006 is NOT licensed to claim:**
- "ξ=0 in the physical theory" — the model *omits* the sector, doesn't set it to zero.
- "No induced-polarization channel" — a scalar tidal-heating channel `k(∇∇Φ)` is
  compatible with both the equations and the sub-object prose; the corpus is silent.
- "MULTING as published is cosmologically degenerate with ΛCDM." Correct wording:
  **under-specified in exactly the sector cosmology needs, hence currently untestable
  at linear order without additional modeling choices.**
- "Q006 closed."

**Q006 resolves only via one of:** (a) an author-supplied `η` (scalar response of `k`
to external tides); (b) a covariant field-theoretic completion; or (c) a theorem that
`k` is a rigid conserved scalar under all external field configurations. **None is in
the corpus** — all require TJB (or a modeling decision on our part, clearly labeled as
an extension).

## Honest closing statement for the cosmological branch

*MULTING's published two-body force admits a pair-potential + non-relativistic
Lagrangian description with `q = k·r` at dipole order. The equations do not resolve
any dynamical response of `k` or `r` to external fields — neither an orientation
coupling `ξ` nor a scalar tidal-heating coupling `η`. Under the auxiliary assumption
"`k, r` are inert scalars," the model is degenerate with ΛCDM at background (P2) and
linear-fσ8 intrinsic branch (P3). That assumption is **not stated in the preprint and
not forced by the equations**; consequently Q006 is not closed but **deferred to a
Lagrangian-completion choice about internal response** — a genuinely different (and
more sharply localized) open question than where the branch started.* This does NOT
refute MULTING (NOT_REFUTATION); it names precisely the one undetermined parameter
(`η`) on which the whole cosmological-signature question now hinges.
