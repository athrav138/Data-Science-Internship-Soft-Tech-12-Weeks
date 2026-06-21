'''
Task 4: Missing Values Challenge 
Input Data 
data = { 
    "Name": ["A", "B", "C", "D", "E"], 
    "Age": [21, None, 23, None, 25], 
    "Marks": [78, 85, None, 90, 88] 
} 
Requirements 
1. Identify missing values.  
2. Handle them appropriately.  
3. Generate a clean dataset. 
'''

import pandas as pd
import numpy as np

data = { 
    "Name": ["A", "B", "C", "D", "E"], 
    "Age": [21, None, 23, None, 25], 
    "Marks": [78, 85, None, 90, 88] 
} 

df = pd.DataFrame(data)
print(df)

# 1. Identify missing values.  
print("Missing Values: ",df.isnull().sum())

# 2. Handle them appropriately.  
df["Age"] = df["Age"].fillna(np.mean(df["Age"]))
df["Marks"] = df["Marks"].fillna(np.mean(df["Marks"]))

# 3. Generate a clean dataset. 
print(df)