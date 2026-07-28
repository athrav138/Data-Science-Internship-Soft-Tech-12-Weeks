import pandas as pd

dict = {"Apple":[1,22,3,444],
        "Banana":[3,4,5,5]}

series = pd.Series(dict)
print(series)
print(series.iloc[0])
print(series.loc["Banana"])
