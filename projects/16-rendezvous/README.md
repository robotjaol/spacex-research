# Orbital rendezvous state-machine study

L16 | Advanced | Design only; not implemented | Priority 8 /22 | Score 4.35/5

## Problem and engineering background

Connect relative-motion estimation to staged approach/hold/abort logic in an educational mission.

## Mathematical model

Begin with two independently propagated Cartesian orbits; subtract positions in a explicitly defined frame before any relative-motion linearization.

## Architecture and implementation

Build a state machine with approach corridors and bounded commands using synthetic initial conditions.

## Simulation and visualization

Relative trajectory and state-transition report.

## Acceptance criteria

Compare relative and absolute formulations, check frame transforms and exercise abort/hold transitions.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

No Dragon perception stack, ISS procedure or autonomous docking certification.

## References and relationship to aerospace

[SpaceX Crew Dragon Completes First NASA Commercial Crew Flight Test](https://www.nasa.gov/wp-content/uploads/2015/05/spm_march_2019_web.pdf); [Revisiting Spacetrack Report#3](https://celestrak.org/publications/AIAA/2006-6753/AIAA-2006-6753-Rev3.pdf); [tudat-team/tudatpy](https://github.com/tudat-team/tudatpy); [CS-SI/Orekit](https://github.com/CS-SI/Orekit).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add a sourced relative-motion model and estimator timing errors.
