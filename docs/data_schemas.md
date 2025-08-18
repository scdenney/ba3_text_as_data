# Data Schemas

## `nk_flattened_corpus.csv` (North Korean journal articles)
Required columns (minimum):
- `doc_id` (string/int): unique identifier
- `title` (string)
- `date` (YYYY-MM-DD or YYYY)
- `section` (e.g., editorial, research article) – if available
- `text` (string): the full text
- `source` = "Kyungje Yongu" (constant)
- `notes` (optional)

## `nikh_corpus.csv` (History textbooks; exported from parquet)
Required columns (minimum):
- `doc_id` (string/int): unique identifier
- `book_id` (string)
- `title` (string) – if available
- `period` (categorical: e.g., Chosun, Colonial, USMG, 1st–7th curriculum, Democratic)
- `level` (e.g., elementary/middle/high)
- `year` (int)
- `text` (string)
- `source` = "NIKH" (constant)

## Encoding
- UTF-8 with BOM is safest for cross-platform CSV.
- Use Unix newlines `\n`.

## Preprocessing choices (instructor)
- Light cleanup only (no stemming) to keep interpretation intuitive.
- Provide `stopwords_ko.txt` and `stopwords_en.txt` in `data/`.
