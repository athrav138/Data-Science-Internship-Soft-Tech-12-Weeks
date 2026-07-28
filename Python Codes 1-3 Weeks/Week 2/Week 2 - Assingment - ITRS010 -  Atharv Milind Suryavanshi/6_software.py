'''
6. Software Asset Tracking Dashboard
An IT department maintains records of software installed on employee systems.
Data:
software = {
 "Chrome": 45,
 "VS Code": 32,
 "Python": 28,
 "MySQL": 20,
 "Git": 25
}
Task:
Create a program that:
• Converts the software names and installation counts into a suitable tabular format.
• Displays all software records.
• Find the software with the highest installation count.
• Find the total number of installations.
• Display only software installed on more than 25 systems. 
'''

import pandas as pd

software = {
 "Chrome": 45,
 "VS Code": 32,
 "Python": 28,
 "MySQL": 20,
 "Git": 25
}

print("The software information is: ",software)

# • Converts the software names and installation counts into a suitable tabular format.
df = pd.DataFrame(list(software.items()),columns=["Software", "Installations"])

# • Displays all software records.
print("Data in tabular form: \n",df)

# • Find the software with the highest installation count.
print("Highest installation count: \n",df.loc[df["Installations"].idxmax()])

# • Find the total number of installations.
print("The total  number of installations: ",sum(df["Installations"]))

# • Display only software installed on more than 25 systems. 
print("The software installed on more than 25 systems: ",df[df["Installations"]>25])
