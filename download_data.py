import requests
import os

url = "https://raw.githubusercontent.com/treselle-systems/customer_churn_analysis/master/WA_Fn-UseC_-Telco-Customer-Churn.csv"
output_path = os.path.join("data", "Telco-Customer-Churn.csv")

print(f"Downloading dataset from {url}...")
try:
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(response.content)
    print(f"Dataset saved to {output_path}")
except Exception as e:
    print(f"Error downloading dataset: {e}")
