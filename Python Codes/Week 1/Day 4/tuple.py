t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = (1,2,"Atharv",4,5.5)

print(t1)
print(t2)

print(len(t1))
print(max(t1))
print(min(t1))

# Changing in the exixsting tuple

l1 = list(t2)
print(l1)
l1.append(10)
l1[3]="Atharv"

t2 = tuple(l1)
print(t2)

# Built in functions of the tuple

print(t1.count(3))
print(t1.index(3))
