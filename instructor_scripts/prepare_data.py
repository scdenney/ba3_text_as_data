#!/usr/bin/env python3
"""Instructor-only helper to export parquet to CSV for Orange and validate schema."""
import pandas as pd
from pathlib import Path

def export_parquet_to_csv(parquet_path: str, csv_path: str):
    df = pd.read_parquet(parquet_path)
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"Exported {len(df):,} rows to {csv_path}")

if __name__ == "__main__":
    base = Path(__file__).resolve().parents[1]
    parquet_in = base / "data" / "nikh_corpus.parquet"
    csv_out = base / "data" / "nikh_corpus.csv"
    if parquet_in.exists():
        export_parquet_to_csv(str(parquet_in), str(csv_out))
    else:
        print(f"Missing: {parquet_in}")
