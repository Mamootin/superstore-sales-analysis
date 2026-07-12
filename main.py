# main.py
import pandas as pd
import joblib

from src.data_prep import load_orders, clean_orders
from src.features import build_features
from src.model import train_baseline, train_random_forest

RAW_PATH = "data/raw/Superstore.xlsx"
PROCESSED_PATH = "data/processed/orders_clean.csv"
MODEL_PATH = "app/profit_model.joblib"


def main():
    print("Loading and cleaning data...")
    df = clean_orders(load_orders(RAW_PATH))
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Saved cleaned data to {PROCESSED_PATH} ({len(df)} rows)")

    print("\nBuilding features...")
    X, y = build_features(df)

    print("\nTraining baseline model (Linear Regression)...")
    train_baseline(X, y)

    print("\nTraining Random Forest model...")
    model = train_random_forest(X, y)

    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    print("\nTop 10 features by importance:")
    print(importances.head(10))

    joblib.dump(model, MODEL_PATH)
    print(f"\nSaved trained model to {MODEL_PATH}")

    print("\nDone. Run `streamlit run app/dashboard.py` to view the dashboard.")


if __name__ == "__main__":
    main()