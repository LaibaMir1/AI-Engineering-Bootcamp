import pandas as pd


def load(path):
    """Read a CSV file into a DataFrame."""
    return pd.read_csv(path)


def clean(df):
    """Fix messy values and remove bad rows."""
    df = df.copy()

    # 1. Remove exact duplicate rows
    df = df.drop_duplicates()

    # 2. Remove rows with no name
    df = df.dropna(subset=["name"])

    # 3. City: remove extra spaces and use the same capitalisation
    df["city"] = df["city"].str.strip().str.title()

    # 4. Age: change the word "twenty" to a number, then make the column numeric
    df["age"] = df["age"].replace("twenty", 20)
    df["age"] = pd.to_numeric(df["age"]).astype(int)

    # 5. Score: fill the missing score with the median score
    df["score"] = df["score"].fillna(df["score"].median())

    return df.reset_index(drop=True)


def add_features(df):
    """Add new columns calculated from existing ones."""
    df = df.copy()
    df["passed"] = df["score"] >= 50
    return df


if __name__ == "__main__":
    df = load("students_messy.csv")
    print("Before cleaning:", df.shape)
    print(df, "\n")

    df = clean(df)
    df = add_features(df)

    df.to_csv("students_clean.csv", index=False)
    print("After cleaning:", df.shape)
    print(df)