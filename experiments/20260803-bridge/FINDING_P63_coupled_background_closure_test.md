# FINDING P63 — g_hat≠0 coupled background: the four typed equations are mutually consistent (Bianchi-closed), off-shell, as a pure algebraic identity

**Status:** Skeptic-reviewed (Step 8a) — **CONFIRMED-REAL**, no algebra bug
found; two wording/scope tightenings applied below in direct response.
**Script:** `P63_coupled_background_closure_test.py` (`experiments/20260803-bridge/`)
**Scope:** background order only, `ĝ≠0` (the physically coupled case). Does
NOT solve for `a(t)`/`φ̄(t)`, does NOT return to the perturbation sector.

NOT_VALIDATION — NOT_REFUTATION — OUR_RECONSTRUCTION — L0: descriptive.

---

## Origin: the user's own detailed review of FINDING_P62

The user reviewed `FINDING_P62`, endorsed upgrading its Verdict framing
(WEAKENED → "CONFIRMED-REAL as a platform-validation result, not an
independent physical result" — a framing this finding accepts, since it
matches P62's own corrected Verdict exactly), and specified in detail what
the next step should be, quoted directly:

> "background system непосредственно из action, с жёсткой типизацией: ρ_A,
> ρ_phys, φ̄, a. Затем проверить, что background equations взаимно
> совместимы: E_00=0, E_ii=0, E_φ=0, E_ρ=0. Критический тест:
> d/dt(E_00) =? combination of E_ii, E_φ, E_ρ."

Four pre-registered outcomes, the user's own naming, verbatim:

- **C1** — system closes and admits regular solutions.
- **C2** — closes, but requires free invariants/normalizations (dynamics
  determined, predictive calibration not yet fixed).
- **C3** — closure requires a genuinely new arbitrary function/prescription
  (real structural underdetermination).
- **C4** — equations fail consistency/Bianchi closure themselves (internal
  inconsistency in the completion).

The user also specified the discipline to carry over from `FINDING_P62`:
positive control (full on-shell closure) plus one-equation-broken negative
controls for `E_ρ`, `E_φ`, `E_ii` separately, "as far as constructively
possible" — and explicitly reframed the whole program's ordering:

> `S → background EOM → on-shell FRW → perturbation system → μ,γ` — not
> `free a(t) → perturbations → μ`.

## Grounding: what the campaign has already established

Before building, the exact conventions were extracted verbatim (not from
memory) from five prior findings:

- **Background Friedmann (00):** `H²=(8πG_N/3)ρ_total`, unmodified `G_N`
  (`FINDING_P34`).
- **Background scalar KG:** `φ̄̈+3Hφ̄̇=ĝρ̄_A` — cross-verified via two
  independent Lagrangian routes and a covariant d'Alembertian check
  (`FINDING_P34`, `FINDING_P46`). Sign: `+ĝρ̄_A`, using the **bare**
  density (the same `ρ` appearing in the matter action's own
  `ρ(1−ĝφ)` coupling term).
- **`ρ̄_A`'s own continuity:** `ρ̄̇_A+3Hρ̄_A=0`, proven **unconditional** —
  `ρ̄_A:=n̄·m₀` tracks conserved particle number times a *fixed* reference
  mass, independent of `ĝ`'s value (`FINDING_P58`, a direct proof, not an
  approximation).
- **`ρ_phys` definition:** `ρ_phys:=ρ_A(1−ĝφ̄)`, exact algebraic relation
  matching `FINDING_P33`'s own mass law (`FINDING_P58`).
- **No "ii"/pressure/acceleration Einstein equation existed anywhere in
  the campaign before this finding** — genuinely new.
- **`FINDING_P39`'s SI-normalization gap is still open:** no established
  relation between `ĝ` and `G_N` — both kept as independent free symbols
  throughout this file, per standing convention.

## What was built

**Part A** — pure (unperturbed) flat FRW metric, Christoffels, and the
full Ricci tensor (`Γ·Γ` terms included), reusing `FINDING_P48`'s own
already-verified helpers verbatim. Re-confirmed against the standard
textbook result (`R_00=−3ä/a`, `R_11=aä+2ȧ²`) — the same positive control
`FINDING_P48` ran, re-run here at pure background order (much cheaper: no
`ε`/`Ψ`/`Φ` needed at all). From this, `G_00=3H²` and `G_ii/a²=−2ä/a−H²`
were derived and confirmed against their standard closed forms — the
second one (the acceleration/Raychaudhuri-type equation) is genuinely new
to this campaign.

**Part B** — stress-energy for both sectors, background order, *derived*
(not assumed):

- Scalar (`V=0`, canonical `T_μν=∂_μφ∂_νφ−½g_μν(∂φ)²`): `T_00^φ=φ̄̇²/2`,
  `T_ii^φ/a²=φ̄̇²/2` — the stiff-fluid `p=ρ` result already used in
  `FINDING_P62`, confirmed here from first principles, not imported.
