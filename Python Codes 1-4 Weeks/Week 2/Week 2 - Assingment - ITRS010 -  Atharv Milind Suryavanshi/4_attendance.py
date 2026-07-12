'''
4. Employee Attendance Investigation
An HR executive receives attendance records for ten consecutive days.
Data:
attendance = ["P","P","A","P","P","A","P","P","P","A"]
Task:
• Display the first three records.
• Display the last four records.
• Display every alternate record.
• Create a new list containing the attendance records repeated three times.
'''

import numpy as np

attendance = ["P","P","A","P","P","A","P","P","P","A"]
print("The Data of attendance: ",attendance)

# • Display the first three records.
print("The first three records: ",attendance[0:3])

# • Display the last four records.
print("The last four records: ",attendance[len(attendance)-4:len(attendance)])

# • Display every alternate record.
print("The alternate record: ",attendance[::2])

# • Create a new list containing the attendance records repeated three times.
arr = attendance * 3
print("List containing the attendance records repeated three times: ",arr)



