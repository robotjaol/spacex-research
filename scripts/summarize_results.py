"""Read recorded experiment metrics; does not rerun or certify the models."""
import json
from pathlib import Path
import sys

path=Path(sys.argv[1] if len(sys.argv)>1 else 'examples/results/results.json')
record=json.loads(path.read_text())
print(f"Evidence: {record['evidence_class']}; seed={record['seed']}")
for name, metrics in record['projects'].items():
    print(f'\n{name}')
    for key,value in metrics.items():
        if isinstance(value,(float,int,bool)) or value is None:
            print(f'  {key}: {value}')
