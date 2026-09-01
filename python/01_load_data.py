import numpy as np
import pandas as pd

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df.head())
print(df.shape)
print(df.columns)

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)

print(df.describe())
df.to_csv("data/cleaned_superstore.csv",index=False)

total_sales = df["Sales"].sum()
print("Total Sales:",total_sales)

total_profit = df["Profit"].sum()
print("Total Profit:",total_profit)

profit_margin = (total_profit / total_sales)*100
print("Profit Margin:",profit_margin)

category_profit = df.groupby("Category")["Profit"].sum()
print(category_profit)

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum()
print(subcategory_profit)

region_profit = df.groupby("Region")["Profit"].sum()
print(region_profit)

customer_profit = df.groupby("Customer Name")["Profit"].sum()
customer_profit = customer_profit.sort_values(ascending=False)
print(customer_profit.head(10))
print(customer_profit.tail(10))

product_profit = df.groupby("Product Name")["Profit"].sum()
product_profit = product_profit.sort_values(ascending=False)
print(product_profit)
print(product_profit.tail(10))

product_sales = df. groupby("Product Name")["Sales"].sum()
product_sales = product_sales.sort_values(ascending=False)
print(product_sales)
print(product_sales.head(10))
print(product_sales.tail(10))

category_profit = df.groupby("Category")["Profit"].sum()
category_profit = category_profit.sort_values(ascending=False)
print(category_profit)
print(category_profit.head(10))

sales_category = df.groupby("Category")["Sales"].sum()
sales_category = sales_category.sort_values(ascending=False)
print(sales_category)


category_quantity = df.groupby("Category")["Quantity"].sum()
category_quantity = category_quantity.sort_values(ascending=False)
print(category_quantity)

region_sales = df.groupby("Region")["Sales"].sum()
region_sales = region_sales.sort_values(ascending=False)
print(region_sales)

region_profit = df.groupby("Region")["Profit"].sum()
region_profit = region_profit.sort_values(ascending=False)
print(region_profit)

region_quantity = df.groupby("Region")["Quantity"].sum()
region_quantity = region_quantity.sort_values(ascending=False)
print(region_quantity)

segment_sales = df.groupby("Segment")["Sales"].sum()
segment_sales = segment_sales.sort_values(ascending=False)
print(segment_sales)

segment_profit = df.groupby("Segment")["Profit"].sum()
segment_profit = segment_profit.sort_values(ascending=False)
print(segment_profit)

segment_quantity = df.groupby("Segment")["Quantity"].sum()
segment_quantity = segment_quantity.sort_values(ascending=False)
print(segment_quantity)

shipmode_sales = df.groupby("Ship Mode")["Sales"].sum()
shipmode_sales = shipmode_sales.sort_values(ascending=False)
print(shipmode_sales)

shipmode_profit =  df.groupby("Ship Mode")["Profit"].sum()
shipmode_profit = shipmode_profit.sort_values(ascending=False)
print(shipmode_profit)

shipmode_quantity = df.groupby("Ship Mode")["Quantity"].sum()
shipmode_quantity = shipmode_quantity.sort_values(ascending=False)
print(shipmode_quantity)

state_sales = df.groupby("State")["Sales"].sum()
state_sales = state_sales.sort_values(ascending=False)
print(state_sales.head(10))

state_profit = df.groupby("State")["Profit"].sum()
state_profit = state_profit.sort_values(ascending=False)
print(state_profit.head(10))
print(state_profit.tail(10))

city_sales = df.groupby("City")["Sales"].sum()
city_sales = city_sales.sort_values(ascending=False)
print(city_sales)
print(city_sales.head(10))

city_profit = df.groupby("City")["Profit"].sum()
city_profit = city_profit.sort_values(ascending=False)
print(city_profit)
print(city_profit.head(10))
print(city_profit.tail(10))

category_margin = ((category_profit) / (sales_category))*100
print(category_margin.sort_values(ascending=False))

region_margin = (region_profit / region_sales)*100
print(region_margin.sort_values(ascending=False))

segment_margin = (segment_profit / segment_sales)*100
print(segment_margin.sort_values(ascending=False))

shipmode_margin = (shipmode_profit / shipmode_sales)*100
print(shipmode_margin.sort_values(ascending=False))

category_discount = df.groupby("Category")["Discount"].mean()
category_discount = category_discount.sort_values(ascending=False)
print(category_discount)

