# Guidance, navigation and control

Scope: launch dynamics, trajectory optimization, state estimation, Kalman filtering, sensor fusion, attitude determination, attitude control, TVC, MPC, optimal control, fault-tolerant control.

Build verified state propagation and estimation before optimization. Frames, sample times and actuator limits are part of the model.

## Evidence and source use

[Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/html/1802.03827v1); [Generalized hp Pseudospectral Convex Programming for Powered Descent and Landing](https://elib.dlr.de/118313/1/Generalized_hp_pseudospectral_convex_algorithm_for_powered_descent_and_landing.pdf); [An Introduction to the Kalman Filter](https://www.cs.utexas.edu/~pstone/Courses/393Rfall15/readings/Welch%2BBishop-TR-95.pdf); [Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Generic vertical landing feedback](../../projects/01-vertical-landing/README.md); [Kalman navigation with observation outage](../../projects/02-kalman-navigation/README.md); [Launch trajectory transcription](../../projects/06-launch-trajectory/README.md); [Successive-convexification powered descent](../../projects/07-convex-powered-descent/README.md); [Attitude and thrust-vector control comparison](../../projects/11-attitude-tvc/README.md).

## Missing evidence and next decision

Academic algorithms are not evidence of SpaceX implementation; modern optimal-control labels require actual constrained solver code.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
