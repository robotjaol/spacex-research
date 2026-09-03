"""Offline integrity checks for research records and repository links."""
import json
from pathlib import Path
import re
import sys
import tomllib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


sources = json.loads((ROOT/'references/sources.json').read_text())
catalogue = json.loads((ROOT/'projects/catalogue.json').read_text())
projects = catalogue['projects']
source_ids = {s['id'] for s in sources}
project_ids = {p['id'] for p in projects}
require(len(source_ids) == len(sources), 'Duplicate source IDs')
require(len({s['url'] for s in sources}) == len(sources), 'Duplicate source URLs')
required = {'id','title','author_or_organization','publication_year','url','source_type',
            'technical_topics','supported_claim','why_relevant','what_can_be_reproduced',
            'evidence_seen','reliability','licensing_status','limitations','checked_at','access_status'}
for s in sources:
    require(required <= s.keys(), f"Missing source fields: {s['id']}")
    require(urlsplit(s['url']).scheme == 'https', f"Non-HTTPS source: {s['id']}")
require(len(project_ids) >= 15, 'Insufficient project concepts')
require(sum(bool(p['command']) for p in projects) == 5, 'Expected five runnable baselines')
for p in projects:
    require(set(p['source_ids']) <= source_ids, f"Unknown source in {p['id']}")
    value = sum(p['scores'][key]*weight for key,weight in catalogue['weights'].items())
    require(abs(round(value,2)-p['weighted_score']) < 1e-8, f"Score mismatch: {p['id']}")
    require((ROOT/'projects'/p['slug']/'README.md').is_file(), f"Missing project plan: {p['id']}")
for t in json.loads((ROOT/'docs/technology-taxonomy.json').read_text()):
    require(set(t['source_ids']) <= source_ids, f"Unknown taxonomy source: {t['id']}")
    require(set(t['project_ids']) <= project_ids, f"Unknown taxonomy project: {t['id']}")
for c in json.loads((ROOT/'references/claims.json').read_text()):
    require(set(c['source_ids']) <= (source_ids | project_ids), f"Unknown claim reference: {c['id']}")

links_checked = 0
for doc in ROOT.rglob('*.md'):
    if any(p in {'.venv','build','dist'} or p.endswith('.egg-info') for p in doc.parts):
        continue
    body = doc.read_text()
    require('\u2014' not in body, f"Narrative em dash: {doc.relative_to(ROOT)}")
    for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', body):
        if urlsplit(target).scheme or target.startswith('#'):
            continue
        path = unquote(target.split('#',1)[0])
        if not path:
            continue
        links_checked += 1
        require((doc.parent/path).exists(), f"Broken local link: {doc.relative_to(ROOT)} -> {target}")

with (ROOT/'pyproject.toml').open('rb') as f:
    meta=tomllib.load(f)
require(meta['project']['version']=='0.1.0', 'Unexpected project version')
for notebook in (ROOT/'notebooks').glob('*.ipynb'):
    content=json.loads(notebook.read_text())
    require(content['nbformat']==4, f"Unsupported notebook: {notebook.name}")
    for i,cell in enumerate(content['cells']):
        if cell['cell_type']=='code':
            try:
                compile(''.join(cell['source']),f'{notebook.name}:{i}','exec')
            except SyntaxError as error:
                errors.append(str(error))

for path in ['LICENSE','README.md','CITATION.cff','CONTRIBUTING.md','ROADMAP.md','SECURITY.md',
             'docs/validation.md','examples/results/results.json']:
    require((ROOT/path).is_file(), f'Missing deliverable: {path}')

if errors:
    print('\n'.join(errors),file=sys.stderr)
    raise SystemExit(1)
print(f'Checked {len(sources)} sources, {len(projects)} project plans and {links_checked} local links')
