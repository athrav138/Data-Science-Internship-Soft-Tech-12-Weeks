'''
8. Retail Store Sales Analysis
A retail company wants to analyze product sales.
Data:
sales_data = {
 "Product": ["Laptop", "Mobile", "Printer", "Laptop", "Mobile"],
 "Sales": [50000, 30000, 12000, 45000, 28000]
}
Task:
• Create a tabular structure using the given data.
• Calculate total sales.
• Calculate average sales. 
• Find the highest sales value.
• Display all records where sales exceed ₹25,000
'''

import pandas as pd

sales_data = {
 "Product": ["Laptop", "Mobile", "Printer", "Laptop", "Mobile"],
 "Sales": [50000, 30000, 12000, 45000, 28000]
}

# • Create a tabular structure using the given data.
df = pd.DataFrame(sales_data)
print(df)

# • Calculate total sales.
total_sales = sum(df["Sales"])
print("Total sales is: ",total_sales)

# • Calculate average sales. 
print("The average sales: ",total_sales/len(df["Sales"]))

# • Find the highest sales value.
print("The highest sales value: ",max(df["Sales"]))

# • Display all records where sales exceed ₹25,000
print("After exceed sales by ₹25000d: \n",df[df["Sales"]>25000])
