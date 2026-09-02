# Task 022 — baseline arm output

## Findings

**Verdict: not supported — contradicted by the report's own facts.** The "5,003 rows, nothing lost" claim is the symptom of a silent data-loss bug, not evidence against one.

`respondent_id` in each file is assigned sequentially starting at 1, independently, by two different systems — a batch-local surrogate key, not a shared identity key. `drop_duplicates(subset="respondent_id", keep="last")` treats colliding IDs as the same person, silently overwriting early-bird rows with unrelated late-respondent rows under the same slot.

Simulation (matching the report's stated sizes: early 1-5003, late 1-3211, late fully inside early's range): merged rows = 5003 = early's own row count exactly; colliding-id count = 3211 (all of the late batch). That equality (merged length == larger input's length, verbatim) is the fingerprint of key collision, not completeness — a true disjoint union should give 5003+3211=8214 rows.

Impact: ~3211 genuine early-bird respondents' real scores are silently replaced by unrelated late respondents' scores under the same slot. The reported average is computed over a corrupted, mislabeled subset.

Fix: either plain concat with no dedup (if genuinely disjoint populations) or dedup on a real stable identity field / source-prefixed ids.

---

**DRAFT CLAIM:** The claim that a merge of 5,003 early-bird + 3,211 late-respondent rows is "complete and correct, no rows lost" (merged=5,003 rows, avg=7.42) is false and contradicted by facts in the same report: respondent_id is assigned independently and sequentially starting at 1 in each file, so it is not a valid cross-file key, yet the merge uses drop_duplicates(subset="respondent_id"). Reconstruction confirms this silently deletes ~3,211 genuine early-bird rows, replacing their scores with unrelated late respondents' scores under the same id slot — which is also why the merged count (5,003) exactly equals the larger input's row count instead of the expected disjoint-union total of 8,214. That exact-match count is the bug's fingerprint, not evidence against it. Fix: plain concat with no dedup, or dedup on a real stable identity key.
