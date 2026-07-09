import pandas as pd

def load_orders(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name="Orders")
    return df

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Ship Time Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    df = df.drop_duplicates()
    return df