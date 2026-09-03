# Public SpaceX engineering research: findings and implementation strategy

Audience: engineers, independent researchers and open-source contributors. Evidence review:3 September 2026. Scope: the systems and technical families in the attached research brief, with public and legally accessible evidence. The repository uses English and targets a CPU-based laptop learning workflow. It is independent and unaffiliated with SpaceX.

## Direct finding

A defensible public repository can connect documented system architecture to original engineering models, academic methods and reproducible tests. The evidence does not support a complete reconstruction of SpaceX's proprietary engineering assets. The useful deliverable is therefore a traceable research baseline with five functioning educational experiments and explicit plans for 17 further projects.

The source set contains 13 system/government/patent records,12 academic or technical-method references,4 data/API references and 22 upstream software records. Counts describe this bounded review, not all available SpaceX information. The [taxonomy](technology-taxonomy.md) covers the requested subject families; topic inclusion must not be mistaken for public availability of every implementation detail.

## What the evidence establishes

| Claim family | Strongest public anchor | Supported boundary |
|---|---|---|
| Falcon architecture |[Falcon User's Guide](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf)|Customer-facing propulsion, interfaces and verification information; no full vehicle source/CAD release|
| Raptor cycle |[Statement before the House Armed Services Subcommittee on Strategic Forces](https://docs.house.gov/meetings/AS/AS29/20150317/103135/HHRG-114-AS29-Wstate-ShotwellG-20150317.pdf)|Historical LOX/methane full-flow architecture statement; no current component maps|
| Starship materials |[Final Tiered Environmental Assessment: Starship/Super Heavy Increased Cadence at Boca Chica](https://www.faa.gov/media/94346)|Materials in an assessed configuration; no certified property database|
| Starship fluid transfer |[NASA Artemis Mission Progresses with SpaceX Starship Test Flight](https://www.nasa.gov/directorates/esdmd/artemis-campaign-development-division/human-landing-system-program/nasa-artemis-mission-progresses-with-spacex-starship-test-flight/)|Internal transfer test account; no proof of completed ship-to-ship refueling|
| Starlink architecture |[Brightness Mitigation Best Practices for Satellite Operators](https://starlink.com/public-files/BrightnessMitigationBestPracticesSatelliteOperators.pdf)|First-party antenna/link concepts; not independent service-performance validation|
| Starlink authorization |[SpaceX NGSO Satellite System: Authorization and Order, DA 26-36](https://docs.fcc.gov/public/attachments/DA-26-36A1.pdf)|Dated authorized scope; not an on-orbit satellite census|
| Additive manufacturing |[SpaceX Demonstrates Astronaut Escape System for Crew Dragon Spacecraft](https://www.nasa.gov/news-release/spacex-demonstrates-astronaut-escape-system-for-crew-dragon-spacecraft/)|A documented printed SuperDraco chamber example; no process recipe|
| Patents |[Antenna modules for phased array antennas, US11018436B2](https://patents.google.com/patent/US11018436B2/en)|Disclosed antenna-module concept; not proof of deployment or freedom to operate|

Official sources are strong for what an organization disclosed or a regulator authorized. They have different limits: a manufacturer statement may be promotional, an assessment may describe an upper-bound proposal, and a patent may never describe a deployed product. The repository preserves these differences in [claims.json](../references/claims.json).

## Method selection

The learning bottleneck is reliable model-to-evidence linkage. A visually convincing simulation can still have wrong units, invalid frames, hidden truth leakage or untested contact logic. The first five projects address those failure modes through independent analytic cases and explicit fault scenarios.

The landing baseline uses sampled vertical PD feedback. It does not implement the successive-convexification algorithm described by [Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time](https://arxiv.org/html/1802.03827v1). That algorithm is a separate research project requiring nonlinear replay and mesh checks. The Kalman baseline adopts a stated stochastic model and keeps its generator separate from the estimator, following the methodological scope of [An Introduction to the Kalman Filter](https://www.cs.utexas.edu/~pstone/Courses/393Rfall15/readings/Welch%2BBishop-TR-95.pdf).

Orbit propagation starts with a synthetic Cartesian state, an analytic circular solution and conservation checks. Current GP element ingestion is deferred to a model-compatible SGP4 adapter, because the element definitions and frames matter. [Revisiting Spacetrack Report#3](https://celestrak.org/publications/AIAA/2006-6753/AIAA-2006-6753-Rev3.pdf) provides public verification cases; [A New Way to Obtain GP Data (aka TLEs)](https://celestrak.org/NORAD/documentation/gp-data-formats.php) provides current-format guidance. The coverage plot is a geometric exercise, while [Exploring the Internet from space with Hypatia](https://bdebopam.github.io/papers/imc2020-hypatia.pdf) motivates a later network simulation with queues and protocols.

The thermal baseline verifies sensible heating of an abstract lump. A physical cryogenic tank requires fluid identity, pressure, phase boundaries and additional states. [Liquid hydrogen tank boil-off model for design and optimization](https://mdolab.engin.umich.edu/bibliography/Adler2025b) supplies a more advanced research direction, but its partially suppressed experimental axes limit exact public-data reproduction. The scalar median voter has a narrow independent-fault interpretation and explicitly exposes common-mode corruption; the distributed result in [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/byz.pdf) must not be transplanted to it.

## Implementation priorities and tradeoffs

The scoring matrix weighs technical20%, portfolio15%, aerospace15%, laptop25%, learning10%, visualization10% and collaboration5%. Scores are editorial judgments. The high laptop weight favors projects that can produce inspectable results with small arrays and simple dependencies. It does not imply that the advanced projects are less valuable scientifically.

The first sequence is vertical dynamics/contact handling, stochastic navigation, orbit/coverage geometry, fault-response behavior and thermal balances. These create reusable validation practices before constrained optimization and coupled systems. The full [project catalogue](../projects/README.md) records individual scores, limits and plans.

Python with NumPy/SciPy/Matplotlib is sufficient for the delivered baselines. Dymos/CasADi, CEA/Cantera, Tudatpy/Orekit, F Prime/cFS, Hypatia, SU2/OpenFOAM and FEA tools have specific future roles. Installing all of them initially would add complexity without improving the five tests. The [upstream catalogue](../resources/github-projects.md) records documentation depth and observed activity. In particular, the community SpaceX-API and poliastro are archived; the former also explicitly disclaims affiliation with SpaceX. Their historical material may remain useful, but new reproducibility work should not assume live support.

## Recorded numerical results

These values come from the shipped code and synthetic inputs. They are numerical verification observations, not physical validation or SpaceX performance estimates. Full precision, scenario masks and package versions are recorded in [results.json](../examples/results/results.json).

| Experiment | Observed result | Interpretation |
|---|---|---|
| Vertical landing |Contact velocity -0.145 m/s;50/50 sampled scenarios met the stated contact criterion|Only the selected initial-state/actuator envelope; no sensor, fuel or atmosphere model|
| Kalman navigation |Mean position RMSE 1.05 m vs 4.97 m for raw observations across 30 seeds|Matched model and identical available timestamps after 10 s; outage error reported separately|
| Orbit |Maximum analytic circular-position discrepancy 0.0040 m over two periods|Checks numerical integration against the same ideal physics, not orbit-prediction accuracy|
| Thermal |Maximum analytic discrepancy 2.1e-09 K|Checks the one-node equation only; no real tank properties|
| Fault response |All SAFE samples suppress the voted estimate|Checks the scripted policy; common-mode faults remain undetectable by agreement alone|

All plots were inspected for labels and clipping. Repository structure, references and numerical tests are covered by the verification commands. A GitHub-rendered page preview and remote CI result cannot be claimed before publication. Windows/macOS execution and clean internet dependency resolution were not tested in this workspace.

## Source rights and missing evidence

The repository contains original code, text, diagrams and synthetic outputs. It links to third-party papers instead of bundling them. The Falcon guide specifically restricts reproduction, and other public documents do not automatically grant reuse rights. Source and software licenses are recorded separately; optional mixed-license packages must be assessed at the component level before code is incorporated.

No verified public internal flight code, production CAD, complete Raptor dataset, full controller specification or complete calibration telemetry was obtained. Some current vehicle pages were not extractable, the old Starship guide path failed, and NASA NTRS direct requests blocked access for selected reports. Accessible official documents and transparently labeled academic mirrors support the included claims. These are documented access limits, not proof that no other public material exists.

## Next release gates

The selected destination is [robotjaol/spacex-research](https://github.com/robotjaol/spacex-research). Publication was attempted but GitHub rejected the initial write with HTTP403; no commit or push succeeded. Restore integration write access before publishing. Next add actuator lag and estimator model mismatch, geometry sampling convergence and timestamped sensor faults. Only after those gates should the project implement constrained optimal control or claim multi-model integration. Each addition needs a declared model, a reproducible input set, an independent validation case and a limitations statement.
