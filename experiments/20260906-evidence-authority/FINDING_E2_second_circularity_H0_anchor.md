# FINDING E2 — v82's own Section IV.M documents a SECOND circularity,
# structurally parallel to the Section II.F case, and TJB's own paper
# already explains exactly why it resists a straightforward fix

**Date:** 2026-09-06
**Continues:** `FINDING_E1` (literature grounding). Second of the
5-step autonomous follow-up on TJB's "de-conflating evidence from
authority" invitation.

## What was found

While tracing Section IV.O's own list of "how much work this direction
still requires" (v82 p.33, Conclusion), a second item — separate from
the already-studied `r_X(z)` circularity (Section II.F, `P196`-`P202`,
`FINDING_P199`) — turned out to be a full, self-contained, carefully
argued case study by TJB himself: **Section IV.M, "H₀,anchor: what it
represents, and why it remains free-floating."**

**The setup:** the force law only ever gives a relative acceleration
between two nodes; recovering a trajectory requires two integrations,
each introducing a free constant (initial separation, initial
velocity). `H₀,anchor` stands in for the missing initial-velocity
constant. Making the model's own implicit assumption explicit
(fractional velocities match, `ȧ/a = ṡ/s`, mirroring the already-used
fractional-acceleration matching) gives `H₀,anchor = ṡ₀/s₀` — **a
purely kinematic ratio: relative velocity over relative separation
between two typical nodes, today** — not an abstract cosmological
parameter at all.

**The attempt:** TJB tried to ground `s₀` and `ṡ₀` directly in real,
citable data — `s₀ ~ 30 Mpc` from the cluster-cluster correlation
length [ref 91], and cluster pairwise-velocity statistics from
simulations calibrated against observations [ref 92]. Combined
directly: `H₀,anchor ~ 11 km/s/Mpc` — not a remotely plausible Hubble
constant.

**The diagnosis, in TJB's own words:** the peculiar-velocity data used
for `ṡ₀` is only extractable because surveys **already subtract an
assumed smooth Hubble flow** from redshift-based distances first —
"using such data to independently derive `H₀` is circular **in the
same sense already flagged for `r_X(z)` via `ρ_crit(z)` (Sec. IIF)**."
A second, compounding problem: at the relevant `~30-60 Mpc`
separations, the systematic (attractive) component of pairwise
velocity fades toward zero, with bulk/random motion dominating — there
may not even be a well-defined "typical `ṡ₀`" at this scale, circularity
aside.

**TJB's own conclusion:** *"We do not think this is a fixable
methodology choice: a genuinely non-circular velocity-and-distance pair
for nearby clusters would require direct, geometric distance
measurements combined with spectroscopic velocities — which is the
distance-ladder methodology already used by SH0ES. Attempting this
ourselves would reconstruct one side of the existing tension, not
provide an independent third answer."* `H₀,anchor` is therefore retained
as a free-floating fit parameter, with sensitivity reported by fixing
it at representative values (including SH0ES) rather than deriving it.

## Why this matters for the "de-conflating evidence from authority" line

**This is a second, independent, TJB-self-diagnosed instance of the
exact same epistemic pattern** as the `r_X(z)`/`ρ_crit(z)` case, and
TJB draws the parallel himself, in his own text, not something this
project inferred. Both share the identical structure:

| | `r_X(z)` (Sec. II.F) | `H₀,anchor` (Sec. IV.M) |
|---|---|---|
| Naively "evidence-only" construction | mass + critical-density evolution `ρ_crit(z)=ρ_crit,0·E(z)²` | correlation length `s₀` + pairwise velocity `ṡ₀`, both real, citable |
| Where the Friedmann/FLRW assumption actually hides | `ρ_crit(z)` itself is defined via `H(z)` — the very thing being tested | the peculiar-velocity data was extracted by *already assuming* an `H₀` to subtract the Hubble flow first |
| TJB's own verdict | "the most serious residual dependence... flag as Class III, circular" | "circular in the same sense... we do not think this is a fixable methodology choice" |
| Resolution in v82 | retained, classified, flagged | retained as free-floating fit parameter, sensitivity-tested instead of derived |

**The general lesson, stated once, applies twice:** trying to build a
"Newtonian/Minkowski-only," FLRW-independent quantity from real data
can fail not because the data itself is unavailable, but because the
data's own *measurement pipeline* already assumes the very global
framework being tested — a subtler, harder-to-spot failure mode than a
missing dataset. TJB's own `H₀,anchor` case is a rare, valuable example
of this being caught, diagnosed, and reported explicitly as a finding
in its own right rather than quietly patched over or hidden.

## Connection to E1's literature

TJB's own diagnosis ("surveys already subtract an assumed smooth Hubble
flow... before the peculiar velocity itself can be extracted") is
precisely the failure mode the distance-duality-relation and
Copernican-principle test literatures (`FINDING_E1`) are built around
avoiding — by construction, those tests use *paired*, independently-
calibrated observables (e.g., SNe Ia luminosity distance vs. galaxy-
cluster angular-diameter distance) specifically so that no single
measurement in the pair needs to assume the relation being tested.
TJB's own `H₀,anchor` attempt used two data sources that turned out not
to be independent in the required sense (the velocity data's own
construction already leaned on the separation/expansion-rate side).

## What this does NOT establish

1. Does not identify a fix for either circularity — TJB's own text
   argues the `H₀,anchor` case specifically may not be fixable without
   reconstructing the SH0ES distance-ladder methodology itself.
2. Does not establish that these are the ONLY two such circularities in
   v82 — the claim-decomposer pass (next step) checks the remaining
   inputs (`m_X(z)`, `k_X(z)`, gas mass, the separation law) explicitly.
3. `NO_AUTHOR_ERROR` — this entire finding is a direct, careful reading
   of TJB's own self-diagnosis, already published in his own paper; no
   claim here is this project's own discovery about v82's correctness.
