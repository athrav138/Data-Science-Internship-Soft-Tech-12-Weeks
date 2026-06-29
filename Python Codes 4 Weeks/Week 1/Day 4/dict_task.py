students = {
"Aman": ["Python", "Java"],
 "Riya": ["C", "Python", "Web "],
 "Rahul": ["Java", "Data Science"],
 "Sneha": ["Python", "Data Science"],
 "Ali": ["C", "Java"]
}

print("Dictionary: \n",students)

print("Names of all Students: ", students.keys())

print("Name of Riya course: ",students["Riya"])

students["Shree"]=["Data Anayltics","python","full Stack"]
print("After adding the new Student: ",students)

students["Aman"].append("Web Development")
print("After adding the new course to aman")

students["Ali"].remove("C")
print("After removing the course of C from ali ",students)

if("Data Science" in students["Rahul"]):
  print("yes Rahul is enrolled in data sciece course")
else:
  print("yes Rahul is not  enrolled in data sciece course")

print("The total number  of students: ",len(students))

# STUDENTS THAT HAS COURSE PYTHON
pyth_count=0

for courses in students.values():
  if "Python" in courses:
    pyth_count += 1

print("No. of students enrolled in python is: ",pyth_count)
# to Count the how many students enrolled in each course


pyth_count = 0
java_count = 0
data_sc = 0
webdev = 0
c = 0

for courses in students.values():
  if "Python" in courses:
    pyth_count += 1
  if "Data science" in courses:
    data_sc += 1
  if "C" in courses:
    c += 1
  if "Web" in courses:
    webdev += 1
  if "Java" in courses:
    java_count+= 1


print("C count = ",c)
print("Java count= ",java_count)
print("Python count= ",pyth_count)
print("Data science count= ",data_sc)
print("Web count= ",webdev)
print("Final Diciontary : ",students)

