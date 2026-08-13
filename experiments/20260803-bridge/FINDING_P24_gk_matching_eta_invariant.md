# P24 — a single parameter η=κ/g controls the k-sector's strength relative to gravity; β_q/β_d=√6/2 survives untouched

**Date:** 2026-08-13
**Origin:** user-directed research plan, following P21→P23's establishment
that `g` (monopole coupling) and `κ` (dipole coupling) are structurally
independent parameters of the *same* action, both sharing the *same*
missing field-normalization constant `A`. This finding asks the natural
next question: does inserting `g`, `κ`, `A` explicitly into P1's own
already-verified multipole derivation (which implicitly set `g=1` and never
separated `A` from the geometric coefficients) reveal a single physical
parameter controlling the k-sector's strength *relative to gravity*?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P24_gk_matching_eta_invariant.py`

## 0. Naming note — read before citing, avoids a real symbol collision

`β_d=2` and `β_q=√6` are **already established, verified, fixed pure
numbers** in this project (`FINDING_two_charge_completion.md`, 2026-08-10)
— the multipole-expansion coefficients relating `ℓ_d`, `ℓ_q²` to
`u_A+u_B`, `u_A·u_B`, where `u_i≡κ·k_i·r_i/(c²·m_i)`. This is an
**intra-k-sector** ratio (dipole geometry vs. quadrupole geometry) that
never involves `g` — `m_i` there is used only as a normalizing denominator
inside `u_i`, not as the field-coupling charge. **This finding does not
redefine `β_d`, `β_q`.** The genuinely new quantity computed here — the
**cross-sector** force ratio (k-sector strength vs. monopole/gravity
strength) — is given a *different* name, `χ_d`, `χ_q`, specifically to
avoid the Type-1 symbolic-overload error `research-methodology.md` flags
(same symbol, two incompatible meanings, in two different constructions).

## 1. Method

Reused P1's own `tiers_from_kernel` function **unchanged** (same `K=1/s`
massless kernel, same mirror-symmetric physical-dipole construction) —
positive control: `g=A=1` must reproduce P1's already-published
coefficients `2` and `6` exactly. Then substituted, for the first time in
this project's multipole work:

- `mᵢ → g·Mᵢ` (monopole charge = coupling `g` times mass, per the action's
  own `g·mᵢ·φ` term)
- `qᵢ → −κ·Kᵢ/c²` (dipole charge, per `FINDING_two_charge_completion.md`'s
  own `q=−κk/c²`)
- `dᵢ → rᵢ` (lever arm = body radius, that finding's own convention)
- one overall factor `A` (P21's field normalization — enters once, since
  force `= −∇[coupling₂·A·φ_raw,1(x₂)]`)

## 2. Result (sympy-verified, positive control passed)

```
F_mm = A·g²·M_A·M_B/r²                                    (matches P21/P22's A·g² exactly)
F_km = −2·A·g·κ·(K_A·M_B·r_A + K_B·M_A·r_B)/(c²·r³)
F_kk = 6·A·κ²·K_A·K_B·r_A·r_B/(c⁴·r⁴)
```

Cross-sector ratios — `A` cancels identically from every one:

```
χ_d := F_km/F_mm = −2κ·(K_A·M_B·r_A+K_B·M_A·r_B)/(M_A·M_B·c²·g·r)
χ_q := F_kk/F_mm = 6κ²·K_A·K_B·r_A·r_B/(M_A·M_B·c⁴·g²·r²)
```

Substituting `κ=η·g` — `g` **also** cancels identically:

```
χ_d(η) = −2η·(K_A·M_B·r_A+K_B·M_A·r_B)/(M_A·M_B·c²·r)      ~ η¹
χ_q(η) = 6η²·K_A·K_B·r_A·r_B/(M_A·M_B·c⁴·r²)                ~ η²
χ_q/χ_d(η) ~ η¹
```

**`η=κ/g` is the sole parameter controlling the k-sector's force strength
relative to gravity** — confirmed symbolically, not asserted.

`β_d=2`, `β_q=√6`, `β_q/β_d=√6/2` are **unchanged** — confirmed by direct
inspection: they were computed *before* any `g`/`κ`/`A` substitution, from
`f_km`, `f_kk` alone, and `g` never enters `u_i`'s own definition at all.
This was already established 2026-08-10; this finding re-confirms it
survives the new `g`-insertion rather than re-deriving it.

## 3. Honest caveat, stated proactively — is this a discovery or an algebraic necessity?

This reduction to a single `η` **follows near-automatically from the
already-assumed bilinear coupling form**: the action couples each body
through exactly *one* power of `g` **or** `κ` — never both, never a cross
term (`g·κ` on the same body). Given that structure, *any* two force tiers
built from these charges will reduce to a pure ratio of coupling constants
by dimensional bookkeeping alone — this is closer to "the algebra of the
already-assumed action shape" than an independent new discovery about
MULTING's physics, in the same sense P16's skeptic review downgraded a
"transfer confirmed" claim to "guaranteed by construction." What is *not*
guaranteed, and *is* the finding's real content: (a) that the reduction is
to `η¹` for dipole and `η²` for quadrupole *specifically* (not some other
power, which depends on the actual bilinear degree of each tier); (b) that
`A` cancels identically from cross-sector ratios (confirms P21/P22's
convention consistently, not a new fact but a needed cross-check); (c) that
`β_q/β_d` is untouched — a fact that was *not* obviously guaranteed in
advance (it required checking `g` doesn't enter `u_i`, not just assuming it).

## 4. What this does NOT establish

1. **A numeric value for `η`, `g`, or `κ` individually.** Only the
   *functional form* of the cross-sector dependence on `η`.
2. **That this is MULTING's own physics**, only that this project's own
   reconstructed action has this algebraic structure — same NOT_AUTHOR_ERROR
   scoping as every prior finding.
3. **Anything about `Ω_φ` or the still-open dimensional-constant value of
   `A`** — P21/P22's own scope limits apply unchanged; this finding adds a
   structural relation, not a numeric one.
4. **A resolution of whether this `η`-reduction is deep or superficial** —
   §3's caveat is stated, not resolved; a fair reading is that it's mostly
   algebraic necessity with a genuinely non-trivial residual (the specific
   powers, and the `β_q/β_d` survival check).
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   P1's action, not a claim about TJB's own theory.

## Reproduction

```bash
python experiments/20260803-bridge/P24_gk_matching_eta_invariant.py
```

## Skeptic verdict (context-blind, Step 8a)

*Pending — to be run with only this file + `P24_gk_matching_eta_invariant.py`
+ `two_field_action_closure.py` + `FINDING_two_charge_completion.md` +
`FINDING_P21_shared_phi_normalization_constraint.md` (corrected version), no
session history.*
