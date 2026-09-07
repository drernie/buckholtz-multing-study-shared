# FINDING P218 — v82's own supplemental code feeds Planck ΛCDM into the
# MULTING force through FOUR channels, not the one this project had recorded

**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Provenance:** found while independently checking an external re-reading's
claim that `H → ṁ → F_acc → H` might be an unclosed self-consistent loop.
That specific alarm is answered directly (§2), and answering it surfaced a
broader fact this project's own 120+ files mentioning "circular" had not
stated precisely (§3).

---

## 1. The question that triggered this

`multing_core.py` builds `F_accretion(z)` from a mass-accretion rate,
`m_dot(z) = 1.1 · H(z) · M(z)`. The question: which `H` — MULTING's own,
under construction, or an external one? If MULTING's own, `addot_over_a(z)`
would need to be solved as an implicit equation in `H`, not evaluated
pointwise.

## 2. Answered directly — it is Planck ΛCDM, not self-consistent

**`multing_core.py:125-129`** `[VERIFIED-code]`:

```python
def Hlcdm_si(z):
    ...
    return H0_planck_si * Efun(z)
```

**`multing_core.py:132-134`**:

```python
def m_dot(z):
    """Mass accretion rate (kg/s)."""
    return 1.1 * Hlcdm_si(z) * M_of(z)
```

`Hlcdm_si` is exactly the Planck ΛCDM Hubble function
(`H0_planck_si = 67.4 km/s/Mpc`, line 42), not `H_of_z_kms`
(MULTING's own output, defined later at line 187). **There is no implicit
equation to solve.** `addot_over_a(z, b1, b2)` (line 150) is a pointwise
function of `z` alone, given `b1, b2` — the accretion term is an external
ΛCDM input, not a feedback loop.

## 3. That answer opens a wider fact: FOUR channels, not one

Searching this project's own record: **120 files mention "circular"**
`[VERIFIED-grep]`, essentially all pointing at one channel — `r_X(z)`'s
dependence on `E_ΛCDM(z)` via `rho_crit(z)`, the one v82 itself names its
*"most significant residual circularity"* (`docs/153`, `P196`/`P197`).
Re-reading `multing_core.py` end to end found **three more, unrecorded**:

| # | quantity | line | uses |
|---|---|---|---|
| 1 | `T_keV_of(z)` (cluster temperature) | 79-81 | `Efun(z)^(2/3)` |
| 2 | `Mgas_of(z)` (ICM gas mass) | 84-86 | `Efun(z)/Efun(z_piv)` |
| 3 | `rho_crit(z) → R_of(z)` (cluster radius) | 94-101 | `Efun(z)²` — **the recorded one** |
| 4 | **`m_dot(z) → F_accretion(z)`** | 125-134 | **`H0_planck_si · Efun(z)`** |

`Efun` itself (line 69-71) is labelled in the code's own comment:
*"LCDM benchmark curve and for E(z) inside MULTING's own scaling laws."*
The comment already says both uses exist; this project's record had only
the third.

## 4. Consequence for every v82-pinned number this project holds

`(β₁, β₂) = 1.4335e10 / 7.8067e17`, `P190`–`P193` (including `H² < 0` at
`z ≈ 16.96`), the ICM branch, `MODEL_SPEC_AUDIT` — **every one** is computed
through `multing_core.py`, and therefore through all four channels, not
just the radius one this project's provenance notes have flagged. None of
this changes any existing verdict — v82 states channel 3 as an admitted
limitation and this project already measured its consequence (`P196`/
`P197`). Channels 1, 2, 4 were simply unrecorded, not previously assessed.

## 5. What this does and does not establish

**Establishes:** the scope of "residual ΛCDM dependence" in v82's own
executable model is wider than this project's documentation stated.

**Does not establish** that any fitted result is wrong — v82's own
self-similar scaling relations (mass-temperature, mass-gas-fraction) are
standard cluster astrophysics, not unique to this circularity question, and
using `E(z)` inside them is a modeling choice the paper states openly (it
is *not* hidden). The severity question — does using ΛCDM's `E(z)` inside
these scalings materially bias the fitted `(β₁,β₂)` relative to a
self-consistent alternative — is untested and is `docs/158` item G3
(joint uncertainty propagation).

**Answers the specific alarm** that motivated this check: the accretion
term is not a hidden self-consistency loop. It is an explicit, stated-in-
code external input.

## 6. Caveats

1. `src/` (this project's own v6-era reconstruction, 39 files, 995 tests)
   contains **zero** references to `Efun`/`E_lcdm`/`Hlcdm` — it has no
   `H(z)` pipeline of its own. Every `H(z)`-related number in this project
   comes from importing v82's own `multing_core.py` as-is
   (`_v82_shared_physics.py`, `P176`-`P193`, ICM `stage1`).
2. No Step 8a pass on this finding. It is a direct code read with line
   numbers, not an inference chain — lower risk than the four findings
   retracted earlier today, but still unreviewed.
