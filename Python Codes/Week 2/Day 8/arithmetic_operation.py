import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([[4,5,6],
                 [7,8,9]])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 / arr2)
print(arr1 * arr2)

print(np.sum(arr1))
print(np.mean(arr1))
print(np.min(arr1))
print(np.max(arr1))


print(np.sum(arr2,axis=0))
print(np.mean(arr2,axis=1))

