import pandas as pd

CATEGORICAL_COLS = ["Category", "Sub-Category", "Region", "Segment", "Ship Mode"]
NUMERIC_COLS = ["Sales", "Quantity", "Discount"]

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    X = pd.get_dummies(df[CATEGORICAL_COLS + NUMERIC_COLS], columns=CATEGORICAL_COLS)
    y = df["Profit"]
    return X, y