# Validation record

Date: 2026-09-03. Evidence class: educational approximation with synthetic inputs. Numerical acceptance criteria were set before the first run. Tests check analytic solutions, numerical properties and scripted failures; they do not establish physical fidelity or flight readiness.

## Reproduce

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
aero-lab all --output outputs --seed 7
```

## Gates and observations

| Model | Acceptance criterion | Observed baseline | Scope |
|---|---|---|---|
| Landing contact |Closed-form free-fall time/speed; nominal speed below 1 m/s|Controlled contact -0.145 m/s at 21.09 s|Constant-mass vertical model|
| Landing refinement |Halving 20 ms step changes contact speed by less than 0.02 m/s|0.000320 m/s|Sampled control and exact ballistic contact within each step|
| Landing scenarios |Keep every trial; contact by 90 s and speed below 1 m/s|50/50 draws; initial height U[80,120] m, initial speed U[-15,-5] m/s, maximum thrust acceleration U[16,20] m/s²|Chosen independent uniform inputs; not a reliability confidence claim|
| Kalman covariance |Symmetric/PSD; uncertainty grows during observation loss|Tested; mean available-sample RMSE 1.05 m vs raw 4.97 m over 30 seeds|Identical evaluation mask t≥10 s and observations present; seed 7 outage RMSE 2.15 m|
| Orbit |Position discrepancy <1 m over two periods; relative energy and angular-momentum drift <1e-8|0.0040 m; energy 3e-10; momentum 1.5e-10|Two-body circular analytic reference only|
| Coverage |Overhead/horizon/opposite-side cases; lower mask cannot reduce counts|Geometric edge and monotonicity tests|60 s sampled synthetic visibility; resolution convergence remains future work|
| Thermal |Analytic discrepancy <1e-6 K and energy imbalance <1e-5|2.1e-09 K and 3e-08 relative|Abstract sensible-heat lump; no phase-change claim|
| Avionics |Single-outlier behavior, missing data, disagreement, safe latch/reset|SAFE estimates unavailable in all 250 scripted SAFE samples|A common-mode corruption test deliberately shows undetected error|

## Runtime and reproduction limits

The stored baseline used Python 3.12.13, NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8 on Linux. The first five-experiment run took approximately 10.0 s in the hosted environment. This is not a benchmark for a particular laptop. The final package smoke test and structural results are in [verification.json](../examples/results/verification.json).

Dependency resolution from a completely empty internet-connected environment was not tested locally. Package installation was checked in an isolated virtual environment reusing the available scientific dependencies. CI defines Python 3.11/3.12 Linux runs; its remote result must be read from GitHub Actions. Windows/macOS and all optional scientific packages remain untested.

All five generated figures were visually inspected for labels, clipping and consistency with their data. Markdown links and records are checked structurally; a hosted GitHub-rendered visual audit is not claimed. The notebook code cells are executed by the package smoke check; an interactive Jupyter front end was not tested.

## Failure interpretation

A failed solver/model gate is a failed run, not missing data to discard. Numerical agreement supports implementation of the chosen equations. Calibration and independent physical validation would require permissioned data with measurement uncertainty and matching conditions. No integrated aerospace system or operational SpaceX model has been validated here.
