import pandas as pd

series1 = pd.Series([1,2,3,4,5,5])
print(series1)

series2 = pd.Series(["Atharv","Shree",1.4],index=['a','b','c'])
print(series2)


print("Shape: ",series1.shape,series2.shape)
print("Mean: ",series1.mean())
print("Unique: ",series1.unique(),series2.unique())

arr = series1.to_numpy()
print(arr)

series1.astype(float)
print(series1)