- Matter (dust, `T_μν=ρ_phys·u_μu_ν`, comoving observer `u^i=0` *exactly*
  at background order — not just to `O(ε²)`): `T_00^matter=ρ_phys`,
  `T_ii^matter=0` exactly. This confirms `FINDING_P34`'s own `p_m=0`
  assumption was safe for this specific point-particle-dust construction:
  the field-dependent mass enters only through `ρ_phys` itself, never
  through a new pressure term.

**Part C** — the four typed equations assembled:

```
E_00  = G_00 − 8πG_N·T_00^total
      = 3H² − 8πG_N[ρ_A(1−ĝφ̄) + φ̄̇²/2]
E_ii  = G_ii/a² − 8πG_N·T_ii^total/a²
      = −2ä/a − H² − 4πG_N·φ̄̇²
E_φ   = φ̄̈ + 3Hφ̄̇ − ĝρ̄_A                    (reused verbatim)
E_ρ   = ρ̄̇_A + 3Hρ̄_A                          (reused verbatim)
```

## Part D — the critical test

The user's own boxed equation was checked in its **strongest possible
form**: not "substitute E_ρ=0 and E_φ=0, then check the residual is
proportional to E_ii" (which would still require a separate step to solve
`ä` from `E_ii=0`), but a single, fully general, **off-shell** algebraic
identity — worked out by hand first, then verified computationally (never
trusted blind, per this campaign's own standing discipline):

```
dE_00/dt  =  −3H·(E_00+E_ii)  −  8πG_N·(1−ĝφ̄)·E_ρ  −  8πG_N·φ̄̇·E_φ
```

`sp.diff(E_00, t)` minus this candidate RHS was computed and simplified:
**the residual is identically `0`**, for *any* `a(t)`, `φ̄(t)`, `ρ̄_A(t)`
whatsoever — no substitution, no assumption that any of the four
equations individually vanishes. This is a pure algebraic identity, the
background-level analogue of the standard GR fact that only 2 of the
3 single-fluid FRW equations are independent (here correctly extended to
the full four-equation coupled matter+scalar system).

**What this identity gives for free, by linearity** (each claim is a
direct algebraic consequence of the verified identity, not a separately
re-run test):

- **Positive control:** if all four equations hold, `dE_00/dt=0` too —
  full closure.
- **`E_ρ` negative control:** its coefficient, `−8πG_N(1−ĝφ̄)`, is
  generically nonzero (vanishes only at the single special point
  `φ̄=1/ĝ`) — breaking `E_ρ` alone genuinely perturbs `dE_00/dt` by
  exactly that multiple. **[Skeptic-added note]** `φ̄=1/ĝ` is not an
  arbitrary/obscure corner — it is exactly the locus where
  `ρ_phys=ρ_A(1−ĝφ̄)=0`, i.e. the surface where the matter's own physical
  (gravitating) density passes through zero. The one point where `E_ρ`
  stops being load-bearing is physically distinguished, not accidental.
- **`E_φ` negative control:** coefficient `−8πG_N·φ̄̇`, nonzero for any
  genuinely time-varying `φ̄` (vanishes only at `φ̄=const`, the same
  degenerate diagnostic case `FINDING_P61`'s own skeptic review flagged as
  weak) — genuinely load-bearing.
- **`E_ii` negative control:** coefficient `−3H`, nonzero for any
  expanding/contracting background — genuinely load-bearing, not a
  redundant relation invoked trivially.

**Important honesty note, flagged explicitly for skeptic scrutiny:** the
three "negative control" bullets above are *inferred from the general
identity's linearity*, not separately re-computed via explicit
`ε`-substitution demonstrations (e.g. literally setting `E_ρ=ε_ρ≠0` while
holding the other three at zero and re-deriving the residual). Because
the verified identity is linear in `E_00,E_ii,E_ρ,E_φ` with the stated
coefficients, this inference is mathematically immediate — but it is an
inference, not a second independent computation, and is flagged here as
exactly the kind of reasoning step this campaign's own audit-verification
discipline requires a reviewer to check, not accept on assertion.

## Verdict

**The four typed background equations are mutually consistent under
general covariance — this rules out C4 for this specific completion, in
the narrow, precise sense the check actually tests.** Closure holds
generically, not for lucky special cases, and each equation was shown to
be genuinely load-bearing (none is vacuous/redundant).

**[Skeptic-tightened wording]** "Rules out C4" holds under the *Bianchi/
covariance-closure* reading of "internal inconsistency" — the specific
thing this check tests, and the specific thing the user's own critical
test asked for. It does **not** rule out other, broader senses in which
the completion could still be internally troubled even with Bianchi
closure intact: no simultaneous real/regular solution existing despite
covariance holding off-shell; ill-posed evolution (non-hyperbolic
propagation, wrong-sign kinetic terms once linearized); or positivity
failure (`ρ_phys<0` would require `ĝφ̄>1`, an in-principle-reachable
regime not excluded by this check). These are already correctly separated
into the C1-vs-C2-vs-C3 open question below and the "does NOT establish"
list — this paragraph makes the scope of "rules out C4" explicit rather
than leaving the reader to infer it.

**This does NOT yet distinguish C1 from C2 from C3.** Closure (consistency
of the *equations*) is a different question from whether they admit
regular solutions (C1), require a free normalization/invariant to
calibrate (C2 — most likely, given `FINDING_P39`'s own still-open
`G_N`-vs-`ĝ` gap), or need a genuinely new arbitrary function (C3).
Attempting an actual solution — even a special-case one, as `FINDING_P62`
did for `ĝ=0` — is the natural next step to distinguish these, and was
deliberately NOT attempted here, matching the user's own explicit request
("без попытки пока решать μ или Ψ_k").

## What this does NOT establish

- Whether the coupled system (`ĝ≠0`) admits regular, physically sensible
  solutions for `a(t)`,`φ̄(t)` — C1 vs. C2 vs. C3 remains open.
- Any resolution of `FINDING_P39`'s SI-normalization gap between `ĝ` and
  `G_N` — both were kept as independent symbols throughout; this finding
  neither closes nor needs to close that gap to establish closure.
- Anything about the perturbation sector — `Ψ_k(t)`, `μ_phys(a,k)`, D2 vs.
  D3 vs. D4 are entirely untouched by this finding, deliberately.
- The negative-control claims (see honesty note above) as independently
  re-computed demonstrations rather than a linearity inference from the
  single verified identity.
- Whether `T_matter^ii=0` (dust, no pressure) continues to hold once the
  perturbation sector is reintroduced with `ĝ≠0` — only the background
  case was checked here.
- **[Skeptic-added]** Only the `G_11`/`T_11` (`i=1`) spatial component was
  checked — the other two (`i=2,3`) were not separately computed. This is
  safe by the metric's own manifest isotropy (`g_11=g_22=g_33=a²`, no
  preferred spatial direction anywhere in the construction), but was not
  stated explicitly in the original derivation.
