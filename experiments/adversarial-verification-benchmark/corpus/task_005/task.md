# Task 005 — Does a new teaching method improve test scores?

An education-statistics research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We ran a pilot of a new interactive-teaching method in one 9th-grade
algebra classroom (n=28 students) and compared end-of-term test scores
to the school's other three 9th-grade algebra classrooms taught
conventionally (n=31, n=29, n=30).

The pilot classroom's mean score was 85.3 (SD=4.1), vs. the
conventional classrooms' pooled mean of 77.1 (SD=3.7). A two-sample
t-test gives t=9.86, p<0.001, and Cohen's d=2.09 (a very large effect).

**Conclusion:** the new interactive-teaching method produces large,
statistically significant improvements in student test performance and
should be rolled out across all math classes at the school, all grade
levels, all subjects.

## Supporting script

```python
import numpy as np
from scipy import stats

pilot_scores = np.array([88, 79, 91, 85, 82, 90, 77, 86, 89, 83, 87, 92, 81, 84,
                          90, 78, 85, 88, 86, 83, 91, 80, 87, 84, 89, 82, 86, 85])
conv_scores = np.array([72, 81, 68, 79, 84, 75, 70, 88, 73, 77, 82, 69, 76, 80,
                         74, 71, 78, 85, 72, 79, 76, 83, 70, 81, 77, 74, 80, 78,
                         73, 76, 82, 79, 71, 84, 77, 75, 80, 73, 78, 76, 74, 81,
                         79, 72, 77, 83, 75, 78, 80, 76, 74, 79, 81, 73, 77, 82,
                         75, 78, 76, 80, 74, 79, 77, 81, 75, 78, 73, 76, 80, 79,
                         77, 74, 81, 76, 78, 75, 79, 73, 80, 77, 76, 79, 74, 78,
                         81, 76, 75, 78, 80, 77])[:90]

t_stat, p_val = stats.ttest_ind(pilot_scores, conv_scores)
pooled_std = np.sqrt((pilot_scores.std()**2 + conv_scores.std()**2) / 2)
cohens_d = (pilot_scores.mean() - conv_scores.mean()) / pooled_std

print(f"Pilot mean: {pilot_scores.mean():.1f}, Conventional mean: {conv_scores.mean():.1f}")
print(f"t={t_stat:.2f}, p={p_val:.4f}, Cohen's d={cohens_d:.2f}")
```

Please review the report's reasoning and its conclusion.
