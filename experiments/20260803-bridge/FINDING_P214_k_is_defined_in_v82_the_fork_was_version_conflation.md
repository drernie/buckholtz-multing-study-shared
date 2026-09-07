# FINDING P214 — `k` **is** defined in v82. `MODEL_SPEC_AUDIT` §5's
# "single load-bearing open question" was a **v6/v82 conflation**, ours.

**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
**`NO_AUTHOR_ERROR` — emphatically**: the author *sharpened* the
definition between versions; this project read two documents as one
corpus. L0 `descriptive`.
**Method:** direct reading of both source documents. No new computation.

---

## 1. The claim being checked

`MODEL_SPEC_AUDIT` §5, verbatim:

> **"Every unresolved row above terminates at the same place: what is
> `k`?"** … *"The corpus's own text supports the broad reading in places
> and the narrow one in the cluster analysis."*

Two readings were enumerated — narrow (thermal only) and broad (binding,
rotational, degeneracy) — differing by `6.8×10⁸` in `|Δψ|` (`P213`), and
the question was drafted for the author and held
(`P3_k_definition_question_DRAFT_HELD.md`).

**It did not need to be asked. v82 answers it in its own symbol table.**

## 2. v82 defines `k` explicitly `[VERIFIED-source]`

`data/source_material/buckholtz_202608.0943v1.v82.md`, **line 207**,
verbatim, in the paragraph that defines every symbol of Eqs. (1)–(4):

> **"`k_A` is the thermal energy that associates with the ICM of node-A.
> `k_A` is nonnegative. `k_A/c²` has dimensions of mass."**

This is a **definition**, not a motivating aside — it sits between the
definitions of `r_A` and `β₁`.

The preceding paragraph (lines 177–186) is equally explicit:

> *"Regarding nodes, cosmology measures the properties mass, radius,
> **thermal energy**, and **bulk energy** (as in the energy that
> characterizes bulk motions within the node). The thermal energy is the
> total of the kinetic energies of the nucleons and electrons that
> comprise the intracluster medium (ICM) of a node. … about **70 percent
> to 90 percent** of a node's ICM kinetic energy is thermal energy
> [13–15]. … (See Sec. IV.F for the physical motivation … for **why
> thermal rather than bulk kinetic energy is treated as the basis for
> this dipole component**.)"*

So v82 (a) names thermal and bulk as **separate** node properties,
(b) defines `k` as the thermal one, (c) states there is a dedicated
section arguing **thermal rather than bulk**, and (d) ties `k` to the
**ICM** specifically.

## 3. The "broad reading" is v6, not v82 `[VERIFIED-tool]`

| | v6 | v82 |
|---|---|---|
| occurrences of "thermal" | **2** | **34** |
| explicit definition `k` = ICM thermal energy | **absent** (grep found none) | **line 207** |
| "kinetic energy, inside objects, of sub-objects" | **line 91** | — |
| "degeneracy" / "degenerate" / "Fermi" | — | **0 hits** |
| "binding energy" | — | **0 hits** |
| "neutron star" | — | **2 hits, both about mergers**, in the sentence *"MULTING does not (yet) adequately discuss overlapping objects or colliding objects"* |

**The author narrowed the definition between versions.** v6 speaks of
"kinetic energy of sub-objects" broadly; v82 defines `k` as ICM thermal
energy and adds a section motivating the choice.

`MODEL_SPEC_AUDIT` §5 cited `multing_core.py:90-91` (v82's supplemental,
docstring *"Total ICM thermal energy k_X(z) = (3/2) N_particles * k_B*T"*)
for the narrow reading, and "the corpus's own text" for the broad one —
but the broad phrasing it was matching is **v6's**.

**This is exactly the failure `CLAUDE.md` names:** *"Cite v6 for anything
already established; cite v82 for anything new going forward; **never
conflate the two without checking.**"*

## 4. Artifact-identity check `[VERIFIED-tool]`

Before treating code and text as one document: the supplemental archive's
own `README.md` opens *"Supplemental archive for 'Multi-Tier Newtonian
Gravity: A Cosmic-Node-Based Alternative to LCDM for the Hubble
Tension'"* — v82's exact title. Code and text belong together. The
differing Zenodo record numbers (`21204955` supplemental vs `22004287`
paper) are separate DOIs for the two artifacts, not two papers.

Also checked: `k` is computed **once** in the whole archive (`k_of`,
`multing_core.py:89`) and consumed in exactly **two** places (`F1`, `F2`,
lines 120–121). There is no second `k` for a different object class.

## 5. Consequences — four open items move

| item | was | now |
|---|---|---|
| `MODEL_SPEC_AUDIT` §5 "single load-bearing open question" | OPEN | **ANSWERED for v82**: `k` = ICM thermal energy |
| `P213`'s `6.8×10⁸` fork | undecided | **resolves to the narrow branch** |
| MICROSCOPE bound on `η` (`P209`) | broad → `η ≲ 9×10⁻⁴` (bites); narrow → `η ≲ 6×10⁵` | **narrow applies ⇒ MICROSCOPE does not usefully bound `η`** |
| periastron bound `β_d < 1.2×10⁻⁵` (pearl row 112) | quoted as excluding Table A1's `4.5` by five orders | **rests on the broad reading ⇒ does not apply to v82** |
| `P3_k_definition_question_DRAFT_HELD.md` | held, awaiting a send window | **no longer needed as posed** |

## 6. This is a LOSS of testable content, not a win — stated plainly

Resolving `k` to ICM thermal energy does not strengthen MULTING. It
**shrinks its domain**:

- A neutron star has **no ICM**. `k` is undefined for it. The pulsar
  periastron test — the sharpest external constraint this project had
  found — **does not reach v82 at all.**
- MICROSCOPE likewise stops constraining `η` usefully.

So two of the project's best falsification routes turn out to be aimed at
a reading v82 does not use. **A theory that cannot be tested by pulsar
timing is not thereby a better theory** — it is a theory with a narrower
testable footprint, which is the same direction `FINDING_E21` already
reported for the high-`z` extrapolations.

## 7. What this does NOT establish

1. **Not that `k` is defined for general objects.** v82 defines it for
   **nodes**, via their ICM. Its discussion section (lines 1444–1452)
   speculates about objects "for which internal energies that associate
   with the motions of sub-objects are significant" — that is *future
   possibility*, not definition, and the same passage assigns **bulk**
   motions a *different* (possibly attractive) role, not `k`'s.
2. **Not that the periastron calculation was wrong.** Its arithmetic
   stands; `FINDING_unsuppressed_observable_periastron.md` already stated
   the conditional openly (*"if k is strictly thermal — which should be
   checked against how the cluster analysis uses it"*). This finding
   performs that check. The bound is real for the broad reading and
   simply does not apply to v82.
3. **Not a claim about the author** (`NO_AUTHOR_ERROR`). v82 is clear.
   The ambiguity lived in **this project's** treatment of two versions as
   one corpus.
4. **Not verified: Sec. IV.F's actual argument.** v82 says a section
   motivates "thermal rather than bulk"; that section's reasoning has not
   been read or assessed here — only its existence and its conclusion.

## 8. Immediate action items

- `MODEL_SPEC_AUDIT` §5 needs an in-place correction banner (originals
  quoted, not deleted).
- `P3_k_definition_question_DRAFT_HELD.md` should be re-headed: the
  question as posed is answered by v82's own line 207.
- Pearl row 112 (periastron) needs its conditional re-stated: the branch
  it depends on is v6's.