region_discount = df.groupby("Region")["Discount"].mean()
region_discount = region_discount.sort_values(ascending=False)
print(region_discount)

segment_discount = df.groupby("Segment")["Discount"].mean()
segment_discount = segment_discount.sort_values(ascending=False)
print(segment_discount)

category_avg_sales = df.groupby("Category")["Sales"].mean()
category_avg_sales = category_avg_sales.sort_values(ascending=False)
print(category_avg_sales)

category_avg_profit = df.groupby("Category")["Profit"].mean()
category_avg_profit = category_avg_profit.sort_values(ascending=False)
print(category_avg_profit)

region_avg_profit = df.groupby("Region")["Profit"].mean()
region_avg_profit = region_avg_profit.sort_values(ascending=False)
print(region_avg_profit)

segment_avg_profit = df.groupby("Segment")["Profit"].mean()
segment_avg_profit = segment_avg_profit.sort_values(ascending=False)
print(segment_avg_profit)

category_avg_quantity = df.groupby("Category")["Quantity"].mean()
category_avg_quantity = category_avg_quantity.sort_values(ascending=False)
print(category_avg_quantity)

segment_avg_quantity = df.groupby("Segment")["Quantity"].mean()
segment_avg_quantity = segment_avg_quantity.sort_values(ascending=False)
print(segment_avg_quantity)

segment_avg_sales = df.groupby("Segment")["Sales"].mean()
segment_avg_sales = segment_avg_sales.sort_values(ascending=False)
print(segment_avg_sales)

shipmode_avg_sales = df.groupby("Ship Mode")["Sales"].mean()
shipmode_avg_sales = shipmode_avg_sales.sort_values(ascending=False)
print(shipmode_avg_sales)

shipmode_avg_profit = df.groupby("Ship Mode")["Profit"].mean()
shipmode_avg_profit = shipmode_avg_profit.sort_values(ascending=False)
print(shipmode_avg_profit)

shipmode_avg_quantity = df.groupby("Ship Mode")["Quantity"].mean()
shipmode_avg_quantity = shipmode_avg_quantity.sort_values(ascending=False)
print(shipmode_avg_quantity)

region_avg_sales = df.groupby("Region")["Sales"].mean()
region_avg_sales = region_avg_sales.sort_values(ascending=False)
print(region_avg_sales)

state_avg_profit = df.groupby("State")["Profit"].mean()
state_avg_profit = state_avg_profit.sort_values(ascending=False)
print(state_avg_profit.head(10))

state_avg_sales = df.groupby("State")["Sales"].mean()
state_avg_sales = state_avg_sales.sort_values(ascending=False)
print(state_avg_sales.head(10))

state_avg_quantity = df.groupby("State")["Quantity"].mean()
state_avg_quantity = state_avg_quantity.sort_values(ascending=False)
print(state_avg_quantity.head(10))

state_avg_discount = df.groupby("State")["Discount"].mean()
state_avg_discount = state_avg_discount.sort_values(ascending=False)
print(state_avg_discount.head(10))

customer_avg_sales = df.groupby("Customer Name")["Sales"].mean()
customer_avg_sales = customer_avg_sales.sort_values(ascending=False)
print(customer_avg_sales.head(10))

customer_avg_profit = df.groupby("Customer Name")["Profit"].mean()
customer_avg_profit = customer_avg_profit.sort_values(ascending=False)
print(customer_avg_profit.head(10))

customer_avg_quantity = df.groupby("Customer Name")["Quantity"].mean()
customer_avg_quantity = customer_avg_quantity.sort_values(ascending=False)
print(customer_avg_quantity.head(10))

product_avg_profit = df.groupby("Product Name")["Profit"].mean()
product_avg_profit = product_avg_profit.sort_values(ascending=False)
print(product_avg_profit.head(10))

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
df.info()

print("Unique Orders:", df["Order ID"].nunique())
print("Unique Customers:", df["Customer ID"].nunique())
print("Unique Products:", df["Product ID"].nunique())

print("Earliest Ship Date:", df["Order Date"].min())
print("Latest Order Date:", df["Order Date"].max())

print("Earliest Ship Date:", df["Ship Date"].min())
print("Latest Ship Date:", df["Ship Date"].max())

print("Minimum Sales:", df['Sales'].min())
print("Maximum Sales:", df['Sales'].max())

print("Minimum Quantity:", df['Quantity'].min())
print("Maximum Quantity:", df['Quantity'].max())

