# Inspection Surface

A public index for deterministic control systems and runtime proof repositories.

**Invariant:**
No valid decision record -> no state mutation.

This repository exists to make inspection easy.

It links to:
- the minimal runtime proof
- the supporting repositories
- the provenance statement
- the verification path

No external context is required.

## Start here

If you only open one repository, open:

**[runtime-commit-gate-demo](https://github.com/LalaSkye/runtime-commit-gate-demo)**

A minimal execution boundary showing that state does not change without a valid decision record.

Verify locally:

```bash
git clone https://github.com/LalaSkye/runtime-commit-gate-demo
cd runtime-commit-gate-demo
pip install -r requirements.txt
python demo/run_demo.py
python -m pytest tests/ -v
```

Expected: 5-step proof sequence. 13 passing tests. 1 allowed, 4 blocked.

## Repository index

Each repository implements one control primitive or proof.

| Repository | What it does | Tests |
|---|---|---|
| [runtime-commit-gate-demo](https://github.com/LalaSkye/runtime-commit-gate-demo) | Execution boundary. Decision record required for mutation. | 13 |
| [start-here](https://github.com/LalaSkye/start-here) | Canonical governance demo. 8-stage evaluator pipeline. | 134 |
| [execution-boundary-lab](https://github.com/LalaSkye/execution-boundary-lab) | Gate interface. 6 contamination cases. Adversarial suite. | yes |
| [constraint-workshop](https://github.com/LalaSkye/constraint-workshop) | Deterministic control primitives. Formal specs. | yes |
| [stop-machine](https://github.com/LalaSkye/stop-machine) | Three-state stop controller. Terminal state enforcement. | yes |
| [admissible-transition-lab](https://github.com/LalaSkye/admissible-transition-lab) | Transition system with admissibility enforcement. | yes |
| [execution-gate-litmus](https://github.com/LalaSkye/execution-gate-litmus) | Tests whether governance actually exists. | yes |
| [invariant-lock](https://github.com/LalaSkye/invariant-lock) | Refuses execution unless version increments. | yes |
| [deterministic-lexicon](https://github.com/LalaSkye/deterministic-lexicon) | Fixed-term vocabulary. No inference. | yes |
| [policy-lint](https://github.com/LalaSkye/policy-lint) | Governance statement linter. 0-1 scoring. | yes |
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
                    │  (10 checks)     │
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

## Provenance

All repositories are independently authored by Ricky Dean Jones / Os-Trilogy LMT.

No external proprietary materials, codebases, or confidential specifications were used.

See [PROVENANCE.md](PROVENANCE.md).

## Licence

MIT — see [LICENSE](LICENSE).

---

This repository demonstrates deterministic control using standard engineering techniques. No proprietary frameworks or external implementations are used.
