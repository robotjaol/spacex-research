# Avionics

Scope: flight computers, IMUs, GNSS, navigation sensors, power electronics, communication buses, distributed avionics, redundant computing.

Separate sensor error, estimator behavior, communication failures and voter failure assumptions.

## Evidence and source use

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [An Introduction to the Kalman Filter](https://www.cs.utexas.edu/~pstone/Courses/393Rfall15/readings/Welch%2BBishop-TR-95.pdf); [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Kalman navigation with observation outage](../../projects/02-kalman-navigation/README.md); [Sensor voting and latched fault response](../../projects/05-avionics-fault-injection/README.md); [Reusable-vehicle model integration workbench](../../projects/18-model-integration/README.md).

## Missing evidence and next decision

The software voter has no hardware certification and does not model radiation or exact vehicle bus protocols.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
