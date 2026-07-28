list1 = [1,2,3,4,5,6,7,3,3]
list2 = [1,2,3.4,"Shreedhar",(1,2,3),3,[2,33]]

print(list1)
print(list2)

print(len(list1))
print(max(list1))
print(min(list1))

print(list1[1:4])
print(list2[:3])
print(list2[3:])

list1.append(100)
print(list1)


print(list1.pop())
list3 = list1.copy()
print(list3)

print(list1.count(3))

list1.insert(2,3)
print(list1)

list1.remove(3)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

list1.clear()