import numpy as np 

arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = np.array([[12,23,4,45],[43,45,34,5]])
print(arr2)

arr3 = np.arange(0,10,2)
print(arr3)


arr4 = np.zeros(5)
print(arr4)

arr5 = np.zeros([2,2])
print(arr5)

arr6 = np.ones(4)
print(arr6)

arr6[3]=45
print(arr6)


print((arr6.reshape(2,2)))


print(arr2.ravel())




