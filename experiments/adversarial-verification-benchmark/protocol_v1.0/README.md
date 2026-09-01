# Protocol v1.0 — frozen snapshot

**Frozen:** 2026-09-01
**Purpose:** per the benchmark plan's Phase A — the treatment arm's
protocol must not silently drift mid-benchmark if the live global rules
change. These are byte-for-byte copies (not symlinks, not references) of
the source files as they existed on 2026-09-01, with SHA-256 hashes for
provenance. If any live source file is edited later, this snapshot is
what the treatment arm actually used — not the current live version.

## Files and provenance

| File | Source (live path) | SHA-256 |
|---|---|---|
| `falsification-ladder.md` | `~/.claude/rules/falsification-ladder.md` | `e498090ec6229836a7a3000ee07d1fc593165f5692baab21b90a54d2fe91bab1` |
| `oracle-adequacy-gate.md` | `~/.claude/docs/oracle-adequacy-gate.md` | `478896b1b9a056a6874a1b05d77fd6356fb4fef88c240b2889a0e666459104d8` |
| `146_failure_mode_taxonomy.md` | `buckholtz-idm-multing-mvp/docs/146_failure_mode_taxonomy.md` | `a399a3dd1faf0d81b7bd7733dbc5bd32532a1e632743cf05b98ba07b87d73464` |
| `sci-code-audit_SKILL.md` | `~/.claude/skills/sci-code-audit/SKILL.md` | `99008efe0368d41bac9b3ed1694256f7fa7a780dbc86f8a0315f3b6ccafb8390` |
| `ab-test_SKILL.md` | `~/.claude/skills/ab-test/SKILL.md` | `916098581bb2b4c86f25bbabb87969d75e9cde2240a717ce11a6dabd69f0577c` |

## What "the treatment protocol" means, operationally

The treatment arm is instructed to run the FL Standard-Ladder sequence
from `falsification-ladder.md` (estimand → claim.md → positive/negative
controls → stress test → Step 8a context-blind skeptic sub-call, fresh
context → decision.md), using `146_failure_mode_taxonomy.md` and
`sci-code-audit_SKILL.md`'s Artifact Zoo as the checklist of failure
modes to actively check for (not shown the specific seeded defect —
Builder Blindness applies to the corpus, not to this general-purpose
checklist). `oracle-adequacy-gate.md` is used separately, in Phase E, to
audit the benchmark's own blind evaluator — not part of what the
treatment arm itself runs.

The baseline arm receives none of these five files, per the plan's
Phase C table.

## Non-goals

This snapshot does not modify, supersede, or fork the live global rules
— `~/.claude/rules/falsification-ladder.md` etc. remain exactly as they
are for every other project. This copy exists solely so the benchmark's
own result_summary.md can honestly state which exact version of the
protocol produced a given result, per this project's own no-silent-drift
discipline.
