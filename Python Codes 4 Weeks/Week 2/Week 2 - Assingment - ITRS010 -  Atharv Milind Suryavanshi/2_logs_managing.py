'''
2. Monthly Log Archive Manager
A software company stores daily system logs in a text file named logs.txt.
Server Started Successfully

User Login: Aman
Database Backup Completed
User Logout: Aman
Server Shutdown Initiated

Task:
Create a program that:
• Reads the file.
• Displays the total number of lines.
• Displays the total number of words.
• Displays the first log entry.
• Displays the last log entry.
• Handles the situation when the file is missing.
'''

try:

  # • Reads the file.
  logs_file = open("logs.txt","r")
  logs = logs_file.readlines()
  print("\nlogs File record: ",logs)
  print()

  # • Displays the total number of lines.
  print("The number of lines in logs file: ",len(logs),"\n")

  # • Displays the total number of words.
  count_words = 0
  for i in logs:
    for j in i.split():
      count_words += 1
  print("The number of words in logs file: ",count_words,"\n")

  # • Displays the first log entry.
  print("First log entry: ",logs[0],"")

  # • Displays the last log entry.
  print("Last log entry: ",logs[-1],"\n")



  logs_file.close()
except FileNotFoundError as f:
  print("The file Not found :",f)
except Exception as e:
  print(e)




