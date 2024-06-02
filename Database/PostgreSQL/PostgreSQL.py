import pandas as pd
from sqlalchemy import create_engine, text

# Create PostgreSQL Engine
engine = create_engine('postgresql://postgres:Pg12345*@localhost:5432/SalesDB')

# Test the connection
try:
    conn = engine.connect()
    print("Bağlantı başarılı!")
    conn.close()
except Exception as e:
    print(f"Bağlantı hatası: {e}")

# Read CSV files
customers_df = pd.read_csv('../customers.csv')
products_df = pd.read_csv('../products.csv')
orders_df = pd.read_csv('../orders.csv')
order_items_df = pd.read_csv('../order_items.csv')

# Upload CSV files to PostgreSQL
customers_df.to_sql('Customers', engine, if_exists='replace', index=False)
products_df.to_sql('Products', engine, if_exists='replace', index=False)
orders_df.to_sql('Orders', engine, if_exists='replace', index=False)
order_items_df.to_sql('Order_Items', engine, if_exists='replace', index=False)

print("Veriler başarıyla yüklendi.")
print("="*50)

# 1. Total Sales by Customer
with open('total_sales_by_customer_sql.sql', 'r') as f:
    total_sales_by_customer_query = f.read()
    
# 2. Top 5 Products by Sales
with open('top_products_query.sql', 'r') as f:
    top_products_query = f.read()

# 3. Monthly Sales for a Specific Year
with open('monthly_sales_query.sql', 'r') as f:
    monthly_sales_query = f.read()

# 4. Total Orders by Status
with open('orders_by_status_query.sql', 'r') as f:
    orders_by_status_query = f.read()

# Execute queries and print results
with engine.connect() as connection:
    for query, description in [
        (total_sales_by_customer_query, "Total Sales by Customer:"),
        (top_products_query, "Top 5 Products by Sales:"),
        (monthly_sales_query, "Monthly Sales for 2003:"),
        (orders_by_status_query, "Total Orders by Status:")
    ]:
        result = connection.execute(text(query))
        print(description)
        for row in result:
            print(row)
        print("\n")