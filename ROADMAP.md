# Roadmap

Order work by evidence and implementation dependencies. Time allocations are planning suggestions, not measured delivery commitments. A milestone is complete only when its gate is met.

| Priority | Milestone | Deliverable | Exit gate | Status |
|---|---|---|---|---|
|0|Public research foundation|Taxonomy, sources, claims, rights and source gaps|Traceable consequential claims and explicit access limits|Complete for the bounded review|
|1|Five educational baselines|Landing, filter, orbit/coverage, thermal, faults|Analytic/failure checks, CSV/JSON outputs and verified figures|Implemented; see validation record|
|2|GitHub publication|Selected repository, default-branch commit and actual CI run|Destination resolved, push verified, CI result inspected|Blocked by integration write authorization (HTTP403)|
|3|Stress the assumptions|Actuator lag/bias, filter mismatch, coverage time refinement, stale sensors|Baseline preserved; failed scenarios retained|Planned|
|4|Independent scientific cross-check|Orbit comparison with a pinned maintained tool; public thermal/structural case|Matched units/frames/inputs and documented residuals|Planned|
|5|Constrained control|L06/L07/L11 in small benchmark cases|Independent nonlinear replay, mesh/constraint checks|Planned|
|6|Thermochemistry and materials|L08/L09/L13/L20/L21|Published regression case, licenses and conservation checks|Planned|
|7|Networks and missions|L15/L16/L19/L22|Frame/geometry tests, clear latency and operational limits|Planned|
|8|Model integration|L18 workbench and optional telemetry analysis|Verified interfaces, timing assumptions and separate integration evidence|Planned|

## Research roadmap

1. Replace partial source access with a directly readable first-party or author copy when it changes an engineering decision.
2. Review superseding vehicle/configuration and regulatory documents before refreshing any current-state claim.
3. Find genuinely public calibrated datasets for thermal, structural and sensor-model validation; reject incomplete reproductions that require hidden parameters.
4. Add benchmark input/output pairs with upstream software/database versions and license evidence.
5. Broaden antenna theory and manufacturing sources before quantitative RF or production claims.

## Contribution-sized work

Useful first contributions include an orbit frame test, a reproduced licensed benchmark, a stale-sensor case, a clarified source version or an independently justified model limit. Large architecture changes should first demonstrate a concrete numerical or reproducibility problem. A future dashboard is optional; correct model outputs take priority.
