import numpy as np 

arr1 = np.array([[1,2,3],[4,5,6]])

print(arr1)

print(arr1[1,1])
print(arr1[0,2])

print(arr1[:,0:2])
print(arr1[0:2,0:1])

print(arr1[arr1 != 3])
print(arr1[arr1 > 5])

print(arr1.T)
print((arr1.T).T)
print((arr1.T).T[0,1])