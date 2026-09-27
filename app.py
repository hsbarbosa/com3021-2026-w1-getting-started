from __future__ import annotations

import csv
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)
DATA_FILE = Path(__file__).parent / "data" / "sample.csv"


def load_values() -> list[float]:
    with DATA_FILE.open(newline="", encoding="utf-8") as source:
        return [float(row["value"]) for row in csv.DictReader(source)]


@app.get("/")
def home():
    return """<!doctype html>
<html lang="en">
  <head><meta charset="utf-8"><title>COM3021 Data Service</title></head>
  <body>
    <h1>COM3021 mini data service</h1>
    <p>This Flask app reads a small CSV file and exposes its summary over HTTP.</p>
    <ul>
      <li><a href="/health">/health</a> — service health</li>
      <li><a href="/api/summary">/api/summary</a> — data summary as JSON</li>
    </ul>
  </body>
</html>"""


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/api/summary")
def summary():
    values = load_values()
    return jsonify(
        records=len(values),
        mean=round(sum(values) / len(values), 2),
        min_value=min(values),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
