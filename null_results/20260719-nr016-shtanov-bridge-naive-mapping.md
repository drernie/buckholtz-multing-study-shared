# NR-016 — Shtanov & Sahni bridge applied to F_oP via naive per-pair mapping — REJECTED

**Date:** 2026-07-19
**Verdict:** REJECT (naive derivation route falsified by skeptic + primary-source check)
**Branch:** literature-derived bridge candidate for F_oP → H(z), continuing
`docs/123` item 53 ("cheapest test": apply Shtanov & Sahni arXiv:1010.6205 directly to F_oP)

---

## Claim (falsified)

Mapping `F_oP`'s two-body potential into Shtanov & Sahni's general form
`φ(r) = -(G/r)f(r)` via `φ(r) ≡ V(r)/(m_A m_P)` and applying their formula
`G_eff = G·lim_{r→∞}[f(r)-rf'(r)]` gives `G_eff = G` exactly, independent of
`β_d`, `β_q` — i.e. MULTING's dipole and quadrupole terms drop out of the
background `H(z)` under this bridge, with any real signature confined to
cluster-scale virial dynamics instead.

## Why falsified

| Test | Result | Evidence |
|------|--------|----------|
| Arithmetic of `f(r)-rf'(r) → 1` as `r→∞` | Correct, no error | `[VERIFIED-BASH]` sympy |
| Is `φ(r)=V(r)/(m_A m_P)` a valid universal Shtanov-Sahni kernel? | **No** — `b/G = β_d(k_A r_A/m_A + k_P r_P/m_P)/(2c²)` depends on `k_A/m_A`, `k_P/m_P` individually, not just the product `m_A m_P` | `[VERIFIED-BASH]` sympy re-derivation |
| What is `k_A` in the source? | "the internal kinetic energy of object-A" — an intrinsic, per-cluster physical quantity (IGM thermal energy for protoclusters/galaxy clusters), independently varying across clusters | `[VERIFIED-DIRECT-QUOTE]` `data/source_material/buckholtz_preprints...v6.md:640` |
| Does Shtanov & Sahni's derivation require a single universal pairwise kernel? | Yes — their Eqs. 15-18 build the many-body potential as a convolution of ONE kernel `φ(r)` with the density field | `[VERIFIED-WEBFETCH]` full PDF text, Sec. II.B-III |
| Is the `r→0` non-regularity of `f(r)` (required `lim_{r→0} rf'(r)=0`, violated here) harmless as originally claimed? | Original dismissal ("only the delta-function term is affected") was imprecise; the volume-integral construction requires convergence, not just a well-behaved tail | skeptic, `[INFERRED]`, medium-strength objection, not independently re-derived by this session |

**Root cause:** `B` and `C` (dipole/quadrupole coefficients in `F_oP`) are defined via
per-cluster internal-kinetic-energy terms `k_A`, `k_P` that do not factor into a
mass-bilinear universal function — the naive substitution treated a per-pair,
per-cluster-property-dependent coefficient as if it were a fixed physical constant
like `G`, silently assuming a scaling (`B ∝ m_A m_P × f(r)` for one shared `f`) that
the source preprint does not support.

## Kill Analysis

**What this KILLED:**
- The specific claim that `φ(r)=V(r)/(m_A m_P)` is *the* correct Shtanov-Sahni
  kernel for `F_oP`.
- The conclusion "`G_eff=G` exactly, dipole/quadrupole absent from background H(z)"
  as *established* by this route — it is not derived validly as stated.

**What this did NOT kill (survives):**
- `arXiv:1010.6205` (Shtanov & Sahni) itself as a real, verified, on-point published
  method for "modified two-body DM potential → Friedmann-like equation" — still a
  legitimate literature candidate for `docs/54`/`docs/92`'s Blocker 1.
- The qualitative pattern that sub-`1/r` correction terms CAN wash out of a
  properly-derived background equation (demonstrated in the source paper's own
  three worked examples) — not disproven, just not established for `F_oP`.
- `docs/54`'s Blocker 2 (cluster variable evolution missing) — this episode
  sharpens it: `k_A`, `r_A` etc. resist reduction to a universal pairwise kernel
  even at fixed `z`, a stronger statement than "unspecified as functions of `z`."

**Relaxation Map (surviving option space):**
- Remove: naive single-pair substitution as the derivation route → dead.
- Weaken: attempt a population-averaged effective kernel `φ_eff(r)` treating
  `k/m`, `r` as drawn from a cluster-population distribution (kinetic-theory/
  Boltzmann route, `docs/123` item 7) — not yet attempted; genuinely harder.
- Replace: check whether the preprint specifies an idealized regime where `k_A/m_A`
  is a universal constant (e.g. virial-equilibrium `k_A ~ m_A σ_v²` with universal
  `σ_v`) — not yet checked against the full preprint text.

## Forbidden use

Do NOT cite this session's derivation as "Shtanov & Sahni prove MULTING's dipole/
quadrupole are absent from H(z)." The citation is real; the application to `F_oP`
via a naive per-pair mapping is REJECTED. Any future claim along these lines needs
the population-average relaxation route above, independently re-derived, not a
restatement of this session's shortcut.

## Correct next direction

If this line is worth pursuing further, the next step is the population-average
kernel derivation (Relaxation 1), not a defense of the naive mapping. Cheapest
check before that: search the full preprint for any stated `k_A`-mass scaling
relation (Relaxation 3) — minutes of work, could make the harder derivation
unnecessary if a simplifying assumption is already given by the author.

---

*REJECT — literature-application bridge falsified. skeptic [FALSIFIED, context-asymmetry]
+ primary-source cross-check [VERIFIED-DIRECT-QUOTE] + sympy re-derivation [VERIFIED-BASH].*
*Parent: `docs/123` item 53 (Shtanov & Sahni candidate, rank 2/12) + `docs/124` (full
derivation, corrected in place after this falsification).*
