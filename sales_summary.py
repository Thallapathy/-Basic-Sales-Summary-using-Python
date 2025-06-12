import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",     # or your database host
    database="shantanu",
    user="postgres",
    password="shantanu"
)

# SQL Query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM 
    sales
GROUP BY 
    product;
"""

# Load into pandas
df = pd.read_sql_query(query, conn)

# Display data
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()
