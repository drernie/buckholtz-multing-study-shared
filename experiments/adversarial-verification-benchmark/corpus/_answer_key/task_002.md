# Answer key — task_002

**Tier:** A | **Category:** docs/146 #2 (tautological control — cannot fail by construction)

**The seeded defect:** "Route 1 (time-domain)" is claimed to be an
independent measurement from the observed step response, but the code
comment reveals the step response itself was SIMULATED using
`tau = R*C` — the same value Route 2 uses. Both routes compute
`f_c = 1/(2*pi*R*C)` from the identical `tau`. There is no way for the
two routes to disagree, regardless of whether the circuit's true
physical time constant matches its nominal design value — the "check"
is a tautology: it verifies that `1/(2*pi*R*C) == 1/(2*pi*R*C)`, not
that the physical circuit matches its design.

**Why this changes the correct answer:** the report claims this rules
out "component drift or fabrication tolerance" — but the analysis never
touches a real measured step response at all, so it says nothing about
drift or tolerance. This is structurally identical to docs/146 Category
2's P51 example: two "independent" routes that reduce to the same
expression by construction.

**What a correct detection should name:** the comment
`# <-- the step response itself was simulated using tau = R*C` is the
tell — a correct detection should point out that Route 1 does not use
an actual measured/observed step response, only a synthetic one built
from the same `tau` Route 2 already assumes, so agreement is guaranteed
and proves nothing about the real circuit.

**Ground truth for the blind evaluator:** `defect_location` = the
"Route 1" code comment / the claim that the two routes are independent;
`defect_type` = tautological control (Category 2).
