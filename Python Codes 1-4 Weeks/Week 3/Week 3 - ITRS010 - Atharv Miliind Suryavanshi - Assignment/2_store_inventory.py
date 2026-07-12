'''
Task 2: Store Inventory
Input Data
products = [
 ["Laptop", 25],
 ["Mouse", 150],
 ["Keyboard", 80],
 ["Monitor", 18],
 ["Printer", 5]
]
Requirements
1. Find products with stock less than 20.
2. Find total inventory count.
3. Sort products by stock quantity.
4. Create a suitable chart. 
'''

import pandas as pd
import matplotlib.pyplot as plt

products =  {
 "Laptop": 25,
 "Mouse":150,
 "Keyboard": 80,
 "Monitor":18,
 "Printer": 5
}

df = pd.DataFrame(products.items(),columns=["Product","Stock"])
print(df)

# 1. Find products with stock less than 20.
print("The product with stock less than 20: ",df[df["Stock"]<20])

# 2. Find total inventory count.
print("The total inventory count: ",sum(df["Stock"]))

# 3. Sort products by stock quantity.
sorted_df = df.sort_values(by="Stock")
print("\nProducts after sorting:")
print(sorted_df)

# 4. Create a suitable chart. 

plt.bar(df["Product"],df["Stock"])
plt.xlabel("Product")
plt.ylabel("Stock")
plt.title("Product Stock Analysis")
plt.show()
