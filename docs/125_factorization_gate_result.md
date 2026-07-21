# docs/125 — P1 Universality/Factorization Gate: Result

**Date:** 2026-07-21
**Status:** SPLIT VERDICT — algebraic factorization `CONFIRMED`; the interpretation
that it revives the Shtanov-Sahni bridge is `FALSIFIED`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Continues:** `null_results/20260719-nr016-shtanov-bridge-naive-mapping.md` (its
Relaxation Map item 1: "population-averaged / non-single-pair kernel"). This gate
tested the matrix-kernel form of that relaxation.
**Artifact:** `scripts/factorization_gate.py` (sympy, exit 0, ruff clean).
**Skeptic:** context-asymmetry review of the *interpretation only* (algebra given as
verified), 2026-07-21, verdict FALSIFIED.

---

## The question (per user's P1, session 24)

Can `F_oP = F_m - F_d + F_q` (preprint Eqs. 14-17) be written with a pairwise kernel
that is **global** (identical for every object pair), as Shtanov & Sahni's
cosmological bridge (arXiv:1010.6205) requires — either as a single scalar kernel
`φ(a,r)` or a finite matrix of kernels `φ_αβ(a,r)`?

## What the gate established (CONFIRMED, sympy-verified)

**Licensed claim:** *`F_oP` admits an exact 2×2 bilinear factorization with a global
kernel matrix and a per-object charge vector `Q_i = (m_i, q_i)`, `q_i ≡ k_i r_i`.*

- Single universal SCALAR kernel `F_ij = -m_i m_j ∂_r φ(r)`: **FAILS**.
  `dipole/(m_i m_j) = 2Gβ_d/c²·(k_i r_i/m_i + k_j r_j/m_j)` is pair-dependent
  (confirms NR-016's obstruction at the scalar level).
- Finite 2×2 MATRIX kernel: **EXACT**. With `Q_i=(m_i, k_i r_i)`, the whole pair
  potential is `Q_iᵀ K(r) Q_j` with **global** (pair-independent) entries
  `κ_mm=G`, `κ_mq=2Gβ_d/c²`, `κ_qq=Gβ_q²/c⁴`. All three residuals exactly 0.
- Non-trivial structural fact: the **same** charge `q_i=k_i r_i` serves both the
  dipole (cross term `q_i m_j + q_j m_i`) and the quadrupole (`q_i q_j`) — a genuine
  2-species structure, not three separate per-multipole charges. This is in the
  preprint's own equations (`r_dA=β_d r_A` ⇒ `k_A r_A` in the dipole;
  `r_qAB²=β_q² r_A r_P` ⇒ `(k_A r_A)(k_P r_P)` in the quadrupole), not pattern-matched.

## What the gate does NOT establish (FALSIFIED interpretation)

**NOT licensed** (verbatim from the skeptic): "Shtanov & Sahni is revived" /
"NR-016's obstruction is non-fatal" / "next step is the multi-component Shtanov
extension."

**Strongest objection (why):** NR-016 was killed by a **physical** fact, not an
algebraic one. Shtanov & Sahni's derivation (their Eqs. 15-18) subtracts a
**conserved cosmological background** `ϱ` from the density field and convolves the
kernel with `[ρ - ϱ]`. The matrix-kernel form promotes `q_i = k_i r_i` to a second
"charge density" `ρ_q(r) = Σ k_i r_i δ(r - r_i)` — but `k_i` (internal kinetic
energy) and `r_i` (radius) both evolve with cosmic time and have **no conserved
background `ϱ_q(t)`** for the subtraction to use. The factorization resolves an
algebraic hurdle while leaving the physical obstruction of NR-016 intact — arguably
**worse**, because it now requires a background for a manifestly non-conserved
quantity. AOG-5 (independent motivation) also fails: the matrix factorization was
motivated by the desire to rescue the mapping, not by independent physics.

This is a clean instance of **"algebraic revival of a physical null"** — resolving
the equation-level obstruction of a killed result without touching the physical
reason it was killed. Logged as a process pattern in `lessons_learned.md`.

## Kill Analysis

**What was killed:** the inference "2×2 factorization ⇒ Shtanov revived / matrix-
component extension is the licensed next step."

**What was NOT killed (survives):**
- The algebraic factorization itself — a real, exact, reusable structural fact about
  `F_oP` (it is a 2-species bilinear form with charges `(m_i, k_i r_i)`). Recorded as
  a pearl.
- NR-016 stands, now **sharpened**: its obstruction is specifically the absence of a
  conserved background for the second charge, not merely "the naive mapping was
  sloppy."
- `docs/54` Blocker 2 (cluster-variable evolution unknown) is confirmed as the true
  bottleneck: even a perfect kernel factorization cannot proceed without the
  cosmological-time evolution / conservation structure of `k_i r_i`.

**Relaxation Map (WEAKENED-upgrade criteria — from the skeptic, before any
convolution may be invoked):**
1. Exhibit a **scaling background `ϱ_q(t)`** for `Σ k_i r_i` (a conserved or
   known-evolution comoving density for the second charge). Not known to exist.
2. Show that `q_i` **virializes** to `q_i ∝ G M_i²` — i.e. by the cosmic virial
   theorem `k_i ~ (1/2) G M_i²/R_i`, so if the dipole radius `r_i ≈ R_i` then
   `q_i ~ (1/2) G M_i²` and `ρ_q` reduces to a **mass-squared-weighted** functional
   (a 2-point statistic of `ρ_m`), which Shtanov-Sahni-type machinery *can* handle.
   This is the most concrete lead, but it (i) assumes virial equilibrium, (ii)
   assumes `r_i ≈ R_i`, and (iii) changes the scaling to `M²` (no longer the
   preprint's independent `k`, `r`) — a materially different model, not the current
   `F_oP` as written. Route to P3 (kinetic coarse-graining), not a Shtanov shortcut.

Per the Anti-Overfitting Gate, neither relaxation is promoted to `[HYPOTHESIS]` —
both are `[SPECULATIVE]` leads for a future session.

## Strategic consequence (updates `decisions.md` P1 line)

The gate did its job: it **cleanly separated the algebraic obstruction from the
physical one**. NR-016's kill is now known to be physical (no conserved background
for the second charge), which is *harder* to escape than an algebraic obstruction
and *closer to a no-go ingredient* than a bridge-revival.

- The matrix-Shtanov shortcut is **closed** (this document).
- The real remaining physical routes are the user's **P3** (multi-species kinetic /
  continuum coarse-graining — the route that must confront the `k/m` distribution
  and its cosmic evolution head-on, exactly the missing `ϱ_q(t)`) and **P4** (scoped
  no-go: "object-dependent, non-conserved interaction charges + isotropy + no
  independent closure ⇒ a single pairwise `F_oP` does not fix a unique background
  `H(z)`"). The skeptic's own strongest objection is close to being P4's central
  lemma.
- Candidate G remains an `INDEPENDENT PHENOMENOLOGICAL BENCHMARK` (unchanged);
  nothing here promotes it.

## Falsifier for this document's own (surviving) claim

If a future derivation exhibits a conserved/known-evolution comoving background
`ϱ_q(t)` for `Σ k_i r_i` (Relaxation 1) OR rigorously reduces `ρ_q` to a functional
of `ρ_m` via virialization (Relaxation 2), then the matrix-kernel Shtanov extension
becomes attemptable and this document's "FALSIFIED interpretation" would upgrade to
`WEAKENED` (attemptable under stated extra assumptions). Absent either, the licensed
claim stays purely algebraic.
