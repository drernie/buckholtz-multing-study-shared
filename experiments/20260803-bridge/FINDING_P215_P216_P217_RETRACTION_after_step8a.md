# RETRACTION — P215, P216 and P217 are ALL FALSIFIED

**Date:** 2026-09-07 (same day they were written, committed and pushed)
**Supersedes:** `FINDING_P215_periastron_survives_on_degenerate_energy.md`,
`FINDING_P216_v82_internal_scope_inconsistency.md`,
`FINDING_P217_beta_universality_axis_swapped_between_versions.md`
**Method:** three independent context-blind Step 8a skeptic passes, one per
finding, each given only its own artifact verbatim plus source paths.
**Every load-bearing citation below was re-read from source by me before
acceptance** (`audit-verification-gate.md`: their `[VERIFIED]` = my
`[INFERRED]`). Line numbers index
`buckholtz_preprints202511.0598.v6_pymupdf-clean.md` — the extraction whose
own header line 10 marks it **PREFERRED for grep/search** — and
`buckholtz_202608.0943v1.v82.md`.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## 0. Verdicts

| finding | verdict | what killed it |
|---|---|---|
| **P215** | **FALSIFIED** | v6 defines `k` as the excess over the **ground state**; a cold Fermi sea **is** the ground state, so `k_deg = 0`. Plus a factor-of-2 error this project had **already found a month earlier**. |
| **P216** | **FALSIFIED** | v82:1028 treats a node **as** an object. Hierarchy, not inconsistency. |
| **P217** | **FALSIFIED** | Both versions assert **both** properties. The registers are swapped, not the axes. |

---

## 1. P215 — the conclusion is INVERTED, not merely wrong

### 1.1 v6 subtracts the ground state, and a degenerate Fermi sea IS the ground state

**v6:652-654** `[VERIFIED-source]`:

> *"We use the symbol `E00,oA` to refer to the **ground-state energy**… the
> two-word term ground state refers to **a lowest-energy state with respect
> to the first-tier nonzero-mass sub-objects** of object-A."*

**v6:675** — what actually couples:

> *"…the internal kinetic energy of object-A (**as in `EoA − E00,oA`**)
> associate with gravitational push."*

**v6:660-661** — the author's own two examples of leaving the ground state:

> *"…it takes energy to **heat up or spin up**, from the state that
> associates with `E00,oA`…"*

A cold neutron star at `T = 0` **is in** its lowest-energy state: the filled
Fermi sea is the ground state of the neutron system. So `EoA = E00,oA`,
`k = 0`, `u_NS = 0`, and the bound does not exist at all.

Both of the author's examples — heat, spin — require **adding** energy.
Degeneracy requires adding nothing; it is there at zero temperature and zero
spin. That is exactly the property that places it on the **subtracted** side
of `EoA − E00,oA`.

**P215's central claim — *"the one internal energy the corpus actually
admits"* — is therefore backwards.** Degeneracy is the most confidently
**excluded** of the three candidates, not the least.

### 1.2 P215's §1 table is wrong in two of its three rows

| row | P215 said | what the source says |
|---|---|---|
| **rotational** | *"excluded by v6's own definition (linear motion, v6:640)"* | **WRONG.** v6:790: *"Suppose that `kA` associates **only with the rotation of a uniform ring of mass**"* — developed with a lever-arm estimate `rdA ≈ SA/(2 mA kA)^½`. v6:798 sets that aside **only for protoclusters and clusters**. For a neutron star, rotational is the **best**-supported reading, not an excluded one. |
| **degeneracy** | *"not addressed"* by either version | **WRONG.** v6 addresses it structurally at 652-675 (ground-state subtraction). v82 addresses it by definition at 207 — *"`k_A` is the thermal energy that associates with the **ICM** of node-A"* — with Sec. IVF devoted to why **thermal** rather than bulk. |

The same mis-enumeration appears in
`FINDING_P214_RETRACTION_after_step8a.md` §3 and is withdrawn there too.

### 1.3 A factor of 2 — found by this project on 2026-08-11, reproduced here

**v6:784, Eq. (15)** `[VERIFIED-source]`:

```
Fd = (G kA c−2 mP |rdA|/(r3)) + (G kP c−2 mA |rdP|/(r3))
```

with `rdA = βd rA`, `rdP = βd rP` (v6:807-810). Dividing by
`Fm = G mA mP/r²`:

```
ell_d = beta_d * [ (kA/(mA c^2)) rA + (kP/(mP c^2)) rP ] = beta_d (u_A + u_P)
```

**One `β_d`, two terms, no factor of 2.** The script asserts
`ell_d = 2 beta_d (u_A + u_B)` and divides by `2(u_a + u_b)`.

`FINDING_P7_k_definition_resolved_from_corpus.md:23` — **in this same
directory, written 2026-08-11** — already recorded it:

> *"a factor-of-2 inconsistency between this project's own
> `FINDING_unsuppressed_observable_periastron.md` (uses `ℓ_d = 2β_d(u_A+u_P)`)
> and MULTING's own Eq. (15) as derived directly (`ℓ_d = β_d(u_A+u_P)`, no
> extra 2)"*

