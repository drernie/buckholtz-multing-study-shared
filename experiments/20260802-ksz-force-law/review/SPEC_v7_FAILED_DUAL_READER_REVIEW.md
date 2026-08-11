**[MAJOR CORRECTION, added later the same session, 2026-08-11] The headline
verdict below (NOT TIGHT, 20 blocking findings) is SUBSTANTIALLY OVERSTATED
— a scoping error, not a spec defect.** This review's own second-reader
prompt explicitly excluded "any prose spec" from context, modeled on
falsification-ladder.md's Context Asymmetry Rule. That rule is about hiding
a BUILDER's post-hoc reasoning chain from a skeptic — it does not apply to
a SPECIFICATION's own definitional text. `DRAFT_SPEC_v7.md`'s own Appendix
says plainly: "Two independent readers answer these from **this document
and the four normative files**" — the spec text and the 4 files are meant
to be read together, by design. Worse: `DRAFT_SPEC_v7.md` itself says "As
v6" for nearly every substantive section (§2-15), meaning the base
definitions live in `DRAFT_SPEC_v6.md` (620 lines), which this review did
not read at all.

Reading `DRAFT_SPEC_v6.md` directly (same session, after this file was
first written) found EXACT, complete definitions for every item this review
called "undefined anywhere":

- **A1** (RNG seed derivation): `DRAFT_SPEC_v6.md` §8, verbatim —
  `rng = numpy.random.default_rng(numpy.random.SeedSequence(entropy=
  rootUsed.entropy, spawn_key=key))`, `key = (keyModel, keyRlo, keyMu,
  keyStage, keyStep)`. **RESOLVED, not a gap.**
- **A2** (`keyModel`/`keyRlo` mappings): same §8 — `keyModel: 0=MODEL-W,
  1=MODEL-R`; `keyRlo: kk in 0..9 for a grid node, 100 for r_lo=6.0`.
  **RESOLVED.**
- **A3** (`keyStep` outside bisection): same §8 — `keyStep: 0 everywhere
  except keyStage=3 (bisection), where it is the 1-based iteration number`.
  **RESOLVED.**
- **A4** (branch identity not keyed): same §8, explicit — "Branches share
  the primary's streams. `key` contains no branch field, so at a given node
  every branch of §11 consumes the same underlying stream as the primary."
  This IS this review's own "reading (b)", confirmed as the intended one,
  not left open. **RESOLVED.**
- **A5** (`sdmc_contract` undefined): `DRAFT_SPEC_v6.md` §10, lines
  ~397-423 — the FULL `SdMC`/`sq`/`dens`/KDE-bandwidth (`hkde`) formula,
  including the `iqr=0` fallback and the `1e-9` floor. **RESOLVED.**
- **A6** (`Qobs, Q95, Qstat, muhat, Chi2, Cand, mu1, muzero, Kw2, Kw3,
  Kraw2, Kraw3` undefined): all exactly defined — `Qstat`/`Chi2`/`muhat`/
  `Cand`/`mu1`/`muzero` in §7, `Kw*`/`Kraw*` in §5, `Q95`/`Qobs` context in
  §8/§10. **RESOLVED.**
- **A7** (4 of 9 controls missing tolerance): `DRAFT_SPEC_v6.md` §12.1 gives
  a full 9-row table. Controls 3, 4, 9 are correctly REPORT-ONLY BY DESIGN
  ("verb on failure: none") — they were never meant to carry a pass/fail
  tolerance, so their "missing tolerance" is not a gap. Control 8 uses
  "exact float64 equality" as its criterion, not a `Drel` tolerance —
  also by design, also not a gap. **RESOLVED, and the original framing
  ("missing tolerance" as if every control needs one) was itself wrong.**

Spot-checked one Tier-B finding too: **B6** (bin structure, edges vs
centers) assumed bins are CONSTRUCTED via a spacing rule. They are not —
`DRAFT_SPEC_v6.md` §7 says bins are SELECTED from `dr6.hdf`'s own existing
`r_mp` field wherever `25 ≤ r_mp ≤ 225`, with a hard requirement of exactly
15. There is no spacing rule to specify because there is no construction
step. **RESOLVED, finding was based on a wrong premise.**

Direct confirmation the 4 files genuinely don't restate these formulas
(so this is not "I missed it in the files either"): `grep -c "Chi2\b"`
`reference_config.yaml` = 1, `state_machine.yaml` = 4 — all NAME the
symbols (for schema/gating purposes) without restating their formulas,
exactly as the project's own header table promises (`reference_config.yaml`
governs "every constant... and its options", not the underlying math).

