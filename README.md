# Text as Data (Korean Studies) – Orange + GitHub

This repository powers a six-week **Text-as-Data** segment using **Orange Data Mining** with two corpora:
1) **`nk_flattened_corpus.csv`** (North Korean economic journal articles – *Kyungje Yongu*).
2) **`nikh_corpus.csv`** (exported from `nikh_corpus.parquet`, South Korean history textbooks).

**Students do not need to code.** All work happens via **Orange workflows (`.ows`)** and **GitHub** for transparency.

## How to use
- Read `docs/onboarding_github.md` to set up GitHub and your local copy.
- Install Orange (see `docs/orange_setup.md`).
- Open the **Week 1** workflow in `orange_workflows/01_intro_explore.ows.plan.md` (a plan with screenshots and steps).
  - The actual `.ows` files will be added by the instructor in this folder.
- Complete weekly assignments in `assignments/` and push your work via Pull Request (PR).

## Datasets
- `data/nk_flattened_corpus.csv` – provided by instructor (schema in `docs/data_schemas.md`).
- `data/nikh_corpus.csv` – exported by instructor from the source parquet (script in `instructor_scripts/prepare_data.py`).

## License
- Course materials: CC-BY 4.0 (see `LICENSE`).
- Data: see `docs/data_license.md` for dataset-specific notes.
