# System Map

## Core flow

```
input (request + decision record)
  │
  ▼
commit gate
  │
  ├── CHECK 1:  record exists?          → NO  → BLOCKED
  ├── CHECK 2:  verdict == ALLOW?       → NO  → BLOCKED
  ├── CHECK 3:  signature valid?        → NO  → BLOCKED
  ├── CHECK 4:  not expired?            → NO  → BLOCKED
  ├── CHECK 5:  nonce unused?           → NO  → BLOCKED
  ├── CHECK 6:  action matches?         → NO  → BLOCKED
  ├── CHECK 7:  object matches?         → NO  → BLOCKED
  ├── CHECK 8:  environment matches?    → NO  → BLOCKED
  ├── CHECK 9:  policy version valid?   → NO  → BLOCKED
  ├── CHECK 10: action is governed?     → NO  → BLOCKED
  │
  ▼
ALL PASS
  │
  ├── consume nonce
  ├── apply mutation → state store
  └── log result → audit log (ALLOWED)

On any failure:
  ├── no mutation
  └── log result → audit log (BLOCKED + reason code)
```

## Repository relationships

```
deterministic-lexicon          ← vocabulary primitives
  │
invariant-lock                 ← version enforcement
  │
stop-machine                   ← state controller
  │
constraint-workshop            ← formal specs
  │
  ├── execution-boundary-lab   ← gate interface + contamination
  ├── execution-gate-litmus    ← governance existence test
  ├── admissible-transition-lab ← transition enforcement
  ├── interpretation-boundary-lab ← pre-verdict admissibility
  └── dual-boundary-admissibility-lab ← rotation corridor
  │
start-here                     ← canonical demo (134 tests)
  │
runtime-commit-gate-demo       ← minimal proof (13 tests)
  │
inspection-surface             ← this index
```

## Measurement layer

```
policy-lint     ← statement analysis (input quality)
csgr-lab        ← drift measurement (output stability)
```

## Public surface

```
trilogyos-surface ← explains behaviour, does not enable replication
```
