# Launch trajectory transcription

L06 | Advanced | Design only; not implemented | Priority 6 /22 | Score 4.45/5

## Problem and engineering background

Find a feasible ascent in an original reduced-order model with an explicit terminal target.

## Mathematical model

Point-mass states $[h,v,m]$ obey force balance and $\dot m=-T/(I_{sp}g_0)$; optimize a declared control history and objective under bounds.

## Architecture and implementation

Use Dymos or CasADi after verifying the force model; begin with a vertical vacuum case and a small mesh.

## Simulation and visualization

Trajectory, mass/control histories and feasibility residuals.

## Acceptance criteria

Reintegrate controls outside the optimizer, report terminal errors, constraint violations and mesh convergence; solver success alone fails acceptance.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

No claimed SpaceX ascent profile; thrust, drag and atmosphere uncertainties dominate fidelity.

## References and relationship to aerospace

[Generalized hp Pseudospectral Convex Programming for Powered Descent and Landing](https://elib.dlr.de/118313/1/Generalized_hp_pseudospectral_convex_algorithm_for_powered_descent_and_landing.pdf); [OpenMDAO/dymos](https://github.com/OpenMDAO/dymos); [OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO); [casadi/casadi](https://github.com/casadi/casadi).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Introduce2D motion, parameter uncertainty and launch-site constraints in separately reviewed steps.