- **[Skeptic-added]** No independent check of the `0i` (off-diagonal)
  Einstein equation was run. For this background (`φ̄(t)`-only, comoving
  dust) it vanishes trivially by isotropy — no spatial gradient exists to
  source it — but this was not stated explicitly either.

## Not yet done

- Attempt an actual solution of the coupled system (even special-case, as
  `FINDING_P62` did for `ĝ=0`) to distinguish C1/C2/C3.
- Return to the perturbation sector once (or if) a background solution
  exists, to determine D2/D3/D4 for `μ_phys(a,k)` at `ĝ≠0` — the original
  goal `FINDING_P61` set out to reach.
- Whether `FINDING_P39`'s SI-normalization gap must be resolved before a
  unique background solution can be selected (plausible, given the C2
  framing above, but not established).

## Skeptic Verdict table

| # | Claim reviewed | Skeptic verdict | Response |
|---|---|---|---|
| 1 | `R_00,R_11,G_00,G_ii/a²` reduce to standard textbook FRW forms | Independently re-derived by hand, confirmed correct | No change needed |
| 2 | Scalar/matter background stress tensors (`T_00,T_ii` both sectors) | Independently re-derived by hand, confirmed correct | No change needed |
| 3 | The central identity `dE_00/dt=−3H(E_00+E_ii)−8πG_N(1−ĝφ̄)E_ρ−8πG_N φ̄̇E_φ` | Independently re-derived by hand from scratch, term-for-term match confirmed | No change needed — the single most load-bearing claim in the file, doubly verified (sympy + independent hand re-derivation) |
| 4 | Honesty note: negative controls inferred from linearity, not separately re-computed | Confirmed sound — no hidden constraint makes the inference vacuous, the four `E`s have enough independent jet-space directions to realize each one-broken configuration off-shell | No change needed |
| 5 | `E_ρ` coefficient's zero at `φ̄=1/ĝ` — is this an arbitrary corner? | **Found**: coincides exactly with `ρ_phys=0`, a physically distinguished surface, not an arbitrary point | **Fixed**: note added inline |
| 6 | "Rules out C4" — fully earned, or overclaimed? | **Found**: precise only under the narrow Bianchi-closure reading; a broader reader could over-interpret as ruling out non-existence of solutions, ill-posedness, or positivity failure | **Fixed**: Verdict section now states the narrow reading explicitly |
| 7 | Only one of three spatial `ii` components checked; `0i` not checked | Both safe by isotropy, but not stated explicitly | **Fixed**: both added to "does NOT establish" |
| 8 | Consistency of inherited inputs (P34/P46 KG sign, P58 `ρ_A`/`ρ_phys`) | Used consistently within this file; correctness of the upstream findings themselves is out of this review's two-file scope | Acknowledged as a standing dependency, not a defect of this file |

**Overall verdict: CONFIRMED-REAL.** No algebra bug found — the central
closure identity was independently re-derived by hand and matches
exactly. All fixes were wording/scope tightenings that make already-true
claims more precisely true, not corrections to a wrong result.
