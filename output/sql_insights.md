# SQL Analysis Insights

## 1. Start by Churn Rate by Contract Type
```sql

            SELECT 
                Contract,
                COUNT(*) as Total_Customers,
                SUM(Churn) as Churned_Customers,
                ROUND(CAST(SUM(Churn) AS FLOAT) / COUNT(*) * 100, 2) as Churn_Rate_Percent
            FROM churn_data
            GROUP BY Contract
            ORDER BY Churn_Rate_Percent DESC;
        
```
| Contract       |   Total_Customers |   Churned_Customers |   Churn_Rate_Percent |
|:---------------|------------------:|--------------------:|---------------------:|
| Month-to-month |              3875 |                1655 |                42.71 |
| One year       |              1473 |                 166 |                11.27 |
| Two year       |              1695 |                  48 |                 2.83 |

## 2. Churn by Tenure Group (Do short-tenure customers churn more?)
```sql

            SELECT 
                TenureGroup,
                COUNT(*) as Total_Customers,
                SUM(Churn) as Churned_Customers,
                ROUND(CAST(SUM(Churn) AS FLOAT) / COUNT(*) * 100, 2) as Churn_Rate_Percent
            FROM churn_data
            GROUP BY TenureGroup
            ORDER BY Churn_Rate_Percent DESC;
        
```
| TenureGroup   |   Total_Customers |   Churned_Customers |   Churn_Rate_Percent |
|:--------------|------------------:|--------------------:|---------------------:|
| New           |              2186 |                1037 |                47.44 |
| Medium        |              1856 |                 474 |                25.54 |
| Long          |              3001 |                 358 |                11.93 |

## 3. Average Monthly Charges: Churn vs Non-Churn
```sql

            SELECT 
                Churn,
                ROUND(AVG(MonthlyCharges), 2) as Avg_Monthly_Charges,
                ROUND(AVG(TotalCharges), 2) as Avg_Total_Charges
            FROM churn_data
            GROUP BY Churn;
        
```
|   Churn |   Avg_Monthly_Charges |   Avg_Total_Charges |
|--------:|----------------------:|--------------------:|
|       0 |                 61.27 |             2549.91 |
|       1 |                 74.44 |             1531.8  |

## 4. Risk Analysis by Internet Service
```sql

            SELECT 
                InternetService,
                COUNT(*) as Total,
                SUM(Churn) as Churned,
                ROUND(CAST(SUM(Churn) AS FLOAT) / COUNT(*) * 100, 2) as Churn_Rate
            FROM churn_data
            GROUP BY InternetService
            ORDER BY Churn_Rate DESC;
        
```
| InternetService   |   Total |   Churned |   Churn_Rate |
|:------------------|--------:|----------:|-------------:|
| Fiber optic       |    3096 |      1297 |        41.89 |
| DSL               |    2421 |       459 |        18.96 |
| No                |    1526 |       113 |         7.4  |

