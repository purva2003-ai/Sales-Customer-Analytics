import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned_superstore.csv",
    encoding="latin1"
)

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("========== DATASET OVERVIEW ==========")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==========================================
# OVERALL BUSINESS KPIs
# ==========================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

unique_orders = df["Order ID"].nunique()
unique_customers = df["Customer ID"].nunique()
unique_products = df["Product ID"].nunique()

average_order_value = (
    df.groupby("Order ID")["Sales"].sum().mean()
)

profit_margin = (
    total_profit / total_sales
) * 100

print("\n========== OVERALL KPIs ==========")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Total Quantity: {total_quantity:,}")
print(f"Unique Orders: {unique_orders:,}")
print(f"Unique Customers: {unique_customers:,}")
print(f"Unique Products: {unique_products:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")

# ==========================================
# YEARLY SALES & PROFIT ANALYSIS
# ==========================================

yearly_sales = (
    df.groupby(df["Order Date"].dt.year)["Sales"]
    .sum()
    .sort_index()
)

yearly_profit = (
    df.groupby(df["Order Date"].dt.year)["Profit"]
    .sum()
    .sort_index()
)

yearly_profit_margin = (
    yearly_profit / yearly_sales
) * 100

yearly_sales_growth = (
    yearly_sales.pct_change() * 100
)

print("\n========== YEARLY PERFORMANCE ==========")

print("\nYearly Sales:")
print(yearly_sales)

print("\nYearly Profit:")
print(yearly_profit)

print("\nYearly Profit Margin:")
print(yearly_profit_margin)

print("\nYearly Sales Growth:")
print(yearly_sales_growth)

# ==========================================
# CATEGORY ANALYSIS
# ==========================================

category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

category_analysis["Profit Margin"] = (
    category_analysis["Profit"]
    / category_analysis["Sales"]
) * 100

category_analysis = category_analysis.sort_values(
    "Profit",
    ascending=False
)

print("\n========== CATEGORY ANALYSIS ==========")
print(category_analysis)

# ==========================================
# SUB-CATEGORY ANALYSIS
# ==========================================