negative_sales = df[df['Sales']<0]
print("Negative Sales Rows:", len(negative_sales))

duplicate_rows = df.duplicated().sum()
print("Duplicate Rows:", duplicate_rows)

unique_orders = df['Order ID'].nunique()

print("Total Rows:", len(df))
print("Unique Orders:", unique_orders)

customer_order_counts = df.groupby('Customer ID')['Order ID'].nunique()

print("Customer with Multiple Orders:",
      (customer_order_counts > 1).sum())

print("Maximum Orders by One Customer:",
      customer_order_counts.max())

Categorical_columns = [
                       'Ship Mode',
                       'Segment',
                       'Country',
                       'Region',
                       'Category',
                       'Sub-Category'
                      ]

for col in Categorical_columns:
    print(f"\n{col}:")
    print(df[col].nunique())
    print(df[col].unique())

print("Unique States:", df['State'].nunique())
print("Unique Cities:", df['City'].nunique())

print("\n States:")
print(df['State'].unique())

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(category_sales)

category_sales_pct = (
    df.groupby('Category')['Sales'].sum()
    / df['Sales'].sum()
    *100
).sort_values(ascending=False)

print(category_sales_pct)

region_sales = df.groupby("Region")["Sales"].sum()
region_sales = region_sales.sort_values(ascending=False)
print(region_sales)

region_sales_pct = (
    df.groupby('Region')['Sales'].sum()
    / df['Sales'].sum()
    *100
    ).sort_values(ascending=False)
print(region_sales_pct)

segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
print(segment_sales)

segment_sales_pct = (
    df.groupby("Segment")["Sales"].sum()
    /df["Sales"].sum()
    *100
    ).sort_values(ascending=False)
print(segment_sales_pct) 

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
print(subcategory_sales)


top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_products)

top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .tail(10)
)
print(top_products)

top_quantity_products = (
    df.groupby('Product Name')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_quantity_products)

order_sales = df.groupby("Order ID")["Sales"].sum()

average_order_value = order_sales.mean()

print("Average Order Value:", average_order_value)

order_sales = df.groupby("Order ID")["Sales"].sum()

highest_order = order_sales.sort_values(ascending=False).head(1)

print("Highest-Value Order:")
print(highest_order)

lowest_order = order_sales.sort_values(ascending=True).head(1)

print("Lowest-Value Order:")
print(lowest_order)

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)

total_quantity = df["Quantity"].sum()

print("Total Quantity:", total_quantity)

order_quantity = df.groupby('Order ID')["Quantity"].sum()

average_quantity_per_order = order_quantity.mean()

print("Average Quantity per Order:", average_quantity_per_order)

yearly_sales = (
    df.groupby(df["Order Date"].dt.year)["Sales"]
    .sum()
    .sort_index()
)

print(yearly_sales)

yearly_sales_growth = yearly_sales.pct_change() * 100

print(yearly_sales_growth)

monthly_sales = (
    df.groupby(df["Order Date"].dt.month)["Sales"]
    .sum()
)

print(monthly_sales)

year_month_sales = (
    df.groupby([
        df['Order Date'].dt.year,
        df['Order Date'].dt.month
    ])['Sales']
    .sum()
)

best_month_each_year = year_month_sales.groupby(level=0).idxmax()

for year, month in best_month_each_year:
    sales = year_month_sales.loc[(year, month)]
    print(f"{year}: Month {month} - Sales ${sales:,.2f}")

    category_year_sales = (
    df.groupby([
        df['Order Date'].dt.year,
        'Category'
    ])['Sales']
    .sum()
    .unstack()
)

print(category_year_sales)

category_growth = (
    (category_year_sales.loc[2017] - category_year_sales.loc[2014])
    / category_year_sales.loc[2014]
    * 100
).sort_values(ascending=False)

print(category_growth)

category_profit = (
    df.groupby('Category')['Profit']
    .sum()
    .sort_values(ascending=False)
)

print(category_profit)

category_profit_margin = (
    df.groupby('Category')['Profit'].sum()
    / df.groupby('Category')['Sales'].sum()
    * 100
).sort_values(ascending=False)

print(category_profit_margin)

category_discount = (
    df.groupby('Category')['Discount']
    .mean()
    .sort_values(ascending=False)
)

print(category_discount)

region_profit = (
    df.groupby('Region')['Profit']
    .sum()
    .sort_values(ascending=False)
)

print(region_profit)

