# Factorial using for 

def fact1(n):
  fact = 1
  for i in range(1,n+1):
    fact *= i

  print("Factorial using for: ",fact)

fact1(5)

def fact2(n):
  fact = 1
  while n >=1:
    fact *= n
    n-=1
  print("factorail using While:",fact)

fact2(6)
    