subcategory_analysis = df.groupby("Sub-Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

subcategory_analysis["Profit Margin"] = (
    subcategory_analysis["Profit"]
    / subcategory_analysis["Sales"]
) * 100

# Sort by profit
subcategory_analysis = subcategory_analysis.sort_values(
    "Profit",
    ascending=False
)

print("\n========== SUB-CATEGORY ANALYSIS ==========")
print(subcategory_analysis)

print("\nTop 10 Sub-Categories by Profit:")
print(subcategory_analysis.head(10))

print("\nBottom 10 Sub-Categories by Profit:")
print(subcategory_analysis.tail(10))

# ==========================================
# REGION ANALYSIS
# ==========================================

region_analysis = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Customers=("Customer ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

region_analysis["Profit Margin"] = (
    region_analysis["Profit"]
    / region_analysis["Sales"]
) * 100

region_analysis = region_analysis.sort_values(
    "Profit",
    ascending=False
)

print("\n========== REGION ANALYSIS ==========")
print(region_analysis)

print("\nTop Regions by Profit:")
print(region_analysis.head(4))

# ==========================================
# CUSTOMER ANALYSIS
# ==========================================

customer_analysis = df.groupby("Customer Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

customer_analysis["Profit Margin"] = (
    customer_analysis["Profit"]
    / customer_analysis["Sales"]
) * 100

# Top 10 customers by profit
top_customers = customer_analysis.sort_values(
    "Profit",
    ascending=False
).head(10)

# Bottom 10 customers by profit
bottom_customers = customer_analysis.sort_values(
    "Profit",
    ascending=True
).head(10)

# Loss-making customers
loss_making_customers = customer_analysis[
    customer_analysis["Profit"] < 0
].sort_values("Profit")

print("\n========== CUSTOMER ANALYSIS ==========")

print("\nTop 10 Customers by Profit:")
print(top_customers)

print("\nBottom 10 Customers by Profit:")
print(bottom_customers)

print("\nNumber of Loss-Making Customers:",
      len(loss_making_customers))

# ==========================================
# PRODUCT ANALYSIS
# ==========================================

product_analysis = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

product_analysis["Profit Margin"] = (
    product_analysis["Profit"]
    / product_analysis["Sales"]
) * 100

# Top 10 products by Sales
top_products_sales = product_analysis.sort_values(
    "Sales",
    ascending=False
).head(10)

# Bottom 10 products by Sales
bottom_products_sales = product_analysis.sort_values(
    "Sales",
    ascending=True
).head(10)

# Top 10 products by Profit
top_products_profit = product_analysis.sort_values(
    "Profit",
    ascending=False
).head(10)

# Bottom 10 products by Profit
bottom_products_profit = product_analysis.sort_values(
    "Profit",
    ascending=True
).head(10)

# Top 10 products by Quantity
top_products_quantity = product_analysis.sort_values(
    "Quantity",
    ascending=False
).head(10)

# Loss-making products
loss_making_products = product_analysis[
    product_analysis["Profit"] < 0
].sort_values("Profit")

print("\n========== PRODUCT ANALYSIS ==========")

print("\nTop 10 Products by Sales:")
print(top_products_sales)

print("\nBottom 10 Products by Sales:")
print(bottom_products_sales)

print("\nTop 10 Products by Profit:")
print(top_products_profit)

print("\nBottom 10 Products by Profit:")
print(bottom_products_profit)

print("\nTop 10 Products by Quantity:")
print(top_products_quantity)

print("\nNumber of Loss-Making Products:",
      len(loss_making_products))

print("\nTotal Loss from Loss-Making Products:",
      loss_making_products["Profit"].sum())

# ==========================================
# CUSTOMER SEGMENT ANALYSIS
# ==========================================

segment_analysis = df.groupby("Segment").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Customers=("Customer ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

segment_analysis["Profit Margin"] = (
    segment_analysis["Profit"]
    / segment_analysis["Sales"]
) * 100

segment_analysis = segment_analysis.sort_values(
    "Profit",
    ascending=False
)

print("\n========== CUSTOMER SEGMENT ANALYSIS ==========")
print(segment_analysis)


# ==========================================
# SHIP MODE ANALYSIS
# ==========================================

shipmode_analysis = df.groupby("Ship Mode").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

shipmode_analysis["Profit Margin"] = (
    shipmode_analysis["Profit"]
    / shipmode_analysis["Sales"]
) * 100

shipmode_analysis = shipmode_analysis.sort_values(
    "Profit",
    ascending=False
)

print("\n========== SHIP MODE ANALYSIS ==========")
print(shipmode_analysis)

# ==========================================
# STATE ANALYSIS
# ==========================================

state_analysis = df.groupby("State").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Customers=("Customer ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

state_analysis["Profit Margin"] = (
    state_analysis["Profit"]
    / state_analysis["Sales"]
) * 100

print("\n========== STATE ANALYSIS ==========")

print("\nTop 10 States by Sales:")
print(
    state_analysis
    .sort_values("Sales", ascending=False)
    .head(10)
)

print("\nTop 10 States by Profit:")
print(
    state_analysis
    .sort_values("Profit", ascending=False)
    .head(10)
)

print("\nBottom 10 States by Profit:")
print(
    state_analysis
    .sort_values("Profit", ascending=True)
    .head(10)
)


# ==========================================
# CITY ANALYSIS
# ==========================================

city_analysis = df.groupby("City").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique"),
    Customers=("Customer ID", "nunique"),
    Avg_Discount=("Discount", "mean")
)

city_analysis["Profit Margin"] = (
    city_analysis["Profit"]
    / city_analysis["Sales"]
) * 100

print("\n========== CITY ANALYSIS ==========")

print("\nTop 10 Cities by Sales:")
print(
    city_analysis
    .sort_values("Sales", ascending=False)
    .head(10)
)

print("\nTop 10 Cities by Profit:")
print(
    city_analysis
    .sort_values("Profit", ascending=False)
    .head(10)
)

print("\nBottom 10 Cities by Profit:")
print(
    city_analysis
    .sort_values("Profit", ascending=True)
    .head(10)
)

# ==========================================
# DISCOUNT & PROFIT ANALYSIS
# ==========================================

discount_profit_correlation = (
    df["Discount"].corr(df["Profit"])
)

print("\n========== DISCOUNT & PROFIT ANALYSIS ==========")

print(
    f"Discount-Profit Correlation: "
    f"{discount_profit_correlation:.3f}"
)


# Average discount by category
category_discount = (
    df.groupby("Category")["Discount"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Discount by Category:")
print(category_discount)


# Average discount by region
region_discount = (
    df.groupby("Region")["Discount"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Discount by Region:")
print(region_discount)


# Average discount by segment
segment_discount = (
    df.groupby("Segment")["Discount"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Discount by Customer Segment:")
print(segment_discount)


# Top 10 products receiving the highest average discount
top_discount_products = (
    df.groupby("Product Name")["Discount"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Average Discount:")
print(top_discount_products)

# ==========================================
# LOSS-MAKING ANALYSIS
# ==========================================

# Loss-making products
loss_making_products = product_analysis[
    product_analysis["Profit"] < 0
].copy()

total_product_loss = loss_making_products["Profit"].sum()

loss_product_percentage = (
    len(loss_making_products)
    / len(product_analysis)
) * 100

print("\n========== LOSS-MAKING PRODUCTS ==========")

print(
    "Number of Loss-Making Products:",
    len(loss_making_products)
)

print(
    f"Total Loss from Loss-Making Products: "
    f"${total_product_loss:,.2f}"
)

print(
    f"Loss-Making Products (%): "
    f"{loss_product_percentage:.2f}%"
)

print("\nBottom 10 Products by Profit:")
print(
    loss_making_products
    .sort_values("Profit")
    [["Sales", "Profit", "Quantity", "Orders", "Profit Margin"]]
    .head(10)
)


# Loss-making customers
loss_making_customers = customer_analysis[
    customer_analysis["Profit"] < 0
].copy()

customer_loss_percentage = (
    len(loss_making_customers)
    / len(customer_analysis)
) * 100

print("\n========== LOSS-MAKING CUSTOMERS ==========")

print(
    "Number of Loss-Making Customers:",
    len(loss_making_customers)
)

print(
    f"Loss-Making Customers (%): "
    f"{customer_loss_percentage:.2f}%"
)

print("\nBottom 10 Customers by Profit:")
print(
    loss_making_customers
    .sort_values("Profit")
    [["Sales", "Profit", "Quantity", "Orders", "Profit Margin"]]
    .head(10)
)


# Loss-making states
loss_making_states = state_analysis[
    state_analysis["Profit"] < 0
].copy()

print("\n========== LOSS-MAKING STATES ==========")

print(
    "Number of Loss-Making States:",
    len(loss_making_states)
)

print("\nLoss-Making States:")
print(
    loss_making_states
    .sort_values("Profit")
)

# ==========================================
# FINAL KPI SUMMARY
# ==========================================

kpi_summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Profit Margin",
        "Total Quantity",
        "Unique Orders",
        "Unique Customers",
        "Unique Products",
        "Average Order Value",
        "Loss-Making Products",
        "Loss-Making Customers",
        "Loss-Making States"
    ],
    "Value": [
        total_sales,
        total_profit,
        profit_margin,
        total_quantity,
        unique_orders,
        unique_customers,
        unique_products,
        average_order_value,
        len(loss_making_products),
        len(loss_making_customers),
        len(loss_making_states)
    ]
})

print("\n========== FINAL KPI SUMMARY ==========")
print(kpi_summary)


# ==========================================
# SAVE ANALYTICAL OUTPUTS
# ==========================================

city_analysis.to_csv(
    "outputs/city_analysis.csv"
)

customer_analysis.to_csv(
    "outputs/customer_analysis.csv"
)

product_analysis.to_csv(
    "outputs/product_analysis.csv"
)

subcategory_analysis.to_csv(
    "outputs/subcategory_analysis.csv"
)

region_analysis.to_csv(
    "outputs/region_analysis.csv"
)

segment_analysis.to_csv(
    "outputs/segment_analysis.csv"
)

state_analysis.to_csv(
    "outputs/state_analysis.csv"
)

kpi_summary.to_csv(
    "outputs/kpi_summary.csv",
    index=False
)

print("\n========== OUTPUT FILES ==========")
print("All analytical outputs saved successfully.")

