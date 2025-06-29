
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from pathlib import Path
import numpy as np

DATA_PATH = Path("../outputs/datasets/collection/HousePricesRecords_clean.csv")


def correlation_analysis_body() -> None:
    """EDA tab – distribution & correlation plots."""
    st.title(" Correlation Analysis")

    
# 1 ·Load data

    if not DATA_PATH.exists():
        st.error("Cleaned dataset not found. Run notebook 01 to generate it.")
        return

    df = pd.read_csv(DATA_PATH)


# 2 ·Sidebar filters

    st.sidebar.header("Filter data ")

    years = sorted(df["Year"].unique())
    counties = sorted(df["County"].unique())

    year_sel = st.sidebar.multiselect("Year", years, default=years)
    county_sel = st.sidebar.multiselect("County", counties, default=counties[:10])

    df_filt = df.query("Year in @year_sel and County in @county_sel")


