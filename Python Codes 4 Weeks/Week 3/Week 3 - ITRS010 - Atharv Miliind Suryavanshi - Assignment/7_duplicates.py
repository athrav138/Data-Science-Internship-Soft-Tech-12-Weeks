'''
Task 7: Duplicate Records 
Input Data 
students = [ 
    ["Amit",22], 
    ["Sara",21], 
    ["Amit",22], 
    ["John",23], 
    ["Sara",21] 
] 
Requirements 
1. Detect duplicates.  
2. Remove duplicates.  
3. Display final dataset.  
'''

import pandas as pd
import numpy as np

students = [ 
    ["Amit",22], 
    ["Sara",21], 
    ["Amit",22], 
    ["John",23], 
    ["Sara",21] 
] 

df = pd.DataFrame(students,columns=["Name","Age"])
print(df)

# 1. Detect duplicates.  
print("Detecting Duplicates: ",df.duplicated())

# 2. Remove duplicates.  
df = df.drop_duplicates()

# 3. Display final dataset.  
print(df)
