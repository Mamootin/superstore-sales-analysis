import pandas as pd
from src.data_prep import clean_orders

def test_ship_time_is_non_negative():
    df = pd.DataFrame({
        "Order Date": ["2024-01-01"], "Ship Date": ["2024-01-03"],
        "Profit": [10], "Sales": [100]
    })
    cleaned = clean_orders(df)
    assert cleaned["Ship Time Days"].iloc[0] >= 0