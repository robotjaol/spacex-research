# Aerodynamics

Scope: CFD, supersonic flow, hypersonic flow, reentry aerodynamics, drag modeling, stability, grid fins.

Match the solver to its physical regime. Panel models, low-speed CFD and reacting hypersonic solvers have different assumptions.

## Evidence and source use

[MIT AVL User Primer: AVL3.36](https://web.mit.edu/drela/Public/web/avl/AVL_User_Primer.pdf); [JSBSim-Team/jsbsim](https://github.com/JSBSim-Team/jsbsim); [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev); [su2code/SU2](https://github.com/su2code/SU2).

These sources support the narrower claims recorded in the [source database](../../references/sources.json). Listing a subtopic is a coverage commitment, not proof that every implementation detail is public.

## Reproducible work

[Reentry point-mass sensitivity](../../projects/10-reentry-sensitivity/README.md); [Grid-fin control-effectiveness study](../../projects/12-grid-fin-surrogate/README.md).

## Missing evidence and next decision

The current experiments do not implement CFD. Full-scale hypersonic validation is beyond the laptop baseline.

Any new quantitative model must declare its input origin, units, reference frame, numerical method and independent validation case. Add a claim record before changing the public-information label.
