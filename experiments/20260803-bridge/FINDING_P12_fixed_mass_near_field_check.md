# P12 — the fixed-mass extension survives the near field, and P1's own kernel invariant needed a correction to say so precisely

**Date:** 2026-08-12 · closes the specific open item `FINDING_P11` named and
did not check: *"whether such a construction is even possible while
respecting the `A₃, A₄` ladder structure that fixed `β_d=2, β_q=√6`."* User
instruction: *"построй fixed-mass расширение и проверь ближнюю зону"* (build
the fixed-mass extension and check the near field).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P12_fixed_mass_near_field_check.py`, ruff clean. Reuses P1's own
`tiers_from_kernel(K)` function (already general in the exchange kernel,
previously applied only to the massless case and to the bare kernel
invariant `Λ(r)`) — applied here directly to the Yukawa kernel to get the
*actual* physical `U_mm, U_km, U_kk`, not just `Λ`. Three positive controls
(massless-kernel reproduction of P1's own printed forms; `μ=0` limit of the
Yukawa tiers reproducing the same forms; internal series-order asserts) all
pass before anything new is trusted.

**[Skeptic review, same day.] First finding in the P9→P12 sequence to
survive context-blind review with both verdicts CONFIRMED-REAL — no
retraction, no falsified claim.** Skeptic independently hand-re-derived
every formula, series coefficient, and numeric value through `O(x⁴)` and
found no algebra or numerical error. Two minor, non-retracting refinements
applied below (§4, §7): the "Helmholtz Green's function" framing was
overstated (the standard multipole expansion gives `O(x²)` uniformly for
every `ℓ`; the "each tier more protected" pattern found here is a real but
construction-specific fact, not a general Helmholtz-theory statement), and
one item was added to "does NOT establish" (laboratory/solar-system
fifth-force constraints — flagged by the skeptic as a real gap in the
enumeration, though not physically substantive given `μ~H₀/c`'s
Hubble-scale Compton wavelength). See "Skeptic verdict" section at the end
for full detail.

---

## 1. The question

P11 found that a fixed-mass Yukawa mediator (`μ~H₀/c`) breaks the exact
double-layer cancellation with no assumed asymmetry — a genuine candidate
mechanism for the k-sector's cosmological signal. But P11 also found that
this collides, on its face, with P1's own proof that `β_q/β_d=√6/2` requires
an *exactly* massless mediator. The skeptic review of P11 resolved the
tension qualitatively (`μ~H₀/c` gives `μr~10⁻⁴` at cluster scale, negligible)
but did not check it quantitatively against the actual near-field
construction — this finding does that check directly.

## 2. The method — reuse, not rebuild

`two_field_action_closure.py` (P1) already has a function,
`tiers_from_kernel(K)`, that derives `U_mm, U_km, U_kk` for *any* exchange
kernel `K(s)` from the same mirror-symmetric point-charge construction used
throughout this track. P1 itself only ever called it with `K=1/s` (massless)
and, separately, computed the bare kernel invariant `Λ(r)=K'''(r)K'(r)/K''(r)²`
for a Yukawa kernel — but never applied `tiers_from_kernel` itself to the
Yukawa case. This finding does exactly that: `tiers_from_kernel(exp(-μs)/s)`.

**Positive control**, checked first: `tiers_from_kernel(1/s)` reproduces
P1's own printed `U_mm=m_Am_B/r`, `U_km=(d_Am_Bq_A+d_Bm_Aq_B)/r²`,
`U_kk=2d_Ad_Bq_Aq_B/r³` exactly (asserted, not eyeballed).

## 3. Exact Yukawa tiers

```
U_mm = m_A m_B exp(-μr)/r
U_km = (μr+1)(d_A m_B q_A + d_B m_A q_B) exp(-μr)/r²
U_kk = d_A d_B q_A q_B (μ²r²+2μr+2) exp(-μr)/r³
```

All three reduce exactly to the `μ=0` control forms (asserted). Taking
`F=-dU/dr` gives the forces `F_mm, F_km, F_kk` (full closed forms in the
script) — the sign/algebra structure that made MULTING's alternating
attract/repel/attract rule a *theorem* (P1 §2) is untouched, because that
result comes from the charge-combination algebra `(m_A-κk_A)(m_P-κk_P)`, not
from the specific functional form of `K(s)`.

## 4. Does the near-field power-law ladder survive? Yes — and each higher multipole is *more* protected

Stripping each tier's leading power law (`F·r²`, `F·r³`, `F·r⁴`) and
series-expanding in `x=μr`:

```
F_mm·r² = m_Am_B·(1 − x²/2 + x³/3 − x⁴/8 + …)     leading correction O(x²)
F_km·r³ = (…)·(2 − x³/3 + x⁴/4 − …)                leading correction O(x³)
F_kk·r⁴ = (…)·(6 − x⁴/4 + x⁵/5 − …)                leading correction O(x⁴)
```

Every tier's leading `1/r²`, `1/r³`, `1/r⁴` power law survives *exactly* at
`x=0`, and — a clean pattern, confirmed by an independent hand re-derivation
in the skeptic review — **each successive multipole's leading correction
appears one power of `x` later than the previous one**: monopole at `O(x²)`,
dipole at `O(x³)`, quadrupole at `O(x⁴)`.

**[Corrected after skeptic review]** This is *not*, as an earlier version of
this file claimed, a general property of "a Helmholtz Green's function's
multipole expansion" — the standard spherical-harmonic (modified spherical
Bessel function) expansion of the Yukawa Green's function gives a leading
correction of `O(x²)` **uniformly for every multipole order `ℓ`**, not
progressively later for higher `ℓ`. The pattern found here is real and
correctly derived, but is a feature specific to *this* point-charge,
derivative-of-`K` construction (each tier's force is built from
`K^{(n)}(r)`, and for `K=exp(-μr)/r` each derivative order happens to carry
a truncated-exponential structure that produces exactly this staggering) —
not a general fact about screened mediators that would carry over
automatically to a different multipole realization (e.g. an extended
charge distribution rather than idealized point pairs).

**Numeric evaluation at `μr=10⁻⁴`** (cluster scale, `μ~H₀/c` — P11's own
physically-motivated scale):

```
monopole   |ΔF_mm/F_mm|  ~ 5.0e-09
dipole     |ΔF_km/F_km|  ~ 1.67e-13
quadrupole |ΔF_kk/F_kk|  ~ 4.17e-18
```

**All utterly negligible.** The dipole and quadrupole coefficients that fix
`β_d=2, β_q=√6` are unaffected at cluster scale to a precision far beyond
any conceivable observational test — the dipole tier specifically (the one
`β_d` is derived from) is protected 5 orders of magnitude *more* than the
`Λ`-based order-of-magnitude estimate P11's skeptic review used
(`(μr)²~10⁻⁸`), because the actual fractional correction is `O(x³)`, not
`O(x²)` — see §5.

## 5. A genuine refinement to P1's own claim: `Λ(r)` is not literally `ℓ_q²/ℓ_d²` for a general kernel

P1's own text states: *"the kernel part of `ℓ_q²/ℓ_d²` is the invariant
`Λ(r)=K'''(r)K'(r)/K''(r)²`."* This finding checked that literally, by
computing the *actual* `ℓ_q²/ℓ_d²` ratio from the real dipole/quadrupole
charge construction (not the bare kernel alone) and comparing series:

