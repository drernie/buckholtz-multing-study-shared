# Task 019 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 019

### 1. Falsifiable claim
"Repeated calls to build_profile(name) inside process_batch(), using the default tags= argument, produce independent, correct per-run profiles."

### 2. Controls supplied
Only single-call tests (docstring doctest, `test_build_profile_basic`) — neither is a control for the actual claim (safety under REPEATED calls in a loop). No negative control exists at all.

### 3. Specific defect
Mutable default argument (`tags=[]`), body does in-place `.append()` — classic Python gotcha. The single-call test structurally cannot observe cross-call state leakage — wrong shape of test for the claim.

### 4. Executed check
`process_batch(["run_1","run_2","run_3"])`: all three profiles share the SAME list object (id() matches), each containing all three runs' tags. Corrected version (`tags=None` sentinel) does NOT exhibit the bug — confirms the check discriminates real pass from real fail.

### 5. Verdict
**REJECT.** Falsified by direct execution. The existing test is a control that cannot distinguish the working case from the broken one — it would report the same result either way, since it never calls the function twice.

---

### DRAFT CLAIM
A reviewed Python utility, build_profile(name, tags=[]), uses a mutable default argument mutated in place via .append(). Because Python evaluates default arguments once at function-definition time, every call omitting tags= shares and mutates the same list across calls. The function's docstring test and the one existing unit test both call build_profile() exactly once in isolation, so neither observes cross-call state sharing; a new process_batch() calls build_profile(name) repeatedly in a loop using the default. Executing process_batch(["run_1","run_2","run_3"]) shows all three profiles share one identical list object, each containing all three runs' entries rather than just its own — the "47 passing tests, safe to use" claim is falsified for the loop-usage scenario the new script actually exercises. A corrected version using a None sentinel does not exhibit this leakage, confirming both the diagnosis and the discriminating check's validity.
