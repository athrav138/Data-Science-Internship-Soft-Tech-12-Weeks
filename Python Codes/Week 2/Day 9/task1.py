import numpy  as np

marks = np.array([78,85,90,67,88,92,75,81,95,70])

# Display all marks
print("All markk:\n",marks)

# Find  highest marks
print("Highest Mark: ",np.max(marks))

# Find Lowest Marks
print("Lowest mark: ",np.min(marks))

# Find Average marks
print("Average mark: ",np.mean(marks))

# Count Studnt score above 80
print("Student Score above 80: ",len(marks[marks>80]))