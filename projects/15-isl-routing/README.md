# Inter-satellite routing experiment

L15 | Advanced | Design only; not implemented | Priority 12 /22 | Score 4.20/5

## Problem and engineering background

Compare shortest paths and disrupted routes on a time-varying synthetic constellation.

## Mathematical model

Edges require geometric line of sight; propagation delay is path length divided by light speed. Queue delay is a separate model.

## Architecture and implementation

Begin with graph snapshots fromL03; use Hypatia/ns-3 only for the packet-level extension.

## Simulation and visualization

Route animation, outage timeline and latency-component comparison.

## Acceptance criteria

Check Earth obstruction, path connectivity, symmetry assumptions and delay lower bounds; hold traffic scenarios constant.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

No Starlink routing protocol inferred; propagation-only delay is not measured internet RTT.

## References and relationship to aerospace

[Exploring the Internet from space with Hypatia](https://bdebopam.github.io/papers/imc2020-hypatia.pdf); [Brightness Mitigation Best Practices for Satellite Operators](https://starlink.com/public-files/BrightnessMitigationBestPracticesSatelliteOperators.pdf); [snkas/hypatia](https://github.com/snkas/hypatia).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Introduce congestion and handovers with pinned packet-simulator settings.
