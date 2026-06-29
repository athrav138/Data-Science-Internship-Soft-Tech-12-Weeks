'''
Task 9: Exam Performance 
Input Data 
maths = [78,85,92,65,80] 
science = [82,88,90,70,75] 
Requirements 
1. Compare subject performance.  
2. Find correlation between subjects.  
3. Create scatter plot. 
'''

import pandas as pd
import matplotlib.pyplot as plt

maths = [78,85,92,65,80] 
science = [82,88,90,70,75] 
stud = ["Student 1","Student 2","Student 3","Student 4","Student 5"]
df = pd.DataFrame({"Students":stud,"Maths":maths,"Science":science})
print(df)

# 1. Compare subject performance.  
for _, i in df.iterrows():
  if i['Maths']>i['Science']:
    print(f"Student {i['Students']} is maths strong")
  elif i['Maths']<i['Science']:
    print(f"Student {i['Students']} is science strong")
  else:
    print(f"Student {i['Students']} has equal performace in both maths & science")

# 2. Find correlation between subjects.  
corr = df["Maths"].corr(df["Science"])
print("Correlation between Maths and Science:", corr)

#  3. Create scatter plot. 
plt.scatter(df["Maths"],df["Science"])
plt.xlabel("Student")
plt.ylabel("Maths & Scienc")
plt.title("Comparing Marks")
plt.show()