**Given this, tier A (7 of 20 findings) is now believed largely or entirely
FALSE-POSITIVE, and tier B/C/D's true residual size is unknown** — this
correction spot-checked only 1 of 13 remaining findings. A properly-scoped
second-reader pass (spec text `+` 4 files, per the appendix's own
instruction) was launched immediately after this was discovered; its result
supersedes both this file's original verdict and this correction note. If
you are reading this file rather than a newer one, check for a follow-up
review file before trusting either.

---

**[Superseded correction from earlier the same session, kept for the audit
trail, itself narrower than the one above]** Reading
`PARK_v7_awaiting_second_reader.md` (which this review did NOT have access
to at write time, by design — context asymmetry) after the fact surfaced
two things this file should say plainly, not bury:

1. **This reader does not satisfy the revival condition on file.**
   `PARK_v7_awaiting_second_reader.md`'s own Independent Verification
   Strength Ladder table rates "same model, isolated context" as
   **Weak–Medium** — explicitly below "different model" and
   "independently-written implementation", which are the two conditions
   actually named as sufficient to resume. `Agent(skeptic)` run as this
   review's second reader is the SAME tier as the ROUND6 skeptic run
   already on file (which found only LABELS-01) — not a genuinely
   independent reader in the sense this track's own gate structure
   requires. The 20 findings below are real (3/3 spot-checked against the
   files directly) and DO block `BLIND_C` on their own evidentiary merit —
   but they do not, by themselves, satisfy "DUAL_READER_REVIEW passed" OR
   let this track claim a proper second reading has now happened. A
   genuinely different-tier reader is still needed after these findings are
   fixed.
2. **No reference implementation of v7's specific `SeedSequence`-keyed
   scheme exists to ground a fix.** The actual scripts that produced the
   already-replicated kSZ result (`task1_full_kernel_refit.py`,
   `task3_xi_covariance.py`, `task345_stats.py`, `recheck_onesided.py`,
   `gate1_fine_coverage.py`) all use a single fixed `np.random.default_rng(
   <one int>)` call — none implement `key_fields`, `rootCal/rootVal/
   rootDual`, or a `SeedSequence`-based per-node derivation, and grepping
   all of them for `Qobs`/`Q95` returns zero hits. `v7`'s elaborate keyed-
   seeding formalism is a SEPARATE, more rigorous specification effort that
   was never implemented against real code — meaning the 7-item fix list
   below cannot be filled in by extracting conventions from existing code;
   each item would have to be AUTHORED from scratch. Given this session's
   own repeated rule against hand-deriving technical constructions under
   time pressure (see the NCG thread's identical caution about the
   Spin(8) triality formula), that authorship is explicitly NOT attempted
   in this round — recorded as the honest stopping point, not silently
   skipped.

---

# Spec v7 — DUAL_READER_REVIEW, second reader — FAILED (2026-08-11)

**Context asymmetry (per falsification-ladder.md § Context Asymmetry Rule):**
this reader was given ONLY `state_machine.yaml`, `reference_config.yaml`,
`output_schema.json`, `test_vectors.json` — no `review/` folder, no prose
`DRAFT_SPEC_v7.md`, no git history, no ROUND6's own findings. ROUND6's own
"Recommended next transition" explicitly required this: *"the transition is
not satisfied by a single reader... this reader has now seen the spec and
cannot serve as the second."*

**Verdict framing (the reader's own scope statement):** *"can two independent
implementations produce bit-identical output on every declared test vector,
working from ONLY these four files — I am not judging whether the underlying
science is right."*

---

## Result: NOT TIGHT

20 blocking findings across 3 tiers. Independently spot-checked against the
actual files before recording here (per audit-verification-gate.md): 3/3
checked claims confirmed —

- **A1** (RNG seed derivation unspecified): `reference_config.yaml` `seeds:`
  block (lines 112-118) names `rootCal/rootVal/rootDual` and `key_fields`
  but never states how the root and the key tuple combine into a
  `SeedSequence`. **Confirmed by direct read.**
- **A5** (`sdmc_contract` invoked, never defined): grepped both normative
  files — 3 references in `state_machine.yaml` (lines 73, 81, 89), zero
  definitions anywhere. **Confirmed by direct read.**
- **A7** (controls 3, 4, 8, 9 have no tolerance): `tolerances:` block (lines
  120-132) lists `control_1, 2, 5, 6, 7` only. **Confirmed by direct read.**

Given 3/3 spot-checks confirmed and the report's own citation discipline
(every claim tagged `[ФАКТ]` with an exact file:key path, every ambiguity
given ≥2 concrete readings and a reachability argument), the remaining 17
findings are recorded here as reported, not independently re-verified one
by one — consistent with this project's spot-check escalation rule (verify
3, and only re-verify everything if any of the 3 fail).

## Why this overturns ROUND6's "0 problems"

