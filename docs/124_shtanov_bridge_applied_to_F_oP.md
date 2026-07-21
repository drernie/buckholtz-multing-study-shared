# docs/124 — Shtanov & Sahni (2010) Bridge Applied to F_oP — FALSIFIED (naive form)

**Date:** 2026-07-19
**Status:** `FALSIFIED` (as originally derived) — see Kill Analysis. The literature find
itself (arXiv:1010.6205 is real and on-point) and the general question it raises
survive; the specific naive derivation below does not.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NOT_AUTHOR_ERROR
**Continues:** `docs/123_f_to_hz_bridge_solution_space.md` item 53 ("cheapest test":
apply Shtanov et al.'s generalized cosmic energy equation formalism directly to
`F_oP`).
**Source:** Y. Shtanov & V. Sahni, "Generalizing the Cosmic Energy Equation,"
[arXiv:1010.6205](https://arxiv.org/abs/1010.6205) — verified real via WebFetch of
the full PDF text (title, authors, abstract, and Secs. I-IV independently confirmed).
**Falsified by:** context-asymmetry skeptic review (claim + code only, no reasoning
chain — see `~/.claude/rules/falsification-ladder.md` § Context Asymmetry Rule),
2026-07-19, verdict `FALSIFIED` with a narrow survival path. Confirmed by independent
re-check against the primary source (`data/source_material/buckholtz_preprints...v6.md`,
line ~640) and a second sympy computation, both done by this session, not the
skeptic.

---

## What happened (honest sequence, not retouched)

1. Derived `G_eff = G · lim_{r→∞}[f(r) - r f'(r)] = G` for `F_oP` mapped into
   Shtanov & Sahni's `φ(r) = -(G/r)f(r)` form, via `φ(r) ≡ V(r)/(m_A m_P)`.
   Computer-algebra-verified the limit (sympy). Presented this as a candidate
   finding — that MULTING's dipole/quadrupole terms drop out of the background
   `H(z)` under this bridge.
2. Before presenting it as established, ran an independent context-asymmetry
   skeptic review (per this project's own standing rule: any claim reversing or
   substantially informing prior work gets adversarial review before being
   finalized, established after the NR-015 walk-back on 2026-07-18).
3. Skeptic verdict: **FALSIFIED**, with the load-bearing objection being that the
   mapping `φ(r) = V(r)/(m_A m_P)` silently assumes `B` and `C` (the dipole and
   quadrupole coefficients) are **bilinear in `(m_A, m_P)` alone** — i.e. that
   `B/(m_A m_P)` is a single universal function of `r`, the same for every cluster
   pair. Shtanov & Sahni's entire derivation (their Eqs. 15-18: the many-body
   potential is a convolution `∫[ρ(r')-ϱ]φ(a,|r-r'|)d³r'` of a SINGLE kernel with
   the density field) requires exactly this universality.
4. Checked the primary source directly (not from memory, not from a prior
   session's summary): `data/source_material/buckholtz_preprints...v6.md` line
   640 states plainly, "`k_A` denotes the internal kinetic energy of object-A" —
   an intrinsic, per-cluster physical quantity (for protoclusters/galaxy
   clusters specifically, IGM thermal energy), independently varying from
   cluster to cluster, NOT a quantity proportional to `m_A × m_P`.
5. Recomputed symbolically: `b/G = β_d·(k_A r_A/m_A + k_P r_P/m_P)/(2c²)` —
   explicitly depends on `k_A/m_A` and `k_P/m_P` individually, per pair. This is
   **not** a universal pair-independent function of `r`. **The skeptic's objection
   is confirmed against the primary source, not just plausible in the abstract.**

---

## Kill Analysis (per Minimal Relaxation Rule / Anti-Overfitting Gate discipline)

**What was killed:** the specific claim "`φ(r) = V(r)/(m_A m_P)` is the correct,
universal Shtanov-Sahni kernel for `F_oP`, therefore `G_eff = G` exactly, dipole and
quadrupole drop out of the background `H(z)`." This derivation route is invalid as
stated — Shtanov & Sahni's machinery requires a universal pairwise kernel, and
`F_oP`'s dipole/quadrupole terms (via `k_A`, `k_P` = per-cluster internal kinetic
energies) do not supply one.

