# Changelog

This file is the release record and the release checklist for this repository.

## Release discipline (applies to every tag)

- **Bounded claim** — one sentence in the relevant section below, naming what
  the artefact does at this tag. Scope qualifier required.
- **What this tag does** — entry points exercised by tests at this commit.
- **What this tag does not claim** — see `NON-CLAIMS.md`. Claim limits in
  `CLAIM_BOUNDARY.md` (per indexed repo). Disclosure surface in
  `PUBLIC_DISCLOSURE_BOUNDARY.md`.
- **Replay path** — single command that reproduces the bounded behaviour from
  a clean checkout.
- **CI status** — green on the tagged commit. Actions pinned to commit SHAs.
- **Release tag** — signed: `git tag -s vX.Y.Z -m "vX.Y.Z — <bounded claim>"`.
- **Security** — `SECURITY.md` present; disclosure address current.
- **Ownership** — `.github/CODEOWNERS` resolves to a maintained handle.
- **Receipt** — release receipt recorded in the canonical receipt path.

Format: Keep a Changelog. Versioning: SemVer.

---

## [v0.3.0] - unreleased

### Changed
- reset the current index to three separate public inspection objects
- made `start-here` the primary entry point and this repository secondary
- replaced system-composition language with object-local claims and ceilings
- refreshed pinned commits, path-resolution observations and the current receipt
- retained wider maps and the earlier receipt only as superseded records

### Claim limit
The index records three bounded objects. It does not establish architecture,
production enforcement, originality, category priority or copying.

---

## [v0.2.0] - unreleased

### Added
- commit-pinned downstream evidence entries
- explicit lifecycle, evidence and replay states
- machine-readable surface schema
- hash-consistent verification receipt
- repository-level claim and receipt boundaries
- CI receipt-consistency verification

### Changed
- generated index now distinguishes declarations, observed path resolution and replay status
- unreleased entries remain explicit and do not imply a release tag

### Claim limit
Structural and path-resolution evidence does not prove downstream claims or replay success.

---

## [v0.1.0] - unreleased

### Added
- surface.yaml source-truth inspection map
- deterministic index generation machinery
- evidence-boundary preamble and index markers
- SHA-pinned index workflow
- SECURITY.md and CODEOWNERS

### Claim limit
The claim stops where the artefact stops.
