'''
Task 6: Online Orders 
Input Data 
orders = [ 
    [101,"Mobile",2,15000], 
    [102,"Laptop",1,55000], 
    [103,"Headphones",3,2000], 
    [104,"Tablet",2,18000] 
] 
Requirements 
1. Calculate bill amount for every order.  
2. Find order with highest value.  
3. Calculate total revenue. 
'''

import pandas as pd
import numpy as np

orders = [ 
    [101,"Mobile",2,15000], 
    [102,"Laptop",1,55000], 
    [103,"Headphones",3,2000], 
    [104,"Tablet",2,18000] 
] 

df = pd.DataFrame(orders,columns=["Order_id","Product","Quantity","Price"])
print(df)

# 1. Calculate bill amount for every order.  
df["bill_amount"] = df["Price"] * df["Quantity"]
print("The bill amount for every order is: \n",df["bill_amount"])

# 2. Find order with highest value.  
high_value = df.loc[df["bill_amount"].idxmax()]
print("The highest value is: \n",high_value)

# 3. Calculate total revenue. 
print("The total revenue is:  ",sum(df["bill_amount"]))