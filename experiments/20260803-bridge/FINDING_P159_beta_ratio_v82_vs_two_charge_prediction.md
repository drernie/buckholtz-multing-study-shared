# FINDING P159 — β₁/β₂ (v82) vs. β_d/β_q (this project's own derivation):
# not a units mismatch, a ratio mismatch — and a category mismatch flagged
# in the process

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math (dimensional analysis + symbolic verification)
**Verdict (final, post-skeptic):** `[HYPOTHESIS]-LEVEL-TENSION-NOT-A-
CONFIRMED-MISMATCH; RATIO-IS-STILL-THE-RIGHT-KIND-OF-TEST-BUT-TWO-LOAD-
BEARING-GAPS-REMAIN-OPEN: (1) THE-TWO-"INDEPENDENT"-ROUTES-ARE-NOT-
INDEPENDENT — ROUTE-A-WAS-CONSTRUCTED-FROM-ROUTE-B, (2) κ'S-DIMENSION-
AND-VALUE-ARE-NEVER-PINNED-DOWN-ANYWHERE-IN-THIS-PROJECT, SO "β_d=2" IS
CONTINGENT-ON-AN-UNSTATED-CHOICE. THE-19.5×-RATIO-GAP-IS-REAL-GIVEN-
THOSE-TWO-ASSUMPTIONS-AND-ROBUST-TO-UNIFORM-LEVER-ARM-RESCALING
(VERIFIED), BUT-IS-NOT-A-SETTLED-FINDING.`
**Correction (2026-08-30, context-asymmetric skeptic-caught, two
independent points confirmed by direct re-reading of this project's own
files):** the original verdict claimed the structural correspondence
(`β1↔β_d`, `β2↔β_q²`) was "confirmed two independent ways" and presented
the `19.5×` ratio gap as "a genuine, unit-independent mismatch — not a
rounding-level disagreement." Both claims were overstated. §2 and §2.1
below correct them in place.
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

## 2. Structural correspondence — ONE route, not two (corrected)

