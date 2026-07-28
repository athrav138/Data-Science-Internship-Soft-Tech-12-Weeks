import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50]).reshape(5,1)
arr3 = np.array([10,20,30,40,50]).T
print(arr1 * arr3)
print(arr1+arr2)
