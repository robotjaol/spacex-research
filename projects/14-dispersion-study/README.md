# Monte Carlo flight dispersion harness

L14 | Intermediate | Design only; not implemented | Priority 14 /22 | Score 4.15/5

## Problem and engineering background

Measure model sensitivity across a declared distribution instead of selecting attractive trials.

## Mathematical model

For outputs $y=f(x)$, propagate explicitly stated parameter distributions; distinguish aleatory variation from model uncertainty.

## Architecture and implementation

Wrap an existing validated model with seed recording, failed-run retention and incremental summaries.

## Simulation and visualization

Dispersion plots and replayable trial records.

## Acceptance criteria

Use analytic linear uncertainty propagation as a benchmark; report sample size, quantiles, failure counts and convergence.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

Assumed distributions are not empirical SpaceX reliability data; tails need more than a small sample.

## References and relationship to aerospace

[Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/html/1802.03827v1); [An Introduction to the Kalman Filter](https://www.cs.utexas.edu/~pstone/Courses/393Rfall15/readings/Welch%2BBishop-TR-95.pdf); [RocketPy-Team/RocketPy](https://github.com/RocketPy-Team/RocketPy).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add sensitivity screening and separate model-form uncertainty.
