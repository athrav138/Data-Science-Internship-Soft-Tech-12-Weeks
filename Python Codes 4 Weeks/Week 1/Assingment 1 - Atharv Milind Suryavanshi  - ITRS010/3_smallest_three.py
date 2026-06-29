def smallest_three1(n1,n2,n3):
  return min(n1,n2,n3)

def smallest_three2(n1,n2,n3):
  if(n1<n2 and n1<n3):
    return n1
  elif(n2<n1 and n2<n3):

    return n2
  else:
    return n3

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


print(f"Smallest among 3 ({a,b,c}) numbers is: ",smallest_three1(a,b,c))
print(f"Smallest among 3 ({a,b,c}) numbers is: ",smallest_three2(a,b,c))

    