and left it open as housekeeping (`P7:143-150`). **P215 did not fix it — it
reproduced it, then certified it with a control.** Every number in P215 §3
and §4 is low by 2×. The corrected headline is **`4.9–5.0` orders, not
`5.2–5.3`**.

### 1.4 The controls could not fail

- **PC1 is a zero-degree-of-freedom fit.** `R_NS_DEFAULT = 11.0e3` is
  labelled in the code itself *"back-solved from the existing binding row,
  see PC1"*. One free parameter tuned to one target. Its `u`-half verifies
  that `0.105 × 11000 = 1155`. Its `β`-half carries exactly one bit of
  information — *is the 2 there?* — and answers "yes", because **both sides
  of the comparison inherit the same error from the same file.** That is
  reproduction, not control.
- **PC2 and NC1 contain no assertions at all** — no `ok2`, no `ok3`, no
  second `return 1`. They print and continue. They cannot fail.
- PC2 "reproduces" `6.0e-2` — a number `P7:113` had already **retracted** in
  favour of `0.12`, for two independent reasons (this same factor of 2, and
  pulsar B's `P ≈ 2.77 s` making its rotational energy ~10⁴× smaller).
  Agreement with a retracted number was presented as a passing control.

### 1.5 The row was not missing

`P7:160-166`, 2026-08-11, had already computed it:

```
n = n0   : E_kin/mc^2 = 0.060
n = 2 n0 : E_kin/mc^2 = 0.094
n = 4 n0 : E_kin/mc^2 = 0.146
n = 7 n0 : E_kin/mc^2 = 0.206
```

and `P7:173` had already said why it could not be used: whether the author's
"ground state" means the quantum ground state (degeneracy already inside the
baseline, netting to ~zero) or a classical zero-velocity baseline *"is not
decided by anything in the corpus — this is a genuine interpretive gap"*,
carrying a skeptic verdict of `NEEDS-REAL-DATA`.

**P215 took a branch a prior round had marked `[UNKNOWN]`, resolved it
silently in one direction, and reported the result as settled.** §1.1 shows
the text resolves it in the *other* direction.

### 1.6 Wrong comparison target

The headline compares against *"Table A1's fitted `β_d = 4.5`"*. Table A1 is
**not in v6 at all**, and `CLAUDE.md` carries a hard rule: Table A1 is
confirmed **AI output**, never a comparison target. v82 has real fitted
`β₁`, `β₂` (Table II, 752-760) — the structurally correct target, unused.
Also dropped: `P7:128-141`'s finding that this is a **joint `(κ, β_d)`**
constraint, not a pure `β_d` bound; at `κ ≈ 0.06` the margin falls to ~3.7
orders.

### 1.7 What survives in P215

The **physics is sound**, independently confirmed: the relativistic Fermi
formula and its prefactor (the integral identity differentiates back
correctly); the internal consistency of the §3 table; NC1's convergence
rates (`≈ −0.1787 x²`); the 5.5 cm limit's derivation
(`2.4e-6 × 6GM/c² = 0.0550 m`); and — by a Jensen argument on the convexity
of `t^{5/3}` — caveat 1's claim that uniform density is genuinely
conservative. The `n = M/(m_n V)` objection was tested and does **not**
break anything (competing biases of a few percent each).

---

## 2. P216 — a node **is** an object, by v82's own definition

**v82:1028** `[VERIFIED-source]`, inside the section titled *"Circumstances
where this framework should not be expected to be accurate"*:

> *"This framework treats each **node** as a single, typical **object**,
> characterized by one mass, radius, and thermal energy at each redshift…"*

**v82:1059**: *"**Typical objects**, not distributions… not a scattered
population of **node** properties."* Both words, one referent, one sentence.

The three "scope statements" are therefore nested, not competing. And
v82:188 says Eqs. (1)-(4) *"pertain **for**"* node-A on node-P — not *"only
for"*, which is the exclusivity P216 needed and never had.

**v82:1350-1351 and 1354-1355 are a matched pair:**

> *"We suggest that **Newtonian physics, such as Eq. (2)**, associates with a
> source (such as object-A)… **but not necessarily with an observer**."*
> *"We suggest than **MULTING, including Eq. (1)**, associates with a source
> (such as object-A)… **but not necessarily with an observer**."*

The subject of both is **the observer**. P216 read a statement about
observers as a statement about scope.

**Self-inflicted:** P216 §1 itself argues *"'Such as' is an example, not an
exhaustion"* — then declines that same reading where `such as object-A`
makes the hierarchy nested.

**Relevant context P216 omitted:** v82:1453 — *"This paper does not explore
possibilities for basing an analog to general relativity on MULTING"*;
v82:1457-1458 — *"concordance cosmology can embrace **both**"*; and
v82:1461-1463 — *"General relativity is extraordinarily well tested where it
has actually been tested directly: solar-system dynamics, **binary pulsar
timing**…"*. v82 assigns the double pulsar to GR's jurisdiction explicitly.

**What survives:** §5's `β₁` per-node / `β₂` per-pair asymmetry (accurate,
standalone, needs neither §1 nor §5a); §4's literal reading of 1453-1456
(collisions, and ref [125] is indeed a merger paper); §3's factual point
that v82's operational `k` exists only in ICM form; and the accuracy of
every quoted line.

