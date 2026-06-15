# N-body k_A catalog (Phase 2b scaffold)

**Status:** DATA NEEDED — not connected by default.

Expected CSV columns:
- `z` — redshift
- `k_A_msun` — kinetic energy / c² in M_sun units (same as supplementary `k_a_c2_msun`)

Sources (external): IllustrisTNG, UniverseMachine, or published cluster kinematics tables.

If catalog is missing, `k_a_closure_test` returns **INCONCLUSIVE** (not FAIL).

See `src/k_a_independent.py::k_a_nbody_from_catalog`.
