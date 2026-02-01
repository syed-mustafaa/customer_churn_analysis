import pandas as pd
import sqlite3
import os

def run_sql_analysis(input_path, output_file):
    print("Loading data for SQL Analysis...")
    df = pd.read_csv(input_path)
    
    # Create in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    df.to_sql('churn_data', conn, index=False, if_exists='replace')
    
    queries = {
        "1. Start by Churn Rate by Contract Type": """
            SELECT 
                Contract,
                COUNT(*) as Total_Customers,
                SUM(Churn) as Churned_Customers,
                ROUND(CAST(SUM(Churn) AS FLOAT) / COUNT(*) * 100, 2) as Churn_Rate_Percent
            FROM churn_data
            GROUP BY Contract
            ORDER BY Churn_Rate_Percent DESC;
        """,
        "2. Churn by Tenure Group (Do short-tenure customers churn more?)": """
            SELECT 
                TenureGroup,
                COUNT(*) as Total_Customers,
                SUM(Churn) as Churned_Customers,
                ROUND(CAST(SUM(Churn) AS FLOAT) / COUNT(*) * 100, 2) as Churn_Rate_Percent
            FROM churn_data
            GROUP BY TenureGroup
            ORDER BY Churn_Rate_Percent DESC;
        """,
        "3. Average Monthly Charges: Churn vs Non-Churn": """
            SELECT 
                Churn,
                ROUND(AVG(MonthlyCharges), 2) as Avg_Monthly_Charges,
                ROUND(AVG(TotalCharges), 2) as Avg_Total_Charges
            FROM churn_data
            GROUP BY Churn;
        """,
        "4. Risk Analysis by Internet Service": """
            SELECT 
                InternetService,
                COUNT(*) as Total,
                SUM(Churn) as Churned,
                ROUND(CAST(SUM(Churn) AS FLOAT) / COUNT(*) * 100, 2) as Churn_Rate
            FROM churn_data
            GROUP BY InternetService
            ORDER BY Churn_Rate DESC;
        """
    }

    print("Running SQL queries...")
    with open(output_file, "w") as f:
        f.write("# SQL Analysis Insights\n\n")
        
        for title, query in queries.items():
            print(f"Running: {title}")
            f.write(f"## {title}\n")
            f.write(f"```sql\n{query}\n```\n")
            
            result = pd.read_sql_query(query, conn)
            markdown_table = result.to_markdown(index=False)
            
            f.write(markdown_table)
            f.write("\n\n")
            
    conn.close()
    print(f"SQL analysis results saved to {output_file}")

if __name__ == "__main__":
    input_csv = os.path.join("data", "cleaned_churn_data.csv")
    output_md = os.path.join("output", "sql_insights.md")
    run_sql_analysis(input_csv, output_md)
