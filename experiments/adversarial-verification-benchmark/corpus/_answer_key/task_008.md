# Answer key — task_008

**Tier:** A | **Category:** docs/146 #8 (domain heuristic applied without checking mechanism sensitivity)

**The seeded defect:** the report applies the general heuristic "more
measurement opportunities ⇒ tighter bound" to test UNIFORMITY of an
effect across individuals — but each survey wave measures only the
POPULATION-AVERAGE effect (the same aggregate quantity, repeated), not
individual-level variation. Six repeated measurements of a population
average make the estimate of that average more precise, but they are
structurally blind to between-subject heterogeneity — a population
average can be measured with arbitrary precision even if the underlying
individual effects vary enormously (some participants respond strongly,
some not at all, canceling out in the average). More waves of the same
aggregate measurement do not add sensitivity to the specific question
being asked (uniformity across individuals).

**Why this changes the correct answer:** the report concludes additional
waves "support treating the effect as genuinely uniform" — but the
script's own printed quantity is a population-mean standard error, which
narrows with more waves regardless of whether individual heterogeneity
exists. This is docs/146 Category 8's own exact pattern (the P23
"universal coupling faces MORE channels, therefore tighter bound"
incident): a plausible general heuristic applied without checking
whether THIS SPECIFIC measurement is actually sensitive to the thing
being tested.

**What a correct detection should name:** the distinction between
"tighter estimate of the population average" (which 6 waves genuinely
gives) and "tighter bound on between-subject uniformity" (which requires
individual-level, not aggregate, measurements) — a correct detection
should point out these are different quantities and the script's own SE
calculation addresses only the former.

**Ground truth for the blind evaluator:** `defect_location` = the
"Assistant's report" reasoning paragraph (the "more waves ⇒ tighter
bound on uniformity" claim); `defect_type` = domain heuristic misapplied
(Category 8).
