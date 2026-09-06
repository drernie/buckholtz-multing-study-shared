# FINDING P207 — one propagated framing error, one retrieval gap, and a
# measured 6% citation base rate that killed most of this file's first draft

**Date:** 2026-09-07
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 **descriptive** (an audit of this project's own
artifacts — no physical claim, no new computation about MULTING)
**Step 8a:** context-blind skeptic, run on the **uncorrected** draft.
Verdicts: C1 WEAKENED, **C2 FALSIFIED**, C3 WEAKENED, C4 diagnosis
confirmed / prescribed fix WEAKENED. All accepted; see §5.

---

## 1. What this file is, after most of it was withdrawn

The tick began as a follow-up to `FINDING_P206` §7.1, which predicted that
grepping prior findings for **structure words** (rank / nullspace /
redundancy / invariant) rather than for a claim's own vocabulary would
surface intra-repo duplication. The grep returned 22 findings, and reading
their titles produced four pairs where a later finding appeared to treat
the same structural object as an earlier one without citing it.

**That framing is withdrawn.** Before the skeptic returned, a base-rate
control was run and it removed most of the claim's information content
(§2). The skeptic then independently reached the same place from different
evidence and additionally falsified the mechanism story (§5).

What survives is smaller and better supported: **one propagated framing
error, one retrieval-infrastructure gap, and one measured number.**

## 2. The base-rate control — run before the skeptic, and decisive

For each of the 22 structure-word findings, counted how many *earlier*
siblings existed at its date and how many of them it cites (word-boundary
`\bP\d{1,3}\b`, self-citations removed):

```
AGGREGATE: 14 / 231 = 0.061
```

**A given earlier sibling is cited ~6% of the time. "Does not cite X" is
the default outcome ~94% of the time.**

Therefore *finding four uncited pairs among 22 findings is exactly what the
base rate predicts.* The four pairs were selected by reading titles for
topical similarity and then "confirmed" by observing a missing citation —
selection on the outcome, against a 94% default. The confirmation carried
no information.

**Consequence — withdrawn from the first draft:**

| withdrawn | why |
|---|---|
| "four unacknowledged pairs" as a finding | consistent with base rate |
| `P190` ↮ `P161` | no consequence demonstrated; base rate explains it |
| `P163` ↮ `P53` | same |
| the "lineage capture" mechanism | fitted to exactly those two pairs |

This control is the same discipline `artifact-provenance-gates.md` Gate 3
requires of a digitizer: run the test on a **known** object before
trusting it on an unknown one. Here the known object is the citation
distribution over the whole corpus, not the four hand-picked pairs.

## 3. What survives — and why each survives for a reason independent of §2

### 3.1 A propagated framing error: `P133` did not see `P52`

This one does **not** rest on the missing citation. Its consequence was
established independently by `FINDING_P206` (skeptic-reviewed twice):
`P133`'s rank-2 result *is* `P52`'s one-dimensional field-normalization
redundancy, and all three of `P133`'s observables are `P52` invariants.

`P52` (2026-08-16) recorded its verdict as **CONDITIONAL**. `P133`
(2026-08-24) recorded the same structure as an **OPEN bottleneck**. Five
findings downstream — `P137`, `P163`, `P205`, `P206`, and `docs/147`'s own
bottleneck-3 entry — were then framed against "open" rather than against
"conditional."

`P133` §2's own text shows the search was real but scoped too narrowly:
*"Grepped every `FINDING_P*.md` for a κ↔g relation. Found one:
`FINDING_P24`."* A κ↔g search cannot surface a finding about `A`.

### 3.2 A retrieval gap: NULL RESULTs are invisible to the prescribed check

Exactly two findings declare `**Verdict:** NULL RESULT` and appear nowhere
in `null_results/INDEX.md`:

- `FINDING_P137` — literature search for a 4th observable, search exhausted
- `FINDING_P140` — positivity does not discriminate the two completions
  (`BOTH-SAFE`)

`null_results/INDEX.md` is 53 lines, uses `NR-###` ids, and contains
**zero** P-numbered bridge findings. The project's prescribed pre-work
check is `grep -i "keyword" null_results/INDEX.md`. **That check could not
have surfaced `P137` for any keyword.**

This survives §2 because it is not about citing habits at all — it is a
mechanical property of the index. The skeptic's own unification is better
than the first draft's and is adopted verbatim: *the pre-work check is
insufficient because the INDEX it queries is populated only from
Full-Ladder REJECT decisions, so any Standard-Ladder NULL RESULT is
structurally invisible to it.*

### 3.3 The 6% rate is itself the most useful output

At a 6% citation rate, **the citation graph is not a retrieval mechanism in
this corpus.** One cannot reach related work by following references. That
does not weaken `P206` §7's structure-word heuristic — it is the reason the
heuristic is needed, and it is why §3.1 and §3.2 were both found by
grepping rather than by reading reference lists.

