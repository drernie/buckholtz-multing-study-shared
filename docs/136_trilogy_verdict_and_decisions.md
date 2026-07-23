# docs/136 — Trilogy Verdict & Decision Log (Audits 1+2+3)

**Date:** 2026-07-23
**Origin:** user-directed precision pass over docs/133 (Audit 1), docs/134 (Audit 2), docs/135
(Audit 3) after reading each in full — this is the FL Step-10 go/no-go artifact (decision.md
equivalent) and the DDD ADR for this stretch of work.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

## 1. What each audit actually established

| Audit | Verdict | One-line reason |
|---|---|---|
| **1 — C1 closure** (docs/133) | `NEEDS_DATA`, leaning `PIVOT` | The chain {k_A,r_A,D(z),β_d,β_q}→F_d/F_m→H_MULT(z) does not reproduce from public materials — not specified, not reproducible, not independently checkable, blocks Planck/Euclid tests. **This is the main result of the whole trilogy.** Strengthened 2026-07-23: applying TJB's own stated bridge formula to TJB's own Table A1 fails self-consistency by ×4365 at z=8.5 (docs/133 new section, `audit/self_consistency_diagnostic.py`, 2026-06-09 finding re-verified today, hand-recomputed + cross-checked against raw source CSV) — H_MULT also correlates r≈0.9996 with H_FLRW (≈1.074× rescaling, no independent signal) |
| **2 — provenance** (docs/134) | 3/9 safety-critical rows had real prose≠table≠code discrepancies | Systemic risk class, not a frequency estimate (the "33% hit rate" framing was retracted — nine rows were not a random sample) |
| **3a — ΛCDM vs wCDM** (docs/135) | ΛCDM weakly preferred (ΔAIC=+2.0, ΔBIC=+3.3) | w=−0.959±0.464 unconstrained by 27 points; simplicity preference, **not exclusion of wCDM** |
| **3b — R011 reproducibility** | PASS (4-digit match) | Coordinator-reproduced, same implementation. r is a correlation metric, not a full likelihood |
| **3c — MULTING vs ΛCDM, fair footing** | `BLOCKED / NOT TESTED` | Reason: missing C1 closure — not a loss, an unresolved precondition |
| **P0 — nesting invariant** (re-checked this session; **already established** by `null_results/20260713-nr013-r011-beta-profile-nesting.md`, 2026-07-13) | Confirmed, no violation | True global optimum of the 443-cluster correlation objective is β≈0 (monopole); R011's "grid optimum" was a restricted-region optimum, not global — NR-013 proved this 10 days earlier via a closed-form limit; this session's script converged on the same numbers independently and adds one new data point: TJB's own literal Table A1 values (4.5, 18.0) land in the same degraded regime (r=0.6234) |

## 2. Global gate

```
GLOBAL VERDICT: PIVOT + NEEDS_DATA
```
Not `NO-GO` — the missing bridge may exist with the author. Not `GO` — the red curve is not yet a
reproducible prediction. The bottleneck, stated once, precisely:

> **The problem with MULTING right now is not a bad χ² — it is the absence of a well-defined
> H_MULT(z).**

## 3. Decision: push 4 local commits to private archive

```
DECISION: GO
```
Conditions (unchanged, all honored): branch only, no PR, no merge to `master`, no public release,
uncommitted files not swept in.

**Executed 2026-07-23:**
```bash
git status --short                                    # reviewed — untracked files left alone
git diff --check origin/feat/hubble-anchoring-artifact...HEAD   # 0 whitespace errors
git push origin feat/hubble-anchoring-artifact
# 171bb1c..1fa0eae  feat/hubble-anchoring-artifact -> feat/hubble-anchoring-artifact
```
Pushed commits: `7575b35`, `af3d5c4`, `ed86ec7`, `1fa0eae`.

**Status:**
```
PRIVATE RESEARCH ARCHIVE
NOT PUBLICATION-READY
NOT EXTERNALLY VERIFIED
```

