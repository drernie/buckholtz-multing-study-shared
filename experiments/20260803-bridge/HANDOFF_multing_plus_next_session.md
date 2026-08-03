# Handoff — MULTING+ formal-bridge thread (parked, not executed)

**Status: PARKED.** Supplied by the user 2026-08-03, immediately after the
consolidated-letter work. The user redirected focus back to the Buckholtz
letter package before any of this was acted on — nothing below has been
registered, tested, or committed as a result. Saved verbatim so the thread
is not lost.

**Scope note:** this describes a multi-LLM tournament (Grok, Gemini, Kimi,
Qwen, DeepSeek, Perplexity, NotebookLM, a ChatGPT-like source-grounded pass)
and three MULTING+ formal candidates (cascade auxiliary-field EFT, P(X)+
worldline multipoles, dipole-polarization thawing model) with two claimed
negative results (NR-019, NR-020). None of this content matched anything in
this repository's git history (local or any of the four origin branches) as
of 2026-08-03 — see the git/grep audit earlier in this session's transcript.
Before any of it is registered under the null_results/ or pearl_registry/
protocol, Gate 1 (Artifact Identity) applies: verify where it actually lives
and that the derivations check out independently, the same discipline this
project has applied to every other claim today.

**Do not feed any of this into Buckholtz-facing material** (letter, one-pager,
figure, memorandum) until it has been through the same certification process
as C1-C5C — per the user's own instruction in the original prompt below
("Не повторяй... Table A1 как будто он ещё открыт", "не защитить MULTING
любой ценой").

---

## Verbatim content supplied by the user

<details>
<summary>Full handoff prompt (click to expand)</summary>

Ты продолжаешь уже проведённое многоагентное исследование MULTING.

Не начинай анализ с нуля и не генерируй ещё один широкий список красивых
теорий. Сначала усвой приведённые ниже результаты, статусы и отрицательные
ветви.

Главная цель предыдущей работы: понять, существует ли воспроизводимый
физический переход

    локальный силовой закон MULTING
            →
    ковариантный или усреднённый физический сектор
            →
    космологическая история H(z).

### 1. Сертифицированные результаты

**1.1 Локальный силовой закон**

    F(r,z) = -A2(z)/r² + A3(z)/r³ - A4(z)/r⁴
    U(r,z) = -A2(z)/r + A3(z)/(2r²) - A4(z)/(3r³) + C(z)

C(z) не влияет на локальную силу, но нельзя автоматически считать его
космологической энергией без ковариантного определения T_mu_nu.

Статус: LOCAL FORCE = MATHEMATICALLY DEFINED / NOT FALSIFIED.

**1.2 Условие отталкивающего окна**

    F(r) ∝ -1/r² + ell_d/r³ - ell_q²/r⁴
    r_± = [ell_d ± sqrt(ell_d²-4ell_q²)]/2

Промежуточное отталкивающее окно существует только при ell_d > 2 ell_q.
Эквивалентно: ell_q >= ell_d/2 означает притяжение на всех расстояниях.
Точный алгебраический результат.

**1.3 Стандартный pair-fluid путь закрыт**

Для U_s = C_s r^(-s), стандартное конфигурационное pair-fluid отображение
даёт p = (s/3)rho, w = s/3. Термы MULTING: 1/r → w=1/3, 1/r² → w=2/3,
1/r³ → w=1. При положительной плотности не создаёт отрицательного давления.

Область строго ограничена: закрывает только pure inverse-power + standard
configurational pair-fluid. НЕ закрывает: ковариантные поля, поляризационные
среды, Buchert/backreaction, нелокальные действия, взаимодействующие
сектора, другие правила усреднения.

Статус: PAIR-FLUID BRIDGE = FAILED WITHIN FROZEN SCOPE.

**1.4 Table A1** — AI-ASSISTED / DATA-CONDITIONED CONSTRUCTION (beta_d spread
~5.8×, beta_q spread ~94.7× across services; H0 anchor at z=0).

**1.5 Оранжевая кривая** — CODE-RENDERED CURVE / SEPARATE ARTIFACT /
GENERATIVE OPERATOR NOT IDENTIFIED. Positive control: blue curve → flat
Planck-like ΛCDM, H0≈67.37, Ωm≈0.3152, residual≈0.002%. Divergence from
Table A1 up to ~44% at z≈2.1, rms ~21%.

### 2. Аудит наблюдательной части

**2.1** CC-level chi2: MULTING ≈15.50 (H0≈73.30) vs ΛCDM ≈14.51 (H0≈68.36)
after H0 profiling, Δchi2≈+1 — CURVE-LEVEL DISTINCT / OBSERVATIONALLY
UNRESOLVED. Not a confirmation of MULTING.

**2.2** MCXC 1742-cluster screening (projected separation, corrected for
peculiar velocities/FoG): at ell_d=8 Mpc, ell_q=0, ~4.25% of pairs could
geometrically sit in the repulsive window, dispersal ~20 Gyr; at ell_q=4 Mpc,
no repulsive window exists. GEOMETRIC SCREENING ONLY / NOT A PARAMETER
CONSTRAINT.

**2.3** kSZ one-sided upper limits (~8 Mpc weighted, ~11 Mpc raw) are
support-conditional on r_lo choice, exploratory — not a final constraint.

### 3. Турнир других LLM

| Model | Proposal | Status |
|---|---|---|
| Grok | broad conceptual map | BROAD MAP / NO CLOSURE |
| Gemini | Buchert/backreaction, IR-resonance | FAILED / hypothesis source only |
| Kimi | 7 toy bridges → dipolar medium | TOY CONSTRUCTION, not reconstruction |
| Qwen | log-virial bridge | FAILED — integration/sign error |
| DeepSeek | chameleon/scalar completion | GENERIC SCALAR COMPLETION, not MULTING bridge |
| Perplexity | — | FAILED — sign error, w=-s/3 instead of +s/3 |
| NotebookLM | one-pair H² = ΣCᵢaⁿ | SOURCE-GROUNDED TOY, one-pair ≠ FLRW background |
| ChatGPT-like | generalized Layzer-Irvine | USEFUL FORMALISM, not closed |

### 4. Поздние кандидаты MULTING+

**4.1 Cascade auxiliary-field EFT** — ∇²φ~ρ, ∇²σ~-(∇φ)², ∇²ξ~-φ(∇φ)²
genuinely produces φ~1/r, σ~1/r², ξ~1/r³. No covariant action; A3,A4
dependence on two-object properties not reproduced; magnitude taken from
external ~10⁻⁵ assumption. Status: USEFUL RADIAL-LADDER HYPOTHESIS / MAIN
NO-GO NOT CERTIFIED.

**4.2 Shift-symmetric P(X) + worldline multipoles** — one 1/r propagator's
derivatives naturally give 1/r, 1/r², 1/r³.

    NR-019: exact ghost-condensate P_X=0 (w=-1) conflicts with the ordinary
    static 1/r propagator, which requires P_X>0. Scope: exact-condensate
    realization only, not a universal no-go.

Status: PROMISING FORMAL ARCHITECTURE / PHYSICAL LINK NOT ESTABLISHED.

**4.3 Dipole-polarization thawing model** — canonical scalar, hilltop
potential, monopole+dipole couplings to dark sector.

    NR-020: bare multipole exchange gives
    ell_q²/ell_d² = 3/2 + 3/(4 g_m²) >= 3/2
    but the F7 repulsive-window condition needs ell_q²/ell_d² < 1/4.
    BARE MULTIPOLE EXCHANGE FAILS THE F7 REPULSIVE-WINDOW CONDITION.

Rescue: decorrelation C(r/xi) = 1/[1+(r/xi)²], xi ≲ ell_d/5 needed — but C's
form is phenomenological, xi not derived, vector/tensor channel distinction
not proven.

    P-DECORR: NECESSARY RESCUE HYPOTHESIS / MICROPHYSICAL DERIVATION ABSENT.

Cosmological part uses a CPL proxy (not the real orange H_target), delta is a
fitted parameter (minimized RMS), lambda=3-5 given in code units without
physical translation, background and local-force sectors nearly
parametrically independent, kSZ/growth claims not run through a two-fluid
calculation.

Status: BLOCKED / PROMISING FORMAL CONSTRUCTION / NOT A COMPLETED MULTING
BRIDGE.

### 5. fσ8 graph

New report claims "+5-8% at z>=1" but the plotted MULTING+ curves visually
sit BELOW ΛCDM at high z. Sign, sigma8 normalization, RSD-fit provenance,
joint covariance, fitted-delta parameter penalty, and two-component
baryon+DM growth are all unverified.

    f sigma_8 prediction = UNVERIFIED. Do not claim faster growth, "within
    1.3 sigma", or "kSZ barely changes" until recomputed from source arrays.

### 6. Real results (R1-R9) and open questions (U1-U6)

R1 Table A1 = data-conditioned AI construction. R2 Table A1 and orange H(z)
are different artifacts. R3 digitization positive-control residual 0.002%.
R4 standard pair-fluid bridge fails structurally, w=n/3>0. R5 local force not
falsified. R6 repulsive-window criterion ell_d>2ell_q. R7 multipole
derivatives of one propagator naturally generate the 1/r,1/r²,1/r³ ladder.
R8 bare multipole realization fails F7: ell_q²/ell_d²>=3/2. R9 exact P(X)
condensate has a propagator/background tension.

U1 can one microphysics fix both cosmological background scale and
A2,A3,A4? U2 can central dipole/quadrupole response be derived without
manual alignment? U3 can a bounded Hamiltonian give the needed signs? U4 can
C(r/xi) be derived rather than inserted? U5 what does a real orange H_target
effective-fluid reconstruction give? U6 what does the model predict for
growth/lensing/pairwise-velocity/kSZ after a two-fluid calculation?

### 7. What not to repeat

Another broad ten-theory tournament; treating pair-fluid as still open;
substituting ΛCDM/CPL for the real orange H_target; averaging different LLM
answers; using Table A1 as an independent prediction; claiming all bridges
are excluded; hand-setting Ω_DE and declaring success; fitting C(r/xi), w(z),
Q(z) or kernel(z) to the target; observational claims without source arrays
and covariance.

### 8. Priority of next work (if and when resumed)

Pick at most one candidate: the multipole scalar/polarization bridge. Four
narrow tests:

- **T1 Real H_target** — use the actual digitized orange curve; recover
  rho_X_req(z), p_X_req(z), w_X_req(z) with digitization/interpolation/H0/Ωm
  uncertainty.
- **T2 Multipole microphysics** — derive the two-body central potential for
  two composite objects; check action-reaction, orientation averaging,
  boundedness, real A2/A3/A4 dependence on both objects' m,k,r.
- **T3 Decorrelator** — derive C(r/xi) from a kinetic/Fokker-Planck/
  Ornstein-Zernike model, don't assume its form; check whether the tensor
  channel can decay while the vector channel survives.
- **T4 Perturbations** — solve at least the linear system for delta_c,
  delta_b, theta_c, theta_b, Phi, Psi; then compute fσ8, G_eff, slip,
  pairwise velocity, kSZ response.

### 9. Required final-status format (if resumed)

Separate verdicts, never collapsed into one: LOCAL FORCE, TABLE A1, ORANGE
H(z), PAIR-FLUID, MULTIPOLE RADIAL LADDER, BARE MULTIPOLE F7 WINDOW,
POLARIZATION/P(X) BRIDGE, GROWTH/fσ8 — each its own line.

</details>

## Materials the user said to attach if/when this resumes

1. C1-C4 certification report (provenance, transcription, w=n/3, corrected
   amplitude estimate)
2. C5A/C5B report (Table A1 origin, orange curve's separate status)
3. Local-force + MCXC report (exact window condition, screening limits)
4. P(X)+multipoles report (formal covariant candidate, propagator/condensate
   conflict)
5. Latest dipole/thawing report (hypothesis only — contains NR-020 and the
   unverified fσ8 claim)
6. Clean orange-curve-vs-Table-A1 comparison figure
