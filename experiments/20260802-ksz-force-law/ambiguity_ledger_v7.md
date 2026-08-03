# Ambiguity ledger — v6 → v7

Control document for the v7 patch. Eighteen registered ambiguities from the
round-5 static review, each with the two readings, the rule chosen, where it now
lives, and the regression witness that fails if the ambiguity returns.

**v7 adds no method, no derivation and no interpretation.** Where a rule could
not be made unambiguous in prose, it moved into a normative machine-readable
file rather than being reworded.

**Normative files.** `state_machine.yaml` governs terminal states and tie
resolution; `reference_config.yaml` governs constants and library contracts;
`output_schema.json` governs report shapes; `test_vectors.json` holds the
witnesses. `DRAFT_SPEC_v7.md` explains them and does not override them.

Legend: **B** found by both readers · **A**/**B'** found by one.

---

## Number-changing

| ID | Two readings | Chosen rule | Where it lives now | Witness |
|---|---|---|---|---|
| ZERO-01 **B** | case B's accepted bracket end is `mu = 0` and is returned / `mu = 0` is barred as an endpoint so no numeric result exists | `mu = 0` is **evaluated**: `Qobs(0) = Q95(0) = 0` analytically, `acc(0)` is true, no simulation. It may be the left bracket end and `L95 = 0.0` is a permitted result. The contradictory clause "never an endpoint" is withdrawn. | `state_machine.yaml` → `zero_node`, `actions.bisect_zero` | TV01 |
| TIE-01 **B** | the reported argmax takes the smallest index / the largest | **`argmax_left`** — smallest index among all maximisers, applied to every argmax and argmin in the specification | `state_machine.yaml` → `tie_rule` | TV02 |
| IDX-01 **B** | only coarse-grid fits increment the counters / every fit does, with `jj` reinterpreted | counters are indexed by **stage**, not by `jj`: `edge_count[model, rlo, stage, boundary]`. Every fit increments the bucket of its own stage. | `output_schema.json` → item 9 | TV03 |
| EMPTY-01 **B** | an empty retained set yields `NOT_DEFINED` / yields the language's empty-max sentinel | explicit contract: empty → `maxViolation = 0.0`, `violationState = NONE`, `range = [null, null]`, `rangeState = NO_RETAINED_NODES` | `state_machine.yaml` → `empty_set_contract` | TV04 |
| INP-01 **B** | `gcurve` is the `g` column in physical Mpc / the `sqrt(g)` column in h⁻¹Mpc | column 0 is the abscissa in h⁻¹Mpc and is multiplied by `1/hdata`; column 1 is `g`; `numpy.interp` with end-value clamping | `reference_config.yaml` → `inputs.gcurve` | TV05 |
| MASK-01 **B** | MODEL-R's observed state is computed at all eleven `r_lo` / those slots are structural zeros | the array keeps shape `(2, 11, 2)` and gains `observed_valid (2, 11)`. Slots where the model was not run are masked false and must not be read. | `output_schema.json` → item 9 | TV06 |
| PAIR-01 **B'** | excluded nodes are skipped and their neighbours compared / excluded nodes remove both comparisons | **remove both comparisons; the gap is not closed.** The contradicting phrase "consecutive retained nodes" is withdrawn. | `DRAFT_SPEC_v7.md` §9, single statement | TV07 |
| QUAD-01 **B'** | the quadrature is any adaptive Gauss–Kronrod / a specific routine | `scipy.integrate.quad` with `epsabs`, `epsrel`, `limit=200`, `full_output=1`, `points` given by rule. Non-convergence is `ier != 0 or abserr > max(epsabs, epsrel·|result|)`. | `reference_config.yaml` → `libraries.quadrature` | TV08 |
| CTRL-03 **B'** | control 5's second-named quantity is the comparison target, making it `Kraw3` vs `Kw3` / each kernel is compared with its own recomputation | each kernel against its own 1e-12 recomputation; the row now names both operand pairs explicitly, so §12.0's "second-named" rule no longer applies to it | `DRAFT_SPEC_v7.md` §12 control 5 | TV09 |
| RNG-01 **B'** | the coverage threshold reuses §10's `rootCal` value / is recomputed under `rootVal` | recomputed under `rootVal`, `keyStage = 0`, `nsim = 100000`. The study owns its threshold. | `reference_config.yaml` → `seeds`; `DRAFT_SPEC_v7.md` §13 | TV10 |

## Report-changing

| ID | Two readings | Chosen rule | Where it lives now | Witness |
|---|---|---|---|---|
| TERM-01 **B** | `INVALID_INPUT` and `NUMERICAL_FAILURE` suppress what `STOP_RUN` suppresses / suppress only what was not yet computed | all three suppress the same set: items 1–7, 9, 10, 12 absent; 8, 11, 13 present | `state_machine.yaml` → `terminal_verbs` | TV11 |
| CTRL-02 **A** | a terminal verb halts the control sequence / all nine controls run first | **all nine controls run to completion and emit their values before any terminal verb is honoured**, so item 8 is always complete | `state_machine.yaml` → `control_completion` | TV12 |
| CTRL-01 **B** | controls 5 and 6 emit one pooled value / one per compared pair | control 5 emits 2, control 6 emits 4; the verdict is taken on the maximum | `output_schema.json` → item 8; `DRAFT_SPEC_v7.md` §12 | TV13 |
| LIST-01 **A** | one excluded-node list / two, for range and for monotonicity | two lists: `excluded_from_range` and `excluded_from_monotonicity` | `output_schema.json` → item 3 | TV14 |
| ANNO-01 **A** | the annotations are emitted with the outputs / they are document prose only | annotations are **report fields**, never outcome labels, never members of item 11 | `output_schema.json` → `annotations` | TV15 |
| SHAPE-01 **A** | non-numeric slots hold `NaN` with labels elsewhere / the arrays hold labels in place | float64 value arrays with `NaN`, plus a parallel `state` array of strings. A label is never stored in a float array. | `output_schema.json` → items 3, 4, 10 | TV16 |
| ORDER-01 **A** | row order and row count are the implementer's choice / fixed | fixed: branch table `primary, 1, 2, 3, 4`; `rlo` axis `kk = 0..9` then `6.0` at index 10; `acc` has 16 rows and the §14 run is not one of them | `output_schema.json` → axes, items 10, 12 | TV17 |
| BRANCH-01 **B'** | a branch with no numeric `L95` is dropped from the table / keeps its row | keeps its row; `STOP_BRANCH` puts the state label in place of `L95` and `SdMC`; the table is always 5 rows | `state_machine.yaml` → `terminal_verbs.STOP_BRANCH`; `output_schema.json` → item 10 | TV18 |

---

## Dismissed — not an ambiguity

| Finding | Why it does not block |
|---|---|
| control 6 versus guard G2 (reader 10, B10) | The control table carries an explicit **Verb on failure** column reading `STOP_RUN PV_EPSILON_SENSITIVE`, which contradicts the alternative reading. Applying the gate's own escape clause, it is not blocking. Reader 9 reached the same conclusion independently. |

## Deferred — would change what is computed

| ID | Item | Why deferred |
|---|---|---|
| DEF-01 | whether the KDE belongs in the frozen core at all | removing it is a method change |
| DEF-02 | whether the `L95(r_lo)` curve stays the primary deliverable | changes the estimand; open for the supervisor |
| DEF-03 | control 4 has no threshold, so the Hartlap premise cannot fail | adding one changes behaviour |

---

## Terminal-state edits — reachable states after the edit

Three versions in a row broke because a repair to a terminal-state rule created
a state the repaired rule did not cover. Every terminal-state edit in v7
therefore carries an enumeration of what the edited rule can now reach, and the
enumeration is checked mechanically rather than asserted.

| Edit | States reachable after it |
|---|---|
| ZERO-01: `acc(0)` is true by evaluation, not by assumption | `RANGE_INSUFFICIENT`, `FINITE_LIMIT_NEAR_ZERO`, `FINITE_LIMIT`, `FINITE_LIMIT_MULTICROSS` — and **no others**, proven by exhaustive enumeration |
| the four-way classification replacing v6's A/B/C/D | same four; v6's `NO_FALLING_TRANSITION` becomes **unreachable by construction**, because a vector that starts true and ends false must contain a falling transition |
| `STOP_BRANCH` gains a raising condition | branch rows are always present; the table is always 5 rows |

**Mechanical check.** `spec_gate.py` enumerates every acceptance vector of
length 2…15 with `acc(0)` true — 32 766 vectors — and classifies each twice, by
two independently written interpreters: one that walks `state_machine.yaml` as
data, one written by hand from the transition table. Both must agree, every
vector must receive exactly one state, and all four states must be reached.
This replaces the prose assertion of totality that v6 made and that round 5
falsified.
