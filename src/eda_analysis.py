import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_eda(input_path, output_dir):
    print("Loading data for EDA...")
    df = pd.read_csv(input_path)
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Set style
    sns.set_theme(style="whitegrid")

    # 1. Overall Churn Distribution
    plt.figure(figsize=(6, 6))
    ax = sns.countplot(x='Churn', data=df, palette='pastel')
    plt.title('Overall Churn Distribution (0=No, 1=Yes)')
    plt.savefig(os.path.join(output_dir, 'churn_distribution.png'))
    plt.close()

    # 2. Churn by Contract Type
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Contract', hue='Churn', data=df, palette='Set2')
    plt.title('Churn by Contract Type')
    plt.savefig(os.path.join(output_dir, 'churn_by_contract.png'))
    plt.close()

    # 3. Churn by Payment Method
    plt.figure(figsize=(10, 6))
    sns.countplot(x='PaymentMethod', hue='Churn', data=df, palette='Set1')
    plt.xticks(rotation=45)
    plt.title('Churn by Payment Method')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'churn_by_payment.png'))
    plt.close()

    # 4. Churn by Tenure Group
    plt.figure(figsize=(8, 6))
    sns.countplot(x='TenureGroup', hue='Churn', data=df, order=['New', 'Medium', 'Long'], palette='viridis')
    plt.title('Churn by Tenure Group')
    plt.savefig(os.path.join(output_dir, 'churn_by_tenure_group.png'))
    plt.close()

    # 5. Monthly Charges vs Churn (Boxplot)
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Churn', y='MonthlyCharges', data=df, palette='coolwarm')
    plt.title('Monthly Charges Distribution by Churn Status')
    plt.savefig(os.path.join(output_dir, 'monthly_charges_vs_churn.png'))
    plt.close()

    # 6. Correlation Heatmap (Numerical)
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=['number'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
    plt.close()

    print(f"EDA plots saved to {output_dir}")

if __name__ == "__main__":
    input_csv = os.path.join("data", "cleaned_churn_data.csv")
    output_folder = os.path.join("output", "plots")
    run_eda(input_csv, output_folder)
