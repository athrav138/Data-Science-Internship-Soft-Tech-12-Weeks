'''
Task 3: Employee Salaries 
Input Data 
employees = [ 
    ["HR", 25000], 
    ["IT", 45000], 
    ["IT", 55000], 
    ["Sales", 30000], 
    ["Sales", 28000], 
    ["HR", 27000] 
] 
Requirements 
1. Calculate average salary department-wise.  
2. Find highest paid employee.  
3. Compare department salaries using a chart. 
'''
import pandas as pd
import matplotlib.pyplot as plt

employees = [
    ["HR", 25000],
    ["IT", 45000],
    ["IT", 55000],
    ["Sales", 30000],
    ["Sales", 28000],
    ["HR", 27000]
]

df = pd.DataFrame(employees, columns=["Department", "Salary"])

print(df)

# 1. Calculate average salary department-wise.  
avg_salary = df.groupby("Department")["Salary"].mean()
print("The average salary department wiese: ",avg_salary)

# 2. Find highest paid employee.  
high_sal = max(df["Salary"])
print("The highest padi employee: ",df[df["Salary"]==high_sal])

# 3. Compare department salaries using a chart. 
plt.bar(df["Department"],df["Salary"])
plt.xlabel("Department")
plt.ylabel("Salary")
plt.title("Salries Comparision Department Wise")
plt.show()