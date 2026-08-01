import json, hashlib
from pathlib import Path
R=Path(__file__).parents[1]
def test_contract_five_claims():
    assert len(json.loads((R/'contract/live_claims.json').read_text())) == 5
def test_source_hashes():
    for line in (R/'evidence/source/SHA256SUMS').read_text().splitlines():
        h,n=line.split('  '); assert hashlib.sha256((R/'evidence/source'/n).read_bytes()).hexdigest()==h
