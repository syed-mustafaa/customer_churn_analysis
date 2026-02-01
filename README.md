# Customer Churn Analysis Project

## 📌 Usage
### 1. Project Overview
This project analyzes customer churn data for a telecommunications company. It identifies key churn drivers, such as contract types, payment methods, and monthly charges, providing actionable insights to improve retention.

### 2. Tools Used
- **Python**: Data cleaning, Analysis, Dashboarding
- **Calculations**: Pandas, NumPy
- **Visualizations**: Matplotlib, Seaborn, Plotly
- **Database**: SQLite (SQL for analysis)
- **Dashboard**: Streamlit
- **Version Control**: Git

### 3. Project Structure
```
customer_churn_analysis/
├── data/
│   ├── Telco-Customer-Churn.csv       # Raw dataset
│   └── cleaned_churn_data.csv         # Processed dataset
├── output/
│   ├── plots/                         # Generated EDA visualization images
│   └── sql_insights.md                # SQL Analysis results
├── src/
│   ├── clean_data.py                  # Data cleaning & feature engineering
│   ├── eda_analysis.py                # Exploratory Data Analysis script
│   ├── sql_analysis.py                # SQL queries for key questions
│   └── dashboard.py                   # Interactive Streamlit dashboard
├── requirements.txt
└── README.md
```

### 4. How to Run
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Data Cleaning**:
    ```bash
    python src/clean_data.py
    ```

3.  **Run SQL Analysis**:
    ```bash
    python src/sql_analysis.py
    ```
    *Check `output/sql_insights.md` for results.*

4.  **Run Exploratory Data Analysis (EDA)**:
    ```bash
    python src/eda_analysis.py
    ```
    *Check `output/plots/` for images.*

5.  **Launch Dashboard**:
    ```bash
    streamlit run src/dashboard.py
    ```

### 5. Key Insights
- **Contract Type**: Month-to-month contracts have the highest churn rate (~40%+).
- **Payment Method**: Electronic Checks are associated with higher churn likelihood.
- **Tenure**: New customers (0-12 months) are at highest risk.
- **High Risk**: Customers with high monthly charges on month-to-month contracts need immediate retention offers.

### 6. Recommendations
- **Incentivize Long-term Contracts**: Offer discounts for 1-2 year commitments.
- **Target New Customers**: Implementation a 90-day onboarding/success program.
- **Payment Migration**: Encourage auto-pay methods to reduce churn from manual payments.
