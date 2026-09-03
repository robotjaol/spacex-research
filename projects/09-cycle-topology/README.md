# Generic rocket-cycle balance graph

L09 | Advanced | Design only; not implemented | Priority 11 /22 | Score 4.20/5

## Problem and engineering background

Compare gas-generator and full-flow topologies without inventing internal engine parameters.

## Mathematical model

Stream mass/enthalpy balances plus pump/turbine shaft-power residuals define a graph model; efficiencies are explicitly assumed.

## Architecture and implementation

Build an original zero-dimensional component graph and a normalized example, separating topology from calibrated component maps.

## Simulation and visualization

Flow graph, balance residuals and normalized sensitivity chart.

## Acceptance criteria

Close all mass, energy and shaft balances; flag underdetermined parameter sets and sensitivity to assumed efficiencies.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

Not a Raptor or Merlin reconstruction; missing component maps prevent validated performance prediction.

## References and relationship to aerospace

[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf); [Statement before the House Armed Services Subcommittee on Strategic Forces](https://docs.house.gov/meetings/AS/AS29/20150317/103135/HHRG-114-AS29-Wstate-ShotwellG-20150317.pdf); [Computer Program for Calculation of Complex Chemical Equilibrium Compositions and Applications. Part 1: Analysis](https://ntrs.nasa.gov/citations/19950013764); [OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO); [Cantera/cantera](https://github.com/Cantera/cantera).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Add an independently licensed published engine benchmark if complete boundary conditions become available.
