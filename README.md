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
- commit-pinned evidence and lifecycle states
- hash-consistent [verification receipts](RECEIPT.md)
- [adversarial pre-review checklist](docs/adversarial-pre-review-checklist-v0.1.md) for claim surfaces before public exposure

It does not claim to inventory every repository, paper, private source, or governance object.

## What automation verifies

The workflow runs structural tests and regenerates `index.json` and the README index from `surface.yaml`. On pull requests, it fails if the committed generated outputs differ from the source record.

Automation verifies deterministic generation, required fields, unique repository names, UTC timestamp format, and generated-file consistency.

It does **not** independently verify downstream release tags, receipt paths, repository claims, or replay commands. Those remain declarations bounded by their referenced artefacts.

## Evidence model

Each entry separates lifecycle, structural evidence, and replay state. A pinned commit is stable; a moving branch is not evidence. `PATHS_RESOLVE` means the repository, proof path, and receipt path were observed at the pinned commit. `NOT_RUN` means no replay result is claimed.

See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md), [RECEIPT.md](RECEIPT.md), and the [v0.2 schema](schema/surface.schema.json).

## Public inspection standard

```text
claim → evidence object → inspection path → claim limit
```

Each public proof surface should be read only at its stated scope.

## Inspection surface index

<!-- INDEX:START -->
| Repo | Evidence | Lifecycle | Ref | Commit | Replay | Proof | Receipt |
|------|----------|-----------|-----|--------|--------|-------|---------|
| [start-here](https://github.com/LalaSkye/start-here) | `PATHS_RESOLVE` | `UNRELEASED` | `—` | [`277e3e0`](https://github.com/LalaSkye/start-here/commit/277e3e021fe33619011862cf6d08d8969383d70a) | `NOT_RUN` | `src/` | `RECEIPT.md` |
| [commit-gate-core](https://github.com/LalaSkye/commit-gate-core) | `PATHS_RESOLVE` | `UNRELEASED` | `—` | [`4af708e`](https://github.com/LalaSkye/commit-gate-core/commit/4af708e5b45be1560837363eddff8a16d11fa93b) | `NOT_RUN` | `src/commit_gate_core/` | `RECEIPT.md` |
| [receipt-chain-core](https://github.com/LalaSkye/receipt-chain-core) | `PATHS_RESOLVE` | `UNRELEASED` | `—` | [`68b9b11`](https://github.com/LalaSkye/receipt-chain-core/commit/68b9b11293e7cec886bc1c7c11577895bb568284) | `NOT_RUN` | `src/receipt_chain_core/` | `docs/PROOF_PACK_v0.1.md` |
| [refusal-receipt-chain](https://github.com/LalaSkye/refusal-receipt-chain) | `PATHS_RESOLVE` | `RELEASED` | `v0.1.1-docs` | [`f712cea`](https://github.com/LalaSkye/refusal-receipt-chain/commit/f712ceac1663f8779dabe53b06c68575d9596c4a) | `NOT_RUN` | `./` | `sample_deny_receipt.json` |
| [fail-closed-ai](https://github.com/LalaSkye/fail-closed-ai) | `PATHS_RESOLVE` | `UNRELEASED` | `—` | [`fb55cd5`](https://github.com/LalaSkye/fail-closed-ai/commit/fb55cd5417663f4423a182208a916e1c4535e774) | `NOT_RUN` | `docs/neo-guard/neo_guard/` | `docs/neo-guard/CHAIN_RECEIPT_v0.1.md` |

_Generated 2026-07-30T07:55:00+00:00 from `surface.yaml`. Verification receipt: [receipts/verification-2026-07-30.json](receipts/verification-2026-07-30.json)._
<!-- INDEX:END -->

_Edit `surface.yaml` and push; `.github/workflows/index.yml` regenerates the table above._

The generated table is pinned to older commits. It is an index snapshot, not a claim that those SHAs are current `main`.

## Key repos

**New to this work:** [start-here](https://github.com/LalaSkye/start-here) — path-local mutation demo

**Authorize-only kernel:** [commit-gate-core](https://github.com/LalaSkye/commit-gate-core) — binds exact payload bytes; does not apply them. Do not read this as a mutation gate.

**Standing versus admission:** [obligation-bound-policy-admission-lab](https://github.com/LalaSkye/obligation-bound-policy-admission-lab)

**Receipt and interrupt evidence:** [interrupt-ledger](https://github.com/LalaSkye/interrupt-ledger)

## Provenance

All public artefacts are independently authored by Ricky Dean Jones / AlvianTech unless otherwise stated.

No external proprietary materials, codebases, or confidential specifications are claimed as sources.

Timestamps are GitHub-recorded and independently verifiable.

## Licence

See individual repository licences. All architecture, methods, and system designs are the original work of Ricky Dean Jones unless otherwise stated.
