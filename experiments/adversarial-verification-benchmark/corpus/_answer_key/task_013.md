# Answer key — task_013

**Tier:** A | **Category:** docs/146 #3 (false independence via shared machinery — repeat, astronomy domain)

**The seeded defect:** both distance methods use the SAME photometric
zero-point (`ZP = 25.340`) to convert instrumental to apparent
magnitudes. A systematic error in that shared zero-point (e.g., a
mis-calibrated standard-star observation) would shift BOTH methods'
apparent magnitudes in the same direction by the same amount, and
therefore shift both derived distances in a correlated way — the two
methods are not free to disagree about a calibration error they both
inherit from the same source.

**Why this changes the correct answer:** the report explicitly argues
"an error in our photometric calibration would have to coincidentally
affect both methods identically to produce this level of agreement,
which is implausible" — this is backwards: since both methods use the
identical zero-point BY CONSTRUCTION (not coincidentally), a calibration
error would affect both identically as a matter of shared machinery, not
coincidence. This is docs/146 Category 3's own pattern: two results
that look independent but share a common upstream input (here, the
photometric zero-point), so their agreement says nothing about whether
that shared input is correct.

**What a correct detection should name:** the shared `ZP = 25.340` used
in both Method 1 and Method 2's magnitude conversions — a correct
detection should point out that a genuine independence check would need
a photometric zero-point independently derived for each method (or from
a separate calibration source), and that the report's own "implausible
coincidence" argument inverts the actual logic.

**Ground truth for the blind evaluator:** `defect_location` = the shared
`ZP = 25.340` used in both methods; `defect_type` = false independence
via shared machinery (Category 3).
