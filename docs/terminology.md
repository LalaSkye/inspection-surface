# Terminology

This project uses mechanical terms. Each term maps to code.

## Core terms

| Term | Meaning | Where it lives |
|---|---|---|
| decision record | Signed, scoped, time-bound input. Required for any mutation. | `decision_record.py` |
| commit gate | Sequence of deterministic checks. Fail-closed. Only path to mutation. | `gate.py` |
| execution boundary | The point where checks run before state changes. | gate entry |
| governed action | An action that must pass through the gate. Closed set. | `GOVERNED_ACTIONS` |
| state store | The data that changes (or doesn't). | `state_store.py` |
| audit log | Append-only record. Every attempt logged. No deletion. | `audit.py` |

## Verdicts

| Verdict | Meaning |
|---|---|
| ALLOW | Mutation proceeds. Decision consumed. |
| DENY | Mutation blocked. Reason logged. |
| HOLD | Mutation deferred. Pending review. |
| ESCALATE | Mutation requires higher authority. |

## Failure codes

| Code | Trigger |
|---|---|
| NO_DECISION_RECORD | No decision provided |
| VERDICT_NOT_ALLOW | Decision verdict is not ALLOW |
| INVALID_SIGNATURE | HMAC check failed |
| DECISION_EXPIRED | expires_at < now |
| NONCE_REPLAYED | Nonce already consumed |
| ACTION_MISMATCH | Decision action != request action |
| OBJECT_MISMATCH | Decision object != request object |
| ENVIRONMENT_MISMATCH | Decision environment != request environment |
| POLICY_VERSION_REJECTED | Policy version not in accepted set |
| UNKNOWN_ACTION | Action not in governed set |

## Design principles

| Principle | Implementation |
|---|---|
| Fail-closed | Any check failure -> no mutation |
| First-failure stops | Checks run in order, stop at first failure |
| Single entry point | All mutations go through `gate.execute()` |
| Nonce consumption | Decision is single-use. Consumed before mutation. |
| Append-only audit | Every attempt recorded. ALLOWED and BLOCKED. |

## Rule

If a term cannot be mapped to a check, condition, or failure code, do not use it.
