def add(a,b):
  return a+b

def addatob(a,b):
  add  = 0
  for i in range(a,b+1):
    add += i

  print(f"Sum of numbers form a={a} to b={b} is: {add}")


a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

print(f" The sum of a={a} and b={b} is : ",add(a,b))

addatob(a,b)