import numpy as np

marks = np.array([
  [80,75,90],
  [65,70,68],
  [92,88,95],
  [78,85,80]
])

# print all marks
print("All marks: ",marks)

# calculate total marks of all student
stu_1 = np.sum(marks[0,:])
print("First student marks total: ",stu_1)

stu_2 = np.sum(marks[1,:])
print("Second student marks total: ",stu_2)

stu_3 = np.sum(marks[2,:])
print("Third student marks total: ",stu_3)

stu_4 = np.sum(marks[3,:])
print("Fourth student marks total: ",stu_4)


# Average of Each student
print("Average of Student 1 :",stu_1/3)
print("Average of Student 2 :",stu_2/3)
print("Average of Student 3 :",stu_3/3)
print("Average of Student 4 :",stu_4/3)

# Find topper

if stu_1 > stu_2 and stu_1 > stu_3 and stu_1 > stu_4:
    print("Student 1 has the Topper :", stu_1)

elif stu_2 > stu_1 and stu_2 > stu_3 and stu_2 > stu_4:
    print("Student 2 has the Topper :", stu_2)

elif stu_3 > stu_1 and stu_3 > stu_2 and stu_3 > stu_4:
    print("Student 3 has the Topper:", stu_3)

else:
    print("Student 4 has the Topper marks:", stu_4)

