"""
Enriches data/processed/output_all18.json with metadata from data/raw/teses.tsv.
The 'id' field in the JSON corresponds to the 0-based row index in the TSV (after the header).
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
TSV_PATH = ROOT / "data" / "raw" / "teses.tsv"
JSON_PATH = ROOT / "data" / "processed" / "output_all18.json"

# Load TSV into a dict keyed by row index
teses: dict[int, dict] = {}
with TSV_PATH.open(encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for i, row in enumerate(reader):
        teses[i] = {k: v for k, v in row.items()}

# Load JSON and merge
with JSON_PATH.open(encoding="utf-8") as f:
    records = json.load(f)

missing = 0
for record in records:
    row = teses.get(record["id"])
    if row is None:
        missing += 1
        continue
    record.update(row)

if missing:
    print(f"Warning: {missing} record(s) had no matching row in the TSV.")

with JSON_PATH.open("w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=4)

print(f"Done. Enriched {len(records) - missing} of {len(records)} records.")
