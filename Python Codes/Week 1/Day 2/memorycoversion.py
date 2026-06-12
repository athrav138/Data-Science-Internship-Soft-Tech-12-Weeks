import  sys

tb = int(input("Enter memeory in tb: "))

while (1):
  print("1. to gb")
  print("2. to mb")
  print("3. to kb")
  print("4. Exit")
  ch = int(input("Enter choice(1-4): "))

  if ch == 1:
      print(f"{tb}TB = {tb*1024}GB")

  elif ch == 2:
      print(f"{tb}TB = {tb*1024*1024} MB")
      
  elif ch == 3:
      print(f"{tb}TB = {tb*1024*1024*1024} KB")
  
  elif ch==4 :
      sys.exit(0)
  else :
      print(" Invalid Choice")

