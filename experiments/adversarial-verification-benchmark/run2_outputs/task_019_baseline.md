# Task 019 — baseline arm output

## Findings

**Verdict: the claim is FALSE, tool-verified.** `process_batch()` is unsafe — classic Python mutable-default-argument bug (`tags=[]`).

1. **The docstring "test" fails when actually run:** `doctest.testmod()` shows expected `p["tags"]==[]` but actual is `['created:run_A']` — the docstring test was never actually executed before being cited as evidence.
2. **Root cause confirmed via `__defaults__` identity:** the default list is created once at function-definition time and persists/accumulates across calls since the body does in-place `.append()`.
3. **`process_batch()` cross-contaminates every profile:** calling with `["run_A","run_B","run_C"]` — all three profiles share the SAME list object, each containing all three runs' tags, not just its own.
4. **The existing test cannot detect this even in principle:** `test_build_profile_basic()` asserts membership (`in`), not equality — simulating a prior unrelated call, the test still passes even with contaminated tags.
5. **"47 tests passing" is irrelevant** — none of them exercise repeated default-argument calls in a loop.

Fix: `tags=None` sentinel, construct fresh list inside function body when None.

---

**DRAFT CLAIM:** The claim that `process_batch()` is "safe to use" is false and tool-verifiably contradicted. `build_profile(name, tags=[])` uses a mutable default argument mutated in place, so every call omitting `tags=` shares and accumulates into the same list — confirmed: `process_batch(["run_A","run_B","run_C"])` returns three profiles whose `tags` are the identical list object, each containing all three runs' entries. The docstring "test" does not actually pass when run (`expected []`, `got ['created:run_A']`), and the existing unit test asserts membership rather than equality so it cannot detect contamination. The "47 tests passing" claim is true but irrelevant — none exercise repeated default-argument calls in a loop. Fix: replace `tags=[]` with `tags=None` plus an inside-function `if tags is None: tags=[]`.
