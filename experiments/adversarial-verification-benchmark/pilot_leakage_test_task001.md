# Pilot Leakage Test — task_001 (2026-09-01)

**Purpose:** Verification item 1 of the benchmark plan
(`Plan: Adversarial Verification Methodology — Benchmark Research
Program`) — test whether a real Tier A task, run through a real
`Agent` call under this session's actual working directory, leaks
project-local or harness-level context that would contaminate a
solving agent's judgment beyond what the public task file itself
contains.

**Setup:** dispatched a `general-purpose` Agent with (1) task_001's
full public content verbatim (materials-science lattice-ratio
coincidence, Tier A / docs/146 Category 2 shape), (2) the baseline
arm's minimal system-prompt-equivalent instruction ("analyze this and
report findings"), (3) a follow-up instruction, in the same call, to
introspect exhaustively on any ambient project-specific knowledge,
file, or methodology it could see that was not in the prompt itself.
No worktree isolation was used — cwd was this session's actual cwd
(`.../buckholtz-idm-multing-mvp/experiments/adversarial-verification-
benchmark/corpus`), nested inside the repo tree — the worst case for
project-local leakage, chosen deliberately to stress-test the risk
named in the plan's Phase D.

## Result 1 — Task-level review (not the leakage question, but the
control that shows the agent engaged honestly with the content)

The agent correctly identified the task's real defect (post-hoc
numerology: the "volume-weighted average radius" mechanism was fitted
to the target ratio, not derived independently; the mechanism's own
claimed comparison value is never computed; measurement-uncertainty
argument is backwards; missing look-elsewhere accounting for how many
alloys/ratios were scanned) — this matches the answer key's intended
defect (Category 2, tautological/post-hoc mechanism) closely, though
via its own reasoning rather than by reciting the taxonomy name. It
also caught a genuine arithmetic inconsistency in the task's own
numbers (5.9412/3.6368 = 1.633634, not the stated 1.63398) that was
not a deliberately seeded feature of the task — noted here for corpus
maintenance, not as a leakage finding.

## Result 2 — Ambient context check (the actual leakage question)

**Project-local channels — clean.** The agent was asked explicitly to
name `docs/146`, `activeContext.md`, or any Buckholtz/MULTING/IDM
project fact, and explicitly reported: no reference to a file named
`docs/146` anywhere in its context; no use of any Buckholtz-specific
fact (no TJB correspondence, no Eq.32/MULTING physics, no cosmology
numbers) anywhere in its task_001 review. It correctly refused to
imply `docs/146` exists when it could not find it — citing the loaded
integrity rules' own phantom-source prohibition as the reason.

**Global-harness channel — confirmed leakage, methodological only.**
The agent reported the full text of the user's global `~/.claude/
CLAUDE.md` and all always-on rule files
(`artifact-provenance-gates.md`, `falsification-ladder.md`,
`estimand-ops.md`, `integrity.md`, `memory-protocol.md`,
`mentor-protocol.md`, `pearl_registry/INDEX.md`, `perelman-audit.md`,
`permissions.md`, `rationalizations.md`, `research-methodology.md`,
`security.md`, `skeptic-triggers.md`) as present in its context,
regardless of the minimal system prompt given. It also reported the
project-specific auto-memory file (`MEMORY.md`) in full, and
environment metadata (cwd, git status, a recent commit message).

Critically: `artifact-provenance-gates.md`'s own header states it was
"extracted from a single failure mode observed end-to-end on
2026-08-03 (Buckholtz/MULTING bridge audit)," and its Gate 2 ("Target
Provenance": prediction vs. fit vs. illustration) is the generalized
form of exactly the failure category task_001 encodes (Category 2,
post-hoc numerology / fitted-not-derived mechanism). The agent's own
self-report: it used no Buckholtz-specific *facts* as evidence in the
task_001 review, but its critique's *shape* (target-provenance
framing, positive-control/sibling-sample demand, "too-exact-at-the-
anchor" suspicion, look-elsewhere accounting) was "directly primed by"
that file.

## Interpretation

This is a different and more structural leakage channel than the two
found earlier in this session (`SubagentStart` hook injecting
`activeContext.md`; `MEMORY.md` project-scoped auto-memory) — both of
those are project-local and were mitigatable (worktree isolation,
temporary hook disable). This channel is harness-level: global
`CLAUDE.md` + always-on rules load into every `agent()` call tied to
the user's home directory, independent of cwd, worktree isolation, or
system prompt content. It cannot be suppressed by any mitigation
available to this benchmark's design.

**Consequence for the study design:** a genuinely "rules-free"
baseline arm, as originally specified in Phase C, is not achievable in
this environment. Per the user's explicit decision (2026-09-01,
AskUserQuestion: "Reframe both arms honestly"), Phase C's arm
definitions were revised in the plan file — baseline is now defined as
"ambient-default (global rules loaded, but not explicitly instructed
to invoke them)" vs. treatment "ambient-default plus an explicit
instruction to run the full FL protocol including a skeptic
sub-call." This is a real, defensible contrast, but narrower than
originally framed, and `result_summary.md` must state this explicitly
alongside every headline result.

## What this pilot does NOT establish

- Does not establish that Run 2's actual worktree-isolated execution
  (per Phase D) will behave identically to this un-isolated pilot —
  project-local isolation is still worth keeping as defense-in-depth
  even though this pilot found that channel already clean without it.
- Does not establish the magnitude of the global-rules priming effect
  on detection rate — only that it exists and is methodological, not
  factual. The benchmark's own headline comparison (Phase F/G) is the
  actual measurement of whatever residual effect explicit protocol
  instruction adds on top of this ambient baseline.
- Single pilot task (n=1), one domain (materials science / Category 2
  shape). Not a claim that every Tier A task would show the identical
  pattern — the corpus sanity check (Verification item 3) and the
  full N=32 run are still required.
