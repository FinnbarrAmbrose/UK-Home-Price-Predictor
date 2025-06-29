import streamlit as st
import pandas as pd
import json
from pathlib import Path

# Load dynamic metrics
METRICS_FILE = Path("../outputs/models/metrics.json")
if METRICS_FILE.exists():
    with open(METRICS_FILE, "r") as f:
        m = json.load(f)
    MODEL_MAE   = m.get("mae", None)
    MODEL_RMSE  = m.get("rmse", None)
    MODEL_R2    = m.get("r2",   None)
else:
    MODEL_MAE   = MODEL_RMSE = MODEL_R2 = None

def page_summary_body() -> None:
    """Landing page – project overview & quick dataset glimpse."""
    st.title("🏠 UK House-Price Estimator – Overview")

    st.markdown(
        """
        This dashboard lets UK house-hunters and data enthusiasts  
        explore historic **Price-Paid** transactions, test a few
        market hypotheses, and obtain an instant sale-price prediction.
        """
    )

   