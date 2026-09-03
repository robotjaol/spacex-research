# Technology-to-project knowledge graph

The arrows represent a learning relationship, not an assertion that SpaceX uses the named open-source package. Source IDs resolve in [sources.json](../references/sources.json); project IDs resolve in the [catalogue](../projects/catalogue.json).

```mermaid
flowchart TD
    P01["P01 Falcon public guide"] --> GNC["Dynamics, estimation and verification"]
    P02["P02 Raptor cycle disclosure"] --> THERMO["Cycle topology and thermodynamics"]
    P09["P09 Starlink public architecture"] --> NETWORK["Orbital geometry and network models"]
    GNC --> A03["A03 Kalman method"]
    GNC --> A01["A01 constrained guidance"]
    THERMO --> A07["A07 tank-model research"]
    THERMO --> CEA["A05 and A06 chemical equilibrium"]
    NETWORK --> A11["A11 propagation verification"]
    NETWORK --> A04["A04 Hypatia networking"]
    A03 --> L02["L02 runnable navigation"]
    A01 --> L07["L07 planned convex guidance"]
    A07 --> L04["L04 limited thermal baseline"]
    CEA --> L08["L08 and L09 planned chemistry/cycles"]
    A11 --> L03["L03 synthetic orbit baseline"]
    A04 --> L15["L15 planned routing"]
```

| Source family | Principle | Current model | Extension | Validation anchor |
|---|---|---|---|---|
| Falcon reliability/interface disclosures |Explicit states and fault assumptions|L05 scalar voting|F Prime/cFS component|Fault scenarios and output invariants|
| Reusable landing context |Force balance and state estimation|L01 vertical feedback;L02 filter|L07 constrained guidance|Analytic motion; independent nonlinear replay|
| Cryogenic-transfer context |Mass and energy conservation|L04 sensible heating|L21 two-tank transfer|Analytic energy balance; public property/test data|
| Starlink architecture |Orbit, visibility, connectivity|L03 synthetic geometry|L15 packets;L19 array factor|Conservation; horizon geometry; known pattern cases|
| Materials/manufacturing context |Structural response to variation|PlannedL13 beam benchmark|L20 tolerance propagation|Analytic deflection and mesh refinement|

The larger taxonomy is maintained as structured [technology-taxonomy.json](technology-taxonomy.json). It records every domain's evidence boundary and associated projects.
