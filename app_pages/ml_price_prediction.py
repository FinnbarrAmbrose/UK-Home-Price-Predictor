import streamlit as st
import pandas as pd
import joblib
import json
import os
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

def ml_price_prediction_body():
    st.title("Machine Learning Model")
    st.write("Train/test metrics, residuals & feature importances for the regression model.")

# 1 -Load trained pipeline
    pipeline_path = Path("../outputs/models/house_price_pipeline.pkl")
    if not pipeline_path.exists():
        st.error(f"Pipeline not found at {pipeline_path!r}. Run Notebook 05 first.")
        return
    pipeline = joblib.load(pipeline_path)

# 2 Load or compute test‐set metrics
    metrics_path = Path("../outputs/models/metrics.json")
    if metrics_path.exists():
        with open(metrics_path, "r") as f:
            m = json.load(f)
        test_mae  = m.get("mae", None)
        test_rmse = m.get("rmse", None)
        test_r2   = m.get("r2",   None)
    else:
        test_mae = test_rmse = test_r2 = None

