'''
Task 5: Monthly Sales 
Input Data 
months = ["Jan","Feb","Mar","Apr","May","Jun"] 
 
sales = [25000,30000,28000,40000,42000,38000] 
Requirements 
1. Calculate average sales.  
2. Find highest and lowest sales month.  
3. Plot sales trend.  
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"] 
sales = [25000,30000,28000,40000,42000,38000] 

df = pd.DataFrame({"Months":months,"Sales":sales})
print(df)

# 1. Calculate average sales.  
print("The average sales: ",np.mean(df["Sales"]))

# 2. Find highest and lowest sales month.
print("The highest sales:")
print(df.loc[df["Sales"].idxmax()])

print("\nThe lowest sales:")
print(df.loc[df["Sales"].idxmin()])

# 3. Plot sales trend.  
plt.plot(months,sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()