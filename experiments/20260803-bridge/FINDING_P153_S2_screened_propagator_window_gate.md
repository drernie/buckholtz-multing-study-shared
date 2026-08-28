# FINDING P153 — S2's background channel closes almost for free: P152's own
# screened-kernel result already answers it, and it disagrees with what a
# literal reading of P11 might suggest

**Date:** 2026-08-28
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
(internal consistency / structural closure of the second escape route
named in `FINDING_P4`, `S2`)
**Verdict:** `SCREENED-PROPAGATOR-NO-COMPATIBLE-WINDOW` for the
Shtanov–Sahni background channel, **now independently confirmed by a
second, structurally different method** (`P154`, see §0b) — **not** a
general closure of S2, and **not** a claim that P11's own finding is
wrong. See §1 for why this scoping is the whole point of this file.
**Origin:** `FINDING_P4` (2026-08-10/11) named **S2** (a `ψ` with its own
distinct/screened propagator) as the second live, uncomputed escape
route, after `S1` (closed by `P152`, same day). The user proposed a
detailed 3-step protocol for `S2` (local-kernel fidelity → background-
cancellation test → `W_local ∩ W_bg` overlap-window gate) with the
explicit background test phrased as `⟨F_k^(μ)⟩_iso = 0?`.
**Script:** `P153_S2_screened_propagator_window_gate.py` (symbolic sympy,
reuses `P149`'s and `P152`'s own already-derived, already-skeptic-checked
results rather than re-deriving them; positive control against `P149`'s
own `β_d(0)=2`, `β_q(0)=√6`; ruff clean; does not touch the 881-test
suite)

## 0. Read this before the rest of the file — a scoping clarification,
not a silent substitution

The user's own Step 2 asked for `⟨F_k^(μ)⟩_iso = 0?` — and named this
"the main scientific payoff." **This file does not run that exact test.**
It runs a *different* test — the Shtanov–Sahni background `G_eff`
criterion, the same one this entire project has used, consistently,
since `docs/124` (2026-07-19), for "does a correction to the pair
potential source the smooth cosmological background `H(z)`." Mandatory
Novelty Check (`falsification-ladder.md` Step -3) surfaced that **both**
tests already exist in this project, computed for different structures,
with **different answers** for a screened kernel:

- `P11_yukawa_screening_breaks_double_layer.py` (2026-08-12): a
  **finite, single dipole shell** (dimensionless shell-radius units),
  Yukawa-screened, exterior potential evaluated a few shell-radii away.
  Result: **nonzero** for every finite `μ` tested, skeptic-`CONFIRMED-
  REAL` via an independent closed-form match.
- `P152_S1_general_pairkernel_background_closure.py` (2026-08-28, its own
  §2 Step 2): the Shtanov–Sahni `G_eff = G·lim_{r→∞}[f−rf']` for a
  screened correction `f(r)=C·r⁻ⁿ·exp(−μr)`, symbolic, any `n≥0`, any
  `μ>0`. Result: **exactly zero**, more robustly than the massless
  power-law case.

These are not two measurements of the same quantity that happen to
disagree — they are **different mathematical objects**: a finite-`r`,
single-structure near-field potential, versus the `r→∞` asymptotic limit
that the S–S formalism uses to determine what survives into a
mean-field, continuum-averaged Friedmann-type background equation. §1
argues in detail for why the **second** is the criterion actually
relevant to "does S2 revive `H(z)` sourcing," and why the first — while
real and unretracted — answers a different, local question. This file
takes a position on that scoping question rather than silently picking
one interpretation; if the skeptic (or the user) disagrees with this
reading, that disagreement is the load-bearing finding, not a detail.

## 0b. Correction (context-asymmetric skeptic review, same day) — the
scoping argument had a real gap, now closed by an independent method

A skeptic review of this file (claim + code + explicitly cited source
docs only, no session history) found the §1 scoping argument below rests
on an **unresolved order-of-limits problem**, not settled by wording
alone: `G_eff`'s `r→∞` real-space limit is *trivially* zero for **any**
exponentially screened correction, because the tail past `r~1/μ` is
already killed by construction — `G_eff=0` for every `μ>0` is therefore
not obviously *informative* the way it is for a power-law correction
(where the massless case's own zero, `n≥1`, is a genuine physical
statement, not a triviality of the functional form). The skeptic's own
Fourier-space check: `FT[exp(−μr)/r] = 1/(k²+μ²)`, finite and **nonzero**
as `k→0` — meaning a Yukawa correction *does* carry nonzero long-
wavelength (background-relevant) content in isolation, merely suppressed
by `1/μ²`, not exactly zero the way the real-space `r→∞` limit suggested.
Separately, the skeptic found §1.1's claim that `G_eff` is the *only*
criterion this project has used for the background question is
**factually inaccurate**: `docs/127`'s own **C1** test (isotropic-
orientation population average of the full vector dipole force at
*finite* `r`, over a filled ball — `scripts/c1_anisotropic_dipole_
nbody.py`) is a second, independently-motivated background-relevant
criterion this project already ran, specifically *because* it is a
genuinely different mechanism (orientation washout) than `G_eff`'s
radial-asymptotic one. §1.1 below is corrected to state this accurately.
The skeptic also flagged that "more robustly than the massless power-law
case" (§0, §1 originally) inverts what "robust" means — a screened
kernel's `G_eff=0` had, before this correction, been verified by only the
*weakest* of `docs/127`'s three rungs (the symbolic limit itself), not
the two independent rungs (Monte-Carlo re-derivation, `C1`) that gave the
massless case its real robustness; corrected below.

