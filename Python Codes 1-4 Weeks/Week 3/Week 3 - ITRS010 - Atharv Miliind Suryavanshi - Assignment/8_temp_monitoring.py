'''
Task 8: Temperature Monitoring 
Input Data 
temp = [32,34,35,33,38,40,42,39,37,36] 
Requirements 
1. Average temperature.  
2. Hottest day.  
3. Coldest day.  
4. Visualize temperatures. 
'''

import pandas as pd
import matplotlib.pyplot as plt

temp = [32,34,35,33,38,40,42,39,37,36] 
days = ["Day1","Day2","Day3","Day4","Day5","Day6","Day7","Day8","Day9","Day10"]

df = pd.DataFrame({"Days":days,"Temp":temp})
print(df)

# 1. Average temperature.  
print("The average temperature: ",df["Temp"].mean())

# 2. Hottest day.  
hot  = df.loc[df["Temp"].idxmax()]
print("The hottest day is: ",hot)

# 3. Coldest day.  
cold = df.loc[df["Temp"].idxmin()]
print("The coldest day is: ",cold)

# 4. Visualize temperatures. 
plt.plot(df["Days"],df["Temp"])
plt.xlabel("Days")
plt.ylabel("Temperatures")
plt.title("Temperature Visualization")
plt.show()
