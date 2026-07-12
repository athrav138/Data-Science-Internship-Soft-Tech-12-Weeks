a  =  int(input("enter num 1: "))
b = int(input("enter num 2:"))

add = a + b

file = open("add.txt","a")
file.write(str(add))
file.close()
