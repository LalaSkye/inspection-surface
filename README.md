# Inspection Surface

**Invariant:**
No valid decision record -> no state mutation on the demonstrated path.

This repository indexes executable control systems and verification paths.

## What this does not prove

This repository does not prove adoption, certification, standardisation, production readiness, or path-universal deployment coverage.

It demonstrates bounded execution-control surfaces that can be run, inspected, and tested at their stated scope.

## Start here

If you only open one repository, open:

**[commit-gate-core](https://github.com/LalaSkye/commit-gate-core)**

A path-local execution-boundary primitive showing that a state mutation cannot proceed without a valid DecisionRecord on the demonstrated path.

Then inspect:

**[runtime-commit-gate-demo](https://github.com/LalaSkye/runtime-commit-gate-demo)**

A runtime demo showing a decision-record controlled mutation path with an adversarial test battery.

Verify locally:

```bash
git clone https://github.com/LalaSkye/runtime-commit-gate-demo
cd runtime-commit-gate-demo
pip install -r requirements.txt
python demo/run_demo.py
python -m pytest tests/ -v
```

Expected: decision-record controlled proof sequence with the current test battery. Check the runtime repo README for the latest test count.

## Repository index

Each repository implements one control primitive or proof.

| Repository | What it does | Tests |
|---|---|---|
| [commit-gate-core](https://github.com/LalaSkye/commit-gate-core) | Path-local commit gate primitive. DecisionRecord required for mutation on the demonstrated path. Known hardening gaps tracked as issues. | yes |
| [runtime-commit-gate-demo](https://github.com/LalaSkye/runtime-commit-gate-demo) | Execution boundary. Decision record required for mutation on a demo path. | 42+ |
| [start-here](https://github.com/LalaSkye/start-here) | Canonical governance demo. 8-stage evaluator pipeline. | 134 |
| [execution-boundary-lab](https://github.com/LalaSkye/execution-boundary-lab) | Gate interface. 6 contamination cases. Adversarial suite. | yes |
| [constraint-workshop](https://github.com/LalaSkye/constraint-workshop) | Deterministic control primitives. Formal specs. | yes |
| [stop-machine](https://github.com/LalaSkye/stop-machine) | Three-state stop controller. Terminal state enforcement. | yes |
| [admissible-transition-lab](https://github.com/LalaSkye/admissible-transition-lab) | Transition system with admissibility enforcement. | yes |
| [execution-gate-litmus](https://github.com/LalaSkye/execution-gate-litmus) | Tests whether governance actually exists. | yes |
| [invariant-lock](https://github.com/LalaSkye/invariant-lock) | Refuses execution unless version increments. | yes |
| [deterministic-lexicon](https://github.com/LalaSkye/deterministic-lexicon) | Fixed-term vocabulary. No inference. | yes |
| [policy-lint](https://github.com/LalaSkye/policy-lint) | Governance statement linter. 0-1 scoring. | 42 |
| [csgr-lab](https://github.com/LalaSkye/csgr-lab) | LLM stability and drift measurement. Hash-chained evidence. | yes |
| [interpretation-boundary-lab](https://github.com/LalaSkye/interpretation-boundary-lab) | Pre-verdict admissibility layer. | yes |
| [dual-boundary-admissibility-lab](https://github.com/LalaSkye/dual-boundary-admissibility-lab) | Admissibility rotation corridor. | yes |
| [trilogyos-surface](https://github.com/LalaSkye/trilogyos-surface) | Public verification surface for TrilogyOS. | yes |

Full descriptions: [docs/repo-index.md](docs/repo-index.md)

## System map

```
                    ┌─────────────────┐
                    │  decision record │
                    │  (signed input)  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   commit gate    │
                    │  (checks)        │
                    │  fail-closed     │
                    └────────┬────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
         ┌──────▼──────┐    │    ┌───────▼───────┐
         │   BLOCKED   │    │    │   ALLOWED     │
         │  (no state  │    │    │  (mutation +  │
         │   change)   │    │    │   audit log)  │
         └─────────────┘    │    └───────────────┘
                            │
                   ┌────────▼────────┐
                   │   audit log     │
                   │  (append-only)  │
                   │  (all attempts) │
                   └─────────────────┘
```

Full map: [docs/system-map.md](docs/system-map.md)

## Verification path

To verify independently:

1. Clone any repository
2. Read the tests
3. Run the tests
4. Check git history timestamps
5. Compare terminology to any external system

Every repo uses standard engineering patterns. No proprietary frameworks. No external implementations.

Full path: [docs/verification-path.md](docs/verification-path.md)

## Terminology

This project uses mechanical terms only.

| Term | Meaning |
|---|---|
| decision record | Signed, scoped, time-bound input required for mutation |
| commit gate | Deterministic check sequence. Fail-closed. |
| execution boundary | Point where checks run before state change |
| ALLOW | Mutation proceeds |
| DENY | Mutation blocked |
| HOLD | Mutation deferred pending review |
| ESCALATE | Mutation requires higher authority |
| governed action | Action that must pass through the gate |
| audit log | Append-only record of all attempts |

Full terminology: [docs/terminology.md](docs/terminology.md)

## Invariant

See [docs/invariant.md](docs/invariant.md).

## Provenance

All repositories are independently authored by Ricky Dean Jones / Os-Trilogy LMT.

No external proprietary materials, codebases, or confidential specifications were used.

See [PROVENANCE.md](PROVENANCE.md).

## Licence

MIT — see [LICENSE](LICENSE).

---

All behaviour is defined by code and tests at each repository's stated scope. No additional interpretation is required.