```
Λ(x)/Λ(0)                    = 1 − x²/2 + 2x³/3 − 5x⁴/12 + …    (leading O(x²))
[ℓ_q²/ℓ_d²](x)/[ℓ_q²/ℓ_d²](0) = 1 + x³/3 − 7x⁴/24 + …             (leading O(x³))
```

**These are different series — `Λ(r)` is NOT the same quantity as the
actual `ℓ_q²/ℓ_d²` ratio for a general kernel.** Asserted in the script (not
just observed): `Λ`'s `O(x²)` coefficient is nonzero, the true ratio's
`O(x²)` coefficient is exactly zero. Tracing why: the actual ratio scales as
`K'''(r)/[K''(r)²·r²]` (from how the dipole/quadrupole terms arise in the
point-charge expansion), which equals `Λ(r)=K'''(r)K'(r)/K''(r)²` **only
when `K'(r)=-1/r²` exactly** — true for the massless kernel `K=1/s`
specifically (`K'=-1/s²`), not for Yukawa (`K'(r)=-exp(-μr)(μr+1)/r² ≠ -1/r²`
for `μ≠0`). So P1's equivalence between `Λ` and `ℓ_q²/ℓ_d²` — asserted as *"the kernel
**part of** `ℓ_q²/ℓ_d²` is the invariant `Λ(r)`"* and then operationally
applied to a Yukawa kernel a few lines later, treating `Λ`'s `r`-dependence
as the physically meaningful sensitivity to mediator mass — is exact only
for the massless case; **[skeptic review]** the "part of" phrasing admits a
charitable reading where P1 only ever intended this for `K=1/s`, but P1's
own next section computes and uses `Λ(r)` for Yukawa specifically, which is
the stricter, kernel-general reading this finding tests and refines — so
this is a warranted correction of how `Λ` was actually *used*, not an
attack on a claim P1 never made. This does not change any prior verdict on
the massless case (P1's `β_q/β_d=√6/2` result is untouched), and the
correction, if anything, makes the near-field survival argument **stronger,
not weaker** — the ACTUAL departure from `β_q/β_d=√6/2` under a small
mediator mass is smaller than `Λ` alone would suggest, `O(x³)` fractional
rather than `O(x²)`.

## 6. Bottom line

**The specific open item `FINDING_P11` flagged is closed:** a fixed-mass
`μ~H₀/c` extension of P1's action is self-consistent with the near-field
derivation of `β_d=2, β_q=√6` to a precision (`~10⁻¹³` fractional at the
dipole tier, at cluster scale) that no observation could ever probe. This
does not, by itself, establish that `μ~H₀/c` is the *correct* physical value
(that remains an assumption, same status as P9's `ε` and P10's absence
finding), nor does it construct a full covariant action with this mass term
(only the flat-space, point-charge kernel substitution was checked, matching
this project's existing scope limits per `MODEL_SPEC_AUDIT.md` row
"UNKNOWN, precondition missing"). But the specific self-consistency worry
P11 raised and left open — "does this break the near field?" — has a
computed, not asserted, answer: **no, by a wide margin.**

## What this does NOT establish

1. **That `μ~H₀/c` is correct**, or gives an observable cosmological
   magnitude — still an assumed scale, same epistemic status as P9's `ε`.
2. **A covariant (curved-spacetime) version of this mass term.** Only the
   flat-space kernel substitution was checked, consistent with
   `MODEL_SPEC_AUDIT.md`'s own already-flagged precondition gap.
3. **That the cosmological-scale (`μr~1`) behavior itself is fully
   understood** — this finding only checks the *opposite* limit (`μr≪1`,
   near field); P11's own cosmological-scale result stands independently.
4. **A resolution of whether the k-sector's cosmological signal is real.**
   This removes one specific objection (near-field self-consistency) to one
   specific candidate mechanism (P11's fixed-mass Yukawa) — it does not
   establish that mechanism is correct, only that it is not immediately
   self-contradictory.
5. **[Added after skeptic review]** Laboratory / solar-system fifth-force
   constraints on the ordinary `g·m_i·φ` monopole coupling, once `φ` carries
   a mass `μ`. Not checked here — flagged by the skeptic as a genuine gap in
   this enumeration. Not expected to be physically substantive: `μ~H₀/c`
   gives a Compton wavelength on the order of the Hubble radius, so the
   screening this mass introduces is negligible at any sub-Hubble scale any
   laboratory or solar-system test could probe — but this is an expectation,
   not a checked result, and belongs in the list of open items regardless.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   (P1's action, extended), not a claim about TJB's own unpublished theory.

## Skeptic verdict (context-blind, 2026-08-12)

Two separate verdicts, per Step 8a / Context Asymmetry (skeptic given only
this file, the script, `two_field_action_closure.py`, and
`FINDING_P11_yukawa_screening_breaks_double_layer.md` — no session history).
**First finding in the P9→P12 sequence with both verdicts CONFIRMED-REAL —
no retraction.**

- **Mathematical/numerical result** (exact Yukawa tiers; series-expansion
  leading-correction orders; numeric fractional corrections at cluster
  scale; the three positive-control asserts): **CONFIRMED-REAL.** The
  skeptic independently hand-re-derived `K(r), K'(r), K''(r), K'''(r)` for
  the Yukawa kernel, the resulting `U_km, U_kk` from the point-charge
  construction, every series coefficient through `O(x⁴)`, and every printed
  numeric value — found no algebra or arithmetic error anywhere. Confirmed
  the `ratio_x2_coeff == 0` assert is a genuine, non-tautological
  discriminator (it would fail if the "actual ratio" literally equaled
  `Λ`). One overstatement caught and corrected in §4 above: the "Helmholtz
  Green's function multipole expansion" framing implied a general fact
  about screened mediators; the skeptic showed the standard modified-
  spherical-Bessel expansion actually gives `O(x²)` uniformly for every
  multipole order, so the staggered-order pattern found here is real but
  specific to this point-charge, derivative-of-`K` construction.
- **`Λ(r) ≠` actual `ℓ_q²/ℓ_d²` ratio, framed as "a genuine refinement to
  P1's own claim":** **CONFIRMED-REAL**, with a scope-of-refinement note
  incorporated into §5 above. The technical distinction (`equality holds
  iff K'(r)·r²=-1`) is exact and correctly explained. P1's own "part of"
  hedge admits a charitable reading limited to `K=1/s`, but P1's own next
  section *operationally applies* `Λ(r)` to the Yukawa kernel as the
  physically meaningful sensitivity — the stricter reading this finding
  tests — so the refinement is warranted against how `Λ` was actually used,
  not a strawman. The skeptic also noted explicitly: this correction makes
  the near-field survival argument *stronger*, not weaker.

A genuine gap the skeptic found in the enumeration (not a math error):
laboratory/solar-system fifth-force constraints on the massive `φ`'s
ordinary monopole coupling were not listed among the open items — added as
item 5 in "What this does NOT establish" above. Assessed by the skeptic as
not physically substantive (`μ~H₀/c`'s Hubble-scale Compton wavelength makes
any sub-Hubble-scale screening effect negligible) but a real omission from
the list regardless.

## Reproduction

```bash
python experiments/20260803-bridge/P12_fixed_mass_near_field_check.py
```

Three internal asserts (massless-kernel control; `μ=0` limit of the Yukawa
tiers; `Λ` vs. actual-ratio series-order distinction) must all pass before
the script proceeds — if any fails, the method itself is broken and nothing
downstream should be trusted.
