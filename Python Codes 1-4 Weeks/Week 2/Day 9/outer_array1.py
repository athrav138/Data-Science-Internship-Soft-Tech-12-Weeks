import numpy as np

arr1 = np.array([2,4,6,8])
arr2 = np.arange(1,11)

arr1 = arr1.reshape(4,1)
print(arr1 * arr2)