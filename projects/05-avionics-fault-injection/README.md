# Sensor voting and latched fault response

L05 | Beginner | Runnable educational baseline | Priority 4 /22 | Score 4.80/5

## Problem and engineering background

Exercise nominal, degraded and safe states under explicit sensor faults, including what the voter cannot detect.

## Mathematical model

For three scalar readings, $\hat x=\operatorname{median}(z_1,z_2,z_3)$. With two healthy readings, the median lies between them. This bound does not hold for common-mode corruption of the healthy pair.

## Architecture and implementation

Synthetic sensors feed a finite-value and agreement check. Three agreeing values are NOMINAL; an agreeing pair is DEGRADED; missing data or no agreeing pair is SAFE. SAFE latches and suppresses estimates until an explicit reset at45 s with healthy input.

## Simulation and visualization

Time-aligned sensor traces, state-transition timeline and fault/event CSV.

## Acceptance criteria

Test one arbitrary outlier, three-way disagreement, missing/NaN data, safe-output suppression and reset semantics. Include a passing-through common-mode corruption test to expose the limitation.250 SAFE samples describe this script, not a reliability estimate.

## Expected behavior and claim boundary

Expected behavior is stated in the acceptance criteria. Recorded baseline outputs are linked below; future improvements are not included in those results.

No radiation, hardware voter, bus, watchdog timing or real-time scheduling. Two agreeing bad sensors can defeat the policy. This is not Byzantine consensus or flight-certified software.

## References and relationship to aerospace

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [The Power of 10: Rules for Developing Safety-Critical Code](https://spinroot.com/gerard/pdf/P10.pdf); [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf); [nasa/fprime](https://github.com/nasa/fprime); [nasa/cFS](https://github.com/nasa/cFS).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add timestamps/staleness, independent voter monitoring and property-based event sequences; port a small component to F Prime only after the behavior is specified.

## Run the baseline

From the repository root, after installation:

```bash
aero-lab avionics --output outputs/avionics --seed 7
```

Model implementation: [models.py](../../src/aerolab/models.py). Reporting: [cli.py](../../src/aerolab/cli.py). Tests: [test_models.py](../../tests/test_models.py). Recorded output: [avionics.png](../../examples/results/avionics.png). Numeric provenance: [results.json](../../examples/results/results.json).

## Detailed implementation plan

1. Freeze the equations, coordinate/sign conventions, units and scenario inputs in a model card before adding complexity.
2. Preserve an independent analytic or failure-case oracle. Define numerical tolerances before accepting the result; do not tighten or loosen them solely to make the run pass.
3. Keep scenario generation, the model, and evaluation separable. Log inputs and every failure; the plot is a view of the records.
4. Add one new physical or software assumption at a time and compare the extended model with this baseline on identical conditions.
5. Submit the source, configuration, full result table, validation argument and remaining limitations together. A numerical match establishes equation implementation, not physical validation.

Baseline state: implementation and numerical checks are complete for the narrow model above. Domain extensions remain the future-work scope.
