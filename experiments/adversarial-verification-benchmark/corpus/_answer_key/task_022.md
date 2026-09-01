# Answer Key — Task 022

**Tier:** C (fresh synthetic, out-of-domain)
**Category:** Artifact Zoo Universal — `duplicate_ids` (silent overwrite)

## The seeded defect

Both exports assign `respondent_id` sequentially starting at 1,
independently, from two separate signup forms. So `respondent_id=1` in
the early-bird file and `respondent_id=1` in the late-respondents file
refer to two *different, unrelated* people who merely happen to share
an ID number. `drop_duplicates(subset="respondent_id", keep="last")`
treats these ID collisions as if they were the same respondent
appearing twice, and silently discards the earlier row for every
colliding ID, keeping only the later ("late respondents") row. Since
both batches independently number from 1 up to their own row count, IDs
1 through 3,211 (the smaller batch's size) collide directly, so up to
3,211 real early-bird respondents' rows are silently dropped rather than
merged.

## Why this changes the correct answer

The report claims "no rows silently lost" and that 7.42 "accurately
reflects the full respondent pool." Both claims are false. The expected
total across both files is 5,003 + 3,211 = 8,214 rows — but the actual
merged table has only 5,003 rows, exactly equal to the early-bird
file's own size. That mismatch is itself a visible tell: since
`respondent_id` collides for IDs 1 through 3,211 (the late file's
range), `drop_duplicates(keep="last")` keeps only one row per colliding
ID (the late-respondent's), dropping the corresponding early-bird row —
net effect, all 3,211 late respondents survive under their own IDs, but
none of the 3,211 early-bird respondents who shared those same ID
numbers survive at all; only early-bird respondents 3,212-5,003 (whose
IDs the late file never reached) are untouched. The reported average is
computed over a population that silently substituted 3,211 unrelated
late-respondent rows in place of the early-bird respondents who should
have occupied those same rows, and lost 3,211 real rows relative to the
true combined total of 8,214.

## What a correct detection should name

- `respondent_id` is not a stable, cross-batch-unique key — it was
  assigned independently and sequentially within each source file.
- `drop_duplicates` on a non-unique-across-sources key silently merges
  unrelated respondents, rather than raising an error or flagging the
  collision.
- The merged row count (5,003) doesn't even match the naive expectation
  (8,214 = 5,003+3,211) — that arithmetic mismatch alone is a cheap,
  available red flag the report's own author never checked, on top of
  the deeper identity-collision mechanism.
- A row count that happens to look "reasonable" is not proof of
  correctness — the actual identities being merged need to be checked,
  e.g. by using a real composite key (source file + original ID) or
  verifying `respondent_id` is globally unique before merging.

## Ground truth for the blind evaluator

- **defect_location:** `merged = pd.concat([early, late]).drop_duplicates(subset="respondent_id", keep="last")`
- **defect_type:** duplicate/colliding IDs across sources, silently
  overwritten rather than detected (Artifact Zoo Universal —
  `duplicate_ids`)
