import random as rd

print(rd.random())
print(rd.randint(1,10))

list1 = [12,34,5,6,67,45,7,7]
# print(rd.choice(list1))
print(rd.randrange(1,100,2))
print(rd.choices(list1,k=2))