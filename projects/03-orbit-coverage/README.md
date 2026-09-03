# Two-body orbit and synthetic constellation coverage

L03 | Intermediate | Runnable educational baseline | Priority 3 /22 | Score 4.80/5

## Problem and engineering background

Verify orbital propagation against an analytic circular orbit and measure geometric visibility for a chosen ground station.

## Mathematical model

$\ddot{\mathbf r}=-\mu\mathbf r/\|\mathbf r\|^3$, $T=2\pi\sqrt{r^3/\mu}$. Elevation uses $\sin e=(\boldsymbol\rho\cdot\hat{\mathbf u})/\|\boldsymbol\rho\|$, where $\boldsymbol\rho$ is station-to-satellite displacement.

## Architecture and implementation

DOP853 propagates a synthetic Cartesian state. A separate circular-shell generator creates6 planes of 12 satellites, rotates them into a simplified Earth-fixed frame and applies a 25-degree elevation mask at−7.25°,112.75°.

## Simulation and visualization

Orbit plot, state/analytic error CSV and a one-day sampled visibility trace.

## Acceptance criteria

Over two periods, require analytic position error below 1 m and relative energy/angular-momentum drift below 1e-8. Check overhead/horizon geometry and monotonicity when the mask is lowered. Coverage is a sampled fraction, not a continuous-time guarantee.

## Expected behavior and claim boundary

Expected behavior is stated in the acceptance criteria. Recorded baseline outputs are linked below; future improvements are not included in those results.

Spherical Earth, constant rotation phase, no J2, drag, real epoch, access scheduling or traffic.72 chosen satellites are not the current Starlink constellation. No TLE/OMM import is implemented.

## References and relationship to aerospace

[Astrodynamic Parameters](https://ssd.jpl.nasa.gov/astro_par.html); [Planetary Physical Parameters](https://ssd.jpl.nasa.gov/planets/phys_par.html); [A New Way to Obtain GP Data (aka TLEs)](https://celestrak.org/NORAD/documentation/gp-data-formats.php); [Exploring the Internet from space with Hypatia](https://bdebopam.github.io/papers/imc2020-hypatia.pdf); [Revisiting Spacetrack Report#3](https://celestrak.org/publications/AIAA/2006-6753/AIAA-2006-6753-Rev3.pdf); [SpaceX NGSO Satellite System: Authorization and Order, DA 26-36](https://docs.fcc.gov/public/attachments/DA-26-36A1.pdf); [Brightness Mitigation Best Practices for Satellite Operators](https://starlink.com/public-files/BrightnessMitigationBestPracticesSatelliteOperators.pdf).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add time-resolution convergence, geodetic frames and a separately validated OMM/SGP4 adapter; only then add network queues and routing.

## Run the baseline

From the repository root, after installation:

```bash
aero-lab orbit --output outputs/orbit --seed 7
```

Model implementation: [models.py](../../src/aerolab/models.py). Reporting: [cli.py](../../src/aerolab/cli.py). Tests: [test_models.py](../../tests/test_models.py). Recorded output: [orbit.png](../../examples/results/orbit.png). Numeric provenance: [results.json](../../examples/results/results.json).

## Detailed implementation plan

1. Freeze the equations, coordinate/sign conventions, units and scenario inputs in a model card before adding complexity.
2. Preserve an independent analytic or failure-case oracle. Define numerical tolerances before accepting the result; do not tighten or loosen them solely to make the run pass.
3. Keep scenario generation, the model, and evaluation separable. Log inputs and every failure; the plot is a view of the records.
4. Add one new physical or software assumption at a time and compare the extended model with this baseline on identical conditions.
5. Submit the source, configuration, full result table, validation argument and remaining limitations together. A numerical match establishes equation implementation, not physical validation.

Baseline state: implementation and numerical checks are complete for the narrow model above. Domain extensions remain the future-work scope.
