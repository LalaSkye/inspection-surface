# Research Surface Map — Ricky Jones / AlvianTech

## Evidence boundary

A claim may not travel farther than the artefact that proves it.

A public artefact does not need to reveal the system. It needs to prove
one bounded behaviour:

- what was admitted,
- what was refused,
- what receipt was produced,
- and what replay shows the boundary held.

The claim stops where the artefact stops.

Per-repo boundaries are defined by each repo's `CLAIM_BOUNDARY.md`,
`NON-CLAIMS.md`, `PUBLIC_DISCLOSURE_BOUNDARY.md`, and `RECEIPT.md`.

**Canonical entry point (live):** [lalaskye.github.io/inspection-surface](https://lalaskye.github.io/inspection-surface/)

A bounded index of selected public proof repositories and their declared inspection routes.

---

## Public disclosure boundary

This repository hosts the Research Surface Map. It is a public inspection surface, not full architecture disclosure.

It shows bounded public inspection routes and claim limits. It must not be read as a system map, orchestration model, or protected architecture disclosure.

See [`NON-CLAIMS.md`](NON-CLAIMS.md) and [`PUBLIC_DISCLOSURE_BOUNDARY.md`](PUBLIC_DISCLOSURE_BOUNDARY.md).

## What this repo is

A bounded public index of selected execution-boundary proof artefacts by Ricky Dean Jones / AlvianTech.

It provides:
- selected public proof-repository entries
- scope-qualified claims
- declared replay commands and proof paths
- canonical receipt paths
- [adversarial pre-review checklist](docs/adversarial-pre-review-checklist-v0.1.md) for claim surfaces before public exposure

It does not claim to inventory every repository, paper, private source, or governance object.

## Public inspection standard

```text
claim → evidence object → inspection path → claim limit
```

Each public proof surface should be read only at its stated scope.

## Inspection surface index

<!-- INDEX:START -->
| Repo | Bounded claim | Proof path | Test command | Tag | Receipt |
|------|---------------|------------|--------------|-----|---------|
| [start-here](https://github.com/LalaSkye/start-here) | Within the scope of this unreleased inspection candidate, provides a single runnable entry point that exercises the minimal admissibility-before-effect demonstration. | `src/` | `python run_demo.py` | `UNRELEASED` | `RECEIPT.md` |
| [commit-gate-core](https://github.com/LalaSkye/commit-gate-core) | Within the scope of this unreleased inspection candidate, refuses state mutation in the absence of a valid DecisionRecord. | `src/commit_gate_core/` | `pytest -q` | `UNRELEASED` | `RECEIPT.md` |
| [receipt-chain-core](https://github.com/LalaSkye/receipt-chain-core) | Within the scope of this unreleased inspection candidate, treats prior decision receipts as inputs to the next admissibility decision. | `src/receipt_chain_core/` | `pytest -q` | `UNRELEASED` | `docs/PROOF_PACK_v0.1.md` |
| [refusal-receipt-chain](https://github.com/LalaSkye/refusal-receipt-chain) | Within the scope of this artefact at the named release tag, emits a refusal receipt at the point admissibility fails. | `./` | `python chain_verify.py` | `v0.1.1-docs` | `sample_deny_receipt.json` |
| [fail-closed-ai](https://github.com/LalaSkye/fail-closed-ai) | Within the scope of this unreleased inspection candidate, produces no downstream effect in the absence of a valid admissibility decision. | `docs/neo-guard/neo_guard/` | `cd docs/neo-guard && pytest -q` | `UNRELEASED` | `docs/neo-guard/CHAIN_RECEIPT_v0.1.md` |

_Generated 2026-07-30T07:31:45+00:00 from `surface.yaml`._
<!-- INDEX:END -->

_Edit `surface.yaml` and push; `.github/workflows/index.yml` regenerates the table above._

## Key repos

**New to this work:** [start-here](https://github.com/LalaSkye/start-here)

**Core execution-boundary proof:** [commit-gate-core](https://github.com/LalaSkye/commit-gate-core)

**Receipt and interrupt evidence:** [interrupt-ledger](https://github.com/LalaSkye/interrupt-ledger)

## Provenance

All public artefacts are independently authored by Ricky Dean Jones / AlvianTech unless otherwise stated.

No external proprietary materials, codebases, or confidential specifications are claimed as sources.

Timestamps are GitHub-recorded and independently verifiable.

## Licence

See individual repository licences. All architecture, methods, and system designs are the original work of Ricky Dean Jones unless otherwise stated.