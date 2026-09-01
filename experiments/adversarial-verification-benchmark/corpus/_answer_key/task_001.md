# Answer key — task_001

**Tier:** A | **Category:** docs/146 #1 (post-hoc numerology / coincidence without mechanism)

**The seeded defect:** the "volume-weighted average radius" mechanism is
invented *after* the numerical coincidence is already known, and it does
not actually explain anything — the script never checks whether the
volume-weighted radius is close to a value that would predict ideal HCP
packing; it just computes a number and the report waves at it ("within
2% of a value that would make the approximation valid") without stating
what that target value is or deriving it independently. The real
mechanism check is missing: there is no first-principles reason a
three-species compound's c/a ratio should equal the single-species ideal
HCP value, and no test of whether OTHER ternary alloys with similarly
"balanced" volume-weighted radii also show this ratio (which the report
itself proposes as the falsifiable prediction but never runs).

**Why this changes the correct answer:** the honest conclusion is "an
unexplained close numerical coincidence, mechanism not established" —
not "not coincidental, explained by X." The report's proposed mechanism
is a retrofit, structurally identical to docs/146 Category 1's own
worked examples (a plausible-sounding shell fitted after the number is
known, not predicting it).

**What a correct detection should name:** the report never independently
derives a target value for the volume-weighted radius and shows the
actual value matches it — it just asserts the match "works out" without
showing the computation, and treats retrospective plausibility as if it
were explanatory power. A good detection flags exactly this — "the
mechanism was proposed after the fact and never independently checked
against a prediction," possibly also noting the report's own suggested
falsification test (checking other alloys) was never run.

**Ground truth for the blind evaluator:** `defect_location` = the
"Proposed mechanism" paragraph; `defect_type` = post-hoc numerology
(Category 1).
