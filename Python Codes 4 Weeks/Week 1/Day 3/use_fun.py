import functions as fun


radius = float (input("Enter radius:"))
fun.circle_area(radius)

p = float(input("Enter principal: "))
n = float(input("Enter no. of Years: "))
r = float(input("Enter rate of interest: "))

fun.simple_interest(p,n,r)

a = int(input("Ente a n1: "))
b = int(input("Ente a n2: "))

fun.max2(a,b)