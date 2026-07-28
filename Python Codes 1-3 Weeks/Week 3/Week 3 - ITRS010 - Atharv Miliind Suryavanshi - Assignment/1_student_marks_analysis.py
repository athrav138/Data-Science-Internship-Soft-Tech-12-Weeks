'''
Task 1: Student Marks Analysis
Input Data
students = [
 ["Amit", 78, 85, 92],
 ["Sara", 65, 72, 68],
 ["John", 90, 88, 95],
 ["Fatima", 45, 52, 48],
 ["Ali", 80, 79, 81]
]
Requirements
1. Calculate total marks.
2. Calculate percentage.
3. Find topper.
4. Find students scoring below 50%.
''' 

import pandas as pd

# Input Data
students = {
 "Amit":[78, 85, 92],
 "Sara":[65, 72, 68],
 "John": [90, 88, 95],
 "Fatima":[ 45, 52, 48],
 "Ali": [80, 79, 81]
}

df = pd.DataFrame(students)
print(df)

# 1. Calculate total marks.
list1 = []
for i in df.keys():
  print(f"Total of {i}: ",sum(df[i]))
  list1.append(sum(df[i]))

# 2. Calculate percentage.
list2 = []
for i in list1:
  list2.append(i/3)

j = 0
for i in df.keys():
  print(f"The percentage of {i}: ",list2[j])
  j += 1

# 3. Find topper.
topper = df.sum().idxmax()
print("The topper is: ",topper)

# 4. Find students scoring below 50%.
print("The Student below 50% scoring: ")
for i in range(len(list2)):
    if list2[i] < 50:
      print(list(students.keys())[i])
      