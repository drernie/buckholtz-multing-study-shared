# Author-Facing Note — H_FLRW Baseline Clarification (DRAFT)

**Status:** DRAFT | NOT_SENT | AUTHOR_CONFIRMATION_REQUIRED
**Labels:** NOT_VALIDATION | NOT_REFUTATION | NOT_AUTHOR_ERROR | DIAGNOSTIC_ONLY
**Date:** 2026-06-01
**Decision to send:** Sergei's call only — do NOT send without explicit approval.

> Purpose: turn the internal `docs/66` H_FLRW provenance diagnostic into ONE
> short, neutral talking point for the call. This is a **clarification question**
> about which baseline reproduces the Table A1 H_FLRW column — not a claim that
> anything is incorrect.

---

## The one-paragraph version (for the call)

> "When I tried to reproduce the H_FLRW column of Table A1 with a standard flat
> ΛCDM baseline (Planck 2018: H0 = 67.4, Ωm = 0.315), I could not match it — and
> the gap grows smoothly with redshift, from about 1 km/s/Mpc at z = 0.06 to
> about 710 km/s/Mpc at z = 8.5. Because the difference is so systematic rather
> than scattered, it looks like the H_FLRW column was built with a different
> parameter set, a different convention, or a different calculator. Could you
> tell me which cosmological baseline (H0, Ωm, ΩΛ, and the H(z) convention)
> should be used as the reference for H_FLRW? That would let me line up FLRW and
> MULT on the same footing."

This is neutral, specific, and invites collaboration. It does not assert error.

---

## Supporting numbers (only if he asks for detail)

Assumed baseline: flat ΛCDM, H0 = 67.4, Ωm = 0.315, ΩΛ = 0.685 (Planck 2018).
Reproduced via `scripts/run_table_a1_recomputation.py` → `docs/66`.

| z | reported H_FLRW | recomputed | diff (km/s/Mpc) |
|---|---:|---:|---:|
| 0.06 | 68.1 | 69.4 | −1.3 |
| 1.00 | 95.7 | 120.7 | −25.0 |
| 3.20 | 187.6 | 330.3 | −142.8 |
| 5.00 | 265.2 | 558.7 | −293.6 |
| 8.50 | 398.5 | 1109.0 | **−710.6** |

**Key signal:** the discrepancy is **monotonic in z**, not scattered. Random
transcription noise would not grow smoothly; a systematic offset points to a
different baseline/convention/tool — exactly the kind of provenance detail worth
pinning down before any model comparison.

Secondary observation (only if relevant): Row 1 (z = 0) sigma_FLRW does not match
any of the three conventions tested (reported −5.600 vs recomputed +5.091),
suggesting z = 0 may use a special treatment.

---

## Why this is a useful contribution (framing)

- It is a **reproducibility prerequisite**: FLRW vs MULT comparison is only fair
  once both use a documented, shared H(z) baseline.
- It is **author-respecting**: the question assumes a defensible reason exists and
  asks for it, rather than asserting a problem.
- It pairs naturally with the Branch A/B framing in `docs/93` (reproduce an
  intended procedure, or formalize an exploratory one).

---

## What NOT to say

- ❌ "Your H_FLRW column is wrong / incorrect."
- ❌ "The table has errors."
- ❌ Any validation/refutation of MULTING.
- ❌ Do not present the full table unprompted — lead with the one paragraph.

## Send checklist (if Sergei approves later)

- [ ] Sergei explicitly approves sending
- [ ] Wording re-read for neutral tone
- [ ] No β numbers or internal jargon in the sent version
- [ ] Framed as a question, not a finding