**What was NOT killed:**
- `arXiv:1010.6205` itself remains a real, verified, on-point published method for
  the general class of problem ("modified two-body DM potential → Friedmann-like
  equation") — the citation and its applicability to *this class* of question is
  not in doubt, only this session's specific naive application of it.
- The qualitative intuition that sub-leading force terms (falling off faster than
  `1/r` in the potential) *can* plausibly wash out of a properly-derived background
  equation remains a real pattern in the source paper (their three worked examples
  all show it) — just not yet established for `F_oP` specifically.
- The observation in the withdrawn draft that `k_A`, `r_A` etc. are per-cluster,
  individually-varying quantities is itself consistent with — and reinforces —
  this project's own long-standing `docs/54` Blocker 2 ("cluster variable evolution
  missing": `m_A(z)`, `k_A(z)`, `r_A(z)` not given as universal functions). If
  anything, this episode sharpens that blocker: it is not just that these
  variables are *unspecified as functions of z*, they may not even be reducible to
  a single universal *pairwise kernel* at fixed `z`, which is a stronger
  statement than `docs/54` originally made.

**Relaxation map (what would need to change to retry, one assumption at a time):**
1. **Population-average route** — instead of substituting one pair's `(k_A, m_A,
   r_A, k_P, m_P, r_P)` into a single-pair kernel, derive an ensemble-averaged
   `φ_eff(r)` treating `k/m` and `r` as drawn from a population with some
   distribution across clusters, in the spirit of `docs/123` item 7
   (kinetic-theory/Boltzmann-equation route) rather than item 53's naive two-body
   substitution. This is a materially different, harder derivation, not yet
   attempted.
2. **Check for an idealized-regime scaling** — search the preprint for whether
   Buckholtz ever specifies a regime where `k_A/m_A` (a kinetic-energy-per-mass,
   i.e. dimensionally a velocity-squared) is treated as a universal constant
   across the cluster population (e.g. via a virial-equilibrium assumption
   `k_A ~ m_A σ_v²` with a universal velocity dispersion `σ_v`) — not yet checked.
3. **Regularize and redo the volume integral explicitly** — the r→0 non-regularity
   objection (skeptic Point 3) was not fully resolved either; even fixing Point 2
   would still require actually carrying out Shtanov & Sahni's Eq. 15-18 volume
   integral with a regularized `F_oP` kernel, not asserting the r→∞ tail survives
   by analogy to their three worked examples.

**Per the Anti-Overfitting Gate:** none of these three relaxations has been
attempted yet. This document does not promote any of them to `[HYPOTHESIS]` status
— they are `[SPECULATIVE]` relaxation candidates only, listed for a future session,
not pursued further today without a new, independent motivation (AOG-5) beyond
"it would rescue the original claim."

---

## What remains genuinely useful from this exercise

1. **The literature search itself succeeded** (this document's original purpose,
   per the user's request "search for a ready-made bridge"): `arXiv:1010.6205` is a
   real, correctly-scoped, previously-unused-in-this-project source directly on
   point for `docs/54`/`docs/92`'s Blocker 1/Gap 2. It remains a legitimate
   candidate to revisit via the population-average route above.
2. **A sharper version of `docs/54`'s Blocker 2** is now on record: cluster
   variables are not just unspecified *functions of z*, they may resist reduction
   to a single universal pairwise kernel even at fixed `z`, which the
   population-average relaxation route would need to address explicitly.
3. **Process lesson**: this is the second time this project (after NR-015,
   2026-07-18) has caught its own high-confidence derivation via a context-
   asymmetry skeptic pass before it left the session. Worth a `lessons_learned.md`
   entry alongside NR-015's — same discipline, same payoff, applied to a
   literature-adaptation claim this time rather than a statistical-correlation
   claim.

---

## Falsifier for a future retry

If the population-average route (Relaxation 1) is attempted and produces a
genuine, pair-independent effective kernel `φ_eff(r)` for `F_oP`'s dipole/quadrupole
terms, re-run Shtanov & Sahni's `G_eff` formula on `φ_eff` and check whether
`G_eff = G` still holds. If it does, the original qualitative conclusion (dipole/
quadrupole absent from background `H(z)`, present only in cluster-scale virial
dynamics) would be independently re-derived, this time validly. If it does not, the
qualitative direction itself is wrong, not just this session's shortcut to it.
