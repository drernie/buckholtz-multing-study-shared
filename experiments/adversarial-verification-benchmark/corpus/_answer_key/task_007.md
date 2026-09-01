# Answer key — task_007

**Tier:** A | **Category:** docs/146 #7 (control evaluated where the tested effect trivially vanishes)

**The seeded defect:** the proposed coupling term is
`k_c * V_ctrl * dV/dt` — it is multiplied by `V_ctrl`. The negative
control is run at `V_ctrl = 0`, which makes the ENTIRE coupling term
identically zero regardless of whether the code correctly implements
`k_c`, correctly implements `dV/dt`, or has any bug at all in the
coupling logic. The control cannot fail no matter what bug might be
present in the coupling implementation, because it never actually
exercises the code path that computes a nonzero coupling contribution.

**Why this changes the correct answer:** the report concludes "the
negative control passed cleanly, so we can trust the model's behavior
when `V_ctrl != 0` as well" — but a control that structurally cannot
detect a bug in the very code path it's meant to validate provides zero
information about that code path. This is docs/146 Category 7's own
exact pattern (the P74/P82 `g_hat=0` incident, and the project's own
extracted rule: "a negative control run at [the coupling parameter]=0
certifies only the uncoupled skeleton, because every term carrying the
coupling vanishes identically").

**What a correct detection should name:** the fact that `V_ctrl = 0`
makes `k_c * V_ctrl * dV/dt` identically zero for ANY value of `k_c` or
any bug in how `dV/dt` is combined with it — a correct detection should
recommend re-running the control at `V_ctrl != 0` (comparing against an
independently-computed expected coupling contribution) as the actual
test of whether the coupling term is implemented correctly.

**Ground truth for the blind evaluator:** `defect_location` =
`V_ctrl_test = 0.0  # negative control`; `defect_type` = control at
trivial zero (Category 7).
