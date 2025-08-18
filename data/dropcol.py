# dropcol.py
import pandas as pd

# === 1. Clean nk_flattened_corpus.csv ===
p_csv = "data/nk_flattened_corpus.csv"
out_csv = "data/nk_flattened_corpus_clean.csv"

df_csv = pd.read_csv(p_csv)

# Drop unwanted column (adjust name if needed)
if "file_path" in df_csv.columns:
    df_csv = df_csv.drop(columns=["file_path"])

df_csv.to_csv(out_csv, index=False)
print(f"Wrote cleaned CSV: {out_csv}")


# === 2. Convert Parquet to CSV ===
p_parquet = "data/nikh_corpus.parquet"
out_parquet_csv = "data/nikh_corpus.csv"

df_parquet = pd.read_parquet(p_parquet)
df_parquet.to_csv(out_parquet_csv, index=False)
print(f"Converted Parquet -> CSV: {out_parquet_csv}")
