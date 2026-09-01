# Answer key — task_005

**Tier:** A | **Category:** docs/146 #5 (narrow result generalized to a broader claim)

**The seeded defect:** the result is legitimately measured for ONE
specific configuration — one teacher, one classroom, one subject
(9th-grade algebra), one term, n=28 pilot students, non-randomized
assignment (a single intact classroom, not randomly assigned students).
The conclusion silently generalizes this to "should be rolled out across
all math classes at the school, all grade levels, all subjects" — a
claim about teacher effects, grade-level effects, and subject-matter
effects that this single-classroom, single-teacher pilot cannot address
at all (it can't even separate "the method works" from "this particular
teacher is unusually effective," since there's no comparison of the same
method taught by a different teacher).

**Why this changes the correct answer:** the statistics themselves
(t-test, effect size) are computed correctly and the within-scope
finding (this classroom did better than the other three, this term) is
real — but the report's own conclusion silently expands the claim well
beyond what a single non-randomized classroom comparison can license.
This is docs/146 Category 5's own pattern: a result honestly proven for
one narrow configuration, silently generalized in the headline/next
step.

**What a correct detection should name:** the jump from "one pilot
classroom, one teacher, one subject, one grade" to "all math classes,
all grade levels, all subjects" — a correct detection should flag that
teacher identity is confounded with method (only one teacher taught the
new method), and that grade/subject generalization has zero supporting
data in this analysis.

**Ground truth for the blind evaluator:** `defect_location` = the
"Conclusion" paragraph's final clause ("should be rolled out... all
grade levels, all subjects"); `defect_type` = narrow-to-broad overclaim
(Category 5).
