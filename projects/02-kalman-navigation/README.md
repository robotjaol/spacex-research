# Kalman navigation with observation outage

L02 | Intermediate | Runnable educational baseline | Priority 2 /22 | Score 4.90/5

## Problem and engineering background

Estimate position and velocity from noisy position samples, and quantify what happens when observations are unavailable.

## Mathematical model

$x_{k+1}=Fx_k+Ga_k+w_k$, $F=[[1,\Delta t],[0,1]]$, $G=[\Delta t^2/2,\Delta t]^T$, $z_k=Hx_k+v_k$, $H=[1,0]$. $Q=\sigma_a^2GG^T$, $R=\sigma_z^2$.

## Architecture and implementation

A seeded truth generator is separate from the estimator. The estimator consumes only noisy observations, known acceleration commands and its prior. Prediction continues during40–50 s observation loss; Joseph-form covariance updates occur only when a measurement exists.

## Simulation and visualization

Estimate/error/covariance CSV, error plot and matched multi-seed RMSE comparison.

## Acceptance criteria

Check covariance symmetry and positive semidefiniteness. Confirm uncertainty increases during prediction-only outage. Compare errors on identical available timestamps after 10 s, over 30 seeds; separately report outage error. Do not choose a favorable seed.

## Expected behavior and claim boundary

Expected behavior is stated in the acceptance criteria. Recorded baseline outputs are linked below; future improvements are not included in those results.

Matched Gaussian noise and process model; no calibrated IMU, bias states, time synchronization or real GNSS. A lower simulated RMSE does not establish operational navigation accuracy.

## References and relationship to aerospace

[An Introduction to the Kalman Filter](https://www.cs.utexas.edu/~pstone/Courses/393Rfall15/readings/Welch%2BBishop-TR-95.pdf); [Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add bias and timing errors, tune on a separate seed set, then evaluate NIS/NEES and an EKF with independent sensor models.

## Run the baseline

From the repository root, after installation:

```bash
aero-lab navigation --output outputs/navigation --seed 7
```

Model implementation: [models.py](../../src/aerolab/models.py). Reporting: [cli.py](../../src/aerolab/cli.py). Tests: [test_models.py](../../tests/test_models.py). Recorded output: [navigation.png](../../examples/results/navigation.png). Numeric provenance: [results.json](../../examples/results/results.json).

## Detailed implementation plan

1. Freeze the equations, coordinate/sign conventions, units and scenario inputs in a model card before adding complexity.
2. Preserve an independent analytic or failure-case oracle. Define numerical tolerances before accepting the result; do not tighten or loosen them solely to make the run pass.
3. Keep scenario generation, the model, and evaluation separable. Log inputs and every failure; the plot is a view of the records.
4. Add one new physical or software assumption at a time and compare the extended model with this baseline on identical conditions.
5. Submit the source, configuration, full result table, validation argument and remaining limitations together. A numerical match establishes equation implementation, not physical validation.

Baseline state: implementation and numerical checks are complete for the narrow model above. Domain extensions remain the future-work scope.
