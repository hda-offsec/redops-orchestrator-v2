from pathlib import Path
import json
import csv

def save_json(data, path: Path):
    path.write_text(json.dumps(data, indent=2))


def save_csv(rows, path: Path):
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
