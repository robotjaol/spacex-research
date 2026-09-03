# Flight software

Scope: real-time architecture, fault tolerance, redundancy, state machines, telemetry, embedded software, Linux-based systems, C/C++, simulation frameworks.

Study components, explicit failure states and timing contracts using public frameworks and original tests.

## Evidence and source use

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [The Power of 10: Rules for Developing Safety-Critical Code](https://spinroot.com/gerard/pdf/P10.pdf); [nasa/fprime](https://github.com/nasa/fprime); [nasa/cFS](https://github.com/nasa/cFS).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Sensor voting and latched fault response](../../projects/05-avionics-fault-injection/README.md); [Synthetic telemetry anomaly detection](../../projects/17-telemetry-anomalies/README.md); [Reusable-vehicle model integration workbench](../../projects/18-model-integration/README.md).

## Missing evidence and next decision

Linux/C++ are ecosystem study topics here; no verified internal SpaceX operating-system or codebase inventory was obtained.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
