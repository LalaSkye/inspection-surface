# Ten-Minute Inspection Path

Each command inspects a separate pinned object. Do not transfer a result to the
other rows.

## 1. Path-local mutation demo

```bash
git clone https://github.com/LalaSkye/start-here.git
cd start-here
git checkout ebe5cd58ca3c4f87b13b1803e6281aa03027b0c9
python run_demo.py
```

Ceiling: demonstrated path only; not production or architecture-wide control.

## 2. Authorize-only kernel

```bash
git clone https://github.com/LalaSkye/commit-gate-core.git
cd commit-gate-core
git checkout a473af4a1fe3af81fe3c6442bdd75331f6a8126b
python -m pip install -e ".[dev]"
PYTHONPATH=src python -m pytest tests/test_authorize.py tests/test_beau_failure_classes.py -q
```

Ceiling: payload-bound authorisation only. The kernel does not apply payloads
or stop an external caller using another route.

## 3. Admission/standing/state harness

```bash
git clone https://github.com/LalaSkye/obligation-bound-policy-admission-lab.git
cd obligation-bound-policy-admission-lab
git checkout 0ac95d3439cf4ef79d2dc6873680c4be93cd0850
PYTHONPATH=src python -m unittest discover -s tests -v
```

Ceiling: single-engine, single-writer, in-memory harness with self-authored
fixtures and oracles. It is not a production gate or external adversary result.
