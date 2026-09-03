# Autonomous landing

Scope: boostback, entry burn, landing burn, drone-ship landing concepts, trajectory prediction, aerodynamic control, landing optimization.

Treat descent phases and moving-platform targets as separate model extensions. The implemented baseline resolves only vertical feedback and contact.

## Evidence and source use

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [Statement before the House Armed Services Subcommittee on Strategic Forces](https://docs.house.gov/meetings/AS/AS29/20150317/103135/HHRG-114-AS29-Wstate-ShotwellG-20150317.pdf); [Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/html/1802.03827v1); [Generalized hp Pseudospectral Convex Programming for Powered Descent and Landing](https://elib.dlr.de/118313/1/Generalized_hp_pseudospectral_convex_algorithm_for_powered_descent_and_landing.pdf).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Generic vertical landing feedback](../../projects/01-vertical-landing/README.md); [Successive-convexification powered descent](../../projects/07-convex-powered-descent/README.md); [Reentry point-mass sensitivity](../../projects/10-reentry-sensitivity/README.md); [Grid-fin control-effectiveness study](../../projects/12-grid-fin-surrogate/README.md).

## Missing evidence and next decision

No calibrated wind, deck motion, grid-fin database, landing-leg dynamics or ignition envelope is reconstructed.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
