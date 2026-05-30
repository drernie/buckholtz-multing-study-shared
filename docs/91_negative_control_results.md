# Negative-Control Test Results

**Status:** INTERNAL_ONLY, DIAGNOSTIC_ONLY, NO_VALIDATION, NO_REFUTATION

## Summary

Tests run: 3 negative-control diagnostics across 3 AI services

Results:
- Test 1 Row-Permutation: PASS (all 3 services)
- Test 2 Randomised Beta: ChatGPT PASS, Claude FAIL, Gemini FAIL
- Test 3 Synthetic LCDM: FAIL (all 3 services)

Key finding: Test 3 failure indicates diagnostic proxy model insufficient.
This is NOT refutation of MULTING - it is proxy limitation.

Verification level: 5/10 (unchanged)

See test run output for detailed metrics.
