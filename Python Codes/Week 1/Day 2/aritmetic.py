import  sys

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

while (1):
  print("1. Add")
  print("2. sub")
  print("3. div")
  print("4. mul")
  print("5. Exit")
  ch = int(input("Enter choice(1-5): "))

  match ch:
    case 1:
      print(f"Addtion is :{n1+n2}")

    case 2:
      print(f"Subtraction is :{n1-n2}")
    
    case 3:
      print(f"Division is :{n1/n2}")
    
    case 4:
      print(f"Multiplication is :{n1*n2}")

    case 5:
      sys.exit(0)

    case _:
      print(" Invalid Choice")

