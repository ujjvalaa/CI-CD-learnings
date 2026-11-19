import pandas as pd
from pathlib import Path

# Locate the dataset relative to the project
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "customers.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


if __name__ == "__main__":
    df = load_data()

    print("Dataset shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nColumn types:")
    print(df.dtypes)