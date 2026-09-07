# FINDING P217 — between v6 and v82 the universality claim for `β` was not
# narrowed, it was moved to a **different axis**: v6 constrains `β` across
# **time** and says nothing about across objects; v82 constrains it across
# **nodes** and says nothing about across time.

**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Provenance:** extracted and **sharpened** from
`FINDING_P214_RETRACTION_after_step8a.md` §7.2, the second of two results
that survived that retraction with no record of its own. §7.2 called this
"a real narrowing." Re-reading both sources today shows *narrowing* is the
wrong word — see §2. All lines re-read from the extractions directly.

---

## 1. The two statements, verbatim

**v6:679-680** — one joint statement for both parameters:

> *"We posit, for the purposes of this paper, Eqs. (18) through (20). **β_d**
> and **β_q** are **nonnegative** numbers **that do not vary significantly
> with time**."*

**v82:213-218** — two separate statements, differently scoped:

> *"**β₁** is a **positive** number that we suggest might be approximately
> **independent of the choice of a specific node**; the subscript 1 in β
> corresponds to the dipole order, (1), in F^(1)."*
> *"**β₂** is a positive number that we suggest might be approximately
> independent of the choice of a specific **pair of nodes**…"*

## 2. Three changes, and the middle one is not a narrowing

| # | v6 | v82 | what kind of change |
|---|---|---|---|
| 1 | **nonnegative** (β = 0 allowed) | **positive** at 213 — but **`β ≥ 0`** at 652 | **not a clean change — v82 is internally inconsistent here, see §2a** |
| 2 | invariant **across time** | invariant **across nodes** / **across pairs** | **axis substitution** |
| 3 | one statement for both β | two statements, `β₁` per-node, `β₂` per-pair | refinement |

### 2a. CORRECTION, made before this finding was committed

**First draft of this file said, in §4.1:** *"`b1 > 0` is **sourced** under
v82… v82:213 supplies it."* **That is wrong**, and it is kept here rather
than deleted (no-silent-correction).

A wider sweep of every `β` mention in v82 — run precisely because this
finding's own §3 is about trusting a negative grep — found **v82:652**:

> *"…determined by chi-squared minimization… subject only to **β₁ ≥ 0,
> β₂ ≥ 0**, and the numerical requirement `[H(z_n)]² > 0`…"*

So v82 says **"positive"** where it defines `β₁` (213) and **`≥ 0`** where
it constrains the fit (652). `β = 0` is excluded by the definition and
admitted by the procedure.

**This is a second instance of exactly the pattern `P216` records** —
a definitional statement and an operational statement disagreeing about
the same symbol, in the same document. `P216` found it for *scope*
(node vs object); this is the same shape for *sign*.

**Consequence:** `b1 > 0` is **not** discharged for v82. It remains a
side-condition, and §4.1 below is corrected accordingly.

Change 2 is the substantive one, and *narrowing* mis-describes it. Time
and object-class are **orthogonal axes**. v6 says nothing about whether
`β` is the same for two different objects; v82 says nothing about whether
`β` is the same at two different epochs. Neither statement is a subset of
the other — **each version leaves unconstrained exactly the axis the other
constrains.**

`[VERIFIED-grep]` v82 contains **no** time-invariance statement for `β`:
the only `"vary with time"` in the document is line 939, about `w`, the
dark-energy equation-of-state parameter, unrelated.

## 3. Cross-check: v6 never uses the word "node" at all

`grep -c -i node` on the v6 extraction returns **2**, and both are
word-gluing artifacts — `"neutri`**`nod`**`ensities"` (lines 1357, 1360),
`neutrino` + `densities` run together. **v6 uses "node" as a physics term
zero times.** Its own scope statement, v6:639, is unambiguous:

> *"Eqs. (14) through (17) pertain, regarding an interaction between an
> **object-A** and an **object-P**, regarding the gravitational force that
> affects object-P."*

So the version story on scope is:

| | scope statements for the force equations |
|---|---|
| **v6** | exactly one, **object** (639). "node" absent from the document. |
| **v82** | three: **node** (188), **object** (1354-1355), **object** (1449-1452) |

v82 did not *replace* object with node. It **added** a node-level statement
alongside object-level ones it kept — which is why the ambiguity `P216`
records is internal to v82 and absent from v6.

## 4. Two concrete consequences for this project's own results

### 4.1 `b1 > 0` is NOT discharged — by either version `[CORRECTED, see §2a]`

The ICM branch's response-sign analysis
(`stage1_dHdk_derivability.py:86`) resolved, after its Step 8a pass, to:

> *"sign is POSITIVE iff `Q < 1` **AND `b1 > 0`**"*

`b1 > 0` was carried there as a stated side-condition, not a sourced fact.
**It still is.** v82:213 appears to supply it — *"β₁ is a **positive**
number"* — but v82:652 constrains its own fit *"subject only to β₁ ≥ 0,
β₂ ≥ 0"*, readmitting the excluded case. v6 says *nonnegative* outright
(679-680). At `β_d = 0` the dipole term vanishes identically and `Q` is
undefined — the code raises on exactly this (`stage1:89`), which is why
`sign_of_response()` exists.

**So the ICM branch's caveat stands under both versions**, and the branch's
existing handling (raise on `b1 = 0`, separate sign function valid for any
`b1`) is the correct one — it was not over-cautious.

### 4.2 `β` constant across redshift is **not** stated by v82

`[VERIFIED-code]` v82's own supplemental `multing_core.py` takes `b1, b2`
as **scalars** (`forces(z, beta_1, beta_2)`, line 112) and applies them
unchanged across the whole `zgrid` (`H2_of_z`, line 180). Constancy in `z`
is built into the implementation.

That constancy is exactly what **v6** asserted — *"do not vary significantly
with time"* — and exactly what **v82 does not restate.**

Every result this project holds is pinned to v82. So the `z`-constancy of
`β` in our fits — including the fitted pair `1.4335e10 / 7.8067e17` — is
currently justified by **v82's code**, not by **v82's text**. Under v82
alone it is an implementation assumption; the textual warrant for it lives
in the earlier version.

This is not a defect in either document. It is a note about which of our
own results inherit their justification from which version — precisely the
distinction `CLAUDE.md` requires and `P214` was retracted for collapsing.

## 5. What this does and does not establish

**Establishes:** the two documents constrain `β` along different axes, and
neither statement implies the other. `[VERIFIED-source]` for all three
changes in §2.

**Does not establish** that either statement is wrong, that the change was
deliberate, or that anything was lost. Both are hedged in the original
(*"we posit, for the purposes of this paper"* / *"we suggest might be
approximately"*) and neither is presented as derived.

**Does not resurrect `P214`.** `P214` claimed the *broad `k`-reading* was
v6's and that v82 had narrowed it; the retraction falsified that in both
directions and this finding does not disturb the falsification. What is
recorded here is a different, narrower, separately-verified claim about the
`β` **universality statement** — not about `k`'s definitional breadth.

## 6. Caveats

1. Line numbers index the markdown extractions, not PDF pagination.
2. Quotes de-glued for readability; content unchanged. The de-gluing is
   itself why §3's `grep -c` needed reading rather than trusting — a
   morphology-blind count would have reported v6 as using "node."
3. No Step 8a pass on `P217` itself.
