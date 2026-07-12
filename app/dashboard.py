import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")

df = pd.read_csv("data/processed/orders_clean.csv", parse_dates=["Order Date", "Ship Date"])
model = joblib.load("app/profit_model.joblib")

st.title("Superstore Sales Dashboard")

region = st.sidebar.multiselect("Region", df["Region"].unique(), default=list(df["Region"].unique()))
filtered = df[df["Region"].isin(region)]

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered['Profit'].sum():,.0f}")
col3.metric("Orders", f"{filtered['Order ID'].nunique():,}")

st.bar_chart(filtered.groupby("Category")["Sales"].sum())