**Original claim (retracted): "confirmed two independent ways."**
A dispatched skeptic pointed out that "Route A" (`scripts/
factorization_gate.py`) and "Route B" (v6's own defining equations)
might not be independent — and re-reading `factorization_gate.py`'s own
comment settles it `[VERIFIED-file, lines 38-39]`:

```
#   dipole    F_d ~ B/r^3,  B = (G beta_d/c^2)(k_i r_i m_j + k_j r_j m_i)   [r_dA=beta_d r_A]
#   quadrupole F_q ~ C/r^4, C = (G beta_q^2/c^4)(k_i r_i)(k_j r_j)          [r_qAB^2=beta_q^2 r_A r_P]
```

The bracketed citations `[r_dA=beta_d r_A]`, `[r_qAB^2=beta_q^2 r_A r_P]`
are v6's own defining relations (§below) — **this kernel was built BY
substituting v6's own relations into a generic dipole-moment force
template** (moment = charge × displacement, with `r_dA` as the
displacement). It is not independent corroboration; it is v6's own
relation, restated in kernel-matrix notation. The apparent "two routes"
were one route.

**v6's own defining equations** (`data/source_material/
buckholtz_preprints202511.0598.v6_pymupdf-clean.md`, lines 805-811,
`[VERIFIED-grep]`) remain the **sole** source for the linear/squared
split:

> "We posit... Eqs. (18) through (20). βd and βq are nonnegative...
> `rdA = βdrA`... `rdP = βdrP`... `|rqAB|² = (βq)²rArP`"

`β_d` is defined via a **linear** length relation (`r_dA=β_d·r_A`);
`β_q` via a **squared** one. The identification `β1 (v82) ↔ β_d`
(linear), `β2 (v82) ↔ β_q²` (squared) still stands — it is a correct
reading of v6's own equations — but rests on **one** source, not two, and
the earlier "confirmed independently" language is withdrawn.

## 2.1 A second, more serious open gap: κ's dimension and value are never pinned down

`two_charge_completion.py`'s own derivation carries an auxiliary
parameter `κ` throughout (introduced via `q_A = -κ·k_A/c²`, line 158),
and reads off `β_d=2, β_q=√6` from `u_A ≡ κ·k_A·r_A/(c²·m_A)` treated as
*already equal to* v6's own dimensionless quantity — i.e. implicitly
**`κ=1`** in whatever units make that true. `[VERIFIED-grep]`: `κ` is
never assigned a numerical value or an explicit dimension anywhere in
`two_charge_completion.py`, `docs/125`, or `docs/130` — it is used as a
free bookkeeping symbol and never resolved.

Whether `κ=1` is a harmless normalization (because it is genuinely
dimensionless and v6's own `u_A` is defined the same way) or a **hidden,
unstated length-scale choice** (if `κ` in fact carries dimension) cannot
be settled without v6's own explicit definition of `u_A`, which this
file has not located and re-verified independently. **`β_d=2, β_q=√6`
should therefore be read as contingent on this unresolved choice, not as
settled numbers ready for comparison against anything external.**

**What survives this gap, verified independently `[VERIFIED-sympy]`**:
the **ratio** `β_q/β_d` is invariant under the specific, one-parameter
generalization "lever arm `d_A = α·r_A`" for any `α` (not just `α=1`) —
```
β_d(α) = 2α,  β_q(α) = α√6  =>  β_q(α)/β_d(α) = √6/2, independent of α
```
— re-derived and confirmed here, not merely asserted by the skeptic.
This is a real, if partial, robustness result: at least *this* specific
degree of freedom (uniform lever-arm rescaling) cannot be the source of
the `19.5×` gap in §3. Other degrees of freedom the skeptic named
(angular/orientation-averaging factors, `κ_A≠κ_P` asymmetry) are **not**
checked here and could move the ratio by a comparable order of magnitude
— this file does not know by how much.

## 3. The ratio comparison — real under stated assumptions, not a settled mismatch

`[VERIFIED-file, two_charge_completion.py line 171]`: this project's own
derivation gives `β_d=2, β_q=√6` **not as a fit to any data** — as a pure
combinatorial consequence of Taylor-expanding an exact two-point-charge
(mirror-symmetric dipole) Coulomb interaction to second order in the
lever-arm/radius ratio, **contingent on the §2.1 caveat about `κ`**. The
file's own printed line: `"PREDICTION beta_q/beta_d = 1.2247"` — this
ratio is the construction's actual falsifiable output, not the raw
`β_d`, `β_q` values individually (which, per §2.1, may not even be
well-defined pure numbers independent of an implicit unit/scale choice).

```
our derived ratio:        β_q/β_d = √6/2       = 1.2247
v82's fitted analog:      √β2/β1  = √(7.7e17)/1.4e10 = 0.0627
                                    (β1≈1.4×10¹⁰, β2≈7.7×10¹⁷, Table II
                                     best-fit row, per docs/149)
discrepancy factor:                                    19.5×
```

`[VERIFIED-sympy+python]`, `P159` script §3, arithmetic only. **Given**
(a) `β1↔β_d`, `β2↔β_q²` (§2, resting on one source now, not two) and
(b) `κ` resolves to a value/dimension consistent with `β_d=2, β_q=√6`
being the intended comparison target (§2.1, unresolved) — this `19.5×`
gap is real and, per §2.1, robust to uniform lever-arm rescaling
specifically. It is **not**, contrary to the original draft, established
as "a genuine, unit-independent mismatch" outright — that language
presumed both (a) and (b) were settled, and only (a) is (partially).

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

**Does mean, at HYPOTHESIS confidence given §2/§2.1's open gaps**: this
project's own first-principles, non-fit prediction for the
dipole-to-quadrupole coupling ratio does not land near where v82's own
best fit to real `H(z)` data landed. This is a real, precise, falsifiable
number under the stated construction — but not yet a confirmed tension
between the frameworks, because the construction's own status (§2.1) is
itself unresolved.

## What this file does NOT establish

1. Not a claim about v82's own theory being wrong (`NO_AUTHOR_ERROR`) —
   only that this project's own two-point-charge construction's
   prediction and v82's own fit disagree on this specific ratio, under
   assumptions this file has not fully verified.
2. Does not check whether `β1`, `β2` are jointly identifiable in v82's
   own fit (analogous to `FINDING_P133` for this project's own `(A,g,κ)`)
   — named in §5 as a real possibility, not tested.
3. **Does not establish that Route A/B are independent** (§2, corrected)
   — only one source (v6's own `r_dA=β_d·r_A` relation) grounds the
   linear/squared correspondence; the "second route" was the first,
   restated.
4. **Does not pin down `κ`'s dimension or value** (§2.1) — `β_d=2,
   β_q=√6` are contingent numbers, not yet shown to be the unique,
   unit-independent output of the construction. Two concrete follow-ups
   named, neither attempted here: (a) locate v6's own explicit definition
   of its `u_A`-type dimensionless quantity and check whether `κ=1`
   follows from it or is an extra assumption; (b) redo §1's dimensional
   check on `κ` itself (not just on `β1`, `β2`) to settle whether it must
   carry a length-scale dimension.
3. Does not address the RAW magnitude of `β1` (`~10¹⁰`) on its own terms
   — only the ratio, which is the part guaranteed unit-independent. Why
   `β1` itself is so large (a genuine physical coupling, vs. an artifact
   of v82's own practical unit choices for `k_A` in keV, `m_A` in `M_☉`,
   `r_A` in Mpc not being carried through with fully consistent `G`, `c`
   values) cannot be determined from the manuscript alone — would require
   the Zenodo supplementary code, not checked here.
4. Does not re-examine whether `two_charge_completion.py`'s own
   mirror-symmetric-orientation requirement (needed to reproduce
   MULTING's sign rule at all, per that file's own derivation) is itself
   the unique construction consistent with v82's specific fitted values —
   only that its magnitude prediction, taken at face value, doesn't match.
5. Closes `docs/149` §2's flagged-but-unchecked note. Does **not** close
   `docs/150` §6 item 4 (the `A·g²`/v82-parameter connection) — a related
   but distinct question this file does not attempt.
