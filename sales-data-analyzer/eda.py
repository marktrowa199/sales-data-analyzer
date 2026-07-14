import pandas as pd

def run_eda():
    # Load dataset
    df = pd.read_csv("data/Superstoree.csv", encoding="latin1")

    print("=" * 50)
    print("FIRST 5 ROWS")
    print("=" * 50)
    print(df.head())

    print("\n" + "=" * 50)
    print("DATASET SHAPE")
    print("=" * 50)
    print(df.shape)

    print("\n" + "=" * 50)
    print("DATASET INFORMATION")
    print("=" * 50)
    print(df.info())

    print("\n" + "=" * 50)
    print("SUMMARY STATISTICS")
    print("=" * 50)
    print(df.describe())

    print("\n" + "=" * 50)
    print("MISSING VALUES")
    print("=" * 50)
    print(df.isnull().sum())

    print("\n" + "=" * 50)
    print("DUPLICATE ROWS")
    print("=" * 50)
    print(df.duplicated().sum())

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

    print("\n" + "=" * 50)
    print("DATA TYPES AFTER CONVERSION")
    print("=" * 50)
    print(df.dtypes)

    df.to_csv("data/cleaned_superstore.csv", index=False)
    return df