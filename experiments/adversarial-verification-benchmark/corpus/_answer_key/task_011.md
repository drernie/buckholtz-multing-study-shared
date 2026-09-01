# Answer key — task_011

**Tier:** A | **Category:** docs/146 #11 (provenance/attribution error — stale or silently-changed value)

**The seeded defect:** `RISK_FREE_RATE` is reassigned between Section
3.2's calculation (4.15%, Q1 data) and Section 5.1's calculation (3.98%,
Q2 data), but Section 5.1's own prose still describes its sensitivity
analysis as being "computed using the current 4.15% risk-free rate" —
the written report's own words are internally inconsistent with the
actual code, which silently switched to a different rate between
sections without flagging the change.

**Why this changes the correct answer:** the report's sensitivity claim
("robust to +/-0.5% swing... 3.65%-4.65%") describes a range CENTERED ON
4.15%, but the actual sensitivity sweep in the code is centered on the
updated 3.98% rate (giving 3.48%-4.48%, not 3.65%-4.65%) — the reported
range doesn't match what the code actually computed. This is docs/146
Category 11's own exact pattern (the stale-constant incident): a value
silently changed between uses, with the written description not updated
to match, producing an internal contradiction not caught by the report's
own author.

**What a correct detection should name:** the `RISK_FREE_RATE`
reassignment from 0.0415 to 0.0398 between the two code sections, and
the mismatch between Section 5.1's stated range (3.65%-4.65%, implying
the OLD 4.15% rate) and what the updated code would actually produce
(centered on 3.98%) — a correct detection should point out this specific
inconsistency, not just say "the numbers should be double-checked."

**Ground truth for the blind evaluator:** `defect_location` = the
`RISK_FREE_RATE = 0.0398` reassignment vs. Section 5.1's prose;
`defect_type` = provenance/attribution error (Category 11).
