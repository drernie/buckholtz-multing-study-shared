# PARKED — T5/T6: does any cogenesis mechanism produce IDM's exact
# 5-identical-sector structure?

**ID:** T5T6-cogenesis
**Date parked (formally indexed):** 2026-09-08. **Underlying work:**
2026-07-22 — this entry closes a citation/indexing gap
(`/research-audit` process-gap scan, `/boyko-why-ladder` Chain D, both
2026-09-08), it is not new physics.
**Verdict:** ARCHIVE (**OPEN**, per the source file's own explicit word —
**not** REJECT, and not falsified). Corrects two same-day
mischaracterizations: this project's own `activeContext`-derived synthesis
and an external pasted analysis both called this "REJECT" or
"REJECT-leaning" without re-reading the primary source's own final verdict
line.
**Source:** `docs/132_open_bottlenecks_task_backlog.md:125-162` (T5, T6,
and the corrected T5.1+T6.1 joint verdict — read directly, verbatim, not
paraphrased, before this file was written).

## The question

Does any known cogenesis/reheating mechanism produce IDM's specific
postulated structure — **five identical dark sectors, each independently
at `n_i/n_b≈1`** — the assumption `Ω_DM/Ω_b = 5×1.074 ≈ 5.36` needs to read
as a real relic prediction rather than tuned arithmetic?

## What was found

**T5 alone** (2026-07-22): hitting `5.36` needs `n_i/n_b=1` to `~1.2%` per
sector with no mechanism in the corpus; mirror-DM/ADM derives the same
5:1 via a competing, unrelated structure. Leaned REJECT in isolation.

**T6 alone** (2026-07-22): thermalized 5-isomer dark neutrinos are excluded
by a real factor `~50` against Planck `ΔN_eff`; early-decoupling and
gravity-only escapes remain open.

**T5↔T6 "coupled" framing — CORRECTED, same day.** The original claim
that the `ΔN_eff` escape and the `n_i/n_b≈1` structure are mutually
exclusive is a **false dichotomy**: a published mechanism class
(decaying-"reheaton" cogenesis into multiple sectors, Easa, Gregoire,
Stolarski & Cosme, *Phys. Rev. D* 109, 075003, arXiv:2206.11314)
transfers a shared asymmetry to several sectors without full thermal
equilibration (`ξ=T_dark/T_SM≲0.35` suffices — `[VERIFIED-BASH]`, toy
calc `scripts/t5t6_cogenesis_estimate.py`), so `ΔN_eff`-safety and
definite per-sector densities **can** coexist in one model.

**But this does not rescue IDM's specific postulate.** No surveyed
mechanism — thermal, non-thermal, or transfer-based — produces IDM's
exact structure. Known constructions reach a comparable *total* ratio
through *different* internal structure (unequal sectors via differential
decoupling, or a few components via conversions), not five equal
densities. **Net: the 5:1 match remains a posited coincidence under every
known cogenesis history checked — for a sharper reason than the original
coupling argument** (no known mechanism reaches the specific
five-equal-sector structure at all, independent of the `ΔN_eff` escape
question). Skeptic-reviewed: **`WEAKENED`, no claim falsified** — the
false-dichotomy sentence was corrected, the underlying "no mechanism
found" conclusion survived.

## Provenance — separated explicitly, per this file's own no-silent-gap discipline

`docs/132` cites `boyko_T5_report.md`, `boyko_T6_report.md`, and
`boyko_T5_T6_cogenesis.md` as the human-readable rationale artifacts.
**`find . -iname "boyko_T*"` returns zero files** (`/research-audit`,
2026-09-08). `git log -S"boyko_T"` traces this to commit `26499de`'s own
message: *"Reports in session scratchpad (boyko_T*_report.md + summary)"*
— written to a session scratchpad, never committed to this repository.

```
RESULT:            exists, reproducible — scripts/t5t6_cogenesis_estimate.py,
                    scripts/t5_relic_abundance.py, scripts/t6_neff_honest.py
                    are all present and runnable in this repo.
HUMAN-READABLE
RATIONALE:          MISSING — session-only artifact, not preserved.
PROVENANCE:         INCOMPLETE — the numeric result survives; the full
                    reasoning chain that produced docs/132's own prose
                    summary above does not exist as a re-readable file.
```

This is stated explicitly, per the same discipline
`artifact-provenance-gates.md` Gate 1 already requires elsewhere in this
project: **a result existing is not the same claim as its evidentiary
chain being preserved.** The summary in `docs/132` itself is trusted here
as `[INFERRED]` (a session's own contemporaneous prose record, close to
the event — see `falsification-ladder.md`'s Hindsight Distortion Gap
Heuristic), not re-derived from scratch in this parking pass.

## Why parked rather than pursued further

This is a `contingent`, not `hard_killed`, non-result — no mechanism found
does not mean no mechanism exists. The natural next move (surveying more
cogenesis literature, or asking TJB for an isomer-level relic derivation)
is a real research direction but not currently prioritized against the
project's other open threads (`docs/147`).

## Revival Condition (measurable)

**(a)** TJB supplies an isomer-level relic-abundance derivation for the
5-isomer IDM structure specifically (not a general cogenesis argument);
**OR**

**(b)** A published cogenesis/reheating mechanism is found that reaches
**five identical, independently-equal-density** dark sectors (not merely
a comparable total ratio via unequal-sector structure) — the specific gap
this file's own search did not close.

## What is explicitly NOT claimed by parking this

1. Not that the 5:1 numerical match itself is wrong — it remains a real,
   unexplained coincidence, same status as Eq.32's own 0.0135% match.
2. Not that cogenesis mechanisms in general are ruled out for IDM — only
   that none surveyed reaches the *specific* five-equal-sector structure.
3. Not a re-verification of `docs/132`'s own arithmetic — this file
   consolidates and indexes an existing, dated result; it does not
   re-derive it.
4. `NO_AUTHOR_ERROR`.

## Cross-references added by this entry

- `docs/114_o7_isomer_ratio_lock.md` (O7 gate, 2026-06-13) predates this
  finding and does not cite it — its own `REJECTED_AS_DERIVATION` verdict
  should be read alongside this file's sharper, later reason (specific
  five-equal-sector structure, not merely "missing mechanisms" in
  general).
- `null_results/INDEX.md` `NR-007` (`docs/114`'s registry entry) — same
  cross-reference gap, same fix.
