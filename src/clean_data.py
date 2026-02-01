import pandas as pd
import numpy as np
import os

def clean_and_feature_engineer(input_path, output_path):
    print("Loading data...")
    df = pd.read_csv(input_path)

    # --- Data Cleaning ---
    print("Cleaning data...")
    
    # 1. Remove duplicates
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_count - len(df)} duplicate rows.")

    # 2. Handle missing values
    # TotalCharges represents accumulated amount, should be numeric. 
    # It often has empty strings " " for new customers (tenure=0).
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Fill missing TotalCharges with 0 (assuming tenure=0 implies no charges yet)
    df['TotalCharges'].fillna(0, inplace=True)
    
    # Check for other missing values
    df.dropna(inplace=True) # Drop rows with other missing values if any (though usually clean in this dataset)

    # 3. Encode Churn
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # --- Feature Engineering ---
    print("Feature Engineering...")

    # TenureGroup
    def categorize_tenure(tenure):
        if tenure <= 12:
            return 'New'
        elif tenure <= 36:
            return 'Medium'
        else:
            return 'Long'
    
    df['TenureGroup'] = df['tenure'].apply(categorize_tenure)

    # ChargeGroup (binning MonthlyCharges)
    df['ChargeGroup'] = pd.qcut(df['MonthlyCharges'], q=3, labels=['Low', 'Medium', 'High'])

    # RiskCategory
    # Simple logic: High risk if Month-to-month contract AND High Monthly Charges
    # This is a heuristic for demonstration.
    def categorize_risk(row):
        if row['Contract'] == 'Month-to-month' and row['ChargeGroup'] == 'High':
            return 'High'
        elif row['Contract'] == 'Month-to-month':
            return 'Medium'
        else:
            return 'Low'

    df['RiskCategory'] = df.apply(categorize_risk, axis=1)

    # --- Save ---
    print(f"Saving processed data to {output_path}...")
    df.to_csv(output_path, index=False)
    print("Done.")

if __name__ == "__main__":
    input_csv = os.path.join("data", "Telco-Customer-Churn.csv")
    output_csv = os.path.join("data", "cleaned_churn_data.csv")
    
    clean_and_feature_engineer(input_csv, output_csv)
