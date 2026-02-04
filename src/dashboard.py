import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set Page Configuration
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    path = os.path.join("data", "cleaned_churn_data.csv")
    return pd.read_csv(path)

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found. Please run src/clean_data.py first.")
    st.stop()

# Title
st.title("📊 Telecom Customer Churn Analysis Dashboard")
st.markdown("Interactive dashboard to analyze customer churn drivers and identify high-risk segments.")

# Sidebar Filters
st.sidebar.header("Filters")
contract_filter = st.sidebar.multiselect(
    "Select Contract Type:",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Select Payment Method:",
    options=df["PaymentMethod"].unique(),
    default=df["PaymentMethod"].unique()
)

st.sidebar.markdown("---")
st.sidebar.info("Created by [Mustafaa](https://github.com/syed-mustafaa) for Customer Churn Analysis Project")
st.sidebar.caption("Data Source: IBM / Kaggle Telco Churn Dataset")

filtered_df = df[
    (df["Contract"].isin(contract_filter)) &
    (df["PaymentMethod"].isin(payment_filter))
]

# --- KPI Section ---
st.subheader("Key Performance Indicators (KPIs)")
col1, col2, col3, col4 = st.columns(4)

total_customers = len(filtered_df)
churn_count = filtered_df['Churn'].sum()
churn_rate = (churn_count / total_customers) * 100 if total_customers > 0 else 0
active_customers = total_customers - churn_count

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Active Customers", f"{active_customers:,}")
col3.metric("Churned Customers", f"{churn_count:,}")
col4.metric("Churn Rate", f"{churn_rate:.2f}%")

st.markdown("---")

# --- Charts Section ---

# Row 1
c1, c2 = st.columns(2)

with c1:
    st.subheader("Churn by Contract Type")
    # Group by Contract and Churn
    contract_churn = filtered_df.groupby(['Contract', 'Churn']).size().reset_index(name='Count')
    fig_contract = px.bar(
        contract_churn, x="Contract", y="Count", color="Churn", 
        barmode='group', title="Churn Distribution by Contract",
        color_discrete_map={0: '#90EE90', 1: '#FFCCCB'} # Green for No, Red for Yes
    )
    st.plotly_chart(fig_contract, use_container_width=True)

with c2:
    st.subheader("Churn by Payment Method")
    payment_churn = filtered_df.groupby(['PaymentMethod', 'Churn']).size().reset_index(name='Count')
    fig_payment = px.bar(
        payment_churn, x="PaymentMethod", y="Count", color="Churn",
        barmode='group', title="Churn Distribution by Payment Method",
        color_discrete_map={0: '#90EE90', 1: '#FFCCCB'}
    )
    st.plotly_chart(fig_payment, use_container_width=True)

# Row 2
c3, c4 = st.columns(2)

with c3:
    st.subheader("Monthly Charges Distribution")
    fig_charges = px.box(
        filtered_df, x="Churn", y="MonthlyCharges", 
        points="all", title="Monthly Charges vs Churn",
        color="Churn", color_discrete_map={0: '#90EE90', 1: '#FFCCCB'}
    )
    st.plotly_chart(fig_charges, use_container_width=True)

with c4:
    st.subheader("Churn by Tenure Group")
    if 'TenureGroup' in filtered_df.columns:
        tenure_churn = filtered_df.groupby(['TenureGroup', 'Churn']).size().reset_index(name='Count')
        # Order tenure groups
        tenure_order = ['New', 'Medium', 'Long']
        fig_tenure = px.bar(
            tenure_churn, x="TenureGroup", y="Count", color="Churn",
            category_orders={"TenureGroup": tenure_order},
            barmode='group', title="Churn by Tenure Group",
            color_discrete_map={0: '#90EE90', 1: '#FFCCCB'}
        )
        st.plotly_chart(fig_tenure, use_container_width=True)
    else:
        st.write("Tenure Group feature missing.")

# --- Data View ---
with st.expander("View Filtered Raw Data"):
    st.dataframe(filtered_df)
    
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name='filtered_churn_data.csv',
        mime='text/csv',
    )

st.markdown("---")
st.markdown("**Insights**: Month-to-month contracts and Electronic Check payments show higher churn rates.")
