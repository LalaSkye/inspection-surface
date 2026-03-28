# Provenance & Independent Design Statement

Author: Ricky Dean Jones / Os-Trilogy LMT

## Statement

All repositories indexed here are original work developed independently using general software engineering principles:

- input validation
- state transition control
- cryptographic signing (HMAC)
- replay protection (nonces)
- expiry / freshness checks
- deterministic evaluation pipelines
- append-only audit logs
- fail-closed gate design

No external proprietary materials, codebases, or confidential specifications were used.

## Timeline

| Date (UTC) | Repository | What was built |
|---|---|---|
| 2026-02-16 | invariant-lock | Version-locked invariant enforcement |
| 2026-02-16 | stop-machine | Deterministic three-state controller |
| 2026-02-16 | deterministic-lexicon | Fixed-term vocabulary primitive |
| 2026-02-16 | constraint-workshop | Deterministic control primitives |
| 2026-02-17 | policy-lint | Governance statement linter |
| 2026-02-18 | execution-boundary-lab | Gate interface + contamination cases |
| 2026-02-20 | csgr-lab | LLM stability measurement |
| 2026-03-13 | interpretation-boundary-lab | Pre-verdict admissibility |
| 2026-03-13 | dual-boundary-admissibility-lab | Admissibility rotation corridor |
| 2026-03-17 | admissible-transition-lab | Transition system enforcement |
| 2026-03-23 | execution-gate-litmus | Governance existence test |
| 2026-03-24 | trilogyos-surface | Public verification surface |
| 2026-03-25 | start-here | Canonical governance demo |
| 2026-03-28 | runtime-commit-gate-demo | Commit gate + 5-step proof |

All dates are GitHub-recorded creation timestamps. Immutable. Independently verifiable.

## Non-claims

This project does not claim ownership of general concepts such as pre-execution validation, authorization checks, or standard security patterns.

## Evidence of independence

- Public git history with timestamps across 14 repositories
- Distinct terminology and implementation structure
- No shared code or licensed material from any third party
- Conformance tests that prove behaviour mechanically

## Contact

For questions regarding authorship or licensing, contact via repository issues.

## Licence

MIT (see LICENSE).
