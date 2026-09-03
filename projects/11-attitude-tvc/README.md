# Attitude and thrust-vector control comparison

L11 | Advanced | Design only; not implemented | Priority 7 /22 | Score 4.45/5

## Problem and engineering background

Compare PID and LQR around the same generic attitude operating point.

## Mathematical model

$I\ddot\theta=\tau$, with actuator saturation and optional first-order lag. Linearization and gain units must be explicit.

## Architecture and implementation

Begin with a one-axis rigid body and independent actuator model; compare identical disturbances, sensors and actuator limits.

## Simulation and visualization

Angle/control histories, settling-time and effort comparisons.

## Acceptance criteria

Check inertia/torque units, closed-loop poles, step-response bounds and saturation recovery; add Monte Carlo variations.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

No flight-qualified gains or specific gimbal geometry; an MPC extension remains separately scoped.

## References and relationship to aerospace

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/html/1802.03827v1); [casadi/casadi](https://github.com/casadi/casadi); [JSBSim-Team/jsbsim](https://github.com/JSBSim-Team/jsbsim).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Extend to quaternion kinematics with norm checks and frame-convention tests.
