# Laptop project catalogue

Twenty-two scoped projects connect public evidence to original experiments. Five include runnable baselines. The remaining17 are implementation plans, with no code or results claimed. Scores are maintainer judgment about value and feasibility, not empirical benchmarks.

Weights: technical20%, portfolio15%, aerospace15%, laptop25%, learning10%, visualization10%, collaboration5%. Each criterion uses1–5; the weighted result remains on a 1–5 scale. Laptop practicality receives the largest weight because transparent, repeatable results are the first deliverable. Scores and future effort estimates should be revisited after implementation.

| Rank | Project | Level | Tech | Portfolio | Aerospace | Laptop | Learn | Visual | Collab | Score | Status |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
|1|[Generic vertical landing feedback](01-vertical-landing/README.md)|Intermediate|5 | 5 | 5 | 5 | 5 | 5 | 4|4.95|Runnable|
|2|[Kalman navigation with observation outage](02-kalman-navigation/README.md)|Intermediate|5 | 5 | 5 | 5 | 5 | 4 | 5|4.90|Runnable|
|3|[Two-body orbit and synthetic constellation coverage](03-orbit-coverage/README.md)|Intermediate|4 | 5 | 5 | 5 | 5 | 5 | 5|4.80|Runnable|
|4|[Sensor voting and latched fault response](05-avionics-fault-injection/README.md)|Beginner|5 | 5 | 5 | 5 | 5 | 3 | 5|4.80|Runnable|
|5|[Lumped cryogenic thermal warmup](04-cryogenic-thermal/README.md)|Beginner|4 | 5 | 4 | 5 | 5 | 4 | 5|4.55|Runnable|
|6|[Launch trajectory transcription](06-launch-trajectory/README.md)|Advanced|5 | 5 | 5 | 3 | 5 | 5 | 4|4.45|Planned|
|7|[Attitude and thrust-vector control comparison](11-attitude-tvc/README.md)|Advanced|5 | 5 | 5 | 3 | 5 | 5 | 4|4.45|Planned|
|8|[Orbital rendezvous state-machine study](16-rendezvous/README.md)|Advanced|5 | 5 | 5 | 3 | 4 | 5 | 4|4.35|Planned|
|9|[Successive-convexification powered descent](07-convex-powered-descent/README.md)|Research-grade|5 | 5 | 5 | 2 | 5 | 5 | 5|4.25|Planned|
|10|[Methalox equilibrium sensitivity](08-methalox-equilibrium/README.md)|Advanced|5 | 4 | 5 | 3 | 5 | 4 | 4|4.20|Planned|
|11|[Generic rocket-cycle balance graph](09-cycle-topology/README.md)|Advanced|5 | 4 | 5 | 3 | 5 | 4 | 4|4.20|Planned|
|12|[Inter-satellite routing experiment](15-isl-routing/README.md)|Advanced|4 | 5 | 5 | 3 | 4 | 5 | 5|4.20|Planned|
|13|[Phased-array beam pattern explorer](19-array-pattern/README.md)|Intermediate|4 | 4 | 4 | 4 | 5 | 5 | 4|4.20|Planned|
|14|[Monte Carlo flight dispersion harness](14-dispersion-study/README.md)|Intermediate|4 | 4 | 4 | 4 | 5 | 4 | 5|4.15|Planned|
|15|[Reusable-vehicle model integration workbench](18-model-integration/README.md)|Research-grade|5 | 5 | 5 | 2 | 4 | 5 | 5|4.15|Planned|
|16|[Reentry point-mass sensitivity](10-reentry-sensitivity/README.md)|Advanced|5 | 5 | 5 | 2 | 4 | 5 | 4|4.10|Planned|
|17|[Analytic-to-FEA structural benchmark](13-structural-benchmark/README.md)|Intermediate|4 | 4 | 4 | 4 | 5 | 4 | 4|4.10|Planned|
|18|[Two-tank cryogenic transfer balance](21-fluid-transfer/README.md)|Advanced|5 | 4 | 5 | 3 | 4 | 4 | 4|4.10|Planned|
|19|[Synthetic telemetry anomaly detection](17-telemetry-anomalies/README.md)|Intermediate|4 | 5 | 3 | 4 | 4 | 4 | 5|4.05|Planned|
|20|[Launch-window geometry explorer](22-launch-window/README.md)|Intermediate|4 | 4 | 5 | 3 | 4 | 5 | 4|4.00|Planned|
|21|[Manufacturing tolerance propagation](20-manufacturing-variation/README.md)|Intermediate|4 | 4 | 3 | 4 | 4 | 4 | 4|3.85|Planned|
|22|[Grid-fin control-effectiveness study](12-grid-fin-surrogate/README.md)|Research-grade|4 | 4 | 5 | 2 | 4 | 5 | 4|3.75|Planned|

## First implementation sequence

UseL01 to establish dynamics/contact checks, L02 to separate truth from estimates, L03 to add frame and conservation checks, L05 to exercise fault behavior, and L04 to establish thermal balances. This gives five distinct validation disciplines before expensive coupled models. The sequence follows the top five scores; folder numbering is stable for citations.

Default experiments use small arrays and CPU integration. The example run records its environment and elapsed time in [results.json](../examples/results/results.json). That hosted-runtime observation is not a laptop speed guarantee. Advanced projects should start with an8–16 GB RAM planning budget and small meshes; these are unmeasured design targets. Full-scale reacting hypersonic CFD and constellation-scale packet simulation are outside the baseline laptop promise.
