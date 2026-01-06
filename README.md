# UK Home Price Estimator (HM Land Registry Analysis, 1995–2017)

## Executive Summary
This project analyses historical UK residential property transactions to identify structural price drivers and assess the feasibility of estimating sale prices using publicly available data. Using HM Land Registry “Price Paid” records (1995–2017), I conducted exploratory analysis, hypothesis testing, and regression modelling, and presented findings through an interactive Streamlit dashboard.

Key findings show that new-build status and property type are statistically significant drivers of sale price, while regional variation explains substantial market differences. The final model does not achieve production-grade accuracy (holdout performance: MAE £69,667; R² 0.53), highlighting the limitations of price estimation without richer property-level features such as floor area, bedrooms, or property condition. The project demonstrates an end-to-end analytical workflow, transparent evaluation, and disciplined communication of uncertainty alongside results.

---

## What This Repository Contains
This repository hosts a predictive analytics project exploring historical UK housing prices using the HM Land Registry “UK House Price Paid” dataset. It enables users to:

- Explore county-level price trends and regional variation  
- Compare new-build versus established property prices  
- Test market hypotheses using Welch’s t-test and one-way ANOVA  
- Train and evaluate regression models for indicative price estimation  
- Interact with results via a multi-page Streamlit dashboard  

The project is designed for analysts, researchers, and data practitioners interested in understanding housing market dynamics rather than producing live property valuations.

---
## Project structure 
```bash
UK-HOME-PRICE-PREDICTOR
├── .devcontainer
├── app_pages
│   ├── __init__.py
│   ├── correlation_analysis.py
│   ├── ml_price_prediction.py
│   ├── multipage.py
│   ├── page_summary.py
│   ├── project_hypothesis.py
│   └── sales_price_prediction.py
├── inputs
│   └── datasets
│       └── raw
│           └── price_paid_records.csv
├── jupyter_notebooks
│   ├── 01-Data Collection.ipynb
│   ├── 02-Data Cleaning.ipynb
│   ├── 03-Exploratory Data Analysis.ipynb
│   ├── 04-Hypothesis Testing.ipynb
│   └── 05-Model Training and Evaluation.ipynb
├── outputs
│   ├── datasets
│   │   └── collection
│   │       └── HousePricesRecords_clean.csv
│   ├── models
│   │   ├── house_price_pipeline.pkl
│   │   └── metrics.json
├── .gitignore
├── .python-version
├── .slugignore
├── app.py
├── Procfile
├── README.md
├── requirements-dev.txt
├── requirements.txt
└── setup.sh
 ```
## Dataset

The analysis uses the HM Land Registry **“UK Housing Prices Paid”** dataset (via Kaggle), comprising **22,489,348** residential property transactions from **1995-01-01** to **2017-06-29**.

**Key variables include:**
- Sale price  
- Transaction date  
- Property type (detached, semi-detached, terraced, flat, other)  
- New-build indicator  
- Tenure  
- Town, district, and county  

The dataset is released under the **Open Government Licence v3.0** (© Crown 2017).

---

## Business Requirements

The primary objective is to enable exploratory analysis of historical UK housing transactions, allowing users to understand how prices varied across regions, property types, and build status in 2017. Secondary objectives include testing commonly cited market claims (e.g. new-build premiums) and demonstrating a structured analytical workflow on a large administrative dataset.

The following performance benchmarks were defined as **aspirational targets**:

- Mean Absolute Error (MAE) < £5,000  
- Root Mean Squared Error (RMSE) < £10,000  
- Coefficient of determination (R²) > 0.70  

These targets were not met, informing subsequent evaluation and interpretation.

---

## Hypotheses

Two market hypotheses were tested using **α = 0.05**:

**H1: New-build properties sell for higher prices than established properties**  
Welch’s t-test indicates a statistically significant difference in sale prices (p < 0.01), supporting the hypothesis.

**H2: Sale price varies by property type**  
One-way ANOVA confirms statistically significant variation across property types (p < 0.001).

---

## Machine Learning Business Case

