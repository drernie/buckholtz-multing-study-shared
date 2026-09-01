# Answer key — task_015

**Tier:** A | **Category:** docs/146 #4 (silently-fixed parameter — repeat, ML hyperparameter sweep)

**The seeded defect:** `max_iter=1` is hardcoded for EVERY learning-rate
value in the sweep — the model only ever takes a single pass over the
training data, regardless of learning rate. With only one epoch, very
small learning rates never get the chance to converge (the model is
essentially still near its random initialization) and very large
learning rates never get the chance to diverge or overshoot badly across
multiple epochs — a single-epoch run compresses the effective dynamic
range of "how much the learning rate actually matters" that a properly-
trained (multi-epoch, until-convergence) run would reveal.

**Why this changes the correct answer:** the report concludes the model
"is robust to learning-rate choice across 4 orders of magnitude" and
recommends skipping careful tuning — but this conclusion requires each
learning-rate setting to have been given a fair chance to actually train
the model (i.e., train until convergence or a consistent fixed number of
effective updates), not artificially capped at one pass for all of them.
This is docs/146 Category 4's own exact pattern (the `eta_q` silently
fixed at 0 / `docs/122` incident): a sweep that looks like a full
profile across one dimension, but silently holds another relevant
"free" setting (here, training duration) fixed in a way that suppresses
the very effect being tested.

**What a correct detection should name:** the `max_iter=1` argument,
fixed identically across every learning-rate value — a correct detection
should point out that a genuine learning-rate sensitivity test requires
training each configuration to convergence (or at least a realistic,
consistent training budget), not capping every run at a single epoch.

**Ground truth for the blind evaluator:** `defect_location` = the
`max_iter=1` argument inside the sweep loop; `defect_type` =
silently-fixed parameter (Category 4).
