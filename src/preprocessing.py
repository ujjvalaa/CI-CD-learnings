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


if __name__ == "__main__":
    df = load_data()

    print("Dataset shape:", df.shape)

    print("\nMissing values:")
    print(check_missing_values(df))