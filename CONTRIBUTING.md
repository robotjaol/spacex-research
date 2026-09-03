# Contributing

Contributions must make the repository easier to inspect, reproduce or correct. Public-facing text uses professional English. Avoid speculative claims about internal SpaceX implementations.

## Development

Install the package using the README, then run:

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
aero-lab all --output outputs --seed 7
```

Do not replace committed example outputs until you have reviewed the changed model/configuration. Record why the result changed. Keep routine generated outputs in the ignored `outputs/` directory.

## Engineering changes

A model contribution needs a problem statement, equations and units, coordinate conventions, explicit assumptions, reproducible input origin, independent test case, acceptance criteria, output artifacts and limitations. Compare like-for-like conditions and preserve failed trials. Separate generator truth from estimator inputs and separate training runs from evaluation runs.

An optimization contribution must report feasibility and independent trajectory replay, not just a solver status. A physical-data contribution needs provenance, measurement uncertainty, calibration/context and redistribution permission. A test that duplicates the same equation in another function is weaker than an independent limiting case.

## Research changes

Add source records to `references/sources.json` with an exact title, author/organization, year or null, URL, type, review depth, relevant claim, reproduction opportunity, rights, limitations and access date. Update the topic/project note and claim ledger together. Distinguish a source you read from an index or abstract you found.

Keep official facts, academic reconstruction, engineering inference and educational approximation distinct. Do not add unavailable proprietary details, copied papers, leaked data, copyrighted diagrams or incompatible source code. Public accessibility is not a license.

## Review and licensing

Use a focused pull request stating the problem, changed behavior and validation. Contributions to original project material are under the MIT License. Third-party components retain their own terms and require provenance and a compatibility review before incorporation. There is no contributor agreement or automated publication workflow in this initial repository.

If an issue is a numerical discrepancy, include the command, seed, inputs, package versions, expected behavior and actual output. For interpretation disputes, cite the exact source scope and explain which claim should change.