region_profit_margin = (
    df.groupby('Region')['Profit'].sum()
    / df.groupby('Region')['Sales'].sum()
    * 100
).sort_values(ascending=False)

print(region_profit_margin)

top_profit_products = (
    df.groupby('Product Name')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_profit_products)

bottom_profit_products = (
    df.groupby('Product Name')['Profit']
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print(bottom_profit_products)

product_profit = df.groupby('Product Name')['Profit'].sum()

loss_making_products = (product_profit < 0).sum()

print("Loss-Making Products:", loss_making_products)

total_products = df['Product Name'].nunique()

loss_percentage = (
    loss_making_products / total_products
) * 100

print("Loss-Making Product Percentage:", loss_percentage)

total_profit = df['Profit'].sum()

print("Total Profit:", total_profit)

overall_profit_margin = (
    total_profit / total_sales
) * 100

print("Overall Profit Margin:", overall_profit_margin)

yearly_profit = (
    df.groupby(df['Order Date'].dt.year)['Profit']
    .sum()
    .sort_index()
)

print(yearly_profit)

yearly_profit_growth = yearly_profit.pct_change() * 100

print(yearly_profit_growth)

yearly_profit_margin = (
    yearly_profit / yearly_sales
) * 100

print(yearly_profit_margin)

subcategory_profit = (
    df.groupby('Sub-Category')['Profit']
    .sum()
    .sort_values(ascending=False)
)

print(subcategory_profit)

subcategory_margin = (
    df.groupby('Sub-Category')['Profit'].sum()
    / df.groupby('Sub-Category')['Sales'].sum()
    * 100
).sort_values(ascending=False)

print(subcategory_margin)

subcategory_discount = (
    df.groupby('Sub-Category')['Discount']
    .mean()
    .sort_values(ascending=False)
)

print(subcategory_discount)

top_discount_products = (
    df.groupby('Product Name')['Discount']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(top_discount_products)

discount_profit_corr = df['Discount'].corr(df['Profit'])

print("Discount-Profit Correlation:", discount_profit_corr)

segment_profit = (
    df.groupby('Segment')['Profit']
    .sum()
    .sort_values(ascending=False)
)

print(segment_profit)

segment_profit_margin = (
    df.groupby('Segment')['Profit'].sum()
    / df.groupby('Segment')['Sales'].sum()
    * 100
).sort_values(ascending=False)

print(segment_profit_margin)

ship_profit = (
    df.groupby('Ship Mode')['Profit']
    .sum()
    .sort_values(ascending=False)
)

print(ship_profit)

ship_profit_margin = (
    df.groupby('Ship Mode')['Profit'].sum()
    / df.groupby('Ship Mode')['Sales'].sum()
    * 100
).sort_values(ascending=False)

print(ship_profit_margin)

ship_profit_per_order = (
    df.groupby('Ship Mode')['Profit'].sum()
    / df.groupby('Ship Mode')['Order ID'].nunique()
).sort_values(ascending=False)

print(ship_profit_per_order)

top_profit_customers = (
    df.groupby('Customer Name')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_profit_customers)

bottom_profit_customers = (
    df.groupby('Customer Name')['Profit']
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print(bottom_profit_customers)

customer_profit = df.groupby('Customer Name')['Profit'].sum()

loss_making_customers = (customer_profit < 0).sum()

print("Loss-Making Customers:", loss_making_customers)

customer_loss_percentage = (
    loss_making_customers / df['Customer Name'].nunique()
) * 100

print("Loss-Making Customer Percentage:", customer_loss_percentage)


state_sales = (
    df.groupby('State')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(state_sales)

state_profit = (
    df.groupby('State')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(state_profit)

state_profit_margin = (
    df.groupby('State')['Profit'].sum()
    / df.groupby('State')['Sales'].sum()
    * 100
).sort_values(ascending=False)

print(state_profit_margin)

all_state_profit = df.groupby('State')['Profit'].sum()

loss_making_states = (all_state_profit < 0).sum()

print("Loss-Making States:", loss_making_states)

loss_making_state_percentage = (
    loss_making_states / df['State'].nunique()
) * 100

print("Loss-Making State Percentage:", loss_making_state_percentage)

city_sales = (
    df.groupby('City')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(city_sales)

city_profit = (
    df.groupby('City')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(city_profit)

city_profit_margin = (
    df.groupby('City')['Profit'].sum()
    / df.groupby('City')['Sales'].sum()
    * 100
).sort_values(ascending=False)

print(city_profit_margin.head(10))

high_margin_city_check = pd.DataFrame({
    'Sales': df.groupby('City')['Sales'].sum(),
    'Profit': df.groupby('City')['Profit'].sum(),
    'Orders': df.groupby('City')['Order ID'].nunique()
})

high_margin_city_check['Profit Margin'] = (
    high_margin_city_check['Profit']
    / high_margin_city_check['Sales']
    * 100
)

print(
    high_margin_city_check
    .sort_values('Profit Margin', ascending=False)
    .head(10)
)

city_analysis = pd.DataFrame({
    'Sales': df.groupby('City')['Sales'].sum(),
    'Profit': df.groupby('City')['Profit'].sum(),
    'Orders': df.groupby('City')['Order ID'].nunique()
})

city_analysis['Profit Margin'] = (
    city_analysis['Profit']
    / city_analysis['Sales']
    * 100
)

meaningful_cities = (
    city_analysis[city_analysis['Orders'] >= 10]
    .sort_values('Profit Margin', ascending=False)
)

print(meaningful_cities.head(10))

loss_cities = (
    city_analysis[city_analysis['Orders'] >= 10]
    .sort_values('Profit', ascending=True)
)

print(loss_cities.head(10))

city_loss_analysis = pd.DataFrame({
    'Sales': df.groupby('City')['Sales'].sum(),
    'Profit': df.groupby('City')['Profit'].sum(),
    'Orders': df.groupby('City')['Order ID'].nunique(),
    'Avg Discount': df.groupby('City')['Discount'].mean()
})

city_loss_analysis['Profit Margin'] = (
    city_loss_analysis['Profit']
    / city_loss_analysis['Sales']
    * 100
)

loss_cities_discount = (
    city_loss_analysis[
        (city_loss_analysis['Orders'] >= 10) &
        (city_loss_analysis['Profit'] < 0)
    ]
    .sort_values('Profit')
    .head(10)
)

print(loss_cities_discount)

city_performance = city_analysis[
    city_analysis['Orders'] >= 10
].copy()

city_performance['Sales Rank'] = (
    city_performance['Sales']
    .rank(ascending=False, method='min')
)

city_performance['Profit Margin Rank'] = (
    city_performance['Profit Margin']
    .rank(ascending=False, method='min')
)

print(
    city_performance
    .sort_values(['Sales', 'Profit'], ascending=False)
    .head(10)
)

sales_median = city_performance['Sales'].median()

high_sales_profitable = city_performance[
    (city_performance['Sales'] >= sales_median) &
    (city_performance['Profit'] > 0)
].sort_values('Profit', ascending=False)

print("Median City Sales:", sales_median)
print(high_sales_profitable)

sales_median = city_analysis['Sales'].median()
profit_median = city_analysis['Profit'].median()

city_quadrants = city_analysis.copy()

city_quadrants['Performance'] = np.where(
    (city_quadrants['Sales'] >= sales_median) &
    (city_quadrants['Profit'] >= profit_median),
    'High Sales - High Profit',
    np.where(
        (city_quadrants['Sales'] >= sales_median) &
        (city_quadrants['Profit'] < profit_median),
        'High Sales - Low Profit',
        np.where(
            (city_quadrants['Sales'] < sales_median) &
            (city_quadrants['Profit'] >= profit_median),
            'Low Sales - High Profit',
            'Low Sales - Low Profit'
        )
    )
)

print("Sales Median:", sales_median)
print("Profit Median:", profit_median)

print(
    city_quadrants['Performance']
    .value_counts()
)

high_sales_low_profit = city_quadrants[
    city_quadrants['Performance'] == 'High Sales - Low Profit'
].sort_values('Profit')

print(high_sales_low_profit.head(10))

high_sales_high_profit = city_quadrants[
    city_quadrants['Performance'] == 'High Sales - High Profit'
].sort_values('Profit', ascending=False)

print(high_sales_high_profit.head(10))

low_sales_high_profit = city_quadrants[
    city_quadrants['Performance'] == 'Low Sales - High Profit'
].sort_values('Profit', ascending=False)

print(low_sales_high_profit.head(10))

growth_city_check = city_quadrants[
    city_quadrants['Performance'] == 'Low Sales - High Profit'
].copy()

print(
    growth_city_check[
        ['Sales', 'Profit', 'Orders', 'Profit Margin']
    ]
    .sort_values('Profit', ascending=False)
    .head(10)
)

customer_analysis = pd.DataFrame({
    'Sales': df.groupby('Customer Name')['Sales'].sum(),
    'Profit': df.groupby('Customer Name')['Profit'].sum(),
    'Orders': df.groupby('Customer Name')['Order ID'].nunique()
})

sales_median_customer = customer_analysis['Sales'].median()
profit_median_customer = customer_analysis['Profit'].median()

customer_analysis['Performance'] = np.where(
    (customer_analysis['Sales'] >= sales_median_customer) &
    (customer_analysis['Profit'] >= profit_median_customer),
    'High Sales - High Profit',
    np.where(
        (customer_analysis['Sales'] >= sales_median_customer) &
        (customer_analysis['Profit'] < profit_median_customer),
        'High Sales - Low Profit',
        np.where(
            (customer_analysis['Sales'] < sales_median_customer) &
            (customer_analysis['Profit'] >= profit_median_customer),
            'Low Sales - High Profit',
            'Low Sales - Low Profit'
        )
    )
)

print("Customer Sales Median:", sales_median_customer)
print("Customer Profit Median:", profit_median_customer)

print(customer_analysis['Performance'].value_counts())

top_customer_profit = (
    customer_analysis
    .sort_values('Profit', ascending=False)
    .head(10)
)

print(top_customer_profit)

loss_customer_analysis = (
    customer_analysis[
        customer_analysis['Profit'] < 0
    ]
    .sort_values('Profit')
    .head(10)
)

print(loss_customer_analysis)

loss_customers = df[df['Customer Name'].isin(
    loss_customer_analysis.index
)]

loss_customer_discount = (
    loss_customers
    .groupby('Customer Name')
    .agg(
        Sales=('Sales', 'sum'),
        Profit=('Profit', 'sum'),
        Orders=('Order ID', 'nunique'),
        Avg_Discount=('Discount', 'mean')
    )
    .sort_values('Profit')
)

print(loss_customer_discount)

product_analysis = (
    df.groupby('Product Name')
    .agg(
        Sales=('Sales', 'sum'),
        Profit=('Profit', 'sum'),
        Quantity=('Quantity', 'sum'),
        Orders=('Order ID', 'nunique')
    )
)

product_analysis['Profit Margin'] = (
    product_analysis['Profit'] /
    product_analysis['Sales'] * 100
)

print(
    product_analysis
    .sort_values('Profit', ascending=False)
    .head(10)
)

worst_products = (
    product_analysis[
        product_analysis['Profit'] < 0
    ]
    .sort_values('Profit')
    .head(10)
)

print(worst_products)

loss_product_summary = product_analysis[
    product_analysis['Profit'] < 0
].copy()

print("Loss-Making Products:", len(loss_product_summary))
print("Total Loss from Loss-Making Products:",
      loss_product_summary['Profit'].sum())

print(
    loss_product_summary
    .sort_values('Profit')
    [['Sales', 'Profit', 'Orders', 'Profit Margin']]
    .head(10)
)

loss_product_summary = product_analysis[
    product_analysis['Profit'] < 0
]

total_product_loss = loss_product_summary['Profit'].sum()

print("Loss-Making Products:", len(loss_product_summary))
print("Total Loss from Loss-Making Products:", total_product_loss)
print("Loss as % of Total Profit:",
      abs(total_product_loss) / df['Profit'].sum() * 100)

kpi_summary = {
    'Total Sales': df['Sales'].sum(),
    'Total Profit': df['Profit'].sum(),
    'Total Quantity': df['Quantity'].sum(),
    'Unique Orders': df['Order ID'].nunique(),
    'Unique Customers': df['Customer ID'].nunique(),
    'Unique Products': df['Product ID'].nunique(),
    'Average Order Value': df.groupby('Order ID')['Sales'].sum().mean(),
    'Average Quantity per Order': df.groupby('Order ID')['Quantity'].sum().mean(),
    'Overall Profit Margin (%)': df['Profit'].sum() / df['Sales'].sum() * 100,
    'Loss-Making Products': (product_analysis['Profit'] < 0).sum(),
    'Loss-Making Customers': (customer_analysis['Profit'] < 0).sum()
}

for key, value in kpi_summary.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")





    
# Save final analytical outputs

city_quadrants.to_csv('outputs/output_city_quadrants.csv')
customer_analysis.to_csv('outputs/output_customer_analysis.csv')
product_analysis.to_csv('outputs/output_product_analysis.csv')

print("All analytical outputs saved successfully.")