---

## 3. P217 — register swap, not axis substitution

### 3.1 v6 DOES constrain `β` across objects — in its equations

**v6:807-810** `[VERIFIED-source]`:

```
rdA = βd rA     (18)
rdP = βd rP     (19)
```

**The same `βd`** for object-A and object-P, while `r` **is**
object-indexed. v6's notation asserts object-independence directly. Same for
the pair: `|rqAB|² = (βq)² rA rP` puts the pair index `AB` on `r`, not on
`βq`.

### 3.2 v82 DOES constrain `β` across time — in its procedure and notation

v82:647-652 and 707-709: **one scalar each**, jointly optimized against all
33 points spanning `0.0233 < z < 2.33`. Table II gives one number per row,
not a function. Every `z`-dependent quantity in v82 carries an explicit
`(z)` — `m_X(z)`, `r_X(z)`, `k_X(z)`, `T_X(z)` — while `β₁`, `β₂` never do.
And v82:336 opens the evolution section with *"The physical properties of
the nodes are **not static**"*, then lists what evolves; `β` is not listed.

### 3.3 The corrected picture

| | across time | across objects/nodes |
|---|---|---|
| **v6** | explicit prose (805-806) | equations only (807-810) |
| **v6 prompt appendix** | *"one value that **does not vary with time**"* (2214) | — |
| **v82** | procedure + notation only (647-652, 707-709, absence of `(z)`) | explicit prose (213-220) |

**Both documents assert both properties.** What changed is which register
carries which. `"narrowing"` — the word `P214`'s retraction §7.2 used, and
which P217 "sharpened" away — was closer to right than its replacement.

### 3.4 §2a and §5a are dead, and the correction was worse than the original

P217 §2a claimed v82:652's `β ≥ 0` contradicts v82:213's *"positive"*, and
called it a second instance of P216's pattern. Both halves fail:

- **v82:1719** — the author's own gloss on those exact constraints: *"…in
  favor of the minimal constraints that are actually necessary
  (**positivity**, numerical feasibility)."* The `≥` is the numerical
  closure of an open condition; it sits in the same sentence as an
  explicitly **numerical** requirement, `[H(z_n)]² > 0`.
- **v6 uses both words for the same symbols**: v6:2214 *"Assume that βd and
  βq are **positive** numbers"*; v6:2313 *"Constrain each one of βd and βq
  to be **non-negative**."* It is the author's own idiom, carried forward —
  not a v82 inconsistency.

So `b1 > 0` **is** sourced by v82:213. P217 §4.1's *first* draft was right,
and the §2a "correction" made it worse. The `stage1` guard stays — as a
numerical guard on numerical grounds, not because "the sources disagree."

### 3.5 Citation defects

- `v6:679-680` for the `nonnegative`/`time` quote is **wrong in both
  extractions**: it is 680-682 (old) / 805-806 (clean). This contradicts
  P217's own header claim, *"All lines re-read from the extractions
  directly."*
- `stage1_dHdk_derivability.py` was cited bare; it lives in
  `experiments/20260907-icm-expansion-correlation/`, not this folder.
- v82:939 was called *"the only"* `vary with time`; a second is at 831-832,
  also about `w`.

---

## 4. Root cause, common to all three

**A one-sided search reported as a two-sided comparison.** Every failure has
the same shape:

- **P217** — I swept every `β` mention **in v82 only**, then stated a
  conclusion about the *relationship between v82 and v6*. The same sweep on
  v6 would have dissolved it in a minute.
- **P215** — I never ran the FL **Step -3 pre-work check** against my own
  directory. `FINDING_P7`, which had already computed the degenerate row,
  already flagged the factor of 2, and already explained why the branch was
  `[UNKNOWN]`, was sitting in the folder I was writing into.
- **P216** — I cited only sections where the theory is **applied**, none
  where it **bounds itself**. Both killing lines (1028, 1719) live in
  sections named exactly that: *"Circumstances where this framework should
  not be expected to be accurate"*, and the retrospective at 1716-1720.
- **All three** — greps ran against the **older, glued** v6 extraction while
  the sibling file's own header line 10 says it is the **PREFERRED text for
  grep/search**.

And both "improvements" made during the session moved *away* from the
sources: `"a real narrowing"` → `"axis substitution"` (worse), and
`"b1 > 0 is sourced"` → `"not discharged"` (worse). Both times the earlier,
less clever formulation was the accurate one.

---

## 5. Actions

- All three findings carry a **DO NOT CITE** banner pointing here.
- The factor-of-2 error is **live and propagating**: `P7:143-150` left it
  open on 2026-08-11, and it has now infected a second file. It needs
  fixing at the source, not per-file.
- `FINDING_P214_RETRACTION_after_step8a.md` §3's energy enumeration is
  **withdrawn** (see §1.2).
- `CURRENT_EVIDENCE_STATE.md` §7.6 is rewritten to match.
- The `k` question **still stands**, and the corpus leans further against
  the compact-object reading than any of these three files claimed.