The project frames price estimation as a supervised regression problem, assessing whether publicly available transaction data can support meaningful price estimation.

- **Success (aspirational):** MAE < £5,000 and R² ≥ 0.70  
- **Observed outcome:** MAE £69,667, RMSE £118,120, R² 0.53  

Results demonstrate moderate explanatory power but insufficient accuracy for production-grade estimation without additional features.

---

## Dashboard Design

The Streamlit dashboard consists of five pages aligned with the analytical workflow:

1. **Project Overview** – dataset context and headline metrics  
2. **Correlation Analysis** – interactive exploration of feature relationships  
3. **Sale Price Estimation** – indicative price estimates with performance disclaimers  
4. **Hypothesis Validation** – statistical test results and interpretations  
5. **Machine Learning Model** – model structure, evaluation metrics, and limitations  

The dashboard is intended as an exploratory and explanatory tool.

---

## Modelling & Evaluation

After data cleaning and feature engineering, the dataset was split into an **80/20 train–test set**. A linear regression baseline was established before tuning a `RandomForestRegressor` via grid search over tree depth and estimator count.

**Final test-set performance:**
- MAE: £69,667  
- RMSE: £118,120  
- R²: 0.53  

The trained pipeline is saved as `house_price_pipeline.pkl` alongside evaluation metrics.

---

## Results & Insights

Key findings from the analysis include:

- New-build properties command a statistically significant price premium.  
- Property type materially influences sale price.  
- Regional variation explains a substantial proportion of market differences.  
- Model performance highlights the limitations of estimation using transaction data alone.  
- Reliance on 2017-only modelling limits applicability to current market conditions.

These insights address the original analytical objectives while clearly identifying constraints.

---

## Policy and Media Relevance

Although not designed as a live valuation tool, this project demonstrates how large administrative datasets can be used to test widely cited housing market claims, explore regional disparities, and evaluate data-driven narratives. The findings illustrate how data coverage, feature availability, and methodological choices materially affect conclusions—an important consideration in policy analysis and media reporting.

---

## Deployment & Usage

**Live dashboard:**  
https://uk-home-price-predictor-475658c4a389.herokuapp.com/

**Primary deliverable:** Interactive Streamlit dashboard  
**Secondary deliverables:** Saved model pipeline and evaluation metrics

### Running Locally

```bash
git clone https://github.com/FinnbarrAmbrose/UK-Home-Price-Predictor.git
cd UK-Home-Price-Predictor
pip install -r requirements.txt
streamlit run app.py

```
For notebook development:
```bash
pip install -r requirements.txt -r requirements-dev.txt
jupyter notebook
```

## Future Code Quality Fixes (Linting Issues)

