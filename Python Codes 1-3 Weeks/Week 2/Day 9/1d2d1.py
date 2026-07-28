import numpy  as np

arr1 = np.arange(1,10).reshape(3,3)

arr2 = np.array([10,20,30])

arr2 = arr2.reshape(3,1)

print(arr1 + arr2)