# Successive-convexification powered descent

L07 | Research-grade | Design only; not implemented | Priority 9 /22 | Score 4.25/5

## Problem and engineering background

Reproduce an accessible academic guidance formulation before adapting its assumptions.

## Mathematical model

Nonlinear rigid-body dynamics are linearized into sequential convex subproblems with trust regions and virtual controls.

## Architecture and implementation

Implement the normalized published case, explicit nondimensionalization and constraint handling; pin solver and transcription versions.

## Simulation and visualization

Convergence traces,6 DOF trajectory and constraint residual plots.

## Acceptance criteria

Reproduce paper conditions, independently integrate the nonlinear system, check residual virtual control and test infeasible cases and multiple meshes.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

Research-grade scope refers to methodology, not implemented maturity. Runtime depends on solver and mesh. No SpaceX control law is released.

## References and relationship to aerospace

[Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/html/1802.03827v1); [Generalized hp Pseudospectral Convex Programming for Powered Descent and Landing](https://elib.dlr.de/118313/1/Generalized_hp_pseudospectral_convex_algorithm_for_powered_descent_and_landing.pdf); [casadi/casadi](https://github.com/casadi/casadi).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Study aerodynamic constraints only after the baseline reproduces the paper.
