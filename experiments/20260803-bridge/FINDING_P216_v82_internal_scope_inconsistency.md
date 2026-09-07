> # [RETRACTED 2026-09-07] DO NOT CITE
>
> Falsified by a context-blind Step 8a skeptic pass the same day, independently re-verified against source by me.
>
> **Core claim FALSIFIED**: v82:1028 — "This framework treats each NODE as a single, typical OBJECT" — the two are nested, not competing scope levels. v82:1350-1355 is a matched pair about the OBSERVER, not about scope. Only the beta1/beta2 asymmetry (§5) survives.
>
> Full record: `FINDING_P215_P216_P217_RETRACTION_after_step8a.md`. Text below kept verbatim, not edited (no-silent-correction).

---

# FINDING P216 — v82 states the scope of Eqs. (1)–(4) at two different
# levels: **node** in the symbol-definition section, **object** twice in
# the discussion. Internal, citable, needs no version comparison.

**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Provenance:** extracted from `FINDING_P214_RETRACTION_after_step8a.md` §7.1
— one of two results that survived that retraction and had until now no
record of its own. All line numbers re-read from
`data/source_material/buckholtz_202608.0943v1.v82.md` today, independently
of the retraction document.

---

## 1. The observation, in v82's own words

| line | scope word | verbatim |
|---|---|---|
| **188** | **node** | *"MULTING suggests that Eqs. (1) through (4) pertain for gravitational effects of a **node-A** on a **node-P**."* |
| **1354-1355** | **object** | *"We suggest than MULTING, **including Eq. (1)**, associates with a source (**such as** object-A) and with a probe (such as object-P) but not necessarily with an observer."* |
| **1449-1452** | **object** | *"MULTING (**including Eqs. (1) through (4)**) suggests that one needs to consider at least one property, the energy of motion of nonzero-mass sub-objects… for each one of an **object-A**… and an **object-P**…"* |

Same equations, named explicitly in all three places. Two different
scope words.

Plus **v82:999-1000** keeps the property class open rather than closing
it: *"some non-mass properties, **such as** thermal kinetic energy, of a
node might couple significantly to another node's mass."* **"Such as" is
an example, not an exhaustion** — same construction as *"such as object-A"*
at 1354.

## 2. Why this is a finding and not a nitpick

The two readings license different applications of the **same** equations:

| reading | what Eqs. (1)–(4) apply to | consequence |
|---|---|---|
| **node** (188) | cosmic-web nodes — clusters, protoclusters | a neutron star is out of scope; no external compact-object bound applies |
| **object** (1354-1355, 1449-1452) | objects generally, with node as one example | a neutron star is in scope; `β` inherits every compact-object constraint |

Every external bound on `β` this project has computed — the double-pulsar
periastron bound (`P215`), the MICROSCOPE η line — is **live under the
second reading and moot under the first**. The reading is not a stylistic
matter; it decides whether a five-order-of-magnitude constraint exists.

## 3. Which reading is load-bearing where, in v82 itself

v82's own **operational** chain is node-scoped: Eqs. (12)–(14) go
`m → T → M_gas → k` through an **X-ray ICM** calibration, executable in
`multing_core.py:79-91`, and `k_A` at line 207 is defined as *"the thermal
energy that associates with the **ICM** of node-A."* A neutron star has no
ICM, so that chain does not evaluate for one.

But the **claim** at 1449-1452 is broader than the chain: it asks for
*"the energy of motion of nonzero-mass sub-objects"* of an **object** —
a quantity a neutron star has (its degenerate Fermi sea, `P215`), even
though the ICM chain cannot compute it.

So the inconsistency is not a typo in one place. It is a **definition
narrower than the claim built on it**: the symbol is given a node-specific
operational meaning, and the surrounding text twice asserts the equations
at object level, where that operational meaning does not evaluate.

## 4. What v82 does exclude, and what it does not

v82:1453-1456 is an explicit exclusion, and it is about **collisions**:
*"MULTING does not (yet) adequately discuss **overlapping objects or
colliding objects**"* — its ref [125] is a neutron-star-**merger** paper.

A binary pulsar on a stable, wide, eccentric orbit is neither overlapping
nor colliding. **That sentence does not exclude compact objects; it
excludes collisions.** (`P214` read it as the former — that misreading is
one of the four claims its retraction withdrew.)

## 5. A third scope word, found today and not in the retraction

The two `β` definitions at v82:213-218 are **not scoped identically to
each other**:

> *"**β₁** is a positive number that we suggest might be approximately
> independent of the choice of a specific **node**"*
> *"**β₂** is a positive number that we suggest might be approximately
> independent of the choice of a specific **pair of nodes**"*

`β₁` per-node, `β₂` per-pair. That asymmetry is structurally correct —
`F^(1)` carries one node's `k_A r_A`, `F^(2)` carries a product across the
pair — but it means the two parameters do not inherit the same universality
claim, and an argument that transfers a bound on one to the other has to
say why.

## 5a. The same pattern, a second time: the sign of `β`

Found the day this finding was written, while hardening `P217`'s greps.
Not scope this time, but the identical shape — **definition and procedure
disagreeing about one symbol inside one document**:

| v82 line | says |
|---|---|
| **213** | *"β₁ is a **positive** number…"* |
| **652** | *"…subject only to **β₁ ≥ 0, β₂ ≥ 0**, and the numerical requirement `[H(z_n)]² > 0`…"* |

`β = 0` is excluded where the symbol is defined and admitted where the fit
is constrained. Consequence recorded in `P217` §2a and §4.1: the ICM
branch's `b1 > 0` side-condition is **not** discharged, and its guard is
load-bearing.

Two instances is not yet a general claim about the document. It is enough
to say the scope case in §1 is **not isolated**, and that any symbol this
project leans on should be checked at both its definition site and its use
site rather than at whichever one is found first.

## 6. What this does and does not establish

**Establishes:** v82, read alone, does not fix the domain of Eqs. (1)–(4)
to a single object class. Both readings are supported by explicit,
equation-naming sentences in the published text.

**Does not establish** that either reading is wrong, that the author
intended one over the other, or that the ambiguity is an error. It is a
statement about what the published text underdetermines — `NO_AUTHOR_ERROR`.

**Does not depend** on v6 in any way. This is the difference between this
finding and `P214`: `P214` claimed the ambiguity was an artifact of reading
two versions as one corpus, and was falsified. The ambiguity is **internal
to v82**, and needs no version comparison to state.

## 7. Consequence for this project's own bounds

Every `β` bound derived from a non-cluster system must now carry its
reading explicitly, rather than assuming scope. `P215`'s periastron result
already does — it states the bound holds *if* `k` extends to compact
objects at all.

## 8. Caveats

1. Line numbers are into the markdown extraction, not the PDF's own
   pagination. Re-verify against the PDF before external citation.
2. The extraction has word-gluing artifacts (`MULTINGsuggeststhatEqs.`);
   quotes above are de-glued for readability, content unchanged.
3. No Step 8a pass on `P216` itself. The underlying observation *was*
   produced by a Step 8a skeptic pass (on `P214`) and independently
   re-read by me both then and today.
