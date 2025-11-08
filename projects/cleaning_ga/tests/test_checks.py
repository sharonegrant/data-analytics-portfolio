from pathlib import Path
import pandas as pd

CLEAN = Path("outputs/data/cleaning_ga/cleaned.csv")

def test_clean_exists():
    assert CLEAN.exists(), f"Missing {CLEAN}"

def test_no_null_names_and_dates():
    df = pd.read_csv(CLEAN)
    assert df["name"].notna().all()
    # dates parse without errors
    pd.to_datetime(df["joined"], errors="raise")
