# Claim Boundary

## Bounded claim

At a named Inspection Surface commit, the repository provides a deterministic,
machine-readable index of three selected public inspection objects and records
the structural evidence status declared for each pinned downstream commit.

The repository's automation can establish:

- that the source record satisfies its structural rules;
- that generated JSON and README output match the source record;
- that the published verification receipt is hash-consistent with
  `surface.yaml`;
- that receipt observations match the commit, reference, and replay fields in
  the source record.

## Claim limit

The Inspection Surface does not by itself prove:

- the truth or completeness of a downstream bounded claim;
- that a downstream replay command succeeds;
- that a referenced receipt proves hidden execution truth;
- that every relevant repository, paper, or governance object is indexed;
- that the three indexed objects compose into a system or architecture;
- originality, category priority, copying, adoption, audience or endorsement;
- production safety, certification, non-bypassability, or legal compliance.

A downstream claim must be inspected at its pinned repository commit and may
not travel beyond the evidence available there.
