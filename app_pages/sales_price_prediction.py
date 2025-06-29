import streamlit as st
import pandas as pd
import joblib
import os

def sales_price_prediction_body():
    st.title(" Sale Price Prediction")
    st.write("Enter property details below and click **Predict Price** to get an estimated sale price.")

# 1 Load data for dropdowns
    data_path = "../outputs/datasets/collection/HousePricesRecords_clean.csv"
    df = pd.read_csv(data_path)
    df["Date of Transfer"] = pd.to_datetime(df["Date of Transfer"])
    max_date = df["Date of Transfer"].max()
    min_date = max_date - pd.DateOffset(years=3)

# 2 Load pipeline
    model_path = "outputs/models/house_price_pipeline.pkl"
    if not os.path.exists(model_path):
        st.error(f"Pipeline not found at {model_path!r}. Run Notebook 05 first.")
        return
    pipeline = joblib.load(model_path)

# 3 PPD mapping
    ppd_map = {
        "A": "Standard sale (market value)",
        "B": "Other sale types (repossessions, buy-to-let, etc.)"
    }
    reverse_ppd = {v: k for k, v in ppd_map.items()}


