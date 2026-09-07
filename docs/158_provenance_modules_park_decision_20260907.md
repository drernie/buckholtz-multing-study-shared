# docs/158 — `source_provenance.py` / `conflict_resolver.py`: PARK decision

**Date:** 2026-09-07
**Closes:** `docs/157`'s infra follow-up, *"wiring decision — decide: wire
it into `provenance_audit.py`'s chain (natural fit), or explicitly mark it
parked/superseded."*
**Verdict:** **PARKED.** Not wired. `docs/157`'s proposed join is a
category error, and the modules' actual status was mis-stated.

---

## 1. What `docs/157` said, and what is actually true

`docs/157` recorded these as *"tested but called by nothing else in the
repo"* and suggested wiring them into `provenance_audit.py` as a
*"natural fit — both are about tracking where a value's authority comes
from."* Checked directly; two of those statements need correcting.

**Correction 1 — the join is a category error.** The two modules work at
different levels:

| module | level | question it answers |
|---|---|---|
| `source_provenance` / `conflict_resolver` | **value** | symbol `beta_d` carries 4.5 from the manuscript and 4.25 from a fit — which wins, and may they be mixed? |
| `provenance_audit` | **chain** | this measurement step declares it *avoids* assumption A, but what does it *incur* instead? (`CIRCULAR` / `OUTSIDE_SIGMA` / `UNQUANTIFIED`) |

`provenance_audit` was built for `FINDING_E6`'s two-field classification —
a step's declared class is not the same as its incurred dependency. That
has nothing to do with adjudicating between two numbers for one symbol.
Wiring them would force a join between an audit of *reasoning steps* and a
registry of *values*.

**Correction 2 — `beta_provenance` is not part of this debt.** It is live
and well-wired: `beta_definitions.py`, `report.py`, `source_provenance.py`,
`tests/test_beta_registry_consistency.py`,
`tests/test_beta_status_required.py` and `scripts/brai_beta.py` all use it.

**Correction 3 — the docstring had the dependency arrow backwards.**
`source_provenance.py` claimed *"INTEGRATION: beta_provenance.py uses this
system for beta values."* It does not. `beta_provenance.py` imports only
`dataclasses` and `typing`; the real edge runs the other way —
`source_provenance` imports `beta_provenance`. Fixed in place, with the
old claim quoted rather than deleted.

So the accurate statement of the debt is narrower than `docs/157` had it:
**`source_provenance` and `conflict_resolver` are a layer sitting on top of
a live module, and nothing above them uses either.**

## 2. Why parked rather than wired

The gap these modules were plausibly built for is
`~/.claude/rules/research-methodology.md`'s **gap #2, the symbol
registry** — Type-1 symbolic overload, "same symbol, two incompatible
meanings, in two different constructions."

That gap is **live and biting**. It hit twice in this session alone:

- **`A`** — the field normalization in `P52`/`P206`/`P208`, versus the
  body-A subscript in `k_A/c²`. A grep for `A/c²` while answering KG2
  returned the wrong `A` and had to be discarded by hand.
- **`η`** — `P24`'s cross-sector ratio `κ/g`, versus `eta_q` in `NR-013`'s
  beta-profile work. Flagged in passing during the same search.

But `ProvenanceTag` keys on `(symbol, value)` and `has_conflict(symbol)`
means *"multiple values registered for one symbol."* A meaning-collision is
not two competing values of one quantity — it is two quantities sharing a
letter. The registry would read `A = 1.0` (normalization) and
`A = 3.16e14 M☉` (a cluster mass) as a value conflict to adjudicate,
when the correct response is "these are different objects, do not compare."

**Revival condition, concrete:** revive if and only if a symbol registry is
actually built, and note it needs a `namespace`/`meaning` field that
`ProvenanceTag` does not currently have. Adding that field is the real
work; the rest of the machinery (registry, conflict detection, canonical
selection) is reusable as-is.

## 3. What was done

- `src/source_provenance.py` docstring corrected: the backwards arrow, the
  true wiring status, the explicit "do not wire into `provenance_audit`"
  with its reason, and the known non-fit for meaning-collisions.
- No code behaviour changed. No module deleted — both remain tested and
  importable, and their tests keep passing.

## 4. What this does NOT establish

1. **Not that the modules are wrong.** They are unused, not defective;
   their own tests pass.
2. **Not that the symbol-registry gap is closed.** It is open, live, and
   now has two dated instances against it.
3. **Not a judgement on `provenance_audit.py`**, which is live (`E9`,
   `FINDING_E9`) and unaffected by this decision.
