# P22 — Archidiacono's β verified against the primary source; maps onto A·g², but a real target-population gap surfaces

**Date:** 2026-08-13
**Origin:** P21 derived `A·g²=4π·ΔG` (`A` the missing normalization constant,
`g` the monopole coupling, `ΔG` the small fifth-force contribution to
Newton's `G`) and named Archidiacono et al.'s external `β` bound on a
scalar fifth force as the natural second equation — but explicitly did
**not** attempt to verify Archidiacono's own definition of `β` against the
actual paper, flagging that as the concrete next step. This finding does
that verification.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P22_archidiacono_beta_mapping.py`

**[CORRECTED after skeptic review, same day.]** The skeptic subagent lacked
WebFetch in its own context and could not independently re-fetch the source
— but still caught a real error: §1 originally explained the absence of
DESI data as "v4 predates DESI DR2," which is false (v4 is dated Nov 2025,
well after DESI DR2). Re-verified directly (own WebFetch, not
delegated): the paper's own version changelog shows v4's only change was
an unrelated technical fix (Sec. 4.2.1 analytic coefficients) — the
dataset was never updated with DESI across any version, for reasons the
changelog doesn't state. Corrected below. The numeric headline
~~`A·g²≲1.05×10⁻¹⁰`~~ was downgraded from "conditional bound" to "soft
ceiling" — see §5 and the Skeptic Verdict section for why. ~~Structural
algebra (`A·g²=16π²·β·G_N`) is unaffected and remains CONFIRMED-REAL.~~

**[CORRECTED AGAIN, same day — a real, user-flagged `4π` error in the
structural algebra itself, independently re-verified before accepting.]**
A collaborator flagged that §2's identification `ΔG≡G_s` double-counts a
`4π` factor: the paper's own text states directly, *"at distances
r≪m_φ⁻¹ the long range force is equivalent to a shift in Newton's
constant, G_N→G_N(1+β)"* — meaning `β` **is** `ΔG/G_N` directly, with no
`G_s` in that chain at all. Separately, the paper describes `G_s` itself as
*"a dimensionful constant analogous to G_N"* — i.e. `G_s` sits at the same
un-normalized level as this project's own `A·g²` (both are `4π` times the
actual `ΔG`), not at the level of `ΔG` itself. Both facts were re-verified
via a fresh, targeted WebFetch before accepting the correction (not taken
on the collaborator's word alone, per this project's own no-memory /
independent-re-verification discipline). Correct identification:
`A·g²≡G_s`, **not** `ΔG≡G_s`. This gives `A·g²=4π·β·G_N`, not
`16π²·β·G_N` — the headline number is corrected to `A·g²≲8.39×10⁻¹²`
(SI), **tighter** by exactly `4π≈12.57×`, not looser. The qualitative
verdict (soft ceiling on the *product* `A·g²`, not on `A` or `g`
individually) is unchanged. See the new §2 and the User-Flagged Correction
section for the full derivation, including a two-independent-route
cross-check that serves as the positive control for this fix.

## 1. Source verification

Fetched directly (WebFetch, this session, cross-checked across three
independent fetches of `arxiv.org/abs/2204.08484` and
`arxiv.org/html/2204.08484`): Archidiacono, Castorina, Redigolo, Salvioni,
*"Unveiling dark fifth forces with linear cosmology,"* published JCAP 10
(2022) 074 (arXiv v4, Nov 2025) — confirmed as the same paper P13a cited.

Verified quotes (not paraphrased):

- **Eq 2.10:** `β ≡ G_s/(4π·G_N)`.
- **Eq 2.17:** `G_s = g_D²/m_χ²` (their specific fermionic-mediator UV
  completion).
- **Eqs 2.15–2.16:** coupling terms `−g_D·φ·χ̄χ` (fermionic DM) and
  `−g_D·m_χ·φ·χ²` (scalar DM) — `φ` couples **only** to the dark-matter
  field `χ`.
- **Confirmed twice, independently:** *"baryons are completely unaffected by
  the scalar fifth force"* — zero baryon coupling in this model, not merely
  a small one.
- **Abstract headline bound:** *"less than a percent of gravity"* →
  `β≲0.01`, from Planck + BAO, for `m_φ≲H₀` — the same long-range regime
  this project's own `μ~H₀/c` mechanism (P11) lives in. **[Corrected]** the
  dataset never incorporates DESI across any of the paper's four arXiv
  versions (v1 2022 → v4 Nov 2025); the changelog shows v4's only change
  was an unrelated technical fix, not a data update — no claim is made here
  about *why* DESI was never added.
- **[Added after skeptic review]** The abstract's own final sentence
  separately names *"the interplay between our constraints and searches for
  violations of the Equivalence Principle in the visible sector"* — i.e.,
  the paper itself treats a DM-only bound and a visible-sector (universal)
  fifth-force bound as distinct constraint channels, independently
  confirming §3's target-population caveat below is not merely this
  project's own speculation.
- **Not independently confirmed at higher precision:** the tighter
  `β<0.0054` figure P13a originally cited. Section 5's precise tables were
  not accessible this session (PDF mirror returned HTTP 403; the HTML
  excerpt tool could not surface table values). Flagged as an open
  precision gap — the `0.01` figure used below is the number this session
  actually verified from primary text, not the more precise one.

## 2. The mapping (sympy-verified, two independent routes)

**[CORRECTED — see banner above; this section replaces the original,
which made the `ΔG≡G_s` identification directly and is superseded, not
merely edited, given how load-bearing the error was.]**

`Archidiacono: β = G_s/(4π·G_N)  ⟹  G_s = 4π·β·G_N`

`This project's own P21-corrected force law: F_MULT(r) = A·c_G·g²·m₁m₂/r²
= (A·g²/4π)·m₁m₂/r², defining ΔG via F_MULT(r) ≡ ΔG·m₁m₂/r²:  ΔG = A·g²/4π`

**Route 1 — direct short-distance statement (the safer route: no
dependence on `G_s`'s own `g_D`/`m_χ` normalization details, which this
project has not independently re-derived).** The paper's own text:

> "at distances r≪m_φ⁻¹ the long range force is equivalent to a shift in
> Newton's constant, G_N→G_N(1+β)"

This gives `ΔG_Archidiacono = β·G_N` **directly**, bypassing `G_s`
entirely. Identifying `ΔG ≡ ΔG_Archidiacono` (both are the same *type* of
quantity — an additive fractional shift to the effective Newton's constant
between two point masses at short range — though still an assumption that
MULTING's `g`-mediated `ΔG` and Archidiacono's DM-only `ΔG` are comparable
in *kind*, not just *type*; see §3):

```
A·g² = 4π·ΔG = 4π·β·G_N
```

**Route 2 — structural identification `A·g²≡G_s`** (corrected from the
original, wrong `ΔG≡G_s`). The paper's own text:

> "G_s is a dimensionful constant analogous to G_N"

`G_s` sits at the *same* un-normalized level as this project's own `A·g²`
— both are "`4π` times the actual `ΔG`" (compare: this project has
`ΔG=(A·g²)/4π`; Archidiacono has, from Eq 2.10, `ΔG=G_s/4π`) — not at the
level of `ΔG` itself. Identifying `A·g² ≡ G_s`:

```
A·g² = G_s = 4π·β·G_N
```

**Cross-check (the positive control for this correction, sympy-verified):**
Routes 1 and 2 use two *independently*-quoted facts from the paper (the
`G_s` definition, and the separate short-distance statement) and **agree
exactly** — confirming Archidiacono's own two stated facts are mutually
consistent, and that this agreement is not assumed but derived. **Not**
independently re-derived here: `G_s=g_D²/m_χ²` (Eq 2.17) from first
principles — this requires understanding the paper's specific
fermionic-mediator non-relativistic field normalization, and attempting it
risked introducing a *different* error; Route 1 deliberately avoids this
dependency, which is why it is presented as the safer of the two.

```
A·g² = 4π·β·G_N        (NOT 16π²·β·G_N)
```

Using the independently-verified `β≲0.01` and `G_N=6.6743×10⁻¹¹` (SI, same
constant already used in `P17_kappa_bounds_consistency_check.py`):

```
A·g² ≲ 8.39×10⁻¹²  (SI units, m³kg⁻¹s⁻²)
```

**Tighter than the original (wrong) figure by exactly `4π≈12.57×`, not
looser.** The qualitative verdict — soft ceiling on the *product* `A·g²`,
not a bound on `A` or `g` individually — is unchanged; only the number
moves.

## 3. The identification `ΔG≡G_s` is an assumption, not a free equivalence

Both quantities are *defined* the same way, but they are not the same
*measurement*. This is the central caveat of this finding, sharper than
anything P13a established:

- **Archidiacono's `φ` couples only to dark matter — zero baryon coupling,
  stated explicitly, twice confirmed.** MULTING's `g·mᵢ·φ` term (P1's own
  action) couples to a body's mass `mᵢ` generically, with no restriction to
  a dark-matter-only component anywhere in the cited files.
- Using `β≲0.01` as a stand-in for MULTING's `g` therefore requires an
  **additional, unverified assumption**: that a hypothetically *universal*
  fifth force (coupling to baryons too, as MULTING's `g` appears to) would
  be constrained *at least as tightly* as Archidiacono's DM-only coupling.
  This is often true in practice (universal fifth forces face additional,
  typically *stronger* equivalence-principle and laboratory bounds that a
  DM-only coupling entirely evades) but is **not the same bound**, and this
  finding does not verify it either way.
- This is a genuinely new, independently-sourced sharpening of P13a's own
  §2, which named the mismatch as "independent coupling constants" but did
  not have direct textual confirmation that the target *populations* of
  matter differ this starkly (zero vs. generic coupling, not just
  independent coefficients on the same population).
- **[Added after skeptic review]** Two further subtleties, not previously
  flagged: (a) Archidiacono's `G_s=g_D²/m_χ²` is defined for the force
  between two *identical dark-matter particles* of mass `m_χ`; ~~this
  finding's identification `ΔG≡G_s`~~ **[corrected — now `A·g²≡G_s`, see
  §2]** treats both as "the coefficient of an `m₁m₂/r²` force in Newton's
  convention" without independently checking that `g_D²/m_χ²` reduces to
  that same form for *generic*, non-identical masses — plausible but not
  verified here; this subtlety is unaffected by the `4π`-factor correction
  and remains open. (b) P21's own S2 skeptic verdict already noted `A`'s
  placement (coupling vs. kinetic term) is a convention, not a physical
  fact; this identification inherits that convention-dependence without
  saying so.
- **[Added after skeptic review]** "Often true in practice" (below,
  original wording) understated the likely gap: for a long-range
  (`m_φ≲H₀`) scalar coupled *universally*, equivalence-principle tests
  (MICROSCOPE, atomic clocks, lunar laser ranging) are, on general grounds,
  expected to constrain far more tightly than a dark-matter-only bound like
  Archidiacono's — plausibly by several orders of magnitude, though this
  finding does not have a verified precise factor (Section 6's exact
  numbers were not accessible this session). The paper's own abstract
  (quoted in §1) independently confirms these are treated as separate
  constraint channels, not that one substitutes cleanly for the other.

## 4. What this does NOT establish

1. **A numeric value for `A` or `g` individually.** Only their *product*
   `A·g²` is conditionally bounded — `Ω_φ` (P14, built from `κ`, not `g`)
   is **not** thereby fixed; extracting `A` alone requires an independent
   estimate of `g`.
2. **That Archidiacono's `β` bound legitimately applies to MULTING's `g`.**
   §3's identification is stated as an assumption, not verified — if
   MULTING's `g` is meant to be a genuinely universal (baryon+DM) coupling,
   this bound is a plausible but unconfirmed proxy, not a direct
   measurement of the same quantity.
3. **The precise `β<0.0054` figure.** Only the independently-verified
   `β≲0.01` order-of-magnitude figure is used; if the tighter number is
   later confirmed, the bound above tightens by roughly a factor of ~2, not
   an order of magnitude — doesn't change the qualitative picture.
4. **[Added after skeptic review; number corrected again, see banner and
   User-Flagged Correction section] A precise numeric bound, full stop.**
   `A·g²≲8.39×10⁻¹²` is a **soft ceiling**, not a precision result — two
   stacking, unresolved uncertainties both point the same direction: (a)
   `β`'s own defining equation was read via WebFetch's small-model
   summarizer, not the raw PDF (convergent across several independent
   fetches, some evidence against pure hallucination, but not
   independently PDF-verified); (b) §3's target-population gap means the
   *true* bound, if MULTING's `g` is universal, is plausibly many orders of
   magnitude tighter than the number shown — see P23, P28, P29 for
   independent, further sharpening of this same caveat from different
   angles. Do not cite `8.39×10⁻¹²` as a precise result in any downstream
   finding. **Historical note:** the original skeptic review (sub-verdict
   A, below) had already flagged `4π`-type placement as a *live risk* in
   this derivation — prescient in kind, though the specific error that
   later materialized (a mis-identification in *this project's own*
   `ΔG≡G_s` step, not a mis-transcription of the paper's equation) was
   different from what was originally anticipated.
5. **Anything about the dipole sector's own remaining open questions**
   (P18, P19, P20) — this is entirely a monopole/gravity-sector question.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   and about what an external, independently-published paper's own text
   says, not a claim about any error in TJB's own theory.

## Reproduction

```bash
python experiments/20260803-bridge/P22_archidiacono_beta_mapping.py
```

Source verification is WebFetch-based (not locally reproducible from the
repo alone) — see §1 for exact URLs and quotes; a future session could
re-fetch `arxiv.org/abs/2204.08484` to re-confirm.

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `FINDING_P21_shared_phi_normalization_constraint.md`
(corrected version), and `FINDING_P13a_archidiacono_bound_scope.md` — no
session history. **Important limitation, disclosed by the skeptic itself:**
the subagent's own tool context lacked WebFetch/WebSearch, so it could
**not** independently re-fetch the primary source as instructed — sub-verdict
(A) below is therefore its own assessed *risk*, not an independent
re-verification. Five sub-verdicts, per Step 8a (not merged):

- **(A)** Primary-source quote accuracy: **NEEDS-REAL-DATA** (skeptic
  could not check directly). Flagged one concrete, checkable inconsistency:
  "v4 predates DESI DR2" — **found to be a genuine reasoning error** on
  independent re-verification (own WebFetch, this session): v4 (Nov 2025)
  postdates DESI DR2; the changelog shows v4 only fixed unrelated technical
  coefficients. *Applied: corrected throughout.* The core quoted formula
  (`β≡G_s/(4πG_N)`) itself was **not** shown to be wrong — convergent
  across multiple independent fetches, but still not independently
  PDF-verified; residual risk stated explicitly in §5.
- **(B)** Algebra `A·g²=16π²·β·G_N`: **CONFIRMED-REAL**, "given the stated
  inputs" — no error found; the skeptic notes correctly that this result
  fully inherits (A)'s residual uncertainty. **[Later found wrong by a
  different route — see the User-Flagged Correction section below.]** The
  skeptic verified the *algebra* was internally consistent given the
  `ΔG≡G_s` premise stated in Step 3 — it did not, and was not asked to,
  re-derive whether that premise itself was the *correct* identification.
  This sub-verdict is not contradicted (the algebra from that premise was
  indeed internally consistent) but the premise it was checked against has
  since been replaced.
- **(C)** `ΔG≡G_s` identification: **WEAKENED** — reasonable but missed two
  subtleties (identical-particle vs. generic-mass reduction of
  `G_s=g_D²/m_χ²`; inherited convention-arbitrariness from P21's own S2).
  *Applied: both added to §3.*
- **(D)** Target-population caveat: **WEAKENED** — direction right,
  magnitude understated ("often true" too soft), and the paper's own named
  Section 6 (visible-sector EP comparison) was not consulted. *Applied:
  independently confirmed via the abstract's own text (§1) that this is a
  distinct constraint channel per the paper itself, not just this
  project's inference; precise numeric factor still not obtained (Section
  6's exact figures were not accessible this session) — stated as an open
  gap, not invented.*
- **(E)** Numeric evaluation `A·g²≲1.05×10⁻¹⁰`: **WEAKENED** — arithmetic
  correct, but the headline number understated the uncertainty inherited
  from both (A) and (D). *Applied: downgraded from "conditional bound" to
  "soft ceiling" throughout §4 and the script's VERDICT block; explicit
  instruction added not to cite the number as precise.*

**Not a core-predicate-false kill (at the time).** The structural algebra
survived fully at this stage; what changed was how the numeric headline was
presented and one concrete factual correction (the DESI/v4 reasoning
error). Methodology note adopted from the skeptic: multiple WebFetch calls
to the same URL are not independent verification of each other — language
implying otherwise ("confirmed twice/three times independently") has been
avoided in the corrected sections above. **This assessment of the
*structural algebra* was later overturned — see below.**

## User-flagged correction (`4π` error), 2026-08-13 — same day, third pass

**Source of this correction:** a human collaborator, working through the
paper's own equations directly, flagged that Step 3's `ΔG≡G_s`
identification double-counts a `4π` factor. This is **not** a
context-blind `Agent(skeptic)` finding — flagged here for accurate
attribution, per this project's own provenance discipline. Per
doubt-driven-development practice, the claim was **not** accepted on the
collaborator's authority alone: independently re-verified via a fresh,
targeted WebFetch of `arxiv.org/html/2204.08484` before building the
correction (see §2 above for the two quoted facts this rests on).

**The error, precisely:** the original Step 3 treated Archidiacono's `G_s`
as directly equal to `ΔG` — the *same* physical quantity as this project's
own fractional-shift `ΔG=A·g²/(4π)`. But the paper's own text shows `G_s`
sits *one 4π level higher* than `ΔG` (exactly as this project's own `A·g²`
sits one `4π` level higher than its own `ΔG`) — `G_s` is "a dimensionful
constant analogous to `G_N`," and separately, `β` (not `G_s`) is what
directly equals `ΔG/G_N` at short range. The original identification
effectively applied the `4π` conversion **twice**: once implicitly (by
setting `ΔG=G_s`, when `G_s` was already `4π` times too large to play that
role) and once explicitly (in the final `A·g²=4π·ΔG` step).

**Positive control applied (user-suggested):** rather than trust either
route alone, both of the paper's independently-quoted facts (the `G_s`
definition, Eq 2.10, and the separate short-distance `G_N→G_N(1+β)`
statement) were used to derive `A·g²` via two different paths — see §2,
Routes 1 and 2. They agree exactly (`sp.simplify` confirms zero
difference), which is the positive-control check for this correction: if
the paper's own two stated facts were mutually inconsistent, or if this
project's re-derivation had introduced a *new* error, the two routes would
not have matched.

**Response per Step 8a Response Matrix:** `FALSIFIED` — a genuine
core-mechanism error in the identification step, not a framing issue.
`FIXED` — §2 fully rewritten with both derivation routes and the
cross-check; §3 and §4 updated to reflect the corrected number; the
script's Step 3 renamed to Steps 3a/3b with the same two-route structure,
plus an explicit check that the new result does *not* match the old,
wrong `16π²` form. **Not a core-predicate-false kill of the finding as a
whole** — the target-population caveat (§3), the WebFetch-evidence-quality
caveat, and the "soft ceiling on the product, not on `A` or `g`
individually" verdict are all unchanged; only the numeric coefficient
moved, and it moved in the *tighter* direction (a stronger, more
constraining ceiling), not the looser one.

**Recommended next step for a future context-blind skeptic pass:**
independently re-verify Route 1's underlying quote (the `G_N→G_N(1+β)`
statement) against the raw paper source if raw-LaTeX access becomes
available — this correction still rests on WebFetch-mediated text, one
tier below a direct source read, per this finding's own §1 evidence-quality
caveat.
