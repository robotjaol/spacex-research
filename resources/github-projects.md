# Open-source repository catalogue

Snapshot: 2026-09-03. A recent push indicates observed activity, not guaranteed support or code quality. GitHub license labels are discovery metadata; mixed components and solver plugins require separate review. No upstream source code has been copied.

| Project | Purpose / language | License evidence | Activity | Role |
|---|---|---|---|---|
| [OpenMDAO/dymos](https://github.com/OpenMDAO/dymos) | Trajectory transcription and optimization / Python | Apache-2.0 | 2026-05-13 | optional dependency |
| [OpenMDAO/OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) | Coupled multidisciplinary models and derivatives / Python | Apache-2.0 (LICENSE.txt read) | 2026-08-25 | optional dependency |
| [nasa/fprime](https://github.com/nasa/fprime) | Component-based flight software / C++ | Apache-2.0 | 2026-09-02 | reference |
| [Cantera/cantera](https://github.com/Cantera/cantera) | Thermochemistry and equilibrium / C++ | BSD-3-Clause (License.txt read) | 2026-09-02 | optional dependency |
| [tudat-team/tudatpy](https://github.com/tudat-team/tudatpy) | Astrodynamics and estimation / C++ | BSD-3-Clause | 2026-09-02 | optional dependency |
| [casadi/casadi](https://github.com/casadi/casadi) | Symbolic differentiation and nonlinear optimization / C++ | LGPL-3.0 | 2026-09-02 | optional dependency |
| [RocketPy-Team/RocketPy](https://github.com/RocketPy-Team/RocketPy) | High-power rocket six-DOF simulation / Python | MIT | 2026-08-24 | reference |
| [JSBSim-Team/jsbsim](https://github.com/JSBSim-Team/jsbsim) | Configurable flight dynamics / C++ | LGPL-2.1 | 2026-08-27 | optional dependency |
| [snkas/hypatia](https://github.com/snkas/hypatia) | LEO geometry and packet networks / C++ | MIT for satgenpy/satviz/paper; GPL-2.0 for ns3-sat-sim (LICENSE read) | 2024-05-15 | reference |
| [nasa/GMAT](https://github.com/nasa/GMAT) | Mission design and navigation / C++ | Apache-2.0 | 2026-08-25 | reference |
| [CS-SI/Orekit](https://github.com/CS-SI/Orekit) | Java space dynamics / Java | Apache-2.0 | 2026-09-02 | optional dependency |
| [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | Parametric CAD / C++ | LGPL-2.1 | 2026-09-02 | optional tool |
| [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) | CFD and heat transfer / C++ | GPL-3.0-or-later (COPYING read) | 2026-09-01 | optional tool |
| [nasa/cFS](https://github.com/nasa/cFS) | Flight software architecture / C | Apache-2.0 | 2026-09-02 | reference |
| [poliastro/poliastro](https://github.com/poliastro/poliastro) | Historical Python astrodynamics / Python | MIT | Archived; 2023-10-14 | avoid as new dependency |
| [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API) | Community launch/vehicle metadata / JavaScript | Apache-2.0 | Archived; 2024-08-17 | historical reference only |
| [nasa/cea](https://github.com/nasa/cea) | Equilibrium chemistry / Fortran | Apache-2.0 | 2026-08-28 | optional dependency |
| [su2code/SU2](https://github.com/su2code/SU2) | CFD and design optimization / C++ | LGPL-2.1 text in upstream COPYING; exact per-file later-version options not audited | 2026-09-02 | optional tool |
| [FEniCS/dolfinx](https://github.com/FEniCS/dolfinx) | Finite-element PDE models / C++ | LGPL-3.0 | 2026-09-02 | optional tool |
| [numpy/numpy](https://github.com/numpy/numpy) | Array computing / Python | BSD-3-Clause for core; installed distribution contains additional component notices | 2026-09-02 | dependency |
| [scipy/scipy](https://github.com/scipy/scipy) | Integration and numerical algorithms / Python | BSD-3-Clause | 2026-09-02 | dependency |
| [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib) | Static visualization / Python | Matplotlib license agreement (permissive); additional bundled notices apply | 2026-09-01 | dependency |

## OpenMDAO/dymos

README read: install guidance, model/phase concepts, citation and versioned documentation links. Use after analytic dynamics tests; solves a formulation, not a validated vehicle. Not installed or benchmarked in this repository.

## OpenMDAO/OpenMDAO

README provides install paths, versioned docs and reproducible-environment guidance. Use for coupled advanced models; pin release and verify derivatives. Not installed or benchmarked in this repository.

## nasa/fprime

README provides prerequisites, tutorial and component/test architecture. Optional later C++ port; not used by these Python demos and not attributed to SpaceX. Not installed or benchmarked in this repository.

## Cantera/cantera

README links tutorials, input format, examples and platform installs. Chemical equilibrium is not a full engine cycle or cooled chamber. Not installed or benchmarked in this repository.

## tudat-team/tudatpy

README documents conda guidance and substantial build prerequisites. Use in a separate environment for advanced perturbation models. Not installed or benchmarked in this repository.

## casadi/casadi

Minimal README points to external homepage/install documentation. Check solver licenses separately; verify optimizer outputs independently. Not installed or benchmarked in this repository.

## RocketPy-Team/RocketPy

README has examples, notebooks and documentation links. Its high-power-rocketry focus does not establish orbital-launcher fidelity. Not installed or benchmarked in this repository.

## JSBSim-Team/jsbsim

README describes forces, frames and batch/Python integrations. Vehicle models require independently validated aerodynamic/inertial data. Not installed or benchmarked in this repository.

## snkas/hypatia

README explains component boundaries and dependencies. Latest observed push2024; use a pinned reproducibility environment and respect mixed licenses. Not installed or benchmarked in this repository.

## nasa/GMAT

Root README.txt read; it routes installation/configuration guidance to application/. Full application manual not reviewed. Use release builds for cross-checking later; installation not tested here. Not installed or benchmarked in this repository.

## CS-SI/Orekit

README describes capabilities and requirements; contributions route to upstream GitLab. GitHub is a mirror; use official Orekit project for contribution workflow. Not installed or benchmarked in this repository.

## FreeCAD/FreeCAD

README links user docs, developer handbook and platform packages. Create original educational geometry; no SpaceX CAD included. Not installed or benchmarked in this repository.

## OpenFOAM/OpenFOAM-dev

README.org links installation, source docs and coding guide. Development branch is not a stable benchmark; small meshes only on laptops. Not installed or benchmarked in this repository.

## nasa/cFS

README explicitly explains lab-bundle scope and verification limitations. Public bundle is a starting point, not a fully verified flight distribution. Not installed or benchmarked in this repository.

## poliastro/poliastro

Historical documentation exists; repository archived. Archive status and 2023 last push favor maintained alternatives. Not installed or benchmarked in this repository.

## r-spacex/SpaceX-API

README documents endpoints and explicitly disclaims SpaceX affiliation. Archived; do not claim current telemetry, authoritative data or an official SpaceX API. Not installed or benchmarked in this repository.

## nasa/cea

README provides modern API/install guidance and examples. Modern reimplementation; freeze database versions before regression comparisons. Not installed or benchmarked in this repository.

## su2code/SU2

README includes binaries, build requirements and documentation. Begin with verified simple cases; no hypersonic validation assumed. Not installed or benchmarked in this repository.

## FEniCS/dolfinx

README links docs, platform installation and source requirements. Native dependencies increase setup cost; start with analytic beam/heat benchmarks. Not installed or benchmarked in this repository.

## numpy/numpy

Official repository reviewed at metadata level; installed API used. Direct tested dependency; numerical dtype/unit choices remain project responsibility. Tested direct dependency.

## scipy/scipy

Official repository metadata and installed API used. Direct tested dependency; integration error is distinct from model error. Tested direct dependency.

## matplotlib/matplotlib

Official repository metadata and installed plotting API used. Direct tested dependency; plots do not independently validate a model. Tested direct dependency.
