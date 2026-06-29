'''
9. Employee Salary Register
An organization wants to maintain employee salary records.
Data:
names = ["Aman", "Riya", "Ali", "Sneha", "Rahul"]
salaries = [35000, 42000, 38000, 45000, 40000]
Task:
• Create a salary record structure.
• Create a table containing employee names and salaries.
• Display employees earning above ₹40,000.
• Add a new column named Bonus containing 10% of salary.
• Display the updated table. 
'''

import pandas as pd

names = ["Aman", "Riya", "Ali", "Sneha", "Rahul"]
salaries = [35000, 42000, 38000, 45000, 40000]

# • Create a salary record structure.
salary_records = {
  "names" : ["Aman", "Riya", "Ali", "Sneha", "Rahul"],
"salaries" : [35000, 42000, 38000, 45000, 40000]
}
print("The salary records structure: \n",salary_records)

# • Create a table containing employee names and salaries.
df = pd.DataFrame(salary_records)
print(df)

# • Display employees earning above ₹40,000.
print("Display employees earning above ₹40000 is: ",df[df["salaries"]>40000])

# • Add a new column named Bonus containing 10% of salary.
df["bonus"] = df["salaries"] * (10/100)

# • Display the updated table. 
print("The updated table is: \n",df)
