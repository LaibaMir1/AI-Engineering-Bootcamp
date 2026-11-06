import pandas as pd
from pipeline import clean


def test_clean():
    messy = pd.DataFrame({
        "name": ["Ali", "Omar", "Omar", None],
        "city": ["Karachi", "KARACHI ", "KARACHI ", "Lahore"],
        "age": ["21", "twenty", "twenty", "23"],
        "score": [80.0, None, None, 66.0],
    })

    result = clean(messy)

    # Duplicate Omar and the row with no name are removed
    assert len(result) == 2
    # City is tidy
    assert result.loc[1, "city"] == "Karachi"
    # "twenty" became the number 20
    assert result.loc[1, "age"] == 20
    # No missing values remain
    assert result.isna().sum().sum() == 0