CI Python Linter (https://pep8ci.herokuapp.com/)

#### Notebook: `01 - Data Collection.ipynb`
- **Line Length (E501):** Many lines exceed the recommended limit (up to 246 characters).
- **Whitespace and Formatting (E211, E225, E228, E231):** Frequent spacing inconsistencies around operators, parentheses, commas, and modulo operators.
- **Indentation Issues (E111, E113):** Multiple incorrect or unexpected indentation instances.
- **Module Import Placement (E402):** Several imports not placed at the top of the notebook.
- **Trailing Whitespace/Newline (W291, W292)**

#### Notebook: `05 - Model Training and Evaluation.ipynb`
- **Import Placement (E402):** Multiple imports not placed at the top.
- **Line Length (E501):** Lines significantly exceeding recommended length (up to 274 characters).
- **Whitespace and Spacing (E211, E221, E231, E272):** Frequent spacing inconsistencies.
- **Indentation (E112):** Incorrect indentation blocks identified.
- **Trailing Whitespace/Newline Issues (W291, W292)**

#### Streamlit App: `sales_price_prediction.py`
- **Blank Lines (E302, E303):** Incorrect blank line spacing.
- **Line Length (E501):** Several lines exceed the 79-character standard.
- **Whitespace Errors (E221, E272, W293):** Multiple spacing inconsistencies around operators.
- **Missing Newline at EOF (W292)**

#### Streamlit App: `ml_price_prediction.py`
- **Blank Lines (E302):** Improper spacing of blank lines.
- **Line Length (E501):** Several lines exceeding recommended lengths.
- **Whitespace Issues (E221, W291):** Extra spaces before operators and trailing whitespace.
- **Missing Newline at EOF (W292)**

Resolving these issues will significantly enhance code clarity and maintainability.

## Known Issues
we’ve identified several issues that are actively tracked in the repo’s Issues tab:

- prediction errors at extreme price ranges (top 1% of values)  
- occasional Streamlit widget misalignment on mobile devices  
- non-numeric columns slipping through the pipeline (e.g., town/city, county flags)  
- dataset size (~22 million rows) can overwhelm local machines; currently we load only the 1,000 most recent 2017 records as a workaround  

## Credits / Acknowledgements
- **Data source:** HM Land Registry “UK Housing Prices Paid” via Kaggle  
- **Inspiration & Example Repos:**  
  - Amareteklay’s [`heritage-housing-issues`](https://github.com/Amareteklay/heritage-housing-issues)  
  - smtilson’s [`pp5-ml-dashboard`](https://github.com/smtilson/pp5-ml-dashboard)  
- **Libraries & Tools:**  
  scikit-learn, Streamlit, XGBoost, feature-engine, pandas, NumPy, Matplotlib, Plotly, SciPy, Yellowbrick, joblib, and others  
- **Collaborators & Mentors:**  
  - my project mentor [`Mo Shami`](https://www.linkedin.com/in/moshami/)
  - classmates on Slack  

### YouTube Tutorials & Learning Resources
Here are some videos I found particularly helpful—replace with the ones you watched:

- **Pandas Data Cleaning**  
  *“Data Cleaning in Pandas | Python Pandas Tutorials”*  
  `https://www.youtube.com/watch?v=bDhvCp3_lYw`

- **Plotly EDA & Mapping**  
  *“Introduction to Interactive Visualization: Plotly Express”*  
  `https://www.youtube.com/watch?v=61YZaYnoWRQ`

- **Statistical Testing with SciPy**  
  *“How to Interpret the Output of Simple Linear Regression in Python”*  
  `https://www.youtube.com/watch?v=NNrJDMhpWPA`

- **Streamlit Dashboard Development**  
  *“
Build and Deploy a Multi-Page Web Application Using Python (Streamlit)”*  
  `https://www.youtube.com/watch?v=9n4Ch2Dgex0`

- **Deploying Streamlit Apps**  
  *“Deploy Streamlit App on Heroku | Streamlit Tutorials”*  
  `https://www.youtube.com/watch?v=W4CBnt0nLls`

## Future Work & Roadmap
we’ve identified several enhancements to make the tool even more useful:

- **Expand feature set** with property style (modern, contemporary, cottage), number of bedrooms/bathrooms, kitchen size, and other interior attributes  
- **Incorporate school catchment areas** and proximity to top-rated schools  
- **Add transport metrics** such as distance to nearest bus stops, train stations, and major roads  
- **Integrate geospatial data** for mapping price heatmaps and neighborhood boundaries  
- **Include telecom service ratings** (mobile signal strength, broadband availability)  
- **Offer real-time scoring** via an API so users can get up-to-date predictions on live data  
- **User personalization**: allow filtering by lifestyle preferences (e.g., family-friendly, modern urban, rural retreat)  
- **Cloud-scale processing**: move from local subset to full dataset in a scalable environment (e.g., AWS/GCP)   
- **Code formatting improvements**: resolve PEP8 issues outlined in the [Future Code Quality Fixes](#future-code-quality-fixes-linting-issues) section to enhance maintainability and meet coding standards.

## License & Contact
this project is licensed under the MIT License.  

feel free to reach out with questions or feedback:  
- **GitHub:** [FinnbarrAmbrose](https://github.com/FinnbarrAmbrose)  
- **LinkedIn:** [Finnbarr Ambrose](https://www.linkedin.com/in/finnbarr-ambrose-5682221b4/)  
