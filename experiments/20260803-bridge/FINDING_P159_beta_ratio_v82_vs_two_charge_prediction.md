# FINDING P159 — β₁/β₂ (v82) vs. β_d/β_q (this project's own derivation):
# not a units mismatch, a ratio mismatch — and a category mismatch flagged
# in the process

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math (dimensional analysis + symbolic verification)
**Verdict (final, second correction — both open gaps resolved by
finding v6's own RAW equations):** `RATIO-COMPARISON-CONFIRMED-BY-TWO-
GENUINELY-INDEPENDENT-PRIMARY-SOURCES (v6's OWN Eqs 14-17, BEFORE
β_d/β_q substitution, MATCHED DIRECTLY AGAINST v82's OWN Eqs 2-4 —
sympy-exact, no circularity); β_d(TJB)=2κ, β_q(TJB)=κ√6 (κ = this
project's own undetermined two-point-charge normalization — NOT TJB's
notation at all, confirmed absent from v6); κ CANCELS EXACTLY in the
ratio β_q/β_d=√6/2, independent of κ's value or dimension. The `19.5×`
gap between this ratio and v82's fitted analog `√β2/β1` is real and
well-grounded, not contingent on the two gaps a skeptic found in the
first draft — both are now resolved (§2, §2.1).
**Correction history (2026-08-30, two rounds, both resolved in place, not
silently):** Round 1 (original draft) claimed "confirmed two independent
ways" and an unconditional "genuine mismatch" — a dispatched skeptic
found the two "independent" routes were circular (one built from the
other) and that an internal parameter `κ` was never pinned down, making
`"β_d=2"` contingent on an unstated choice. Round 2 (this update, at the
user's own direction: "найди определение u_A у TJB, проверь κ") located
`u_A` in v6's primary text — it does not exist there; it is this
project's own internal symbol. But the search surfaced v6's own **raw**
Eqs. 14-17 (page/lines below), which supply a second, genuinely
independent primary source, and matching them against v82's Eqs. 2-4
directly (sympy, both simplified separately, compared, exact match)
resolves both Round-1 gaps at once: independence is real (§2), and `κ`'s
role is now precisely known — it cancels in the ratio (§2.1).
**Continues:** `docs/150` §6 item 4 ("Do the `A·g²` growth-rate ceiling and
v82's own fit parameters connect... once unit conventions are reconciled?")
and `docs/149` §2's own flagged-but-unchecked note ("These are not
obviously the same fitted quantities under a unit change; not checked
here.") This file works through it, further than before, but does not
settle it.

## 0. Why "unit reconciliation" was the wrong framing to start from

The task as posed ("compare β1/β2 with our β_d/β_q, units") presumes a
units-conversion problem. Direct dimensional analysis of v82's own
printed equations (§1) shows there isn't one — β₁, β₂ are **already
dimensionless**, exactly like our own β_d, β_q. The real question, once
that's settled, turns out to be sharper: **do these dimensionless numbers
even answer the same question?**

## 1. v82's `β₁`, `β₂` are dimensionless — `[VERIFIED-PDF p.4-5, VERIFIED-sympy]`

v82's own equations, read directly from the PDF (not the markdown
conversion):

```
F^(0) = -G m_A m_P / s^2                                          (2)
F^(1) = β1(-G k_A c^-2 m_P r_A/s^3) + β1(-G m_A k_P c^-2 r_P/s^3)  (3)
F^(2) = β2(-G k_A k_P c^-4 r_A r_P/s^4)                            (4)
```

**Correction (2026-08-30):** `FINDING_P156`/`P157`/`P158` all quoted Eq. 3
with an extra `/2` in the denominator (`.../(2c²s³)`), inherited from a
misreading earlier in the session. The PDF has no such factor — verified
by direct re-reading of p.4 for this file. The `/2` did not affect any of
those files' actual conclusions (P156/P157 used only the radial-power
structure; P158 used only mass-exponents — both invariant to an overall
constant), but is corrected here for the record, since this file's own
numeric ratio depends on getting the coefficient exactly right.

Symbolic dimensional analysis (`[VERIFIED-sympy]`, `P159` script §1),
treating `k_A` as an energy (per v82's own text, p.4: "`k_A` is the
thermal energy... `k_A/c²` has dimensions of mass"): all three equations
balance to force (`M·L·T⁻²`) with **`β1`, `β2` absent from the
dimensional bookkeeping entirely**. Both are true, unit-system-independent
dimensionless numbers — not "dimensional, large-magnitude values" as an
earlier, uncorrected note in `docs/149` §2 speculated without checking.

## 2. Structural correspondence — resolved via v6's own RAW equations (Round 2)

**`u_A` is not TJB's notation.** `[VERIFIED-grep]`: zero hits for `u_A`,
`uA`, `u_P` anywhere in v6's text. It is this project's own internal
symbol (`two_charge_completion.py` line 162), invented to help derive a
candidate value for `β_d`, `β_q` — not something to look up in TJB's own
work. Searching for it, though, surfaced something better: v6's own
**pre-substitution** force law.

**v6's own raw equations** (`data/source_material/buckholtz_
preprints202511.0598.v6_pymupdf-clean.md`, lines 780-811, `[VERIFIED-
grep]`), quoted in full because they turn out to be the key:

```
F_m = G m_A m_P / r^2                                              (14)
F_d = (G k_A c^-2 m_P |r_dA| / r^3) + (G k_P c^-2 m_A |r_dP| / r^3)  (15)
F_q = G k_A k_P c^-4 |r_qAB|^2 / r^4                                (16)
F_oP = F_m - F_d + F_q                                              (17)
...
r_dA = β_d r_A     (18)      r_dP = β_d r_P     (19)
|r_qAB|^2 = (β_q)^2 r_A r_P                                        (20)
```

Eqs. (14)-(17) give `F_d`, `F_q` in terms of the **undetermined**
lengths `r_dA`, `r_dP`, `r_qAB` — *before* Eqs. (18)-(20) fix them via
`β_d`, `β_q`. This is genuinely independent of anything this project's
own `factorization_gate.py` built (that file's kernel, per §0's original
finding, was constructed BY substituting Eqs. 18-20 into a generic
template — one route, not two). v6's Eqs. (14)-(17) are TJB's own,
pre-substitution primary source.

**Substituting Eqs. (18)-(20) into (15)-(16) and comparing directly
against v82's own Eqs. (3)-(4)** `[VERIFIED-sympy]`: both simplified
independently (v6's own `F_d/F_m`, `F_q/F_m` from its raw equations;
v82's own `F^(1)/F^(0)`, `F^(2)/F^(0)` from its printed equations), then
compared — **exact symbolic match** under `β_d→β1`, `β_q²→β2`:

```
v6  (after its own Eq.18-20):  F_d/F_m = β_d·(k_A m_P r_A + k_P m_A r_P)/(c² m_A m_P r)
v82 (Eq. 3, directly):         F^(1)/F^(0) = β1·(k_A m_P r_A + k_P m_A r_P)/(c² m_A m_P r)   -- IDENTICAL

v6  (after its own Eq.18-20):  F_q/F_m = β_q²·k_A k_P r_A r_P/(c⁴ m_A m_P r²)
v82 (Eq. 4, directly):         F^(2)/F^(0) = β2·k_A k_P r_A r_P/(c⁴ m_A m_P r²)              -- IDENTICAL
```

This is genuine, two-source, non-circular corroboration: `β1(v82) =
β_d(v6)` directly, `β2(v82) = β_q(v6)²` (squared) — confirmed from each
paper's own equations, not from this project's own kernel construction.

## 2.1 κ resolved: it cancels exactly in the ratio, confirmed by the same match

Matching `two_charge_completion.py`'s own construction (`q_A=-κk_A/c²`,
lever arm `d_A=r_A`) against v6's **raw** `F_d`, `F_q` (§2, before Eq.
18-20 fixes the numbers) — not against an assumed target — and solving
for what `β_d`, `β_q` must be `[VERIFIED-sympy]`:

```
β_d(TJB) = 2κ           (not "2" — the "2" printed by two_charge_
β_q(TJB) = κ√6            completion.py silently dropped this factor)

β_q(TJB)/β_d(TJB) = κ√6/(2κ) = √6/2   -- κ CANCELS EXACTLY
```

This resolves the Round-1 gap precisely, rather than leaving it open:
`"β_d=2"` on its own was imprecise notation (missing a factor of `κ`, an
undetermined normalization of this project's own two-point-charge
model's effective coupling) — but the **ratio**, which is what §3
actually compares, is unconditionally `κ`-independent. This also
explains, retroactively, why the earlier uniform-lever-arm-rescaling
check (`d_A=α·r_A`) found the ratio `α`-invariant: `α` and `κ` enter the
construction the same way (both are overall normalizations of the
"effective charge" `q_A`), and both must cancel in a ratio built from
one power of each tier.

**What remains genuinely unchecked** (real, not resolved by this round):
angular/orientation-averaging factors and `κ_A≠κ_P` (asymmetric coupling
between the two nodes) — a skeptic-named concern this file still does
not address. These are structurally different from the `α`/`κ`
normalization (which is proven to cancel); whether they also cancel in
the ratio is not established here.

## 3. The ratio comparison — real under stated assumptions, not a settled mismatch

`[VERIFIED-file, two_charge_completion.py line 171]`: this project's own
derivation gives `β_d(TJB)=2κ, β_q(TJB)=κ√6` **not as a fit to any
data** — as a pure combinatorial consequence of Taylor-expanding an
exact two-point-charge (mirror-symmetric dipole) Coulomb interaction to
second order in the lever-arm/radius ratio, with `κ` an undetermined
overall normalization (§2.1) that **cancels exactly** in the ratio. The
ratio, not the individual values, is the construction's genuinely
falsifiable, unit/normalization-independent output:

```
our derived ratio:        β_q/β_d = √6/2       = 1.2247
v82's fitted analog:      √β2/β1  = √(7.7e17)/1.4e10 = 0.0627
                                    (β1≈1.4×10¹⁰, β2≈7.7×10¹⁷, Table II
                                     best-fit row, per docs/149)
discrepancy factor:                                    19.5×
```

`[VERIFIED-sympy+python]`, `P159` script §3, arithmetic only. **Both
Round-1 gaps are now closed**: (a) `β1↔β_d`, `β2↔β_q²` is confirmed by
two genuinely independent primary sources (v6's own Eqs. 14-20, v82's
own Eqs. 2-4 — §2); (b) `κ`'s exact role is now known (§2.1) — it enters
`β_d`, `β_q` identically and cancels in their ratio. The `19.5×` gap
stands as a real, well-grounded discrepancy in this specific
falsifiable ratio, under the two_charge_completion.py's own stated
construction (mirror-symmetric two-point-charge, uniform lever-arm
normalization — §5 below lists what is NOT ruled out by this).

## 4. Important caveat: v6's own β_d, β_q are not a stable anchor either — `[VERIFIED-grep, v6 lines 2215-2516]`

v6's own text reveals its `β_d`, `β_q` were **not** independently derived
by TJB either — they were parameters an AI service was asked to fit
(the same Table A1 exercise already established as `[VERIFIED-SOURCE]`
AI-output, not a MULTING calculation, per this project's own
`table_a1_is_ai_output.md`):

> "Try to choose positive values for βd and βq that minimize the
> standard-deviations..." (v6 line 2314) ... "Disagreements regarding
> values, that the services suggested, for βd and βq were noticeable."
> (v6 line 2516)

One AI service reportedly chose `β_d=4.5, β_q=18.0` (project memory,
`table_a1_is_ai_output.md`) — wildly different from this project's own
`β_d=2, β_q=√6`, and from v82's fitted `β1≈1.4×10¹⁰, β2≈7.7×10¹⁷`, and
presumably from whatever other services reported ("noticeable
disagreements"). **v6 supplies no trustworthy numeric anchor at all** —
only this project's own two-point-charge derivation is a genuinely
theory-motivated (not fit, not AI-guessed) number.

## 5. What a 19.5× ratio mismatch does and does not mean

**Does not mean**: v82's fit is wrong, or that MULTING's physical
dipole/quadrupole mechanism is impossible (`NO_AUTHOR_ERROR`). Several
structurally different explanations remain open, none tested here:

1. The real physical mechanism sourcing MULTING's dipole/quadrupole terms
   may not be the simple mirror-symmetric two-point-charge picture this
   project's own construction assumes — `two_charge_completion.py`'s own
   header already flags this as one candidate construction among several
   (it was chosen because it is local and ghost-free, not because it was
   independently confirmed as the unique correct mechanism).
2. `two_charge_completion.py`'s own identification `d_A=r_A` (the
   two-point-charge's own separation set equal to the node's physical
   radius) is a **specific modeling choice**, not something v82's own fit
   is required to respect — a fit is free to land anywhere in the
   `(β1,β2)` plane regardless of whether that point matches a
   point-charge-geometry prediction.
3. `FINDING_P133`'s own identifiability result (this project's separate,
   already-established finding) showed `(A,g,κ)` are not jointly
   identifiable from current observational handles — an analogous
   degeneracy in `(β1,β2,H0,anchor)` space is plausible and would mean
   the specific fitted point is not uniquely meaningful to begin with;
   not checked here (this is `docs/150` §6 item 1, still open).

**Does mean**: this project's own first-principles, non-fit prediction
for the dipole-to-quadrupole coupling ratio does not land near where
v82's own best fit to real `H(z)` data landed — a real, precise,
falsifiable tension, now grounded in two independent primary sources
(v6's own raw equations, v82's own equations — §2) with the construction's
only free normalization (`κ`) shown to cancel exactly (§2.1). This is the
strongest-supported form the finding has reached this session.

## What this file does NOT establish

1. Not a claim about v82's own theory being wrong (`NO_AUTHOR_ERROR`) —
   only that this project's own two-point-charge construction's
   prediction and v82's own fit disagree on this specific ratio.
2. Does not check whether `β1`, `β2` are jointly identifiable in v82's
   own fit (analogous to `FINDING_P133` for this project's own `(A,g,κ)`)
   — named in §5 as a real possibility, not tested.
3. **Does not check angular/orientation-averaging factors or `κ_A≠κ_P`
   asymmetry** (skeptic-named, §2.1) — unlike the `κ`/`α` normalization
   (proven to cancel in the ratio, §2.1), these are structurally
   different degrees of freedom whose effect on the ratio is not derived
   here. A genuinely different, currently-unknown-magnitude source of
   the `19.5×` gap.
4. Does not address the RAW magnitude of `β1` (`~10¹⁰`) on its own terms
   — only the ratio, which is the part guaranteed unit-independent. Why
   `β1` itself is so large (a genuine physical coupling, vs. an artifact
   of v82's own practical unit choices for `k_A` in keV, `m_A` in `M_☉`,
   `r_A` in Mpc not being carried through with fully consistent `G`, `c`
   values) cannot be determined from the manuscript alone — would require
   the Zenodo supplementary code, not checked here.
5. Does not re-examine whether `two_charge_completion.py`'s own
   mirror-symmetric-orientation requirement (needed to reproduce
   MULTING's sign rule at all, per that file's own derivation) is itself
   the unique construction consistent with v82's specific fitted values —
   only that its magnitude prediction, taken at face value, doesn't match.
6. Closes `docs/149` §2's flagged-but-unchecked note. Does **not** close
   `docs/150` §6 item 4 (the `A·g²`/v82-parameter connection) — a related
   but distinct question this file does not attempt.
