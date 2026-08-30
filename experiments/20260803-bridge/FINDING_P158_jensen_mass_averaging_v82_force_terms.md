# FINDING P158 — the mechanically-correct calculation: Jensen's inequality,
# not angular cancellation, applied to v82's own mass-derived scalar chain

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math (independent verification: sympy + Monte Carlo)
**Verdict (final, post-skeptic):** `CONDITIONAL-DIRECTIONAL-PREDICTION;
F2-GETS-A-LARGER-POPULATION-AVERAGING-BOOST-THAN-F1-ONLY-IF-LOG-MASS-
CORRELATION-BETWEEN-PAIRED-NODES-EXCEEDS-RHO=-0.5; ORDERING-REVERSES-
BELOW-THAT-THRESHOLD; REAL-CORRELATION-SIGN-UNKNOWN;
MAGNITUDE-ILLUSTRATIVE-ONLY-NO-REAL-MASS-FUNCTION-USED`
**Correction (2026-08-30, context-asymmetric skeptic-caught):** the
original verdict claimed the `F^(2)>F^(1)` enhancement ordering was robust
"whenever mass scatter is nonzero," treating the independence assumption
(`m_A ⊥ m_P`) as a magnitude-only caveat (item 3 of the original "what
this does NOT establish" list). A dispatched skeptic found this false:
independence is the **hinge the entire direction of the claim pivots
on**, not just its size. §2.1 below derives, and independently
re-verifies, the exact threshold. This is a correction to the claim's
own robustness, not a retraction of the underlying mechanism (Jensen's
inequality itself, and the mass-degree bookkeeping in §1, both survive
unchanged and unattacked).
**Continues:** `FINDING_P157` §3, which correctly retracted an overclaimed
analogy (`docs/127`'s `C1` angular-cancellation result does not apply to
v82's own scalar `F^(1)` term) and named, but did not attempt, the
mechanically appropriate tool: Jensen's inequality / covariance over v82's
own mass-derived scalar chain. This file attempts it.
**Script:** `P158_jensen_mass_averaging_v82_force_terms.py` — two
independent verification methods (sympy analytic + Monte Carlo,
`N=4×10⁶`), both required to agree, per this project's own Independent
Verification Strength Ladder. ruff clean, does not touch the 881-test
suite.

## 1. Setup — v82's own mass-power-law chain, at fixed z `[VERIFIED-PDF pp.6-7]`

v82's Eqs. (10)-(14) make every node property a **deterministic power law
of the node's own mass `m_X`**, at fixed redshift (the `E(z)` factors in
each equation are constants shared by every node at a given `z`, so they
cancel in every ratio used below):

```
r_X(z) ~ m_X^(1/3)                                        [Eq 11]
T_X(z) ~ m_X^(2/3)                                         [Eq 12]
M_gas,X(z) ~ T_X(z)^B ~ m_X^(2B/3),  B=2.24 (v82's own fit) [Eq 13]
k_X(z) = const · M_gas,X(z) · T_X(z) ~ m_X^(2(B+1)/3)       [Eq 14]
```

`[VERIFIED-sympy]`: at `B=2.24`, `k_X ~ m_X^2.16` exactly (`2·3.24/3`), and
the combination `(k_X·r_X)` that appears in `F^(1)`/`F^(2)` scales as
`m_X^2.4933`.

**Total mass-degree of each force tier** (sum of exponents on `m_A`, `m_P`
in v82's own Eqs. 2-4):

| Tier | v82 formula (structure) | Mass degree |
|---|---|---|
| `F^(0)` (monopole) | `m_A·m_P` | **2** (bilinear, independent factors) |
| `F^(1)` (dipole) | `k_A·m_P·r_A + k_P·m_A·r_P` | **3.4933** |
| `F^(2)` (quadrupole) | `(k_A r_A)·(k_P r_P)` | **4.9867** |

The degree **strictly increases** monopole → dipole → quadrupole — a
structural fact about v82's own equations, independent of any analogy to
this project's own prior work.

## 2. The mechanically-correct tool: Jensen's inequality on the mass distribution

For a population of node-pairs `(m_A, m_P)`, independent draws from the
same mass distribution at fixed `z`, define the **enhancement factor**

```
R(p) ≡ ⟨m^p⟩ / ⟨m⟩^p
```

comparing the true population average of `m^p` to the power applied to
the population's own mean (v82's "representative value," per its own Sec.
IV.H framing). `R(p)=1` exactly for `p=0,1` (no scatter effect possible);
`R(p)>1` strictly for any `p>1` whenever the mass has nonzero scatter
(Jensen's inequality, `x^p` convex for `p>1`).

Using independence of `m_A`, `m_P` (`docs/125`'s own bilinear-kernel
structure already treats the two nodes' charges as independent per-pair
inputs — the same assumption used here):

```
F^(0) enhancement = ⟨m_A m_P⟩/⟨m⟩²           = 1              (EXACT — no Jensen bias)
F^(1) enhancement = ⟨(k_A r_A) m_P⟩/⟨m⟩^3.4933 = R(2.4933)
F^(2) enhancement = ⟨(k_A r_A)(k_P r_P)⟩/⟨m⟩^4.9867 = R(2.4933)²
```

**`F^(2)`'s enhancement is the exact square of `F^(1)`'s** — a direct
consequence of `F^(2)` being built from the *same* `(k·r)` factor on
*both* nodes, while `F^(1)` carries it on only one. **Under independence**
(`m_A ⊥ m_P`), `R(p)>1` whenever there is real mass scatter, so
`R(p)² > R(p)` and the quadrupole term is boosted more than the dipole
term, for any nonzero scatter, regardless of its exact size. **This
"regardless of size" robustness does NOT extend to robustness against
correlation — see the correction in §2.1.**

## 2.1 Correction: independence is load-bearing for the *direction*, not just the magnitude

A dispatched, context-asymmetric skeptic attacked the independence
assumption directly, and found it breaks the ordering, not just shifts
its size. Re-derived here independently (closed-form, then cross-checked
against the skeptic's own numbers) using a bivariate lognormal for
`(m_A, m_P)` with log-space correlation `ρ` (`ρ=0` recovers §2 exactly —
verified as a positive control, `test_correlated_recovers_independence_
case`):

```
F^(0) enhancement = exp(ρσ²)                    -- no longer exactly 1 unless ρ=0
F^(1) enhancement = exp[q σ²(q+2ρ−1)/2]          (q ≡ 2.4933)
F^(2) enhancement = exp[q σ²(qρ+q−1)]
```

`[VERIFIED-sympy]`: `log(F^(2)/F^(1)) = q σ²(q−1)(2ρ+1)/2`. Since `q>1`
and `σ²>0`, this is positive — i.e. `F^(2)` boosted more than `F^(1)`, the
original claim — **if and only if `ρ > −1/2`**, an exact threshold,
independent of `q` and `σ`. Below `ρ=−1/2`, `F^(2)`'s enhancement is
*smaller* than `F^(1)`'s — the ordering the original verdict called
"robust regardless of scatter size" **reverses**.

A second, related threshold: `F^(1)`'s own enhancement stays above 1
(still boosted, just no longer boosted *more than* `F^(2)`) until
`ρ = −56/75 ≈ −0.747`. Between `ρ≈−0.747` and `ρ=−0.5` both terms are
still enhanced relative to the representative value, but `F^(2)` is
enhanced *less* than `F^(1)` — the reverse of §2's picture.

`[VERIFIED-Monte-Carlo]`: correlated lognormal sampling (`N=4×10⁶`,
Cholesky-correlated draws, no formula injected) at the threshold itself
(`σ=0.5, ρ=−0.5`) gives `F^(1) enh=1.1664`, `F^(2) enh=1.1664` — matching
the analytic prediction (`1.1662`, `1.1662`) to `<0.02%`, and confirming
the two enhancements are equal exactly where the closed form says they
should cross.

**What this project does not know, and cannot resolve from the manuscript
alone:** whether real cosmic-web node pairs (however v82's own "node"
construction defines a pair) have `ρ` above or below `−0.5` in log-mass.
Physically, `ρ` could plausibly be **positive** (pairs of similar-mass
objects preferentially link in some structure-formation pictures — mass
assortativity is a real, studied effect in cosmic-web connectivity
literature, though not checked here) or **negative** (a large object
paired with a smaller satellite/infalling substructure). Both are
physically motivated; this project has no basis to prefer one sign over
the other for v82's own specific node-pair definition. The directional
claim from §2 is therefore **conditional**, not unconditional — see the
corrected verdict at the top of this file.

## 3. Verification `[VERIFIED-sympy + VERIFIED-Monte-Carlo, independent methods]`

- **Positive controls**: `R(0)=1`, `R(1)=1` exactly (sympy) — the formula
  cannot spuriously produce enhancement for the trivial cases.
- **`F^(0)` independence control**: Monte Carlo (`N=4×10⁶`, independent
  lognormal draws) gives `F^(0)` enhancement `=1.0000` — matches the exact
  analytic prediction, confirming the independence assumption is applied
  correctly in the simulation.
- **`F^(1)`, `F^(2)` cross-check**: Monte Carlo enhancement factors match
  the analytic `R(p)` and `R(p)²` predictions to `<0.2%` at `σ_lnm=0.5` —
  two structurally different computational methods (closed-form lognormal
  moments vs. brute-force sampling) agree.

## 4. Illustrative magnitudes — NOT a claim about the real cluster mass function

`R(p)` for a lognormal mass distribution has closed form
`R(p) = exp(p·σ²(p−1)/2)`. For illustration only (this project has no
independently-established scatter for the halo-mass range v82 targets,
`~5-6×10¹⁴ M_☉` per `FINDING_P155`'s own context):

| `σ_lnm` | `F^(1)` enhancement | `F^(2)` enhancement |
|---|---|---|
| 0.2 | 1.08× | 1.16× |
| 0.3 | 1.18× | 1.40× |
| 0.5 | 1.59× | 2.54× |
| 0.7 | 2.49× | 6.20× |

`σ_lnm≈0.2-0.3` is a conservative, commonly-cited ballpark for
mass-observable scatter in galaxy-cluster cosmology; `σ_lnm≈0.5+` would
apply to a broader population spanning a wider mass range than a
narrowly-selected cluster sample. **This project does not know which, if
any, applies to v82's own intended node population** — these rows
illustrate the qualitative direction and rough scale, not a specific
prediction. **Table restated: this is the `ρ=0` (independent-pairs)
case only** — per §2.1, the entire table's ordering (`F^(2)`
enhancement `>` `F^(1)`'s) inverts if paired nodes' log-masses are
correlated below `ρ=−0.5`; the table does not hold unconditionally.

## 5. Why this matters for Table III, stated carefully (now conditional on `ρ>−0.5`)

Table III (`[VERIFIED-PDF p.14]`, also used in `FINDING_P156`/`P157`)
shows `F^(1)` and `F^(2)` as the two dominant, nearly-cancelling
contributions (`~+53%`, `~−46.5%`) to the gross force budget, with a small
net residual (`+4% to +6%`). **If** paired nodes' masses are independent
or positively correlated (`ρ>−0.5` — §2.1, unknown for v82's own node-pair
definition), `F^(2)`'s population-averaging enhancement exceeds
`F^(1)`'s, and a proper population treatment would grow `F^(2)`'s
magnitude disproportionately — pushing the net balance toward `F^(2)`
(already negative in Table III's sign convention), not toward zero and
not toward `F^(1)`. Below that threshold, the direction reverses. This
is a **conditional directional** prediction, not an unconditional one:
the sign of the effect on the net force depends on the sign of a
correlation this project does not know, in addition to depending on the
unknown scatter size (`σ_lnm`) that already limited it to a direction-
only claim in the first draft of this file.

A separate, unconditional piece survives from the skeptic's own review
(their attack (c), which failed to break this part): **given** `ρ≥0`
(independence or positive correlation), Table III's own specific
coefficients (`a≈0.53` for `F^(1)`'s share, `b≈0.465` for `F^(2)`'s)
satisfy `a<2b`, which makes the net-force shift monotonically more
negative as the (now-established-larger) `F^(2)` enhancement grows —
not merely "larger in percentage terms" but larger in a way that
provably dominates the absolute net-force arithmetic for these specific
Table III numbers, for any scatter size, *conditional on* `ρ≥0` holding.

**This corrects the shape of `FINDING_P157`'s retracted "stakes"
argument, not just its confidence.** `P157`'s original (retracted) claim
borrowed `C1`'s "collapse toward zero" shape from an unrelated angular
mechanism. The mechanically-correct shape, derived here, is different: not
a collapse, but a **differential growth favoring the higher-mass-degree
term** — `F^(2)` over `F^(1)`, `F^(1)` over `F^(0)` (which is exactly
unaffected, `enhancement=1`, confirming §1's independence-based intuition
from `P157`'s own corrected `docs/124` discussion).

## What this file does NOT establish

1. **Not a claim about v82's own `H(z)` values or β-fit.** No refitting of
   `β₁`, `β₂`, `H₀,anchor` against population-corrected force terms was
   attempted — that is a materially larger undertaking (would require
   redoing v82's own χ²-minimization against the 33-point dataset with a
   modified force law) and is explicitly out of scope here.
2. **Does not know the real cluster/proto-cluster mass-function scatter**
   at v82's own target mass/redshift range — §4's numbers are illustrative
   only, using a lognormal for closed-form tractability, not because
   real halo mass functions are lognormal (Press-Schechter/Tinker-type
   functions have different, generally heavier, high-mass tails — which
   would likely make the enhancement *larger*, not smaller, but this is
   not computed here).
3. **`ρ` (log-mass correlation between paired nodes) is unknown, and per
   §2.1 this is not a magnitude-only caveat — it determines the
   direction of the entire result.** `ρ>−0.5` is required for this
   file's directional claim to hold at all; `ρ<−0.5` reverses it. This
   project has no verified pair-correlation data for v82's own node-pair
   construction and no basis to assert `ρ` is on either side of that
   threshold.
4. **Assumes v82's own "representative value" `m₀` is intended as the
   population mean** `⟨m⟩`. Checked (not merely assumed) for the mean and
   median specifically: both give the same qualitative ordering (a
   skeptic-derived general threshold, `κ < [⟨m^q⟩/⟨m⟩]^{1/(q−1)}`, is
   satisfied by both anchors for any `σ`). **Not checked for every
   possible anchor** — a sufficiently large, moment-weighted "typical
   value" (a realistic candidate for what an implicit fit procedure might
   effectively select in a right-skewed mass distribution) could exceed
   that threshold and reverse the ordering by anchor choice alone, even
   at fixed `ρ`. This file does not know which anchor, if any, v82's own
   fit implicitly uses.
5. **`NO_AUTHOR_ERROR`**: does not say v82's "representative value" choice
   is wrong — this remains v82's own explicitly-named, self-acknowledged
   open question (`FINDING_P157` §2). This file supplies a mechanically
   grounded direction and illustrative scale for what that gap *could*
   look like, nothing more.
6. **Does not close `docs/150` §6 item 2 or the pearl_registry row.** Both
   remain open — this sharpens the open question with a concrete,
   verified mechanism and direction, not a resolution.
