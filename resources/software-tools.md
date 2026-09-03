# Software and simulation tools

The default experiments use Python, NumPy, SciPy and Matplotlib on a CPU. There is no GPU, aerospace hardware, cloud account or live-data requirement. The recorded run is Linux/Python 3.12; Windows/macOS are intended targets but were not tested in this workspace.

| Layer | Preferred starting point | Advanced alternative | Decision |
|---|---|---|---|
| Dynamics / estimation | NumPy + SciPy | Tudatpy, Orekit, JSBSim | Start from analytic test cases; add a tool only for a specific model need |
| Trajectory optimization | SciPy for small prototypes | OpenMDAO/Dymos, CasADi | Verify derivatives and continuous constraints separately |
| Equilibrium chemistry | No default chemistry dependency | NASA CEA, Cantera | Match thermodynamic datasets before comparing outputs |
| Satellite networks | Synthetic geometry | Hypatia / ns-3 | Add packet queues and protocols only after geometry verification |
| Flight software | Python state-machine experiment | F Prime or cFS | An architectural reference is not certification |
| CFD | Analytical baseline first | SU2 or OpenFOAM | Begin with small2D meshes and published convergence cases |
| CAD / FEA | Beam theory and original simple geometry | FreeCAD, DOLFINx | CAD plausibility does not establish structural validity |

Purpose, language, licensing, maintenance and documentation assessments for each named package are in the [repository catalogue](github-projects.md). CalculiX, PyTorch, PyBullet and MATLAB alternatives remain possible future choices, not evaluated dependencies. Adding every available package would increase setup cost without improving the five starter experiments.
