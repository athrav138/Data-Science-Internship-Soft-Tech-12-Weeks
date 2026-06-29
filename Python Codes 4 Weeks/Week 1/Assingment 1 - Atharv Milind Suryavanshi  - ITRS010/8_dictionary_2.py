courses = {

"Amit": ["Python", "Java"],

"Riya": ["C", "Python"],

"Rahul": ["Java", "Web"]

}

print("Dictionary is: ",courses)

# Add new Course of Amit
courses["Amit"].append("Data Sciecne")
print("\nAfter the Appeding 'Data Science' course to the Amint:\n",courses)

# Remove the 'C' from Riya course list
courses["Riya"].remove("C")
print("\nAfter the removing 'C' course from Riya: \n",courses)

# Display Rahul Courses
print("\nRahul courses: \n",courses["Rahul"])