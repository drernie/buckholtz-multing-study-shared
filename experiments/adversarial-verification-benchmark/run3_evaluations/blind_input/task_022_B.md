# Task 022 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 022

### 1. Falsifiable claim
Every one of the 8,214 source rows is represented distinctly in the merged table, and satisfaction.mean() is computed over the full, correctly-identified population.

### 2. Controls
**None supplied.** Only check is len(merged) from the SAME function under test — not compared against sum of input row counts (8,214), no independently-known-correct small case run.

### 3. What's wrong
Report's own footnote is the smoking gun: respondent_id assigned sequentially starting at 1 by two SEPARATE systems — batch-local surrogate keys, not shared identity. `keep="last"` + concat(early first) means colliding IDs get silently overwritten by the late respondent. "merged rows = 5,003" is treated as proof nothing was lost, but given the footnote, 5,003 is the MATHEMATICALLY FORCED outcome of the bug (late's range 1-3211 is a full subset of early's 1-5003), not evidence against it.

### 4. Executable check
Reproduced the exact scenario + report's own function verbatim, plus a positive control (genuinely unique combined key):
```
[reported check] Merged rows: 5003, Average satisfaction: 7.74
[diagnosis] early respondents silently discarded: 3211 (64.2% of early batch)
[positive control, unique key] merged rows = 8214 (expected)
[ground truth union] rows=8214, avg=7.4336
[buggy merge] rows=5003, avg=7.7400 -- delta +0.31 bias from the collision bug alone
```

### 5. Verdict
**REJECT.** False given the report's own stated facts; the report's own printed number is self-incriminating once checked against len(early)+len(late) instead of against nothing.

---

### DRAFT CLAIM
A survey-merge script combines early_bird.csv (5,003 rows) and late_respondents.csv (3,211 rows) via concat+drop_duplicates(subset="respondent_id", keep="last"), reporting 5,003 merged rows, avg satisfaction 7.42, as evidence of a complete, lossless merge. Both files assign respondent_id independently starting at 1, so the IDs are batch-local row indices, not a shared identity key; late's range (1-3211) is a full subset of early's (1-5003). Under this scheme, drop_duplicates is guaranteed to treat every late respondent as a duplicate of an unrelated early respondent sharing the same index, discarding 3,211 of 5,003 early-bird rows (64%) and replacing them with late respondents' answers — reducing the merged count to exactly len(early), precisely the number cited as proof of success. No positive or negative control was used. Verdict: REJECT — "no rows lost" is falsified by the report's own ID-generation scheme, and the reported count is the fingerprint of the bug, not evidence against it.
