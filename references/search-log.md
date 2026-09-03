# Search and review log

Date:2026-09-03. This is a query-family and decision log, not a verbatim browser transcript.

| Lane | Queries / source routes used | Result and follow-up |
|---|---|---|
| Official systems |SpaceX Falcon user guide; Starship FAA assessment; Raptor Shotwell testimony|Readable Falcon guide and congressional testimony; verified cycle/material claims|
| Regulators |FAA Boca Chica/LC-39A project indexes; FCC Gen2 authorization DA26-36|Preserved assessed/authorized scope and date; avoided fleet/cadence extrapolation|
| Satellites/patents |Starlink brightness mitigation; Mini specifications; SpaceX antenna patent|Confirmed public architecture, device-specific specs and patent-family metadata|
| Historical tests |NASA StarshipFlight3; Crew Dragon pad abort; Dragon PICA-X; Demo-1|Separated tested event, technology-transfer account and internal implementation|
| Academic control |Szmuk Açıkmeşe successive convexification; Sagliano hp pseudospectral; Welch Bishop Kalman|Accessible manuscripts/manuals with explicit numerical/model assumptions|
| Thermochemistry/thermal |NASA CEA RP 1311; Adler Martins cryogenic boil-off model|PartII mirror readable;PartI text-review gap retained; tank-data reproduction limitation recorded|
| Networking/verification |Hypatia IMC 2020; Vallado Spacetrack Report3; Holzmann Power of 10; Lamport Byzantine Generals|Used appropriate model-specific checks; avoided misapplying distributed-consensus guarantees|
| Aero/structures |MIT AVL primer; MIT2.080 beam lecture|Established limited-regime validation starting points|
| Upstream software |Official GitHub metadata for 22 repositories; README/license files where applicable|Recorded archive flag, last push, docs scope, rights and adoption role|
| Numerical API/data |NASA JPL constants; CelesTrak GP formats; SciPy solve_ivp docs and installed API|Kept synthetic states separate from GP elements; recorded web-extraction limitation|

Example coordinator queries included `site.github.com OpenMDAO dymos license trajectory optimization`, `site.github.com nasa fprime license flight software`, `site.github.com cantera cantera license equilibrium`, `site.github.com tudat-team tudatpy license`, `site.github.com/spacex official SpaceX open source` and `site.nasa.gov orbit two body equation gravitational parameter earth`.

One guessed SpaceX repository path returned404 and was excluded. The GitHub generic fetch route rejected README endpoints; the supported file route and returned directory listings were used instead. Case-sensitive README names for Dymos and GMAT were resolved from those listings. Failures did not become source claims.

Review stopped after 51 curated records covered the defined taxonomy and model decisions, primary evidence supported consequential claims, and remaining gaps were unlikely to be closed by repeating broad queries. No claim of exhaustive discovery is made.
