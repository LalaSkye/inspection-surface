# Adversarial Pre-Review Checklist v0.1

**Scope stamp:** v0.1 — scope only, not enforcement. No CI hook implied.

Use this checklist before a repo, README patch, release note, public post, or public reply cites an artefact as proof.

---

## Operating question

> What exactly proves that consequence cannot happen another way?

If the answer is not code, test, issue, scope note, receipt, or explicit out-of-scope boundary: **HOLD**.

---

## How to use this checklist

For each review class, answer:

- **PASS** — claim is proven or explicitly scoped.
- **HOLD** — claim may be true, but needs a patch, issue, test, or scope note.
- **DENY** — claim materially exceeds the artefact and is not scoped out.

Do not defend the work.
Do not make the claim louder.
Make the boundary inspectable.

---

## 1. Claim boundary

**Question:** Does the repo say more than the artefact proves?

Check:

- production readiness
- certification
- standardisation
- compliance
- adoption
- institutional validation
- full governance-system status
- current-tense wording for future work

**PASS rule:** all claims are smaller than the visible artefact.

**HOLD trigger:** any current-tense phrase describes an unimplemented hardening target.

---

## 2. Path-local vs path-universal

**Question:** Does the repo distinguish the demonstrated path from deployment-wide coverage?

Check:

- local gate claim
- path-universal claim
- alternate routes
- human handoffs
- downstream agents
- side channels
- retry and recovery paths

**PASS rule:** the repo states whether it proves one path or all reachable paths.

**HOLD trigger:** a reader could infer all paths are covered when only one path is demonstrated.

---

## 3. Proof-consequence ordering

**Question:** Can consequence occur before durable proof is written?

Check:

- audit append order
- receipt creation order
- mutation order
- failure after mutation
- post-hoc proof masquerading as precondition

**PASS rule:** proof is committed before consequence binds, or the limitation is explicit.

**HOLD trigger:** mutation can happen before durable audit or receipt.

---

## 4. Payload and effect binding

**Question:** Is the authorised proof bound to the actual mutation payload?

Check:

- payload hash
- effect descriptor
- canonical mutation representation
- callback-created side effects
- attempted action vs authorised record vs actual effect

**PASS rule:** the repo proves the authorised payload is the payload that binds.

**HOLD trigger:** proof authorises an envelope but the callback can produce another effect.

---

## 5. Atomicity

**Question:** Are proof, nonce, mutation, and audit one atomic boundary?

Check:

- nonce consumed before or after mutation
- rollback path
- rollback failure
- audit failure
- partial commit states
- transaction boundary

**PASS rule:** atomicity is implemented or explicitly out of scope.

**HOLD trigger:** separate operations are described as an atomic commit.

---

## 6. Audit and receipt failure

**Question:** What happens when audit or receipt writing fails?

Check:

- audit exception path
- receipt exception path
- silent audit failure
- uncontrolled exception escape
- specific result code
- replayable evidence

**PASS rule:** audit failure has a controlled result and cannot silently succeed.

**HOLD trigger:** a failed audit can crash, disappear, or still permit a success claim.

---

## 7. Mutable input drift

**Question:** Can validated input change before the audit receipt is written?

Check:

- mutable DecisionRecord
- callback mutation of record
- frozen snapshot
- audit uses authorised record or post-callback record

**PASS rule:** the authorised record is snapshotted before mutation or mutation cannot alter it.

**HOLD trigger:** receipt may record a different record from the one validated.

---

## 8. Condition freshness

**Question:** Is the condition behind the decision still evidenced at execution time?

Check:

- condition expiry
- evidence freshness
- state version at check
- state version at commit
- stale / unknown / out-of-scope condition

**PASS rule:** stale, unknown, or unevidenced freshness fails closed.

**HOLD trigger:** a condition can go stale between check and execution without being caught or scoped out.

---

## 9. Concurrency and replay

**Question:** Can replay protection race?

Check:

- nonce `contains` and `consume`
- transaction or lock
- two simultaneous calls
- idempotency
- replay under retry

**PASS rule:** replay protection is atomic, locked, transactional, or explicitly best-effort.

**HOLD trigger:** two calls can both pass before either consumes the nonce.

---

## 10. Inspection path

**Question:** Can a first-time inspector find the proof surface quickly?

Check:

- README links
- file paths
- repo index
- test path
- docs path
- examples path
- stale counts

**PASS rule:** links and paths resolve, and proof is findable in under one minute.

**HOLD trigger:** README points to files or folders that do not exist.

---

## 11. Test execution

**Question:** Can tests run from a clean clone?

Check:

- import configuration
- `pytest` setup
- `pyproject.toml`
- `conftest.py`
- hidden install step
- exposure tests that accidentally pass for the wrong reason

**PASS rule:** a reviewer can run the tests from a fresh clone using documented commands.

**HOLD trigger:** test collection fails before the proof tests run.

---

## 12. Public-surface readiness

**Question:** Is the repo ready to be cited publicly?

Check:

- known gaps fixed, tracked, or scoped out
- repo language smaller than evidence
- public reply points to artefacts, not reassurance
- no endorsement drift
- no adoption drift
- no validation drift

**PASS rule:** the public line can point to code, test, issue, receipt, or scope note.

**HOLD trigger:** reply would rely on reassurance rather than artefact.

---

## Required review output

Every review must return:

1. **Verdict:** PASS / HOLD / DENY
2. **Claim patches required**
3. **Issues required**
4. **Tests required**
5. **README or release-note changes required**
6. **Public posture:** REPLY / HOLD / STOP
7. **One clean line explaining why**

---

## PASS / HOLD / DENY rules

### PASS

The repo claim is smaller than the evidence.
Inspection paths work.
Tests can run.
Material gaps are fixed, tracked, or explicitly out of scope.

### HOLD

The repo is directionally honest, but at least one gap remains untracked, a path is stale, tests may not run, or wording still implies more than the artefact proves.

### DENY

The repo materially claims enforcement, proof, deployment coverage, production readiness, certification, adoption, or capability that the artefact does not support and does not scope out.

---

## Public posture gate

### REPLY

Use only when all material gaps are fixed, tracked, or scoped out.
Reply with artefacts, not reassurance.

### HOLD

Use when a known issue is not yet tracked or the claim surface still needs narrowing.

### STOP

Use when there is no new technical content, or replying would create social loop, status play, or unnecessary surface area.

---

## Claim boundary

This checklist does not prove:

- correctness
- security
- compliance
- production readiness
- adoption
- institutional validation
- path-universal enforcement

It is a pre-publication inspection aid.
It makes gaps visible earlier.

---

## Clean line

> If a claim cannot be proven, narrow it, test it, issue it, or scope it out.
