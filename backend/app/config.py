from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_DIR = PROJECT_ROOT / "dataset"
RAW_DIR = DATASET_DIR / "raw"
SAMPLE_DIR = DATASET_DIR / "sample"
PROCESSED_DIR = DATASET_DIR / "processed"
FEATURES_DIR = DATASET_DIR / "features"