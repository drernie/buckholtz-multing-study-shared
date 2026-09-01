# Answer key — task_014

**Tier:** A | **Category:** docs/146 #9 (numerical artifact — repeat, boundary-copied-bounds pattern)

**The seeded defect:** the optimizer's search bounds `(5.0, 45.0)` were
copied from a PREVIOUS, differently-scaled problem (large-diameter,
high-temperature pipe) and never updated for the new small-diameter,
low-temperature pipe, whose true cost-minimizing thickness is expected
to be much smaller (the report's own script comment notes "true optimum
should be a few cm, not tens of cm"). The true unconstrained optimum for
this cost function is x≈4.32 cm — below the copied lower bound of 5.0.
The optimizer converges to `x* = 5.0`, exactly the lower bound of the
copied, stale search window — a classic sign the true unconstrained
optimum lies outside the searched range and the optimizer simply walked
to the boundary.

**Why this changes the correct answer:** the report treats "the
optimizer converged cleanly (no error, no warning)" as validation that
5 cm is a genuine result — but `minimize_scalar` with `method="bounded"`
will report success even when the true optimum lies at or beyond the
boundary; a result landing exactly on a search bound is itself a red
flag, not a confirmation. This is docs/146 Category 9's own exact
pattern (the P128 incident): optimizer bounds copied from a different
problem instance at a different scale, causing the optimizer to walk to
a stale boundary instead of finding the true minimum.

**What a correct detection should name:** that the result `x* = 5.0`
lands exactly at the lower bound `bounds=(5.0, 45.0)`, and that these
bounds were explicitly noted (in the code comment) as copied from a
different, larger-scale problem — a correct detection should recommend
re-running with a bounds range appropriate to the new problem's actual
scale (e.g., 0.5-5 cm) before trusting the result.

**Ground truth for the blind evaluator:** `defect_location` = the
`bounds=(5.0, 45.0)` argument, copied-bounds code comment — result lands
at the **lower** bound (5.0), not the upper bound; `defect_type` =
numerical/optimizer artifact (Category 9).
