# Verification Receipts

Verification receipts are machine-readable records under `receipts/`.

The current receipt is:

- [verification-2026-08-30.json](receipts/verification-2026-08-30.json)

The earlier five-repository receipt remains available as a historical record:

- [verification-2026-07-30.json](receipts/verification-2026-07-30.json)

A receipt records the source hash, pinned downstream commits, reference/path
resolution observations, and replay status. Its canonical SHA-256 protects the
receipt object's internal consistency.

A receipt does not prove the correctness of downstream claims or convert a
`NOT_RUN` replay into evidence of success. See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md).
