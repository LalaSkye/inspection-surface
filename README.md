# Secondary Public Inspection Index

## Public class

This repository is the routing index for the three inspection objects.
It is not a fourth inspection object.
Proofs do not inherit across the rows it lists.

**Primary entry point:** [stop-machine](https://github.com/LalaSkye/stop-machine)

`start-here` remains listed below only as a retained historical inspection
artefact, superseded by `stop-machine` and not the current entry point. Its
pinned evidence stays scoped to that historical object and does not transfer to
`stop-machine`.

This repository is a secondary, commit-pinned index of three bounded public
inspection artefacts. It is not the first URL, a product page, a system map or
a claim that the three objects compose into one architecture.

## Evidence boundary

A claim may not travel farther than the artefact that proves it. A pinned SHA
identifies the inspected version. `PATHS_RESOLVE` means the named repository,
proof path and receipt path were observed at that commit. `NOT_RUN` means this
index does not claim a fresh replay result.

## Retained inspection objects

<!-- INDEX:START -->
| Repo | Evidence | Lifecycle | Ref | Commit | Replay | Proof | Receipt |
|------|----------|-----------|-----|--------|--------|-------|---------|
| [start-here](https://github.com/LalaSkye/start-here) | `PATHS_RESOLVE` | `UNRELEASED` | `—` | [`ebe5cd5`](https://github.com/LalaSkye/start-here/commit/ebe5cd58ca3c4f87b13b1803e6281aa03027b0c9) | `NOT_RUN` | `run_demo.py` | `RECEIPT.md` |
| [commit-gate-core](https://github.com/LalaSkye/commit-gate-core) | `PATHS_RESOLVE` | `UNRELEASED` | `—` | [`a473af4`](https://github.com/LalaSkye/commit-gate-core/commit/a473af4a1fe3af81fe3c6442bdd75331f6a8126b) | `NOT_RUN` | `src/commit_gate_core/authorize.py` | `RECEIPT.md` |
| [obligation-bound-policy-admission-lab](https://github.com/LalaSkye/obligation-bound-policy-admission-lab) | `PATHS_RESOLVE` | `UNRELEASED` | `—` | [`0ac95d3`](https://github.com/LalaSkye/obligation-bound-policy-admission-lab/commit/0ac95d3439cf4ef79d2dc6873680c4be93cd0850) | `NOT_RUN` | `src/obpa_lab/` | `artifacts/release-manifest-v0.6.json` |

_Generated 2026-08-30T05:58:10+00:00 from `surface.yaml`. Verification receipt: [receipts/verification-2026-08-30.json](receipts/verification-2026-08-30.json)._
<!-- INDEX:END -->

The generated table is sourced from `surface.yaml`. Each row is a separate
object; evidence does not inherit across rows. The `start-here` row remains a
historical evidence object only.

## One sentence per object

1. **start-here** — retained historical artefact, superseded by
   `stop-machine` and not the current entry point; run `python run_demo.py`;
   on that demonstrated path, mutation does not occur without a valid decision
   record.
2. **commit-gate-core** — the unreleased authorize-only kernel binds exact
   payload bytes and returns a verdict; it never applies them.
3. **obligation-bound-policy-admission-lab** — historical admission, current
   standing and observed active state are distinct predicates in one
   single-engine in-memory harness; it is not a gate.

## What automation verifies

The workflow checks source structure, deterministic generation and internal
receipt consistency. It does not independently prove downstream behaviour,
release status, production enforcement, originality, category priority or
copying.

## Historical material

Older maps and wider repository lists are retained only as superseded records.
They are not current routing or architecture claims.

Other public repositories on the account are not these three objects. A public
name is not an inspection-object admission.

## Claim ceiling

These objects are bounded public behaviours. They do not establish production
readiness, deployment, certification, compliance, adoption, path-universal
enforcement or control of another party's agents.
