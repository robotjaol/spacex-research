# Generic vertical landing feedback

L01 | Intermediate | Runnable educational baseline | Priority 1 /22 | Score 4.95/5

## Problem and engineering background

Measure how sampled feedback changes contact velocity in a one-axis descent, while distinguishing controller performance from numerical contact handling.

## Mathematical model

$\dot h=v,\ \dot v=u-g$, with $u=\operatorname{clip}(g+k_p(h_* - h)-k_d v,0,u_{max})$. SI units; constant mass. Held acceleration gives $h(t+\Delta t)=h+v\Delta t+a\Delta t^2/2$.

## Architecture and implementation

A frozen configuration feeds the sampled controller, analytic ballistic segment integrator, contact detector and result recorder. The below-surface virtual setpoint gives contact rather than asymptotic hover. It is not a target penetration command for hardware.

## Simulation and visualization

Height and velocity traces, contact metrics, unpowered baseline and seeded scenario CSV.

## Acceptance criteria

Free fall must match its closed-form contact time and speed. Nominal contact must occur within 90 s with speed below 1 m/s. Halving the 20 ms step must change contact speed by less than 0.02 m/s. Report all 50 scenario draws, including failures.

## Expected behavior and claim boundary

Expected behavior is stated in the acceptance criteria. Recorded baseline outputs are linked below; future improvements are not included in those results.

No variable mass, drag, engine ignition, minimum throttle, gimbal dynamics, sensors or landing legs. A successful test cannot establish a Falcon 9 landing envelope.

## References and relationship to aerospace

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [Statement before the House Armed Services Subcommittee on Strategic Forces](https://docs.house.gov/meetings/AS/AS29/20150317/103135/HHRG-114-AS29-Wstate-ShotwellG-20150317.pdf); [Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/html/1802.03827v1); [Generalized hp Pseudospectral Convex Programming for Powered Descent and Landing](https://elib.dlr.de/118313/1/Generalized_hp_pseudospectral_convex_algorithm_for_powered_descent_and_landing.pdf).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add actuator lag and sensor bias before 2D motion; then compare controller designs under the same constraints. Implement constrained guidance as a separate project.

## Run the baseline

From the repository root, after installation:

```bash
aero-lab landing --output outputs/landing --seed 7
```

Model implementation: [models.py](../../src/aerolab/models.py). Reporting: [cli.py](../../src/aerolab/cli.py). Tests: [test_models.py](../../tests/test_models.py). Recorded output: [landing.png](../../examples/results/landing.png). Numeric provenance: [results.json](../../examples/results/results.json).

## Detailed implementation plan

1. Freeze the equations, coordinate/sign conventions, units and scenario inputs in a model card before adding complexity.
2. Preserve an independent analytic or failure-case oracle. Define numerical tolerances before accepting the result; do not tighten or loosen them solely to make the run pass.
3. Keep scenario generation, the model, and evaluation separable. Log inputs and every failure; the plot is a view of the records.
4. Add one new physical or software assumption at a time and compare the extended model with this baseline on identical conditions.
5. Submit the source, configuration, full result table, validation argument and remaining limitations together. A numerical match establishes equation implementation, not physical validation.

Baseline state: implementation and numerical checks are complete for the narrow model above. Domain extensions remain the future-work scope.
