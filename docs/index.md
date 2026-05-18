---
layout: default
title: Research Surface Map — Ricky Jones / AlvianTech
description: Public index for execution-boundary AI governance research. Repos, papers, terminology, provenance, and inspection levels.
---

# Research Surface Map

**Ricky Dean Jones / AlvianTech / TrinityOS**

Public index for execution-boundary AI governance research.

---

## What this is

A canonical, crawlable inspection index for one governance research workstream.

It lists repositories, papers, terminology, provenance, and inspection levels.

It is not a product site, authority claim, or compliance surface.

**Non-claims:**
This index does not certify safety, compliance, correctness, regulatory adequacy, production readiness, or institutional endorsement. See each repository's `NON-CLAIMS.md` or `CLAIM_BOUNDARY.md` for per-repo scope.

---

## Core question

> Where does the system physically stop?

Governance becomes real at the execution boundary: where an AI-supported system must either prove authority to act or fail closed with an inspectable refusal receipt.

---

## Repositories

### Entry points

| Repository | Description | Inspection level |
|---|---|---|
| [start-here](https://github.com/LalaSkye/start-here) | Canonical entry point. Minimal runnable governance demo. 134 tests. | Level 5 — Replayable Audit Surface |
| [inspection-surface](https://github.com/LalaSkye/inspection-surface) | Full repo index, system map, terminology, provenance. | Level 4 — Inspectable Receipt Surface |
| [interrupt-ledger](https://github.com/LalaSkye/interrupt-ledger) | Receipt schema, replay notes, stop evidence. All five dispositions. | Level 4 — Inspectable Receipt Surface |

### Execution-boundary proof surfaces

| Repository | Description | Inspection level |
|---|---|---|
| [commit-gate-core](https://github.com/LalaSkye/commit-gate-core) | Runtime commit gate. No valid DecisionRecord → no mutation. | Level 5 — Replayable Audit Surface |
| [execution-boundary-lab](https://github.com/LalaSkye/execution-boundary-lab) | Gate interface contract. Contamination cases. Adversarial suite. | Level 5 — Replayable Audit Surface |
| [runtime-commit-gate-demo](https://github.com/LalaSkye/runtime-commit-gate-demo) | Minimal 5-step commit gate proof. 13 tests. | Level 5 — Replayable Audit Surface |
| [execution-gate-litmus](https://github.com/LalaSkye/execution-gate-litmus) | Tests whether governance exists. Adversarial suite. | Level 5 — Replayable Audit Surface |

### Admissibility surfaces

| Repository | Description | Inspection level |
|---|---|---|
| [admissible-transition-lab](https://github.com/LalaSkye/admissible-transition-lab) | Transition system. Admissibility enforced at execution boundary. | Level 5 — Replayable Audit Surface |
| [interpretation-boundary-lab](https://github.com/LalaSkye/interpretation-boundary-lab) | Pre-verdict admissibility for interpretation proposals. | Level 4 — Inspectable Receipt Surface |
| [admissibility-interrogation-surface](https://github.com/LalaSkye/admissibility-interrogation-surface) | Pre-decision interrogation. First UNSATISFIED halts chain. | Level 4 — Inspectable Receipt Surface |
| [dual-boundary-admissibility-lab](https://github.com/LalaSkye/dual-boundary-admissibility-lab) | Admissibility rotation corridor. Closed constitutional runtime. | Level 4 — Inspectable Receipt Surface |
| [transition-admissibility-gate](https://github.com/LalaSkye/transition-admissibility-gate) | Gate surface for transition admissibility. | Level 4 — Inspectable Receipt Surface |

### Refusal and receipt surfaces

| Repository | Description | Inspection level |
|---|---|---|
| [fail-closed-ai](https://github.com/LalaSkye/fail-closed-ai) | Documentation surface. Fail-closed governance pattern. | Level 3 — Workflow Orchestration |
| [refusal-receipt-chain](https://github.com/LalaSkye/refusal-receipt-chain) | Minimal refusal receipt chain. | Level 4 — Inspectable Receipt Surface |
| [receipt-chain-core](https://github.com/LalaSkye/receipt-chain-core) | Prior decision receipts participate in next admissibility decision. | Level 4 — Inspectable Receipt Surface |
| [executable-state-denial-receipt](https://github.com/LalaSkye/executable-state-denial-receipt) | Receipt at the point where admissibility fails. Schema + replay verifier. | Level 5 — Replayable Audit Surface |

### Control primitives

| Repository | Description | Inspection level |
|---|---|---|
| [stop-machine](https://github.com/LalaSkye/stop-machine) | Deterministic three-state stop controller. Terminal state enforcement. | Level 5 — Replayable Audit Surface |
| [invariant-lock](https://github.com/LalaSkye/invariant-lock) | Control primitive. Refuses execution unless invariants hold. | Level 4 — Inspectable Receipt Surface |
| [deterministic-lexicon](https://github.com/LalaSkye/deterministic-lexicon) | Fixed-term vocabulary. Exact matches. No inference. | Level 3 — Workflow Orchestration |
| [constraint-workshop](https://github.com/LalaSkye/constraint-workshop) | Deterministic control primitives. Formal specs. | Level 4 — Inspectable Receipt Surface |
| [semantic-ambiguity-gate](https://github.com/LalaSkye/semantic-ambiguity-gate) | Unresolved semantic ambiguity refuses before consequence. | Level 4 — Inspectable Receipt Surface |

### Measurement and analysis

| Repository | Description | Inspection level |
|---|---|---|
| [policy-lint](https://github.com/LalaSkye/policy-lint) | Governance statement linter. Typed warnings. 0–1 scoring. No ML. | Level 4 — Inspectable Receipt Surface |
| [csgr-lab](https://github.com/LalaSkye/csgr-lab) | LLM stability and drift measurement. Hash-chained evidence. | Level 5 — Replayable Audit Surface |

### Verification and disclosure surfaces

| Repository | Description | Inspection level |
|---|---|---|
| [trilogyos-surface](https://github.com/LalaSkye/trilogyos-surface) | Public verification surface for TrilogyOS. Explains behaviour. Does not enable replication. | Level 3 — Workflow Orchestration |
| [reference-surface-validation](https://github.com/LalaSkye/reference-surface-validation) | Minimum structural evidence validation. Inspection artefact only. | Level 4 — Inspectable Receipt Surface |

---

## Inspection level key

These levels are from the [interrupt-ledger inspection framework](https://github.com/LalaSkye/interrupt-ledger).

| Level | Label | What is present |
|---|---|---|
| 1 | Conceptual Architecture | Architecture in prose or diagrams |
| 2 | UI Simulation | Interface shows governance-like behaviour |
| 3 | Workflow Orchestration | Steps sequenced as governance workflow |
| 3a | Observability Boundary | Events emitted and observable |
| 4 | Inspectable Receipt Surface | Receipts exist, have schema, can be retrieved |
| 5 | Replayable Audit Surface | Custody chains reconstructable from artefacts |
| 6 | Verifiable Cryptographic Proof | Receipts signed and independently verifiable |
| 7 | Runtime Enforcement Evidence | Downstream execution provably prevented |
| 8 | Production Interrupt Mechanism Claim | Sustained enforcement under operational conditions |

Level assignments are informational. Lower levels are legitimate positions. No level is a failure verdict.

---

## Papers

Papers include explicit claim boundaries, canonical repo links, and provenance.

| Paper | Status | Canonical repo | DOI / Preprint |
|---|---|---|---|
| *Governance at the Point of Mutation: Why Control Is Real Only When Inadmissible Transitions Are Unreachable* | Draft / under review | [commit-gate-core](https://github.com/LalaSkye/commit-gate-core) | Pending |
| *Execution-Boundary Governance: Admissibility at the Point of Consequence* | Draft | [execution-boundary-lab](https://github.com/LalaSkye/execution-boundary-lab) | Pending |

Papers are updated here as DOIs and preprint links become available.

All papers carry the following non-claim: *This paper is a research artefact. It does not constitute production guidance, compliance certification, or regulatory advice.*

---

## Terminology

These terms are reused deliberately to keep the research surface semantically coherent, not to claim ownership over the language.

| Term | Meaning |
|---|---|
| execution-boundary AI governance | Governance applied at the point where AI systems produce consequences, not before or after |
| runtime governance | Control mechanisms that operate during execution, not only at design time |
| admissibility at execution time | Determining whether a proposed action meets required conditions before execution proceeds |
| refusal receipts | Structured records showing an action was refused, what was proposed, and what check failed |
| fail-closed AI governance | Design principle: on any governance failure, the system stops rather than proceeds |
| consequence control | Governance applied specifically at the point where actions produce irreversible or externally-visible effects |
| decision record | Signed, scoped, time-bound authorisation required for governed mutation |
| commit gate | Deterministic, fail-closed check sequence at the execution boundary |
| custody chain | Ordered record of who held responsibility for an action at each step |
| stop_was_reachable | Whether a stop mechanism was available at the time a governed event occurred |

---

## Provenance

All repositories in this index are the original work of **Ricky Dean Jones** / AlvianTech unless otherwise stated.

No external proprietary materials, codebases, or confidential specifications are claimed as sources.

### Creation timeline (GitHub-recorded, independently verifiable)

| Date | Repository | What was built |
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
| 2026-05-18 | interrupt-ledger | Receipt schema, replay, stop evidence |

---

## Non-claims

This surface does not:
- certify safety of any system
- constitute compliance with any standard or regulation
- imply institutional endorsement
- prove production readiness of any repository
- claim that any system is complete or exhaustive

Each repository carries its own explicit claim boundary.

---

## Attribution

If you use, adapt, or reference this work, please retain attribution to **Ricky Dean Jones** and link to this surface or the original repository.

GitHub: [github.com/LalaSkye](https://github.com/LalaSkye)  
LinkedIn: [linkedin.com/in/ricky-jones-1b745474](https://linkedin.com/in/ricky-jones-1b745474)

---

*This surface is updated as repositories and papers are added. Last updated: 2026-05-18.*