**Noted, not actioned (left for a future session, out of current scope):** two stray untracked
items were found during pre-push review and deliberately left untouched — `docs/122_bridge_solution_space.md`
(a numbering collision with the already-tracked `docs/122_bottleneck_synthesis_cosmological_branch_verdict.md`;
different content, an earlier unrelated draft, never committed) and an empty
`experiments/20260713-h1e-agn-feedback-confound/artifacts/.claude/state/` directory. Neither
blocks the push (untracked files are not swept into commits); flagged here so they aren't
mistaken for new work later.

## 4. Decision: TJB letter

```
DECISION: SEND — after cooling-off + one final proofread
```
Final proofread against the 5-point checklist, run this session against the current v8 draft
(`reply_to_TJB_EMAIL_READY.txt`, Desktop):

| Check | Result |
|---|---|
| No excessive length | ✅ PASS — 4 main questions + 2 minor, unchanged from prior review |
| Attachment name/version matches | ✅ PASS — `hubble_anchor_control_comparison.png`, consistent in body sender-notes and Desktop file |
| Does not claim the 27 points are the author's own set | ✅ PASS — explicitly asks "a pointer to the... compilation your legend's count refers to, so I can align it" — flags the uncertainty rather than assuming |
| States solid curves differ only in H0 at the same Ωm | ✅ PASS — "differ only in their adopted H0 anchors" (same flat-ΛCDM shape stated first, so Ωm-equality is implied); the **figure itself** states Ωm=0.317 explicitly in both curve legends (already fixed this session, commit af3d5c4) |
| k_A/c² formula correct | ✅ PASS — "k_A/c² ≈ (3/2) M_A (σ_v/c)² ≈ 5.3×10⁹ M☉", correct grouping, matches this session's [VERIFIED-BASH] number |

**All 5 checks pass. No further edits to the letter text were needed.** Submission Gate status
carried over from the letter's own sender-notes: skeptic pass done (v6), pre-submission checklist
done, text↔figure consistency re-done correctly in v8 (after catching that v7's check was invalid
— see letter's own changelog). **24h cooling-off: still not observed** — this document does not
start or waive that clock; sending remains the user's explicit action, taken separately.

## 5. Post-response branching (unchanged from user's framework, recorded for continuity)

| TJB's reply | Status to assign |
|---|---|
| Supplies formula/code for H_MULT(z) | Run one bounded cycle: exact reproduction → same likelihood → held-out comparison |
| Confirms it's a phenomenological fit, not first-principles | `PHENOMENOLOGICAL FIT / NOT FIRST-PRINCIPLES PREDICTION` |
| Confirms CC data was used in building the curve | `DATA-CONDITIONED RECONSTRUCTION / NOT AN INDEPENDENT TEST OF HUBBLE TENSION` |
| No reproducible bridge provided | `C1 UNRESOLVED / COSMOLOGICAL BRANCH PARKED` |

None of these statuses are applied yet — all four remain open until a reply arrives.

## 6. Explicitly not done this session (per user's list — scope discipline)

Not run: a fourth broad audit · pixel-based w(z) extraction from the chart image · a comparison of
R011's AIC to the CC-likelihood AIC (the exact error Audit 3 itself retracted) · Planck/Euclid
constraint construction · a declaration that MULTING "lost" via the `n/a` cells · any expansion of
numerology pattern search. The only new computation this session was the P0 nesting invariant
test, which was in-scope (resolving Audit 3's own internal question, explicitly requested as the
cheapest, most urgent check) — **though "new" is imprecise: it duplicated `null_results/20260713-nr013-r011-beta-profile-nesting.md`,
which should have been found first via `grep -i nesting null_results/INDEX.md` per the Adaptive
Iteration Branch Rule. Process gap noted for future sessions; both docs/122 and docs/135 now carry
the cross-reference.**

---

*This document supersedes any prior verbal summary of the trilogy's verdict. If docs/133/134/135
and this document ever disagree, this document is authoritative for the consolidated verdict;
each numbered doc remains authoritative for its own detailed working.*