`spec_gate.py`'s 10 checks (all PASS, confirmed live 2026-08-11 before this
review was commissioned) verify **internal consistency of the four files
against each other** — state-machine reachability, hash agreement, no
undefined terminal states, etc. They do **not** check whether the four files
are **self-contained enough for an independent implementer to compute a
single number**. This review found they are not: `Qobs, Q95, Qstat, muhat,
Chi2, Cand, Kw2, Kw3, Kraw2, Kraw3, mu1, muzero, mu1_in_range` are all named
in the schema/state-machine but defined nowhere in the four-file bundle —
`state_machine.yaml`'s own line 2 says prose (`DRAFT_SPEC_v7.md`) governs
where it's not in these files, and prose was deliberately excluded from this
reader's context by the DUAL_READER_REVIEW protocol itself.

**`spec_gate.py` PASS is real and does not need re-litigating** — it answers
a different, narrower question than DUAL_READER_REVIEW asks.

## Blocking findings (plain list, full detail in the reader's own report — see below)

1. RNG seed derivation from `key_fields` unspecified (A1)
2. `keyModel`/`keyRlo` (grid) integer mappings unspecified (A2)
3. `keyStep` undefined for coarse/refined/coverage stages (A3)
4. Branch identity not in `key_fields` despite branch-conditional RNG use (A4)
5. `sdmc_contract` invoked, never defined (A5)
6. Core operators (`Qobs, Q95, Qstat, muhat, Chi2, Cand, Kw*, Kraw*, mu1,
   muzero, mu1_in_range`) named, not defined, in these four files (A6)
7. 9 controls' semantics undefined; tolerances missing for controls 3,4,8,9 (A7)
8. `refined` grid boundary containment at 0.05-multiple `jlast` endpoints (B1)
9. `argmax of Qobs over acceptance grid` domain ambiguous with interior rejections (B2)
10. `range` field `float64`+`nullable` vs TV04's literal `[null,null]` (B3)
11. `L95_rule` — "linear interpolation" doesn't name the root-of-linear-interp construction (B5)
12. Bin structure (15 bins, [25,225] Mpc) — edges vs centers, spacing unspecified (B6)
13. `coverage.verdict` PASS/FAIL rule and `band` construction unspecified (B7)
14. `dual_unit.verdict` LABELS_ONLY trigger unspecified (B8)
15. `p_value` formula for item 6 unspecified (B9)
16. `excluded_from_range`/`excluded_from_monotonicity` population rules unspecified (B10)
17. Monotonicity pair-generation rule only inferrable from TV07's forced count (B11)
18. `numpy.quantile` `q` parameter not stated in the quantile block (D4)
19. Cubic-spline `outside_range: 0.0` not resolvable to a scipy argument as written (D5)
20. Bisection at `max_iterations` without convergence — no exit behavior (D1)

## What DOES survive (fair-minded, checked by the reader against its own criticisms)

State-machine classification skeleton (S1-S4 exhaustive on `acc(600) x |P| x
|F|`), tie_rule `argmax_left`, empty-set contract enumeration, the
`labels_emitted` byte-sort metamorphic contract (TV22), and all arithmetic
in TV01/TV02/TV03/TV19/TV21 — all independently re-derived by the reader and
confirmed PASS.

## Recommended next transition

```
DRAFT_v7 -> LOCAL_STATIC_LINT [PASS] -> SPEC_GATE [PASS] -> DUAL_READER_REVIEW [FAIL, this file]
```

Per ROUND6's own standing stop rule and this project's Substrate Gate
discipline: a `FAIL` here is not evidence about the underlying kSZ force-law
constraint (`ℓ_d` limits already CROSS-IMPLEMENTATION-REPLICATED, per
facts.json R011) — it is a finding about whether the SPEC ITSELF can be
independently re-executed byte-for-byte, a prerequisite for `BLIND_C` that
has not yet been met. Does not block or weaken the existing statistical
result; blocks only the next verification stage (`BLIND_C`, a true blind
reproduction against a frozen spec).

**Fix required before re-attempting DUAL_READER_REVIEW:** the 7-item list at
the end of the reader's full report — (i) seed-derivation pseudocode, (ii)
explicit `keyModel`/`keyRlo` tables, (iii) `keyStep` per stage, (iv)
`keyBranch` in `key_fields` or an explicit non-keyed clause, (v) an
`sdmc_contract` block, (vi) import or hash-pin the operator definitions
currently only in prose, (vii) a `controls` block with definitions and
tolerances for all nine controls.

**Full 20-finding report (verbatim reader output, all evidence citations):**
kept in this session's task transcript; condensed into the list above for
the repo record. Re-run the second-reader Agent prompt in
`.claude/memory/activeContext.md`'s 2026-08-11 entry if the full text is
needed again.
