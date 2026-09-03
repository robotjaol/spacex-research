# Methalox equilibrium sensitivity

L08 | Advanced | Design only; not implemented | Priority 10 /22 | Score 4.20/5

## Problem and engineering background

Compare equilibrium composition and thermodynamic outputs across documented boundary conditions.

## Mathematical model

Constrained Gibbs-energy minimization enforces element balances; distinguish equilibrium from frozen expansion assumptions.

## Architecture and implementation

Wrap NASA CEA or Cantera in a versioned input/output adapter; use published example problems before educational sweeps.

## Simulation and visualization

Temperature/species/sensitivity plots and reproducible input deck.

## Acceptance criteria

Close element and energy balances, reproduce a documented regression case and record mechanism/database versions.

## Expected behavior and claim boundary

This is a design proposal. The expected deliverable is the stated comparison or residual plot; no achieved numerical result, runtime or validated implementation is claimed.

Equilibrium chemistry is not combustion stability, heat flux, engine life or full Raptor performance.

## References and relationship to aerospace

[Computer Program for Calculation of Complex Chemical Equilibrium Compositions and Applications. Part 1: Analysis](https://ntrs.nasa.gov/citations/19950013764); [Computer Program for Calculation of Complex Chemical Equilibrium Compositions and Applications. II. Users Manual and Program Description](https://rocketcea.readthedocs.io/en/latest/_static/CEA_User_Manual_(NASA_RP-1311).pdf); [Statement before the House Armed Services Subcommittee on Strategic Forces](https://docs.house.gov/meetings/AS/AS29/20150317/103135/HHRG-114-AS29-Wstate-ShotwellG-20150317.pdf); [Cantera/cantera](https://github.com/Cantera/cantera); [nasa/cea](https://github.com/nasa/cea).

These sources provide public context or generic methods. Any connection to SpaceX is educational unless a specific source explicitly documents it. Equations and code here do not establish internal implementation.

## Future work

Cross-compare packages using the same species and thermodynamic assumptions.