## 4. Material sub-claim, narrowed: `P137`'s class-(i) null is necessary
## — *conditional on no external scale breaking the rescaling redundancy*

`P133` named three classes of candidate 4th observable: **(i)** a monomial
whose exponent vector is independent of the 2-D span, **(ii)** a
non-monomial observable, **(iii)** a theory-fixed value of `A`. `P137`
searched the literature and returned NULL, with its own §5.1 caveat: *"two
targeted searches, not an exhaustive review."*

`P206` upgrades class (i) **by derivation**: raising the rank ⟺ `L ≠ 0` ⟺
non-invariant under `φ → λφ̄`. So no class-(i) monomial can break the
degeneracy while remaining convention-independent.

**The hidden assumption, named by the skeptic and accepted:** the step
*"non-invariant ⟹ not a physical observable"* is a stance, not a theorem.
It holds when `φ → λφ̄` is an exact redundancy of the whole theory. It
fails if an external scale fixes `λ` — a non-minimal `ξφ²R` coupling, a
`φ/M_Pl` suppression, or any sector requiring canonical normalization.
**That caveat matters specifically here**, because MULTING is explicitly
trying to bridge to gravity and cosmology, which is exactly where such
scales enter.

**Surviving statement:** *for any class-(i) candidate arriving as a
monomial in `(A, g, κ)`, and given that the `φ → λφ̄` redundancy is
unbroken, `P137`'s null is necessary rather than contingent — so repeating
that literature search has no expected yield.* Class (ii) remains open.
Class (iii) is reinterpreted by `P206` as a convention choice.

**Convergence worth recording:** this is the **third** independent
context-blind skeptic run to raise the external-anchor caveat (two on
`P206`, one here). Three independent raisings of the same limitation is
stronger evidence that it is load-bearing than any single verdict.
It is already carried in `P206` §6.2 and in the `pearl_registry` row.

## 5. Step 8a — verdicts accepted, and one substrate finding

| claim | verdict | disposition |
|---|---|---|
| C1 four pairs | WEAKENED | accepted; already withdrawn by §2 independently |
| C2 three mechanisms | **FALSIFIED** | accepted, withdrawn entirely |
| C3 class-(i) closure | WEAKENED | accepted; caveat added, §4 |
| C4 mis-filing diagnosis | CONFIRMED | accepted |
| C4 prescribed fix | WEAKENED | accepted; see below |

**C4's fix was over-engineered and is withdrawn.** The first draft
prescribed a separately-labelled section for non-REJECT nulls. Checked
directly: the index already carries `REJECT (partial)`, `WEAKENED
(mechanism unresolved)`, `REJECTED_AS_DERIVATION`, `REJECTED WITHIN
IMPLEMENTATION`, `REJECT/INCONCLUSIVE`, and 4 `KILL` rows. The schema
already tolerates precise non-REJECT verdicts. Two accurately-labelled
rows suffice; no structural change.

**Substrate finding — recorded, not treated as evidence.** The skeptic
reported it could not open `FINDING_P52`, `FINDING_P53`, `FINDING_P161`,
or `FINDING_P206` under any filename variant, and correctly flagged its
verdicts on C1(a)/C1(d)/C3 as resting on transitive corroboration. **All
four files exist** (`ls` verified; three were read directly earlier this
session). Per the Substrate Gate's own rule, "the reviewer could not open
the file" is `BLOCKED-INFRASTRUCTURE`, never evidence against a claim —
so C1(a) keeps the status its own direct verification gives it, and C3's
weakening stands on the skeptic's *reasoning*, which needed none of those
files.

**One skeptic point adopted that the draft had missed:** C1(b)
(`P205` ↮ `P137`) is a **courtesy** gap, not duplicated work. `P205`
derived the structural criterion that supersedes `P137`'s empirical
negative; one need not cite a failed search one has turned into a theorem.
Reporting it as "redundant work" would have been the same over-read §2
already caught elsewhere.

## 6. What this does NOT establish

1. **Not that the four pairs are harmless** — only that a missing citation
   is uninformative at a 6% base rate. `P190`↮`P161` and `P163`↮`P53` are
   *unchecked*, not cleared.
2. **Not that `P52`'s CONDITIONAL verdict is correct** — inherited
   unchanged, including its KG2 (form invariance ≠ value determination),
   which remains the genuinely open question behind bottleneck 3/wall 4.
3. **Not a claim about MULTING** (`NO_AUTHOR_ERROR`). This audits this
   project's own filing and retrieval, nothing about the preprint.
4. **Not that adding two index rows fixes the cause.** It fixes retrieval
   for those two findings. The behavioural half — searching across
   parallel chains before writing — is untouched, and at a 6% citation
   rate there is no evidence it has ever been practised here.
