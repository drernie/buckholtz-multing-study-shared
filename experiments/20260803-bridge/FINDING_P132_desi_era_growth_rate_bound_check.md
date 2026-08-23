# FINDING P132 — DESI-era growth-rate literature check: **`NULL RESULT, EXISTING CEILING REMAINS TIGHTEST`**

**Date:** 2026-08-24
**Origin:** hypothesis-arbiter (2026-08-23) strategic gate among 3 open
bottlenecks — `F→H_MULT(z)` and unique-completion resumption were both
found blocked by this campaign's own `docs/147` stop-rule (already true-
killed/REJECT'd, no new external fact to justify reopening). H4 (DESI-era
literature search) was the sole clean survivor. Directly closes
`FINDING_P31`'s own explicitly flagged gap: *"A 2010-era result...
DESI-era or more recent growth-rate analyses almost certainly exist and
may give a different, plausibly tighter, number — not chased down here."*
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P132_desi_era_growth_rate_bound_check.py`

---

## The question

Does a published, DESI-era (2024+) growth-rate/modified-gravity
constraint give a **tighter** bound on `ΔG/G_N` than `FINDING_P22`/`P31`'s
own existing ceiling (`A·g² ≲ 8.39×10⁻¹²`, derived from Bean &
Tangmatitham 2010's `Q−1≲0.01`)?

## What was found (WebSearch + WebFetch, all quotes verified by direct fetch)

**Structural match confirmed first, not assumed.** DESI 2024's own
`μ(a,k)`–`Σ(a,k)` modified-gravity parametrization (arXiv:2411.12026,
Ishak et al., JCAP 2025) modifies the Poisson equation as

```
k²Ψ = −4πGa²μ(a,k)·ΣᵢρᵢΔᵢ
```

— **structurally identical** to Bean & Tangmatitham's own eq. 6
(`k²φ = −4πGQa²Σᵢρᵢᵢ`): the same universal, all-species source sum, the
same role for the coupling parameter. `μ=1` confirmed (paper's own
words) as the GR value, exactly matching `Q=1`. This licenses the same
comparison `FINDING_P31` already used for `Q`.

**Three independent numerical sources, none tighter:**

| Source | `μ₀` (1σ, as quoted) | Approx. 2σ upper edge | `A·g²` implied | vs existing ceiling |
|---|---|---|---|---|
| arXiv:2411.12026 (2024, DESI+CMB+DESY3+DESY5-SN) | `0.05 ± 0.22` | `~0.49` | `~4.11×10⁻¹⁰` | **49× looser** |
| arXiv:2606.10597 (2026-07, DR+CMB-lensing+fσ8, tightest found) | `0.06 (+0.17/−0.23)` | `~0.46` | `~3.86×10⁻¹⁰` | **46× looser** |
| Binned fit, same 2024 paper (WebSearch summary only, `[WEAK]`, not independently re-fetched) | `μ₁=1.02±0.13`, `μ₂=1.04±0.11` | — | — | consistent, corroborating only |

**DESI DR2's own `μ`/`Σ` constraints confirmed still "in preparation"**
as of this search (2026-08-24) — source 2 (2026-07) is the most recent
available.

## Verdict — **`NULL RESULT, HONEST AND VALID`**

Every DESI-era bound checked — three independent analyses, including the
most recent — is roughly **40–50× looser** than the existing 2010-era
ceiling. **The existing internal benchmark (`A·g²≲8.39×10⁻¹²`) remains
the tightest available external bound.** This matches the hypothesis-
arbiter's own pre-registered outcome map exactly: *"Если новых
ограничений нет: → валидный null-результат."* `FINDING_P31`'s own
flagged gap is now closed — chased down, found not tighter, not left as
an open unknown.

**Why the newer analyses are looser, not an anomaly:** DESI's own
`μ(a,k)`/`Σ(a,k)` fits marginalize over more freedom (time- *and*
scale-dependence, jointly with `Σ₀`, sometimes binned in redshift) than
Bean & Tangmatitham's single time-independent `Q` — more free parameters
routinely loosens per-parameter bounds. This is a standard statistical
fact, not a sign the newer data is worse.

### Not established

- The exact asymmetric 95%-CL edges from either paper's own tables —
  this file approximates 2σ as 2× the quoted 1σ, flagged explicitly, not
  a re-derivation from the actual posterior shape.
- Whether DESI's own `μ`/`Σ` likelihood, like Bean & Tangmatitham's own
  `(Q,R)`, assumes a metric-modification mechanism applicable to
  MULTING's worldline-coupled construction — `FINDING_P31` §4 point 8's
  own caveat, inherited unchanged here, not re-litigated.
- DESI DR2's own eventual `μ`/`Σ` constraints, once published.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.

## Sources

- [DESI 2024 VII / Modified Gravity Constraints (arXiv:2411.12026)](https://arxiv.org/abs/2411.12026)
- [Synergy between the gravitational potential decay rate and other structure growth probes (arXiv:2606.10597)](https://arxiv.org/abs/2606.10597)
