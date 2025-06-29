import streamlit as st
import pandas as pd
from pathlib import Path
from scipy import stats


DATA_PATH = Path("outputs/datasets/collection/HousePricesRecords_clean.csv")

def project_hypothesis_body():
    """Hypothesis Validation – t-test & ANOVA on the cleaned dataset."""
    st.title("🔬 Hypothesis Validation")
    st.markdown(
        "Use statistical tests to confirm or reject our market hypotheses."
    )

    
    if not DATA_PATH.exists():
        st.error("Dataset not found. Run 01_Data_Collection to generate it.")
        return

    df = pd.read_csv(DATA_PATH)

    
    st.subheader("H1: Are new houses more expensive than old ones?")
    
    new_prices = df[df["Old/New"] == 1]["Price"]
    old_prices = df[df["Old/New"] == 0]["Price"]

    
    t_stat, p_val = stats.ttest_ind(new_prices, old_prices, equal_var=False)
    st.write(f"- T-statistic: **{t_stat:.2f}**")
    st.write(f"- p-value: **{p_val:.4f}**")

    if p_val < 0.05:
        st.success("✅ Reject H₀ — new houses are significantly more expensive.")
    else:
        st.info("ℹ️ Fail to reject H₀ — no significant price difference found.")

    
