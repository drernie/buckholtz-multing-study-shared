# Answer key — task_010

**Tier:** A | **Category:** docs/146 #10 (recomposition overclaim — combined claim stronger than parts license)

**The seeded defect:** each subsystem's 95%-confidence model explicitly
assumed the OTHER two subsystems were operating at "nominal" conditions
(nominal load for bearing, nominal temperature/chemical exposure for
seal, nominal flow/cavitation-free for impeller) — these nominal-
condition assumptions were shared as a common baseline across all three
models, not independently derived. Multiplying the three 95% figures
together (`p_bearing * p_seal * p_impeller`) is only valid if the three
subsystem failure modes are STATISTICALLY INDEPENDENT — but since all
three models share the same underlying "nominal operating conditions"
assumption, a real-world deviation from nominal (e.g., unusually high
flow rate, or elevated temperature) would tend to stress multiple
subsystems simultaneously, correlating their failure probabilities
rather than leaving them independent.

**Why this changes the correct answer:** the report's combined 85.7%
figure is a straightforward product-of-independent-probabilities
calculation applied to three sub-claims that are each individually
reasonable but share a common, unstated dependency (the shared nominal-
conditions assumption) — the honest combined claim is weaker than the
naive product suggests, since correlated failure modes make the true
joint reliability lower than independence would predict. This is
docs/146 Category 10's own exact pattern: individually true (or
individually reasonable) sub-claims chained into a combined verdict
stronger than their honest conjunction actually licenses.

**What a correct detection should name:** the shared "nominal
conditions" assumption across all three subsystem models, and the fact
that multiplying probabilities requires genuine independence, which this
shared assumption undermines — a correct detection should flag that a
correlated-failure or worst-case joint analysis (not simple
multiplication) is needed before the 80% program requirement can be
honestly claimed as met.

**Ground truth for the blind evaluator:** `defect_location` = the
"Combined conclusion" paragraph's multiplication of the three
probabilities; `defect_type` = recomposition overclaim (Category 10).
