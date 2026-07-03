import numpy as np

arr = [1,2,3,4,5]

np.save("arr.npy",arr)
print(np.load("arr.npy"))