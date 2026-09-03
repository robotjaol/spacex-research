# Testing and validation

Scope: static fire, HIL, SIL, Monte Carlo, fault injection, system identification, model validation.

Distinguish code execution, analytic agreement, integration testing and physical validation. Keep failed trials and define denominators.

## Evidence and source use

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [SpaceX Demonstrates Astronaut Escape System for Crew Dragon Spacecraft](https://www.nasa.gov/news-release/spacex-demonstrates-astronaut-escape-system-for-crew-dragon-spacecraft/); [The Power of 10: Rules for Developing Safety-Critical Code](https://spinroot.com/gerard/pdf/P10.pdf).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Generic vertical landing feedback](../../projects/01-vertical-landing/README.md); [Kalman navigation with observation outage](../../projects/02-kalman-navigation/README.md); [Sensor voting and latched fault response](../../projects/05-avionics-fault-injection/README.md); [Monte Carlo flight dispersion harness](../../projects/14-dispersion-study/README.md).

## Missing evidence and next decision

The delivered evidence consists of software simulations and numerical checks, with no physical aerospace hardware test.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
