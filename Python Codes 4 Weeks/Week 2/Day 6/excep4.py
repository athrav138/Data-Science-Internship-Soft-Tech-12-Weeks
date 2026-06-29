

try :
  n1 = int(input("Enter a number: "))
  n2 = int(input("Enter a number: "))

  print("Multiplication: ",n1*n2)

#except ValueError as e:
#  print("Invalid Input ! Please enter numeric values only")
except Exception as e:
  print(e)
finally:
  print("all Done")