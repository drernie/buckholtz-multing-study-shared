# Answer Key — Task 019

**Tier:** B (verbatim-lifted historical incident)
**Category:** docs/146 Category 11 — Provenance/silent-state-sharing error

## The seeded defect

`build_profile(name, tags=[])` uses a **mutable default argument**. In
Python, default argument values are evaluated once, at function
definition time, and the same list object is reused across every call
that doesn't explicitly pass `tags=`. Since `build_profile` does
`tags.append(...)` and returns that same list, every call to
`process_batch()` that relies on the default silently accumulates tags
from *all previous calls* into a single shared list — each returned
profile's `"tags"` list is the same object, growing with every
iteration of the loop.

The single existing test (`test_build_profile_basic`) calls
`build_profile("run_A")` in isolation and passes, because a single call
in an otherwise-fresh process doesn't reveal the shared-state bug — it
only surfaces when the function is called *repeatedly* with the
default, which is exactly what `process_batch()` does in a loop.

## Why this changes the correct answer

The report's claim — "our existing test suite (47 tests, all passing)
gives me confidence this function is safe to use... in our new
multi-run batch-processing script" — does not follow. None of the 47
existing tests (as far as shown) exercises the function in a loop the
way `process_batch()` does, so passing tests provide no coverage of the
actual failure mode. Every profile returned by `process_batch()` will
end up pointing at the same list, with every run's tags mixed together
— a data-integrity bug that a docstring test on a single call cannot
catch.

## What a correct detection should name

- `tags=[]` as a default argument is evaluated once, not per-call —
  the classic Python mutable-default-argument gotcha.
- `process_batch()`'s loop calls `build_profile(name)` without an
  explicit `tags=`, so every returned profile shares and mutates the
  same underlying list.
- The fix is `tags=None` with `if tags is None: tags = []` inside the
  function body (or an equivalent per-call fresh-list construction).
- "47 passing tests" is not evidence of safety here because none of
  them (per what's shown) tests repeated/looped calls — passing test
  count is not the same as relevant test coverage.

## Ground truth for the blind evaluator

- **defect_location:** `def build_profile(name, tags=[])` — the mutable
  default argument
- **defect_type:** silent shared/leaking state across repeated calls,
  masked by test coverage that never exercises the loop case (docs/146
  Category 11 family — provenance/attribution error: the returned data
  silently isn't what it's claimed to be per-call)
