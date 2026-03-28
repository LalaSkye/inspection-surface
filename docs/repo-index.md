# Repository Index

Each repository implements one control primitive or proof. No repository depends on another at runtime.

## Runtime proof

### runtime-commit-gate-demo
- **URL:** github.com/LalaSkye/runtime-commit-gate-demo
- **What:** Execution boundary. State does not change without a valid decision record.
- **Proof:** 5-step sequence: no decision, valid decision, replay, scope mismatch, expired.
- **Tests:** 13
- **Run:** `python demo/run_demo.py`

### start-here
- **URL:** github.com/LalaSkye/start-here
- **What:** Canonical governance demo. 8-stage evaluator pipeline. 10 bulkhead invariants.
- **Tests:** 134
- **Run:** `python run_demo.py`

## Gate and boundary implementations

### execution-boundary-lab
- **URL:** github.com/LalaSkye/execution-boundary-lab
- **What:** Gate interface contract. 6 contamination cases. Adversarial test suite.
- **Created:** 2026-02-18

### execution-gate-litmus
- **URL:** github.com/LalaSkye/execution-gate-litmus
- **What:** Tests whether governance exists. Execution gate + adversarial suite.
- **Created:** 2026-03-23

### admissible-transition-lab
- **URL:** github.com/LalaSkye/admissible-transition-lab
- **What:** Formal transition system. Admissibility enforced at execution boundary.
- **Created:** 2026-03-17

### interpretation-boundary-lab
- **URL:** github.com/LalaSkye/interpretation-boundary-lab
- **What:** Deterministic admissibility layer for interpretation proposals.
- **Created:** 2026-03-13

### dual-boundary-admissibility-lab
- **URL:** github.com/LalaSkye/dual-boundary-admissibility-lab
- **What:** Admissibility rotation corridor.
- **Created:** 2026-03-13

## Control primitives

### constraint-workshop
- **URL:** github.com/LalaSkye/constraint-workshop
- **What:** Small, deterministic control primitives. Formal specs (ADMISSIBILITY_ALGEBRA_v1, CANONICAL_PACKET_NORMAL_FORM_v1, PROOF_CARRYING_PACKET_SPEC_v1, GOLDEN_CONFORMANCE_CORPUS_v1).
- **Created:** 2026-02-16

### stop-machine
- **URL:** github.com/LalaSkye/stop-machine
- **What:** Deterministic three-state stop controller. Terminal state enforcement.
- **Created:** 2026-02-16

### invariant-lock
- **URL:** github.com/LalaSkye/invariant-lock
- **What:** Refuses execution unless version increments. Drift prevention.
- **Created:** 2026-02-16

### deterministic-lexicon
- **URL:** github.com/LalaSkye/deterministic-lexicon
- **What:** Fixed-term vocabulary. Exact matches. No inference.
- **Created:** 2026-02-16

## Measurement and analysis

### policy-lint
- **URL:** github.com/LalaSkye/policy-lint
- **What:** Governance statement linter. Typed warnings. 0-1 scoring. No ML.
- **Created:** 2026-02-17

### csgr-lab
- **URL:** github.com/LalaSkye/csgr-lab
- **What:** LLM stability and drift measurement. Deterministic scoring. Hash-chained evidence.
- **Created:** 2026-02-20

## Public surface

### trilogyos-surface
- **URL:** github.com/LalaSkye/trilogyos-surface
- **What:** Public verification surface for TrilogyOS. Explains behaviour. Does not enable replication.
- **Created:** 2026-03-24
