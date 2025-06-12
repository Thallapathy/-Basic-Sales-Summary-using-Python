# 🧾 Basic Sales Summary – Internship Task 7

## 🎯 Objective
Use SQL inside a Python script to connect to a PostgreSQL database and extract basic sales information — such as **total quantity sold** and **total revenue per product**. The results are printed and visualized using a simple bar chart.

---

## 🛠️ Tools Used
- Python (with `psycopg2`, `pandas`, `matplotlib`)
- PostgreSQL (Database with `sales_data` table)
- `.py` script

---

## 🗃️ Dataset
- **Table:** `sales_data`  
- **Created in PostgreSQL manually**, containing:
  - `product` – Product name
  - `quantity` – Quantity sold
  - `price` – Price per unit

---

## 🧮 Processing & Analysis Steps

1. **Table Creation in PostgreSQL**
   - A table `sales_data` was created manually using SQL.
   - Sample sales data was inserted.

2. **Python Connection**
   - Used `psycopg2` to connect Python to the PostgreSQL database.

3. **SQL Query Executed**
   - Fetched total quantity and total revenue per product:
     ```sql
     SELECT product, 
            SUM(quantity) AS total_qty, 
            SUM(quantity * price) AS revenue 
     FROM sales_data 
     GROUP BY product;
     ```

4. **Loaded Results into Pandas**
   - Converted the SQL result into a Pandas DataFrame for easier analysis.

5. **Displayed Output**
   - Used `print(df)` to show tabular result.
   - Used `matplotlib` to create a simple bar chart of revenue per product.

---

## ✅ Output Example

| product  | total_qty | revenue |
|----------|-----------|---------|
| Coffee   |     100   |  5000.0 |
| Donuts   |      50   |  2500.0 |
| Tea      |      75   |  2250.0 |

---

## 📊 Visualization
- Bar chart of `product` vs `revenue` using `matplotlib.pyplot`.
- Optional: `plt.savefig("sales_chart.png")` to save the chart.

---

## 📂 Files in This Repo
- `sales_summary.py`: Python script for connecting to PostgreSQL, running queries, and plotting chart
- `sales_chart.png`: Bar chart
- `README.md`: This file

---

## 🙋‍♂️ Done by
- **Name:** Shantanu Bhadage  
- **Date:** June 2025
