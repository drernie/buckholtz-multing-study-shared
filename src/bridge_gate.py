"""Bridge permission gate — MCMC blocked, NOT_VALIDATION labels."""

from __future__ import annotations

OUTPUT_LABEL = "NOT_VALIDATION"
INTERNAL_CLOSURE_TEST = "INTERNAL_CLOSURE_TEST"
AUTHOR_CONFIRMATION_REQUIRED = "AUTHOR_CONFIRMATION_REQUIRED"
VERIFIED_DIAGNOSTIC = "VERIFIED_DIAGNOSTIC"
NOT_REFUTATION = "NOT_REFUTATION"
AUTHOR_BRIDGE_NEEDED = "AUTHOR_BRIDGE_NEEDED"

is_mcmc_allowed: bool = False
PREDICTION_BLOCKED: bool = True


class BridgeGateError(RuntimeError):
    pass


def assert_not_mcmc(caller: str = "") -> None:
    if is_mcmc_allowed:
        return
    raise BridgeGateError(
        f"[bridge_gate] MCMC blocked for {caller or 'bridge'}. "
        f"Label: {OUTPUT_LABEL}. Author bridge confirmation required."
    )


def assert_not_new_z_prediction(caller: str = "") -> None:
    if not PREDICTION_BLOCKED:
        return
    raise BridgeGateError(
        f"[bridge_gate] Prediction on new z blocked for {caller or 'bridge'}. "
        f"Label: {OUTPUT_LABEL}."
    )


def get_output_label() -> str:
    return OUTPUT_LABEL
