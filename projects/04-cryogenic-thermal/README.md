# Lumped cryogenic thermal warmup

L04 | Beginner | Runnable educational baseline | Priority 5 /22 | Score 4.55/5

## Problem and engineering background

Build and verify a heat-balance baseline before introducing tank pressure or phase change.

## Mathematical model

$C\dot T=UA(T_a-T)$, $T(t)=T_a+(T_0-T_a)e^{-UA t/C}$. Stored energy is $C(T-T_0)$ and heat flow is $UA(T_a-T)$.

## Architecture and implementation

An abstract effective thermal body starts at90 K with ambient120 K, capacity200000 J/K and conductance5 W/K. Numerical integration is compared with the exponential solution over 7200 s. These are chosen effective inputs, not measured fluid properties.

## Simulation and visualization

Temperature/heat-flow curves, energy balance and numerical residuals.

## Acceptance criteria

Maximum analytic error below 1e-6 K; integrated heat versus stored energy relative mismatch below 1e-5. Check equilibrium and cooling as separate limiting cases. Require a pressure/fluid-dependent phase boundary before extending into a real tank model.

## Expected behavior and claim boundary

Expected behavior is stated in the acceptance criteria. Recorded baseline outputs are linked below; future improvements are not included in those results.

Only sensible heat in an abstract lump. No fluid identity, saturation pressure, wall capacitance, latent heat, radiation or slosh; no boil-off prediction. The94.94 K output is not a validated real propellant state.

## References and relationship to aerospace

[Liquid hydrogen tank boil-off model for design and optimization](https://mdolab.engin.umich.edu/bibliography/Adler2025b); [NASA Artemis Mission Progresses with SpaceX Starship Test Flight](https://www.nasa.gov/directorates/esdmd/artemis-campaign-development-division/human-landing-system-program/nasa-artemis-mission-progresses-with-spacex-starship-test-flight/).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add separate wall/liquid nodes and validated property tables, then phase-change events and mass conservation. Compare to a public dataset before claiming tank fidelity.

## Run the baseline

From the repository root, after installation:

```bash
aero-lab thermal --output outputs/thermal --seed 7
```

Model implementation: [models.py](../../src/aerolab/models.py). Reporting: [cli.py](../../src/aerolab/cli.py). Tests: [test_models.py](../../tests/test_models.py). Recorded output: [thermal.png](../../examples/results/thermal.png). Numeric provenance: [results.json](../../examples/results/results.json).

## Detailed implementation plan

1. Freeze the equations, coordinate/sign conventions, units and scenario inputs in a model card before adding complexity.
2. Preserve an independent analytic or failure-case oracle. Define numerical tolerances before accepting the result; do not tighten or loosen them solely to make the run pass.
3. Keep scenario generation, the model, and evaluation separable. Log inputs and every failure; the plot is a view of the records.
4. Add one new physical or software assumption at a time and compare the extended model with this baseline on identical conditions.
5. Submit the source, configuration, full result table, validation argument and remaining limitations together. A numerical match establishes equation implementation, not physical validation.

Baseline state: implementation and numerical checks are complete for the narrow model above. Domain extensions remain the future-work scope.
