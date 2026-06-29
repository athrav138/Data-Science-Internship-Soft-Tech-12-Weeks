import numpy as np

salary = np.array([25000,30000,28000,35000,40000,32000])

# print all salary
print("All salary is: ",salary)

# increase every sal by 10%
increase_sal = salary * (10/100)
salary = salary + increase_sal
print("Updated Salary:",salary)

# find emloyee earning morethan 30000
print("Salary More than 30000: ",salary[salary>30000])
print("Salary More than 30000 count : ",len(salary[salary>30000]))