**Response, per the Falsification Ladder Step 8a matrix (skeptic verdict
= `WEAKENED`, not a veto — respond per concern):** the skeptic's own
proposed cheapest differentiating test — rerun `docs/127`'s `C1`
methodology with a Yukawa-screened kernel, at the physically relevant
scale `r~few/μ` rather than `r→∞` — was run as `P154`
(`P154_screened_C1_isotropic_population_average.py`). Result: the
isotropic-orientation ensemble mean is consistent with zero at `μ=1`
(ball `[0.5,5.0]/μ`, `z=+0.35σ`) **and** across a scale-robustness scan
from `1/μ` to `20/μ` (all `|z|<3`), while the aligned (non-isotropic)
control remains definite at every scale tested — see `FINDING_P154` for
full detail. This **independently confirms** `W_bg=∅` by a genuinely
different method (a finite-`r`, real-space population average, not an
`r→∞` asymptotic limit), directly answering the order-of-limits concern:
whatever nonzero long-wavelength content the Yukawa kernel carries in
isolation, it does not survive isotropic averaging over a realistic
population — the same orientation-cancellation mechanism `C1` already
established for the massless case applies here too. §1 below is
corrected to reflect both fixes (accurate criterion history; independent
finite-`r` confirmation, not reliance on `G_eff` alone).

## 1. Why the S–S `G_eff` criterion — corroborated, not alone, by `C1`
and now `P154` — answers "does S2 source `H(z)`"

Two considerations, both checked against primary sources rather than
asserted, **corrected per §0b**:

1. **This project has used `G_eff` as its primary background criterion
   since `docs/124`, corroborated (not superseded) by a second,
   independently-motivated criterion, `C1`, for the power-law case — and
   now, per `P154`, for the screened case too.** `docs/124` cites
   Shtanov & Sahni (arXiv:1010.6205) *by name* as "Generalizing the
   Cosmic Energy Equation," and `docs/125`, `docs/126`, `docs/127`/P2,
   `P152` all used `G_eff` as *a* background test — **corrected**: not
   the *only* one. `docs/127`'s own `C1` test (isotropic-orientation
   population average at finite `r`, keeping the dipole's full vector
   character rather than `G_eff`'s scalar-radial reduction) is a second,
   independently-motivated criterion this project already ran for
   exactly this question, and its own text frames it as *the* check on
   whether `G_eff`'s scalar reduction might be hiding something —
   language `P153`'s first version should have found and did not.
   `P154` extends `C1`'s own method (not `G_eff`'s) to the screened
   case, and both criteria now agree: `W_bg=∅`.
2. **The mathematical objects are not interchangeable in general, and
   for a screened kernel the difference is not merely academic.** `G_eff`
   is defined by an `r→∞` limit; a finite shell's near-field exterior
   potential (P11) or a finite-population isotropic average (`C1`,
   `P154`) are evaluated at *finite* `r`. For a power-law correction
   these different formulations converge on the same conclusion, and the
   `r→∞` limit is genuinely informative (docs/127's three-rung
   convergence). For a *screened* correction, `G_eff`'s `r→∞` limit is
   zero *by construction*, independent of the physics — which is exactly
   why the skeptic's Fourier-space concern (§0b) had to be taken
   seriously rather than dismissed, and why `P154`'s independent,
   finite-`r`, population-average confirmation — not `G_eff` alone — is
   what actually licenses `W_bg=∅` for the screened case.

## 2. Method — assemble, don't re-derive

Per the mandatory Novelty Check, this file **reuses** rather than
re-derives:

- **`W_local`** (Step 1): `P149`'s own closed-form Yukawa correction
  functions, `β_d(x)/β_d(0) = e⁻ˣ(x²+2x+2)/2` and
  `β_q²(x)/β_q²(0) = e⁻ˣ(x³+3x²+6x+6)/6` (`x=μr`), re-confirmed here as
  a positive control (`x→0` limit `=1` for both, matching `β_d=2,
  β_q=√6`). `P149`'s own physical-scale table (already computed, not
  redone here) shows negligible (`~10⁻⁸`) deviation at cluster scale
  (`μ=H₀/c`, `r~` few Mpc), growing toward `O(1)` only near the Hubble
  radius — a wide `W_local`.
