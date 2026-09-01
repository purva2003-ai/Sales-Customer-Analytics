# Sales & Customer Analytics Dashboard

## 📌 Project Overview

This project analyzes sales, profit, customer, product, and regional performance using the Superstore dataset.

The project combines **Python for data analysis** and **Microsoft Power BI for interactive visualization** to identify business trends, profitable areas, loss-making products and customers, and opportunities for improvement.

---

## 🎯 Business Objective

The main objectives of this project are:

- Analyze overall sales and profitability
- Identify top-performing and loss-making products
- Analyze customer profitability and purchasing behavior
- Compare regional and state-level performance
- Analyze sales and profit by category and sub-category
- Understand the relationship between discount and profit
- Identify business areas that require attention
- Build an interactive Power BI dashboard for decision-making

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Microsoft Power BI
- Power Query
- DAX
- CSV
- Data Visualization
- Exploratory Data Analysis (EDA)

---

## 📂 Project Structure

```text
Sales_Customer_Analytics/
│
├── data/
│   ├── Sample - Superstore.csv
│   └── cleaned_superstore.csv
│
├── python/
│   ├── 01_load_data.py
│   └── 02_eda_analysis.py
│
├── outputs/
│   ├── city_analysis.csv
│   ├── customer_analysis.csv
│   ├── kpi_summary.csv
│   ├── output_city_quadrants.csv
│   ├── output_customer_analysis.csv
│   ├── output_product_analysis.csv
│   ├── product_analysis.csv
│   ├── region_analysis.csv
│   ├── segment_analysis.csv
│   ├── state_analysis.csv
│   └── subcategory_analysis.csv
│
├── Dashboard.pbix
├── requirements.txt
└── README.md