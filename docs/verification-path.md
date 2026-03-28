# Verification Path

If any governed action can execute without a valid decision record, the invariant is violated.

## Step 1: Run the proof

```bash
git clone https://github.com/LalaSkye/runtime-commit-gate-demo
cd runtime-commit-gate-demo
pip install -r requirements.txt
python demo/run_demo.py
```

Expected output:
- Step 1: no decision -> BLOCKED
- Step 2: valid decision -> ALLOWED
- Step 3: replay -> BLOCKED
- Step 4: scope mismatch -> BLOCKED
- Step 5: expired -> BLOCKED

## Step 2: Run the tests

```bash
python -m pytest tests/ -v
```

Expected: 13 tests passing.

## Step 3: Read the gate

Open `src/gate.py`. Read the 10 checks. Each check has a failure code. First failure stops evaluation.

No configuration. No external calls. No inference.

## Step 4: Check the timeline

```bash
gh api repos/LalaSkye/runtime-commit-gate-demo/commits --jq '.[].commit | {date: .author.date, message: .message}'
```

Or visit the commit history on GitHub. All timestamps are recorded by GitHub, not by the author.

## Step 5: Check the broader work

The commit gate demo is one repository. The supporting primitives go back to February 2026:

```bash
gh repo list LalaSkye --json name,createdAt --jq '.[] | {name, createdAt}' --limit 20
```

## Step 6: Compare terminology

Read the code. Compare to any external system. Note:

- Different function names
- Different data structures
- Different check sequences
- Different terminology

## Step 7: Read PROVENANCE.md

Every repository includes a provenance statement declaring independent authorship and non-claims.

## What you should find

- Working code
- Deterministic checks
- Failing tests for bypass attempts
- Public timestamps
- Standard engineering patterns
- No external dependencies beyond Python stdlib + FastAPI (for optional API)