- **`W_bg`** (Step 2): `P152`'s own screened-kernel symbolic proof,
  re-confirmed here directly for MULTING's own two tiers (`n=1` dipole,
  `n=2` quadrupole, not just the abstract general-`n` case): `G_eff=0`
  for **any** `μ>0`, exactly — corroborated (per §0b) by `P154`'s
  independent, finite-`r`, isotropic-population-average confirmation
  (`C1`'s own methodology, screened kernel), which agrees `W_bg=∅` at
  `μ=1` and across a `1/μ`–`20/μ` scale scan. `W_bg` (the set of `μ`
  values giving a nonzero background contribution) is therefore the
  **empty set** — not merely small, not merely negligible at some scales
  and significant at others, but structurally empty for every `μ`, by
  two independently-motivated methods, not one formula alone.

## 3. Result

`W_local ∩ W_bg = W_local ∩ ∅ = ∅`. **Verdict:**
`SCREENED-PROPAGATOR-NO-COMPATIBLE-WINDOW` for the background channel,
**now supported by two independently-motivated criteria** (`G_eff`'s
`r→∞` limit, per §2; `C1`'s finite-`r` isotropic population average, per
`P154`) **agreeing**, not by `G_eff` alone. Unlike the user's own
anticipated failure mode ("screening either preserves background zero,
or breaks local hierarchy before giving a cosmological effect" — their
`M0`), the actual mechanism found here is different from both:
**`W_local` is wide and comfortable** (screening does *not* threaten the
near-field ladder at any physically relevant scale) **and `W_bg` is
empty on its own terms**, independent of `W_local` entirely — there is
no trade-off to navigate, because one side of the trade never has
anything on it. This is closer to the user's own pre-registered `M0` in
spirit (no escape) but reached by a different route than either `M0`
sub-case they anticipated (not "local hierarchy breaks first"; rather
"background never turns on, at any scale, by two independent tests").

## 4. What this file does NOT establish

1. **Does not overturn or retract P11.** P11's own finite-shell,
   near-field, skeptic-confirmed nonzero result stands unmodified — it
   answers a real, different question (§0, §1), not a wrong answer to
   this file's question.
2. **Does not close S2 as a whole.** P11's own live result — a
   screened mediator produces a genuine, nonzero near-field departure
   from the exact double-layer cancellation — remains a real, open lead
   for **structure-formation / second-order observables** (this
   project's own recurring theme: "degenerate with ΛCDM at first order,
   distinguishable only at second," the `beta_cv.py` pearl,
   `docs/127`'s own §3 pointer to Sec. III observables). This file does
   not pursue that lead; it only prevents it from being mis-filed as a
   background-`H(z)` effect.
3. **Does not establish that `G_eff` (rather than some other criterion)
   is the objectively unique correct definition of "sources the
   background" in all possible generalized closures** — only that it is
   the criterion this project's own methodology has consistently used
   for this specific question since `docs/124`, and that departing from
   it without flagging the departure would itself be a methodological
   error. §0/§1 state this position explicitly rather than assuming it.
4. **Does not re-derive `W_local`'s own robustness independently** — it
   reuses `P149`'s own already-skeptic-adjacent-checked result (verdict
   `MASSIVE-MEDIATOR-NEAR-FIELD-RATIO-INVARIANT-COMPATIBLE`) rather than
   re-verifying it from scratch, per the Novelty Check discipline.
5. **Not a claim about MULTING's own theory** (`NO_AUTHOR_ERROR`) —
   entirely this project's own reconstruction of the S–S background
   closure applied to its own candidate scalar-completion construction.
6. **Per `P152`'s own §0/§0b caveats (inherited, not re-litigated here):**
   the `G_eff` criterion's own applicability to a charge sector without a
   conserved cosmological background is itself an assumption inherited
   from `docs/127`'s three-rung verification (rung 1, the sympy limit) —
   not independently re-verified at general `n` or general `μ` by this
   file either.
7. **`P154`'s own confirmation reuses `C1`'s filled-ball, uniform-density
   ansatz** — a population with genuine spatial-orientation correlations
   was not re-examined (it was already excluded on physical grounds,
   CMB isotropy, by `docs/127`'s own `C1` finding, not re-derived here),
   and `P154`'s scale-robustness scan used reduced statistics at most
   scanned points (its own largest `z`-score point, `R_MAX=20`, was
   reconfirmed at full statistics per `FINDING_P154` §4) — see
   `FINDING_P154` §"does NOT establish" for the full, itemized list of
   what `P154` itself does not cover.
8. **A third skeptic review (documented in `FINDING_P154` §4) found the
   original `P154` covered only the dipole tier** — MULTING's quadrupole
   tier (`docs/125`'s `κ_qq` term) is structurally a *cross term between
   two different bodies' own dipole charges*, per `two_charge_
   completion.py`'s own established header, not a single-body rank-2
   tensor — so the dipole's `⟨n̂⟩=0` vector-washout mechanism does not
   automatically transfer to it (a genuine self-quadrupole tensor would
   `not` wash out isotropically, `⟨n_in_j⟩=δ_ij/3≠0`). `P154` §4/§Step 3
   closes this by verifying the *actually relevant* mechanism for
   MULTING's own cross-dipole structure — independence of two different
   bodies' orientations, `E[n̂_A·n̂_P]=0` — numerically, not merely by
   asserting the dipole result transfers. `W_bg=∅` is now independently
   confirmed for both tiers, not the dipole tier alone.
