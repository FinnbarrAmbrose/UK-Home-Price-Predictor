# House-price-for-uk

A predictive analytics project built to explore and model historical uk housing prices using the hm land registry “uk housing prices paid” dataset. this repo lets users:


## Dataset


## Business Requirements
Our primary goal is to enable prospective buyers to see what similar homes in their county sold for in 2017 so they can make informed offers. We also want to give real-estate analysts an easy way to compare price trends across new builds versus old builds and different regions to spot emerging markets. Finally, we aim to offer data enthusiasts a simple interface to test market hypotheses and derive actionable insights from past transactions.

success will be measured by:
- mean absolute error (MAE) < £5 000
- root mean squared error (RMSE) < £10 000
- coefficient of determination (R²) > 0.70

## Hypotheses
We test two main market hypotheses using α = 0.05:

**H1: new builds fetch higher sale prices than established properties**  
we split prices into new (Y) vs old (N) and run a welch’s t-test.  
t-statistic: –3.96, p-value: 0.0051 → **reject H₀: new builds are significantly more expensive**  


**H2: sale price varies by property type**  
we group prices by type (D, F, S, T) and run a one-way anova.  
F-statistic: 43.93, p-value: < 0.0001 → **reject H₀: property type affects price**  



## Epics & User Stories
We organized the work into five epics:

**1. Data and Information Collecting**  
User Story 1: As a developer, I want to install the tools and packages I need so I can build and run my project.  
- Make a list of required libraries (pandas, numpy, etc.)  
- Record them in `requirements.txt`  
- Set up a virtual environment (venv or conda)  
- Install with `pip install -r requirements.txt`

User Story 2: As a developer, I want to load my data into Jupyter Notebook so I can start exploring it.  
- Download the CSV file  
- Use `pd.read_csv()` to load it  
- Display the first few rows (`df.head()`)  
- Inspect missing values and data types

**2. Data Visualization, Cleaning & Preparation**  
User Story 1: As a developer, I want to remove or fix any missing or incorrect values in the dataset so I can trust my analysis.  
- Check for nulls and either fill or drop them  
- Fix formatting issues (date parsing, string casing)

User Story 2: As a developer, I want to create simple charts so I can spot patterns in the data.  
- Generate histograms, bar charts, or scatter plots  
- Use libraries like Matplotlib or Seaborn

User Story 3: As a developer, I want to check and change data types so my models work correctly.  
- Review with `df.dtypes`  
- Convert columns to appropriate types  
- Rename columns for clarity

**3. Model Training, Optimization & Validation**  
As a developer, I want to train a regression model, tune its hyperparameters, and validate performance so I can be confident in its accuracy.

**4. Dashboard Planning, Design & Development**  
As a user I want a homepage that explains the project’s purpose, as a user I want interactive exploratory plots to analyze regional trends, and as a user I want to input property details and receive an instant price estimate.

**5. Dashboard Deployment & Release**  
User Story 1: As a developer, I want to deploy the dashboard online so that users can access it through a web link.  
User Story 2: As a developer, I want to test the deployed app so I can fix any errors before users see them.  
User Story 3: As a user, I want to access a clean, working version of the app so I can explore it without installing anything.  
User Story 4: As a developer, I want to keep the app updated so I can release improvements and bug fixes easily.


## Technologies
This project is built with python 3.12 and uses:

- **streamlit** for the multipage dashboard interface  
- **pandas** for data manipulation  
- **numpy** for numerical operations  
- **plotly.express** & **plotly.figure_factory** for interactive histograms and heatmaps  
- **matplotlib** & **seaborn** for plots and tables  
- **scikit-learn** (model selection, metrics, preprocessing)  
- **xgboost** for gradient-boosted regression  
- **feature-engine** for feature‐engineering pipelines  
- **imbalanced-learn** for handling class imbalance (if used)  
- **joblib** & **json** for model serialization and metrics storage  
- **scipy** for statistical tests (Welch’s t-test, ANOVA)  
- **pathlib** & **os** for file and path operations  

_dev tools (in `requirements-dev.txt`):_  
- **data-profiling** for exploratory reports  
- **ppscore** for model scoring insights  
- **yellowbrick** for visual diagnostics  