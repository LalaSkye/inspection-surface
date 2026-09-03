# Verification Receipts

Verification receipts are machine-readable records under `receipts/`.

The current receipt is:

- [verification-2026-09-03.json](receipts/verification-2026-09-03.json)

Earlier receipts remain available as historical records and are not rewritten:

- [verification-2026-08-30.json](receipts/verification-2026-08-30.json)
- [verification-2026-07-30.json](receipts/verification-2026-07-30.json)

A receipt records the source hash, pinned downstream commits, reference/path
resolution observations, and replay status. Its canonical SHA-256 protects the
receipt object's internal consistency.

A receipt does not prove the correctness of downstream claims or convert a
`NOT_RUN` replay into evidence of success. See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md).

Pinned commits are historical evidence identities. A current receipt does not
claim that a pin is current `main` or the GitHub Latest release. The retained
`start-here` evidence does not transfer to `stop-machine`, and this surface
records no verification evidence for `stop-machine`.
