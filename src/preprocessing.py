import pandas as pd
from pathlib import Path

# Locate the dataset relative to the project
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "customers.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

def check_missing_values(df):
    missing_values = df.isnull().sum()
    return missing_values

def fix_total_charges(df):
    # 1. Work on a copy so the original df isn't changed
    df = df.copy()

    # 2. Convert text to numbers; blanks (" ") become NaN
    charges = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # 3. Find rows that are missing AND have tenure 0, and set them to 0
    missing_at_zero_tenure = charges.isna() & df["tenure"].eq(0)
    df["TotalCharges"] = charges.mask(missing_at_zero_tenure, 0)

    # 4. Return the cleaned copy
    return df


if __name__ == "__main__":
    df = fix_total_charges(load_data())

    print("Dataset shape:", df.shape)
    print("TotalCharges type:", df["TotalCharges"].dtype)

    print("\nMissing values:")
    print(check_missing_values(df))