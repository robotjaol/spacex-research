# Research methodology

Review date:3 September 2026. Objective: build an independent engineering learning repository from public SpaceX context, academic methods and maintained software. Scope follows the 13-domain taxonomy. It excludes leaked/proprietary/restricted material and does not claim an exhaustive internal technology inventory.

## Source hierarchy

Prefer official technical documents, original government records, author/publisher research and upstream project documentation. Manufacturer evidence is strongest for the disclosed configuration, and regulator evidence for the precise decision. Neither automatically establishes measured operational performance. Academic papers support the model under their assumptions, not its use by SpaceX.

The source database records title, organization/authors, year or null, URL, type, topic, relevance, reproducible use, evidence actually reviewed, confidence, rights, limitations and check date. Source descriptions are concise original summaries. Code is original; optional packages are not vendored.

## Retrieval and reconciliation

Research proceeded through official system/regulator documents, academic methods and upstream software. First-pass findings were merged before follow-up. Follow-up addressed cycle/material evidence, current authorization versus fleet count, source rights, software archive status and accessible full text. High-impact cycle, materials, authorization, Kalman, orbit and tank-model claims were spot-checked before synthesis.

Persistent extraction failures were recorded, and accessible official documents or labeled author mirrors were used where available. Missing evidence stayed missing. The [gap matrix](../references/gaps.md) records limitations and the next useful retrieval action; the [search log](../references/search-log.md) records query families and the stopping rule.

## Evidence labels

Use `confirmed public information`, `academic reconstruction`, `engineering inference` or `educational approximation` at the claim/model level. Do not give an entire document a stronger label because one fact is verified. The method-reference label in the source catalogue describes the source type; the claim ledger gives the implementation's evidence class.

## Numerical claims

Set acceptance criteria before accepting a run. Record units, reference frames, seed, baseline, evaluation mask, solver/settings and package versions. Distinguish generated inputs from observations, and preserve failed trials. Check equations against an independent limiting case before interpreting a scenario. Integration accuracy, physical-model accuracy and operational success are separate quantities.

## Stopping rule and coverage limits

Stop when the requested subject families are mapped, consequential public claims have primary support or explicit gaps, the five project decisions have defensible validation cases and further broad searching mainly duplicates evidence. This review met that bounded condition. It does not establish that all public documents or repositories have been found, nor that every optional tool has been installed or benchmarked.
